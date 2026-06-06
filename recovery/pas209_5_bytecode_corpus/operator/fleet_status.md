# operator/fleet_status

- **pyc:** `app\services\operator\__pycache__\fleet_status.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/fleet_status.py`
- **co_filename (from bytecode):** `app\services\operator\fleet_status.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS187 — Fleet observability aggregator (read-only).

Composes per-brokerage health signals into fleet-wide
structural reports. Operator/admin-only. No PII. No raw
payloads. No tenant surface. Never raises.

Public surface:

  * ``fleet_chain_status_report(...)``
        Aggregate per-brokerage audit-chain status into a
        fleet roll-up.
  * ``fleet_brokerage_health_summary(...)``
        Per-brokerage health envelope (queue depth + stale
        dialing + callbacks + learning review counts +
        chain status + verification status + rollout stage
        + action_required).
  * ``fleet_rollout_readiness_summary(...)``
        Fleet-wide readiness verdict by rollout stage
        (TRUSTED_PILOT / EXPANDED_PILOT / PRODUCTION_READY_REVIEW).
  * ``fleet_exception_report(...)``
        Sub-set of fleet_brokerage_health_summary rows where
        ``action_required != "none"``. Used by the daily
        ops operator to triage quickly.

Doctrine:

* **Read-only.** No mutation surface. No autonomous
  remediation.
* **Bounded.** ``limit`` is clamped between 1 and 200; the
  default is 50.
* **No PII / no secrets / no raw payloads.** The forbidden-
  token scanner from the existing operator-route pattern
  is mirrored here as a final defence on the returned
  envelope.
* **NEVER raises.** Any unexpected exception collapses to
  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``
  and a logger warning.
* **DB unavailable** -> ``status="skipped"`` + a warning;
  partial fleet results are returned (best-effort).
* **Closed allow-list per envelope row.** Each row exposes
  only the structural keys named in the function
  docstrings.
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `__future__`, `annotations`, `app.db.brokerage_store`, `app.services.callbacks.callback_schedule`, `app.services.ingestion.pending_call_recovery`, `app.services.learning.recommendation_review`, `app.services.operator.audit_chain_verifier`, `app.services.operator.audit_verification_runs`, `detect_stale_dialing_rows`, `get_brokerage`, `latest_verification_run_status`, `list_brokerages`, `list_learning_recommendations`, `logging`, `queue_status_report`, `reminder_report`, `typing`, `verify_brokerage_chain`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_classify_action_required`, `_final_envelope`, `_project_row`, `_safe_brokerage`, `_safe_brokerage_iter`, `_safe_brokerage_list_from_db`, `_scan_for_forbidden`, `_signal_callback_due`, `_signal_chain_status`, `_signal_learning_review_count`, `_signal_queue_depth`, `_signal_rollout_stage`, `_signal_security_warning_count`, `_signal_stale_dialing`, `_signal_verification_status`, `fleet_brokerage_health_summary`, `fleet_chain_status_report`, `fleet_exception_report`, `fleet_rollout_readiness_summary`

## Env-key candidates

`UNKNOWN`

## String constants (redacted where noted)

- '\nPAS187 — Fleet observability aggregator (read-only).\n\nComposes per-brokerage health signals into fleet-wide\nstructural reports. Operator/admin-only. No PII. No raw\npayloads. No tenant surface. Never raises.\n\nPublic surface:\n\n  * ``fleet_chain_status_report(...)``\n        Aggregate per-brokerage audit-chain status into a\n        fleet roll-up.\n  * ``fleet_brokerage_health_summary(...)``\n        Per-brokerage health envelope (queue depth + stale\n        dialing + callbacks + learning review counts +\n        chain status + verification status + rollout stage\n        + action_required).\n  * ``fleet_rollout_readiness_summary(...)``\n        Fleet-wide readiness verdict by rollout stage\n        (TRUSTED_PILOT / EXPANDED_PILOT / PRODUCTION_READY_REVIEW).\n  * ``fleet_exception_report(...)``\n        Sub-set of fleet_brokerage_health_summary rows where\n        ``action_required != "none"``. Used by the daily\n        ops operator to triage quickly.\n\nDoctrine:\n\n* **Read-only.** No mutation surface. No autonomous\n  remediation.\n* **Bounded.** ``limit`` is clamped between 1 and 200; the\n  default is 50.\n* **No PII / no secrets / no raw payloads.** The forbidden-\n  token scanner from the existing operator-route pattern\n  is mirrored here as a final defence on the returned\n  envelope.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``\n  and a logger warning.\n* **DB unavailable** -> ``status="skipped"`` + a warning;\n  partial fleet results are returned (best-effort).\n* **Closed allow-list per envelope row.** Each row exposes\n  only the structural keys named in the function\n  docstrings.\n'
- 'pas.operator.fleet_status'
- 'none'
- 'review_required'
- 'urgent'
- 'brokerage_ids'
- 'limit'
- 'value'
- 'Any'
- 'int'
- 'default'
- 'return'
- 'Optional[str]'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'str'
- 'fleet_status surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'fleet_envelope_forbidden_token'
- 'warnings'
- 'rows'
- 'count'
- 'row'
- 'Project to the closed allow-list. Drops everything else.'
- 'Optional[Iterable[Any]]'
- 'List[str]'
- 'Best-effort enumeration of active brokerage IDs. DB\nunavailable returns an empty list (caller falls back to\nskipped status).'
- 'fleet_status list_brokerages error type='
- 'brokerage_id'
- 'Returns the latest chain status string for the brokerage,\nor None on DB unavailable / unknown.'
- 'fleet_status chain status brokerage='
- ' error type='
- 'fleet_status verification brokerage='
- 'Optional[int]'
- 'fleet_status queue brokerage='
- 'total'
- 'fleet_status stale_dialing brokerage='
- 'fleet_status callback brokerage='
- 'due_count'
- 'fleet_status learning brokerage='
- 'Conservative default: zero. Wired through here so that\na future PAS phase can light up the signal without changing\nthe row shape.'
- "Best-effort fetch of the brokerage's pilot stage. DB\nunavailable returns 'UNKNOWN'."
- 'UNKNOWN'
- 'fleet_status rollout_stage brokerage='
- 'config'
- 'pilot_stage'
- 'rollout_stage'
- 'chain_status'
- 'verification_status'
- 'queue_depth'
- 'stale_dialing'
- 'callback_due'
- 'learning_count'
- 'security_warnings'
- "Closed three-value classifier. Conservative: any\n'failed' signal escalates to urgent; partial / amber\nsignals escalate to review_required; everything else\nis none."
- 'Per-brokerage health envelope. Closed row shape.\n\nReturns::\n\n    {\n      "status":  "ok" | "skipped" | "failed",\n      "surface": "ops.fleet.brokerage_health",\n      "count":   <int>,\n      "rows":    [ { ...closed allow-list... }, ... ],\n      "warnings": [...],\n      "error_code": null | str,\n    }\n'
- 'ops.fleet.brokerage_health'
- 'skipped'
- 'no_brokerage_ids_available'
- 'latest_chain_status'
- 'unknown'
- 'latest_verification_status'
- 'pending_call_queue_depth'
- 'stale_dialing_count'
- 'callback_due_count'
- 'learning_review_count'
- 'security_warning_count'
- 'action_required'
- 'db_unavailable_or_signals_unavailable'
- 'fleet_brokerage_health_summary error type='
- 'unexpected:'
- 'Fleet-wide audit-chain roll-up. Composed from\n``fleet_brokerage_health_summary`` so signal logic is\nnot duplicated.'
- 'ops.fleet.chain_status'
- 'summary'
- 'Fleet-wide rollout-stage roll-up.'
- 'ops.fleet.rollout_readiness'
- 'by_stage'
- 'by_action'
- "Sub-set of brokerage rows whose action_required is not\n'none'. The daily-ops operator pulls this to triage."
- 'ops.fleet.exceptions'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS187 — Fleet observability aggregator (read-only).\n\nComposes per-brokerage health signals into fleet-wide\nstructural reports. Operator/admin-only. No PII. No raw\npayloads. No tenant surface. Never raises.\n\nPublic surface:\n\n  * ``fleet_chain_status_report(...)``\n        Aggregate per-brokerage audit-chain status into a\n        fleet roll-up.\n  * ``fleet_brokerage_health_summary(...)``\n        Per-brokerage health envelope (queue depth + stale\n        dialing + callbacks + learning review counts +\n        chain status + verification status + rollout stage\n        + action_required).\n  * ``fleet_rollout_readiness_summary(...)``\n        Fleet-wide readiness verdict by rollout stage\n        (TRUSTED_PILOT / EXPANDED_PILOT / PRODUCTION_READY_REVIEW).\n  * ``fleet_exception_report(...)``\n        Sub-set of fleet_brokerage_health_summary rows where\n        ``action_required != "none"``. Used by the daily\n        ops operator to triage quickly.\n\nDoctrine:\n\n* **Read-only.** No mutation surface. No autonomous\n  remediation.\n* **Bounded.** ``limit`` is clamped between 1 and 200; the\n  default is 50.\n* **No PII / no secrets / no raw payloads.** The forbidden-\n  token scanner from the existing operator-route pattern\n  is mirrored here as a final defence on the returned\n  envelope.\n* **NEVER raises.** Any unexpected exception collapses to\n  ``status="skipped"`` + ``error_code="unexpected:<TypeName>"``\n  and a logger warning.\n* **DB unavailable** -> ``status="skipped"`` + a warning;\n  partial fleet results are returned (best-effort).\n* **Closed allow-list per envelope row.** Each row exposes\n  only the structural keys named in the function\n  docstrings.\n')
              STORE_NAME               0 (__doc__)

 46           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 48           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 49           LOAD_SMALL_INT           0
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

 52           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.operator.fleet_status')
              CALL                     1
              STORE_NAME              11 (logger)

 59           LOAD_SMALL_INT         200
              STORE_NAME              12 (_BROKERAGE_ID_MAX_LEN)

 60           LOAD_SMALL_INT          50
              STORE_NAME              13 (_LIMIT_DEFAULT)

 61           LOAD_SMALL_INT           1
              STORE_NAME              14 (_LIMIT_MIN)

 62           LOAD_SMALL_INT         200
              STORE_NAME              15 (_LIMIT_MAX)

 64           LOAD_CONST              50 (('ONBOARDING', 'TRUSTED_PILOT', 'EXPANDED_PILOT', 'PRODUCTION_READY_REVIEW', 'PRODUCTION', 'PAUSED', 'UNKNOWN'))
              STORE_NAME              16 (_ROLLOUT_STAGES)

 74           LOAD_CONST               5 ('none')
              STORE_NAME              17 (_ACTION_NONE)

 75           LOAD_CONST               6 ('review_required')
              STORE_NAME              18 (_ACTION_ATTENTION)

 76           LOAD_CONST               7 ('urgent')
              STORE_NAME              19 (_ACTION_URGENT)

 78           LOAD_CONST              51 (('brokerage_id', 'latest_chain_status', 'latest_verification_status', 'pending_call_queue_depth', 'stale_dialing_count', 'callback_due_count', 'learning_review_count', 'security_warning_count', 'rollout_stage', 'action_required'))
              STORE_NAME              20 (_BROKERAGE_ROW_ALLOWLIST)

 91           LOAD_CONST              52 (('phone', 'email', 'name_token', 'transcript', 'summary_text', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'callback_notes', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_raw', 'api_key', 'token', 'stack_trace'))
              STORE_NAME              21 (_FORBIDDEN_RESPONSE_TOKENS)

105           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\fleet_status.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _clamp_int at 0x0000018C18038F30, file "app\services\operator\fleet_status.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_clamp_int)

117           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\fleet_status.py", line 117>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _safe_brokerage at 0x0000018C17F96420, file "app\services\operator\fleet_status.py", line 117>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_safe_brokerage)

126           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\fleet_status.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _scan_for_forbidden at 0x0000018C18025130, file "app\services\operator\fleet_status.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_scan_for_forbidden)

150           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\fleet_status.py", line 150>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _final_envelope at 0x0000018C17FE1680, file "app\services\operator\fleet_status.py", line 150>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_final_envelope)

168           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\fleet_status.py", line 168>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _project_row at 0x0000018C18053750, file "app\services\operator\fleet_status.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_project_row)

177           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\fleet_status.py", line 177>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _safe_brokerage_iter at 0x0000018C180483B0, file "app\services\operator\fleet_status.py", line 177>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_safe_brokerage_iter)

196           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\fleet_status.py", line 196>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _safe_brokerage_list_from_db at 0x0000018C17EE1CC0, file "app\services\operator\fleet_status.py", line 196>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_brokerage_list_from_db)

226           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\fleet_status.py", line 226>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _signal_chain_status at 0x0000018C17D77E00, file "app\services\operator\fleet_status.py", line 226>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_signal_chain_status)

250           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\fleet_status.py", line 250>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _signal_verification_status at 0x0000018C18048730, file "app\services\operator\fleet_status.py", line 250>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_signal_verification_status)

267           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\fleet_status.py", line 267>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _signal_queue_depth at 0x0000018C17ECDD80, file "app\services\operator\fleet_status.py", line 267>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_signal_queue_depth)

289           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\fleet_status.py", line 289>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _signal_stale_dialing at 0x0000018C17E8A6D0, file "app\services\operator\fleet_status.py", line 289>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_signal_stale_dialing)

316           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\fleet_status.py", line 316>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _signal_callback_due at 0x0000018C17ECF000, file "app\services\operator\fleet_status.py", line 316>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_signal_callback_due)

338           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\fleet_status.py", line 338>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _signal_learning_review_count at 0x0000018C17E8A9A0, file "app\services\operator\fleet_status.py", line 338>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_signal_learning_review_count)

365           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\fleet_status.py", line 365>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _signal_security_warning_count at 0x0000018C180690D0, file "app\services\operator\fleet_status.py", line 365>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_signal_security_warning_count)

372           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\fleet_status.py", line 372>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _signal_rollout_stage at 0x0000018C17D8BF50, file "app\services\operator\fleet_status.py", line 372>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_signal_rollout_stage)

400           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C180C4250, file "app\services\operator\fleet_status.py", line 400>)
              MAKE_FUNCTION
              LOAD_CONST              39 (<code object _classify_action_required at 0x0000018C17D8C280, file "app\services\operator\fleet_status.py", line 400>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_classify_action_required)

437           LOAD_CONST              40 ('brokerage_ids')

439           LOAD_CONST               2 (None)

437           LOAD_CONST              41 ('limit')

440           LOAD_NAME               13 (_LIMIT_DEFAULT)

437           BUILD_MAP                2
              LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\fleet_status.py", line 437>)
              MAKE_FUNCTION
              LOAD_CONST              43 (<code object fleet_brokerage_health_summary at 0x0000018C17D7E880, file "app\services\operator\fleet_status.py", line 437>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (fleet_brokerage_health_summary)

537           LOAD_CONST              40 ('brokerage_ids')

539           LOAD_CONST               2 (None)

537           LOAD_CONST              41 ('limit')

540           LOAD_NAME               13 (_LIMIT_DEFAULT)

537           BUILD_MAP                2
              LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\fleet_status.py", line 537>)
              MAKE_FUNCTION
              LOAD_CONST              45 (<code object fleet_chain_status_report at 0x0000018C17EDA250, file "app\services\operator\fleet_status.py", line 537>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (fleet_chain_status_report)

580           LOAD_CONST              40 ('brokerage_ids')

582           LOAD_CONST               2 (None)

580           LOAD_CONST              41 ('limit')

583           LOAD_NAME               13 (_LIMIT_DEFAULT)

580           BUILD_MAP                2
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\fleet_status.py", line 580>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object fleet_rollout_readiness_summary at 0x0000018C17EDA5A0, file "app\services\operator\fleet_status.py", line 580>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (fleet_rollout_readiness_summary)

609           LOAD_CONST              40 ('brokerage_ids')

611           LOAD_CONST               2 (None)

609           LOAD_CONST              41 ('limit')

612           LOAD_NAME               13 (_LIMIT_DEFAULT)

609           BUILD_MAP                2
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025730, file "app\services\operator\fleet_status.py", line 609>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object fleet_exception_report at 0x0000018C17D76780, file "app\services\operator\fleet_status.py", line 609>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (fleet_exception_report)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\fleet_status.py", line 105>:
105           RESUME                   0
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

Disassembly of <code object _clamp_int at 0x0000018C18038F30, file "app\services\operator\fleet_status.py", line 105>:
 105           RESUME                   0

 106           NOP

 107   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 110   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 111           LOAD_FAST                1 (lo)
               RETURN_VALUE

 112   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 113           LOAD_FAST                2 (hi)
               RETURN_VALUE

 114   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 108           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 109           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 108   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\operator\fleet_status.py", line 117>:
117           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F96420, file "app\services\operator\fleet_status.py", line 117>:
117           RESUME                   0

118           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

119           LOAD_CONST               0 (None)
              RETURN_VALUE

120   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

121           LOAD_FAST_BORROW         1 (s)
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

122   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

123   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\fleet_status.py", line 126>:
126           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025130, file "app\services\operator\fleet_status.py", line 126>:
  --           MAKE_CELL                1 (walk)

 126           RESUME                   0

 127           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\fleet_status.py", line 127>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2960, file "app\services\operator\fleet_status.py", line 127>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 147           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\fleet_status.py", line 127>:
127           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC2960, file "app\services\operator\fleet_status.py", line 127>:
  --            COPY_FREE_VARS           1

 127            RESUME                   0

 128            NOP

 129    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 130    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 131            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 132            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 133            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 134            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 135    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 133    L9:     END_FOR
                POP_ITER

 136   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 137            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 138   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 130   L14:     END_FOR
                POP_ITER

 146   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 139   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 140            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 141            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 142            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 143   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 140   L21:     END_FOR
                POP_ITER

 146   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 144            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 145   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 144   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\fleet_status.py", line 150>:
150           RESUME                   0
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

Disassembly of <code object _final_envelope at 0x0000018C17FE1680, file "app\services\operator\fleet_status.py", line 150>:
150           RESUME                   0

151           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

152           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       41 (to L1)
              NOT_TAKEN

153           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

154           LOAD_CONST               0 ('fleet_status surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

153           CALL                     1
              POP_TOP

158           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

159           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

160           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('fleet_envelope_forbidden_token')

161           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('fleet_envelope_forbidden_token')
              BUILD_LIST               1

162           LOAD_CONST               8 ('rows')
              BUILD_LIST               0

163           LOAD_CONST               9 ('count')
              LOAD_SMALL_INT           0

157           BUILD_MAP                6
              RETURN_VALUE

165   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\fleet_status.py", line 168>:
168           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C18053750, file "app\services\operator\fleet_status.py", line 168>:
168           RESUME                   0

170           BUILD_MAP                0
              STORE_FAST               1 (out)

171           LOAD_GLOBAL              0 (_BROKERAGE_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

172           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

173   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

171   L3:     END_FOR
              POP_ITER

174           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\fleet_status.py", line 177>:
177           RESUME                   0
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

Disassembly of <code object _safe_brokerage_iter at 0x0000018C180483B0, file "app\services\operator\fleet_status.py", line 177>:
177           RESUME                   0

178           LOAD_FAST_BORROW         0 (brokerage_ids)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

179           BUILD_LIST               0
              RETURN_VALUE

180   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

181           LOAD_GLOBAL              1 (set + NULL)
              CALL                     0
              STORE_FAST               2 (seen)

182           LOAD_FAST_BORROW         0 (brokerage_ids)
              GET_ITER
      L2:     FOR_ITER                85 (to L5)
              STORE_FAST               3 (value)

183           LOAD_GLOBAL              3 (_safe_brokerage + NULL)
              LOAD_FAST_BORROW         3 (value)
              CALL                     1
              STORE_FAST               4 (safe)

184           LOAD_FAST_BORROW         4 (safe)
              TO_BOOL
              POP_JUMP_IF_FALSE       41 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (safe, seen)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       35 (to L3)
              NOT_TAKEN

185           LOAD_FAST_BORROW         2 (seen)
              LOAD_ATTR                5 (add + NULL|self)
              LOAD_FAST_BORROW         4 (safe)
              CALL                     1
              POP_TOP

186           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         4 (safe)
              CALL                     1
              POP_TOP

187   L3:     LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              LOAD_GLOBAL             10 (_LIMIT_MAX)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           84 (to L2)

188   L4:     POP_TOP

189           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

182   L5:     END_FOR
              POP_ITER

189           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\fleet_status.py", line 196>:
196           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _safe_brokerage_list_from_db at 0x0000018C17EE1CC0, file "app\services\operator\fleet_status.py", line 196>:
 196            RESUME                   0

 200            NOP

 201    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('list_brokerages',))
                IMPORT_NAME              0 (app.db.brokerage_store)
                IMPORT_FROM              1 (list_brokerages)
                STORE_FAST               0 (list_brokerages)
                POP_TOP

 204    L2:     NOP

 205    L3:     LOAD_FAST                0 (list_brokerages)
                PUSH_NULL
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     STORE_FAST               1 (rows)

 211    L7:     BUILD_LIST               0
                STORE_FAST               3 (out)

 212            LOAD_FAST                1 (rows)
                GET_ITER
        L8:     FOR_ITER               141 (to L20)
                STORE_FAST               4 (r)

 213            NOP

 214    L9:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (r)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       44 (to L13)
                NOT_TAKEN

 215            LOAD_FAST                4 (r)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               4 ('id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_FAST                4 (r)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1
       L12:     STORE_FAST               5 (bid)
                JUMP_FORWARD            34 (to L17)

 217   L13:     LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST                4 (r)
                LOAD_CONST               4 ('id')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST                4 (r)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_CONST               3 (None)
                CALL                     3
       L16:     STORE_FAST               5 (bid)

 218   L17:     LOAD_GLOBAL             23 (_safe_brokerage + NULL)
                LOAD_FAST                5 (bid)
                CALL                     1
                STORE_FAST               6 (safe)

 219            LOAD_FAST                6 (safe)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L19)
                NOT_TAKEN

 220            LOAD_FAST                3 (out)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_FAST                6 (safe)
                CALL                     1
                POP_TOP
       L18:     JUMP_BACKWARD          141 (to L8)

 219   L19:     JUMP_BACKWARD          143 (to L8)

 212   L20:     END_FOR
                POP_ITER

 223            LOAD_FAST                3 (out)
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 202            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L23)
                NOT_TAKEN
                POP_TOP

 203            BUILD_LIST               0
                SWAP                     2
       L22:     POP_EXCEPT
                RETURN_VALUE

 202   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 206            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L30)
                NOT_TAKEN
                STORE_FAST               2 (e)

 207   L26:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 208            LOAD_CONST               2 ('fleet_status list_brokerages error type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 207            CALL                     1
                POP_TOP

 210            BUILD_LIST               0
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               3 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 206   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 221            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L34)
                NOT_TAKEN
                POP_TOP

 222   L33:     POP_EXCEPT
                JUMP_BACKWARD          249 (to L8)

 221   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L21 [0]
  L3 to L4 -> L25 [0]
  L5 to L7 -> L25 [0]
  L9 to L10 -> L32 [1]
  L11 to L14 -> L32 [1]
  L15 to L18 -> L32 [1]
  L21 to L22 -> L24 [1] lasti
  L23 to L24 -> L24 [1] lasti
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti
  L32 to L33 -> L35 [2] lasti
  L34 to L35 -> L35 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\fleet_status.py", line 226>:
226           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_chain_status at 0x0000018C17D77E00, file "app\services\operator\fleet_status.py", line 226>:
 226            RESUME                   0

 229            NOP

 230    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('verify_brokerage_chain',))
                IMPORT_NAME              0 (app.services.operator.audit_chain_verifier)
                IMPORT_FROM              1 (verify_brokerage_chain)
                STORE_FAST               1 (verify_brokerage_chain)
                POP_TOP

 235    L2:     NOP

 236    L3:     LOAD_FAST                1 (verify_brokerage_chain)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (report)

 243    L4:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (report)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L5)
                NOT_TAKEN

 244            LOAD_FAST                2 (report)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                STORE_FAST               4 (status)

 245            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (status)
                LOAD_GLOBAL             20 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 246            LOAD_FAST                4 (status)
                RETURN_VALUE

 247    L5:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 233            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L8)
                NOT_TAKEN
                POP_TOP

 234    L7:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 233    L8:     RERAISE                  0

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 237            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 238   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 239            LOAD_CONST               3 ('fleet_status chain status brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               4 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               5 (' error type=')

 240            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 239            BUILD_STRING             4

 238            CALL                     1
                POP_TOP

 242   L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 237   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L4 -> L10 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\fleet_status.py", line 250>:
250           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_verification_status at 0x0000018C18048730, file "app\services\operator\fleet_status.py", line 250>:
 250            RESUME                   0

 251            NOP

 252    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('latest_verification_run_status',))
                IMPORT_NAME              0 (app.services.operator.audit_verification_runs)
                IMPORT_FROM              1 (latest_verification_run_status)
                STORE_FAST               1 (latest_verification_run_status)
                POP_TOP

 257    L2:     NOP

 258    L3:     LOAD_FAST                1 (latest_verification_run_status)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                CALL                     1
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 255            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L7)
                NOT_TAKEN
                POP_TOP

 256    L6:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 255    L7:     RERAISE                  0

  --    L8:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
        L9:     PUSH_EXC_INFO

 259            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L13)
                NOT_TAKEN
                STORE_FAST               2 (e)

 260   L10:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 261            LOAD_CONST               3 ('fleet_status verification brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               4 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               5 (' error type=')

 262            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                2 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 261            BUILD_STRING             4

 260            CALL                     1
                POP_TOP

 264   L11:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L12:     LOAD_CONST               2 (None)
                STORE_FAST               2 (e)
                DELETE_FAST              2 (e)
                RERAISE                  1

 259   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L9 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\fleet_status.py", line 267>:
267           RESUME                   0
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
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_queue_depth at 0x0000018C17ECDD80, file "app\services\operator\fleet_status.py", line 267>:
 267            RESUME                   0

 268            NOP

 269    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('queue_status_report',))
                IMPORT_NAME              0 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              1 (queue_status_report)
                STORE_FAST               1 (queue_status_report)
                POP_TOP

 274    L2:     NOP

 275    L3:     LOAD_FAST                1 (queue_status_report)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               3 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               2 (report)

 282    L4:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (report)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L5)
                NOT_TAKEN

 283            LOAD_FAST                2 (report)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('total')
                CALL                     1
                STORE_FAST               4 (total)

 284            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (total)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L5)
                NOT_TAKEN
                LOAD_FAST                4 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 285            LOAD_FAST                4 (total)
                RETURN_VALUE

 286    L5:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 272            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L8)
                NOT_TAKEN
                POP_TOP

 273    L7:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 272    L8:     RERAISE                  0

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 276            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 277   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 278            LOAD_CONST               4 ('fleet_status queue brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               5 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               6 (' error type=')

 279            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 278            BUILD_STRING             4

 277            CALL                     1
                POP_TOP

 281   L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 276   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L4 -> L10 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\fleet_status.py", line 289>:
289           RESUME                   0
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
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_stale_dialing at 0x0000018C17E8A6D0, file "app\services\operator\fleet_status.py", line 289>:
 289            RESUME                   0

 290            NOP

 291    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('detect_stale_dialing_rows',))
                IMPORT_NAME              0 (app.services.ingestion.pending_call_recovery)
                IMPORT_FROM              1 (detect_stale_dialing_rows)
                STORE_FAST               1 (detect_stale_dialing_rows)
                POP_TOP

 296    L2:     NOP

 297    L3:     LOAD_FAST                1 (detect_stale_dialing_rows)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               3 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               2 (report)

 304    L4:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (report)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      113 (to L6)
                NOT_TAKEN

 307            LOAD_FAST                2 (report)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('total')
                CALL                     1
                STORE_FAST               4 (total)

 308            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (total)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L5)
                NOT_TAKEN
                LOAD_FAST                4 (total)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 309            LOAD_FAST                4 (total)
                RETURN_VALUE

 310    L5:     LOAD_FAST                2 (report)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               8 ('rows')
                CALL                     1
                STORE_FAST               5 (rows)

 311            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                5 (rows)
                LOAD_GLOBAL             22 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 312            LOAD_GLOBAL             25 (min + NULL)
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1
                LOAD_GLOBAL             28 (_LIMIT_MAX)
                CALL                     2
                RETURN_VALUE

 313    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 294            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 295    L8:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 294    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     PUSH_EXC_INFO

 298            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 299   L12:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 300            LOAD_CONST               4 ('fleet_status stale_dialing brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               5 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               6 (' error type=')

 301            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 300            BUILD_STRING             4

 299            CALL                     1
                POP_TOP

 303   L13:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L14:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 298   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L3 to L4 -> L11 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti
  L11 to L12 -> L16 [1] lasti
  L12 to L13 -> L14 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\fleet_status.py", line 316>:
316           RESUME                   0
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
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_callback_due at 0x0000018C17ECF000, file "app\services\operator\fleet_status.py", line 316>:
 316            RESUME                   0

 317            NOP

 318    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('reminder_report',))
                IMPORT_NAME              0 (app.services.callbacks.callback_schedule)
                IMPORT_FROM              1 (reminder_report)
                STORE_FAST               1 (reminder_report)
                POP_TOP

 323    L2:     NOP

 324    L3:     LOAD_FAST                1 (reminder_report)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                LOAD_SMALL_INT          60
                LOAD_CONST               3 (('lookahead_minutes',))
                CALL_KW                  2
                STORE_FAST               2 (report)

 331    L4:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (report)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L5)
                NOT_TAKEN

 332            LOAD_FAST                2 (report)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('due_count')
                CALL                     1
                STORE_FAST               4 (due)

 333            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (due)
                LOAD_GLOBAL             20 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L5)
                NOT_TAKEN
                LOAD_FAST                4 (due)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 334            LOAD_FAST                4 (due)
                RETURN_VALUE

 335    L5:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 321            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L8)
                NOT_TAKEN
                POP_TOP

 322    L7:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 321    L8:     RERAISE                  0

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 325            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 326   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 327            LOAD_CONST               4 ('fleet_status callback brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               5 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               6 (' error type=')

 328            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 327            BUILD_STRING             4

 326            CALL                     1
                POP_TOP

 330   L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 325   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L6 [0]
  L3 to L4 -> L10 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti
  L10 to L11 -> L15 [1] lasti
  L11 to L12 -> L13 [1] lasti
  L13 to L15 -> L15 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\fleet_status.py", line 338>:
338           RESUME                   0
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
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_learning_review_count at 0x0000018C17E8A9A0, file "app\services\operator\fleet_status.py", line 338>:
 338            RESUME                   0

 339            NOP

 340    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('list_learning_recommendations',))
                IMPORT_NAME              0 (app.services.learning.recommendation_review)
                IMPORT_FROM              1 (list_learning_recommendations)
                STORE_FAST               1 (list_learning_recommendations)
                POP_TOP

 345    L2:     NOP

 346    L3:     LOAD_FAST                1 (list_learning_recommendations)
                PUSH_NULL

 347            LOAD_FAST                0 (brokerage_id)
                LOAD_GLOBAL              6 (_LIMIT_MAX)

 346            LOAD_CONST               3 (('brokerage_id', 'limit'))
                CALL_KW                  2
                STORE_FAST               2 (env)

 355    L4:     LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST                2 (env)
                LOAD_GLOBAL             18 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      113 (to L6)
                NOT_TAKEN

 356            LOAD_FAST                2 (env)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               7 ('count')
                CALL                     1
                STORE_FAST               4 (count)

 357            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST                4 (count)
                LOAD_GLOBAL             22 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L5)
                NOT_TAKEN
                LOAD_FAST                4 (count)
                LOAD_SMALL_INT           0
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 358            LOAD_FAST                4 (count)
                RETURN_VALUE

 359    L5:     LOAD_FAST                2 (env)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST               8 ('rows')
                CALL                     1
                STORE_FAST               5 (rows)

 360            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST                5 (rows)
                LOAD_GLOBAL             24 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 361            LOAD_GLOBAL             27 (min + NULL)
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1
                LOAD_GLOBAL              6 (_LIMIT_MAX)
                CALL                     2
                RETURN_VALUE

 362    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 343            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 344    L8:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 343    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     PUSH_EXC_INFO

 349            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 350   L12:     LOAD_GLOBAL              8 (logger)
                LOAD_ATTR               11 (warning + NULL|self)

 351            LOAD_CONST               4 ('fleet_status learning brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               5 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               6 (' error type=')

 352            LOAD_GLOBAL             13 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               14 (__name__)
                FORMAT_SIMPLE

 351            BUILD_STRING             4

 350            CALL                     1
                POP_TOP

 354   L13:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L14:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 349   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L3 to L4 -> L11 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti
  L11 to L12 -> L16 [1] lasti
  L12 to L13 -> L14 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\operator\fleet_status.py", line 365>:
365           RESUME                   0
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
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _signal_security_warning_count at 0x0000018C180690D0, file "app\services\operator\fleet_status.py", line 365>:
365           RESUME                   0

369           LOAD_SMALL_INT           0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\operator\fleet_status.py", line 372>:
372           RESUME                   0
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

Disassembly of <code object _signal_rollout_stage at 0x0000018C17D8BF50, file "app\services\operator\fleet_status.py", line 372>:
 372            RESUME                   0

 375            NOP

 376    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_brokerage',))
                IMPORT_NAME              0 (app.db.brokerage_store)
                IMPORT_FROM              1 (get_brokerage)
                STORE_FAST               1 (get_brokerage)
                POP_TOP

 379    L2:     NOP

 380    L3:     LOAD_FAST                1 (get_brokerage)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (rec)

 387    L4:     LOAD_FAST                2 (rec)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 388            LOAD_CONST               2 ('UNKNOWN')
                RETURN_VALUE

 389    L5:     NOP

 390    L6:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (rec)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN
                LOAD_FAST                2 (rec)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               7 ('config')
                CALL                     1
                JUMP_FORWARD            12 (to L8)
        L7:     LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST                2 (rec)
                LOAD_CONST               7 ('config')
                LOAD_CONST               6 (None)
                CALL                     3
        L8:     STORE_FAST               4 (cfg)

 391            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                4 (cfg)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L13)
                NOT_TAKEN

 392            LOAD_FAST                4 (cfg)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               8 ('pilot_stage')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_FAST                4 (cfg)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               9 ('rollout_stage')
                CALL                     1
       L11:     STORE_FAST               5 (stage)

 393            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                5 (stage)
                LOAD_GLOBAL             22 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L13)
                NOT_TAKEN
                LOAD_FAST                5 (stage)
                LOAD_GLOBAL             24 (_ROLLOUT_STAGES)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN

 394            LOAD_FAST                5 (stage)
       L12:     RETURN_VALUE

 397   L13:     LOAD_CONST               2 ('UNKNOWN')
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 377            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L16)
                NOT_TAKEN
                POP_TOP

 378   L15:     POP_EXCEPT
                LOAD_CONST               2 ('UNKNOWN')
                RETURN_VALUE

 377   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     PUSH_EXC_INFO

 381            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L22)
                NOT_TAKEN
                STORE_FAST               3 (e)

 382   L19:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 383            LOAD_CONST               3 ('fleet_status rollout_stage brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               4 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               5 (' error type=')

 384            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 383            BUILD_STRING             4

 382            CALL                     1
                POP_TOP

 386   L20:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 ('UNKNOWN')
                RETURN_VALUE

  --   L21:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 381   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L24:     PUSH_EXC_INFO

 395            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L26)
                NOT_TAKEN
                POP_TOP

 396   L25:     POP_EXCEPT

 397            LOAD_CONST               2 ('UNKNOWN')
                RETURN_VALUE

 395   L26:     RERAISE                  0

  --   L27:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L3 to L4 -> L18 [0]
  L6 to L9 -> L24 [0]
  L10 to L12 -> L24 [0]
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti
  L18 to L19 -> L23 [1] lasti
  L19 to L20 -> L21 [1] lasti
  L21 to L23 -> L23 [1] lasti
  L24 to L25 -> L27 [1] lasti
  L26 to L27 -> L27 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180C4250, file "app\services\operator\fleet_status.py", line 400>:
400           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('chain_status')

402           LOAD_CONST               2 ('Optional[str]')

400           LOAD_CONST               3 ('verification_status')

403           LOAD_CONST               2 ('Optional[str]')

400           LOAD_CONST               4 ('queue_depth')

404           LOAD_CONST               5 ('Optional[int]')

400           LOAD_CONST               6 ('stale_dialing')

405           LOAD_CONST               5 ('Optional[int]')

400           LOAD_CONST               7 ('callback_due')

406           LOAD_CONST               5 ('Optional[int]')

400           LOAD_CONST               8 ('learning_count')

407           LOAD_CONST               5 ('Optional[int]')

400           LOAD_CONST               9 ('security_warnings')

408           LOAD_CONST              10 ('int')

400           LOAD_CONST              11 ('return')

409           LOAD_CONST              12 ('str')

400           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _classify_action_required at 0x0000018C17D8C280, file "app\services\operator\fleet_status.py", line 400>:
400           RESUME                   0

414           LOAD_FAST_BORROW         0 (chain_status)
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (chain_status)
              LOAD_CONST               1 ('ok')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        7 (to L1)
              NOT_TAKEN

415           LOAD_GLOBAL              0 (_ACTION_URGENT)
              RETURN_VALUE

416   L1:     LOAD_FAST_BORROW         1 (verification_status)
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (verification_status)
              LOAD_CONST               2 (('ok', 'skipped', None))
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        7 (to L2)
              NOT_TAKEN

417           LOAD_GLOBAL              0 (_ACTION_URGENT)
              RETURN_VALUE

418   L2:     LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (stale_dialing)
              LOAD_GLOBAL              4 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (stale_dialing)
              LOAD_SMALL_INT           5
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L3)
              NOT_TAKEN

419           LOAD_GLOBAL              0 (_ACTION_URGENT)
              RETURN_VALUE

420   L3:     LOAD_FAST_BORROW         6 (security_warnings)
              LOAD_SMALL_INT           1
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L4)
              NOT_TAKEN

421           LOAD_GLOBAL              0 (_ACTION_URGENT)
              RETURN_VALUE

422   L4:     LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (stale_dialing)
              LOAD_GLOBAL              4 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (stale_dialing)
              LOAD_SMALL_INT           1
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L5)
              NOT_TAKEN

423           LOAD_GLOBAL              6 (_ACTION_ATTENTION)
              RETURN_VALUE

424   L5:     LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (callback_due)
              LOAD_GLOBAL              4 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L6)
              NOT_TAKEN
              LOAD_FAST_BORROW         4 (callback_due)
              LOAD_SMALL_INT          10
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L6)
              NOT_TAKEN

425           LOAD_GLOBAL              6 (_ACTION_ATTENTION)
              RETURN_VALUE

426   L6:     LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (queue_depth)
              LOAD_GLOBAL              4 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L7)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (queue_depth)
              LOAD_SMALL_INT         100
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L7)
              NOT_TAKEN

427           LOAD_GLOBAL              6 (_ACTION_ATTENTION)
              RETURN_VALUE

428   L7:     LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (learning_count)
              LOAD_GLOBAL              4 (int)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       14 (to L8)
              NOT_TAKEN
              LOAD_FAST_BORROW         5 (learning_count)
              LOAD_SMALL_INT          25
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_FALSE        7 (to L8)
              NOT_TAKEN

429           LOAD_GLOBAL              6 (_ACTION_ATTENTION)
              RETURN_VALUE

430   L8:     LOAD_GLOBAL              8 (_ACTION_NONE)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\operator\fleet_status.py", line 437>:
437           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

439           LOAD_CONST               2 ('Optional[Iterable[Any]]')

437           LOAD_CONST               3 ('limit')

440           LOAD_CONST               4 ('Any')

437           LOAD_CONST               5 ('return')

441           LOAD_CONST               6 ('Dict[str, Any]')

437           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object fleet_brokerage_health_summary at 0x0000018C17D7E880, file "app\services\operator\fleet_status.py", line 437>:
 437            RESUME                   0

 455            LOAD_CONST               1 ('ops.fleet.brokerage_health')
                STORE_FAST               2 (surface)

 456            NOP

 457    L1:     LOAD_GLOBAL              1 (_clamp_int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                LOAD_GLOBAL              2 (_LIMIT_MIN)
                LOAD_GLOBAL              4 (_LIMIT_MAX)
                LOAD_GLOBAL              6 (_LIMIT_DEFAULT)
                CALL                     4
                STORE_FAST               3 (capped)

 458            LOAD_GLOBAL              9 (_safe_brokerage_iter + NULL)
                LOAD_FAST_BORROW         0 (brokerage_ids)
                CALL                     1
                STORE_FAST               4 (explicit)

 459            LOAD_FAST_BORROW         4 (explicit)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L2)
                NOT_TAKEN

 460            LOAD_GLOBAL             11 (_safe_brokerage_list_from_db + NULL)
                CALL                     0
                STORE_FAST               4 (explicit)

 461    L2:     LOAD_FAST_BORROW         4 (explicit)
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L6)
        L3:     NOT_TAKEN

 462    L4:     LOAD_GLOBAL             13 (_final_envelope + NULL)

 463            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 464            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 465            LOAD_CONST               5 ('count')
                LOAD_SMALL_INT           0

 466            LOAD_CONST               6 ('rows')
                BUILD_LIST               0

 467            LOAD_CONST               7 ('warnings')
                LOAD_CONST               8 ('no_brokerage_ids_available')
                BUILD_LIST               1

 468            LOAD_CONST               9 ('error_code')
                LOAD_CONST               8 ('no_brokerage_ids_available')

 462            BUILD_MAP                6

 469            LOAD_FAST_BORROW         2 (surface)

 462            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
        L5:     RETURN_VALUE

 470    L6:     LOAD_FAST_BORROW         4 (explicit)
                LOAD_CONST              11 (None)
                LOAD_FAST_BORROW         3 (capped)
                BINARY_SLICE
                STORE_FAST               4 (explicit)

 472            BUILD_LIST               0
                STORE_FAST               5 (rows)

 473            BUILD_LIST               0
                STORE_FAST               6 (warnings)

 474            LOAD_FAST_BORROW         4 (explicit)
                GET_ITER
        L7:     FOR_ITER               199 (to L20)
                STORE_FAST               7 (bid)

 475            LOAD_GLOBAL             15 (_signal_chain_status + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST               8 (chain)

 476            LOAD_GLOBAL             17 (_signal_verification_status + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST               9 (verif)

 477            LOAD_GLOBAL             19 (_signal_queue_depth + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              10 (queue)

 478            LOAD_GLOBAL             21 (_signal_stale_dialing + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              11 (stale)

 479            LOAD_GLOBAL             23 (_signal_callback_due + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              12 (cbdue)

 480            LOAD_GLOBAL             25 (_signal_learning_review_count + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              13 (lrnct)

 481            LOAD_GLOBAL             27 (_signal_security_warning_count + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              14 (secct)

 482            LOAD_GLOBAL             29 (_signal_rollout_stage + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST              15 (stage)

 483            LOAD_GLOBAL             31 (_classify_action_required + NULL)

 484            LOAD_FAST_BORROW         8 (chain)

 485            LOAD_FAST_BORROW         9 (verif)

 486            LOAD_FAST_BORROW        10 (queue)

 487            LOAD_FAST_BORROW        11 (stale)

 488            LOAD_FAST_BORROW        12 (cbdue)

 489            LOAD_FAST_BORROW        13 (lrnct)

 490            LOAD_FAST_BORROW        14 (secct)

 483            LOAD_CONST              12 (('chain_status', 'verification_status', 'queue_depth', 'stale_dialing', 'callback_due', 'learning_count', 'security_warnings'))
                CALL_KW                  7
                STORE_FAST              16 (action)

 492            LOAD_FAST                5 (rows)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_GLOBAL             35 (_project_row + NULL)

 493            LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST                7 (bid)

 494            LOAD_CONST              14 ('latest_chain_status')
                LOAD_FAST                8 (chain)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              15 ('unknown')

 495    L8:     LOAD_CONST              16 ('latest_verification_status')
                LOAD_FAST                9 (verif)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST              15 ('unknown')

 496   L11:     LOAD_CONST              17 ('pending_call_queue_depth')
                LOAD_FAST_BORROW        10 (queue)
                POP_JUMP_IF_NONE         3 (to L12)
                NOT_TAKEN
                LOAD_FAST               10 (queue)
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_SMALL_INT           0

 497   L13:     LOAD_CONST              18 ('stale_dialing_count')
                LOAD_FAST_BORROW        11 (stale)
                POP_JUMP_IF_NONE         3 (to L14)
                NOT_TAKEN
                LOAD_FAST               11 (stale)
                JUMP_FORWARD             1 (to L15)
       L14:     LOAD_SMALL_INT           0

 498   L15:     LOAD_CONST              19 ('callback_due_count')
                LOAD_FAST_BORROW        12 (cbdue)
                POP_JUMP_IF_NONE         3 (to L16)
                NOT_TAKEN
                LOAD_FAST               12 (cbdue)
                JUMP_FORWARD             1 (to L17)
       L16:     LOAD_SMALL_INT           0

 499   L17:     LOAD_CONST              20 ('learning_review_count')
                LOAD_FAST_BORROW        13 (lrnct)
                POP_JUMP_IF_NONE         3 (to L18)
                NOT_TAKEN
                LOAD_FAST               13 (lrnct)
                JUMP_FORWARD             1 (to L19)
       L18:     LOAD_SMALL_INT           0

 500   L19:     LOAD_CONST              21 ('security_warning_count')
                LOAD_FAST_BORROW        14 (secct)

 501            LOAD_CONST              22 ('rollout_stage')
                LOAD_FAST_BORROW        15 (stage)

 502            LOAD_CONST              23 ('action_required')
                LOAD_FAST_BORROW        16 (action)

 492            BUILD_MAP               10
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          201 (to L7)

 474   L20:     END_FOR
                POP_ITER

 508            LOAD_FAST_BORROW         5 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       76 (to L33)
       L21:     NOT_TAKEN
       L22:     LOAD_GLOBAL             36 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L29)
       L23:     NOT_TAKEN
       L24:     POP_TOP
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18010DF0, file "app\services\operator\fleet_status.py", line 508>)
                MAKE_FUNCTION

 511            LOAD_FAST_BORROW         5 (rows)
                GET_ITER

 508            CALL                     0
       L25:     FOR_ITER                12 (to L28)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L27)
       L26:     NOT_TAKEN
                JUMP_BACKWARD           11 (to L25)
       L27:     POP_ITER
                LOAD_CONST              25 (False)
                JUMP_FORWARD            17 (to L30)
       L28:     END_FOR
                POP_ITER
                LOAD_CONST              26 (True)
                JUMP_FORWARD            13 (to L30)
       L29:     PUSH_NULL
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18010DF0, file "app\services\operator\fleet_status.py", line 508>)
                MAKE_FUNCTION

 511            LOAD_FAST_BORROW         5 (rows)
                GET_ITER

 508            CALL                     0
                CALL                     1
       L30:     TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L33)
       L31:     NOT_TAKEN

 513   L32:     LOAD_FAST_BORROW         6 (warnings)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_CONST              27 ('db_unavailable_or_signals_unavailable')
                CALL                     1
                POP_TOP

 515   L33:     LOAD_GLOBAL             13 (_final_envelope + NULL)

 516            LOAD_CONST               2 ('status')
                LOAD_CONST              28 ('ok')

 517            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 518            LOAD_CONST               5 ('count')
                LOAD_GLOBAL             39 (len + NULL)
                LOAD_FAST_BORROW         5 (rows)
                CALL                     1

 519            LOAD_CONST               6 ('rows')
                LOAD_FAST_BORROW         5 (rows)

 520            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         6 (warnings)

 521            LOAD_CONST               9 ('error_code')
                LOAD_CONST              11 (None)

 515            BUILD_MAP                6

 522            LOAD_FAST_BORROW         2 (surface)

 515            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
       L34:     RETURN_VALUE

  --   L35:     PUSH_EXC_INFO

 523            LOAD_GLOBAL             40 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L40)
                NOT_TAKEN
                STORE_FAST              17 (e)

 524   L36:     LOAD_GLOBAL             42 (logger)
                LOAD_ATTR               45 (warning + NULL|self)

 525            LOAD_CONST              29 ('fleet_brokerage_health_summary error type=')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 524            CALL                     1
                POP_TOP

 527            LOAD_GLOBAL             13 (_final_envelope + NULL)

 528            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('skipped')

 529            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 530            LOAD_CONST               5 ('count')
                LOAD_SMALL_INT           0

 531            LOAD_CONST               6 ('rows')
                BUILD_LIST               0

 532            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 533            LOAD_CONST               9 ('error_code')
                LOAD_CONST              30 ('unexpected:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 527            BUILD_MAP                6

 534            LOAD_FAST                2 (surface)

 527            LOAD_CONST              10 (('surface',))
                CALL_KW                  2
       L37:     SWAP                     2
       L38:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L39:     LOAD_CONST              11 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 523   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L35 [0]
  L4 to L5 -> L35 [0]
  L6 to L9 -> L35 [0]
  L10 to L21 -> L35 [0]
  L22 to L23 -> L35 [0]
  L24 to L26 -> L35 [0]
  L27 to L31 -> L35 [0]
  L32 to L34 -> L35 [0]
  L35 to L36 -> L41 [1] lasti
  L36 to L37 -> L39 [1] lasti
  L37 to L38 -> L41 [1] lasti
  L39 to L41 -> L41 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18010DF0, file "app\services\operator\fleet_status.py", line 508>:
 508           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 511   L2:     FOR_ITER                53 (to L6)
               STORE_FAST               1 (r)

 509           LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('latest_chain_status')
               CALL                     1
               LOAD_CONST               1 ('unknown')
               COMPARE_OP              72 (==)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       21 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP

 510           LOAD_FAST_BORROW         1 (r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('latest_verification_status')
               CALL                     1
               LOAD_CONST               1 ('unknown')
               COMPARE_OP              72 (==)

 509   L5:     YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           55 (to L2)

 511   L6:     END_FOR
               POP_ITER
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\operator\fleet_status.py", line 537>:
537           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

539           LOAD_CONST               2 ('Optional[Iterable[Any]]')

537           LOAD_CONST               3 ('limit')

540           LOAD_CONST               4 ('Any')

537           LOAD_CONST               5 ('return')

541           LOAD_CONST               6 ('Dict[str, Any]')

537           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object fleet_chain_status_report at 0x0000018C17EDA250, file "app\services\operator\fleet_status.py", line 537>:
 537           RESUME                   0

 545           LOAD_CONST               1 ('ops.fleet.chain_status')
               STORE_FAST               2 (surface)

 546           LOAD_GLOBAL              1 (fleet_brokerage_health_summary + NULL)

 547           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_ids, limit)

 546           LOAD_CONST               2 (('brokerage_ids', 'limit'))
               CALL_KW                  2
               STORE_FAST               3 (base)

 549           LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               3 ('rows')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     STORE_FAST               4 (rows)

 550           LOAD_GLOBAL              5 (sum + NULL)
               LOAD_CONST               4 (<code object <genexpr> at 0x0000018C1802CAE0, file "app\services\operator\fleet_status.py", line 550>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         4 (rows)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               5 (ok_count)

 551           LOAD_GLOBAL              5 (sum + NULL)
               LOAD_CONST               5 (<code object <genexpr> at 0x0000018C1802C750, file "app\services\operator\fleet_status.py", line 551>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         4 (rows)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               6 (fail_count)

 552           LOAD_GLOBAL              5 (sum + NULL)
               LOAD_CONST               6 (<code object <genexpr> at 0x0000018C1802CC10, file "app\services\operator\fleet_status.py", line 552>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         4 (rows)
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               7 (unk_count)

 554           LOAD_CONST               7 ('ok')
               LOAD_FAST_BORROW         5 (ok_count)

 555           LOAD_CONST               8 ('failed')
               LOAD_FAST_BORROW         6 (fail_count)

 556           LOAD_CONST               9 ('unknown')
               LOAD_FAST_BORROW         7 (unk_count)

 557           LOAD_CONST              10 ('total')
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         4 (rows)
               CALL                     1

 553           BUILD_MAP                4
               STORE_FAST               8 (summary)

 560           LOAD_CONST              11 ('status')
               LOAD_FAST_BORROW         6 (fail_count)
               LOAD_SMALL_INT           0
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       19 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              11 ('status')
               LOAD_CONST               7 ('ok')
               CALL                     2
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               8 ('failed')

 561   L3:     LOAD_CONST              12 ('surface')
               LOAD_FAST                2 (surface)

 562           LOAD_CONST              13 ('summary')
               LOAD_FAST                8 (summary)

 563           LOAD_CONST               3 ('rows')

 571           LOAD_FAST_BORROW         4 (rows)
               GET_ITER

 563           LOAD_FAST_AND_CLEAR      9 (r)
               SWAP                     2
       L4:     BUILD_LIST               0
               SWAP                     2

 571   L5:     FOR_ITER                90 (to L6)
               STORE_FAST               9 (r)

 565           LOAD_CONST              14 ('brokerage_id')
               LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              14 ('brokerage_id')
               CALL                     1

 566           LOAD_CONST              15 ('latest_chain_status')
               LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              15 ('latest_chain_status')
               CALL                     1

 567           LOAD_CONST              16 ('latest_verification_status')
               LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              16 ('latest_verification_status')
               CALL                     1

 568           LOAD_CONST              17 ('rollout_stage')
               LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              17 ('rollout_stage')
               CALL                     1

 569           LOAD_CONST              18 ('action_required')
               LOAD_FAST_BORROW         9 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              18 ('action_required')
               CALL                     1

 564           BUILD_MAP                5
               LIST_APPEND              2
               JUMP_BACKWARD           92 (to L5)

 571   L6:     END_FOR
               POP_ITER

 563   L7:     SWAP                     2
               STORE_FAST               9 (r)

 573           LOAD_CONST              19 ('count')
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_FAST_BORROW         4 (rows)
               CALL                     1

 574           LOAD_CONST              20 ('warnings')
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              20 ('warnings')
               BUILD_LIST               0
               CALL                     2

 575           LOAD_CONST              21 ('error_code')
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              21 ('error_code')
               CALL                     1

 559           BUILD_MAP                7
               STORE_FAST              10 (out)

 577           LOAD_GLOBAL              9 (_final_envelope + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (out, surface)
               LOAD_CONST              22 (('surface',))
               CALL_KW                  2
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 563           SWAP                     2
               STORE_FAST               9 (r)
               RERAISE                  0
ExceptionTable:
  L4 to L7 -> L8 [9]

Disassembly of <code object <genexpr> at 0x0000018C1802CAE0, file "app\services\operator\fleet_status.py", line 550>:
 550           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('latest_chain_status')
               CALL                     1
               LOAD_CONST               1 ('ok')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802C750, file "app\services\operator\fleet_status.py", line 551>:
 551           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('latest_chain_status')
               CALL                     1
               LOAD_CONST               2 (('ok', 'unknown'))
               CONTAINS_OP              1 (not in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C1802CC10, file "app\services\operator\fleet_status.py", line 552>:
 552           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                30 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               0 ('latest_chain_status')
               CALL                     1
               LOAD_CONST               1 ('unknown')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           32 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\fleet_status.py", line 580>:
580           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

582           LOAD_CONST               2 ('Optional[Iterable[Any]]')

580           LOAD_CONST               3 ('limit')

583           LOAD_CONST               4 ('Any')

580           LOAD_CONST               5 ('return')

584           LOAD_CONST               6 ('Dict[str, Any]')

580           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object fleet_rollout_readiness_summary at 0x0000018C17EDA5A0, file "app\services\operator\fleet_status.py", line 580>:
580           RESUME                   0

586           LOAD_CONST               1 ('ops.fleet.rollout_readiness')
              STORE_FAST               2 (surface)

587           LOAD_GLOBAL              1 (fleet_brokerage_health_summary + NULL)

588           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_ids, limit)

587           LOAD_CONST               2 (('brokerage_ids', 'limit'))
              CALL_KW                  2
              STORE_FAST               3 (base)

590           LOAD_FAST_BORROW         3 (base)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               3 ('rows')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               4 (rows)

591           BUILD_MAP                0
              STORE_FAST               5 (by_stage)

592           BUILD_MAP                0
              STORE_FAST               6 (by_action)

593           LOAD_FAST_BORROW         4 (rows)
              GET_ITER
      L2:     FOR_ITER               115 (to L5)
              STORE_FAST               7 (r)

594           LOAD_FAST_BORROW         7 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               4 ('rollout_stage')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('UNKNOWN')
      L3:     STORE_FAST               8 (stage)

595           LOAD_FAST_BORROW         7 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               6 ('action_required')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         7 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              4 (_ACTION_NONE)
      L4:     STORE_FAST               9 (action)

596           LOAD_FAST_BORROW         5 (by_stage)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         8 (stage)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (by_stage, stage)
              STORE_SUBSCR

597           LOAD_FAST_BORROW         6 (by_action)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_FAST_BORROW         9 (action)
              LOAD_SMALL_INT           0
              CALL                     2
              LOAD_SMALL_INT           1
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 105 (by_action, action)
              STORE_SUBSCR
              JUMP_BACKWARD          117 (to L2)

593   L5:     END_FOR
              POP_ITER

598           LOAD_GLOBAL              7 (_final_envelope + NULL)

599           LOAD_CONST               7 ('status')
              LOAD_FAST_BORROW         3 (base)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               7 ('status')
              LOAD_CONST               8 ('ok')
              CALL                     2

600           LOAD_CONST               9 ('surface')
              LOAD_FAST_BORROW         2 (surface)

601           LOAD_CONST              10 ('by_stage')
              LOAD_FAST_BORROW         5 (by_stage)

602           LOAD_CONST              11 ('by_action')
              LOAD_FAST_BORROW         6 (by_action)

603           LOAD_CONST              12 ('count')
              LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         4 (rows)
              CALL                     1

604           LOAD_CONST              13 ('warnings')
              LOAD_FAST_BORROW         3 (base)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              13 ('warnings')
              BUILD_LIST               0
              CALL                     2

605           LOAD_CONST              14 ('error_code')
              LOAD_FAST_BORROW         3 (base)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              14 ('error_code')
              CALL                     1

598           BUILD_MAP                7

606           LOAD_FAST_BORROW         2 (surface)

598           LOAD_CONST              15 (('surface',))
              CALL_KW                  2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\operator\fleet_status.py", line 609>:
609           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

611           LOAD_CONST               2 ('Optional[Iterable[Any]]')

609           LOAD_CONST               3 ('limit')

612           LOAD_CONST               4 ('Any')

609           LOAD_CONST               5 ('return')

613           LOAD_CONST               6 ('Dict[str, Any]')

609           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object fleet_exception_report at 0x0000018C17D76780, file "app\services\operator\fleet_status.py", line 609>:
 609           RESUME                   0

 616           LOAD_CONST               1 ('ops.fleet.exceptions')
               STORE_FAST               2 (surface)

 617           LOAD_GLOBAL              1 (fleet_brokerage_health_summary + NULL)

 618           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage_ids, limit)

 617           LOAD_CONST               2 (('brokerage_ids', 'limit'))
               CALL_KW                  2
               STORE_FAST               3 (base)

 620           LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               3 ('rows')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     STORE_FAST               4 (rows)

 622           LOAD_FAST_BORROW         4 (rows)
               GET_ITER

 621           LOAD_FAST_AND_CLEAR      5 (r)
               SWAP                     2
       L2:     BUILD_LIST               0
               SWAP                     2

 622   L3:     FOR_ITER                39 (to L6)
               STORE_FAST               5 (r)

 623           LOAD_FAST_BORROW         5 (r)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               4 ('action_required')
               CALL                     1
               LOAD_GLOBAL              4 (_ACTION_ATTENTION)
               LOAD_GLOBAL              6 (_ACTION_URGENT)
               BUILD_TUPLE              2
               CONTAINS_OP              0 (in)

 622   L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           37 (to L3)
       L5:     LOAD_FAST_BORROW         5 (r)
               LIST_APPEND              2
               JUMP_BACKWARD           41 (to L3)
       L6:     END_FOR
               POP_ITER

 621   L7:     STORE_FAST               6 (exceptions)
               STORE_FAST               5 (r)

 625           LOAD_GLOBAL              9 (_final_envelope + NULL)

 626           LOAD_CONST               5 ('status')
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('status')
               LOAD_CONST               6 ('ok')
               CALL                     2

 627           LOAD_CONST               7 ('surface')
               LOAD_FAST_BORROW         2 (surface)

 628           LOAD_CONST               8 ('count')
               LOAD_GLOBAL             11 (len + NULL)
               LOAD_FAST_BORROW         6 (exceptions)
               CALL                     1

 629           LOAD_CONST               3 ('rows')
               LOAD_FAST_BORROW         6 (exceptions)

 630           LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               9 ('warnings')
               BUILD_LIST               0
               CALL                     2

 631           LOAD_CONST              10 ('error_code')
               LOAD_FAST_BORROW         3 (base)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              10 ('error_code')
               CALL                     1

 625           BUILD_MAP                6

 632           LOAD_FAST_BORROW         2 (surface)

 625           LOAD_CONST              11 (('surface',))
               CALL_KW                  2
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 621           SWAP                     2
               STORE_FAST               5 (r)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]
```
