# learning/manual_test_harness

- **pyc:** `app\services\learning\__pycache__\manual_test_harness.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/manual_test_harness.py`
- **co_filename (from bytecode):** `app/services/learning/manual_test_harness.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS181 — Bounded manual-test execution harness.

Simulation-only execution of APPROVED_FOR_MANUAL_TEST
learning recommendations (PAS180). The harness:

1. Verifies the recommendation is APPROVED_FOR_MANUAL_TEST.
   CANDIDATE / REJECTED / EXPIRED are NEVER eligible.
2. Creates a PLANNED run in ``pas_learning_manual_test_runs``.
3. Builds a bounded structural evidence packet.
4. Computes deterministic scores (no LLM).
5. Transitions PLANNED → RUNNING, attaching evidence + scores.
6. Awaits an operator confirmation step (``complete``) before
   transitioning RUNNING → COMPLETED. High-risk runs require
   an explicit ``acknowledge_high_risk`` body field.

Doctrine:

* **Simulation-only.** No live PAS state is touched. No
  outbound calls. No booking writes. No Memory Review writes.
  No prompt mutation. No worker enqueue. No LLM calls.
* **NEVER raises.** All failures collapse to structural
  envelopes.
* **Closed transition table:**
    PLANNED   → RUNNING       (harness)
    PLANNED   → CANCELLED     (operator)
    RUNNING   → COMPLETED     (operator confirmation)
    RUNNING   → FAILED        (harness error)
    RUNNING   → CANCELLED     (operator)
* **Append-only audit.** Every successful and failed
  transition writes a PAS174 audit row via
  ``log_operator_action``.
* **Operator-only.** Only OPERATOR / ADMIN actors can call
  the create / complete / cancel helpers.

Public surface:

  * ``ALLOWED_MANUAL_TEST_STATUSES``                    — closed enum.
  * ``ALLOWED_MANUAL_TEST_MODES``                       — closed enum.
  * ``ALLOWED_HARNESS_TRANSITIONS``                     — closed map.
  * ``MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS``      — single literal.
  * ``create_manual_test_plan(...)``                    — PLANNED insert.
  * ``run_manual_test_simulation(...)``                 — PLANNED → RUNNING.
  * ``complete_manual_test_run(...)``                   — RUNNING → COMPLETED.
  * ``cancel_manual_test_run(...)``                     — PLANNED/RUNNING → CANCELLED.
  * ``manual_test_run_report(...)``                     — bounded read.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.learning.manual_test_evidence`, `app.services.learning.manual_test_scoring`, `app.services.operator.audit_service`, `build_manual_test_evidence_packet`, `datetime`, `get_supabase`, `log_operator_action`, `logging`, `score_manual_test_result`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit`, `_bound_brokerage_id`, `_bound_id`, `_clamp_limit`, `_get_db_safe`, `_lookup_recommendation`, `_lookup_test_run`, `_now_iso`, `_project_metadata`, `_project_row`, `_safe_envelope`, `_validate_transition`, `cancel_manual_test_run`, `complete_manual_test_run`, `create_manual_test_plan`, `get_manual_test_run`, `manual_test_run_report`, `run_manual_test_simulation`

## Env-key candidates

`ALLOWED_ACTOR_TYPES`, `ALLOWED_HARNESS_TRANSITIONS`, `ALLOWED_MANUAL_TEST_MODES`, `ALLOWED_MANUAL_TEST_STATUSES`, `ALLOWED_SCENARIO_TYPES`, `ALLOWED_TEST_METADATA_KEYS`, `APPROVED_FOR_MANUAL_TEST`, `CANCELLED`, `COMPLETED`, `FAILED`, `MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS`, `OPERATOR`, `PLANNED`, `RUNNING`, `SIMULATION_ONLY`, `SUCCESS`

## String constants (redacted where noted)

- '\nPAS181 — Bounded manual-test execution harness.\n\nSimulation-only execution of APPROVED_FOR_MANUAL_TEST\nlearning recommendations (PAS180). The harness:\n\n1. Verifies the recommendation is APPROVED_FOR_MANUAL_TEST.\n   CANDIDATE / REJECTED / EXPIRED are NEVER eligible.\n2. Creates a PLANNED run in ``pas_learning_manual_test_runs``.\n3. Builds a bounded structural evidence packet.\n4. Computes deterministic scores (no LLM).\n5. Transitions PLANNED → RUNNING, attaching evidence + scores.\n6. Awaits an operator confirmation step (``complete``) before\n   transitioning RUNNING → COMPLETED. High-risk runs require\n   an explicit ``acknowledge_high_risk`` body field.\n\nDoctrine:\n\n* **Simulation-only.** No live PAS state is touched. No\n  outbound calls. No booking writes. No Memory Review writes.\n  No prompt mutation. No worker enqueue. No LLM calls.\n* **NEVER raises.** All failures collapse to structural\n  envelopes.\n* **Closed transition table:**\n    PLANNED   → RUNNING       (harness)\n    PLANNED   → CANCELLED     (operator)\n    RUNNING   → COMPLETED     (operator confirmation)\n    RUNNING   → FAILED        (harness error)\n    RUNNING   → CANCELLED     (operator)\n* **Append-only audit.** Every successful and failed\n  transition writes a PAS174 audit row via\n  ``log_operator_action``.\n* **Operator-only.** Only OPERATOR / ADMIN actors can call\n  the create / complete / cancel helpers.\n\nPublic surface:\n\n  * ``ALLOWED_MANUAL_TEST_STATUSES``                    — closed enum.\n  * ``ALLOWED_MANUAL_TEST_MODES``                       — closed enum.\n  * ``ALLOWED_HARNESS_TRANSITIONS``                     — closed map.\n  * ``MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS``      — single literal.\n  * ``create_manual_test_plan(...)``                    — PLANNED insert.\n  * ``run_manual_test_simulation(...)``                 — PLANNED → RUNNING.\n  * ``complete_manual_test_run(...)``                   — RUNNING → COMPLETED.\n  * ``cancel_manual_test_run(...)``                     — PLANNED/RUNNING → CANCELLED.\n  * ``manual_test_run_report(...)``                     — bounded read.\n'
- 'pas.learning.manual_test_harness'
- 'pas_learning_manual_test_runs'
- 'pas_learning_recommendations'
- 'PLANNED'
- 'RUNNING'
- 'Tuple[str, ...]'
- 'ALLOWED_MANUAL_TEST_STATUSES'
- 'SIMULATION_ONLY'
- 'ALLOWED_MANUAL_TEST_MODES'
- 'OPERATOR'
- 'ALLOWED_ACTOR_TYPES'
- 'APPROVED_FOR_MANUAL_TEST'
- 'str'
- 'MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS'
- 'Dict[str, Tuple[str, ...]]'
- 'ALLOWED_HARNESS_TRANSITIONS'
- 'ALLOWED_SCENARIO_TYPES'
- 'event'
- 'ALLOWED_TEST_METADATA_KEYS'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'brokerage_id'
- 'status'
- 'mode'
- 'warning_count'
- 'error_code'
- 'actor_type'
- 'actor_id'
- 'test_run'
- 'evidence'
- 'transition'
- 'audit_row'
- 'warnings'
- 'target_status'
- 'audit_status'
- 'SUCCESS'
- 'acknowledge_high_risk'
- 'limit'
- 'return'
- 'seconds'
- 'manual_test_harness db client unavailable type='
- 'value'
- 'Any'
- 'Optional[str]'
- 'max_len'
- 'int'
- 'metadata'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'from_status'
- 'to_status'
- 'Returns None if the transition is permitted; else a\nbounded structural ``error_code``.'
- 'invalid_target_status'
- 'walk_back_to_planned_forbidden'
- 'missing_current_status'
- 'invalid_transition'
- 'action'
- 'record'
- 'Best-effort PAS174 audit-row append. NEVER raises.'
- 'learning_manual_test_run'
- 'test_run_id'
- 'learning.manual_test.event'
- 'manual_test_harness audit error type='
- 'recommendation_id'
- 'Read a single recommendation row. NEVER raises.'
- 'recommendation_id, brokerage_id, recommendation_type, source_type, source_id, status, confidence_score, risk_score, usefulness_score, recommended_action, rationale_token, created_at, reviewed_at'
- 'data'
- '_lookup_recommendation error type='
- '_lookup_test_run error type='
- 'scenario_type'
- 'Validate eligibility + INSERT a PLANNED test run.\nNEVER raises.'
- 'failed'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'invalid_recommendation_id'
- 'invalid_scenario_type'
- 'invalid_mode'
- 'skipped'
- 'learning_manual_test_runs_store_unavailable'
- 'recommendation_not_found'
- 'recommendation_not_eligible'
- 'recommendation_status:'
- 'started_at'
- 'completed_at'
- 'score'
- 'confidence_score'
- 'risk_score'
- 'evidence_fingerprint'
- 'learning.manual_test.planned'
- 'operator_command'
- 'create_manual_test_plan'
- 'recommendation_type'
- 'rationale_token'
- 'create_manual_test_plan insert error type='
- 'db_write_failed:'
- 'plan_manual_test'
- 'from'
- 'Transition PLANNED → RUNNING. Computes deterministic\nevidence packet + scores. NEVER raises. NEVER mutates live\nPAS state.'
- 'invalid_test_run_id'
- 'test_run_not_found'
- 'run_manual_test'
- 'FAILED'
- 'learning.manual_test.failed'
- 'recommendation_no_longer_eligible'
- 'run_manual_test_simulation import error type='
- 'unexpected:'
- 'evidence_build_failed'
- 'scoring_failed'
- 'components'
- 'confidence'
- 'risk'
- 'fingerprint'
- 'learning.manual_test.started'
- 'scenario_fingerprint'
- 'evidence_warning_count'
- 'escalation_required'
- 'run_manual_test_simulation'
- 'run_manual_test_simulation update error type='
- 'policy_refused_or_no_rows'
- 'packet'
- 'bool'
- 'Operator confirmation gate. Transitions RUNNING →\nCOMPLETED. High-risk runs require ``acknowledge_high_risk=True``.\nNEVER raises.'
- 'COMPLETED'
- 'complete_manual_test'
- 'high_risk_acknowledgement_required'
- 'learning.manual_test.completed'
- 'complete_manual_test_run'
- 'ack_high_risk_recorded'
- 'complete_manual_test_run update error type='
- 'Cancel a PLANNED or RUNNING test run. NEVER raises.'
- 'CANCELLED'
- 'cancel_manual_test'
- 'learning.manual_test.cancelled'
- 'cancel_manual_test_run'
- 'cancel_manual_test_run update error type='
- 'Bounded list of test runs. NEVER raises. NEVER returns\nPII.'
- 'rows'
- 'count'
- 'invalid_status'
- 'manual_test_run_report read error type='
- 'db_read_failed:'
- 'Single test run read. Optionally brokerage-scoped for\ntenant route. NEVER raises.'
- 'get_manual_test_run read error type='
- 'test_run_not_found_or_cross_brokerage'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS181 — Bounded manual-test execution harness.\n\nSimulation-only execution of APPROVED_FOR_MANUAL_TEST\nlearning recommendations (PAS180). The harness:\n\n1. Verifies the recommendation is APPROVED_FOR_MANUAL_TEST.\n   CANDIDATE / REJECTED / EXPIRED are NEVER eligible.\n2. Creates a PLANNED run in ``pas_learning_manual_test_runs``.\n3. Builds a bounded structural evidence packet.\n4. Computes deterministic scores (no LLM).\n5. Transitions PLANNED → RUNNING, attaching evidence + scores.\n6. Awaits an operator confirmation step (``complete``) before\n   transitioning RUNNING → COMPLETED. High-risk runs require\n   an explicit ``acknowledge_high_risk`` body field.\n\nDoctrine:\n\n* **Simulation-only.** No live PAS state is touched. No\n  outbound calls. No booking writes. No Memory Review writes.\n  No prompt mutation. No worker enqueue. No LLM calls.\n* **NEVER raises.** All failures collapse to structural\n  envelopes.\n* **Closed transition table:**\n    PLANNED   → RUNNING       (harness)\n    PLANNED   → CANCELLED     (operator)\n    RUNNING   → COMPLETED     (operator confirmation)\n    RUNNING   → FAILED        (harness error)\n    RUNNING   → CANCELLED     (operator)\n* **Append-only audit.** Every successful and failed\n  transition writes a PAS174 audit row via\n  ``log_operator_action``.\n* **Operator-only.** Only OPERATOR / ADMIN actors can call\n  the create / complete / cancel helpers.\n\nPublic surface:\n\n  * ``ALLOWED_MANUAL_TEST_STATUSES``                    — closed enum.\n  * ``ALLOWED_MANUAL_TEST_MODES``                       — closed enum.\n  * ``ALLOWED_HARNESS_TRANSITIONS``                     — closed map.\n  * ``MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS``      — single literal.\n  * ``create_manual_test_plan(...)``                    — PLANNED insert.\n  * ``run_manual_test_simulation(...)``                 — PLANNED → RUNNING.\n  * ``complete_manual_test_run(...)``                   — RUNNING → COMPLETED.\n  * ``cancel_manual_test_run(...)``                     — PLANNED/RUNNING → CANCELLED.\n  * ``manual_test_run_report(...)``                     — bounded read.\n')
               STORE_NAME               1 (__doc__)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (uuid)
               STORE_NAME               5 (uuid)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              6 (datetime)
               IMPORT_FROM              6 (datetime)
               STORE_NAME               6 (datetime)
               IMPORT_FROM              7 (timezone)
               STORE_NAME               7 (timezone)
               POP_TOP

  54           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              8 (typing)
               IMPORT_FROM              9 (Any)
               STORE_NAME               9 (Any)
               IMPORT_FROM             10 (Dict)
               STORE_NAME              10 (Dict)
               IMPORT_FROM             11 (List)
               STORE_NAME              11 (List)
               IMPORT_FROM             12 (Optional)
               STORE_NAME              12 (Optional)
               IMPORT_FROM             13 (Tuple)
               STORE_NAME              13 (Tuple)
               POP_TOP

  57           LOAD_NAME                4 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.learning.manual_test_harness')
               CALL                     1
               STORE_NAME              15 (logger)

  60           LOAD_CONST               6 ('pas_learning_manual_test_runs')
               STORE_NAME              16 (_TABLE)

  61           LOAD_CONST               7 ('pas_learning_recommendations')
               STORE_NAME              17 (_RECOMMENDATIONS_TABLE)

  65           LOAD_CONST              79 (('PLANNED', 'RUNNING', 'COMPLETED', 'FAILED', 'CANCELLED'))
               STORE_NAME              18 (ALLOWED_MANUAL_TEST_STATUSES)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              11 ('ALLOWED_MANUAL_TEST_STATUSES')
               STORE_SUBSCR

  73           LOAD_CONST              80 (('SIMULATION_ONLY', 'OBSERVATIONAL_ONLY'))
               STORE_NAME              20 (ALLOWED_MANUAL_TEST_MODES)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              13 ('ALLOWED_MANUAL_TEST_MODES')
               STORE_SUBSCR

  78           LOAD_CONST              81 (('OPERATOR', 'ADMIN'))
               STORE_NAME              21 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              15 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

  81           LOAD_CONST              16 ('APPROVED_FOR_MANUAL_TEST')
               STORE_NAME              22 (MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS)
               LOAD_CONST              17 ('str')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              18 ('MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS')
               STORE_SUBSCR

  87           LOAD_CONST               8 ('PLANNED')
               LOAD_CONST              82 (('RUNNING', 'CANCELLED'))

  88           LOAD_CONST               9 ('RUNNING')
               LOAD_CONST              83 (('COMPLETED', 'FAILED', 'CANCELLED'))

  86           BUILD_MAP                2
               STORE_NAME              23 (ALLOWED_HARNESS_TRANSITIONS)
               LOAD_CONST              19 ('Dict[str, Tuple[str, ...]]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              20 ('ALLOWED_HARNESS_TRANSITIONS')
               STORE_SUBSCR

  94           LOAD_CONST              84 (('LEAD_RESPONSE', 'OBJECTION_HANDLING', 'CALLBACK_FLOW', 'BOOKING_FLOW', 'DUPLICATE_SUPPRESSION', 'WORKER_FAILURE', 'PROVIDER_FAILURE', 'MEMORY_INJECTION_EFFECT'))
               STORE_NAME              24 (ALLOWED_SCENARIO_TYPES)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              21 ('ALLOWED_SCENARIO_TYPES')
               STORE_SUBSCR

 107           LOAD_CONST              85 (('scenario_fingerprint', 'recommendation_type', 'evidence_warning_count', 'escalation_required', 'ack_high_risk_recorded', 'operator_command', 'rationale_token', 'event'))
               STORE_NAME              25 (ALLOWED_TEST_METADATA_KEYS)
               LOAD_CONST              10 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              23 ('ALLOWED_TEST_METADATA_KEYS')
               STORE_SUBSCR

 120           LOAD_SMALL_INT         200
               STORE_NAME              26 (_BROKERAGE_ID_MAX_LEN)

 121           LOAD_SMALL_INT         200
               STORE_NAME              27 (_ACTOR_ID_MAX_LEN)

 122           LOAD_SMALL_INT         200
               STORE_NAME              28 (_RECOMMENDATION_ID_MAX_LEN)

 123           LOAD_SMALL_INT         200
               STORE_NAME              29 (_TEST_RUN_ID_MAX_LEN)

 124           LOAD_CONST              24 (500)
               STORE_NAME              30 (_LIST_HARD_CAP)

 125           LOAD_SMALL_INT          50
               STORE_NAME              31 (_DEFAULT_LIMIT)

 128           LOAD_CONST              25 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 127           STORE_NAME              32 (_ALLOWED_TOKEN_CHARS)

 135           LOAD_CONST              86 (('test_run_id', 'recommendation_id', 'brokerage_id', 'scenario_type', 'status', 'mode', 'started_at', 'completed_at', 'score', 'confidence_score', 'risk_score', 'evidence_fingerprint', 'warning_count', 'error_code', 'actor_type', 'actor_id', 'metadata'))
               STORE_NAME              33 (_STRUCTURAL_COLUMNS)

 160           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/manual_test_harness.py", line 160>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object _now_iso at 0x0000018C18038DF0, file "app/services/learning/manual_test_harness.py", line 160>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_now_iso)

 164           LOAD_CONST              35 (<code object _get_db_safe at 0x0000018C17FF0C30, file "app/services/learning/manual_test_harness.py", line 164>)
               MAKE_FUNCTION
               STORE_NAME              35 (_get_db_safe)

 176           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/manual_test_harness.py", line 176>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/learning/manual_test_harness.py", line 176>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_bound_brokerage_id)

 185           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025A30, file "app/services/learning/manual_test_harness.py", line 185>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object _bound_id at 0x0000018C17FA92F0, file "app/services/learning/manual_test_harness.py", line 185>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_bound_id)

 197           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/manual_test_harness.py", line 197>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object _clamp_limit at 0x0000018C17972550, file "app/services/learning/manual_test_harness.py", line 197>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_clamp_limit)

 209           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/manual_test_harness.py", line 209>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _project_metadata at 0x0000018C17FED630, file "app/services/learning/manual_test_harness.py", line 209>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_project_metadata)

 224           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/manual_test_harness.py", line 224>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object _project_row at 0x0000018C1804CD30, file "app/services/learning/manual_test_harness.py", line 224>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_project_row)

 235           LOAD_CONST              46 ('test_run')

 238           LOAD_CONST               2 (None)

 235           LOAD_CONST              47 ('evidence')

 239           LOAD_CONST               2 (None)

 235           LOAD_CONST              48 ('transition')

 240           LOAD_CONST               2 (None)

 235           LOAD_CONST              49 ('audit_row')

 241           LOAD_CONST               2 (None)

 235           LOAD_CONST              50 ('warnings')

 242           LOAD_CONST               2 (None)

 235           LOAD_CONST              30 ('error_code')

 243           LOAD_CONST               2 (None)

 235           BUILD_MAP                6
               LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18090360, file "app/services/learning/manual_test_harness.py", line 235>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object _safe_envelope at 0x0000018C18053510, file "app/services/learning/manual_test_harness.py", line 235>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_safe_envelope)

 256           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/manual_test_harness.py", line 256>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object _validate_transition at 0x0000018C17FE17D0, file "app/services/learning/manual_test_harness.py", line 256>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_validate_transition)

 276           LOAD_CONST              55 ('target_status')

 280           LOAD_CONST               2 (None)

 276           LOAD_CONST              31 ('actor_type')

 281           LOAD_CONST              14 ('OPERATOR')

 276           LOAD_CONST              32 ('actor_id')

 282           LOAD_CONST               2 (None)

 276           LOAD_CONST              56 ('audit_status')

 283           LOAD_CONST              57 ('SUCCESS')

 276           LOAD_CONST              30 ('error_code')

 284           LOAD_CONST               2 (None)

 276           LOAD_CONST              22 ('event')

 285           LOAD_CONST               2 (None)

 276           LOAD_CONST              29 ('warning_count')

 286           LOAD_SMALL_INT           0

 276           BUILD_MAP                7
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18090140, file "app/services/learning/manual_test_harness.py", line 276>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _audit at 0x0000018C1801C9E0, file "app/services/learning/manual_test_harness.py", line 276>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_audit)

 313           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025930, file "app/services/learning/manual_test_harness.py", line 313>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _lookup_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/manual_test_harness.py", line 313>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_lookup_recommendation)

 344           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18025B30, file "app/services/learning/manual_test_harness.py", line 344>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _lookup_test_run at 0x0000018C17F78840, file "app/services/learning/manual_test_harness.py", line 344>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_lookup_test_run)

 372           LOAD_CONST              32 ('actor_id')

 377           LOAD_CONST               2 (None)

 372           LOAD_CONST              28 ('mode')

 378           LOAD_CONST              12 ('SIMULATION_ONLY')

 372           BUILD_MAP                2
               LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18025630, file "app/services/learning/manual_test_harness.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object create_manual_test_plan at 0x0000018C17ED1350, file "app/services/learning/manual_test_harness.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              46 (create_manual_test_plan)

 472           LOAD_CONST              31 ('actor_type')

 475           LOAD_CONST              14 ('OPERATOR')

 472           LOAD_CONST              32 ('actor_id')

 476           LOAD_CONST               2 (None)

 472           BUILD_MAP                2
               LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18025230, file "app/services/learning/manual_test_harness.py", line 472>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object run_manual_test_simulation at 0x0000018C17F74AD0, file "app/services/learning/manual_test_harness.py", line 472>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              47 (run_manual_test_simulation)

 756           LOAD_CONST              32 ('actor_id')

 760           LOAD_CONST               2 (None)

 756           LOAD_CONST              68 ('acknowledge_high_risk')

 761           LOAD_CONST              69 (False)

 756           BUILD_MAP                2
               LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/manual_test_harness.py", line 756>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object complete_manual_test_run at 0x0000018C17ED36F0, file "app/services/learning/manual_test_harness.py", line 756>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              48 (complete_manual_test_run)

 900           LOAD_CONST              32 ('actor_id')

 904           LOAD_CONST               2 (None)

 900           BUILD_MAP                1
               LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18025730, file "app/services/learning/manual_test_harness.py", line 900>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object cancel_manual_test_run at 0x0000018C17F80CC0, file "app/services/learning/manual_test_harness.py", line 900>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              49 (cancel_manual_test_run)

1020           LOAD_CONST              26 ('brokerage_id')

1022           LOAD_CONST               2 (None)

1020           LOAD_CONST              27 ('status')

1023           LOAD_CONST               2 (None)

1020           LOAD_CONST              74 ('limit')

1024           LOAD_NAME               31 (_DEFAULT_LIMIT)

1020           BUILD_MAP                3
               LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18025030, file "app/services/learning/manual_test_harness.py", line 1020>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object manual_test_run_report at 0x0000018C17F81320, file "app/services/learning/manual_test_harness.py", line 1020>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              50 (manual_test_run_report)

1085           LOAD_CONST              26 ('brokerage_id')

1088           LOAD_CONST               2 (None)

1085           BUILD_MAP                1
               LOAD_CONST              77 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/learning/manual_test_harness.py", line 1085>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object get_manual_test_run at 0x0000018C17F81A80, file "app/services/learning/manual_test_harness.py", line 1085>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              51 (get_manual_test_run)

1145           BUILD_LIST               0
               LOAD_CONST              87 (('ALLOWED_MANUAL_TEST_STATUSES', 'ALLOWED_MANUAL_TEST_MODES', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_HARNESS_TRANSITIONS', 'ALLOWED_TEST_METADATA_KEYS', 'ALLOWED_SCENARIO_TYPES', 'MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS', 'create_manual_test_plan', 'run_manual_test_simulation', 'complete_manual_test_run', 'cancel_manual_test_run', 'manual_test_run_report', 'get_manual_test_run'))
               LIST_EXTEND              1
               STORE_NAME              52 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/manual_test_harness.py", line 160>:
160           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038DF0, file "app/services/learning/manual_test_harness.py", line 160>:
160           RESUME                   0

161           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF0C30, file "app/services/learning/manual_test_harness.py", line 164>:
 164           RESUME                   0

 165           NOP

 166   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 167           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 168           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 169   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 170           LOAD_CONST               2 ('manual_test_harness db client unavailable type=')

 171           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 170           BUILD_STRING             2

 169           CALL                     1
               POP_TOP

 173   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 168   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/learning/manual_test_harness.py", line 176>:
176           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95E60, file "app/services/learning/manual_test_harness.py", line 176>:
176           RESUME                   0

177           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

178           LOAD_CONST               0 (None)
              RETURN_VALUE

179   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

180           LOAD_FAST_BORROW         1 (s)
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

181   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

182   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/services/learning/manual_test_harness.py", line 185>:
185           RESUME                   0
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

Disassembly of <code object _bound_id at 0x0000018C17FA92F0, file "app/services/learning/manual_test_harness.py", line 185>:
185           RESUME                   0

186           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

187           LOAD_CONST               0 (None)
              RETURN_VALUE

188   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

189           LOAD_FAST_BORROW         2 (s)
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

190   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

191   L3:     LOAD_FAST_BORROW         2 (s)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               3 (ch)

192           LOAD_FAST_BORROW         3 (ch)
              LOAD_GLOBAL              8 (_ALLOWED_TOKEN_CHARS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

193   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

191   L6:     END_FOR
              POP_ITER

194           LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app/services/learning/manual_test_harness.py", line 197>:
197           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C17972550, file "app/services/learning/manual_test_harness.py", line 197>:
 197           RESUME                   0

 198           NOP

 199   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 202   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 203           LOAD_SMALL_INT           1
               RETURN_VALUE

 204   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 205           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 206   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 200           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 201           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 200   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/learning/manual_test_harness.py", line 209>:
209           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metadata')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_metadata at 0x0000018C17FED630, file "app/services/learning/manual_test_harness.py", line 209>:
209           RESUME                   0

210           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

211           BUILD_MAP                0
              RETURN_VALUE

212   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

213           LOAD_GLOBAL              4 (ALLOWED_TEST_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               108 (to L8)
              STORE_FAST               2 (k)

214           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

215           JUMP_BACKWARD           11 (to L2)

216   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

217           LOAD_FAST_BORROW         3 (v)
              POP_JUMP_IF_NONE        34 (to L4)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL              6 (bool)
              LOAD_GLOBAL              8 (int)
              LOAD_GLOBAL             10 (float)
              BUILD_TUPLE              3
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

218   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

219   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (v)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           86 (to L2)
      L6:     LOAD_GLOBAL             15 (len + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          104 (to L2)

220   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          110 (to L2)

213   L8:     END_FOR
              POP_ITER

221           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/learning/manual_test_harness.py", line 224>:
224           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1804CD30, file "app/services/learning/manual_test_harness.py", line 224>:
224           RESUME                   0

225           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

226           LOAD_CONST               0 (None)
              RETURN_VALUE

227   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

228           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

229           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

230   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

228   L4:     END_FOR
              POP_ITER

231           LOAD_GLOBAL              7 (_project_metadata + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('metadata')
              STORE_SUBSCR

232           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090360, file "app/services/learning/manual_test_harness.py", line 235>:
235           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

237           LOAD_CONST               2 ('str')

235           LOAD_CONST               3 ('test_run')

238           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

235           LOAD_CONST               5 ('evidence')

239           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

235           LOAD_CONST               6 ('transition')

240           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

235           LOAD_CONST               7 ('audit_row')

241           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

235           LOAD_CONST               8 ('warnings')

242           LOAD_CONST               9 ('Optional[List[str]]')

235           LOAD_CONST              10 ('error_code')

243           LOAD_CONST              11 ('Optional[str]')

235           LOAD_CONST              12 ('return')

244           LOAD_CONST              13 ('Dict[str, Any]')

235           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18053510, file "app/services/learning/manual_test_harness.py", line 235>:
235           RESUME                   0

246           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

247           LOAD_CONST               1 ('test_run')
              LOAD_FAST                1 (test_run)

248           LOAD_CONST               2 ('evidence')
              LOAD_FAST                2 (evidence)

249           LOAD_CONST               3 ('transition')
              LOAD_FAST                3 (transition)

250           LOAD_CONST               4 ('audit_row')
              LOAD_FAST                4 (audit_row)

251           LOAD_CONST               5 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                5 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

252           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

245           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/manual_test_harness.py", line 256>:
256           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('from_status')

258           LOAD_CONST               2 ('Optional[str]')

256           LOAD_CONST               3 ('to_status')

259           LOAD_CONST               4 ('str')

256           LOAD_CONST               5 ('return')

260           LOAD_CONST               2 ('Optional[str]')

256           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _validate_transition at 0x0000018C17FE17D0, file "app/services/learning/manual_test_harness.py", line 256>:
256           RESUME                   0

263           LOAD_FAST_BORROW         1 (to_status)
              LOAD_GLOBAL              0 (ALLOWED_MANUAL_TEST_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

264           LOAD_CONST               1 ('invalid_target_status')
              RETURN_VALUE

265   L1:     LOAD_FAST_BORROW         1 (to_status)
              LOAD_CONST               6 (('PLANNED',))
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

266           LOAD_CONST               2 ('walk_back_to_planned_forbidden')
              RETURN_VALUE

267   L2:     LOAD_FAST_BORROW         0 (from_status)
              POP_JUMP_IF_NOT_NONE     3 (to L3)
              NOT_TAKEN

268           LOAD_CONST               4 ('missing_current_status')
              RETURN_VALUE

269   L3:     LOAD_FAST_BORROW         0 (from_status)
              LOAD_GLOBAL              2 (ALLOWED_HARNESS_TRANSITIONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

270           LOAD_CONST               5 ('invalid_transition')
              RETURN_VALUE

271   L4:     LOAD_FAST_BORROW         1 (to_status)
              LOAD_GLOBAL              2 (ALLOWED_HARNESS_TRANSITIONS)
              LOAD_FAST_BORROW         0 (from_status)
              BINARY_OP               26 ([])
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

272           LOAD_CONST               5 ('invalid_transition')
              RETURN_VALUE

273   L5:     LOAD_CONST               3 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090140, file "app/services/learning/manual_test_harness.py", line 276>:
276           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('action')

278           LOAD_CONST               2 ('str')

276           LOAD_CONST               3 ('record')

279           LOAD_CONST               4 ('Dict[str, Any]')

276           LOAD_CONST               5 ('target_status')

280           LOAD_CONST               6 ('Optional[str]')

276           LOAD_CONST               7 ('actor_type')

281           LOAD_CONST               2 ('str')

276           LOAD_CONST               8 ('actor_id')

282           LOAD_CONST               6 ('Optional[str]')

276           LOAD_CONST               9 ('audit_status')

283           LOAD_CONST               2 ('str')

276           LOAD_CONST              10 ('error_code')

284           LOAD_CONST               6 ('Optional[str]')

276           LOAD_CONST              11 ('event')

285           LOAD_CONST               6 ('Optional[str]')

276           LOAD_CONST              12 ('warning_count')

286           LOAD_CONST              13 ('int')

276           LOAD_CONST              14 ('return')

287           LOAD_CONST              15 ('Optional[Dict[str, Any]]')

276           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _audit at 0x0000018C1801C9E0, file "app/services/learning/manual_test_harness.py", line 276>:
 276            RESUME                   0

 289            NOP

 290    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('log_operator_action',))
                IMPORT_NAME              0 (app.services.operator.audit_service)
                IMPORT_FROM              1 (log_operator_action)
                STORE_FAST               9 (log_operator_action)
                POP_TOP

 291            LOAD_FAST                9 (log_operator_action)
                PUSH_NULL

 292            LOAD_FAST_BORROW         1 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                CALL                     1

 293            LOAD_FAST                3 (actor_type)

 294            LOAD_FAST                4 (actor_id)

 295            LOAD_FAST                0 (action)

 296            LOAD_FAST                5 (audit_status)

 297            LOAD_CONST               3 ('learning_manual_test_run')

 298            LOAD_FAST_BORROW         1 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               4 ('test_run_id')
                CALL                     1

 299            LOAD_FAST                8 (warning_count)

 301            LOAD_CONST               5 ('event')
                LOAD_FAST                7 (event)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               6 ('learning.manual_test.event')

 302    L4:     LOAD_CONST               7 ('target_status')
                LOAD_FAST_BORROW         2 (target_status)

 303            LOAD_CONST               8 ('error_code')
                LOAD_FAST_BORROW         6 (error_code)

 300            BUILD_MAP                3

 291            LOAD_CONST               9 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
                CALL_KW                  9
        L5:     RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 306            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L10)
                NOT_TAKEN
                STORE_FAST              10 (e)

 307    L7:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 308            LOAD_CONST              10 ('manual_test_harness audit error type=')
                LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 307            CALL                     1
                POP_TOP

 310    L8:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                LOAD_CONST              11 (None)
                RETURN_VALUE

  --    L9:     LOAD_CONST              11 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 306   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L5 -> L6 [0]
  L6 to L7 -> L11 [1] lasti
  L7 to L8 -> L9 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/learning/manual_test_harness.py", line 313>:
313           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')

314           LOAD_CONST               2 ('Any')

313           LOAD_CONST               3 ('recommendation_id')

316           LOAD_CONST               4 ('str')

313           LOAD_CONST               5 ('return')

317           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

313           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _lookup_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/manual_test_harness.py", line 313>:
 313            RESUME                   0

 319            NOP

 321    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_RECOMMENDATIONS_TABLE)
                CALL                     1

 322            LOAD_ATTR                5 (select + NULL|self)

 323            LOAD_CONST               1 ('recommendation_id, brokerage_id, recommendation_type, source_type, source_id, status, confidence_score, risk_score, usefulness_score, recommended_action, rationale_token, created_at, reviewed_at')

 322            CALL                     1

 328            LOAD_ATTR                7 (eq + NULL|self)
                LOAD_CONST               2 ('recommendation_id')
                LOAD_FAST_BORROW         1 (recommendation_id)
                CALL                     2

 329            LOAD_ATTR                9 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 330            LOAD_ATTR               11 (execute + NULL|self)
                CALL                     0

 320            STORE_FAST               2 (result)

 332            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         2 (result)
                LOAD_CONST               3 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               3 (rows)

 333            LOAD_FAST_BORROW         3 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L5:     NOT_TAKEN

 334            LOAD_CONST               4 (None)
                RETURN_VALUE

 335    L6:     LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               4 (row)

 336            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (row)
                LOAD_GLOBAL             18 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (row)
        L7:     RETURN_VALUE
        L8:     LOAD_CONST               4 (None)
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 337            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                STORE_FAST               5 (e)

 338   L11:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 339            LOAD_CONST               5 ('_lookup_recommendation error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 338            CALL                     1
                POP_TOP

 341   L12:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 337   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L3 to L5 -> L10 [0]
  L6 to L7 -> L10 [0]
  L8 to L9 -> L10 [0]
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app/services/learning/manual_test_harness.py", line 344>:
344           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')

345           LOAD_CONST               2 ('Any')

344           LOAD_CONST               3 ('test_run_id')

347           LOAD_CONST               4 ('str')

344           LOAD_CONST               5 ('return')

348           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

344           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _lookup_test_run at 0x0000018C17F78840, file "app/services/learning/manual_test_harness.py", line 344>:
 344            RESUME                   0

 349            NOP

 351    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_GLOBAL              2 (_TABLE)
                CALL                     1

 352            LOAD_ATTR                5 (select + NULL|self)
                LOAD_CONST               0 (',')
                LOAD_ATTR                7 (join + NULL|self)
                LOAD_GLOBAL              8 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 353            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST               1 ('test_run_id')
                LOAD_FAST_BORROW         1 (test_run_id)
                CALL                     2

 354            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 355            LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0

 350            STORE_FAST               2 (result)

 357            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         2 (result)
                LOAD_CONST               2 ('data')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                BUILD_LIST               0
        L4:     CALL                     1
                STORE_FAST               3 (rows)

 358            LOAD_FAST_BORROW         3 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L5:     NOT_TAKEN

 359            LOAD_CONST               3 (None)
                RETURN_VALUE

 360    L6:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             22 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
        L7:     RETURN_VALUE
        L8:     LOAD_CONST               3 (None)
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 361            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                STORE_FAST               4 (e)

 362   L11:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 363            LOAD_CONST               4 ('_lookup_test_run error type=')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 362            CALL                     1
                POP_TOP

 365   L12:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 361   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L3 to L5 -> L10 [0]
  L6 to L7 -> L10 [0]
  L8 to L9 -> L10 [0]
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app/services/learning/manual_test_harness.py", line 372>:
372           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('recommendation_id')

374           LOAD_CONST               2 ('str')

372           LOAD_CONST               3 ('scenario_type')

375           LOAD_CONST               2 ('str')

372           LOAD_CONST               4 ('actor_type')

376           LOAD_CONST               2 ('str')

372           LOAD_CONST               5 ('actor_id')

377           LOAD_CONST               6 ('Optional[str]')

372           LOAD_CONST               7 ('mode')

378           LOAD_CONST               2 ('str')

372           LOAD_CONST               8 ('return')

379           LOAD_CONST               9 ('Dict[str, Any]')

372           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object create_manual_test_plan at 0x0000018C17ED1350, file "app/services/learning/manual_test_harness.py", line 372>:
 372            RESUME                   0

 382            LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 383            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 384    L1:     LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL              6 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               5 (actor)

 385            LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 386            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 387    L4:     LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (recommendation_id)
                LOAD_GLOBAL              8 (_RECOMMENDATION_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               6 (rid)

 388            LOAD_FAST_BORROW         6 (rid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 389            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_recommendation_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 390    L5:     LOAD_FAST_BORROW         1 (scenario_type)
                LOAD_GLOBAL             10 (ALLOWED_SCENARIO_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 391            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               7 ('invalid_scenario_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 392    L6:     LOAD_FAST_BORROW         4 (mode)
                LOAD_GLOBAL             12 (ALLOWED_MANUAL_TEST_MODES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L7)
                NOT_TAKEN

 393            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               8 ('invalid_mode')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 395    L7:     LOAD_GLOBAL             15 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 396            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L8)
                NOT_TAKEN

 397            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 398            LOAD_CONST               9 ('skipped')

 399            LOAD_CONST              10 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

 400            LOAD_CONST              10 ('learning_manual_test_runs_store_unavailable')

 397            LOAD_CONST              11 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 403    L8:     LOAD_GLOBAL             17 (_lookup_recommendation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (db, rid)
                LOAD_CONST              12 (('recommendation_id',))
                CALL_KW                  2
                STORE_FAST               8 (rec)

 404            LOAD_FAST_BORROW         8 (rec)
                POP_JUMP_IF_NOT_NONE    14 (to L9)
                NOT_TAKEN

 405            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 406            LOAD_CONST               1 ('failed')

 407            LOAD_CONST              13 ('recommendation_not_found')

 405            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 409    L9:     LOAD_FAST_BORROW         8 (rec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              14 ('status')
                CALL                     1
                STORE_FAST               9 (rec_status)

 410            LOAD_FAST_BORROW         9 (rec_status)
                LOAD_GLOBAL             20 (MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       19 (to L10)
                NOT_TAKEN

 411            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 412            LOAD_CONST               1 ('failed')

 413            LOAD_CONST              15 ('recommendation_not_eligible')

 414            LOAD_CONST              16 ('recommendation_status:')
                LOAD_FAST_BORROW         9 (rec_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 411            LOAD_CONST              17 (('status', 'error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 417   L10:     BUILD_MAP                0

 418            LOAD_CONST              18 ('test_run_id')
                LOAD_GLOBAL             23 (str + NULL)
                LOAD_GLOBAL             24 (uuid)
                LOAD_ATTR               26 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 417            MAP_ADD                  1

 419            LOAD_CONST              19 ('recommendation_id')
                LOAD_FAST_BORROW         6 (rid)

 417            MAP_ADD                  1

 420            LOAD_CONST              20 ('brokerage_id')
                LOAD_FAST_BORROW         8 (rec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              20 ('brokerage_id')
                CALL                     1

 417            MAP_ADD                  1

 421            LOAD_CONST              21 ('scenario_type')
                LOAD_FAST_BORROW         1 (scenario_type)

 417            MAP_ADD                  1

 422            LOAD_CONST              14 ('status')
                LOAD_CONST              22 ('PLANNED')

 417            MAP_ADD                  1

 423            LOAD_CONST              23 ('mode')
                LOAD_FAST_BORROW         4 (mode)

 417            MAP_ADD                  1

 424            LOAD_CONST              24 ('started_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 417            MAP_ADD                  1

 425            LOAD_CONST              25 ('completed_at')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 426            LOAD_CONST              26 ('score')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 427            LOAD_CONST              27 ('confidence_score')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 428            LOAD_CONST              28 ('risk_score')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 429            LOAD_CONST              29 ('evidence_fingerprint')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 430            LOAD_CONST              30 ('warning_count')
                LOAD_SMALL_INT           0

 417            MAP_ADD                  1

 431            LOAD_CONST              31 ('error_code')
                LOAD_CONST               4 (None)

 417            MAP_ADD                  1

 432            LOAD_CONST              32 ('actor_type')
                LOAD_FAST_BORROW         2 (actor_type)

 417            MAP_ADD                  1

 433            LOAD_CONST              33 ('actor_id')
                LOAD_FAST_BORROW         5 (actor)

 417            MAP_ADD                  1

 434            LOAD_CONST              34 ('metadata')
                LOAD_GLOBAL             31 (_project_metadata + NULL)

 435            LOAD_CONST              35 ('event')
                LOAD_CONST              36 ('learning.manual_test.planned')

 436            LOAD_CONST              37 ('operator_command')
                LOAD_CONST              38 ('create_manual_test_plan')

 437            LOAD_CONST              39 ('recommendation_type')
                LOAD_FAST_BORROW         8 (rec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              39 ('recommendation_type')
                CALL                     1

 438            LOAD_CONST              40 ('rationale_token')
                LOAD_FAST_BORROW         8 (rec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              40 ('rationale_token')
                CALL                     1

 434            BUILD_MAP                4
                CALL                     1

 417            MAP_ADD                  1
                STORE_FAST              10 (row)

 442            NOP

 443   L11:     LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1
                LOAD_ATTR               37 (insert + NULL|self)
                LOAD_FAST_BORROW        10 (row)
                CALL                     1
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                STORE_FAST              11 (result)

 444            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW        11 (result)
                LOAD_CONST              41 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L12:     CALL                     1
                STORE_FAST              12 (rows_after)

 455   L13:     LOAD_FAST               12 (rows_after)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L14)
                NOT_TAKEN
                LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               12 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L15)
       L14:     LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               10 (row)
                CALL                     1
       L15:     STORE_FAST              14 (inserted)

 456            LOAD_GLOBAL             57 (_audit + NULL)

 457            LOAD_CONST              44 ('plan_manual_test')

 458            LOAD_FAST               14 (inserted)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               10 (row)

 459   L16:     LOAD_CONST              22 ('PLANNED')

 460            LOAD_FAST                2 (actor_type)

 461            LOAD_FAST                5 (actor)

 462            LOAD_CONST              36 ('learning.manual_test.planned')

 456            LOAD_CONST              45 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST              15 (audit_env)

 464            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 465            LOAD_CONST              46 ('ok')

 466            LOAD_FAST               14 (inserted)

 467            LOAD_CONST              47 ('from')
                LOAD_CONST               4 (None)
                LOAD_CONST              48 ('to')
                LOAD_CONST              22 ('PLANNED')
                LOAD_CONST              46 ('ok')
                LOAD_CONST              49 (True)
                BUILD_MAP                3

 468            LOAD_FAST               15 (audit_env)

 464            LOAD_CONST              50 (('status', 'test_run', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 445            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L22)
                NOT_TAKEN
                STORE_FAST              13 (e)

 446   L18:     LOAD_GLOBAL             46 (logger)
                LOAD_ATTR               49 (warning + NULL|self)

 447            LOAD_CONST              42 ('create_manual_test_plan insert error type=')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 446            CALL                     1
                POP_TOP

 449            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 450            LOAD_CONST               9 ('skipped')

 451            LOAD_CONST              43 ('db_write_failed:')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 452            LOAD_CONST              10 ('learning_manual_test_runs_store_unavailable')

 449            LOAD_CONST              11 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 445   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L13 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/learning/manual_test_harness.py", line 472>:
472           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

474           LOAD_CONST               2 ('str')

472           LOAD_CONST               3 ('actor_type')

475           LOAD_CONST               2 ('str')

472           LOAD_CONST               4 ('actor_id')

476           LOAD_CONST               5 ('Optional[str]')

472           LOAD_CONST               6 ('return')

477           LOAD_CONST               7 ('Dict[str, Any]')

472           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object run_manual_test_simulation at 0x0000018C17F74AD0, file "app/services/learning/manual_test_harness.py", line 472>:
 472            RESUME                   0

 481            LOAD_FAST_BORROW         1 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 482            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 483    L1:     LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                LOAD_GLOBAL              6 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               3 (actor)

 484            LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 485            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 486    L4:     LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                LOAD_GLOBAL              8 (_TEST_RUN_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               4 (trid)

 487            LOAD_FAST_BORROW         4 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 488            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_test_run_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 490    L5:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 491            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 492            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 493            LOAD_CONST               7 ('skipped')

 494            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

 495            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 492            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 498    L6:     LOAD_GLOBAL             13 (_lookup_test_run + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (db, trid)
                LOAD_CONST              10 (('test_run_id',))
                CALL_KW                  2
                STORE_FAST               6 (current)

 499            LOAD_FAST_BORROW         6 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 500            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 501            LOAD_CONST               1 ('failed')

 502            LOAD_CONST              11 ('test_run_not_found')

 500            LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 504    L7:     LOAD_GLOBAL             15 (_validate_transition + NULL)

 505            LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1

 506            LOAD_CONST              13 ('RUNNING')

 504            LOAD_CONST              14 (('from_status', 'to_status'))
                CALL_KW                  2
                STORE_FAST               7 (err)

 508            LOAD_FAST_BORROW         7 (err)
                POP_JUMP_IF_NONE        67 (to L8)
                NOT_TAKEN

 509            LOAD_GLOBAL             19 (_audit + NULL)

 510            LOAD_CONST              15 ('run_manual_test')

 511            LOAD_FAST_BORROW         6 (current)

 512            LOAD_CONST              13 ('RUNNING')

 513            LOAD_FAST_BORROW         1 (actor_type)

 514            LOAD_FAST_BORROW         3 (actor)

 515            LOAD_CONST              16 ('FAILED')

 516            LOAD_FAST_BORROW         7 (err)

 517            LOAD_CONST              17 ('learning.manual_test.failed')

 518            LOAD_SMALL_INT           1

 509            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 520            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 521            LOAD_CONST               1 ('failed')

 522            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 523            LOAD_FAST_BORROW         8 (audit_env)

 524            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('RUNNING')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 525            LOAD_FAST_BORROW         7 (err)

 520            LOAD_CONST              23 (('status', 'test_run', 'audit_row', 'transition', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 528    L8:     LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              24 ('recommendation_id')
                CALL                     1
                STORE_FAST               9 (rid)

 529            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (rid)
                LOAD_GLOBAL             24 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL             27 (_lookup_recommendation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 89 (db, rid)
                LOAD_CONST              25 (('recommendation_id',))
                CALL_KW                  2
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST               4 (None)
       L10:     STORE_FAST              10 (rec)

 530            LOAD_FAST_BORROW        10 (rec)
                POP_JUMP_IF_NOT_NONE   150 (to L13)
                NOT_TAKEN

 534            LOAD_CONST              12 ('status')
                LOAD_CONST              16 ('FAILED')

 535            LOAD_CONST              26 ('completed_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 536            LOAD_CONST              27 ('error_code')
                LOAD_CONST              28 ('recommendation_not_found')

 533            BUILD_MAP                3
                STORE_FAST              11 (patch)

 538            NOP

 539   L11:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1
                LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST_BORROW        11 (patch)
                CALL                     1
                LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST_BORROW         4 (trid)
                CALL                     2
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                POP_TOP

 542   L12:     LOAD_GLOBAL             19 (_audit + NULL)

 543            LOAD_CONST              15 ('run_manual_test')

 544            LOAD_FAST_BORROW         6 (current)

 545            LOAD_CONST              16 ('FAILED')

 546            LOAD_FAST_BORROW         1 (actor_type)

 547            LOAD_FAST_BORROW         3 (actor)

 548            LOAD_CONST              16 ('FAILED')

 549            LOAD_CONST              28 ('recommendation_not_found')

 550            LOAD_CONST              17 ('learning.manual_test.failed')

 551            LOAD_SMALL_INT           1

 542            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 553            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 554            LOAD_CONST               1 ('failed')

 555            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 556            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              16 ('FAILED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 557            LOAD_FAST_BORROW         8 (audit_env)

 558            LOAD_CONST              28 ('recommendation_not_found')

 553            LOAD_CONST              30 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 560   L13:     LOAD_FAST_BORROW        10 (rec)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_GLOBAL             42 (MANUAL_TEST_ELIGIBLE_RECOMMENDATION_STATUS)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      150 (to L16)
                NOT_TAKEN

 563            LOAD_CONST              12 ('status')
                LOAD_CONST              16 ('FAILED')

 564            LOAD_CONST              26 ('completed_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 565            LOAD_CONST              27 ('error_code')
                LOAD_CONST              31 ('recommendation_no_longer_eligible')

 562            BUILD_MAP                3
                STORE_FAST              11 (patch)

 567            NOP

 568   L14:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1
                LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST_BORROW        11 (patch)
                CALL                     1
                LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST_BORROW         4 (trid)
                CALL                     2
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                POP_TOP

 571   L15:     LOAD_GLOBAL             19 (_audit + NULL)

 572            LOAD_CONST              15 ('run_manual_test')

 573            LOAD_FAST_BORROW         6 (current)

 574            LOAD_CONST              16 ('FAILED')

 575            LOAD_FAST_BORROW         1 (actor_type)

 576            LOAD_FAST_BORROW         3 (actor)

 577            LOAD_CONST              16 ('FAILED')

 578            LOAD_CONST              31 ('recommendation_no_longer_eligible')

 579            LOAD_CONST              17 ('learning.manual_test.failed')

 580            LOAD_SMALL_INT           1

 571            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 582            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 583            LOAD_CONST               1 ('failed')

 584            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 585            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              16 ('FAILED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 586            LOAD_FAST_BORROW         8 (audit_env)

 587            LOAD_CONST              31 ('recommendation_no_longer_eligible')

 582            LOAD_CONST              30 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 592   L16:     NOP

 593   L17:     LOAD_SMALL_INT           0
                LOAD_CONST              32 (('build_manual_test_evidence_packet',))
                IMPORT_NAME             22 (app.services.learning.manual_test_evidence)
                IMPORT_FROM             23 (build_manual_test_evidence_packet)
                STORE_FAST              12 (build_manual_test_evidence_packet)
                POP_TOP

 596            LOAD_SMALL_INT           0
                LOAD_CONST              33 (('score_manual_test_result',))
                IMPORT_NAME             24 (app.services.learning.manual_test_scoring)
                IMPORT_FROM             25 (score_manual_test_result)
                STORE_FAST              13 (score_manual_test_result)
                POP_TOP

 610   L18:     LOAD_FAST               12 (build_manual_test_evidence_packet)
                PUSH_NULL

 611            LOAD_FAST               10 (rec)

 612            LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              37 ('scenario_type')
                CALL                     1

 613            LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              38 ('mode')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              39 ('SIMULATION_ONLY')

 614   L19:     LOAD_SMALL_INT           1

 615            LOAD_SMALL_INT           0

 610            LOAD_CONST              40 (('recommendation', 'scenario_type', 'mode', 'observation_count', 'warning_count'))
                CALL_KW                  5
                STORE_FAST              15 (evidence_env)

 617            LOAD_FAST               15 (evidence_env)
                LOAD_CONST              12 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST              21 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      205 (to L23)
                NOT_TAKEN

 619            LOAD_CONST              12 ('status')
                LOAD_CONST              16 ('FAILED')

 620            LOAD_CONST              26 ('completed_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 621            LOAD_CONST              27 ('error_code')
                LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              41 ('evidence_build_failed')

 618   L20:     BUILD_MAP                3
                STORE_FAST              11 (patch)

 623            NOP

 624   L21:     LOAD_FAST                5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1
                LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST               11 (patch)
                CALL                     1
                LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST                4 (trid)
                CALL                     2
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                POP_TOP

 627   L22:     LOAD_GLOBAL             19 (_audit + NULL)

 628            LOAD_CONST              15 ('run_manual_test')

 629            LOAD_FAST                6 (current)

 630            LOAD_CONST              16 ('FAILED')

 631            LOAD_FAST                1 (actor_type)

 632            LOAD_FAST                3 (actor)

 633            LOAD_CONST              16 ('FAILED')

 634            LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1

 635            LOAD_CONST              17 ('learning.manual_test.failed')

 636            LOAD_SMALL_INT           1

 627            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 638            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 639            LOAD_CONST               1 ('failed')

 640            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 641            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              16 ('FAILED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 642            LOAD_FAST                8 (audit_env)

 643            LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1

 638            LOAD_CONST              30 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 646   L23:     LOAD_FAST               13 (score_manual_test_result)
                PUSH_NULL

 647            LOAD_FAST               10 (rec)

 648            LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              38 ('mode')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              39 ('SIMULATION_ONLY')

 649   L24:     LOAD_SMALL_INT           0

 646            LOAD_CONST              42 (('recommendation', 'mode', 'warning_count'))
                CALL_KW                  3
                STORE_FAST              16 (score_env)

 651            LOAD_FAST               16 (score_env)
                LOAD_CONST              12 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST              21 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE      205 (to L28)
                NOT_TAKEN

 653            LOAD_CONST              12 ('status')
                LOAD_CONST              16 ('FAILED')

 654            LOAD_CONST              26 ('completed_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 655            LOAD_CONST              27 ('error_code')
                LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              43 ('scoring_failed')

 652   L25:     BUILD_MAP                3
                STORE_FAST              11 (patch)

 657            NOP

 658   L26:     LOAD_FAST                5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1
                LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST               11 (patch)
                CALL                     1
                LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST                4 (trid)
                CALL                     2
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                POP_TOP

 661   L27:     LOAD_GLOBAL             19 (_audit + NULL)

 662            LOAD_CONST              15 ('run_manual_test')

 663            LOAD_FAST                6 (current)

 664            LOAD_CONST              16 ('FAILED')

 665            LOAD_FAST                1 (actor_type)

 666            LOAD_FAST                3 (actor)

 667            LOAD_CONST              16 ('FAILED')

 668            LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1

 669            LOAD_CONST              17 ('learning.manual_test.failed')

 670            LOAD_SMALL_INT           1

 661            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 672            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 673            LOAD_CONST               1 ('failed')

 674            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 675            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              16 ('FAILED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 676            LOAD_FAST                8 (audit_env)

 677            LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              27 ('error_code')
                CALL                     1

 672            LOAD_CONST              30 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 680   L28:     LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              44 ('components')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L29)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L29:     STORE_FAST              17 (components)

 682            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('RUNNING')

 683            LOAD_CONST              45 ('score')
                LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              45 ('score')
                CALL                     1

 684            LOAD_CONST              46 ('confidence_score')
                LOAD_FAST               17 (components)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              47 ('confidence')
                CALL                     1

 685            LOAD_CONST              48 ('risk_score')
                LOAD_FAST               17 (components)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              49 ('risk')
                CALL                     1

 686            LOAD_CONST              50 ('evidence_fingerprint')
                LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              51 ('fingerprint')
                CALL                     1

 687            LOAD_CONST              52 ('metadata')
                LOAD_GLOBAL             61 (_project_metadata + NULL)

 688            LOAD_CONST              53 ('event')
                LOAD_CONST              54 ('learning.manual_test.started')

 689            LOAD_CONST              55 ('recommendation_type')
                LOAD_FAST               10 (rec)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              55 ('recommendation_type')
                CALL                     1

 690            LOAD_CONST              56 ('rationale_token')
                LOAD_FAST               10 (rec)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              56 ('rationale_token')
                CALL                     1

 691            LOAD_CONST              57 ('scenario_fingerprint')
                LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              51 ('fingerprint')
                CALL                     1

 692            LOAD_CONST              58 ('evidence_warning_count')
                LOAD_SMALL_INT           0

 693            LOAD_CONST              59 ('escalation_required')
                LOAD_GLOBAL             63 (bool + NULL)
                LOAD_FAST               16 (score_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              59 ('escalation_required')
                CALL                     1
                CALL                     1

 694            LOAD_CONST              60 ('operator_command')
                LOAD_CONST              61 ('run_manual_test_simulation')

 687            BUILD_MAP                7
                CALL                     1

 681            BUILD_MAP                6
                STORE_FAST              11 (patch)

 698            NOP

 700   L30:     LOAD_FAST                5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1

 701            LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST               11 (patch)
                CALL                     1

 702            LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST                4 (trid)
                CALL                     2

 703            LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0

 699            STORE_FAST              18 (upd)

 705            LOAD_GLOBAL             65 (list + NULL)
                LOAD_GLOBAL             67 (getattr + NULL)
                LOAD_FAST               18 (upd)
                LOAD_CONST              62 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L31)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L31:     CALL                     1
                STORE_FAST              19 (rows_after)

 717   L32:     LOAD_FAST               19 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        67 (to L33)
                NOT_TAKEN

 719            LOAD_GLOBAL             19 (_audit + NULL)

 720            LOAD_CONST              15 ('run_manual_test')

 721            LOAD_FAST                6 (current)

 722            LOAD_CONST              13 ('RUNNING')

 723            LOAD_FAST                1 (actor_type)

 724            LOAD_FAST                3 (actor)

 725            LOAD_CONST              16 ('FAILED')

 726            LOAD_CONST              65 ('policy_refused_or_no_rows')

 727            LOAD_CONST              17 ('learning.manual_test.failed')

 728            LOAD_SMALL_INT           1

 719            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 730            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 731            LOAD_CONST               1 ('failed')

 732            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 733            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('RUNNING')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 734            LOAD_FAST                8 (audit_env)

 735            LOAD_CONST              65 ('policy_refused_or_no_rows')

 730            LOAD_CONST              30 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 738   L33:     LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST               19 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              20 (new_record)

 739            LOAD_GLOBAL             19 (_audit + NULL)

 740            LOAD_CONST              15 ('run_manual_test')

 741            LOAD_FAST               20 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L34)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                6 (current)

 742   L34:     LOAD_CONST              13 ('RUNNING')

 743            LOAD_FAST                1 (actor_type)

 744            LOAD_FAST                3 (actor)

 745            LOAD_CONST              54 ('learning.manual_test.started')

 739            LOAD_CONST              66 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST               8 (audit_env)

 747            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 748            LOAD_CONST              21 ('ok')

 749            LOAD_FAST               20 (new_record)

 750            LOAD_FAST               15 (evidence_env)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              67 ('packet')
                CALL                     1

 751            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('RUNNING')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              68 (True)
                BUILD_MAP                3

 752            LOAD_FAST                8 (audit_env)

 747            LOAD_CONST              69 (('status', 'test_run', 'evidence', 'transition', 'audit_row'))
                CALL_KW                  5
                RETURN_VALUE

  --   L35:     PUSH_EXC_INFO

 540            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L37)
                NOT_TAKEN
                POP_TOP

 541   L36:     POP_EXCEPT
                EXTENDED_ARG             4
                JUMP_BACKWARD_NO_INTERRUPT 1256 (to L12)

 540   L37:     RERAISE                  0

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L39:     PUSH_EXC_INFO

 569            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L41)
                NOT_TAKEN
                POP_TOP

 570   L40:     POP_EXCEPT
                EXTENDED_ARG             4
                JUMP_BACKWARD_NO_INTERRUPT 1099 (to L15)

 569   L41:     RERAISE                  0

  --   L42:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L43:     PUSH_EXC_INFO

 599            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       99 (to L48)
                NOT_TAKEN
                STORE_FAST              14 (e)

 600   L44:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 601            LOAD_CONST              34 ('run_manual_test_simulation import error type=')

 602            LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE

 601            BUILD_STRING             2

 600            CALL                     1
                POP_TOP

 604            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 605            LOAD_CONST               1 ('failed')

 606            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 607            LOAD_CONST              35 ('unexpected:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 604            LOAD_CONST              36 (('status', 'test_run', 'error_code'))
                CALL_KW                  3
       L45:     SWAP                     2
       L46:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L47:     LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 599   L48:     RERAISE                  0

  --   L49:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L50:     PUSH_EXC_INFO

 625            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L52)
                NOT_TAKEN
                POP_TOP

 626   L51:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 975 (to L22)

 625   L52:     RERAISE                  0

  --   L53:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L54:     PUSH_EXC_INFO

 659            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L56)
                NOT_TAKEN
                POP_TOP

 660   L55:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 739 (to L27)

 659   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 706            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L63)
                NOT_TAKEN
                STORE_FAST              14 (e)

 707   L59:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 708            LOAD_CONST              63 ('run_manual_test_simulation update error type=')

 709            LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE

 708            BUILD_STRING             2

 707            CALL                     1
                POP_TOP

 711            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 712            LOAD_CONST               7 ('skipped')

 713            LOAD_CONST              64 ('db_write_failed:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 714            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 711            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L60:     SWAP                     2
       L61:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L62:     LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 706   L63:     RERAISE                  0

  --   L64:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L12 -> L35 [0]
  L14 to L15 -> L39 [0]
  L17 to L18 -> L43 [0]
  L21 to L22 -> L50 [0]
  L26 to L27 -> L54 [0]
  L30 to L32 -> L58 [0]
  L35 to L36 -> L38 [1] lasti
  L37 to L38 -> L38 [1] lasti
  L39 to L40 -> L42 [1] lasti
  L41 to L42 -> L42 [1] lasti
  L43 to L44 -> L49 [1] lasti
  L44 to L45 -> L47 [1] lasti
  L45 to L46 -> L49 [1] lasti
  L47 to L49 -> L49 [1] lasti
  L50 to L51 -> L53 [1] lasti
  L52 to L53 -> L53 [1] lasti
  L54 to L55 -> L57 [1] lasti
  L56 to L57 -> L57 [1] lasti
  L58 to L59 -> L64 [1] lasti
  L59 to L60 -> L62 [1] lasti
  L60 to L61 -> L64 [1] lasti
  L62 to L64 -> L64 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/manual_test_harness.py", line 756>:
756           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

758           LOAD_CONST               2 ('str')

756           LOAD_CONST               3 ('actor_type')

759           LOAD_CONST               2 ('str')

756           LOAD_CONST               4 ('actor_id')

760           LOAD_CONST               5 ('Optional[str]')

756           LOAD_CONST               6 ('acknowledge_high_risk')

761           LOAD_CONST               7 ('bool')

756           LOAD_CONST               8 ('return')

762           LOAD_CONST               9 ('Dict[str, Any]')

756           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object complete_manual_test_run at 0x0000018C17ED36F0, file "app/services/learning/manual_test_harness.py", line 756>:
 756            RESUME                   0

 766            LOAD_FAST_BORROW         1 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 767            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 768    L1:     LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                LOAD_GLOBAL              6 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               4 (actor)

 769            LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 770            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 771    L4:     LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                LOAD_GLOBAL              8 (_TEST_RUN_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               5 (trid)

 772            LOAD_FAST_BORROW         5 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 773            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_test_run_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 775    L5:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 776            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 777            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 778            LOAD_CONST               7 ('skipped')

 779            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

 780            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 777            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 783    L6:     LOAD_GLOBAL             13 (_lookup_test_run + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (db, trid)
                LOAD_CONST              10 (('test_run_id',))
                CALL_KW                  2
                STORE_FAST               7 (current)

 784            LOAD_FAST_BORROW         7 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 785            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST              11 ('test_run_not_found')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 786    L7:     LOAD_GLOBAL             15 (_validate_transition + NULL)

 787            LOAD_FAST_BORROW         7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1

 788            LOAD_CONST              13 ('COMPLETED')

 786            LOAD_CONST              14 (('from_status', 'to_status'))
                CALL_KW                  2
                STORE_FAST               8 (err)

 790            LOAD_FAST_BORROW         8 (err)
                POP_JUMP_IF_NONE        67 (to L8)
                NOT_TAKEN

 791            LOAD_GLOBAL             19 (_audit + NULL)

 792            LOAD_CONST              15 ('complete_manual_test')

 793            LOAD_FAST_BORROW         7 (current)

 794            LOAD_CONST              13 ('COMPLETED')

 795            LOAD_FAST_BORROW         1 (actor_type)

 796            LOAD_FAST_BORROW         4 (actor)

 797            LOAD_CONST              16 ('FAILED')

 798            LOAD_FAST_BORROW         8 (err)

 799            LOAD_CONST              17 ('learning.manual_test.failed')

 800            LOAD_SMALL_INT           1

 791            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               9 (audit_env)

 802            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 803            LOAD_CONST               1 ('failed')

 804            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         7 (current)
                CALL                     1

 805            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('COMPLETED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 806            LOAD_FAST_BORROW         9 (audit_env)

 807            LOAD_FAST_BORROW         8 (err)

 802            LOAD_CONST              23 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 812    L8:     LOAD_FAST_BORROW         7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              24 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L9:     STORE_FAST              10 (md)

 813            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (md)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L10)
                NOT_TAKEN
                LOAD_GLOBAL             27 (bool + NULL)
                LOAD_FAST_BORROW        10 (md)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              25 ('escalation_required')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              22 (False)
       L11:     STORE_FAST              11 (escalation)

 814            LOAD_FAST_BORROW        11 (escalation)
                TO_BOOL
                POP_JUMP_IF_FALSE       84 (to L12)
                NOT_TAKEN
                LOAD_GLOBAL             27 (bool + NULL)
                LOAD_FAST_BORROW         3 (acknowledge_high_risk)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        67 (to L12)
                NOT_TAKEN

 815            LOAD_GLOBAL             19 (_audit + NULL)

 816            LOAD_CONST              15 ('complete_manual_test')

 817            LOAD_FAST_BORROW         7 (current)

 818            LOAD_CONST              13 ('COMPLETED')

 819            LOAD_FAST_BORROW         1 (actor_type)

 820            LOAD_FAST_BORROW         4 (actor)

 821            LOAD_CONST              16 ('FAILED')

 822            LOAD_CONST              26 ('high_risk_acknowledgement_required')

 823            LOAD_CONST              17 ('learning.manual_test.failed')

 824            LOAD_SMALL_INT           1

 815            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               9 (audit_env)

 826            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 827            LOAD_CONST               1 ('failed')

 828            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         7 (current)
                CALL                     1

 829            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('COMPLETED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 830            LOAD_FAST_BORROW         9 (audit_env)

 831            LOAD_CONST              26 ('high_risk_acknowledgement_required')

 826            LOAD_CONST              23 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 834   L12:     LOAD_GLOBAL             29 (_project_metadata + NULL)
                BUILD_MAP                0

 835            LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST_BORROW        10 (md)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_FAST               10 (md)
                JUMP_FORWARD             1 (to L14)
       L13:     BUILD_MAP                0

 834   L14:     DICT_UPDATE              1

 836            LOAD_CONST              27 ('event')
                LOAD_CONST              28 ('learning.manual_test.completed')

 837            LOAD_CONST              29 ('operator_command')
                LOAD_CONST              30 ('complete_manual_test_run')

 838            LOAD_CONST              31 ('ack_high_risk_recorded')
                LOAD_GLOBAL             27 (bool + NULL)
                LOAD_FAST_BORROW         3 (acknowledge_high_risk)
                CALL                     1

 834            BUILD_MAP                3
                DICT_UPDATE              1
                CALL                     1
                STORE_FAST              12 (new_metadata)

 841            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('COMPLETED')

 842            LOAD_CONST              32 ('completed_at')
                LOAD_GLOBAL             31 (_now_iso + NULL)
                CALL                     0

 843            LOAD_CONST              24 ('metadata')
                LOAD_FAST_BORROW        12 (new_metadata)

 840            BUILD_MAP                3
                STORE_FAST              13 (patch)

 846            NOP

 848   L15:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1

 849            LOAD_ATTR               37 (update + NULL|self)
                LOAD_FAST_BORROW        13 (patch)
                CALL                     1

 850            LOAD_ATTR               39 (eq + NULL|self)
                LOAD_CONST              33 ('test_run_id')
                LOAD_FAST_BORROW         5 (trid)
                CALL                     2

 851            LOAD_ATTR               41 (execute + NULL|self)
                CALL                     0

 847            STORE_FAST              14 (upd)

 853            LOAD_GLOBAL             43 (list + NULL)
                LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST_BORROW        14 (upd)
                LOAD_CONST              34 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              15 (rows_after)

 864   L17:     LOAD_FAST               15 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        67 (to L18)
                NOT_TAKEN

 865            LOAD_GLOBAL             19 (_audit + NULL)

 866            LOAD_CONST              15 ('complete_manual_test')

 867            LOAD_FAST                7 (current)

 868            LOAD_CONST              13 ('COMPLETED')

 869            LOAD_FAST                1 (actor_type)

 870            LOAD_FAST                4 (actor)

 871            LOAD_CONST              16 ('FAILED')

 872            LOAD_CONST              37 ('policy_refused_or_no_rows')

 873            LOAD_CONST              17 ('learning.manual_test.failed')

 874            LOAD_SMALL_INT           1

 865            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               9 (audit_env)

 876            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 877            LOAD_CONST               1 ('failed')

 878            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                7 (current)
                CALL                     1

 879            LOAD_CONST              19 ('from')
                LOAD_FAST                7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('COMPLETED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 880            LOAD_FAST                9 (audit_env)

 881            LOAD_CONST              37 ('policy_refused_or_no_rows')

 876            LOAD_CONST              23 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 883   L18:     LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST               15 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              17 (new_record)

 884            LOAD_GLOBAL             19 (_audit + NULL)

 885            LOAD_CONST              15 ('complete_manual_test')

 886            LOAD_FAST               17 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                7 (current)

 887   L19:     LOAD_CONST              13 ('COMPLETED')

 888            LOAD_FAST                1 (actor_type)

 889            LOAD_FAST                4 (actor)

 890            LOAD_CONST              28 ('learning.manual_test.completed')

 884            LOAD_CONST              38 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST               9 (audit_env)

 892            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 893            LOAD_CONST              21 ('ok')

 894            LOAD_FAST               17 (new_record)

 895            LOAD_CONST              19 ('from')
                LOAD_FAST                7 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('COMPLETED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              39 (True)
                BUILD_MAP                3

 896            LOAD_FAST                9 (audit_env)

 892            LOAD_CONST              40 (('status', 'test_run', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 854            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L25)
                NOT_TAKEN
                STORE_FAST              16 (e)

 855   L21:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 856            LOAD_CONST              35 ('complete_manual_test_run update error type=')

 857            LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE

 856            BUILD_STRING             2

 855            CALL                     1
                POP_TOP

 859            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 860            LOAD_CONST               7 ('skipped')

 861            LOAD_CONST              36 ('db_write_failed:')
                LOAD_GLOBAL             53 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               54 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 862            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 859            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 854   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L15 to L17 -> L20 [0]
  L20 to L21 -> L26 [1] lasti
  L21 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/learning/manual_test_harness.py", line 900>:
900           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

902           LOAD_CONST               2 ('str')

900           LOAD_CONST               3 ('actor_type')

903           LOAD_CONST               2 ('str')

900           LOAD_CONST               4 ('actor_id')

904           LOAD_CONST               5 ('Optional[str]')

900           LOAD_CONST               6 ('return')

905           LOAD_CONST               7 ('Dict[str, Any]')

900           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object cancel_manual_test_run at 0x0000018C17F80CC0, file "app/services/learning/manual_test_harness.py", line 900>:
 900            RESUME                   0

 907            LOAD_FAST_BORROW         1 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       14 (to L1)
                NOT_TAKEN

 908            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               2 ('invalid_actor_type')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 909    L1:     LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         2 (actor_id)
                LOAD_GLOBAL              6 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               4 (None)
        L3:     STORE_FAST               3 (actor)

 910            LOAD_FAST_BORROW         2 (actor_id)
                POP_JUMP_IF_NONE        18 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (actor)
                POP_JUMP_IF_NOT_NONE    14 (to L4)
                NOT_TAKEN

 911            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               5 ('invalid_actor_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 912    L4:     LOAD_GLOBAL              5 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                LOAD_GLOBAL              8 (_TEST_RUN_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               4 (trid)

 913            LOAD_FAST_BORROW         4 (trid)
                POP_JUMP_IF_NOT_NONE    14 (to L5)
                NOT_TAKEN

 914            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST               6 ('invalid_test_run_id')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 916    L5:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 917            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L6)
                NOT_TAKEN

 918            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 919            LOAD_CONST               7 ('skipped')

 920            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

 921            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 918            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 924    L6:     LOAD_GLOBAL             13 (_lookup_test_run + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (db, trid)
                LOAD_CONST              10 (('test_run_id',))
                CALL_KW                  2
                STORE_FAST               6 (current)

 925            LOAD_FAST_BORROW         6 (current)
                POP_JUMP_IF_NOT_NONE    14 (to L7)
                NOT_TAKEN

 926            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_CONST              11 ('test_run_not_found')
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 927    L7:     LOAD_GLOBAL             15 (_validate_transition + NULL)

 928            LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1

 929            LOAD_CONST              13 ('CANCELLED')

 927            LOAD_CONST              14 (('from_status', 'to_status'))
                CALL_KW                  2
                STORE_FAST               7 (err)

 931            LOAD_FAST_BORROW         7 (err)
                POP_JUMP_IF_NONE        67 (to L8)
                NOT_TAKEN

 932            LOAD_GLOBAL             19 (_audit + NULL)

 933            LOAD_CONST              15 ('cancel_manual_test')

 934            LOAD_FAST_BORROW         6 (current)

 935            LOAD_CONST              13 ('CANCELLED')

 936            LOAD_FAST_BORROW         1 (actor_type)

 937            LOAD_FAST_BORROW         3 (actor)

 938            LOAD_CONST              16 ('FAILED')

 939            LOAD_FAST_BORROW         7 (err)

 940            LOAD_CONST              17 ('learning.manual_test.cancelled')

 941            LOAD_SMALL_INT           1

 932            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 943            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 944            LOAD_CONST               1 ('failed')

 945            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST_BORROW         6 (current)
                CALL                     1

 946            LOAD_CONST              19 ('from')
                LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('CANCELLED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 947            LOAD_FAST_BORROW         8 (audit_env)

 948            LOAD_FAST_BORROW         7 (err)

 943            LOAD_CONST              23 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 951    L8:     LOAD_FAST_BORROW         6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              24 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L9:     STORE_FAST               9 (md)

 952            LOAD_GLOBAL             23 (_project_metadata + NULL)
                BUILD_MAP                0

 953            LOAD_GLOBAL             25 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (md)
                LOAD_GLOBAL             26 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_FAST                9 (md)
                JUMP_FORWARD             1 (to L11)
       L10:     BUILD_MAP                0

 952   L11:     DICT_UPDATE              1

 954            LOAD_CONST              25 ('event')
                LOAD_CONST              17 ('learning.manual_test.cancelled')

 955            LOAD_CONST              26 ('operator_command')
                LOAD_CONST              27 ('cancel_manual_test_run')

 952            BUILD_MAP                2
                DICT_UPDATE              1
                CALL                     1
                STORE_FAST              10 (new_metadata)

 958            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('CANCELLED')

 959            LOAD_CONST              28 ('completed_at')
                LOAD_GLOBAL             29 (_now_iso + NULL)
                CALL                     0

 960            LOAD_CONST              24 ('metadata')
                LOAD_FAST_BORROW        10 (new_metadata)

 957            BUILD_MAP                3
                STORE_FAST              11 (patch)

 963            NOP

 965   L12:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR               31 (table + NULL|self)
                LOAD_GLOBAL             32 (_TABLE)
                CALL                     1

 966            LOAD_ATTR               35 (update + NULL|self)
                LOAD_FAST_BORROW        11 (patch)
                CALL                     1

 967            LOAD_ATTR               37 (eq + NULL|self)
                LOAD_CONST              29 ('test_run_id')
                LOAD_FAST_BORROW         4 (trid)
                CALL                     2

 968            LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0

 964            STORE_FAST              12 (upd)

 970            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW        12 (upd)
                LOAD_CONST              30 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1
                STORE_FAST              13 (rows_after)

 980   L14:     LOAD_FAST               13 (rows_after)
                TO_BOOL
                POP_JUMP_IF_TRUE        67 (to L15)
                NOT_TAKEN

 981            LOAD_GLOBAL             19 (_audit + NULL)

 982            LOAD_CONST              15 ('cancel_manual_test')

 983            LOAD_FAST                6 (current)

 984            LOAD_CONST              13 ('CANCELLED')

 985            LOAD_FAST                1 (actor_type)

 986            LOAD_FAST                3 (actor)

 987            LOAD_CONST              16 ('FAILED')

 988            LOAD_CONST              33 ('policy_refused_or_no_rows')

 989            LOAD_CONST              17 ('learning.manual_test.cancelled')

 990            LOAD_SMALL_INT           1

 981            LOAD_CONST              18 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                STORE_FAST               8 (audit_env)

 992            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 993            LOAD_CONST               1 ('failed')

 994            LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST                6 (current)
                CALL                     1

 995            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('CANCELLED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              22 (False)
                BUILD_MAP                3

 996            LOAD_FAST                8 (audit_env)

 997            LOAD_CONST              33 ('policy_refused_or_no_rows')

 992            LOAD_CONST              23 (('status', 'test_run', 'transition', 'audit_row', 'error_code'))
                CALL_KW                  5
                RETURN_VALUE

 999   L15:     LOAD_GLOBAL             21 (_project_row + NULL)
                LOAD_FAST               13 (rows_after)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST              15 (new_record)

1000            LOAD_GLOBAL             19 (_audit + NULL)

1001            LOAD_CONST              15 ('cancel_manual_test')

1002            LOAD_FAST               15 (new_record)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                6 (current)

1003   L16:     LOAD_CONST              13 ('CANCELLED')

1004            LOAD_FAST                1 (actor_type)

1005            LOAD_FAST                3 (actor)

1006            LOAD_CONST              17 ('learning.manual_test.cancelled')

1000            LOAD_CONST              34 (('action', 'record', 'target_status', 'actor_type', 'actor_id', 'event'))
                CALL_KW                  6
                STORE_FAST               8 (audit_env)

1008            LOAD_GLOBAL              3 (_safe_envelope + NULL)

1009            LOAD_CONST              21 ('ok')

1010            LOAD_FAST               15 (new_record)

1011            LOAD_CONST              19 ('from')
                LOAD_FAST                6 (current)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              20 ('to')
                LOAD_CONST              13 ('CANCELLED')
                LOAD_CONST              21 ('ok')
                LOAD_CONST              35 (True)
                BUILD_MAP                3

1012            LOAD_FAST                8 (audit_env)

1008            LOAD_CONST              36 (('status', 'test_run', 'transition', 'audit_row'))
                CALL_KW                  4
                RETURN_VALUE

  --   L17:     PUSH_EXC_INFO

 971            LOAD_GLOBAL             44 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L22)
                NOT_TAKEN
                STORE_FAST              14 (e)

 972   L18:     LOAD_GLOBAL             46 (logger)
                LOAD_ATTR               49 (warning + NULL|self)

 973            LOAD_CONST              31 ('cancel_manual_test_run update error type=')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 972            CALL                     1
                POP_TOP

 975            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 976            LOAD_CONST               7 ('skipped')

 977            LOAD_CONST              32 ('db_write_failed:')
                LOAD_GLOBAL             51 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               52 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 978            LOAD_CONST               8 ('learning_manual_test_runs_store_unavailable')

 975            LOAD_CONST               9 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               4 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 971   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L12 to L14 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app/services/learning/manual_test_harness.py", line 1020>:
1020           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('brokerage_id')

1022           LOAD_CONST               2 ('Optional[str]')

1020           LOAD_CONST               3 ('status')

1023           LOAD_CONST               2 ('Optional[str]')

1020           LOAD_CONST               4 ('limit')

1024           LOAD_CONST               5 ('Any')

1020           LOAD_CONST               6 ('return')

1025           LOAD_CONST               7 ('Dict[str, Any]')

1020           BUILD_MAP                4
               RETURN_VALUE

Disassembly of <code object manual_test_run_report at 0x0000018C17F81320, file "app/services/learning/manual_test_harness.py", line 1020>:
1020            RESUME                   0

1028            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               3 (bid)

1029            LOAD_FAST_BORROW         1 (status)
                POP_JUMP_IF_NONE        26 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (status)
                LOAD_GLOBAL              2 (ALLOWED_MANUAL_TEST_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       15 (to L3)
                NOT_TAKEN

1031            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

1032            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

1033            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

1034            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

1035            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

1036            LOAD_CONST               8 ('error_code')
                LOAD_CONST               9 ('invalid_status')

1030            BUILD_MAP                6
                RETURN_VALUE

1038    L3:     LOAD_GLOBAL              5 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               4 (capped)

1039            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               5 (db)

1040            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L4)
                NOT_TAKEN

1042            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

1043            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

1044            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

1045            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

1046            LOAD_CONST               7 ('warnings')
                LOAD_CONST              11 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

1047            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('learning_manual_test_runs_store_unavailable')

1041            BUILD_MAP                6
                RETURN_VALUE

1049    L4:     NOP

1051    L5:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

1052            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              12 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

1053            LOAD_ATTR               19 (order + NULL|self)
                LOAD_CONST              13 ('started_at')
                LOAD_CONST              14 (True)
                LOAD_CONST              15 (('desc',))
                CALL_KW                  2

1054            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     1

1050            STORE_FAST               6 (query)

1056            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

1057    L7:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               6 (query)

1058    L8:     LOAD_FAST_BORROW         1 (status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

1059   L10:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         1 (status)
                CALL                     2
                STORE_FAST               6 (query)

1060   L11:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               25 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

1061            LOAD_GLOBAL             27 (list + NULL)
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

1062            LOAD_CONST              17 (<code object <genexpr> at 0x0000018C180909C0, file "app/services/learning/manual_test_harness.py", line 1062>)
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

1064            LOAD_CONST               2 ('status')
                LOAD_CONST              18 ('ok')

1065            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

1066            LOAD_CONST               5 ('rows')
                LOAD_FAST_BORROW        10 (projected)

1067            LOAD_CONST               6 ('count')
                LOAD_GLOBAL             31 (len + NULL)
                LOAD_FAST_BORROW        10 (projected)
                CALL                     1

1068            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

1069            LOAD_CONST               8 ('error_code')
                LOAD_CONST               1 (None)

1063            BUILD_MAP                6
       L21:     RETURN_VALUE

  --   L22:     SWAP                     2
                POP_TOP

1062            SWAP                     2
                STORE_FAST               9 (p)
                RERAISE                  0

  --   L23:     PUSH_EXC_INFO

1071            LOAD_GLOBAL             32 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L28)
                NOT_TAKEN
                STORE_FAST              11 (e)

1072   L24:     LOAD_GLOBAL             34 (logger)
                LOAD_ATTR               37 (warning + NULL|self)

1073            LOAD_CONST              19 ('manual_test_run_report read error type=')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

1072            CALL                     1
                POP_TOP

1076            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

1077            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                3 (bid)

1078            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

1079            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

1080            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             39 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               40 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

1081            LOAD_CONST               8 ('error_code')
                LOAD_CONST              11 ('learning_manual_test_runs_store_unavailable')

1075            BUILD_MAP                6
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

1071   L28:     RERAISE                  0

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

Disassembly of <code object <genexpr> at 0x0000018C180909C0, file "app/services/learning/manual_test_harness.py", line 1062>:
1062           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/learning/manual_test_harness.py", line 1085>:
1085           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('test_run_id')

1087           LOAD_CONST               2 ('str')

1085           LOAD_CONST               3 ('brokerage_id')

1088           LOAD_CONST               4 ('Optional[str]')

1085           LOAD_CONST               5 ('return')

1089           LOAD_CONST               6 ('Dict[str, Any]')

1085           BUILD_MAP                3
               RETURN_VALUE

Disassembly of <code object get_manual_test_run at 0x0000018C17F81A80, file "app/services/learning/manual_test_harness.py", line 1085>:
1085            RESUME                   0

1092            LOAD_GLOBAL              1 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                LOAD_GLOBAL              2 (_TEST_RUN_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               2 (trid)

1093            LOAD_FAST_BORROW         2 (trid)
                POP_JUMP_IF_NOT_NONE    11 (to L1)
                NOT_TAKEN

1095            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

1096            LOAD_CONST               4 ('test_run')
                LOAD_CONST               1 (None)

1097            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

1098            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_test_run_id')

1094            BUILD_MAP                4
                RETURN_VALUE

1100    L1:     LOAD_FAST_BORROW         1 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

1101            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

1102            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L4)
                NOT_TAKEN

1104            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

1105            LOAD_CONST               4 ('test_run')
                LOAD_CONST               1 (None)

1106            LOAD_CONST               5 ('warnings')
                LOAD_CONST               9 ('learning_manual_test_runs_store_unavailable')
                BUILD_LIST               1

1107            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('learning_manual_test_runs_store_unavailable')

1103            BUILD_MAP                4
                RETURN_VALUE

1109    L4:     NOP

1111    L5:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

1112            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              10 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

1113            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              11 ('test_run_id')
                LOAD_FAST_BORROW         2 (trid)
                CALL                     2

1114            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

1110            STORE_FAST               5 (query)

1116            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

1117    L7:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               5 (query)

1118    L8:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

1119            LOAD_GLOBAL             25 (list + NULL)
                LOAD_GLOBAL             27 (getattr + NULL)
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

1130   L12:     LOAD_FAST                7 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L13)
                NOT_TAKEN

1132            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

1133            LOAD_CONST               4 ('test_run')
                LOAD_CONST               1 (None)

1134            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

1135            LOAD_CONST               6 ('error_code')
                LOAD_CONST              16 ('test_run_not_found_or_cross_brokerage')

1131            BUILD_MAP                4
                RETURN_VALUE

1138   L13:     LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('ok')

1139            LOAD_CONST               4 ('test_run')
                LOAD_GLOBAL             39 (_project_row + NULL)
                LOAD_FAST                7 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

1140            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

1141            LOAD_CONST               6 ('error_code')
                LOAD_CONST               1 (None)

1137            BUILD_MAP                4
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

1120            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L19)
                NOT_TAKEN
                STORE_FAST               8 (e)

1121   L15:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

1122            LOAD_CONST              14 ('get_manual_test_run read error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

1121            CALL                     1
                POP_TOP

1125            LOAD_CONST               2 ('status')
                LOAD_CONST               8 ('skipped')

1126            LOAD_CONST               4 ('test_run')
                LOAD_CONST               1 (None)

1127            LOAD_CONST               5 ('warnings')
                LOAD_CONST              15 ('db_read_failed:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

1128            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('learning_manual_test_runs_store_unavailable')

1124            BUILD_MAP                4
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

1120   L19:     RERAISE                  0

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
```
