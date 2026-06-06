# learning/recommendation_engine

- **pyc:** `app\services\learning\__pycache__\recommendation_engine.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/recommendation_engine.py`
- **co_filename (from bytecode):** `app/services/learning/recommendation_engine.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Learning recommendation engine (CANDIDATE-only).

Produces structural ``CANDIDATE`` learning recommendations
from scenario simulation + outcome feedback signals. PAS179
NEVER auto-approves, NEVER auto-applies, and NEVER mutates
live PAS behavior. The operator transitions recommendations
to ``APPROVED_FOR_MANUAL_TEST`` / ``REJECTED`` / ``EXPIRED``
through a deliberate review path (out of scope for PAS179).

Doctrine:

* **CANDIDATE only.** ``build_learning_recommendation`` and
  ``persist_learning_recommendation`` produce / store
  recommendations only with status ``CANDIDATE``. There is
  no helper in PAS179 that writes a non-candidate status.
* **No auto-approval.** No code path in PAS179 calls into
  the SQL UPDATE policy. Status transitions require an
  explicit future operator surface (PAS180+).
* **No live behavior mutation.** Recommendations are records,
  not actions. PAS179 does not call into the outbound FSM,
  Memory Review, booking engine, or any other live PAS
  surface.
* **No LLM calls.** Scoring is deterministic and rule-based.
* **Storage helper missing → ``status="skipped"``.** The v28
  table is PROPOSAL ONLY; when not promoted, persistence
  collapses to a skipped envelope.
* **NEVER raises.** All failures return structural envelopes.
* **No raw rationale.** ``rationale_token`` is a closed-
  character-set token; no freeform prose ever lands.

Public surface:

  * ``ALLOWED_RECOMMENDATION_TYPES``                    — closed enum
  * ``ALLOWED_RECOMMENDED_ACTIONS``                     — closed allow-list
  * ``ALLOWED_RATIONALE_TOKENS``                        — closed allow-list
  * ``ALLOWED_RECOMMENDATION_METADATA_KEYS``            — closed allow-list
  * ``build_learning_recommendation(...)``              — CANDIDATE builder
  * ``score_learning_recommendation(...)``              — deterministic scorer
  * ``recommendation_report(...)``                      — read-only summary
  * ``persist_learning_recommendation(record)``         — append-only INSERT
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_bound_token`, `_clamp_score`, `_get_db_safe`, `_now_iso`, `_project_metadata`, `_project_row`, `build_learning_recommendation`, `persist_learning_recommendation`, `recommendation_report`, `score_learning_recommendation`

## Env-key candidates

`ALLOWED_INITIAL_STATUSES`, `ALLOWED_RATIONALE_TOKENS`, `ALLOWED_RECOMMENDATION_METADATA_KEYS`, `ALLOWED_RECOMMENDATION_TYPES`, `ALLOWED_RECOMMENDED_ACTIONS`, `ALLOWED_SOURCE_TYPES`, `CANDIDATE`

## String constants (redacted where noted)

- '\nPAS179 — Learning recommendation engine (CANDIDATE-only).\n\nProduces structural ``CANDIDATE`` learning recommendations\nfrom scenario simulation + outcome feedback signals. PAS179\nNEVER auto-approves, NEVER auto-applies, and NEVER mutates\nlive PAS behavior. The operator transitions recommendations\nto ``APPROVED_FOR_MANUAL_TEST`` / ``REJECTED`` / ``EXPIRED``\nthrough a deliberate review path (out of scope for PAS179).\n\nDoctrine:\n\n* **CANDIDATE only.** ``build_learning_recommendation`` and\n  ``persist_learning_recommendation`` produce / store\n  recommendations only with status ``CANDIDATE``. There is\n  no helper in PAS179 that writes a non-candidate status.\n* **No auto-approval.** No code path in PAS179 calls into\n  the SQL UPDATE policy. Status transitions require an\n  explicit future operator surface (PAS180+).\n* **No live behavior mutation.** Recommendations are records,\n  not actions. PAS179 does not call into the outbound FSM,\n  Memory Review, booking engine, or any other live PAS\n  surface.\n* **No LLM calls.** Scoring is deterministic and rule-based.\n* **Storage helper missing → ``status="skipped"``.** The v28\n  table is PROPOSAL ONLY; when not promoted, persistence\n  collapses to a skipped envelope.\n* **NEVER raises.** All failures return structural envelopes.\n* **No raw rationale.** ``rationale_token`` is a closed-\n  character-set token; no freeform prose ever lands.\n\nPublic surface:\n\n  * ``ALLOWED_RECOMMENDATION_TYPES``                    — closed enum\n  * ``ALLOWED_RECOMMENDED_ACTIONS``                     — closed allow-list\n  * ``ALLOWED_RATIONALE_TOKENS``                        — closed allow-list\n  * ``ALLOWED_RECOMMENDATION_METADATA_KEYS``            — closed allow-list\n  * ``build_learning_recommendation(...)``              — CANDIDATE builder\n  * ``score_learning_recommendation(...)``              — deterministic scorer\n  * ``recommendation_report(...)``                      — read-only summary\n  * ``persist_learning_recommendation(record)``         — append-only INSERT\n'
- 'pas.learning.recommendation_engine'
- 'pas_learning_recommendations'
- 'Tuple[str, ...]'
- 'ALLOWED_RECOMMENDATION_TYPES'
- 'ALLOWED_SOURCE_TYPES'
- 'ALLOWED_INITIAL_STATUSES'
- 'ALLOWED_RECOMMENDED_ACTIONS'
- 'ALLOWED_RATIONALE_TOKENS'
- 'ALLOWED_RECOMMENDATION_METADATA_KEYS'
- 🔒 '<REDACTED:high-entropy blob, len=64>'
- 'source_id'
- 'confidence_score'
- 'risk_score'
- 'usefulness_score'
- 'rationale_token'
- 'metadata'
- 'limit'
- 'return'
- 'str'
- 'seconds'
- 'recommendation_engine db client unavailable type='
- 'value'
- 'Any'
- 'Optional[str]'
- 'max_len'
- 'int'
- 'Optional[float]'
- 'Dict[str, Any]'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'brokerage_id'
- 'recommendation_type'
- 'source_type'
- 'recommended_action'
- 'Build a CANDIDATE recommendation record. NEVER raises.\n\nAlways emits ``status="CANDIDATE"``. No code path here is\nable to write a non-candidate status; that is a deliberate\nPAS179 invariant.\n'
- 'status'
- 'failed'
- 'record'
- 'warnings'
- 'error_code'
- 'invalid_recommendation_type'
- 'invalid_source_type'
- 'invalid_recommended_action'
- 'missing_brokerage_id'
- 'invalid_source_id'
- 'invalid_rationale_token'
- 'recommendation_id'
- 'CANDIDATE'
- 'created_at'
- 'reviewed_at'
- 'reviewed_by_actor_type'
- 'reviewed_by_actor_id'
- 'Deterministic structural score envelope for a built\nrecommendation. NEVER raises.\n\nReturns the bounded {confidence, risk, usefulness, overall}\ntuple; overall = clamp(usefulness * (1 - risk) * confidence).\n'
- 'scores'
- 'invalid_record'
- 'confidence'
- 'risk'
- 'usefulness'
- 'overall'
- 'score_learning_recommendation error type='
- 'unexpected:'
- 'Insert a CANDIDATE learning recommendation. NEVER raises.\n\n* Storage helper missing / DB unavailable → ``status="skipped"``.\n* Record with non-candidate status → ``status="failed"`` with\n  ``error_code="recommendation_status_must_be_candidate"``.\n  PAS179 forbids writing any other status from this helper.\n'
- 'rec_row'
- 'recommendation_status_must_be_candidate'
- 'skipped'
- 'learning_recommendations_store_unavailable'
- 'data'
- 'persist_learning_recommendation db error type='
- 'db_write_failed:'
- 'Read-only structural summary of CANDIDATE\nrecommendations for the brokerage. NEVER raises. NEVER\nreturns PII.'
- 'total'
- 'by_type'
- 'by_status'
- 'rows'
- 'recommendation_report read error type='
- 'db_read_failed:'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS179 — Learning recommendation engine (CANDIDATE-only).\n\nProduces structural ``CANDIDATE`` learning recommendations\nfrom scenario simulation + outcome feedback signals. PAS179\nNEVER auto-approves, NEVER auto-applies, and NEVER mutates\nlive PAS behavior. The operator transitions recommendations\nto ``APPROVED_FOR_MANUAL_TEST`` / ``REJECTED`` / ``EXPIRED``\nthrough a deliberate review path (out of scope for PAS179).\n\nDoctrine:\n\n* **CANDIDATE only.** ``build_learning_recommendation`` and\n  ``persist_learning_recommendation`` produce / store\n  recommendations only with status ``CANDIDATE``. There is\n  no helper in PAS179 that writes a non-candidate status.\n* **No auto-approval.** No code path in PAS179 calls into\n  the SQL UPDATE policy. Status transitions require an\n  explicit future operator surface (PAS180+).\n* **No live behavior mutation.** Recommendations are records,\n  not actions. PAS179 does not call into the outbound FSM,\n  Memory Review, booking engine, or any other live PAS\n  surface.\n* **No LLM calls.** Scoring is deterministic and rule-based.\n* **Storage helper missing → ``status="skipped"``.** The v28\n  table is PROPOSAL ONLY; when not promoted, persistence\n  collapses to a skipped envelope.\n* **NEVER raises.** All failures return structural envelopes.\n* **No raw rationale.** ``rationale_token`` is a closed-\n  character-set token; no freeform prose ever lands.\n\nPublic surface:\n\n  * ``ALLOWED_RECOMMENDATION_TYPES``                    — closed enum\n  * ``ALLOWED_RECOMMENDED_ACTIONS``                     — closed allow-list\n  * ``ALLOWED_RATIONALE_TOKENS``                        — closed allow-list\n  * ``ALLOWED_RECOMMENDATION_METADATA_KEYS``            — closed allow-list\n  * ``build_learning_recommendation(...)``              — CANDIDATE builder\n  * ``score_learning_recommendation(...)``              — deterministic scorer\n  * ``recommendation_report(...)``                      — read-only summary\n  * ``persist_learning_recommendation(record)``         — append-only INSERT\n')
               STORE_NAME               1 (__doc__)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  46           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  47           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (uuid)
               STORE_NAME               5 (uuid)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              6 (datetime)
               IMPORT_FROM              6 (datetime)
               STORE_NAME               6 (datetime)
               IMPORT_FROM              7 (timezone)
               STORE_NAME               7 (timezone)
               POP_TOP

  49           LOAD_SMALL_INT           0
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

  52           LOAD_NAME                4 (logging)
               LOAD_ATTR               28 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.learning.recommendation_engine')
               CALL                     1
               STORE_NAME              15 (logger)

  55           LOAD_CONST               6 ('pas_learning_recommendations')
               STORE_NAME              16 (_TABLE)

  58           LOAD_CONST              43 (('MEMORY_UPDATE', 'SCRIPT_BRANCH_REVIEW', 'CALLBACK_TIMING_REVIEW', 'LEAD_PRIORITY_REVIEW', 'ROUTING_RULE_REVIEW', 'OBJECTION_PATTERN_REVIEW'))
               STORE_NAME              17 (ALLOWED_RECOMMENDATION_TYPES)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST               8 ('ALLOWED_RECOMMENDATION_TYPES')
               STORE_SUBSCR

  68           LOAD_CONST              44 (('SIMULATION_RUN', 'OUTCOME_FEEDBACK', 'MEMORY_CANDIDATE', 'OPERATOR_REVIEW'))
               STORE_NAME              19 (ALLOWED_SOURCE_TYPES)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST               9 ('ALLOWED_SOURCE_TYPES')
               STORE_SUBSCR

  79           LOAD_CONST              45 (('CANDIDATE',))
               STORE_NAME              20 (ALLOWED_INITIAL_STATUSES)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST              10 ('ALLOWED_INITIAL_STATUSES')
               STORE_SUBSCR

  84           LOAD_CONST              46 (('REVIEW_MEMORY_CANDIDATE', 'REVIEW_SCRIPT_BRANCH', 'REVIEW_CALLBACK_TIMING', 'REVIEW_LEAD_PRIORITY', 'REVIEW_ROUTING_RULE', 'REVIEW_OBJECTION_PATTERN', 'NO_ACTION_REQUIRED'))
               STORE_NAME              21 (ALLOWED_RECOMMENDED_ACTIONS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST              11 ('ALLOWED_RECOMMENDED_ACTIONS')
               STORE_SUBSCR

  96           LOAD_CONST              47 (('LOW_BOOKING_RATE', 'HIGH_CALLBACK_DROP', 'HIGH_OBJECTION_RATE', 'HIGH_PROVIDER_FAILURE', 'HIGH_WORKER_FAILURE', 'HIGH_DUPLICATE_RATE', 'HIGH_USEFULNESS_SCORE', 'LOW_CONFIDENCE', 'OPERATOR_REVIEW_REQUESTED'))
               STORE_NAME              22 (ALLOWED_RATIONALE_TOKENS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST              12 ('ALLOWED_RATIONALE_TOKENS')
               STORE_SUBSCR

 109           LOAD_CONST              48 (('scenario_type', 'scenario_fingerprint', 'simulation_run_id', 'outcome_count', 'warning_count'))
               STORE_NAME              23 (ALLOWED_RECOMMENDATION_METADATA_KEYS)
               LOAD_CONST               7 ('Tuple[str, ...]')
               LOAD_NAME               18 (__annotations__)
               LOAD_CONST              13 ('ALLOWED_RECOMMENDATION_METADATA_KEYS')
               STORE_SUBSCR

 119           LOAD_SMALL_INT         200
               STORE_NAME              24 (_BROKERAGE_ID_MAX_LEN)

 120           LOAD_SMALL_INT         200
               STORE_NAME              25 (_SOURCE_ID_MAX_LEN)

 121           LOAD_SMALL_INT         200
               STORE_NAME              26 (_VALUE_MAX_LEN)

 125           LOAD_CONST              14 ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_')

 124           STORE_NAME              27 (_ALLOWED_TOKEN_CHARS)

 132           LOAD_CONST              49 (('recommendation_id', 'brokerage_id', 'recommendation_type', 'source_type', 'source_id', 'status', 'confidence_score', 'risk_score', 'usefulness_score', 'recommended_action', 'rationale_token', 'created_at', 'reviewed_at', 'reviewed_by_actor_type', 'reviewed_by_actor_id', 'metadata'))
               STORE_NAME              28 (_STRUCTURAL_COLUMNS)

 156           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/recommendation_engine.py", line 156>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _now_iso at 0x0000018C18039070, file "app/services/learning/recommendation_engine.py", line 156>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_now_iso)

 160           LOAD_CONST              23 (<code object _get_db_safe at 0x0000018C17FF0C30, file "app/services/learning/recommendation_engine.py", line 160>)
               MAKE_FUNCTION
               STORE_NAME              30 (_get_db_safe)

 172           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA35A0, file "app/services/learning/recommendation_engine.py", line 172>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/recommendation_engine.py", line 172>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_bound_brokerage_id)

 181           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025930, file "app/services/learning/recommendation_engine.py", line 181>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _bound_token at 0x0000018C179C3C30, file "app/services/learning/recommendation_engine.py", line 181>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_bound_token)

 192           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/recommendation_engine.py", line 192>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _clamp_score at 0x0000018C17FE17D0, file "app/services/learning/recommendation_engine.py", line 192>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_clamp_score)

 206           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/recommendation_engine.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _project_metadata at 0x0000018C17FEDA30, file "app/services/learning/recommendation_engine.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_project_metadata)

 221           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/recommendation_engine.py", line 221>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _project_row at 0x0000018C1796DBD0, file "app/services/learning/recommendation_engine.py", line 221>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_project_row)

 236           LOAD_CONST              19 ('rationale_token')

 242           LOAD_CONST               2 (None)

 236           LOAD_CONST              16 ('confidence_score')

 243           LOAD_CONST               2 (None)

 236           LOAD_CONST              17 ('risk_score')

 244           LOAD_CONST               2 (None)

 236           LOAD_CONST              18 ('usefulness_score')

 245           LOAD_CONST               2 (None)

 236           LOAD_CONST              15 ('source_id')

 246           LOAD_CONST               2 (None)

 236           LOAD_CONST              20 ('metadata')

 247           LOAD_CONST               2 (None)

 236           BUILD_MAP                6
               LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18053510, file "app/services/learning/recommendation_engine.py", line 236>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object build_learning_recommendation at 0x0000018C17ED9FB0, file "app/services/learning/recommendation_engine.py", line 236>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (build_learning_recommendation)

 331           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/recommendation_engine.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object score_learning_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/recommendation_engine.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (score_learning_recommendation)

 378           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/learning/recommendation_engine.py", line 378>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object persist_learning_recommendation at 0x0000018C17F75AE0, file "app/services/learning/recommendation_engine.py", line 378>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (persist_learning_recommendation)

 438           LOAD_CONST              40 ('limit')

 441           LOAD_SMALL_INT         100

 438           BUILD_MAP                1
               LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18024C30, file "app/services/learning/recommendation_engine.py", line 438>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object recommendation_report at 0x0000018C17ED78E0, file "app/services/learning/recommendation_engine.py", line 438>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (recommendation_report)

 522           BUILD_LIST               0
               LOAD_CONST              50 (('ALLOWED_RECOMMENDATION_TYPES', 'ALLOWED_SOURCE_TYPES', 'ALLOWED_INITIAL_STATUSES', 'ALLOWED_RECOMMENDED_ACTIONS', 'ALLOWED_RATIONALE_TOKENS', 'ALLOWED_RECOMMENDATION_METADATA_KEYS', 'build_learning_recommendation', 'score_learning_recommendation', 'recommendation_report', 'persist_learning_recommendation'))
               LIST_EXTEND              1
               STORE_NAME              40 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/learning/recommendation_engine.py", line 156>:
156           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18039070, file "app/services/learning/recommendation_engine.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object _get_db_safe at 0x0000018C17FF0C30, file "app/services/learning/recommendation_engine.py", line 160>:
 160           RESUME                   0

 161           NOP

 162   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 163           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 164           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 165   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 166           LOAD_CONST               2 ('recommendation_engine db client unavailable type=')

 167           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 166           BUILD_STRING             2

 165           CALL                     1
               POP_TOP

 169   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 164   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app/services/learning/recommendation_engine.py", line 172>:
172           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C17F95CF0, file "app/services/learning/recommendation_engine.py", line 172>:
172           RESUME                   0

173           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

174           LOAD_CONST               0 (None)
              RETURN_VALUE

175   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

176           LOAD_FAST_BORROW         1 (s)
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

177   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

178   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/learning/recommendation_engine.py", line 181>:
181           RESUME                   0
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

Disassembly of <code object _bound_token at 0x0000018C179C3C30, file "app/services/learning/recommendation_engine.py", line 181>:
181           RESUME                   0

182           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

183           LOAD_CONST               0 (None)
              RETURN_VALUE

184   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

185           LOAD_FAST_BORROW         2 (s)
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

186   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

187   L3:     LOAD_GLOBAL              8 (any)
              COPY                     1
              LOAD_COMMON_CONSTANT     4 (<built-in function any>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C180909C0, file "app/services/learning/recommendation_engine.py", line 187>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (s)
              GET_ITER
              CALL                     0
      L4:     FOR_ITER                12 (to L6)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L4)
      L5:     POP_ITER
              LOAD_CONST               2 (True)
              JUMP_FORWARD            17 (to L8)
      L6:     END_FOR
              POP_ITER
              LOAD_CONST               3 (False)
              JUMP_FORWARD            13 (to L8)
      L7:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C180909C0, file "app/services/learning/recommendation_engine.py", line 187>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         2 (s)
              GET_ITER
              CALL                     0
              CALL                     1
      L8:     TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L9)
              NOT_TAKEN

188           LOAD_CONST               0 (None)
              RETURN_VALUE

189   L9:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180909C0, file "app/services/learning/recommendation_engine.py", line 187>:
 187           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                13 (to L3)
               STORE_FAST_LOAD_FAST    17 (ch, ch)
               LOAD_GLOBAL              0 (_ALLOWED_TOKEN_CHARS)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/learning/recommendation_engine.py", line 192>:
192           RESUME                   0
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

Disassembly of <code object _clamp_score at 0x0000018C17FE17D0, file "app/services/learning/recommendation_engine.py", line 192>:
 192           RESUME                   0

 193           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 194           LOAD_CONST               0 (None)
               RETURN_VALUE

 195   L1:     NOP

 196   L2:     LOAD_GLOBAL              1 (float + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 199   L3:     LOAD_FAST                1 (v)
               LOAD_CONST               1 (0.0)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 200           LOAD_CONST               1 (0.0)
               RETURN_VALUE

 201   L4:     LOAD_FAST                1 (v)
               LOAD_CONST               2 (1.0)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN

 202           LOAD_CONST               2 (1.0)
               RETURN_VALUE

 203   L5:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 197           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 198   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 197   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/learning/recommendation_engine.py", line 206>:
206           RESUME                   0
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

Disassembly of <code object _project_metadata at 0x0000018C17FEDA30, file "app/services/learning/recommendation_engine.py", line 206>:
206           RESUME                   0

207           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (metadata)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

208           BUILD_MAP                0
              RETURN_VALUE

209   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

210           LOAD_GLOBAL              4 (ALLOWED_RECOMMENDATION_METADATA_KEYS)
              GET_ITER
      L2:     FOR_ITER               112 (to L8)
              STORE_FAST               2 (k)

211           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, metadata)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

212           JUMP_BACKWARD           11 (to L2)

213   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (metadata, k)
              BINARY_OP               26 ([])
              STORE_FAST               3 (v)

214           LOAD_FAST_BORROW         3 (v)
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

215   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           62 (to L2)

216   L5:     LOAD_GLOBAL              1 (isinstance + NULL)
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
              LOAD_GLOBAL             16 (_VALUE_MAX_LEN)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD          108 (to L2)

217   L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD          114 (to L2)

210   L8:     END_FOR
              POP_ITER

218           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app/services/learning/recommendation_engine.py", line 221>:
221           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C1796DBD0, file "app/services/learning/recommendation_engine.py", line 221>:
221           RESUME                   0

222           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

223           LOAD_CONST               0 (None)
              RETURN_VALUE

224   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

225           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

226           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

227   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

225   L4:     END_FOR
              POP_ITER

228           LOAD_GLOBAL              7 (_project_metadata + NULL)
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

229           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053510, file "app/services/learning/recommendation_engine.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

238           LOAD_CONST               2 ('Any')

236           LOAD_CONST               3 ('recommendation_type')

239           LOAD_CONST               4 ('str')

236           LOAD_CONST               5 ('source_type')

240           LOAD_CONST               4 ('str')

236           LOAD_CONST               6 ('recommended_action')

241           LOAD_CONST               4 ('str')

236           LOAD_CONST               7 ('rationale_token')

242           LOAD_CONST               8 ('Optional[str]')

236           LOAD_CONST               9 ('confidence_score')

243           LOAD_CONST               2 ('Any')

236           LOAD_CONST              10 ('risk_score')

244           LOAD_CONST               2 ('Any')

236           LOAD_CONST              11 ('usefulness_score')

245           LOAD_CONST               2 ('Any')

236           LOAD_CONST              12 ('source_id')

246           LOAD_CONST               8 ('Optional[str]')

236           LOAD_CONST              13 ('metadata')

247           LOAD_CONST              14 ('Optional[Dict[str, Any]]')

236           LOAD_CONST              15 ('return')

248           LOAD_CONST              16 ('Dict[str, Any]')

236           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object build_learning_recommendation at 0x0000018C17ED9FB0, file "app/services/learning/recommendation_engine.py", line 236>:
236           RESUME                   0

255           LOAD_FAST_BORROW         1 (recommendation_type)
              LOAD_GLOBAL              0 (ALLOWED_RECOMMENDATION_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       11 (to L1)
              NOT_TAKEN

257           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

258           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

259           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

260           LOAD_CONST               6 ('error_code')
              LOAD_CONST               7 ('invalid_recommendation_type')

256           BUILD_MAP                4
              RETURN_VALUE

262   L1:     LOAD_FAST_BORROW         2 (source_type)
              LOAD_GLOBAL              2 (ALLOWED_SOURCE_TYPES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       11 (to L2)
              NOT_TAKEN

264           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

265           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

266           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

267           LOAD_CONST               6 ('error_code')
              LOAD_CONST               8 ('invalid_source_type')

263           BUILD_MAP                4
              RETURN_VALUE

269   L2:     LOAD_FAST_BORROW         3 (recommended_action)
              LOAD_GLOBAL              4 (ALLOWED_RECOMMENDED_ACTIONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       11 (to L3)
              NOT_TAKEN

271           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

272           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

273           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

274           LOAD_CONST               6 ('error_code')
              LOAD_CONST               9 ('invalid_recommended_action')

270           BUILD_MAP                4
              RETURN_VALUE

276   L3:     LOAD_GLOBAL              7 (_bound_brokerage_id + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              STORE_FAST              10 (bid)

277           LOAD_FAST_BORROW        10 (bid)
              POP_JUMP_IF_NOT_NONE    11 (to L4)
              NOT_TAKEN

279           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

280           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

281           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

282           LOAD_CONST               6 ('error_code')
              LOAD_CONST              10 ('missing_brokerage_id')

278           BUILD_MAP                4
              RETURN_VALUE

284   L4:     LOAD_CONST               4 (None)
              STORE_FAST              11 (sid)

285           LOAD_FAST_BORROW         8 (source_id)
              POP_JUMP_IF_NONE        31 (to L5)
              NOT_TAKEN

286           LOAD_GLOBAL              9 (_bound_token + NULL)
              LOAD_FAST_BORROW         8 (source_id)
              LOAD_GLOBAL             10 (_SOURCE_ID_MAX_LEN)
              CALL                     2
              STORE_FAST              11 (sid)

287           LOAD_FAST_BORROW        11 (sid)
              POP_JUMP_IF_NOT_NONE    11 (to L5)
              NOT_TAKEN

289           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

290           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

291           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

292           LOAD_CONST               6 ('error_code')
              LOAD_CONST              11 ('invalid_source_id')

288           BUILD_MAP                4
              RETURN_VALUE

294   L5:     LOAD_CONST               4 (None)
              STORE_FAST              12 (rationale)

295           LOAD_FAST_BORROW         4 (rationale_token)
              POP_JUMP_IF_NONE        24 (to L7)
              NOT_TAKEN

296           LOAD_FAST_BORROW         4 (rationale_token)
              LOAD_GLOBAL             12 (ALLOWED_RATIONALE_TOKENS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       11 (to L6)
              NOT_TAKEN

298           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

299           LOAD_CONST               3 ('record')
              LOAD_CONST               4 (None)

300           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

301           LOAD_CONST               6 ('error_code')
              LOAD_CONST              12 ('invalid_rationale_token')

297           BUILD_MAP                4
              RETURN_VALUE

303   L6:     LOAD_FAST                4 (rationale_token)
              STORE_FAST              12 (rationale)

305   L7:     BUILD_MAP                0

306           LOAD_CONST              13 ('recommendation_id')
              LOAD_GLOBAL             15 (str + NULL)
              LOAD_GLOBAL             16 (uuid)
              LOAD_ATTR               18 (uuid4)
              PUSH_NULL
              CALL                     0
              CALL                     1

305           MAP_ADD                  1

307           LOAD_CONST              14 ('brokerage_id')
              LOAD_FAST_BORROW        10 (bid)

305           MAP_ADD                  1

308           LOAD_CONST              15 ('recommendation_type')
              LOAD_FAST_BORROW         1 (recommendation_type)

305           MAP_ADD                  1

309           LOAD_CONST              16 ('source_type')
              LOAD_FAST_BORROW         2 (source_type)

305           MAP_ADD                  1

310           LOAD_CONST              17 ('source_id')
              LOAD_FAST_BORROW        11 (sid)

305           MAP_ADD                  1

311           LOAD_CONST               1 ('status')
              LOAD_CONST              18 ('CANDIDATE')

305           MAP_ADD                  1

312           LOAD_CONST              19 ('confidence_score')
              LOAD_GLOBAL             21 (_clamp_score + NULL)
              LOAD_FAST_BORROW         5 (confidence_score)
              CALL                     1

305           MAP_ADD                  1

313           LOAD_CONST              20 ('risk_score')
              LOAD_GLOBAL             21 (_clamp_score + NULL)
              LOAD_FAST_BORROW         6 (risk_score)
              CALL                     1

305           MAP_ADD                  1

314           LOAD_CONST              21 ('usefulness_score')
              LOAD_GLOBAL             21 (_clamp_score + NULL)
              LOAD_FAST_BORROW         7 (usefulness_score)
              CALL                     1

305           MAP_ADD                  1

315           LOAD_CONST              22 ('recommended_action')
              LOAD_FAST_BORROW         3 (recommended_action)

305           MAP_ADD                  1

316           LOAD_CONST              23 ('rationale_token')
              LOAD_FAST_BORROW        12 (rationale)

305           MAP_ADD                  1

317           LOAD_CONST              24 ('created_at')
              LOAD_GLOBAL             23 (_now_iso + NULL)
              CALL                     0

305           MAP_ADD                  1

318           LOAD_CONST              25 ('reviewed_at')
              LOAD_CONST               4 (None)

305           MAP_ADD                  1

319           LOAD_CONST              26 ('reviewed_by_actor_type')
              LOAD_CONST               4 (None)

305           MAP_ADD                  1

320           LOAD_CONST              27 ('reviewed_by_actor_id')
              LOAD_CONST               4 (None)

305           MAP_ADD                  1

321           LOAD_CONST              28 ('metadata')
              LOAD_GLOBAL             25 (_project_metadata + NULL)
              LOAD_FAST_BORROW         9 (metadata)
              CALL                     1

305           MAP_ADD                  1
              STORE_FAST              13 (record)

324           LOAD_CONST               1 ('status')
              LOAD_CONST              29 ('ok')

325           LOAD_CONST               3 ('record')
              LOAD_FAST_BORROW        13 (record)

326           LOAD_CONST               5 ('warnings')
              BUILD_LIST               0

327           LOAD_CONST               6 ('error_code')
              LOAD_CONST               4 (None)

323           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/learning/recommendation_engine.py", line 331>:
331           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object score_learning_recommendation at 0x0000018C17D6DFC0, file "app/services/learning/recommendation_engine.py", line 331>:
 331            RESUME                   0

 338            NOP

 339    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L3)
                NOT_TAKEN

 341            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 342            LOAD_CONST               3 ('scores')
                LOAD_CONST               4 (None)

 343            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_record')

 340            BUILD_MAP                3
        L2:     RETURN_VALUE

 345    L3:     LOAD_GLOBAL              5 (_clamp_score + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               7 ('confidence_score')
                CALL                     1
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                LOAD_CONST               8 (0.0)
        L6:     STORE_FAST               1 (c)

 346            LOAD_GLOBAL              5 (_clamp_score + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               9 ('risk_score')
                CALL                     1
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_CONST               8 (0.0)
        L9:     STORE_FAST               2 (r)

 347            LOAD_GLOBAL              5 (_clamp_score + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              10 ('usefulness_score')
                CALL                     1
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST               8 (0.0)
       L12:     STORE_FAST               3 (u)

 348            LOAD_FAST_BORROW         3 (u)
                LOAD_CONST              11 (1.0)
                LOAD_FAST_BORROW         2 (r)
                BINARY_OP               10 (-)
                BINARY_OP                5 (*)
                LOAD_FAST_BORROW         1 (c)
                BINARY_OP                5 (*)
                STORE_FAST               4 (overall)

 349            LOAD_FAST_BORROW         4 (overall)
                LOAD_CONST               8 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 350            LOAD_CONST               8 (0.0)
                STORE_FAST               4 (overall)

 351   L13:     LOAD_FAST_BORROW         4 (overall)
                LOAD_CONST              11 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 352            LOAD_CONST              11 (1.0)
                STORE_FAST               4 (overall)

 354   L14:     LOAD_CONST               1 ('status')
                LOAD_CONST              12 ('ok')

 355            LOAD_CONST               3 ('scores')

 356            LOAD_CONST              13 ('confidence')
                LOAD_FAST_BORROW         1 (c)

 357            LOAD_CONST              14 ('risk')
                LOAD_FAST_BORROW         2 (r)

 358            LOAD_CONST              15 ('usefulness')
                LOAD_FAST_BORROW         3 (u)

 359            LOAD_CONST              16 ('overall')
                LOAD_GLOBAL              9 (round + NULL)
                LOAD_FAST_BORROW         4 (overall)
                LOAD_SMALL_INT           4
                CALL                     2

 355            BUILD_MAP                4

 361            LOAD_CONST               5 ('error_code')
                LOAD_CONST               4 (None)

 353            BUILD_MAP                3
       L15:     RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 363            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L21)
                NOT_TAKEN
                STORE_FAST               5 (e)

 364   L17:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 365            LOAD_CONST              17 ('score_learning_recommendation error type=')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 364            CALL                     1
                POP_TOP

 368            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 369            LOAD_CONST               3 ('scores')
                LOAD_CONST               4 (None)

 370            LOAD_CONST               5 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 367            BUILD_MAP                3
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               4 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 363   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L16 [0]
  L3 to L4 -> L16 [0]
  L5 to L7 -> L16 [0]
  L8 to L10 -> L16 [0]
  L11 to L15 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/learning/recommendation_engine.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object persist_learning_recommendation at 0x0000018C17F75AE0, file "app/services/learning/recommendation_engine.py", line 378>:
 378            RESUME                   0

 386            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (record)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L1)
                NOT_TAKEN

 388            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 389            LOAD_CONST               3 ('rec_row')
                LOAD_CONST               4 (None)

 390            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 391            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('invalid_record')

 387            BUILD_MAP                4
                RETURN_VALUE

 393    L1:     LOAD_FAST_BORROW         0 (record)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST               8 ('CANDIDATE')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       11 (to L2)
                NOT_TAKEN

 395            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 396            LOAD_CONST               3 ('rec_row')
                LOAD_CONST               4 (None)

 397            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 398            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('recommendation_status_must_be_candidate')

 394            BUILD_MAP                4
                RETURN_VALUE

 400    L2:     LOAD_GLOBAL              3 (dict + NULL)
                LOAD_FAST_BORROW         0 (record)
                CALL                     1
                STORE_FAST               1 (row)

 401            LOAD_CONST               8 ('CANDIDATE')
                LOAD_FAST_BORROW         1 (row)
                LOAD_CONST               1 ('status')
                STORE_SUBSCR

 402            LOAD_GLOBAL              7 (_project_metadata + NULL)
                LOAD_FAST_BORROW         1 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L3:     CALL                     1
                LOAD_FAST_BORROW         1 (row)
                LOAD_CONST              10 ('metadata')
                STORE_SUBSCR

 403            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               2 (db)

 404            LOAD_FAST_BORROW         2 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L4)
                NOT_TAKEN

 406            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('skipped')

 407            LOAD_CONST               3 ('rec_row')
                LOAD_CONST               4 (None)

 408            LOAD_CONST               5 ('warnings')
                LOAD_CONST              12 ('learning_recommendations_store_unavailable')
                BUILD_LIST               1

 409            LOAD_CONST               6 ('error_code')
                LOAD_CONST              12 ('learning_recommendations_store_unavailable')

 405            BUILD_MAP                4
                RETURN_VALUE

 411    L4:     NOP

 412    L5:     LOAD_FAST_BORROW         2 (db)
                LOAD_ATTR               11 (table + NULL|self)
                LOAD_GLOBAL             12 (_TABLE)
                CALL                     1
                LOAD_ATTR               15 (insert + NULL|self)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               3 (result)

 413            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         3 (result)
                LOAD_CONST              13 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               4 (rows)

 414            LOAD_FAST_BORROW         4 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN
       L10:     LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW         4 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L12)
       L11:     LOAD_GLOBAL             23 (_project_row + NULL)
                LOAD_FAST_BORROW         1 (row)
                CALL                     1
       L12:     STORE_FAST               5 (proj)

 416            LOAD_CONST               1 ('status')
                LOAD_CONST              14 ('ok')

 417            LOAD_CONST               3 ('rec_row')
                LOAD_FAST_BORROW         5 (proj)

 418            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 419            LOAD_CONST               6 ('error_code')
                LOAD_CONST               4 (None)

 415            BUILD_MAP                4
       L13:     RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 421            LOAD_GLOBAL             24 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 422   L15:     LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 423            LOAD_CONST              15 ('persist_learning_recommendation db error type=')

 424            LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE

 423            BUILD_STRING             2

 422            CALL                     1
                POP_TOP

 427            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('skipped')

 428            LOAD_CONST               3 ('rec_row')
                LOAD_CONST               4 (None)

 429            LOAD_CONST               5 ('warnings')
                LOAD_CONST              16 ('db_write_failed:')
                LOAD_GLOBAL             31 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               32 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 430            LOAD_CONST               6 ('error_code')
                LOAD_CONST              12 ('learning_recommendations_store_unavailable')

 426            BUILD_MAP                4
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST               4 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 421   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L14 [0]
  L7 to L9 -> L14 [0]
  L10 to L13 -> L14 [0]
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/services/learning/recommendation_engine.py", line 438>:
438           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

440           LOAD_CONST               2 ('Any')

438           LOAD_CONST               3 ('limit')

441           LOAD_CONST               4 ('int')

438           LOAD_CONST               5 ('return')

442           LOAD_CONST               6 ('Dict[str, Any]')

438           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object recommendation_report at 0x0000018C17ED78E0, file "app/services/learning/recommendation_engine.py", line 438>:
 438            RESUME                   0

 446            LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 447            LOAD_FAST_BORROW         2 (bid)
                POP_JUMP_IF_NOT_NONE    19 (to L1)
                NOT_TAKEN

 449            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 450            LOAD_CONST               4 ('brokerage_id')
                LOAD_CONST               1 (None)

 451            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 452            LOAD_CONST               6 ('by_type')
                BUILD_MAP                0

 453            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 454            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 455            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 456            LOAD_CONST              10 ('error_code')
                LOAD_CONST              11 ('missing_brokerage_id')

 448            BUILD_MAP                8
                RETURN_VALUE

 458    L1:     LOAD_GLOBAL              3 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              5 (min + NULL)
                LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_GLOBAL              8 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_SMALL_INT         100
        L3:     LOAD_CONST              12 (5000)
                CALL                     2
                CALL                     2
                STORE_FAST               3 (capped)

 459            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 460            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    20 (to L4)
                NOT_TAKEN

 462            LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('skipped')

 463            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 464            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 465            LOAD_CONST               6 ('by_type')
                BUILD_MAP                0

 466            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 467            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 468            LOAD_CONST               9 ('warnings')
                LOAD_CONST              14 ('learning_recommendations_store_unavailable')
                BUILD_LIST               1

 469            LOAD_CONST              10 ('error_code')
                LOAD_CONST              14 ('learning_recommendations_store_unavailable')

 461            BUILD_MAP                8
                RETURN_VALUE

 471    L4:     NOP

 473    L5:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_GLOBAL             14 (_TABLE)
                CALL                     1

 474            LOAD_ATTR               17 (select + NULL|self)
                LOAD_CONST              15 (',')
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_GLOBAL             20 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 475            LOAD_ATTR               23 (eq + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 476            LOAD_ATTR               25 (order + NULL|self)
                LOAD_CONST              16 ('created_at')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('desc',))
                CALL_KW                  2

 477            LOAD_ATTR               27 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 478            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 472            STORE_FAST               5 (result)

 480            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              19 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST               6 (rows)

 495    L9:     BUILD_MAP                0
                STORE_FAST               8 (by_type)

 496            BUILD_MAP                0
                STORE_FAST               9 (by_status)

 497            BUILD_LIST               0
                STORE_FAST              10 (projected)

 498            LOAD_FAST                6 (rows)
                GET_ITER
       L10:     FOR_ITER               204 (to L15)
                STORE_FAST              11 (r)

 499            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               11 (r)
                LOAD_GLOBAL             44 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN

 500            JUMP_BACKWARD           27 (to L10)

 501   L11:     LOAD_GLOBAL             47 (_project_row + NULL)
                LOAD_FAST               11 (r)
                CALL                     1
                STORE_FAST              12 (proj)

 502            LOAD_FAST               12 (proj)
                POP_JUMP_IF_NONE        18 (to L12)
                NOT_TAKEN

 503            LOAD_FAST               10 (projected)
                LOAD_ATTR               49 (append + NULL|self)
                LOAD_FAST               12 (proj)
                CALL                     1
                POP_TOP

 504   L12:     LOAD_FAST               11 (r)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_CONST              22 ('recommendation_type')
                CALL                     1
                STORE_FAST              13 (t)

 505            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               13 (t)
                LOAD_GLOBAL             52 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L13)
                NOT_TAKEN
                LOAD_FAST               13 (t)
                LOAD_GLOBAL             54 (ALLOWED_RECOMMENDATION_TYPES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       28 (to L13)
                NOT_TAKEN

 506            LOAD_FAST                8 (by_type)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_FAST               13 (t)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    141 (by_type, t)
                STORE_SUBSCR

 507   L13:     LOAD_FAST               11 (r)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                STORE_FAST              14 (s)

 508            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST               14 (s)
                LOAD_GLOBAL             52 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD          177 (to L10)

 509   L14:     LOAD_FAST                9 (by_status)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_FAST               14 (s)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_LOAD_FAST    158 (by_status, s)
                STORE_SUBSCR
                JUMP_BACKWARD          206 (to L10)

 498   L15:     END_FOR
                POP_ITER

 511            LOAD_CONST               2 ('status')
                LOAD_CONST              23 ('ok')

 512            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 513            LOAD_CONST               5 ('total')
                LOAD_GLOBAL             57 (len + NULL)
                LOAD_FAST               10 (projected)
                CALL                     1

 514            LOAD_CONST               6 ('by_type')
                LOAD_FAST                8 (by_type)

 515            LOAD_CONST               7 ('by_status')
                LOAD_FAST                9 (by_status)

 516            LOAD_CONST               8 ('rows')
                LOAD_FAST               10 (projected)

 517            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 518            LOAD_CONST              10 ('error_code')
                LOAD_CONST               1 (None)

 510            BUILD_MAP                8
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 481            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       95 (to L21)
                NOT_TAKEN
                STORE_FAST               7 (e)

 482   L17:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 483            LOAD_CONST              20 ('recommendation_report read error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 482            CALL                     1
                POP_TOP

 486            LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('skipped')

 487            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                2 (bid)

 488            LOAD_CONST               5 ('total')
                LOAD_SMALL_INT           0

 489            LOAD_CONST               6 ('by_type')
                BUILD_MAP                0

 490            LOAD_CONST               7 ('by_status')
                BUILD_MAP                0

 491            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 492            LOAD_CONST               9 ('warnings')
                LOAD_CONST              21 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 493            LOAD_CONST              10 ('error_code')
                LOAD_CONST              14 ('learning_recommendations_store_unavailable')

 485            BUILD_MAP                8
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 481   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L16 [0]
  L7 to L9 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti
```
