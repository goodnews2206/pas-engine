# operator/operator_policy_report

- **pyc:** `app\services\operator\__pycache__\operator_policy_report.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/operator_policy_report.py`
- **co_filename (from bytecode):** `app\services\operator\operator_policy_report.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS190 — Operator policy report (read-only roll-up).

Composes the existing PAS180-PAS189 operator surfaces into
a single structured envelope the cutover-operator can read
before approving a brokerage's pilot promotion or a fleet-
wide doctrine review.

Doctrine:

* **Read-only.** Every helper only READS from existing
  surfaces (PAS188 incident_log + cutover_approval +
  daily_ops_checklist + fleet_status + PAS189 circuit_
  breaker_policy + cache_invalidation). No DB writes. No
  state mutation. No autonomous remediation.
* **No PII / no secrets / no raw payloads.** The
  forbidden-token scanner is the last defence on the
  returned envelope.
* **NEVER raises.** Every underlying call is wrapped in
  try/except; failures collapse to ``status="skipped"``
  with a structural warning.
* **Bounded.** ``limit`` is clamped between 1 and 200.

Public surface:

  * ``operator_policy_report()``
        Fleet-wide policy report (every section a
        sub-envelope of counts + verdict).
  * ``brokerage_policy_report(brokerage_id)``
        Per-brokerage policy report (same sections,
        scoped).
  * ``fleet_policy_exception_report(...)``
        Subset of fleet rows where any section reports
        a non-OK verdict. Used by the daily-ops operator
        to triage.
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.operator.circuit_breaker_policy`, `app.services.operator.cutover_approval`, `app.services.operator.daily_ops_checklist`, `app.services.operator.incident_log`, `brokerage_circuit_breaker_status`, `cutover_status_report`, `daily_ops_checklist_report`, `list_incidents`, `logging`, `os`, `pathlib`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_final`, `_safe_brokerage`, `_safe_brokerage_iter`, `_safe_call`, `_scan_for_forbidden`, `_section_breaker_for_brokerage`, `_section_cutover_for_brokerage`, `_section_daily_checklist_for_brokerage`, `_section_incident_for_brokerage`, `_section_learning_mutation_posture`, `_section_migration_posture`, `_section_security_gate_posture`, `brokerage_policy_report`, `fleet_policy_exception_report`, `operator_policy_report`

## Env-key candidates

`APPROVED`, `COMPLETED`, `OPEN`, `TRIPPED`

## String constants (redacted where noted)

- '\nPAS190 — Operator policy report (read-only roll-up).\n\nComposes the existing PAS180-PAS189 operator surfaces into\na single structured envelope the cutover-operator can read\nbefore approving a brokerage\'s pilot promotion or a fleet-\nwide doctrine review.\n\nDoctrine:\n\n* **Read-only.** Every helper only READS from existing\n  surfaces (PAS188 incident_log + cutover_approval +\n  daily_ops_checklist + fleet_status + PAS189 circuit_\n  breaker_policy + cache_invalidation). No DB writes. No\n  state mutation. No autonomous remediation.\n* **No PII / no secrets / no raw payloads.** The\n  forbidden-token scanner is the last defence on the\n  returned envelope.\n* **NEVER raises.** Every underlying call is wrapped in\n  try/except; failures collapse to ``status="skipped"``\n  with a structural warning.\n* **Bounded.** ``limit`` is clamped between 1 and 200.\n\nPublic surface:\n\n  * ``operator_policy_report()``\n        Fleet-wide policy report (every section a\n        sub-envelope of counts + verdict).\n  * ``brokerage_policy_report(brokerage_id)``\n        Per-brokerage policy report (same sections,\n        scoped).\n  * ``fleet_policy_exception_report(...)``\n        Subset of fleet rows where any section reports\n        a non-OK verdict. Used by the daily-ops operator\n        to triage.\n'
- 'pas.operator.policy_report'
- 'circuit_breaker'
- 'daily_checklist'
- 'migration_posture'
- 'incident_posture'
- 'cutover_posture'
- 'security_gate_posture'
- 'learning_mutation_posture'
- 'brokerage_ids'
- 'limit'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Optional[Iterable[Any]]'
- 'List[str]'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'str'
- 'policy_report surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'policy_report_envelope_forbidden_token'
- 'warnings'
- 'Optional[Dict[str, Any]]'
- 'Call a section helper; never raises. Returns the\ndict envelope on success or None on any exception.'
- 'policy_report section call failed type='
- 'brokerage_id'
- 'section'
- 'skipped'
- 'tripped'
- 'policy_import_failed'
- 'policy_call_failed'
- 'row'
- 'TRIPPED'
- 'row_status'
- 'reason_code'
- 'completed_count'
- 'failed_count'
- 'daily_ops_import_failed'
- 'daily_ops_call_failed'
- 'rows'
- 'rows_inspected'
- 'COMPLETED'
- 'open_count'
- 'incident_log_import_failed'
- 'OPEN'
- 'incident_log_call_failed'
- 'open_request_count'
- 'cutover_import_failed'
- 'cutover_call_failed'
- 'approved_count'
- 'APPROVED'
- 'Static check: count v37 / v38 proposals on disk +\ndetect any vN > 38 unratified migration.'
- 'scripts'
- 'count'
- 'scripts_dir_unavailable'
- 'migrate_v'
- '.sql'
- 'proposal_count'
- 'unratified'
- '_section_migration_posture error type='
- 'unexpected:'
- 'Static check: confirm PAS-SECURITY-01..04 readiness\nscripts are on disk.'
- 'missing'
- 'Static check: confirm PAS179 governance carry-forward\n(worker OFF + no autopilot flag default-true).'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- 'utf-8'
- 'replace'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker_off_default'
- 'autopilot_enabled'
- 'adaptive_autowrite'
- 'Per-brokerage policy report. Composes 5 brokerage-\nscoped sections + 2 fleet-scoped sections (migration +\nsecurity gate + learning mutation).'
- 'ops.policy_report.brokerage'
- 'invalid_brokerage_id'
- 'review_required'
- 'sections'
- 'section_count'
- 'non_ok_count'
- 'brokerage_policy_report error type='
- 'Fleet-wide policy report. If ``brokerage_ids`` is\nsupplied, scopes the per-brokerage sections to that\nset. Otherwise it returns the global posture sections\nonly (migration, security gate, learning mutation).\n\nReturns a structural envelope. NEVER raises.'
- 'ops.policy_report.fleet'
- 'global_sections'
- 'per_brokerage'
- 'per_brokerage_count'
- 'operator_policy_report error type='
- 'Sub-set of fleet brokerages whose overall policy\nreport is not ``ok``. Used by the daily-ops operator\nto triage.'
- 'ops.policy_report.exceptions'
- 'fleet_policy_exception_report error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS190 — Operator policy report (read-only roll-up).\n\nComposes the existing PAS180-PAS189 operator surfaces into\na single structured envelope the cutover-operator can read\nbefore approving a brokerage\'s pilot promotion or a fleet-\nwide doctrine review.\n\nDoctrine:\n\n* **Read-only.** Every helper only READS from existing\n  surfaces (PAS188 incident_log + cutover_approval +\n  daily_ops_checklist + fleet_status + PAS189 circuit_\n  breaker_policy + cache_invalidation). No DB writes. No\n  state mutation. No autonomous remediation.\n* **No PII / no secrets / no raw payloads.** The\n  forbidden-token scanner is the last defence on the\n  returned envelope.\n* **NEVER raises.** Every underlying call is wrapped in\n  try/except; failures collapse to ``status="skipped"``\n  with a structural warning.\n* **Bounded.** ``limit`` is clamped between 1 and 200.\n\nPublic surface:\n\n  * ``operator_policy_report()``\n        Fleet-wide policy report (every section a\n        sub-envelope of counts + verdict).\n  * ``brokerage_policy_report(brokerage_id)``\n        Per-brokerage policy report (same sections,\n        scoped).\n  * ``fleet_policy_exception_report(...)``\n        Subset of fleet rows where any section reports\n        a non-OK verdict. Used by the daily-ops operator\n        to triage.\n')
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
              LOAD_CONST               3 (('Any', 'Dict', 'Iterable', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (Iterable)
              STORE_NAME               7 (Iterable)
              IMPORT_FROM              8 (List)
              STORE_NAME               8 (List)
              IMPORT_FROM              9 (Optional)
              STORE_NAME               9 (Optional)
              POP_TOP

 44           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.operator.policy_report')
              CALL                     1
              STORE_NAME              11 (logger)

 51           LOAD_SMALL_INT         200
              STORE_NAME              12 (_BROKERAGE_ID_MAX_LEN)

 52           LOAD_SMALL_INT          50
              STORE_NAME              13 (_LIMIT_DEFAULT)

 53           LOAD_SMALL_INT           1
              STORE_NAME              14 (_LIMIT_MIN)

 54           LOAD_SMALL_INT         200
              STORE_NAME              15 (_LIMIT_MAX)

 56           LOAD_CONST              44 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values', 'operator_notes', 'webhook_url'))
              STORE_NAME              16 (_FORBIDDEN_RESPONSE_TOKENS)

 66           LOAD_CONST               5 ('circuit_breaker')
              STORE_NAME              17 (_SECTION_BREAKER)

 67           LOAD_CONST               6 ('daily_checklist')
              STORE_NAME              18 (_SECTION_DAILY_CHECKLIST)

 68           LOAD_CONST               7 ('migration_posture')
              STORE_NAME              19 (_SECTION_MIGRATION)

 69           LOAD_CONST               8 ('incident_posture')
              STORE_NAME              20 (_SECTION_INCIDENT)

 70           LOAD_CONST               9 ('cutover_posture')
              STORE_NAME              21 (_SECTION_CUTOVER)

 71           LOAD_CONST              10 ('security_gate_posture')
              STORE_NAME              22 (_SECTION_SECURITY)

 72           LOAD_CONST              11 ('learning_mutation_posture')
              STORE_NAME              23 (_SECTION_LEARNING)

 79           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\operator_policy_report.py", line 79>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _safe_brokerage at 0x0000018C17F96420, file "app\services\operator\operator_policy_report.py", line 79>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_safe_brokerage)

 88           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\operator_policy_report.py", line 88>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _safe_brokerage_iter at 0x0000018C180483B0, file "app\services\operator\operator_policy_report.py", line 88>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_safe_brokerage_iter)

103           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\operator_policy_report.py", line 103>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _scan_for_forbidden at 0x0000018C18024C30, file "app\services\operator\operator_policy_report.py", line 103>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_scan_for_forbidden)

127           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025530, file "app\services\operator\operator_policy_report.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _final at 0x0000018C17FE1920, file "app\services\operator\operator_policy_report.py", line 127>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_final)

143           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\operator_policy_report.py", line 143>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _safe_call at 0x0000018C18060DB0, file "app\services\operator\operator_policy_report.py", line 143>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_call)

164           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\operator_policy_report.py", line 164>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _section_breaker_for_brokerage at 0x0000018C17D8C5C0, file "app\services\operator\operator_policy_report.py", line 164>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_section_breaker_for_brokerage)

188           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\operator_policy_report.py", line 188>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _section_daily_checklist_for_brokerage at 0x0000018C17D76780, file "app\services\operator\operator_policy_report.py", line 188>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_section_daily_checklist_for_brokerage)

219           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\operator_policy_report.py", line 219>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _section_incident_for_brokerage at 0x0000018C179C3A50, file "app\services\operator\operator_policy_report.py", line 219>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_section_incident_for_brokerage)

238           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\operator_policy_report.py", line 238>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _section_cutover_for_brokerage at 0x0000018C17D77E00, file "app\services\operator\operator_policy_report.py", line 238>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_section_cutover_for_brokerage)

275           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\operator_policy_report.py", line 275>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _section_migration_posture at 0x0000018C17F6A360, file "app\services\operator\operator_policy_report.py", line 275>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_section_migration_posture)

327           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\operator_policy_report.py", line 327>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _section_security_gate_posture at 0x0000018C17D7CFB0, file "app\services\operator\operator_policy_report.py", line 327>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_section_security_gate_posture)

356           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\operator_policy_report.py", line 356>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _section_learning_mutation_posture at 0x0000018C17EE1CC0, file "app\services\operator\operator_policy_report.py", line 356>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_section_learning_mutation_posture)

391           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA3D20, file "app\services\operator\operator_policy_report.py", line 391>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object brokerage_policy_report at 0x0000018C17F6A820, file "app\services\operator\operator_policy_report.py", line 391>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (brokerage_policy_report)

442           LOAD_CONST              38 ('brokerage_ids')

444           LOAD_CONST               2 (None)

442           LOAD_CONST              39 ('limit')

445           LOAD_NAME               13 (_LIMIT_DEFAULT)

442           BUILD_MAP                2
              LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18026130, file "app\services\operator\operator_policy_report.py", line 442>)
              MAKE_FUNCTION
              LOAD_CONST              41 (<code object operator_policy_report at 0x0000018C17E89970, file "app\services\operator\operator_policy_report.py", line 442>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              37 (operator_policy_report)

507           LOAD_CONST              38 ('brokerage_ids')

509           LOAD_CONST               2 (None)

507           LOAD_CONST              39 ('limit')

510           LOAD_NAME               13 (_LIMIT_DEFAULT)

507           BUILD_MAP                2
              LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18026230, file "app\services\operator\operator_policy_report.py", line 507>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object fleet_policy_exception_report at 0x0000018C17E94650, file "app\services\operator\operator_policy_report.py", line 507>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (fleet_policy_exception_report)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\operator_policy_report.py", line 79>:
 79           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F96420, file "app\services\operator\operator_policy_report.py", line 79>:
 79           RESUME                   0

 80           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 81           LOAD_CONST               0 (None)
              RETURN_VALUE

 82   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 83           LOAD_FAST_BORROW         1 (s)
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

 84   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

 85   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\operator_policy_report.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')
              LOAD_CONST               2 ('Optional[Iterable[Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_brokerage_iter at 0x0000018C180483B0, file "app\services\operator\operator_policy_report.py", line 88>:
 88           RESUME                   0

 89           LOAD_FAST_BORROW         0 (brokerage_ids)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 90           BUILD_LIST               0
              RETURN_VALUE

 91   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

 92           LOAD_GLOBAL              1 (set + NULL)
              CALL                     0
              STORE_FAST               2 (seen)

 93           LOAD_FAST_BORROW         0 (brokerage_ids)
              GET_ITER
      L2:     FOR_ITER                85 (to L5)
              STORE_FAST               3 (v)

 94           LOAD_GLOBAL              3 (_safe_brokerage + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              STORE_FAST               4 (s)

 95           LOAD_FAST_BORROW         4 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       41 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (s, seen)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       35 (to L3)
              NOT_TAKEN

 96           LOAD_FAST_BORROW         2 (seen)
              LOAD_ATTR                5 (add + NULL|self)
              LOAD_FAST_BORROW         4 (s)
              CALL                     1
              POP_TOP

 97           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         4 (s)
              CALL                     1
              POP_TOP

 98   L3:     LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              LOAD_GLOBAL             10 (_LIMIT_MAX)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           84 (to L2)

 99   L4:     POP_TOP

100           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

 93   L5:     END_FOR
              POP_ITER

100           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\operator_policy_report.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18024C30, file "app\services\operator\operator_policy_report.py", line 103>:
  --           MAKE_CELL                1 (walk)

 103           RESUME                   0

 104           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\operator_policy_report.py", line 104>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2E60, file "app\services\operator\operator_policy_report.py", line 104>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 124           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\operator_policy_report.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2E60, file "app\services\operator\operator_policy_report.py", line 104>:
  --            COPY_FREE_VARS           1

 104            RESUME                   0

 105            NOP

 106    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 107    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 108            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 109            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 110            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 111            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 112    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 110    L9:     END_FOR
                POP_ITER

 113   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 114            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 115   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 107   L14:     END_FOR
                POP_ITER

 123   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 116   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 117            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 118            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 119            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 120   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 117   L21:     END_FOR
                POP_ITER

 123   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 121            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 122   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 121   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\operator\operator_policy_report.py", line 127>:
127           RESUME                   0
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

Disassembly of <code object _final at 0x0000018C17FE1920, file "app\services\operator\operator_policy_report.py", line 127>:
127           RESUME                   0

128           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

129           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

130           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

131           LOAD_CONST               0 ('policy_report surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

130           CALL                     1
              POP_TOP

135           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

136           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

137           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('policy_report_envelope_forbidden_token')

138           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('policy_report_envelope_forbidden_token')
              BUILD_LIST               1

134           BUILD_MAP                4
              RETURN_VALUE

140   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\operator_policy_report.py", line 143>:
143           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _safe_call at 0x0000018C18060DB0, file "app\services\operator\operator_policy_report.py", line 143>:
 143            RESUME                   0

 146            LOAD_FAST_BORROW         0 (fn)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 147            LOAD_CONST               1 (None)
                RETURN_VALUE

 148    L1:     NOP

 149    L2:     LOAD_FAST_BORROW         0 (fn)
                PUSH_NULL
                LOAD_CONST               3 (())
                BUILD_MAP                0
                LOAD_FAST_BORROW         1 (kwargs)
                DICT_MERGE               1
                CALL_FUNCTION_EX
                STORE_FAST               2 (out)

 155    L3:     LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST                2 (out)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 156            LOAD_FAST                2 (out)
                RETURN_VALUE

 157    L4:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 150            LOAD_GLOBAL              0 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 151    L6:     LOAD_GLOBAL              2 (logger)
                LOAD_ATTR                5 (warning + NULL|self)

 152            LOAD_CONST               2 ('policy_report section call failed type=')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 151            CALL                     1
                POP_TOP

 154    L7:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 150    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\operator_policy_report.py", line 164>:
164           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _section_breaker_for_brokerage at 0x0000018C17D8C5C0, file "app\services\operator\operator_policy_report.py", line 164>:
 164           RESUME                   0

 165           NOP

 166   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('brokerage_circuit_breaker_status',))
               IMPORT_NAME              0 (app.services.operator.circuit_breaker_policy)
               IMPORT_FROM              1 (brokerage_circuit_breaker_status)
               STORE_FAST               1 (brokerage_circuit_breaker_status)
               POP_TOP

 172   L2:     LOAD_GLOBAL              9 (_safe_call + NULL)
               LOAD_FAST                1 (brokerage_circuit_breaker_status)

 173           LOAD_FAST                0 (brokerage_id)

 172           LOAD_CONST               9 (('brokerage_id',))
               CALL_KW                  2
               STORE_FAST               2 (env)

 174           LOAD_FAST                2 (env)
               POP_JUMP_IF_NOT_NONE    15 (to L3)
               NOT_TAKEN

 175           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_BREAKER)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 176           LOAD_CONST               5 ('tripped')
               LOAD_CONST               6 (False)
               LOAD_CONST               7 ('error_code')
               LOAD_CONST              10 ('policy_call_failed')

 175           BUILD_MAP                4
               RETURN_VALUE

 177   L3:     LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              11 ('row')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L4:     STORE_FAST               3 (row)

 178           LOAD_GLOBAL             13 (str + NULL)
               LOAD_FAST                3 (row)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               3 ('status')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              12 ('OK')
       L5:     CALL                     1
               LOAD_ATTR               15 (upper + NULL|self)
               CALL                     0
               STORE_FAST               4 (status)

 180           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_BREAKER)

 181           LOAD_CONST               3 ('status')
               LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               3 ('status')
               LOAD_CONST              13 ('ok')
               CALL                     2

 182           LOAD_CONST               5 ('tripped')
               LOAD_FAST                4 (status)
               LOAD_CONST              14 ('TRIPPED')
               COMPARE_OP              72 (==)

 183           LOAD_CONST              15 ('row_status')
               LOAD_FAST                4 (status)

 184           LOAD_CONST              16 ('reason_code')
               LOAD_FAST                3 (row)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              16 ('reason_code')
               CALL                     1

 179           BUILD_MAP                5
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 169           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       18 (to L8)
               NOT_TAKEN
               POP_TOP

 170           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_BREAKER)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 171           LOAD_CONST               5 ('tripped')
               LOAD_CONST               6 (False)
               LOAD_CONST               7 ('error_code')
               LOAD_CONST               8 ('policy_import_failed')

 170           BUILD_MAP                4
               SWAP                     2
       L7:     POP_EXCEPT
               RETURN_VALUE

 169   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\operator_policy_report.py", line 188>:
188           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _section_daily_checklist_for_brokerage at 0x0000018C17D76780, file "app\services\operator\operator_policy_report.py", line 188>:
 188           RESUME                   0

 189           NOP

 190   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('daily_ops_checklist_report',))
               IMPORT_NAME              0 (app.services.operator.daily_ops_checklist)
               IMPORT_FROM              1 (daily_ops_checklist_report)
               STORE_FAST               1 (daily_ops_checklist_report)
               POP_TOP

 197   L2:     LOAD_GLOBAL              9 (_safe_call + NULL)
               LOAD_FAST                1 (daily_ops_checklist_report)

 198           LOAD_FAST                0 (brokerage_id)
               LOAD_SMALL_INT          10

 197           LOAD_CONST               9 (('brokerage_id', 'limit'))
               CALL_KW                  3
               STORE_FAST               2 (env)

 199           LOAD_FAST                2 (env)
               POP_JUMP_IF_NOT_NONE    17 (to L3)
               NOT_TAKEN

 200           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_DAILY_CHECKLIST)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 201           LOAD_CONST               5 ('completed_count')
               LOAD_SMALL_INT           0
               LOAD_CONST               6 ('failed_count')
               LOAD_SMALL_INT           0

 202           LOAD_CONST               7 ('error_code')
               LOAD_CONST              10 ('daily_ops_call_failed')

 200           BUILD_MAP                5
               RETURN_VALUE

 203   L3:     LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              11 ('rows')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L4:     STORE_FAST               3 (rows)

 204           LOAD_GLOBAL             13 (sum + NULL)
               LOAD_CONST              12 (<code object <genexpr> at 0x0000018C1804CED0, file "app\services\operator\operator_policy_report.py", line 204>)
               MAKE_FUNCTION
               LOAD_FAST                3 (rows)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               4 (completed)

 207           LOAD_GLOBAL             13 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C1804D070, file "app\services\operator\operator_policy_report.py", line 207>)
               MAKE_FUNCTION
               LOAD_FAST                3 (rows)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               5 (failed)

 211           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_DAILY_CHECKLIST)

 212           LOAD_CONST               3 ('status')
               LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               3 ('status')
               LOAD_CONST              14 ('ok')
               CALL                     2

 213           LOAD_CONST              15 ('rows_inspected')
               LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST                3 (rows)
               CALL                     1

 214           LOAD_CONST               5 ('completed_count')
               LOAD_FAST                4 (completed)

 215           LOAD_CONST               6 ('failed_count')
               LOAD_FAST                5 (failed)

 210           BUILD_MAP                5
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 193           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       20 (to L7)
               NOT_TAKEN
               POP_TOP

 194           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_DAILY_CHECKLIST)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 195           LOAD_CONST               5 ('completed_count')
               LOAD_SMALL_INT           0
               LOAD_CONST               6 ('failed_count')
               LOAD_SMALL_INT           0

 196           LOAD_CONST               7 ('error_code')
               LOAD_CONST               8 ('daily_ops_import_failed')

 194           BUILD_MAP                5
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 193   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804CED0, file "app\services\operator\operator_policy_report.py", line 204>:
 204            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)
        L2:     FOR_ITER                88 (to L10)
                STORE_FAST               1 (r)

 205            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL

 204    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L2)

 206    L4:     LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               0 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               1 ('')
        L7:     CALL                     1
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_CONST               2 ('COMPLETED')
                COMPARE_OP              88 (bool(==))

 204    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           84 (to L2)
        L9:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           90 (to L2)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L11 [0] lasti
  L6 to L8 -> L11 [0] lasti
  L9 to L11 -> L11 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804D070, file "app\services\operator\operator_policy_report.py", line 207>:
 207            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)
        L2:     FOR_ITER                88 (to L10)
                STORE_FAST               1 (r)

 208            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL

 207    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L2)

 209    L4:     LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               0 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               1 ('')
        L7:     CALL                     1
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_CONST               3 (('FAILED', 'PARTIAL'))
                CONTAINS_OP              0 (in)

 207    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           84 (to L2)
        L9:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           90 (to L2)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L11 [0] lasti
  L6 to L8 -> L11 [0] lasti
  L9 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\operator_policy_report.py", line 219>:
219           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _section_incident_for_brokerage at 0x0000018C179C3A50, file "app\services\operator\operator_policy_report.py", line 219>:
 219           RESUME                   0

 220           NOP

 221   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('list_incidents',))
               IMPORT_NAME              0 (app.services.operator.incident_log)
               IMPORT_FROM              1 (list_incidents)
               STORE_FAST               1 (list_incidents)
               POP_TOP

 225   L2:     LOAD_GLOBAL              9 (_safe_call + NULL)
               LOAD_FAST                1 (list_incidents)

 226           LOAD_FAST                0 (brokerage_id)
               LOAD_CONST               8 ('OPEN')
               LOAD_SMALL_INT          50

 225           LOAD_CONST               9 (('brokerage_id', 'status', 'limit'))
               CALL_KW                  4
               STORE_FAST               2 (env)

 227           LOAD_FAST                2 (env)
               POP_JUMP_IF_NOT_NONE    15 (to L3)
               NOT_TAKEN

 228           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_INCIDENT)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 229           LOAD_CONST               5 ('open_count')
               LOAD_SMALL_INT           0
               LOAD_CONST               6 ('error_code')
               LOAD_CONST              10 ('incident_log_call_failed')

 228           BUILD_MAP                4
               RETURN_VALUE

 230   L3:     LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              11 ('rows')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L4:     STORE_FAST               3 (rows)

 232           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_INCIDENT)

 233           LOAD_CONST               3 ('status')
               LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               3 ('status')
               LOAD_CONST              12 ('ok')
               CALL                     2

 234           LOAD_CONST               5 ('open_count')
               LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST                3 (rows)
               CALL                     1

 231           BUILD_MAP                3
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 222           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN
               POP_TOP

 223           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_INCIDENT)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 224           LOAD_CONST               5 ('open_count')
               LOAD_SMALL_INT           0
               LOAD_CONST               6 ('error_code')
               LOAD_CONST               7 ('incident_log_import_failed')

 223           BUILD_MAP                4
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 222   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\operator_policy_report.py", line 238>:
238           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _section_cutover_for_brokerage at 0x0000018C17D77E00, file "app\services\operator\operator_policy_report.py", line 238>:
 238           RESUME                   0

 239           NOP

 240   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('cutover_status_report',))
               IMPORT_NAME              0 (app.services.operator.cutover_approval)
               IMPORT_FROM              1 (cutover_status_report)
               STORE_FAST               1 (cutover_status_report)
               POP_TOP

 247   L2:     LOAD_GLOBAL              9 (_safe_call + NULL)
               LOAD_FAST                1 (cutover_status_report)

 248           LOAD_FAST                0 (brokerage_id)
               LOAD_SMALL_INT          20

 247           LOAD_CONST               8 (('brokerage_id', 'limit'))
               CALL_KW                  3
               STORE_FAST               2 (env)

 249           LOAD_FAST                2 (env)
               POP_JUMP_IF_NOT_NONE    15 (to L3)
               NOT_TAKEN

 250           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_CUTOVER)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 251           LOAD_CONST               5 ('open_request_count')
               LOAD_SMALL_INT           0

 252           LOAD_CONST               6 ('error_code')
               LOAD_CONST               9 ('cutover_call_failed')

 250           BUILD_MAP                4
               RETURN_VALUE

 253   L3:     LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST              10 ('rows')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L4:     STORE_FAST               3 (rows)

 254           LOAD_GLOBAL             13 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C1804CD30, file "app\services\operator\operator_policy_report.py", line 254>)
               MAKE_FUNCTION

 255           LOAD_FAST                3 (rows)
               GET_ITER

 254           CALL                     0
               CALL                     1
               STORE_FAST               4 (open_requested)

 261           LOAD_GLOBAL             13 (sum + NULL)
               LOAD_CONST              12 (<code object <genexpr> at 0x0000018C1804D550, file "app\services\operator\operator_policy_report.py", line 261>)
               MAKE_FUNCTION

 262           LOAD_FAST                3 (rows)
               GET_ITER

 261           CALL                     0
               CALL                     1
               STORE_FAST               5 (approved)

 267           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_CUTOVER)

 268           LOAD_CONST               3 ('status')
               LOAD_FAST                2 (env)
               LOAD_ATTR               11 (get + NULL|self)
               LOAD_CONST               3 ('status')
               LOAD_CONST              13 ('ok')
               CALL                     2

 269           LOAD_CONST              14 ('rows_inspected')
               LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST                3 (rows)
               CALL                     1

 270           LOAD_CONST               5 ('open_request_count')
               LOAD_FAST                4 (open_requested)

 271           LOAD_CONST              15 ('approved_count')
               LOAD_FAST                5 (approved)

 266           BUILD_MAP                5
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 243           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN
               POP_TOP

 244           LOAD_CONST               2 ('section')
               LOAD_GLOBAL              6 (_SECTION_CUTOVER)
               LOAD_CONST               3 ('status')
               LOAD_CONST               4 ('skipped')

 245           LOAD_CONST               5 ('open_request_count')
               LOAD_SMALL_INT           0

 246           LOAD_CONST               6 ('error_code')
               LOAD_CONST               7 ('cutover_import_failed')

 244           BUILD_MAP                4
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 243   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804CD30, file "app\services\operator\operator_policy_report.py", line 254>:
 254            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)

 255    L2:     FOR_ITER                88 (to L10)
                STORE_FAST               1 (r)

 256            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL

 255    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L2)

 257    L4:     LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               0 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               1 ('')
        L7:     CALL                     1
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_CONST               3 (('REQUESTED', 'FIRST_APPROVED'))
                CONTAINS_OP              0 (in)

 255    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           84 (to L2)
        L9:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           90 (to L2)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L11 [0] lasti
  L6 to L8 -> L11 [0] lasti
  L9 to L11 -> L11 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1804D550, file "app\services\operator\operator_policy_report.py", line 261>:
 261            RETURN_GENERATOR
                POP_TOP
        L1:     RESUME                   0
                LOAD_FAST                0 (.0)

 262    L2:     FOR_ITER                88 (to L10)
                STORE_FAST               1 (r)

 263            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL

 262    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L2)

 264    L4:     LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         1 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               0 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_CONST               1 ('')
        L7:     CALL                     1
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_CONST               2 ('APPROVED')
                COMPARE_OP              88 (bool(==))

 262    L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           84 (to L2)
        L9:     LOAD_SMALL_INT           1
                YIELD_VALUE              0
                RESUME                   5
                POP_TOP
                JUMP_BACKWARD           90 (to L2)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L11:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0] lasti
  L4 to L5 -> L11 [0] lasti
  L6 to L8 -> L11 [0] lasti
  L9 to L11 -> L11 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\operator_policy_report.py", line 275>:
275           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _section_migration_posture at 0x0000018C17F6A360, file "app\services\operator\operator_policy_report.py", line 275>:
 275            RESUME                   0

 278            NOP

 279    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('Path',))
                IMPORT_NAME              0 (pathlib)
                IMPORT_FROM              1 (Path)
                STORE_FAST               0 (Path)
                POP_TOP

 284            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              2 (os)
                STORE_FAST               1 (os)

 285            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR                9 (abspath + NULL|self)

 286            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               11 (join + NULL|self)
                LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               13 (dirname + NULL|self)
                LOAD_GLOBAL             14 (__file__)
                CALL                     1
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                CALL                     4

 285            CALL                     1
                STORE_FAST               2 (repo_root)

 288            LOAD_FAST_BORROW         0 (Path)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (repo_root)
                CALL                     1
                LOAD_CONST               4 ('scripts')
                BINARY_OP               11 (/)
                STORE_FAST               3 (scripts_dir)

 289            LOAD_FAST_BORROW         3 (scripts_dir)
                LOAD_ATTR               17 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L5)
        L2:     NOT_TAKEN

 290    L3:     LOAD_CONST               5 ('section')
                LOAD_GLOBAL             18 (_SECTION_MIGRATION)
                LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('skipped')

 291            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 292            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 ('scripts_dir_unavailable')

 290            BUILD_MAP                4
        L4:     RETURN_VALUE

 293    L5:     LOAD_SMALL_INT          38
                STORE_FAST               4 (v_max_known)

 294            BUILD_LIST               0
                STORE_FAST               5 (unratified)

 295            LOAD_SMALL_INT           0
                STORE_FAST               6 (proposals)

 296            LOAD_FAST_BORROW         3 (scripts_dir)
                LOAD_ATTR               21 (iterdir + NULL|self)
                CALL                     0
                GET_ITER
        L6:     FOR_ITER               180 (to L16)
                STORE_FAST               7 (entry)

 297            LOAD_FAST_BORROW         7 (entry)
                LOAD_ATTR               22 (name)
                STORE_FAST               8 (name)

 298            LOAD_FAST_BORROW         8 (name)
                LOAD_ATTR               25 (startswith + NULL|self)
                LOAD_CONST              11 ('migrate_v')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN

 299            JUMP_BACKWARD           40 (to L6)

 300    L7:     LOAD_FAST_BORROW         8 (name)
                LOAD_ATTR               27 (endswith + NULL|self)
                LOAD_CONST              12 ('.sql')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN

 301    L9:     JUMP_BACKWARD           65 (to L6)

 302   L10:     NOP

 303   L11:     LOAD_FAST_BORROW         8 (name)
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_CONST              11 ('migrate_v')
                CALL                     1
                LOAD_CONST               2 (None)
                BINARY_SLICE
                STORE_FAST               9 (tail)

 304            LOAD_FAST_BORROW         9 (tail)
                LOAD_ATTR               31 (split + NULL|self)
                LOAD_CONST              13 ('_')
                LOAD_SMALL_INT           1
                CALL                     2
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               31 (split + NULL|self)
                LOAD_CONST              14 ('.')
                LOAD_SMALL_INT           1
                CALL                     2
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              10 (num_str)

 305            LOAD_GLOBAL             33 (int + NULL)
                LOAD_FAST_BORROW        10 (num_str)
                CALL                     1
                STORE_FAST              11 (n)

 308   L12:     LOAD_FAST               11 (n)
                LOAD_CONST              21 ((37, 38))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       10 (to L13)
                NOT_TAKEN

 309            LOAD_FAST                6 (proposals)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               6 (proposals)

 310   L13:     LOAD_FAST_LOAD_FAST    180 (n, v_max_known)
                COMPARE_OP             148 (bool(>))
       L14:     POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD          163 (to L6)

 311   L15:     LOAD_FAST                5 (unratified)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_FAST                8 (name)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          182 (to L6)

 296   L16:     END_FOR
                POP_ITER

 313            LOAD_CONST               5 ('section')
                LOAD_GLOBAL             18 (_SECTION_MIGRATION)

 314            LOAD_CONST               6 ('status')
                LOAD_FAST_BORROW         5 (unratified)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     LOAD_CONST              15 ('ok')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST              16 ('failed')

 315   L20:     LOAD_CONST              17 ('proposal_count')
                LOAD_FAST_BORROW         6 (proposals)

 316            LOAD_CONST              18 ('unratified')
                LOAD_FAST_BORROW         5 (unratified)

 312            BUILD_MAP                4
       L21:     RETURN_VALUE

  --   L22:     PUSH_EXC_INFO

 306            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L24)
                NOT_TAKEN
                POP_TOP

 307   L23:     POP_EXCEPT
                JUMP_BACKWARD          222 (to L6)

 306   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L26:     PUSH_EXC_INFO

 318            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       90 (to L31)
                NOT_TAKEN
                STORE_FAST              12 (e)

 319   L27:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 320            LOAD_CONST              19 ('_section_migration_posture error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 319            CALL                     1
                POP_TOP

 322            LOAD_CONST               5 ('section')
                LOAD_GLOBAL             18 (_SECTION_MIGRATION)
                LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('skipped')

 323            LOAD_CONST               8 ('count')
                LOAD_SMALL_INT           0

 324            LOAD_CONST               9 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 322            BUILD_MAP                4
       L28:     SWAP                     2
       L29:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L30:     LOAD_CONST               2 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 318   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L26 [0]
  L3 to L4 -> L26 [0]
  L5 to L8 -> L26 [0]
  L9 to L10 -> L26 [0]
  L11 to L12 -> L22 [1]
  L12 to L14 -> L26 [0]
  L15 to L17 -> L26 [0]
  L18 to L21 -> L26 [0]
  L22 to L23 -> L25 [2] lasti
  L23 to L24 -> L26 [0]
  L24 to L25 -> L25 [2] lasti
  L25 to L26 -> L26 [0]
  L26 to L27 -> L32 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L28 to L29 -> L32 [1] lasti
  L30 to L32 -> L32 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\operator_policy_report.py", line 327>:
327           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _section_security_gate_posture at 0x0000018C17D7CFB0, file "app\services\operator\operator_policy_report.py", line 327>:
 327            RESUME                   0

 330            NOP

 331    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('Path',))
                IMPORT_NAME              0 (pathlib)
                IMPORT_FROM              1 (Path)
                STORE_FAST               0 (Path)
                POP_TOP

 332            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              2 (os)
                STORE_FAST               1 (os)

 333            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR                9 (abspath + NULL|self)

 334            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               11 (join + NULL|self)
                LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               13 (dirname + NULL|self)
                LOAD_GLOBAL             14 (__file__)
                CALL                     1
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                CALL                     4

 333            CALL                     1
                STORE_FAST               2 (repo_root)

 336            LOAD_CONST              12 (('scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
                STORE_FAST               3 (files)

 342            BUILD_LIST               0
                STORE_FAST               4 (missing)

 343            LOAD_FAST_BORROW         3 (files)
                GET_ITER
        L2:     FOR_ITER                57 (to L5)
                STORE_FAST               5 (relpath)

 344            LOAD_FAST_BORROW         0 (Path)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         5 (relpath)
                BINARY_OP               11 (/)
                LOAD_ATTR               17 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
        L3:     POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           40 (to L2)

 345    L4:     LOAD_FAST_BORROW         4 (missing)
                LOAD_ATTR               19 (append + NULL|self)
                LOAD_FAST_BORROW         5 (relpath)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           59 (to L2)

 343    L5:     END_FOR
                POP_ITER

 347            LOAD_CONST               4 ('section')
                LOAD_GLOBAL             20 (_SECTION_SECURITY)

 348            LOAD_CONST               5 ('status')
                LOAD_FAST_BORROW         4 (missing)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     LOAD_CONST               6 ('ok')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               7 ('failed')

 349    L9:     LOAD_CONST               8 ('missing')
                LOAD_FAST_BORROW         4 (missing)

 346            BUILD_MAP                3
       L10:     RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 351            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L16)
                NOT_TAKEN
                STORE_FAST               6 (e)

 352   L12:     LOAD_CONST               4 ('section')
                LOAD_GLOBAL             20 (_SECTION_SECURITY)
                LOAD_CONST               5 ('status')
                LOAD_CONST               9 ('skipped')

 353            LOAD_CONST              10 ('error_code')
                LOAD_CONST              11 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 352            BUILD_MAP                3
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 351   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L11 [0]
  L4 to L6 -> L11 [0]
  L7 to L10 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\operator_policy_report.py", line 356>:
356           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _section_learning_mutation_posture at 0x0000018C17EE1CC0, file "app\services\operator\operator_policy_report.py", line 356>:
 356            RESUME                   0

 359            NOP

 360    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('Path',))
                IMPORT_NAME              0 (pathlib)
                IMPORT_FROM              1 (Path)
                STORE_FAST               0 (Path)
                POP_TOP

 361            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              2 (os)
                STORE_FAST               1 (os)

 362            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR                9 (abspath + NULL|self)

 363            LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               11 (join + NULL|self)
                LOAD_FAST_BORROW         1 (os)
                LOAD_ATTR                6 (path)
                LOAD_ATTR               13 (dirname + NULL|self)
                LOAD_GLOBAL             14 (__file__)
                CALL                     1
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                LOAD_CONST               3 ('..')
                CALL                     4

 362            CALL                     1
                STORE_FAST               2 (repo_root)

 365            LOAD_FAST_BORROW         0 (Path)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (repo_root)
                CALL                     1
                LOAD_CONST               4 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               5 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               6 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               7 ('worker.py')
                BINARY_OP               11 (/)
                STORE_FAST               3 (worker_path)

 366            LOAD_CONST               8 ('')
                STORE_FAST               4 (worker_src)

 367    L2:     NOP

 368    L3:     LOAD_FAST_BORROW         3 (worker_path)
                LOAD_ATTR               17 (read_text + NULL|self)
                LOAD_CONST               9 ('utf-8')
                LOAD_CONST              10 ('replace')
                LOAD_CONST              11 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               4 (worker_src)

 372    L4:     LOAD_CONST              12 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
                LOAD_FAST_BORROW         4 (worker_src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP

 373            LOAD_CONST              13 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
                LOAD_FAST_BORROW         4 (worker_src)
                CONTAINS_OP              0 (in)

 371    L7:     STORE_FAST               5 (worker_off)

 376            LOAD_CONST              14 ('section')
                LOAD_GLOBAL             20 (_SECTION_LEARNING)

 377            LOAD_CONST              15 ('status')
                LOAD_FAST_BORROW         5 (worker_off)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
        L8:     NOT_TAKEN
        L9:     LOAD_CONST              16 ('ok')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              17 ('failed')

 378   L11:     LOAD_CONST              18 ('worker_off_default')
                LOAD_GLOBAL             23 (bool + NULL)
                LOAD_FAST_BORROW         5 (worker_off)
                CALL                     1

 379            LOAD_CONST              19 ('autopilot_enabled')
                LOAD_CONST              20 (False)

 380            LOAD_CONST              21 ('adaptive_autowrite')
                LOAD_CONST              20 (False)

 375            BUILD_MAP                5
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 369            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L15)
                NOT_TAKEN
                POP_TOP

 370            LOAD_CONST               8 ('')
                STORE_FAST               4 (worker_src)
       L14:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 68 (to L4)

 369   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L17:     PUSH_EXC_INFO

 382            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       45 (to L22)
                NOT_TAKEN
                STORE_FAST               6 (e)

 383   L18:     LOAD_CONST              14 ('section')
                LOAD_GLOBAL             20 (_SECTION_LEARNING)
                LOAD_CONST              15 ('status')
                LOAD_CONST              22 ('skipped')

 384            LOAD_CONST              23 ('error_code')
                LOAD_CONST              24 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 383            BUILD_MAP                3
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               2 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 382   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L17 [0]
  L3 to L4 -> L13 [0]
  L4 to L5 -> L17 [0]
  L6 to L8 -> L17 [0]
  L9 to L12 -> L17 [0]
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L17 [0]
  L15 to L16 -> L16 [1] lasti
  L16 to L17 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app\services\operator\operator_policy_report.py", line 391>:
391           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object brokerage_policy_report at 0x0000018C17F6A820, file "app\services\operator\operator_policy_report.py", line 391>:
 391            RESUME                   0

 395            LOAD_CONST               1 ('ops.policy_report.brokerage')
                STORE_FAST               1 (surface)

 396            NOP

 397    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 398            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 399            LOAD_GLOBAL              3 (_final + NULL)

 400            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 401            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 402            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 403            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 399            BUILD_MAP                4

 404            LOAD_FAST_BORROW         1 (surface)

 399            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 406    L3:     LOAD_GLOBAL              5 (_section_breaker_for_brokerage + NULL)
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1

 407            LOAD_GLOBAL              7 (_section_daily_checklist_for_brokerage + NULL)
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1

 408            LOAD_GLOBAL              9 (_section_incident_for_brokerage + NULL)
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1

 409            LOAD_GLOBAL             11 (_section_cutover_for_brokerage + NULL)
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1

 410            LOAD_GLOBAL             13 (_section_migration_posture + NULL)
                CALL                     0

 411            LOAD_GLOBAL             15 (_section_security_gate_posture + NULL)
                CALL                     0

 412            LOAD_GLOBAL             17 (_section_learning_mutation_posture + NULL)
                CALL                     0

 405            BUILD_LIST               7
                STORE_FAST               3 (sections)

 417            LOAD_FAST_BORROW         3 (sections)
                GET_ITER

 416            LOAD_FAST_AND_CLEAR      4 (s)
                SWAP                     2
        L4:     BUILD_LIST               0
                SWAP                     2

 417    L5:     FOR_ITER                53 (to L8)
                STORE_FAST               4 (s)

 418            LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         4 (s)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('')
                CALL                     2
                CALL                     1
                LOAD_ATTR               23 (lower + NULL|self)
                CALL                     0
                LOAD_CONST              20 (('ok', 'skipped'))
                CONTAINS_OP              1 (not in)

 417    L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L5)
        L7:     LOAD_FAST_BORROW         4 (s)
                LIST_APPEND              2
                JUMP_BACKWARD           55 (to L5)
        L8:     END_FOR
                POP_ITER

 416    L9:     STORE_FAST               5 (non_ok)
                STORE_FAST               4 (s)

 420            LOAD_GLOBAL              3 (_final + NULL)

 421            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         5 (non_ok)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                LOAD_CONST              10 ('ok')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              12 ('review_required')

 422   L11:     LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 423            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 424            LOAD_CONST              14 ('sections')
                LOAD_FAST_BORROW         3 (sections)

 425            LOAD_CONST              15 ('section_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST_BORROW         3 (sections)
                CALL                     1

 426            LOAD_CONST              16 ('non_ok_count')
                LOAD_GLOBAL             25 (len + NULL)
                LOAD_FAST_BORROW         5 (non_ok)
                CALL                     1

 427            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 428            LOAD_CONST               5 ('error_code')
                LOAD_CONST              17 (None)

 420            BUILD_MAP                8

 429            LOAD_FAST_BORROW         1 (surface)

 420            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

  --   L13:     SWAP                     2
                POP_TOP

 416            SWAP                     2
                STORE_FAST               4 (s)
                RERAISE                  0

  --   L14:     PUSH_EXC_INFO

 430            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 431   L15:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 432            LOAD_CONST              18 ('brokerage_policy_report error type=')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 431            CALL                     1
                POP_TOP

 434            LOAD_GLOBAL              3 (_final + NULL)

 435            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 436            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 437            LOAD_CONST               5 ('error_code')
                LOAD_CONST              19 ('unexpected:')
                LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 438            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 434            BUILD_MAP                4

 439            LOAD_FAST                1 (surface)

 434            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST              17 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST              17 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 430   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L3 to L4 -> L14 [0]
  L4 to L6 -> L13 [2]
  L7 to L9 -> L13 [2]
  L9 to L12 -> L14 [0]
  L13 to L14 -> L14 [0]
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\services\operator\operator_policy_report.py", line 442>:
442           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

444           LOAD_CONST               2 ('Optional[Iterable[Any]]')

442           LOAD_CONST               3 ('limit')

445           LOAD_CONST               4 ('Any')

442           LOAD_CONST               5 ('return')

446           LOAD_CONST               6 ('Dict[str, Any]')

442           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object operator_policy_report at 0x0000018C17E89970, file "app\services\operator\operator_policy_report.py", line 442>:
 442            RESUME                   0

 453            LOAD_CONST               1 ('ops.policy_report.fleet')
                STORE_FAST               2 (surface)

 454            NOP

 455            NOP

 456    L1:     LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (cap)

 459    L2:     LOAD_FAST_BORROW         3 (cap)
                LOAD_GLOBAL              8 (_LIMIT_MIN)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        7 (to L3)
                NOT_TAKEN

 460            LOAD_GLOBAL              8 (_LIMIT_MIN)
                STORE_FAST               3 (cap)

 461    L3:     LOAD_FAST_BORROW         3 (cap)
                LOAD_GLOBAL             10 (_LIMIT_MAX)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        7 (to L4)
                NOT_TAKEN

 462            LOAD_GLOBAL             10 (_LIMIT_MAX)
                STORE_FAST               3 (cap)

 463    L4:     LOAD_GLOBAL             13 (_safe_brokerage_iter + NULL)
                LOAD_FAST_BORROW         0 (brokerage_ids)
                CALL                     1
                LOAD_CONST               2 (None)
                LOAD_FAST_BORROW         3 (cap)
                BINARY_SLICE
                STORE_FAST               4 (ids)

 464            BUILD_LIST               0
                STORE_FAST               5 (per_brokerage)

 465            LOAD_FAST_BORROW         4 (ids)
                GET_ITER
        L5:     FOR_ITER                77 (to L6)
                STORE_FAST               6 (bid)

 466            LOAD_GLOBAL             15 (brokerage_policy_report + NULL)
                LOAD_FAST_BORROW         6 (bid)
                CALL                     1
                STORE_FAST               7 (env)

 467            LOAD_FAST_BORROW         5 (per_brokerage)
                LOAD_ATTR               17 (append + NULL|self)

 468            LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         6 (bid)

 469            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1

 470            LOAD_CONST               5 ('non_ok_count')
                LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         7 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               5 ('non_ok_count')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1

 467            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           79 (to L5)

 465    L6:     END_FOR
                POP_ITER

 473            LOAD_GLOBAL             21 (_section_migration_posture + NULL)
                CALL                     0

 474            LOAD_GLOBAL             23 (_section_security_gate_posture + NULL)
                CALL                     0

 475            LOAD_GLOBAL             25 (_section_learning_mutation_posture + NULL)
                CALL                     0

 472            BUILD_LIST               3
                STORE_FAST               8 (global_sections)

 478            LOAD_FAST_BORROW         8 (global_sections)
                GET_ITER

 477            LOAD_FAST_AND_CLEAR      9 (s)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2

 478    L8:     FOR_ITER                53 (to L11)
                STORE_FAST               9 (s)

 479            LOAD_GLOBAL             27 (str + NULL)
                LOAD_FAST_BORROW         9 (s)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_CONST               6 ('')
                CALL                     2
                CALL                     1
                LOAD_ATTR               29 (lower + NULL|self)
                CALL                     0
                LOAD_CONST              22 (('ok', 'skipped'))
                CONTAINS_OP              1 (not in)

 478    L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L8)
       L10:     LOAD_FAST_BORROW         9 (s)
                LIST_APPEND              2
                JUMP_BACKWARD           55 (to L8)
       L11:     END_FOR
                POP_ITER

 477   L12:     STORE_FAST              10 (non_ok_global)
                STORE_FAST               9 (s)

 482            LOAD_FAST_BORROW        10 (non_ok_global)
                TO_BOOL
                POP_JUMP_IF_TRUE        61 (to L23)
                NOT_TAKEN

 483            LOAD_GLOBAL             30 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L19)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_CONST               9 (<code object <genexpr> at 0x0000018C18053CF0, file "app\services\operator\operator_policy_report.py", line 483>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         5 (per_brokerage)
                GET_ITER
                CALL                     0
       L15:     FOR_ITER                12 (to L18)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
       L16:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L15)
       L17:     POP_ITER
                LOAD_CONST              10 (False)
                JUMP_FORWARD            17 (to L20)
       L18:     END_FOR
                POP_ITER
                LOAD_CONST              11 (True)
                JUMP_FORWARD            13 (to L20)
       L19:     PUSH_NULL
                LOAD_CONST               9 (<code object <genexpr> at 0x0000018C18053CF0, file "app\services\operator\operator_policy_report.py", line 483>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         5 (per_brokerage)
                GET_ITER
                CALL                     0
                CALL                     1
       L20:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L23)
       L21:     NOT_TAKEN

 482   L22:     LOAD_CONST               7 ('ok')
                JUMP_FORWARD             1 (to L24)

 484   L23:     LOAD_CONST              12 ('review_required')

 481   L24:     STORE_FAST              11 (overall)

 486            LOAD_GLOBAL             33 (_final + NULL)

 487            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW        11 (overall)

 488            LOAD_CONST              13 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 489            LOAD_CONST              14 ('global_sections')
                LOAD_FAST_BORROW         8 (global_sections)

 490            LOAD_CONST              15 ('per_brokerage')
                LOAD_FAST_BORROW         5 (per_brokerage)

 491            LOAD_CONST              16 ('per_brokerage_count')
                LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST_BORROW         5 (per_brokerage)
                CALL                     1

 492            LOAD_CONST              17 ('warnings')
                BUILD_LIST               0

 493            LOAD_CONST              18 ('error_code')
                LOAD_CONST               2 (None)

 486            BUILD_MAP                7

 494            LOAD_FAST_BORROW         2 (surface)

 486            LOAD_CONST              19 (('surface',))
                CALL_KW                  2
       L25:     RETURN_VALUE

  --   L26:     PUSH_EXC_INFO

 457            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L28)
                NOT_TAKEN
                POP_TOP

 458            LOAD_GLOBAL              6 (_LIMIT_DEFAULT)
                STORE_FAST               3 (cap)
       L27:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 359 (to L2)

 457   L28:     RERAISE                  0

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     SWAP                     2
                POP_TOP

 477            SWAP                     2
                STORE_FAST               9 (s)
                RERAISE                  0

  --   L31:     PUSH_EXC_INFO

 495            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L36)
                NOT_TAKEN
                STORE_FAST              12 (e)

 496   L32:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 497            LOAD_CONST              20 ('operator_policy_report error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 496            CALL                     1
                POP_TOP

 499            LOAD_GLOBAL             33 (_final + NULL)

 500            LOAD_CONST               4 ('status')
                LOAD_CONST               8 ('skipped')

 501            LOAD_CONST              13 ('surface')
                LOAD_FAST                2 (surface)

 502            LOAD_CONST              18 ('error_code')
                LOAD_CONST              21 ('unexpected:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 503            LOAD_CONST              17 ('warnings')
                BUILD_LIST               0

 499            BUILD_MAP                4

 504            LOAD_FAST                2 (surface)

 499            LOAD_CONST              19 (('surface',))
                CALL_KW                  2
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L35:     LOAD_CONST               2 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 495   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L26 [0]
  L2 to L7 -> L31 [0]
  L7 to L9 -> L30 [2]
  L10 to L12 -> L30 [2]
  L12 to L13 -> L31 [0]
  L14 to L16 -> L31 [0]
  L17 to L21 -> L31 [0]
  L22 to L25 -> L31 [0]
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [0]
  L28 to L29 -> L29 [1] lasti
  L29 to L31 -> L31 [0]
  L31 to L32 -> L37 [1] lasti
  L32 to L33 -> L35 [1] lasti
  L33 to L34 -> L37 [1] lasti
  L35 to L37 -> L37 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "app\services\operator\operator_policy_report.py", line 483>:
 483           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                24 (to L3)
               STORE_FAST_LOAD_FAST    17 (b, b)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('status')
               CALL                     1
               LOAD_CONST               1 ('ok')
               COMPARE_OP              72 (==)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           26 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\operator\operator_policy_report.py", line 507>:
507           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

509           LOAD_CONST               2 ('Optional[Iterable[Any]]')

507           LOAD_CONST               3 ('limit')

510           LOAD_CONST               4 ('Any')

507           LOAD_CONST               5 ('return')

511           LOAD_CONST               6 ('Dict[str, Any]')

507           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object fleet_policy_exception_report at 0x0000018C17E94650, file "app\services\operator\operator_policy_report.py", line 507>:
 507            RESUME                   0

 515            LOAD_CONST               1 ('ops.policy_report.exceptions')
                STORE_FAST               2 (surface)

 516            NOP

 517    L1:     LOAD_GLOBAL              1 (operator_policy_report + NULL)

 518            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_ids, limit)

 517            LOAD_CONST               2 (('brokerage_ids', 'limit'))
                CALL_KW                  2
                STORE_FAST               3 (env)

 520            LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               3 ('per_brokerage')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                BUILD_LIST               0
        L4:     STORE_FAST               4 (per_brokerage)

 522            LOAD_FAST_BORROW         4 (per_brokerage)
                GET_ITER

 521            LOAD_FAST_AND_CLEAR      5 (r)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2

 522    L6:     FOR_ITER                29 (to L9)
                STORE_FAST               5 (r)

 523            LOAD_FAST_BORROW         5 (r)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_CONST               5 ('ok')
                COMPARE_OP             119 (bool(!=))

 522    L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L6)
        L8:     LOAD_FAST_BORROW         5 (r)
                LIST_APPEND              2
                JUMP_BACKWARD           31 (to L6)
        L9:     END_FOR
                POP_ITER

 521   L10:     STORE_FAST               6 (bad)
                STORE_FAST               5 (r)

 525            LOAD_GLOBAL              5 (_final + NULL)

 526            LOAD_CONST               4 ('status')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('ok')
                CALL                     2

 527            LOAD_CONST               6 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 528            LOAD_CONST               7 ('count')
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         6 (bad)
                CALL                     1

 529            LOAD_CONST               8 ('rows')
                LOAD_FAST_BORROW         6 (bad)

 530            LOAD_CONST               9 ('global_sections')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               9 ('global_sections')
                BUILD_LIST               0
                CALL                     2

 531            LOAD_CONST              10 ('warnings')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2

 532            LOAD_CONST              11 ('error_code')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              11 ('error_code')
                CALL                     1

 525            BUILD_MAP                7

 533            LOAD_FAST_BORROW         2 (surface)

 525            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L11:     RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 521            SWAP                     2
                STORE_FAST               5 (r)
                RERAISE                  0

  --   L13:     PUSH_EXC_INFO

 534            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L18)
                NOT_TAKEN
                STORE_FAST               7 (e)

 535   L14:     LOAD_GLOBAL             10 (logger)
                LOAD_ATTR               13 (warning + NULL|self)

 536            LOAD_CONST              13 ('fleet_policy_exception_report error type=')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 535            CALL                     1
                POP_TOP

 538            LOAD_GLOBAL              5 (_final + NULL)

 539            LOAD_CONST               4 ('status')
                LOAD_CONST              14 ('skipped')

 540            LOAD_CONST               6 ('surface')
                LOAD_FAST                2 (surface)

 541            LOAD_CONST               8 ('rows')
                BUILD_LIST               0

 542            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 543            LOAD_CONST              11 ('error_code')
                LOAD_CONST              15 ('unexpected:')
                LOAD_GLOBAL             15 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               16 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 544            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 538            BUILD_MAP                6

 545            LOAD_FAST                2 (surface)

 538            LOAD_CONST              12 (('surface',))
                CALL_KW                  2
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST              16 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST              16 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 534   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L5 -> L13 [0]
  L5 to L7 -> L12 [2]
  L8 to L10 -> L12 [2]
  L10 to L11 -> L13 [0]
  L12 to L13 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti
```
