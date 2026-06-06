# learning/adaptive_memory_bridge

- **pyc:** `app\services\learning\__pycache__\adaptive_memory_bridge.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/adaptive_memory_bridge.py`
- **co_filename (from bytecode):** `app/services/learning/adaptive_memory_bridge.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS182 — Adaptive memory bridge.

Strictly-gated bridge from a COMPLETED manual-test run (PAS181)
into a CANDIDATE memory record (PAS163). The bridge is:

* **Operator-initiated.** No background worker, no schedule.
* **Auditable.** Every confirmation + every rejection writes a
  PAS174 audit row.
* **Non-autonomous.** Every step requires an explicit operator
  call; the bridge never auto-confirms, never auto-creates a
  candidate, and never auto-approves a candidate. APPROVED is
  the Memory Review console's job — PAS182 is the entry to the
  CANDIDATE-only pipeline.

Doctrine — invariants enforced in this module:

* **CANDIDATE only.** ``bridge_to_memory_candidate`` calls
  ``app.services.memory.candidate_pipeline``; that pipeline
  filters DANGEROUS / EPHEMERAL, pins ``brokerage_id`` from the
  argument, sanitises evidence, and forces
  ``MemoryStatus.CANDIDATE``. PAS182 never creates APPROVED.
* **Eligibility gate.** ``evaluate_bridge_eligibility`` returns
  the 8 closed conditions; ALL must be true for the bridge to
  proceed. Any failed condition surfaces a structural
  ``reason_code``.
* **NEVER raises.** Every public function collapses to a
  structural envelope.
* **No LLM. No embeddings. No vector DB. No live behaviour
  mutation.** PAS182 never imports the outbound FSM, Memory
  Review UI, booking engine, Slack core, or worker.
* **Closed payload allow-list.** ``ALLOWED_BRIDGE_KEYS``
  matches the PAS182 spec — nothing else leaks out.

Public surface:

  * ``LOW_RISK_THRESHOLD``                       — float, default 0.3
  * ``HIGH_CONFIDENCE_THRESHOLD``                — float, default 0.7
  * ``ALLOWED_BRIDGE_REASON_CODES``              — closed enum
  * ``ALLOWED_BRIDGE_KEYS``                      — payload allow-list
  * ``evaluate_bridge_eligibility(...)``         — pure verdict
  * ``bridge_to_memory_candidate(...)``          — CANDIDATE-only
  * ``adaptive_memory_bridge_report(...)``       — bounded read
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.learning.guardrails`, `app.services.learning.manual_test_harness`, `app.services.memory.candidate_pipeline`, `app.services.operator.audit_service`, `datetime`, `generate_memory_candidates_from_replay`, `get_manual_test_run`, `get_supabase`, `learning_forbidden_field_scan`, `log_operator_action`, `logging`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_audit`, `_bound_brokerage_id`, `_bound_id`, `_bridge_envelope`, `_build_candidate_bundle`, `_clamp_limit`, `_get_db_safe`, `_lookup_recommendation`, `_lookup_test_run`, `_now_iso`, `_safe_float`, `adaptive_memory_bridge_report`, `bridge_to_memory_candidate`, `evaluate_bridge_eligibility`

## Env-key candidates

`ALLOWED_ACTOR_TYPES`, `ALLOWED_BRIDGE_KEYS`, `ALLOWED_BRIDGE_REASON_CODES`, `APPROVED_FOR_MANUAL_TEST`, `COMPLETED`, `FAILED`, `HIGH_CONFIDENCE_THRESHOLD`, `LOW_RISK_THRESHOLD`, `MANUAL_TEST_RUN`, `PAS182_BRIDGE`, `SUCCESS`, `SYSTEM`

## String constants (redacted where noted)

- "\nPAS182 — Adaptive memory bridge.\n\nStrictly-gated bridge from a COMPLETED manual-test run (PAS181)\ninto a CANDIDATE memory record (PAS163). The bridge is:\n\n* **Operator-initiated.** No background worker, no schedule.\n* **Auditable.** Every confirmation + every rejection writes a\n  PAS174 audit row.\n* **Non-autonomous.** Every step requires an explicit operator\n  call; the bridge never auto-confirms, never auto-creates a\n  candidate, and never auto-approves a candidate. APPROVED is\n  the Memory Review console's job — PAS182 is the entry to the\n  CANDIDATE-only pipeline.\n\nDoctrine — invariants enforced in this module:\n\n* **CANDIDATE only.** ``bridge_to_memory_candidate`` calls\n  ``app.services.memory.candidate_pipeline``; that pipeline\n  filters DANGEROUS / EPHEMERAL, pins ``brokerage_id`` from the\n  argument, sanitises evidence, and forces\n  ``MemoryStatus.CANDIDATE``. PAS182 never creates APPROVED.\n* **Eligibility gate.** ``evaluate_bridge_eligibility`` returns\n  the 8 closed conditions; ALL must be true for the bridge to\n  proceed. Any failed condition surfaces a structural\n  ``reason_code``.\n* **NEVER raises.** Every public function collapses to a\n  structural envelope.\n* **No LLM. No embeddings. No vector DB. No live behaviour\n  mutation.** PAS182 never imports the outbound FSM, Memory\n  Review UI, booking engine, Slack core, or worker.\n* **Closed payload allow-list.** ``ALLOWED_BRIDGE_KEYS``\n  matches the PAS182 spec — nothing else leaks out.\n\nPublic surface:\n\n  * ``LOW_RISK_THRESHOLD``                       — float, default 0.3\n  * ``HIGH_CONFIDENCE_THRESHOLD``                — float, default 0.7\n  * ``ALLOWED_BRIDGE_REASON_CODES``              — closed enum\n  * ``ALLOWED_BRIDGE_KEYS``                      — payload allow-list\n  * ``evaluate_bridge_eligibility(...)``         — pure verdict\n  * ``bridge_to_memory_candidate(...)``          — CANDIDATE-only\n  * ``adaptive_memory_bridge_report(...)``       — bounded read\n"
- 'pas.learning.adaptive_memory_bridge'
- 'float'
- 'LOW_RISK_THRESHOLD'
- 'HIGH_CONFIDENCE_THRESHOLD'
- 'eligible'
- 'Tuple[str, ...]'
- 'ALLOWED_BRIDGE_REASON_CODES'
- 'brokerage_id'
- 'recommendation_id'
- 'test_run_id'
- 'memory_candidate_id'
- 'risk_score'
- 'confidence_score'
- 'warning_count'
- 'error_code'
- 'actor_type'
- 'actor_id'
- 'ALLOWED_BRIDGE_KEYS'
- 'ALLOWED_ACTOR_TYPES'
- 'APPROVED_FOR_MANUAL_TEST'
- 'str'
- '_ELIGIBLE_RECOMMENDATION_STATUS'
- 'COMPLETED'
- '_ELIGIBLE_TEST_RUN_STATUS'
- '_ELIGIBLE_TEST_RUN_MODES'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'reason_code'
- 'evidence_fingerprint'
- 'warnings'
- 'audit_status'
- 'SUCCESS'
- 'event'
- 'learning.adaptive_memory.bridge_event'
- 'confirm'
- 'limit'
- 'return'
- 'seconds'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'Optional[float]'
- 'status'
- 'Optional[bool]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'Closed-shape bridge envelope. ``reason_code`` is validated\nagainst the closed enum; anything else collapses to None.'
- 'created_at'
- 'adaptive_memory_bridge db client unavailable type='
- 'Optional[Dict[str, Any]]'
- 'test_run'
- 'adaptive_memory_bridge lookup_test_run error type='
- 'pas_learning_recommendations'
- 'recommendation_id, brokerage_id, recommendation_type, source_type, source_id, status, confidence_score, risk_score, usefulness_score, rationale_token, created_at, reviewed_at'
- 'data'
- 'adaptive_memory_bridge lookup_recommendation error type='
- 'action'
- 'target_id'
- 'Best-effort PAS174 audit-row append. NEVER raises.'
- 'learning_adaptive_memory_bridge'
- 'adaptive_memory_bridge audit error type='
- 'Pure structural verdict — is this manual-test run eligible\nto bridge into a CANDIDATE memory record?\n\nReturns the closed envelope shape; ``eligible`` is True iff\nALL 8 conditions hold:\n\n  1. ``recommendation`` row exists\n  2. ``recommendation.status == APPROVED_FOR_MANUAL_TEST``\n  3. ``test_run`` row exists (and matches brokerage if given)\n  4. ``test_run.status == COMPLETED``\n  5. ``test_run.mode in {SIMULATION_ONLY, OBSERVATIONAL_ONLY}``\n  6. ``test_run.risk_score <= LOW_RISK_THRESHOLD``\n  7. ``test_run.confidence_score >= HIGH_CONFIDENCE_THRESHOLD``\n  8. ``test_run.evidence_fingerprint`` is present\n\nPlus a forbidden-field guardrail scan on the resolved\nrecommendation + test_run pair.\n\nNEVER raises.'
- 'failed'
- 'invalid_test_run_id'
- 'skipped'
- 'store_unavailable'
- 'test_run_not_found'
- 'cross_brokerage_lookup'
- 'test_run_not_completed'
- 'test_run_status:'
- 'mode'
- 'test_run_mode_not_simulation'
- 'test_run_mode:'
- 'test_run_risk_too_high'
- 'test_run_confidence_too_low'
- 'test_run_evidence_fingerprint_missing'
- 'recommendation_not_found'
- 'recommendation_not_approved_for_manual_test'
- 'recommendation'
- 'evaluate_bridge_eligibility guardrail import error type='
- 'valid'
- 'guardrail_forbidden_field_present'
- "Build a strictly structural bundle that PAS163's\nclassifier can consume. NEVER carries raw text or PII —\nevery value is a closed enum token, a fingerprint, or a\nbounded numeric. The PAS163 pipeline re-sanitises evidence\non the way to storage as defence-in-depth."
- 'source_kind'
- 'PAS182_BRIDGE'
- 'source_type'
- 'MANUAL_TEST_RUN'
- 'recommendation_type'
- 'scenario_type'
- 'final_outcome'
- 'manual_test_completed'
- 'rationale_token'
- 'confidence_hint'
- 'risk_hint'
- 'score_hint'
- 'score'
- 'missing_lifecycle_steps'
- 'bool'
- 'Operator-initiated bridge from a COMPLETED manual-test run\ninto a CANDIDATE memory record.\n\n``confirm`` MUST be ``True``. Any call with ``confirm=False``\nis rejected as ``bridge_rejected_by_operator`` — the bridge\nrequires an explicit operator confirmation step.\n\nOn success the candidate is created via\n``app.services.memory.candidate_pipeline.generate_memory_\ncandidates_from_replay`` with the bridge bundle. The pipeline\nforces ``MemoryStatus.CANDIDATE``, filters DANGEROUS /\nEPHEMERAL, and sanitises evidence. PAS182 NEVER creates\nAPPROVED.\n\nIf the PAS163 storage helper is unavailable the bridge\nreturns ``status="skipped"`` + ``reason_code="missing_storage_\nhelper"``. NEVER raises.'
- 'invalid_actor_type'
- 'invalid_actor_id'
- 'adaptive_memory_bridge_rejected'
- 'FAILED'
- 'learning.adaptive_memory.bridge_rejected'
- 'bridge_rejected_by_operator'
- 'bridge_to_memory_candidate pipeline import error type='
- 'memory_candidate_pipeline_unavailable'
- 'pipeline_import_failed:'
- 'SYSTEM'
- 'pas182_bridge:'
- 'unknown'
- 'candidates_created'
- 'results'
- 'memory_id'
- 'missing_storage_helper'
- 'adaptive_memory_bridge_skipped'
- 'adaptive_memory_bridge_confirmed'
- 'learning.adaptive_memory.bridge_confirmed'
- 'adaptive_memory_candidate_created'
- 'learning.adaptive_memory.candidate_created'
- 'candidate_created'
- 'candidate_skipped'
- 'adaptive_memory_bridge_failed'
- 'candidate_failed'
- 'Bounded paginated read of bridge activity for the\noperator dashboard. Reads from the PAS174 operator-actions\naudit log filtered to PAS182 bridge events. NEVER raises.\nNEVER returns PII.\n\nTenant callers MUST use the safe tenant projection layer in\n``adaptive_memory_projection.project_tenant_bridge_list``.'
- 'rows'
- 'count'
- 'pas_operator_actions_log'
- 'id, brokerage_id, actor_type, action, status, target_type, target_id, warning_count, error_code, created_at'
- 'adaptive_memory_bridge_report read error type='
- 'db_read_failed:'
- 'target_type'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ("\nPAS182 — Adaptive memory bridge.\n\nStrictly-gated bridge from a COMPLETED manual-test run (PAS181)\ninto a CANDIDATE memory record (PAS163). The bridge is:\n\n* **Operator-initiated.** No background worker, no schedule.\n* **Auditable.** Every confirmation + every rejection writes a\n  PAS174 audit row.\n* **Non-autonomous.** Every step requires an explicit operator\n  call; the bridge never auto-confirms, never auto-creates a\n  candidate, and never auto-approves a candidate. APPROVED is\n  the Memory Review console's job — PAS182 is the entry to the\n  CANDIDATE-only pipeline.\n\nDoctrine — invariants enforced in this module:\n\n* **CANDIDATE only.** ``bridge_to_memory_candidate`` calls\n  ``app.services.memory.candidate_pipeline``; that pipeline\n  filters DANGEROUS / EPHEMERAL, pins ``brokerage_id`` from the\n  argument, sanitises evidence, and forces\n  ``MemoryStatus.CANDIDATE``. PAS182 never creates APPROVED.\n* **Eligibility gate.** ``evaluate_bridge_eligibility`` returns\n  the 8 closed conditions; ALL must be true for the bridge to\n  proceed. Any failed condition surfaces a structural\n  ``reason_code``.\n* **NEVER raises.** Every public function collapses to a\n  structural envelope.\n* **No LLM. No embeddings. No vector DB. No live behaviour\n  mutation.** PAS182 never imports the outbound FSM, Memory\n  Review UI, booking engine, Slack core, or worker.\n* **Closed payload allow-list.** ``ALLOWED_BRIDGE_KEYS``\n  matches the PAS182 spec — nothing else leaks out.\n\nPublic surface:\n\n  * ``LOW_RISK_THRESHOLD``                       — float, default 0.3\n  * ``HIGH_CONFIDENCE_THRESHOLD``                — float, default 0.7\n  * ``ALLOWED_BRIDGE_REASON_CODES``              — closed enum\n  * ``ALLOWED_BRIDGE_KEYS``                      — payload allow-list\n  * ``evaluate_bridge_eligibility(...)``         — pure verdict\n  * ``bridge_to_memory_candidate(...)``          — CANDIDATE-only\n  * ``adaptive_memory_bridge_report(...)``       — bounded read\n")
               STORE_NAME               1 (__doc__)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              5 (datetime)
               IMPORT_FROM              5 (datetime)
               STORE_NAME               5 (datetime)
               IMPORT_FROM              6 (timezone)
               STORE_NAME               6 (timezone)
               POP_TOP

  50           LOAD_SMALL_INT           0
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

  53           LOAD_NAME                4 (logging)
               LOAD_ATTR               26 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.learning.adaptive_memory_bridge')
               CALL                     1
               STORE_NAME              14 (logger)

  63           LOAD_CONST               6 (0.3)
               STORE_NAME              15 (LOW_RISK_THRESHOLD)
               LOAD_CONST               7 ('float')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST               8 ('LOW_RISK_THRESHOLD')
               STORE_SUBSCR

  64           LOAD_CONST               9 (0.7)
               STORE_NAME              17 (HIGH_CONFIDENCE_THRESHOLD)
               LOAD_CONST               7 ('float')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              10 ('HIGH_CONFIDENCE_THRESHOLD')
               STORE_SUBSCR

  68           LOAD_CONST              71 (('eligible', 'recommendation_not_found', 'recommendation_not_approved_for_manual_test', 'test_run_not_found', 'test_run_not_completed', 'test_run_mode_not_simulation', 'test_run_risk_too_high', 'test_run_confidence_too_low', 'test_run_evidence_fingerprint_missing', 'guardrail_forbidden_field_present', 'store_unavailable', 'memory_candidate_pipeline_unavailable', 'missing_storage_helper', 'invalid_actor_type', 'invalid_actor_id', 'invalid_test_run_id', 'cross_brokerage_lookup', 'bridge_rejected_by_operator', 'candidate_created', 'candidate_skipped', 'candidate_failed'))
               STORE_NAME              18 (ALLOWED_BRIDGE_REASON_CODES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              13 ('ALLOWED_BRIDGE_REASON_CODES')
               STORE_SUBSCR

  94           LOAD_CONST              72 (('brokerage_id', 'recommendation_id', 'test_run_id', 'memory_candidate_id', 'status', 'risk_score', 'confidence_score', 'warning_count', 'error_code', 'actor_type', 'actor_id'))
               STORE_NAME              19 (ALLOWED_BRIDGE_KEYS)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              24 ('ALLOWED_BRIDGE_KEYS')
               STORE_SUBSCR

 110           LOAD_CONST              73 (('OPERATOR', 'ADMIN'))
               STORE_NAME              20 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              25 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

 114           LOAD_CONST              26 ('APPROVED_FOR_MANUAL_TEST')
               STORE_NAME              21 (_ELIGIBLE_RECOMMENDATION_STATUS)
               LOAD_CONST              27 ('str')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              28 ('_ELIGIBLE_RECOMMENDATION_STATUS')
               STORE_SUBSCR

 115           LOAD_CONST              29 ('COMPLETED')
               STORE_NAME              22 (_ELIGIBLE_TEST_RUN_STATUS)
               LOAD_CONST              27 ('str')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              30 ('_ELIGIBLE_TEST_RUN_STATUS')
               STORE_SUBSCR

 116           LOAD_CONST              74 (('SIMULATION_ONLY', 'OBSERVATIONAL_ONLY'))
               STORE_NAME              23 (_ELIGIBLE_TEST_RUN_MODES)
               LOAD_CONST              12 ('Tuple[str, ...]')
               LOAD_NAME               16 (__annotations__)
               LOAD_CONST              31 ('_ELIGIBLE_TEST_RUN_MODES')
               STORE_SUBSCR

 123           LOAD_SMALL_INT         200
               STORE_NAME              24 (_BROKERAGE_ID_MAX_LEN)

 124           LOAD_SMALL_INT         200
               STORE_NAME              25 (_ACTOR_ID_MAX_LEN)

 125           LOAD_SMALL_INT         200
               STORE_NAME              26 (_TEST_RUN_ID_MAX_LEN)

 126           LOAD_SMALL_INT         200
               STORE_NAME              27 (_RECOMMENDATION_ID_MAX_LEN)

 127           LOAD_CONST              32 (500)
               STORE_NAME              28 (_LIST_HARD_CAP)

 128           LOAD_SMALL_INT          50
               STORE_NAME              29 (_DEFAULT_LIMIT)

 131           LOAD_CONST              33 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 130           STORE_NAME              30 (_ALLOWED_TOKEN_CHARS)

 141           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/adaptive_memory_bridge.py", line 141>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _now_iso at 0x0000018C18038CB0, file "app/services/learning/adaptive_memory_bridge.py", line 141>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now_iso)

 145           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/adaptive_memory_bridge.py", line 145>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object _bound_id at 0x0000018C17FA92F0, file "app/services/learning/adaptive_memory_bridge.py", line 145>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_bound_id)

 157           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/adaptive_memory_bridge.py", line 157>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/adaptive_memory_bridge.py", line 157>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_bound_brokerage_id)

 166           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/adaptive_memory_bridge.py", line 166>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object _clamp_limit at 0x0000018C17972D90, file "app/services/learning/adaptive_memory_bridge.py", line 166>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_clamp_limit)

 178           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/learning/adaptive_memory_bridge.py", line 178>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _safe_float at 0x0000018C17C49B80, file "app/services/learning/adaptive_memory_bridge.py", line 178>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_safe_float)

 187           LOAD_CONST              14 ('brokerage_id')

 190           LOAD_CONST               2 (None)

 187           LOAD_CONST              15 ('recommendation_id')

 191           LOAD_CONST               2 (None)

 187           LOAD_CONST              16 ('test_run_id')

 192           LOAD_CONST               2 (None)

 187           LOAD_CONST              17 ('memory_candidate_id')

 193           LOAD_CONST               2 (None)

 187           LOAD_CONST              11 ('eligible')

 194           LOAD_CONST               2 (None)

 187           LOAD_CONST              44 ('reason_code')

 195           LOAD_CONST               2 (None)

 187           LOAD_CONST              18 ('risk_score')

 196           LOAD_CONST               2 (None)

 187           LOAD_CONST              19 ('confidence_score')

 197           LOAD_CONST               2 (None)

 187           LOAD_CONST              20 ('warning_count')

 198           LOAD_SMALL_INT           0

 187           LOAD_CONST              21 ('error_code')

 199           LOAD_CONST               2 (None)

 187           LOAD_CONST              22 ('actor_type')

 200           LOAD_CONST               2 (None)

 187           LOAD_CONST              23 ('actor_id')

 201           LOAD_CONST               2 (None)

 187           LOAD_CONST              45 ('evidence_fingerprint')

 202           LOAD_CONST               2 (None)

 187           LOAD_CONST              46 ('warnings')

 203           LOAD_CONST               2 (None)

 187           BUILD_MAP               14
               LOAD_CONST              47 (<code object __annotate__ at 0x0000018C1802C4F0, file "app/services/learning/adaptive_memory_bridge.py", line 187>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _bridge_envelope at 0x0000018C1796DBD0, file "app/services/learning/adaptive_memory_bridge.py", line 187>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (_bridge_envelope)

 228           LOAD_CONST              49 (<code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/learning/adaptive_memory_bridge.py", line 228>)
               MAKE_FUNCTION
               STORE_NAME              37 (_get_db_safe)

 240           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18024930, file "app/services/learning/adaptive_memory_bridge.py", line 240>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _lookup_test_run at 0x0000018C17D76C00, file "app/services/learning/adaptive_memory_bridge.py", line 240>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_lookup_test_run)

 260           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18025930, file "app/services/learning/adaptive_memory_bridge.py", line 260>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _lookup_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/adaptive_memory_bridge.py", line 260>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_lookup_recommendation)

 287           LOAD_CONST              54 ('audit_status')

 294           LOAD_CONST              55 ('SUCCESS')

 287           LOAD_CONST              21 ('error_code')

 295           LOAD_CONST               2 (None)

 287           LOAD_CONST              56 ('event')

 296           LOAD_CONST              57 ('learning.adaptive_memory.bridge_event')

 287           LOAD_CONST              20 ('warning_count')

 297           LOAD_SMALL_INT           0

 287           BUILD_MAP                4
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18090690, file "app/services/learning/adaptive_memory_bridge.py", line 287>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _audit at 0x0000018C1804CD30, file "app/services/learning/adaptive_memory_bridge.py", line 287>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_audit)

 327           LOAD_CONST              14 ('brokerage_id')

 330           LOAD_CONST               2 (None)

 327           BUILD_MAP                1
               LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/adaptive_memory_bridge.py", line 327>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object evaluate_bridge_eligibility at 0x0000018C17ED8060, file "app/services/learning/adaptive_memory_bridge.py", line 327>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (evaluate_bridge_eligibility)

 553           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18025A30, file "app/services/learning/adaptive_memory_bridge.py", line 553>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object _build_candidate_bundle at 0x0000018C17F78410, file "app/services/learning/adaptive_memory_bridge.py", line 553>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_build_candidate_bundle)

 584           LOAD_CONST              14 ('brokerage_id')

 587           LOAD_CONST               2 (None)

 584           LOAD_CONST              23 ('actor_id')

 589           LOAD_CONST               2 (None)

 584           LOAD_CONST              64 ('confirm')

 590           LOAD_CONST              65 (False)

 584           BUILD_MAP                3
               LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/adaptive_memory_bridge.py", line 584>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object bridge_to_memory_candidate at 0x0000018C17F7AF50, file "app/services/learning/adaptive_memory_bridge.py", line 584>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (bridge_to_memory_candidate)

 955           LOAD_CONST              14 ('brokerage_id')

 957           LOAD_CONST               2 (None)

 955           LOAD_CONST              68 ('limit')

 958           LOAD_NAME               29 (_DEFAULT_LIMIT)

 955           BUILD_MAP                2
               LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18025730, file "app/services/learning/adaptive_memory_bridge.py", line 955>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object adaptive_memory_bridge_report at 0x0000018C17F7C5E0, file "app/services/learning/adaptive_memory_bridge.py", line 955>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (adaptive_memory_bridge_report)

1061           BUILD_LIST               0
               LOAD_CONST              75 (('LOW_RISK_THRESHOLD', 'HIGH_CONFIDENCE_THRESHOLD', 'ALLOWED_BRIDGE_REASON_CODES', 'ALLOWED_BRIDGE_KEYS', 'ALLOWED_ACTOR_TYPES', 'evaluate_bridge_eligibility', 'bridge_to_memory_candidate', 'adaptive_memory_bridge_report'))
               LIST_EXTEND              1
               STORE_NAME              45 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/learning/adaptive_memory_bridge.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "app/services/learning/adaptive_memory_bridge.py", line 141>:
141           RESUME                   0

142           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/learning/adaptive_memory_bridge.py", line 145>:
145           RESUME                   0
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

Disassembly of <code object _bound_id at 0x0000018C17FA92F0, file "app/services/learning/adaptive_memory_bridge.py", line 145>:
145           RESUME                   0

146           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

147           LOAD_CONST               0 (None)
              RETURN_VALUE

148   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

149           LOAD_FAST_BORROW         2 (s)
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

150   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

151   L3:     LOAD_FAST_BORROW         2 (s)
              GET_ITER
      L4:     FOR_ITER                17 (to L6)
              STORE_FAST               3 (ch)

152           LOAD_FAST_BORROW         3 (ch)
              LOAD_GLOBAL              8 (_ALLOWED_TOKEN_CHARS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           16 (to L4)

153   L5:     POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

151   L6:     END_FOR
              POP_ITER

154           LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/adaptive_memory_bridge.py", line 157>:
157           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/adaptive_memory_bridge.py", line 157>:
157           RESUME                   0

158           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

159           LOAD_CONST               0 (None)
              RETURN_VALUE

160   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

161           LOAD_FAST_BORROW         1 (s)
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

162   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

163   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/learning/adaptive_memory_bridge.py", line 166>:
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17972D90, file "app/services/learning/adaptive_memory_bridge.py", line 166>:
 166           RESUME                   0

 167           NOP

 168   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 171   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 172           LOAD_SMALL_INT           1
               RETURN_VALUE

 173   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 174           LOAD_GLOBAL              8 (_LIST_HARD_CAP)
               RETURN_VALUE

 175   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 169           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 170           LOAD_GLOBAL              6 (_DEFAULT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 169   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/learning/adaptive_memory_bridge.py", line 178>:
178           RESUME                   0
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
              LOAD_CONST               4 ('Optional[float]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_float at 0x0000018C17C49B80, file "app/services/learning/adaptive_memory_bridge.py", line 178>:
 178           RESUME                   0

 179           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 180           LOAD_CONST               0 (None)
               RETURN_VALUE

 181   L1:     NOP

 182   L2:     LOAD_GLOBAL              1 (float + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
       L3:     RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 183           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 184   L5:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 183   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1802C4F0, file "app/services/learning/adaptive_memory_bridge.py", line 187>:
187           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

189           LOAD_CONST               2 ('str')

187           LOAD_CONST               3 ('brokerage_id')

190           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST               5 ('recommendation_id')

191           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST               6 ('test_run_id')

192           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST               7 ('memory_candidate_id')

193           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST               8 ('eligible')

194           LOAD_CONST               9 ('Optional[bool]')

187           LOAD_CONST              10 ('reason_code')

195           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST              11 ('risk_score')

196           LOAD_CONST              12 ('Optional[float]')

187           LOAD_CONST              13 ('confidence_score')

197           LOAD_CONST              12 ('Optional[float]')

187           LOAD_CONST              14 ('warning_count')

198           LOAD_CONST              15 ('int')

187           LOAD_CONST              16 ('error_code')

199           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST              17 ('actor_type')

200           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST              18 ('actor_id')

201           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST              19 ('evidence_fingerprint')

202           LOAD_CONST               4 ('Optional[str]')

187           LOAD_CONST              20 ('warnings')

203           LOAD_CONST              21 ('Optional[List[str]]')

187           LOAD_CONST              22 ('return')

204           LOAD_CONST              23 ('Dict[str, Any]')

187           BUILD_MAP               16
              RETURN_VALUE

Disassembly of <code object _bridge_envelope at 0x0000018C1796DBD0, file "app/services/learning/adaptive_memory_bridge.py", line 187>:
187           RESUME                   0

207           LOAD_FAST_BORROW         6 (reason_code)
              LOAD_GLOBAL              0 (ALLOWED_BRIDGE_REASON_CODES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST                6 (reason_code)
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 (None)
      L2:     STORE_FAST              15 (rc)

208           BUILD_MAP                0

209           LOAD_CONST               2 ('status')
              LOAD_FAST_BORROW         0 (status)

208           MAP_ADD                  1

210           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         1 (brokerage_id)

208           MAP_ADD                  1

211           LOAD_CONST               4 ('recommendation_id')
              LOAD_FAST_BORROW         2 (recommendation_id)

208           MAP_ADD                  1

212           LOAD_CONST               5 ('test_run_id')
              LOAD_FAST_BORROW         3 (test_run_id)

208           MAP_ADD                  1

213           LOAD_CONST               6 ('memory_candidate_id')
              LOAD_FAST_BORROW         4 (memory_candidate_id)

208           MAP_ADD                  1

214           LOAD_CONST               7 ('eligible')
              LOAD_FAST_BORROW         5 (eligible)

208           MAP_ADD                  1

215           LOAD_CONST               8 ('reason_code')
              LOAD_FAST_BORROW        15 (rc)

208           MAP_ADD                  1

216           LOAD_CONST               9 ('risk_score')
              LOAD_FAST_BORROW         7 (risk_score)

208           MAP_ADD                  1

217           LOAD_CONST              10 ('confidence_score')
              LOAD_FAST_BORROW         8 (confidence_score)

208           MAP_ADD                  1

218           LOAD_CONST              11 ('warning_count')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         9 (warning_count)
              CALL                     1

208           MAP_ADD                  1

219           LOAD_CONST              12 ('error_code')
              LOAD_FAST_BORROW        10 (error_code)

208           MAP_ADD                  1

220           LOAD_CONST              13 ('actor_type')
              LOAD_FAST_BORROW        11 (actor_type)

208           MAP_ADD                  1

221           LOAD_CONST              14 ('actor_id')
              LOAD_FAST_BORROW        12 (actor_id)

208           MAP_ADD                  1

222           LOAD_CONST              15 ('evidence_fingerprint')
              LOAD_FAST_BORROW        13 (evidence_fingerprint)

208           MAP_ADD                  1

223           LOAD_CONST              16 ('warnings')
              LOAD_GLOBAL              5 (list + NULL)
              LOAD_FAST               14 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L3:     CALL                     1

208           MAP_ADD                  1

224           LOAD_CONST              17 ('created_at')
              LOAD_GLOBAL              7 (_now_iso + NULL)
              CALL                     0

208           MAP_ADD                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF10B0, file "app/services/learning/adaptive_memory_bridge.py", line 228>:
 228           RESUME                   0

 229           NOP

 230   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 231           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 232           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 233   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 234           LOAD_CONST               2 ('adaptive_memory_bridge db client unavailable type=')

 235           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 234           BUILD_STRING             2

 233           CALL                     1
               POP_TOP

 237   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 232   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/learning/adaptive_memory_bridge.py", line 240>:
240           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('test_run_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[Dict[str, Any]]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _lookup_test_run at 0x0000018C17D76C00, file "app/services/learning/adaptive_memory_bridge.py", line 240>:
 240            RESUME                   0

 241            NOP

 242    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_manual_test_run',))
                IMPORT_NAME              0 (app.services.learning.manual_test_harness)
                IMPORT_FROM              1 (get_manual_test_run)
                STORE_FAST               2 (get_manual_test_run)
                POP_TOP

 245            LOAD_FAST_BORROW         2 (get_manual_test_run)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (test_run_id)
                LOAD_CONST               2 (('test_run_id',))
                CALL_KW                  1
                STORE_FAST               3 (env)

 246            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (env)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 247    L2:     LOAD_CONST               3 (None)
                RETURN_VALUE

 248    L3:     LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_CONST               5 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 249    L4:     LOAD_CONST               3 (None)
                RETURN_VALUE

 250    L5:     LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('test_run')
                CALL                     1
                STORE_FAST               4 (record)

 251            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (record)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (record)
        L6:     RETURN_VALUE
        L7:     LOAD_CONST               3 (None)
        L8:     RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 252            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L13)
                NOT_TAKEN
                STORE_FAST               5 (e)

 253   L10:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 254            LOAD_CONST               7 ('adaptive_memory_bridge lookup_test_run error type=')

 255            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 254            BUILD_STRING             2

 253            CALL                     1
                POP_TOP

 257   L11:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L12:     LOAD_CONST               3 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 252   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L3 to L4 -> L9 [0]
  L5 to L6 -> L9 [0]
  L7 to L8 -> L9 [0]
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/learning/adaptive_memory_bridge.py", line 260>:
260           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('db')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('recommendation_id')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[Dict[str, Any]]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _lookup_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/adaptive_memory_bridge.py", line 260>:
 260            RESUME                   0

 261            NOP

 263    L1:     LOAD_FAST_BORROW         0 (db)
                LOAD_ATTR                1 (table + NULL|self)
                LOAD_CONST               0 ('pas_learning_recommendations')
                CALL                     1

 264            LOAD_ATTR                3 (select + NULL|self)

 265            LOAD_CONST               1 ('recommendation_id, brokerage_id, recommendation_type, source_type, source_id, status, confidence_score, risk_score, usefulness_score, rationale_token, created_at, reviewed_at')

 264            CALL                     1

 270            LOAD_ATTR                5 (eq + NULL|self)
                LOAD_CONST               2 ('recommendation_id')
                LOAD_FAST_BORROW         1 (recommendation_id)
                CALL                     2

 271            LOAD_ATTR                7 (limit + NULL|self)
                LOAD_SMALL_INT           2
                CALL                     1

 272            LOAD_ATTR                9 (execute + NULL|self)
                CALL                     0

 262            STORE_FAST               2 (result)

 274            LOAD_GLOBAL             11 (list + NULL)
                LOAD_GLOBAL             13 (getattr + NULL)
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

 275            LOAD_FAST_BORROW         3 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L5:     NOT_TAKEN

 276            LOAD_CONST               4 (None)
                RETURN_VALUE

 277    L6:     LOAD_FAST_BORROW         3 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST               4 (row)

 278            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (row)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (row)
        L7:     RETURN_VALUE
        L8:     LOAD_CONST               4 (None)
        L9:     RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 279            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                STORE_FAST               5 (e)

 280   L11:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 281            LOAD_CONST               5 ('adaptive_memory_bridge lookup_recommendation error type=')

 282            LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 281            BUILD_STRING             2

 280            CALL                     1
                POP_TOP

 284   L12:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                LOAD_CONST               4 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 279   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18090690, file "app/services/learning/adaptive_memory_bridge.py", line 287>:
287           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('action')

289           LOAD_CONST               2 ('str')

287           LOAD_CONST               3 ('brokerage_id')

290           LOAD_CONST               4 ('Optional[str]')

287           LOAD_CONST               5 ('target_id')

291           LOAD_CONST               4 ('Optional[str]')

287           LOAD_CONST               6 ('actor_type')

292           LOAD_CONST               2 ('str')

287           LOAD_CONST               7 ('actor_id')

293           LOAD_CONST               4 ('Optional[str]')

287           LOAD_CONST               8 ('audit_status')

294           LOAD_CONST               2 ('str')

287           LOAD_CONST               9 ('error_code')

295           LOAD_CONST               4 ('Optional[str]')

287           LOAD_CONST              10 ('event')

296           LOAD_CONST               2 ('str')

287           LOAD_CONST              11 ('warning_count')

297           LOAD_CONST              12 ('int')

287           LOAD_CONST              13 ('return')

298           LOAD_CONST              14 ('Optional[Dict[str, Any]]')

287           BUILD_MAP               10
              RETURN_VALUE

Disassembly of <code object _audit at 0x0000018C1804CD30, file "app/services/learning/adaptive_memory_bridge.py", line 287>:
 287           RESUME                   0

 300           NOP

 301   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('log_operator_action',))
               IMPORT_NAME              0 (app.services.operator.audit_service)
               IMPORT_FROM              1 (log_operator_action)
               STORE_FAST               9 (log_operator_action)
               POP_TOP

 302           LOAD_FAST_BORROW         9 (log_operator_action)
               PUSH_NULL

 303           LOAD_FAST_BORROW         1 (brokerage_id)

 304           LOAD_FAST_BORROW         3 (actor_type)

 305           LOAD_FAST_BORROW         4 (actor_id)

 306           LOAD_FAST_BORROW         0 (action)

 307           LOAD_FAST_BORROW         5 (audit_status)

 308           LOAD_CONST               2 ('learning_adaptive_memory_bridge')

 309           LOAD_FAST_BORROW         2 (target_id)

 310           LOAD_FAST_BORROW         8 (warning_count)

 312           LOAD_CONST               3 ('event')
               LOAD_FAST_BORROW         7 (event)

 313           LOAD_CONST               4 ('error_code')
               LOAD_FAST_BORROW         6 (error_code)

 311           BUILD_MAP                2

 302           LOAD_CONST               5 (('brokerage_id', 'actor_type', 'actor_id', 'action', 'status', 'target_type', 'target_id', 'warning_count', 'metadata'))
               CALL_KW                  9
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 316           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST              10 (e)

 317   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 318           LOAD_CONST               6 ('adaptive_memory_bridge audit error type=')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST               10 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 317           CALL                     1
               POP_TOP

 320   L5:     POP_EXCEPT
               LOAD_CONST               7 (None)
               STORE_FAST              10 (e)
               DELETE_FAST             10 (e)
               LOAD_CONST               7 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               7 (None)
               STORE_FAST              10 (e)
               DELETE_FAST             10 (e)
               RERAISE                  1

 316   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/learning/adaptive_memory_bridge.py", line 327>:
327           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

329           LOAD_CONST               2 ('str')

327           LOAD_CONST               3 ('brokerage_id')

330           LOAD_CONST               4 ('Optional[str]')

327           LOAD_CONST               5 ('return')

331           LOAD_CONST               6 ('Dict[str, Any]')

327           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object evaluate_bridge_eligibility at 0x0000018C17ED8060, file "app/services/learning/adaptive_memory_bridge.py", line 327>:
 327            RESUME                   0

 351            LOAD_GLOBAL              1 (_bound_id + NULL)
                LOAD_FAST_BORROW         0 (test_run_id)
                LOAD_GLOBAL              2 (_TEST_RUN_ID_MAX_LEN)
                CALL                     2
                STORE_FAST               2 (trid)

 352            LOAD_FAST_BORROW         2 (trid)
                POP_JUMP_IF_NOT_NONE    16 (to L1)
                NOT_TAKEN

 353            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 354            LOAD_CONST               2 ('failed')

 355            LOAD_CONST               3 (False)

 356            LOAD_CONST               4 ('invalid_test_run_id')

 357            LOAD_CONST               4 ('invalid_test_run_id')

 353            LOAD_CONST               5 (('status', 'eligible', 'reason_code', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 359    L1:     LOAD_FAST_BORROW         1 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               3 (bid)

 361            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 362            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L4)
                NOT_TAKEN

 363            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 364            LOAD_CONST               6 ('skipped')

 365            LOAD_FAST_BORROW         3 (bid)

 366            LOAD_FAST_BORROW         2 (trid)

 367            LOAD_CONST               3 (False)

 368            LOAD_CONST               7 ('store_unavailable')

 369            LOAD_CONST               7 ('store_unavailable')

 370            LOAD_CONST               7 ('store_unavailable')
                BUILD_LIST               1

 363            LOAD_CONST               8 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'warnings'))
                CALL_KW                  7
                RETURN_VALUE

 373    L4:     LOAD_GLOBAL             11 (_lookup_test_run + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (db, trid)
                LOAD_CONST               9 (('test_run_id',))
                CALL_KW                  2
                STORE_FAST               5 (test_run)

 374            LOAD_FAST_BORROW         5 (test_run)
                POP_JUMP_IF_NOT_NONE    18 (to L5)
                NOT_TAKEN

 375            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 376            LOAD_CONST               2 ('failed')

 377            LOAD_FAST_BORROW         3 (bid)

 378            LOAD_FAST_BORROW         2 (trid)

 379            LOAD_CONST               3 (False)

 380            LOAD_CONST              10 ('test_run_not_found')

 381            LOAD_CONST              10 ('test_run_not_found')

 375            LOAD_CONST              11 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 384    L5:     LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                STORE_FAST               6 (run_bid)

 385            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NONE        46 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (run_bid)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (run_bid, bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN

 386            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 387            LOAD_CONST               2 ('failed')

 388            LOAD_FAST_BORROW         3 (bid)

 389            LOAD_FAST_BORROW         2 (trid)

 390            LOAD_CONST               3 (False)

 391            LOAD_CONST              13 ('cross_brokerage_lookup')

 392            LOAD_CONST              13 ('cross_brokerage_lookup')

 386            LOAD_CONST              11 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 395    L6:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (run_bid)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (run_bid)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_FAST                6 (run_bid)
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_FAST                3 (bid)

 394    L8:     STORE_FAST               7 (effective_bid)

 398            LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              14 ('status')
                CALL                     1
                STORE_FAST               8 (run_status)

 399            LOAD_FAST_BORROW         8 (run_status)
                LOAD_GLOBAL             20 (_ELIGIBLE_TEST_RUN_STATUS)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       23 (to L9)
                NOT_TAKEN

 400            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 401            LOAD_CONST               2 ('failed')

 402            LOAD_FAST_BORROW         7 (effective_bid)

 403            LOAD_FAST_BORROW         2 (trid)

 404            LOAD_CONST               3 (False)

 405            LOAD_CONST              15 ('test_run_not_completed')

 406            LOAD_CONST              15 ('test_run_not_completed')

 407            LOAD_CONST              16 ('test_run_status:')
                LOAD_FAST_BORROW         8 (run_status)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 400            LOAD_CONST               8 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'warnings'))
                CALL_KW                  7
                RETURN_VALUE

 410    L9:     LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              17 ('mode')
                CALL                     1
                STORE_FAST               9 (run_mode)

 411            LOAD_FAST_BORROW         9 (run_mode)
                LOAD_GLOBAL             22 (_ELIGIBLE_TEST_RUN_MODES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       23 (to L10)
                NOT_TAKEN

 412            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 413            LOAD_CONST               2 ('failed')

 414            LOAD_FAST_BORROW         7 (effective_bid)

 415            LOAD_FAST_BORROW         2 (trid)

 416            LOAD_CONST               3 (False)

 417            LOAD_CONST              18 ('test_run_mode_not_simulation')

 418            LOAD_CONST              18 ('test_run_mode_not_simulation')

 419            LOAD_CONST              19 ('test_run_mode:')
                LOAD_FAST_BORROW         9 (run_mode)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 412            LOAD_CONST               8 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'warnings'))
                CALL_KW                  7
                RETURN_VALUE

 422   L10:     LOAD_GLOBAL             25 (_safe_float + NULL)
                LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1
                CALL                     1
                STORE_FAST              10 (risk)

 423            LOAD_FAST_BORROW        10 (risk)
                POP_JUMP_IF_NONE        12 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW        10 (risk)
                LOAD_GLOBAL             26 (LOW_RISK_THRESHOLD)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       19 (to L12)
                NOT_TAKEN

 424   L11:     LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 425            LOAD_CONST               2 ('failed')

 426            LOAD_FAST_BORROW         7 (effective_bid)

 427            LOAD_FAST_BORROW         2 (trid)

 428            LOAD_CONST               3 (False)

 429            LOAD_CONST              21 ('test_run_risk_too_high')

 430            LOAD_CONST              21 ('test_run_risk_too_high')

 431            LOAD_FAST_BORROW        10 (risk)

 424            LOAD_CONST              22 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score'))
                CALL_KW                  7
                RETURN_VALUE

 434   L12:     LOAD_GLOBAL             25 (_safe_float + NULL)
                LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              23 ('confidence_score')
                CALL                     1
                CALL                     1
                STORE_FAST              11 (confidence)

 435            LOAD_FAST_BORROW        11 (confidence)
                POP_JUMP_IF_NONE        12 (to L13)
                NOT_TAKEN
                LOAD_FAST_BORROW        11 (confidence)
                LOAD_GLOBAL             28 (HIGH_CONFIDENCE_THRESHOLD)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       20 (to L14)
                NOT_TAKEN

 436   L13:     LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 437            LOAD_CONST               2 ('failed')

 438            LOAD_FAST_BORROW         7 (effective_bid)

 439            LOAD_FAST_BORROW         2 (trid)

 440            LOAD_CONST               3 (False)

 441            LOAD_CONST              24 ('test_run_confidence_too_low')

 442            LOAD_CONST              24 ('test_run_confidence_too_low')

 443            LOAD_FAST_BORROW        11 (confidence)

 444            LOAD_FAST_BORROW        10 (risk)

 436            LOAD_CONST              25 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'confidence_score', 'risk_score'))
                CALL_KW                  8
                RETURN_VALUE

 447   L14:     LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              26 ('evidence_fingerprint')
                CALL                     1
                STORE_FAST              12 (evidence_fp)

 448            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (evidence_fp)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW        12 (evidence_fp)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        20 (to L16)
                NOT_TAKEN

 449   L15:     LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 450            LOAD_CONST               2 ('failed')

 451            LOAD_FAST_BORROW         7 (effective_bid)

 452            LOAD_FAST_BORROW         2 (trid)

 453            LOAD_CONST               3 (False)

 454            LOAD_CONST              27 ('test_run_evidence_fingerprint_missing')

 455            LOAD_CONST              27 ('test_run_evidence_fingerprint_missing')

 456            LOAD_FAST_BORROW        10 (risk)

 457            LOAD_FAST_BORROW        11 (confidence)

 449            LOAD_CONST              28 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score'))
                CALL_KW                  8
                RETURN_VALUE

 460   L16:     LOAD_FAST_BORROW         5 (test_run)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              29 ('recommendation_id')
                CALL                     1
                STORE_FAST              13 (rid)

 461            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (rid)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (rid)
                LOAD_ATTR               19 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L18)
                NOT_TAKEN

 462   L17:     LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 463            LOAD_CONST               2 ('failed')

 464            LOAD_FAST_BORROW         7 (effective_bid)

 465            LOAD_FAST_BORROW         2 (trid)

 466            LOAD_CONST               3 (False)

 467            LOAD_CONST              30 ('recommendation_not_found')

 468            LOAD_CONST              30 ('recommendation_not_found')

 469            LOAD_FAST_BORROW        10 (risk)

 470            LOAD_FAST_BORROW        11 (confidence)

 471            LOAD_FAST_BORROW        12 (evidence_fp)

 462            LOAD_CONST              31 (('status', 'brokerage_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint'))
                CALL_KW                  9
                RETURN_VALUE

 474   L18:     LOAD_GLOBAL             31 (_lookup_recommendation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 77 (db, rid)
                LOAD_CONST              32 (('recommendation_id',))
                CALL_KW                  2
                STORE_FAST              14 (recommendation)

 475            LOAD_FAST_BORROW        14 (recommendation)
                POP_JUMP_IF_NOT_NONE    22 (to L19)
                NOT_TAKEN

 476            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 477            LOAD_CONST               2 ('failed')

 478            LOAD_FAST_BORROW         7 (effective_bid)

 479            LOAD_FAST_BORROW        13 (rid)

 480            LOAD_FAST_BORROW         2 (trid)

 481            LOAD_CONST               3 (False)

 482            LOAD_CONST              30 ('recommendation_not_found')

 483            LOAD_CONST              30 ('recommendation_not_found')

 484            LOAD_FAST_BORROW        10 (risk)

 485            LOAD_FAST_BORROW        11 (confidence)

 486            LOAD_FAST_BORROW        12 (evidence_fp)

 476            LOAD_CONST              33 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint'))
                CALL_KW                 10
                RETURN_VALUE

 489   L19:     LOAD_FAST_BORROW        14 (recommendation)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              14 ('status')
                CALL                     1
                LOAD_GLOBAL             32 (_ELIGIBLE_RECOMMENDATION_STATUS)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       22 (to L20)
                NOT_TAKEN

 490            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 491            LOAD_CONST               2 ('failed')

 492            LOAD_FAST_BORROW         7 (effective_bid)

 493            LOAD_FAST_BORROW        13 (rid)

 494            LOAD_FAST_BORROW         2 (trid)

 495            LOAD_CONST               3 (False)

 496            LOAD_CONST              34 ('recommendation_not_approved_for_manual_test')

 497            LOAD_CONST              34 ('recommendation_not_approved_for_manual_test')

 498            LOAD_FAST_BORROW        10 (risk)

 499            LOAD_FAST_BORROW        11 (confidence)

 500            LOAD_FAST_BORROW        12 (evidence_fp)

 490            LOAD_CONST              33 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint'))
                CALL_KW                 10
                RETURN_VALUE

 507   L20:     NOP

 508   L21:     LOAD_SMALL_INT           0
                LOAD_CONST              35 (('learning_forbidden_field_scan',))
                IMPORT_NAME             17 (app.services.learning.guardrails)
                IMPORT_FROM             18 (learning_forbidden_field_scan)
                STORE_FAST              15 (learning_forbidden_field_scan)
                POP_TOP

 511            LOAD_FAST_BORROW        15 (learning_forbidden_field_scan)
                PUSH_NULL

 512            LOAD_CONST              36 ('test_run')
                LOAD_FAST_BORROW         5 (test_run)

 513            LOAD_CONST              37 ('recommendation')
                LOAD_FAST_BORROW        14 (recommendation)

 511            BUILD_MAP                2
                CALL                     1
                STORE_FAST              16 (scan)

 522   L22:     LOAD_FAST_BORROW        16 (scan)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              39 ('valid')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        22 (to L23)
                NOT_TAKEN

 523            LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 524            LOAD_CONST               2 ('failed')

 525            LOAD_FAST_BORROW         7 (effective_bid)

 526            LOAD_FAST_BORROW        13 (rid)

 527            LOAD_FAST_BORROW         2 (trid)

 528            LOAD_CONST               3 (False)

 529            LOAD_CONST              41 ('guardrail_forbidden_field_present')

 530            LOAD_CONST              41 ('guardrail_forbidden_field_present')

 531            LOAD_FAST_BORROW        10 (risk)

 532            LOAD_FAST_BORROW        11 (confidence)

 533            LOAD_FAST_BORROW        12 (evidence_fp)

 523            LOAD_CONST              33 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint'))
                CALL_KW                 10
                RETURN_VALUE

 536   L23:     LOAD_GLOBAL              5 (_bridge_envelope + NULL)

 537            LOAD_CONST              42 ('ok')

 538            LOAD_FAST_BORROW         7 (effective_bid)

 539            LOAD_FAST_BORROW        13 (rid)

 540            LOAD_FAST_BORROW         2 (trid)

 541            LOAD_CONST              40 (True)

 542            LOAD_CONST              43 ('eligible')

 543            LOAD_FAST_BORROW        10 (risk)

 544            LOAD_FAST_BORROW        11 (confidence)

 545            LOAD_FAST_BORROW        12 (evidence_fp)

 536            LOAD_CONST              44 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'risk_score', 'confidence_score', 'evidence_fingerprint'))
                CALL_KW                  9
                RETURN_VALUE

  --   L24:     PUSH_EXC_INFO

 515            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       58 (to L28)
                NOT_TAKEN
                STORE_FAST              17 (e)

 516   L25:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 517            LOAD_CONST              38 ('evaluate_bridge_eligibility guardrail import error type=')

 518            LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 517            BUILD_STRING             2

 516            CALL                     1
                POP_TOP

 520            LOAD_CONST              39 ('valid')
                LOAD_CONST              40 (True)
                BUILD_MAP                1
                STORE_FAST              16 (scan)
       L26:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                JUMP_BACKWARD_NO_INTERRUPT 127 (to L22)

  --   L27:     LOAD_CONST               1 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 515   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L21 to L22 -> L24 [0]
  L24 to L25 -> L29 [1] lasti
  L25 to L26 -> L27 [1] lasti
  L27 to L29 -> L29 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app/services/learning/adaptive_memory_bridge.py", line 553>:
553           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

555           LOAD_CONST               2 ('str')

553           LOAD_CONST               3 ('recommendation')

556           LOAD_CONST               4 ('Dict[str, Any]')

553           LOAD_CONST               5 ('test_run')

557           LOAD_CONST               4 ('Dict[str, Any]')

553           LOAD_CONST               6 ('evidence_fingerprint')

558           LOAD_CONST               2 ('str')

553           LOAD_CONST               7 ('return')

559           LOAD_CONST               4 ('Dict[str, Any]')

553           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _build_candidate_bundle at 0x0000018C17F78410, file "app/services/learning/adaptive_memory_bridge.py", line 553>:
553           RESUME                   0

566           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)

567           LOAD_CONST               2 ('source_kind')
              LOAD_CONST               3 ('PAS182_BRIDGE')

568           LOAD_CONST               4 ('source_type')
              LOAD_CONST               5 ('MANUAL_TEST_RUN')

569           LOAD_CONST               6 ('test_run_id')
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('test_run_id')
              CALL                     1

570           LOAD_CONST               7 ('recommendation_id')
              LOAD_FAST_BORROW         1 (recommendation)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('recommendation_id')
              CALL                     1

571           LOAD_CONST               8 ('recommendation_type')
              LOAD_FAST_BORROW         1 (recommendation)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('recommendation_type')
              CALL                     1

572           LOAD_CONST               9 ('scenario_type')
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('scenario_type')
              CALL                     1

573           LOAD_CONST              10 ('mode')
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('mode')
              CALL                     1

574           LOAD_CONST              11 ('final_outcome')
              LOAD_CONST              12 ('manual_test_completed')

575           LOAD_CONST              13 ('evidence_fingerprint')
              LOAD_FAST_BORROW         3 (evidence_fingerprint)

576           LOAD_CONST              14 ('rationale_token')
              LOAD_FAST_BORROW         1 (recommendation)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              14 ('rationale_token')
              CALL                     1

577           LOAD_CONST              15 ('confidence_hint')
              LOAD_GLOBAL              3 (_safe_float + NULL)
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              16 ('confidence_score')
              CALL                     1
              CALL                     1

578           LOAD_CONST              17 ('risk_hint')
              LOAD_GLOBAL              3 (_safe_float + NULL)
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              18 ('risk_score')
              CALL                     1
              CALL                     1

579           LOAD_CONST              19 ('score_hint')
              LOAD_GLOBAL              3 (_safe_float + NULL)
              LOAD_FAST_BORROW         2 (test_run)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              20 ('score')
              CALL                     1
              CALL                     1

580           LOAD_CONST              21 ('missing_lifecycle_steps')
              BUILD_LIST               0

565           BUILD_MAP               15
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/learning/adaptive_memory_bridge.py", line 584>:
584           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('test_run_id')

586           LOAD_CONST               2 ('str')

584           LOAD_CONST               3 ('brokerage_id')

587           LOAD_CONST               4 ('Optional[str]')

584           LOAD_CONST               5 ('actor_type')

588           LOAD_CONST               2 ('str')

584           LOAD_CONST               6 ('actor_id')

589           LOAD_CONST               4 ('Optional[str]')

584           LOAD_CONST               7 ('confirm')

590           LOAD_CONST               8 ('bool')

584           LOAD_CONST               9 ('return')

591           LOAD_CONST              10 ('Dict[str, Any]')

584           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object bridge_to_memory_candidate at 0x0000018C17F7AF50, file "app/services/learning/adaptive_memory_bridge.py", line 584>:
 584            RESUME                   0

 609            LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              0 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       46 (to L2)
                NOT_TAKEN

 610            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 611            LOAD_CONST               1 ('failed')

 612            LOAD_CONST               2 (False)

 613            LOAD_CONST               3 ('invalid_actor_type')

 614            LOAD_CONST               3 ('invalid_actor_type')

 615            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (actor_type)

 610            LOAD_CONST               5 (('status', 'eligible', 'reason_code', 'error_code', 'actor_type'))
                CALL_KW                  5
                RETURN_VALUE

 615    L1:     LOAD_CONST               4 (None)

 610            LOAD_CONST               5 (('status', 'eligible', 'reason_code', 'error_code', 'actor_type'))
                CALL_KW                  5
                RETURN_VALUE

 617    L2:     LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        17 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              9 (_bound_id + NULL)
                LOAD_FAST_BORROW         3 (actor_id)
                LOAD_GLOBAL             10 (_ACTOR_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               4 (None)
        L4:     STORE_FAST               5 (actor)

 618            LOAD_FAST_BORROW         3 (actor_id)
                POP_JUMP_IF_NONE        21 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (actor)
                POP_JUMP_IF_NOT_NONE    17 (to L5)
                NOT_TAKEN

 619            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 620            LOAD_CONST               1 ('failed')

 621            LOAD_CONST               2 (False)

 622            LOAD_CONST               6 ('invalid_actor_id')

 623            LOAD_CONST               6 ('invalid_actor_id')

 624            LOAD_FAST_BORROW         2 (actor_type)

 619            LOAD_CONST               5 (('status', 'eligible', 'reason_code', 'error_code', 'actor_type'))
                CALL_KW                  5
                RETURN_VALUE

 627    L5:     LOAD_GLOBAL             13 (evaluate_bridge_eligibility + NULL)

 628            LOAD_FAST_BORROW         0 (test_run_id)

 629            LOAD_FAST_BORROW         1 (brokerage_id)

 627            LOAD_CONST               7 (('test_run_id', 'brokerage_id'))
                CALL_KW                  2
                STORE_FAST               6 (eligibility)

 631            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                LOAD_CONST               9 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        25 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('eligible')
                CALL                     1
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_TRUE       270 (to L9)
                NOT_TAKEN

 633    L6:     LOAD_GLOBAL             17 (_audit + NULL)

 634            LOAD_CONST              11 ('adaptive_memory_bridge_rejected')

 635            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1

 636            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1

 637            LOAD_FAST_BORROW         2 (actor_type)

 638            LOAD_FAST_BORROW         5 (actor)

 639            LOAD_CONST              14 ('FAILED')

 640            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('error_code')
                CALL                     1

 641            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 642            LOAD_SMALL_INT           1

 633            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 644            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 645            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('failed')

 646    L7:     LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1

 647            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('recommendation_id')
                CALL                     1

 648            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1

 649            LOAD_CONST               2 (False)

 650            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              19 ('reason_code')
                CALL                     1

 651            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('error_code')
                CALL                     1

 652            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 653            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 654            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 655            LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              23 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1

 656            LOAD_FAST_BORROW         2 (actor_type)

 657            LOAD_FAST_BORROW         5 (actor)

 658            LOAD_SMALL_INT           1

 644            LOAD_CONST              24 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'warnings', 'actor_type', 'actor_id', 'warning_count'))
                CALL_KW                 14
                RETURN_VALUE

 661    L9:     LOAD_GLOBAL             21 (bool + NULL)
                LOAD_FAST_BORROW         4 (confirm)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE       165 (to L10)
                NOT_TAKEN

 662            LOAD_GLOBAL             17 (_audit + NULL)

 663            LOAD_CONST              11 ('adaptive_memory_bridge_rejected')

 664            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1

 665            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1

 666            LOAD_FAST_BORROW         2 (actor_type)

 667            LOAD_FAST_BORROW         5 (actor)

 668            LOAD_CONST              14 ('FAILED')

 669            LOAD_CONST              25 ('bridge_rejected_by_operator')

 670            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 671            LOAD_SMALL_INT           1

 662            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 673            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 674            LOAD_CONST               1 ('failed')

 675            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1

 676            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('recommendation_id')
                CALL                     1

 677            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1

 678            LOAD_CONST              26 (True)

 679            LOAD_CONST              25 ('bridge_rejected_by_operator')

 680            LOAD_CONST              25 ('bridge_rejected_by_operator')

 681            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 682            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 683            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 684            LOAD_FAST_BORROW         2 (actor_type)

 685            LOAD_FAST_BORROW         5 (actor)

 686            LOAD_SMALL_INT           1

 673            LOAD_CONST              27 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warning_count'))
                CALL_KW                 13
                RETURN_VALUE

 690   L10:     LOAD_GLOBAL             23 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 691            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE   117 (to L11)
                NOT_TAKEN

 692            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 693            LOAD_CONST              28 ('skipped')

 694            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1

 695            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('recommendation_id')
                CALL                     1

 696            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1

 697            LOAD_CONST              26 (True)

 698            LOAD_CONST              29 ('store_unavailable')

 699            LOAD_CONST              29 ('store_unavailable')

 700            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 701            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 702            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 703            LOAD_FAST_BORROW         2 (actor_type)

 704            LOAD_FAST_BORROW         5 (actor)

 705            LOAD_CONST              29 ('store_unavailable')
                BUILD_LIST               1

 706            LOAD_SMALL_INT           1

 692            LOAD_CONST              30 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings', 'warning_count'))
                CALL_KW                 14
                RETURN_VALUE

 709   L11:     LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('recommendation_id')
                CALL                     1
                STORE_FAST               8 (rid)

 710            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              13 ('test_run_id')
                CALL                     1
                STORE_FAST               9 (trid)

 711            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                STORE_FAST              10 (bid)

 712            LOAD_GLOBAL             25 (_lookup_test_run + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 121 (db, trid)
                LOAD_CONST              31 (('test_run_id',))
                CALL_KW                  2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L12:     STORE_FAST              11 (test_run)

 714            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (rid)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L13)
                NOT_TAKEN
                LOAD_GLOBAL             27 (_lookup_recommendation + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (db, rid)
                LOAD_CONST              32 (('recommendation_id',))
                CALL_KW                  2
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               4 (None)

 713   L14:     COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP

 715            BUILD_MAP                0

 713   L15:     STORE_FAST              12 (recommendation)

 717            LOAD_GLOBAL             29 (_build_candidate_bundle + NULL)

 718            LOAD_FAST               10 (bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('')

 719   L16:     LOAD_FAST               12 (recommendation)

 720            LOAD_FAST               11 (test_run)

 721            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('')

 717   L17:     LOAD_CONST              34 (('brokerage_id', 'recommendation', 'test_run', 'evidence_fingerprint'))
                CALL_KW                  4
                STORE_FAST              13 (bundle)

 726            NOP

 727   L18:     LOAD_SMALL_INT           0
                LOAD_CONST              35 (('learning_forbidden_field_scan',))
                IMPORT_NAME             15 (app.services.learning.guardrails)
                IMPORT_FROM             16 (learning_forbidden_field_scan)
                STORE_FAST              14 (learning_forbidden_field_scan)
                POP_TOP

 730            LOAD_FAST_BORROW        14 (learning_forbidden_field_scan)
                PUSH_NULL
                LOAD_FAST_BORROW        13 (bundle)
                CALL                     1
                STORE_FAST              15 (scan)

 733   L19:     LOAD_FAST_BORROW        15 (scan)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              36 ('valid')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        90 (to L20)
                NOT_TAKEN

 734            LOAD_GLOBAL             17 (_audit + NULL)

 735            LOAD_CONST              11 ('adaptive_memory_bridge_rejected')

 736            LOAD_FAST_BORROW        10 (bid)

 737            LOAD_FAST_BORROW         9 (trid)

 738            LOAD_FAST_BORROW         2 (actor_type)

 739            LOAD_FAST_BORROW         5 (actor)

 740            LOAD_CONST              14 ('FAILED')

 741            LOAD_CONST              37 ('guardrail_forbidden_field_present')

 742            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 743            LOAD_SMALL_INT           1

 734            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 745            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 746            LOAD_CONST               1 ('failed')

 747            LOAD_FAST_BORROW        10 (bid)

 748            LOAD_FAST_BORROW         8 (rid)

 749            LOAD_FAST_BORROW         9 (trid)

 750            LOAD_CONST              26 (True)

 751            LOAD_CONST              37 ('guardrail_forbidden_field_present')

 752            LOAD_CONST              37 ('guardrail_forbidden_field_present')

 753            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 754            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 755            LOAD_FAST_BORROW         6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 756            LOAD_FAST_BORROW         2 (actor_type)

 757            LOAD_FAST_BORROW         5 (actor)

 758            LOAD_SMALL_INT           1

 745            LOAD_CONST              27 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warning_count'))
                CALL_KW                 13
                RETURN_VALUE

 762   L20:     NOP

 763   L21:     LOAD_SMALL_INT           0
                LOAD_CONST              38 (('generate_memory_candidates_from_replay',))
                IMPORT_NAME             18 (app.services.memory.candidate_pipeline)
                IMPORT_FROM             19 (generate_memory_candidates_from_replay)
                STORE_FAST              16 (generate_memory_candidates_from_replay)
                POP_TOP

 799   L22:     LOAD_FAST               16 (generate_memory_candidates_from_replay)
                PUSH_NULL

 800            LOAD_FAST               13 (bundle)

 801            LOAD_FAST               10 (bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              33 ('')

 802   L23:     LOAD_CONST              42 ('SYSTEM')

 803            LOAD_CONST              43 ('pas182_bridge:')
                LOAD_FAST                5 (actor)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              44 ('unknown')
       L24:     FORMAT_SIMPLE
                BUILD_STRING             2

 799            LOAD_CONST              45 (('brokerage_id', 'actor_type', 'actor_id'))
                CALL_KW                  4
                STORE_FAST              18 (report)

 805            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST               18 (report)
                LOAD_GLOBAL             48 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
                NOT_TAKEN

 806            BUILD_MAP                0
                STORE_FAST              18 (report)

 808   L25:     LOAD_FAST               18 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('failed')
       L26:     STORE_FAST              19 (rep_status)

 809            LOAD_GLOBAL             51 (int + NULL)
                LOAD_FAST               18 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              46 ('candidates_created')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L27:     CALL                     1
                STORE_FAST              20 (created)

 810            LOAD_GLOBAL             51 (int + NULL)
                LOAD_FAST               18 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               1 ('failed')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L28)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L28:     CALL                     1
                STORE_FAST              21 (failed)

 811            LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST               18 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              23 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L29)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L29:     CALL                     1
                STORE_FAST              22 (rep_warnings)

 812            LOAD_GLOBAL             19 (list + NULL)
                LOAD_FAST               18 (report)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              47 ('results')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L30:     CALL                     1
                STORE_FAST              23 (results)

 814            LOAD_CONST               4 (None)
                STORE_FAST              24 (memory_candidate_id)

 815            LOAD_FAST               23 (results)
                TO_BOOL
                POP_JUMP_IF_FALSE      109 (to L31)
                NOT_TAKEN

 816            LOAD_FAST               23 (results)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              25 (first)

 817            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST               25 (first)
                LOAD_GLOBAL             48 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L31)
                NOT_TAKEN

 818            LOAD_FAST               25 (first)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              48 ('memory_id')
                CALL                     1
                STORE_FAST              26 (mid)

 819            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST               26 (mid)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L31)
                NOT_TAKEN
                LOAD_FAST               26 (mid)
                LOAD_ATTR               53 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L31)
                NOT_TAKEN

 820            LOAD_FAST               26 (mid)
                LOAD_ATTR               53 (strip + NULL|self)
                CALL                     0
                STORE_FAST              24 (memory_candidate_id)

 823   L31:     LOAD_FAST               19 (rep_status)
                LOAD_CONST              28 ('skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      116 (to L34)
                NOT_TAKEN

 824            LOAD_CONST              49 ('missing_storage_helper')
                LOAD_FAST               22 (rep_warnings)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         8 (to L32)
                NOT_TAKEN
                LOAD_FAST               20 (created)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      102 (to L34)
                NOT_TAKEN

 826   L32:     LOAD_GLOBAL             17 (_audit + NULL)

 827            LOAD_CONST              50 ('adaptive_memory_bridge_skipped')

 828            LOAD_FAST               10 (bid)

 829            LOAD_FAST                9 (trid)

 830            LOAD_FAST                2 (actor_type)

 831            LOAD_FAST                5 (actor)

 832            LOAD_CONST              14 ('FAILED')

 833            LOAD_CONST              49 ('missing_storage_helper')

 834            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 835            LOAD_SMALL_INT           1

 826            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 837            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 838            LOAD_CONST              28 ('skipped')

 839            LOAD_FAST               10 (bid)

 840            LOAD_FAST                8 (rid)

 841            LOAD_FAST                9 (trid)

 842            LOAD_CONST              26 (True)

 843            LOAD_CONST              49 ('missing_storage_helper')

 844            LOAD_CONST              49 ('missing_storage_helper')

 845            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 846            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 847            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 848            LOAD_FAST                2 (actor_type)

 849            LOAD_FAST                5 (actor)

 850            LOAD_FAST               22 (rep_warnings)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         4 (to L33)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              49 ('missing_storage_helper')
                BUILD_LIST               1

 851   L33:     LOAD_SMALL_INT           1

 837            LOAD_CONST              30 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings', 'warning_count'))
                CALL_KW                 14
                RETURN_VALUE

 854   L34:     LOAD_FAST               19 (rep_status)
                LOAD_CONST               9 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      125 (to L36)
                NOT_TAKEN
                LOAD_FAST               20 (created)
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE      118 (to L36)
                NOT_TAKEN

 855            LOAD_GLOBAL             17 (_audit + NULL)

 856            LOAD_CONST              51 ('adaptive_memory_bridge_confirmed')

 857            LOAD_FAST               10 (bid)

 858            LOAD_FAST                9 (trid)

 859            LOAD_FAST                2 (actor_type)

 860            LOAD_FAST                5 (actor)

 861            LOAD_CONST              52 ('SUCCESS')

 862            LOAD_CONST              53 ('learning.adaptive_memory.bridge_confirmed')

 863            LOAD_SMALL_INT           0

 855            LOAD_CONST              54 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'event', 'warning_count'))
                CALL_KW                  8
                POP_TOP

 865            LOAD_GLOBAL             17 (_audit + NULL)

 866            LOAD_CONST              55 ('adaptive_memory_candidate_created')

 867            LOAD_FAST               10 (bid)

 868            LOAD_FAST               24 (memory_candidate_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L35)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                9 (trid)

 869   L35:     LOAD_FAST                2 (actor_type)

 870            LOAD_FAST                5 (actor)

 871            LOAD_CONST              52 ('SUCCESS')

 872            LOAD_CONST              56 ('learning.adaptive_memory.candidate_created')

 873            LOAD_SMALL_INT           0

 865            LOAD_CONST              54 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'event', 'warning_count'))
                CALL_KW                  8
                POP_TOP

 875            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 876            LOAD_CONST               9 ('ok')

 877            LOAD_FAST               10 (bid)

 878            LOAD_FAST                8 (rid)

 879            LOAD_FAST                9 (trid)

 880            LOAD_FAST               24 (memory_candidate_id)

 881            LOAD_CONST              26 (True)

 882            LOAD_CONST              57 ('candidate_created')

 883            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 884            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 885            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 886            LOAD_FAST                2 (actor_type)

 887            LOAD_FAST                5 (actor)

 888            LOAD_FAST               22 (rep_warnings)

 875            LOAD_CONST              58 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'memory_candidate_id', 'eligible', 'reason_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings'))
                CALL_KW                 13
                RETURN_VALUE

 893   L36:     LOAD_FAST               19 (rep_status)
                LOAD_CONST               9 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       98 (to L37)
                NOT_TAKEN
                LOAD_FAST               20 (created)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       91 (to L37)
                NOT_TAKEN

 894            LOAD_GLOBAL             17 (_audit + NULL)

 895            LOAD_CONST              50 ('adaptive_memory_bridge_skipped')

 896            LOAD_FAST               10 (bid)

 897            LOAD_FAST                9 (trid)

 898            LOAD_FAST                2 (actor_type)

 899            LOAD_FAST                5 (actor)

 900            LOAD_CONST              14 ('FAILED')

 901            LOAD_CONST              59 ('candidate_skipped')

 902            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 903            LOAD_SMALL_INT           1

 894            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 905            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 906            LOAD_CONST              28 ('skipped')

 907            LOAD_FAST               10 (bid)

 908            LOAD_FAST                8 (rid)

 909            LOAD_FAST                9 (trid)

 910            LOAD_CONST              26 (True)

 911            LOAD_CONST              59 ('candidate_skipped')

 912            LOAD_CONST              59 ('candidate_skipped')

 913            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 914            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 915            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 916            LOAD_FAST                2 (actor_type)

 917            LOAD_FAST                5 (actor)

 918            LOAD_FAST               22 (rep_warnings)

 919            LOAD_SMALL_INT           1

 905            LOAD_CONST              30 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings', 'warning_count'))
                CALL_KW                 14
                RETURN_VALUE

 922   L37:     LOAD_GLOBAL             17 (_audit + NULL)

 923            LOAD_CONST              60 ('adaptive_memory_bridge_failed')

 924            LOAD_FAST               10 (bid)

 925            LOAD_FAST                9 (trid)

 926            LOAD_FAST                2 (actor_type)

 927            LOAD_FAST                5 (actor)

 928            LOAD_CONST              14 ('FAILED')

 929            LOAD_CONST              61 ('candidate_failed')

 930            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 931            LOAD_SMALL_INT           1

 922            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 933            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 934            LOAD_CONST               1 ('failed')

 935            LOAD_FAST               10 (bid)

 936            LOAD_FAST                8 (rid)

 937            LOAD_FAST                9 (trid)

 938            LOAD_CONST              26 (True)

 939            LOAD_CONST              61 ('candidate_failed')

 940            LOAD_CONST              61 ('candidate_failed')

 941            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 942            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 943            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 944            LOAD_FAST                2 (actor_type)

 945            LOAD_FAST                5 (actor)

 946            LOAD_FAST               22 (rep_warnings)

 947            LOAD_GLOBAL             55 (max + NULL)
                LOAD_FAST               21 (failed)
                LOAD_SMALL_INT           1
                CALL                     2

 933            LOAD_CONST              30 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings', 'warning_count'))
                CALL_KW                 14
                RETURN_VALUE

  --   L38:     PUSH_EXC_INFO

 731            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        9 (to L40)
                NOT_TAKEN
                POP_TOP

 732            LOAD_CONST              36 ('valid')
                LOAD_CONST              26 (True)
                BUILD_MAP                1
                STORE_FAST              15 (scan)
       L39:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 942 (to L19)

 731   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L42:     PUSH_EXC_INFO

 766            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      167 (to L47)
                NOT_TAKEN
                STORE_FAST              17 (e)

 767   L43:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 768            LOAD_CONST              39 ('bridge_to_memory_candidate pipeline import error type=')

 769            LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 768            BUILD_STRING             2

 767            CALL                     1
                POP_TOP

 771            LOAD_GLOBAL             17 (_audit + NULL)

 772            LOAD_CONST              11 ('adaptive_memory_bridge_rejected')

 773            LOAD_FAST               10 (bid)

 774            LOAD_FAST                9 (trid)

 775            LOAD_FAST                2 (actor_type)

 776            LOAD_FAST                5 (actor)

 777            LOAD_CONST              14 ('FAILED')

 778            LOAD_CONST              40 ('memory_candidate_pipeline_unavailable')

 779            LOAD_CONST              16 ('learning.adaptive_memory.bridge_rejected')

 780            LOAD_SMALL_INT           1

 771            LOAD_CONST              17 (('action', 'brokerage_id', 'target_id', 'actor_type', 'actor_id', 'audit_status', 'error_code', 'event', 'warning_count'))
                CALL_KW                  9
                POP_TOP

 782            LOAD_GLOBAL              3 (_bridge_envelope + NULL)

 783            LOAD_CONST              28 ('skipped')

 784            LOAD_FAST               10 (bid)

 785            LOAD_FAST                8 (rid)

 786            LOAD_FAST                9 (trid)

 787            LOAD_CONST              26 (True)

 788            LOAD_CONST              40 ('memory_candidate_pipeline_unavailable')

 789            LOAD_CONST              40 ('memory_candidate_pipeline_unavailable')

 790            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              20 ('risk_score')
                CALL                     1

 791            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              21 ('confidence_score')
                CALL                     1

 792            LOAD_FAST                6 (eligibility)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              22 ('evidence_fingerprint')
                CALL                     1

 793            LOAD_FAST                2 (actor_type)

 794            LOAD_FAST                5 (actor)

 795            LOAD_CONST              41 ('pipeline_import_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 796            LOAD_SMALL_INT           1

 782            LOAD_CONST              30 (('status', 'brokerage_id', 'recommendation_id', 'test_run_id', 'eligible', 'reason_code', 'error_code', 'risk_score', 'confidence_score', 'evidence_fingerprint', 'actor_type', 'actor_id', 'warnings', 'warning_count'))
                CALL_KW                 14
       L44:     SWAP                     2
       L45:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L46:     LOAD_CONST               4 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 766   L47:     RERAISE                  0

  --   L48:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L18 to L19 -> L38 [0]
  L21 to L22 -> L42 [0]
  L38 to L39 -> L41 [1] lasti
  L40 to L41 -> L41 [1] lasti
  L42 to L43 -> L48 [1] lasti
  L43 to L44 -> L46 [1] lasti
  L44 to L45 -> L48 [1] lasti
  L46 to L48 -> L48 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/learning/adaptive_memory_bridge.py", line 955>:
955           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

957           LOAD_CONST               2 ('Optional[str]')

955           LOAD_CONST               3 ('limit')

958           LOAD_CONST               4 ('Any')

955           LOAD_CONST               5 ('return')

959           LOAD_CONST               6 ('Dict[str, Any]')

955           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object adaptive_memory_bridge_report at 0x0000018C17F7C5E0, file "app/services/learning/adaptive_memory_bridge.py", line 955>:
 955            RESUME                   0

 967            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               2 (bid)

 968            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 970            LOAD_GLOBAL              5 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 971            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L3)
                NOT_TAKEN

 973            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 974            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 975            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 976            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 977            LOAD_CONST               7 ('warnings')
                LOAD_CONST               8 ('store_unavailable')
                BUILD_LIST               1

 978            LOAD_CONST               9 ('error_code')
                LOAD_CONST               8 ('store_unavailable')

 972            BUILD_MAP                6
                RETURN_VALUE

 981    L3:     LOAD_CONST              36 (('adaptive_memory_bridge_confirmed', 'adaptive_memory_candidate_created', 'adaptive_memory_bridge_rejected', 'adaptive_memory_bridge_skipped', 'adaptive_memory_bridge_failed'))
                STORE_FAST               5 (bridge_actions)

 989            NOP

 991    L4:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR                7 (table + NULL|self)
                LOAD_CONST              14 ('pas_operator_actions_log')
                CALL                     1

 992            LOAD_ATTR                9 (select + NULL|self)

 993            LOAD_CONST              15 ('id, brokerage_id, actor_type, action, status, target_type, target_id, warning_count, error_code, created_at')

 992            CALL                     1

 997            LOAD_ATTR               11 (in_ + NULL|self)
                LOAD_CONST              16 ('action')
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_FAST_BORROW         5 (bridge_actions)
                CALL                     1
                CALL                     2

 998            LOAD_ATTR               15 (order + NULL|self)
                LOAD_CONST              17 ('created_at')
                LOAD_CONST              18 (True)
                LOAD_CONST              19 (('desc',))
                CALL_KW                  2

 999            LOAD_ATTR               17 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 990            STORE_FAST               6 (query)

1001            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L5)
                NOT_TAKEN

1002            LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2
                STORE_FAST               6 (query)

1003    L5:     LOAD_FAST_BORROW         6 (query)
                LOAD_ATTR               21 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (result)

1004            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             23 (getattr + NULL)
                LOAD_FAST_BORROW         7 (result)
                LOAD_CONST              20 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               8 (rows)

1019    L9:     BUILD_LIST               0
                STORE_FAST              10 (projected)

1020            LOAD_FAST                8 (rows)
                GET_ITER
       L10:     EXTENDED_ARG             1
                FOR_ITER               344 (to L25)
                STORE_FAST              11 (r)

1021            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN

1022            JUMP_BACKWARD           28 (to L10)

1023   L11:     LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              16 ('action')
                CALL                     1
                STORE_FAST              12 (action)

1024            LOAD_FAST               12 (action)
                LOAD_CONST              10 ('adaptive_memory_bridge_confirmed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        6 (to L12)
                NOT_TAKEN

1025            LOAD_CONST              23 ('ok')
                STORE_FAST              13 (status_token)

1026            LOAD_CONST              24 ('candidate_created')
                STORE_FAST              14 (reason)
                JUMP_FORWARD           115 (to L19)

1027   L12:     LOAD_FAST               12 (action)
                LOAD_CONST              11 ('adaptive_memory_candidate_created')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        6 (to L13)
                NOT_TAKEN

1028            LOAD_CONST              23 ('ok')
                STORE_FAST              13 (status_token)

1029            LOAD_CONST              24 ('candidate_created')
                STORE_FAST              14 (reason)
                JUMP_FORWARD           103 (to L19)

1030   L13:     LOAD_FAST               12 (action)
                LOAD_CONST              12 ('adaptive_memory_bridge_skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       31 (to L15)
                NOT_TAKEN

1031            LOAD_CONST               3 ('skipped')
                STORE_FAST              13 (status_token)

1032            LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              25 ('candidate_skipped')
       L14:     STORE_FAST              14 (reason)
                JUMP_FORWARD            66 (to L19)

1033   L15:     LOAD_FAST               12 (action)
                LOAD_CONST              13 ('adaptive_memory_bridge_failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN

1034            LOAD_CONST              26 ('failed')
                STORE_FAST              13 (status_token)

1035            LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              27 ('candidate_failed')
       L16:     STORE_FAST              14 (reason)
                JUMP_FORWARD            29 (to L19)

1037   L17:     LOAD_CONST              26 ('failed')
                STORE_FAST              13 (status_token)

1038            LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              28 ('bridge_rejected_by_operator')
       L18:     STORE_FAST              14 (reason)

1039   L19:     LOAD_FAST               14 (reason)
                LOAD_GLOBAL             40 (ALLOWED_BRIDGE_REASON_CODES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_FAST               14 (reason)
                JUMP_FORWARD             1 (to L21)
       L20:     LOAD_CONST               1 (None)
       L21:     STORE_FAST              15 (rc)

1040            LOAD_FAST               10 (projected)
                LOAD_ATTR               43 (append + NULL|self)

1041            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                CALL                     1

1042            LOAD_CONST              29 ('test_run_id')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              30 ('target_type')
                CALL                     1
                LOAD_CONST              31 ('learning_adaptive_memory_bridge')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L22)
                NOT_TAKEN
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              32 ('target_id')
                CALL                     1
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST               1 (None)

1043   L23:     LOAD_CONST               2 ('status')
                LOAD_FAST               13 (status_token)

1044            LOAD_CONST              33 ('reason_code')
                LOAD_FAST               15 (rc)

1045            LOAD_CONST              34 ('actor_type')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              34 ('actor_type')
                CALL                     1

1046            LOAD_CONST              35 ('warning_count')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              35 ('warning_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0

1047   L24:     LOAD_CONST               9 ('error_code')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               9 ('error_code')
                CALL                     1

1048            LOAD_CONST              17 ('created_at')
                LOAD_FAST               11 (r)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              17 ('created_at')
                CALL                     1

1040            BUILD_MAP                8
                CALL                     1
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          347 (to L10)

1020   L25:     END_FOR
                POP_ITER

1052            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('ok')

1053            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

1054            LOAD_CONST               5 ('rows')
                LOAD_FAST               10 (projected)

1055            LOAD_CONST               6 ('count')
                LOAD_GLOBAL             45 (len + NULL)
                LOAD_FAST               10 (projected)
                CALL                     1

1056            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

1057            LOAD_CONST               9 ('error_code')
                LOAD_CONST               1 (None)

1051            BUILD_MAP                6
                RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

1005            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L31)
                NOT_TAKEN
                STORE_FAST               9 (e)

1006   L27:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

1007            LOAD_CONST              21 ('adaptive_memory_bridge_report read error type=')

1008            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

1007            BUILD_STRING             2

1006            CALL                     1
                POP_TOP

1011            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

1012            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

1013            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

1014            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

1015            LOAD_CONST               7 ('warnings')
                LOAD_CONST              22 ('db_read_failed:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

1016            LOAD_CONST               9 ('error_code')
                LOAD_CONST               8 ('store_unavailable')

1010            BUILD_MAP                6
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

1005   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L6 -> L26 [0]
  L7 to L9 -> L26 [0]
  L26 to L27 -> L32 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti
```
