# monitoring/detectors

- **pyc:** `app\services\monitoring\__pycache__\detectors.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/detectors.py`
- **co_filename (from bytecode):** `app\services\monitoring\detectors.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS143F2 — Deterministic monitoring detectors.

Each `detect_*` function consumes the JSON-shape that the upstream
audit / verification / replay / optimization tools already emit, and
returns a list of `Alert` objects. Detectors:

  - never raise (defensive on every input)
  - never call I/O (pure transforms over the dict-shape they receive)
  - never include raw secrets, transcripts, or PII in alert bodies
    (the dispatcher redacts again as a belt-and-braces second pass)

Coverage:
  detect_security_findings        — security_audit_report.json
  detect_integrity_findings       — integrity_check_report.json
  detect_backup_verification      — verification_report.json
  detect_event_ingestion_health   — pas_events row list (or stats)
  detect_tenant_scope_violation   — TenantScopingError instance / dict
  detect_replay_quality           — evaluator output OR reconstruction
  detect_optimization_health      — generate_optimization_report dict
```

## Imports

`Alert`, `Any`, `Category`, `List`, `Optional`, `Severity`, `TenantScopingError`, `__future__`, `annotations`, `app.db.tenant_safe`, `app.services.monitoring.contracts`, `re`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_push`, `_safe_id_fragment`, `_try_alert`, `detect_backup_verification`, `detect_event_ingestion_health`, `detect_integrity_findings`, `detect_optimization_health`, `detect_replay_quality`, `detect_restore_drill_failures`, `detect_security_findings`, `detect_tenant_scope_violation`

## Env-key candidates

`CRITICAL`, `HIGH`, `MEDIUM`

## String constants (redacted where noted)

- '\nPAS143F2 — Deterministic monitoring detectors.\n\nEach `detect_*` function consumes the JSON-shape that the upstream\naudit / verification / replay / optimization tools already emit, and\nreturns a list of `Alert` objects. Detectors:\n\n  - never raise (defensive on every input)\n  - never call I/O (pure transforms over the dict-shape they receive)\n  - never include raw secrets, transcripts, or PII in alert bodies\n    (the dispatcher redacts again as a belt-and-braces second pass)\n\nCoverage:\n  detect_security_findings        — security_audit_report.json\n  detect_integrity_findings       — integrity_check_report.json\n  detect_backup_verification      — verification_report.json\n  detect_event_ingestion_health   — pas_events row list (or stats)\n  detect_tenant_scope_violation   — TenantScopingError instance / dict\n  detect_replay_quality           — evaluator output OR reconstruction\n  detect_optimization_health      — generate_optimization_report dict\n'
- 'app.services.monitoring.detectors'
- 'max_len'
- 'Any'
- 'int'
- 'return'
- 'str'
- 'Coerce arbitrary input to a slug suitable for an Alert.id suffix.'
- 'unknown'
- '[^A-Za-z0-9]+'
- 'Optional[Alert]'
- 'Construct an Alert; return None on bad input rather than raising.'
- 'out'
- 'List[Alert]'
- 'alert'
- 'None'
- 'security_report'
- '\nConsume scripts/security_audit.py output.\n\nMaps:\n  counts.CRITICAL > 0  → CRITICAL SECURITY alert\n  counts.HIGH > 0      → HIGH SECURITY alert (only if no CRITICAL)\nNever reproduces the secret value — only counts + file references.\n'
- 'counts'
- 'CRITICAL'
- 'HIGH'
- 'MEDIUM'
- 'security_critical_findings'
- 'Security audit found '
- ' CRITICAL finding(s)'
- 'The static security scanner reported one or more CRITICAL findings (literal secret pattern). Block deploys until remediated; rotate any leaked credentials.'
- 'critical_count'
- 'high_count'
- 'medium_count'
- 'security_high_findings'
- ' HIGH finding(s)'
- 'Static security scanner reported HIGH findings. Review before next deploy; resolve before persisting brain memory.'
- 'integrity_report'
- '\nConsume scripts/integrity_check.py output.\n\nEach failed check becomes one INTEGRITY alert. Severity is\nclassified by token in the check name.\n'
- 'results'
- 'passed'
- 'name'
- 'detail'
- 'integrity_'
- 'Integrity check failed: '
- '<unnamed>'
- "See integrity_check_report.json for the failing check's context."
- 'check_name'
- 'category'
- 'verification_report'
- '\nConsume scripts/verify_backup.py output.\n\nSeverity:\n  checksum mismatch / dump missing / dump empty → CRITICAL\n  manifest missing / JSONL malformed / row-count mismatch → HIGH\n  anything else failing → HIGH\n'
- 'checks'
- 'sha-256'
- 'sha256'
- 'checksum'
- 'Backup checksum mismatch'
- 'non-empty'
- 'Backup dump file empty'
- 'dump file exists'
- 'Backup dump file missing'
- 'manifest'
- 'Backup manifest unreadable or absent'
- 'jsonl parses'
- 'Event JSONL inside backup is malformed'
- 'row count'
- 'row_count'
- 'Event row count does not match manifest'
- 'Backup verification failed: '
- 'backup_'
- 'Re-run scripts/verify_backup.py --strict against this directory; do not rely on this backup until it passes.'
- 'events'
- '\nLightweight statistical detector over a list of pas_events rows.\n\nInputs accepted: list[dict] | None | anything-else.\n'
- 'ingestion_empty_window'
- 'No pas_events in inspected window'
- 'The event stream is empty. Investigate Supabase reachability, service-role key validity, or a stalled engine.'
- 'event_count'
- 'ingestion_volume_spike'
- 'Event volume spike: '
- ' events in window'
- 'Investigate which event_type dominates the window — usually indicates a misconfigured loop or an over-emitting feature.'
- 'ingestion_provider_failure_spike'
- 'Provider failure spike: '
- ' provider.failed events'
- 'Investigate provider outage or API-key failure. Likely culprits: Anthropic / OpenAI / Twilio / Deepgram / Cal.com.'
- 'provider_failed_count'
- 'event_id'
- 'ingestion_duplicate_event_ids'
- 'Duplicate event_ids detected ('
- 'Possible double-write or replay corruption. Confirm the UNIQUE INDEX on pas_events.event_id is in place.'
- 'duplicate_count'
- 'call_id'
- 'event_type'
- 'call.ended'
- 'lead.uttered'
- 'pas.uttered'
- 'ingestion_missing_turn_events'
- ' completed call(s) lack turn events'
- 'Calls completed without lead.uttered / pas.uttered rows. PAS_EVENT_TURN_LOGGING may be off or a write path is dropping turns.'
- 'affected_calls'
- 'provider.failed'
- 'error_or_event'
- '\nSurface attempted cross-tenant reads as CRITICAL.\n\nAccepted shapes:\n  - TenantScopingError instance\n  - other Exception (only flagged if message mentions tenant/brokerage)\n  - str: error message\n  - dict: {message, source?, brokerage_id?, context?, unscoped?}\n\nThe portal-context unscoped attempt is the most dangerous; flagged\nexplicitly with its own alert id.\n'
- 'tenant_scoping_error'
- 'Tenant scoping violation: TenantScopingError raised'
- 'error_class'
- 'TenantScopingError'
- 'brokerage'
- 'tenant'
- 'tenant_unknown_exception'
- 'Tenant-related exception raised'
- 'context'
- 'unscoped'
- 'message'
- 'brokerage_id'
- 'portal'
- 'tenant_unscoped_in_portal'
- 'Unscoped read attempted in portal context'
- 'A portal-context call attempted an unscoped data access. Stop tenant memory writes immediately and investigate the call site.'
- 'tenant_scoping_dict'
- 'Tenant scoping signal received'
- 'source'
- 'tenant_scoping_message'
- 'replay_or_reconstruction'
- '\nAccept either:\n  - evaluator output: {replay_score, is_replayable, missing_steps, summary}\n  - reconstruction output: {final_outcome, missing_lifecycle_steps, ...}\n'
- 'replay_score'
- 'replay_score_out_of_range'
- 'Replay score '
- ' outside [0, 100]'
- 'The evaluator returned an out-of-range score. Likely a bug in evaluate_reconstruction or corrupted reconstruction input.'
- 'score'
- 'is_replayable'
- 'final_outcome'
- 'replay_unreplayable_terminal'
- "Call had terminal outcome '"
- "' but is not replayable"
- "Lifecycle gaps prevent reconstruction. Audit the call's event stream — usually means lead.uttered / pas.uttered rows are missing."
- 'outcome'
- 'missing_steps'
- 'missing_lifecycle_steps'
- 'completed'
- 'replay_missing_completed_step'
- "Reconstruction missing 'completed' step"
- 'No terminal event (call.ended / call.ended_with_callback / call.failed) was found in the event stream. Operators should audit recent calls for missing terminal events.'
- 'restore_report'
- '\nConsume scripts/restore_drill.py output (`restore_drill_report.json`).\n\nSeverity rules (from PAS143G monitoring integration):\n  - restore_success == False        → CRITICAL BACKUP alert\n  - integrity_status != "pass"      → HIGH BACKUP alert\n  - monitoring_status != "pass"     → HIGH BACKUP alert\n  - durations.total_s > threshold   → MEDIUM BACKUP alert\n'
- 'restore_success'
- 'failures'
- 'backup_restore_drill_failed'
- 'Restore drill failed'
- 'The drill could not reconstruct the backup. Investigate the failure list before relying on this archive for production restore. Summary: '
- 'see restore_drill_report.json'
- 'archive'
- 'failure_count'
- 'integrity_status'
- 'backup_restore_drill_integrity_fail'
- 'Integrity check failed during restore drill'
- 'The restored backup did not pass the integrity check. The archive may be from a substrate version that has since drifted; treat the backup as suspect until investigated.'
- 'monitoring_status'
- 'backup_restore_drill_monitoring_fail'
- 'Monitoring check failed during restore drill'
- 'Running the monitoring check inside the drill workspace produced HIGH/CRITICAL alerts. The backup itself may be fine, but the substrate that produced it had open issues.'
- 'durations'
- 'total_s'
- 'backup_restore_drill_slow'
- 'Restore drill ran slowly ('
- '.1f'
- 'Drill exceeded the comfort threshold. Right-size the backup, prune historic dumps, or move the workspace to faster storage.'
- 'threshold_s'
- 'optimization_report'
- '\nValidate the post-PAS143C optimization report shape.\n'
- 'metrics'
- 'ranked_strategies'
- 'optimization_negative_metrics'
- 'Negative aggregate metric value(s): '
- 'Aggregation bug — every metric in compute_matrix_metrics should be non-negative.'
- 'negative_keys'
- 'total_runs'
- 'optimization_empty_matrix'
- 'Optimization matrix is empty (no runs)'
- 'No cells in the matrix — check the scenario/strategy filters or registry contents.'
- 'optimization_ranking_invalid'
- 'Strategy ranking not monotonically descending'
- 'rank_strategies returned scores out of order — investigate the sort key.'
- 'first_5_scores'
- 'optimization_all_strategies_tied'
- 'All strategies tied at top score'
- 'Scenarios may not exercise the strategy axes. Add more scenarios that target distinct personalities.'
- 'strategies_count'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143F2 — Deterministic monitoring detectors.\n\nEach `detect_*` function consumes the JSON-shape that the upstream\naudit / verification / replay / optimization tools already emit, and\nreturns a list of `Alert` objects. Detectors:\n\n  - never raise (defensive on every input)\n  - never call I/O (pure transforms over the dict-shape they receive)\n  - never include raw secrets, transcripts, or PII in alert bodies\n    (the dispatcher redacts again as a belt-and-braces second pass)\n\nCoverage:\n  detect_security_findings        — security_audit_report.json\n  detect_integrity_findings       — integrity_check_report.json\n  detect_backup_verification      — verification_report.json\n  detect_event_ingestion_health   — pas_events row list (or stats)\n  detect_tenant_scope_violation   — TenantScopingError instance / dict\n  detect_replay_quality           — evaluator output OR reconstruction\n  detect_optimization_health      — generate_optimization_report dict\n')
              STORE_NAME               0 (__doc__)

 23           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 25           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (re)
              STORE_NAME               3 (re)

 26           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (List)
              STORE_NAME               6 (List)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 28           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('TenantScopingError',))
              IMPORT_NAME              8 (app.db.tenant_safe)
              IMPORT_FROM              9 (TenantScopingError)
              STORE_NAME               9 (TenantScopingError)
              POP_TOP

 29           LOAD_SMALL_INT           0
              LOAD_CONST               5 (('Alert', 'Category', 'Severity'))
              IMPORT_NAME             10 (app.services.monitoring.contracts)
              IMPORT_FROM             11 (Alert)
              STORE_NAME              11 (Alert)
              IMPORT_FROM             12 (Category)
              STORE_NAME              12 (Category)
              IMPORT_FROM             13 (Severity)
              STORE_NAME              13 (Severity)
              POP_TOP

 36           LOAD_CONST               6 ('app.services.monitoring.detectors')
              STORE_NAME              14 (_SOURCE)

 39           LOAD_CONST               7 ('max_len')
              LOAD_SMALL_INT          60
              BUILD_MAP                1
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\monitoring\detectors.py", line 39>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _safe_id_fragment at 0x0000018C180608A0, file "app\services\monitoring\detectors.py", line 39>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              15 (_safe_id_fragment)

 51           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\monitoring\detectors.py", line 51>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _try_alert at 0x0000018C17FBFEE0, file "app\services\monitoring\detectors.py", line 51>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_try_alert)

 59           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\monitoring\detectors.py", line 59>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _push at 0x0000018C180C4140, file "app\services\monitoring\detectors.py", line 59>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_push)

 68           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\monitoring\detectors.py", line 68>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object detect_security_findings at 0x0000018C17D7D650, file "app\services\monitoring\detectors.py", line 68>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (detect_security_findings)

125           LOAD_CONST              32 (('duplicate', 'outcome', 'impossible', 'invalid'))
              STORE_NAME              19 (_INTEGRITY_HIGH_TOKENS)

126           LOAD_CONST              33 (('malformed', 'missing', 'consistency'))
              STORE_NAME              20 (_INTEGRITY_MEDIUM_TOKENS)

129           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\monitoring\detectors.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object detect_integrity_findings at 0x0000018C17ED7630, file "app\services\monitoring\detectors.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (detect_integrity_findings)

179           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\monitoring\detectors.py", line 179>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object detect_backup_verification at 0x0000018C17ED7F90, file "app\services\monitoring\detectors.py", line 179>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (detect_backup_verification)

249           LOAD_SMALL_INT           5
              STORE_NAME              23 (_PROVIDER_FAILURE_SPIKE)

253           LOAD_CONST              20 (5000)
              STORE_NAME              24 (_EVENT_VOLUME_SPIKE)

256           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\monitoring\detectors.py", line 256>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object detect_event_ingestion_health at 0x0000018C17D8AB60, file "app\services\monitoring\detectors.py", line 256>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (detect_event_ingestion_health)

381           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\monitoring\detectors.py", line 381>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object detect_tenant_scope_violation at 0x0000018C17D8BE60, file "app\services\monitoring\detectors.py", line 381>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (detect_tenant_scope_violation)

481           BUILD_SET                0
              LOAD_CONST              34 (frozenset({'booked', 'qualified_callback_requested', 'callback_requested'}))
              SET_UPDATE               1
              STORE_NAME              27 (_TERMINAL_OUTCOMES)

486           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\monitoring\detectors.py", line 486>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object detect_replay_quality at 0x0000018C17D81A00, file "app\services\monitoring\detectors.py", line 486>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (detect_replay_quality)

558           LOAD_CONST              27 (300.0)
              STORE_NAME              29 (_RESTORE_DRILL_SLOW_S)

561           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\monitoring\detectors.py", line 561>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object detect_restore_drill_failures at 0x0000018C17F7D8D0, file "app\services\monitoring\detectors.py", line 561>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (detect_restore_drill_failures)

653           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\monitoring\detectors.py", line 653>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object detect_optimization_health at 0x0000018C17E04B30, file "app\services\monitoring\detectors.py", line 653>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (detect_optimization_health)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\monitoring\detectors.py", line 39>:
 39           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('s')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_id_fragment at 0x0000018C180608A0, file "app\services\monitoring\detectors.py", line 39>:
  39           RESUME                   0

  41           LOAD_FAST_BORROW         0 (s)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  42           LOAD_CONST               2 ('unknown')
               RETURN_VALUE

  43   L1:     NOP

  44   L2:     LOAD_GLOBAL              1 (str + NULL)
               LOAD_FAST_BORROW         0 (s)
               CALL                     1
               STORE_FAST               2 (text)

  47   L3:     LOAD_GLOBAL              4 (re)
               LOAD_ATTR                6 (sub)
               PUSH_NULL
               LOAD_CONST               3 ('[^A-Za-z0-9]+')
               LOAD_CONST               4 ('_')
               LOAD_FAST                2 (text)
               CALL                     3
               LOAD_ATTR                9 (strip + NULL|self)
               LOAD_CONST               4 ('_')
               CALL                     1
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (text)

  48           LOAD_FAST                2 (text)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('unknown')
       L4:     LOAD_CONST               1 (None)
               LOAD_FAST                1 (max_len)
               BINARY_SLICE
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  45           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

  46   L6:     POP_EXCEPT
               LOAD_CONST               2 ('unknown')
               RETURN_VALUE

  45   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\monitoring\detectors.py", line 51>:
 51           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[Alert]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _try_alert at 0x0000018C17FBFEE0, file "app\services\monitoring\detectors.py", line 51>:
  51           RESUME                   0

  53           NOP

  54   L1:     LOAD_GLOBAL              1 (Alert + NULL)
               LOAD_CONST               2 (())
               BUILD_MAP                0
               LOAD_FAST_BORROW         0 (kw)
               DICT_MERGE               1
               CALL_FUNCTION_EX
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  55           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

  56   L4:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

  55   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\monitoring\detectors.py", line 59>:
 59           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('out')
              LOAD_CONST               2 ('List[Alert]')
              LOAD_CONST               3 ('alert')
              LOAD_CONST               4 ('Optional[Alert]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _push at 0x0000018C180C4140, file "app\services\monitoring\detectors.py", line 59>:
 59           RESUME                   0

 60           LOAD_FAST_BORROW         1 (alert)
              POP_JUMP_IF_NONE        20 (to L1)
              NOT_TAKEN

 61           LOAD_FAST_BORROW         0 (out)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_FAST_BORROW         1 (alert)
              CALL                     1
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

 60   L1:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\monitoring\detectors.py", line 68>:
 68           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('security_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_security_findings at 0x0000018C17D7D650, file "app\services\monitoring\detectors.py", line 68>:
 68           RESUME                   0

 77           BUILD_LIST               0
              STORE_FAST               1 (out)

 78           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (security_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 79           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

 81   L1:     LOAD_FAST_BORROW         0 (security_report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('counts')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     STORE_FAST               2 (counts)

 82           LOAD_GLOBAL              7 (int + NULL)
              LOAD_FAST_BORROW         2 (counts)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('CRITICAL')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L3:     CALL                     1
              STORE_FAST               3 (crit)

 83           LOAD_GLOBAL              7 (int + NULL)
              LOAD_FAST_BORROW         2 (counts)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('HIGH')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L4:     CALL                     1
              STORE_FAST               4 (high)

 84           LOAD_GLOBAL              7 (int + NULL)
              LOAD_FAST_BORROW         2 (counts)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('MEDIUM')
              LOAD_SMALL_INT           0
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
      L5:     CALL                     1
              STORE_FAST               5 (medium)

 86           LOAD_FAST_BORROW         3 (crit)
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       73 (to L6)
              NOT_TAKEN

 87           LOAD_GLOBAL              9 (_push + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_GLOBAL             11 (_try_alert + NULL)

 88           LOAD_CONST               5 ('security_critical_findings')

 89           LOAD_GLOBAL             12 (Category)
              LOAD_ATTR               14 (SECURITY)

 90           LOAD_GLOBAL             16 (Severity)
              LOAD_ATTR               18 (CRITICAL)

 91           LOAD_CONST               6 ('Security audit found ')
              LOAD_FAST_BORROW         3 (crit)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' CRITICAL finding(s)')
              BUILD_STRING             3

 93           LOAD_CONST               8 ('The static security scanner reported one or more CRITICAL findings (literal secret pattern). Block deploys until remediated; rotate any leaked credentials.')

 97           LOAD_GLOBAL             20 (_SOURCE)

 99           LOAD_CONST               9 ('critical_count')
              LOAD_FAST_BORROW         3 (crit)

100           LOAD_CONST              10 ('high_count')
              LOAD_FAST_BORROW         4 (high)

101           LOAD_CONST              11 ('medium_count')
              LOAD_FAST_BORROW         5 (medium)

 98           BUILD_MAP                3

 87           LOAD_CONST              12 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
              CALL_KW                  7
              CALL                     2
              POP_TOP

117           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

104   L6:     LOAD_FAST_BORROW         4 (high)
              LOAD_SMALL_INT           0
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       69 (to L7)
              NOT_TAKEN

105           LOAD_GLOBAL              9 (_push + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_GLOBAL             11 (_try_alert + NULL)

106           LOAD_CONST              13 ('security_high_findings')

107           LOAD_GLOBAL             12 (Category)
              LOAD_ATTR               14 (SECURITY)

108           LOAD_GLOBAL             16 (Severity)
              LOAD_ATTR               22 (HIGH)

109           LOAD_CONST               6 ('Security audit found ')
              LOAD_FAST_BORROW         4 (high)
              FORMAT_SIMPLE
              LOAD_CONST              14 (' HIGH finding(s)')
              BUILD_STRING             3

111           LOAD_CONST              15 ('Static security scanner reported HIGH findings. Review before next deploy; resolve before persisting brain memory.')

114           LOAD_GLOBAL             20 (_SOURCE)

115           LOAD_CONST              10 ('high_count')
              LOAD_FAST_BORROW         4 (high)
              LOAD_CONST              11 ('medium_count')
              LOAD_FAST_BORROW         5 (medium)
              BUILD_MAP                2

105           LOAD_CONST              12 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
              CALL_KW                  7
              CALL                     2
              POP_TOP

117   L7:     LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\monitoring\detectors.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('integrity_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_integrity_findings at 0x0000018C17ED7630, file "app\services\monitoring\detectors.py", line 129>:
  --            MAKE_CELL                7 (name_lower)

 129            RESUME                   0

 136            BUILD_LIST               0
                STORE_FAST               1 (out)

 137            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (integrity_report)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 138            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 140    L1:     LOAD_FAST_BORROW         0 (integrity_report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('results')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L2:     STORE_FAST               2 (results)

 141            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (results)
                LOAD_GLOBAL              6 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 142            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 144    L3:     LOAD_FAST_BORROW         2 (results)
                GET_ITER
        L4:     EXTENDED_ARG             1
                FOR_ITER               468 (to L25)
                STORE_FAST               3 (r)

 145            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 146            JUMP_BACKWARD           28 (to L4)

 147    L5:     LOAD_FAST_BORROW         3 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('passed')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 148            JUMP_BACKWARD           53 (to L4)

 149    L6:     LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         3 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('name')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L7:     CALL                     1
                STORE_FAST               4 (name)

 150            LOAD_FAST_BORROW         4 (name)
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              7 (name_lower)

 151            LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         3 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('detail')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L8:     CALL                     1
                LOAD_CONST               6 (slice(None, 300, None))
                BINARY_OP               26 ([])
                STORE_FAST               5 (detail)

 153            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         7 (name_lower)
                BUILD_TUPLE              1
                LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18025C30, file "app\services\monitoring\detectors.py", line 153>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             14 (_INTEGRITY_HIGH_TOKENS)
                GET_ITER
                CALL                     0
        L9:     FOR_ITER                12 (to L11)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L9)
       L10:     POP_ITER
                LOAD_CONST               8 (True)
                JUMP_FORWARD            24 (to L13)
       L11:     END_FOR
                POP_ITER
                LOAD_CONST               9 (False)
                JUMP_FORWARD            20 (to L13)
       L12:     PUSH_NULL
                LOAD_FAST_BORROW         7 (name_lower)
                BUILD_TUPLE              1
                LOAD_CONST               7 (<code object <genexpr> at 0x0000018C18025C30, file "app\services\monitoring\detectors.py", line 153>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             14 (_INTEGRITY_HIGH_TOKENS)
                GET_ITER
                CALL                     0
                CALL                     1
       L13:     TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L14)
                NOT_TAKEN

 154            LOAD_GLOBAL             16 (Severity)
                LOAD_ATTR               18 (HIGH)
                STORE_FAST               6 (sev)
                JUMP_FORWARD           105 (to L21)

 155   L14:     LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       35 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         7 (name_lower)
                BUILD_TUPLE              1
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18024930, file "app\services\monitoring\detectors.py", line 155>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             20 (_INTEGRITY_MEDIUM_TOKENS)
                GET_ITER
                CALL                     0
       L15:     FOR_ITER                12 (to L17)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L15)
       L16:     POP_ITER
                LOAD_CONST               8 (True)
                JUMP_FORWARD            24 (to L19)
       L17:     END_FOR
                POP_ITER
                LOAD_CONST               9 (False)
                JUMP_FORWARD            20 (to L19)
       L18:     PUSH_NULL
                LOAD_FAST_BORROW         7 (name_lower)
                BUILD_TUPLE              1
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18024930, file "app\services\monitoring\detectors.py", line 155>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_GLOBAL             20 (_INTEGRITY_MEDIUM_TOKENS)
                GET_ITER
                CALL                     0
                CALL                     1
       L19:     TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L20)
                NOT_TAKEN

 156            LOAD_GLOBAL             16 (Severity)
                LOAD_ATTR               22 (MEDIUM)
                STORE_FAST               6 (sev)
                JUMP_FORWARD            16 (to L21)

 158   L20:     LOAD_GLOBAL             16 (Severity)
                LOAD_ATTR               22 (MEDIUM)
                STORE_FAST               6 (sev)

 160   L21:     LOAD_GLOBAL             25 (_push + NULL)
                LOAD_FAST                1 (out)
                LOAD_GLOBAL             27 (_try_alert + NULL)

 161            LOAD_CONST              11 ('integrity_')
                LOAD_GLOBAL             29 (_safe_id_fragment + NULL)
                LOAD_FAST_BORROW         4 (name)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2

 162            LOAD_GLOBAL             30 (Category)
                LOAD_ATTR               32 (INTEGRITY)

 163            LOAD_FAST                6 (sev)

 164            LOAD_CONST              12 ('Integrity check failed: ')
                LOAD_FAST_BORROW         4 (name)
                LOAD_CONST              13 (slice(None, 80, None))
                BINARY_OP               26 ([])
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              14 ('<unnamed>')
       L22:     FORMAT_SIMPLE
                BUILD_STRING             2

 166            LOAD_FAST                5 (detail)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                POP_TOP

 167            LOAD_CONST              15 ("See integrity_check_report.json for the failing check's context.")

 169   L23:     LOAD_GLOBAL             34 (_SOURCE)

 170            LOAD_CONST              16 ('check_name')
                LOAD_FAST                4 (name)
                LOAD_CONST              17 ('category')
                LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         3 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              17 ('category')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
       L24:     CALL                     1
                BUILD_MAP                2

 160            LOAD_CONST              18 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP
                EXTENDED_ARG             1
                JUMP_BACKWARD          471 (to L4)

 144   L25:     END_FOR
                POP_ITER

 172            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "app\services\monitoring\detectors.py", line 153>:
  --           COPY_FREE_VARS           1

 153           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (tok, tok)
               LOAD_DEREF               2 (name_lower)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "app\services\monitoring\detectors.py", line 155>:
  --           COPY_FREE_VARS           1

 155           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (tok, tok)
               LOAD_DEREF               2 (name_lower)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\monitoring\detectors.py", line 179>:
179           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('verification_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_backup_verification at 0x0000018C17ED7F90, file "app\services\monitoring\detectors.py", line 179>:
179            RESUME                   0

188            BUILD_LIST               0
               STORE_FAST               1 (out)

189            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (verification_report)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

190            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

192    L1:     LOAD_FAST_BORROW         0 (verification_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('checks')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L2:     STORE_FAST               2 (checks)

193            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (checks)
               LOAD_GLOBAL              6 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

194            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

196    L3:     LOAD_FAST_BORROW         2 (checks)
               GET_ITER
       L4:     EXTENDED_ARG             1
               FOR_ITER               423 (to L19)
               STORE_FAST               3 (c)

197            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (c)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

198            JUMP_BACKWARD           28 (to L4)

199    L5:     LOAD_FAST_BORROW         3 (c)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('ok')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

200            JUMP_BACKWARD           53 (to L4)

201    L6:     LOAD_GLOBAL              9 (str + NULL)
               LOAD_FAST_BORROW         3 (c)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('name')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L7:     CALL                     1
               STORE_FAST               4 (name)

202            LOAD_FAST_BORROW         4 (name)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (name_l)

203            LOAD_GLOBAL              9 (str + NULL)
               LOAD_FAST_BORROW         3 (c)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('detail')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L8:     CALL                     1
               LOAD_CONST               6 (slice(None, 300, None))
               BINARY_OP               26 ([])
               STORE_FAST               6 (detail)

205            LOAD_CONST               7 ('sha-256')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        15 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('sha256')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         8 (to L9)
               NOT_TAKEN
               LOAD_CONST               9 ('checksum')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L10)
               NOT_TAKEN

206    L9:     LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               14 (CRITICAL)
               STORE_FAST               7 (sev)

207            LOAD_CONST              10 ('Backup checksum mismatch')
               STORE_FAST               8 (title)
               JUMP_FORWARD           165 (to L17)

208   L10:     LOAD_CONST              11 ('non-empty')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L11)
               NOT_TAKEN

209            LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               14 (CRITICAL)
               STORE_FAST               7 (sev)

210            LOAD_CONST              12 ('Backup dump file empty')
               STORE_FAST               8 (title)
               JUMP_FORWARD           139 (to L17)

211   L11:     LOAD_CONST              13 ('dump file exists')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L12)
               NOT_TAKEN

212            LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               14 (CRITICAL)
               STORE_FAST               7 (sev)

213            LOAD_CONST              14 ('Backup dump file missing')
               STORE_FAST               8 (title)
               JUMP_FORWARD           113 (to L17)

214   L12:     LOAD_CONST              15 ('manifest')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L13)
               NOT_TAKEN

215            LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               16 (HIGH)
               STORE_FAST               7 (sev)

216            LOAD_CONST              16 ('Backup manifest unreadable or absent')
               STORE_FAST               8 (title)
               JUMP_FORWARD            87 (to L17)

217   L13:     LOAD_CONST              17 ('jsonl parses')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L14)
               NOT_TAKEN

218            LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               16 (HIGH)
               STORE_FAST               7 (sev)

219            LOAD_CONST              18 ('Event JSONL inside backup is malformed')
               STORE_FAST               8 (title)
               JUMP_FORWARD            61 (to L17)

220   L14:     LOAD_CONST              19 ('row count')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         8 (to L15)
               NOT_TAKEN
               LOAD_CONST              20 ('row_count')
               LOAD_FAST_BORROW         5 (name_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       20 (to L16)
               NOT_TAKEN

221   L15:     LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               16 (HIGH)
               STORE_FAST               7 (sev)

222            LOAD_CONST              21 ('Event row count does not match manifest')
               STORE_FAST               8 (title)
               JUMP_FORWARD            28 (to L17)

224   L16:     LOAD_GLOBAL             12 (Severity)
               LOAD_ATTR               16 (HIGH)
               STORE_FAST               7 (sev)

225            LOAD_CONST              22 ('Backup verification failed: ')
               LOAD_FAST_BORROW         4 (name)
               LOAD_CONST              23 (slice(None, 80, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               STORE_FAST               8 (title)

227   L17:     LOAD_GLOBAL             19 (_push + NULL)
               LOAD_FAST                1 (out)
               LOAD_GLOBAL             21 (_try_alert + NULL)

228            LOAD_CONST              24 ('backup_')
               LOAD_GLOBAL             23 (_safe_id_fragment + NULL)
               LOAD_FAST_BORROW         4 (name)
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2

229            LOAD_GLOBAL             24 (Category)
               LOAD_ATTR               26 (BACKUP)

230            LOAD_FAST                7 (sev)

231            LOAD_FAST                8 (title)

233            LOAD_FAST                6 (detail)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L18)
               NOT_TAKEN
               POP_TOP

234            LOAD_CONST              25 ('Re-run scripts/verify_backup.py --strict against this directory; do not rely on this backup until it passes.')

237   L18:     LOAD_GLOBAL             28 (_SOURCE)

238            LOAD_CONST              26 ('check_name')
               LOAD_FAST_BORROW         4 (name)
               BUILD_MAP                1

227            LOAD_CONST              27 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          426 (to L4)

196   L19:     END_FOR
               POP_ITER

240            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\monitoring\detectors.py", line 256>:
256           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_event_ingestion_health at 0x0000018C17D8AB60, file "app\services\monitoring\detectors.py", line 256>:
 256            RESUME                   0

 262            BUILD_LIST               0
                STORE_FAST               1 (out)

 263            LOAD_FAST_BORROW         0 (events)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 264            BUILD_LIST               0
                STORE_FAST               0 (events)

 265    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (events)
                LOAD_GLOBAL              2 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN

 266            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 268    L2:     LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         0 (events)
                CALL                     1
                STORE_FAST               2 (n)

 271            LOAD_FAST_BORROW         2 (n)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       65 (to L3)
                NOT_TAKEN

 272            LOAD_GLOBAL              7 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL              9 (_try_alert + NULL)

 273            LOAD_CONST               1 ('ingestion_empty_window')

 274            LOAD_GLOBAL             10 (Category)
                LOAD_ATTR               12 (INGESTION)

 275            LOAD_GLOBAL             14 (Severity)
                LOAD_ATTR               16 (HIGH)

 276            LOAD_CONST               2 ('No pas_events in inspected window')

 278            LOAD_CONST               3 ('The event stream is empty. Investigate Supabase reachability, service-role key validity, or a stalled engine.')

 281            LOAD_GLOBAL             18 (_SOURCE)

 282            LOAD_CONST               4 ('event_count')
                LOAD_SMALL_INT           0
                BUILD_MAP                1

 272            LOAD_CONST               5 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 284            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 287    L3:     LOAD_FAST_BORROW         2 (n)
                LOAD_GLOBAL             20 (_EVENT_VOLUME_SPIKE)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       67 (to L4)
                NOT_TAKEN

 288            LOAD_GLOBAL              7 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL              9 (_try_alert + NULL)

 289            LOAD_CONST               6 ('ingestion_volume_spike')

 290            LOAD_GLOBAL             10 (Category)
                LOAD_ATTR               12 (INGESTION)

 291            LOAD_GLOBAL             14 (Severity)
                LOAD_ATTR               22 (MEDIUM)

 292            LOAD_CONST               7 ('Event volume spike: ')
                LOAD_FAST_BORROW         2 (n)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' events in window')
                BUILD_STRING             3

 294            LOAD_CONST               9 ('Investigate which event_type dominates the window — usually indicates a misconfigured loop or an over-emitting feature.')

 297            LOAD_GLOBAL             18 (_SOURCE)

 298            LOAD_CONST               4 ('event_count')
                LOAD_FAST_BORROW         2 (n)
                BUILD_MAP                1

 288            LOAD_CONST               5 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 302    L4:     LOAD_GLOBAL             25 (sum + NULL)
                LOAD_CONST              10 (<code object <genexpr> at 0x0000018C18010B30, file "app\services\monitoring\detectors.py", line 302>)
                MAKE_FUNCTION

 303            LOAD_FAST_BORROW         0 (events)
                GET_ITER

 302            CALL                     0
                CALL                     1
                STORE_FAST               3 (provider_fails)

 306            LOAD_FAST_BORROW         3 (provider_fails)
                LOAD_GLOBAL             26 (_PROVIDER_FAILURE_SPIKE)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       67 (to L5)
                NOT_TAKEN

 307            LOAD_GLOBAL              7 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL              9 (_try_alert + NULL)

 308            LOAD_CONST              11 ('ingestion_provider_failure_spike')

 309            LOAD_GLOBAL             10 (Category)
                LOAD_ATTR               12 (INGESTION)

 310            LOAD_GLOBAL             14 (Severity)
                LOAD_ATTR               16 (HIGH)

 311            LOAD_CONST              12 ('Provider failure spike: ')
                LOAD_FAST_BORROW         3 (provider_fails)
                FORMAT_SIMPLE
                LOAD_CONST              13 (' provider.failed events')
                BUILD_STRING             3

 313            LOAD_CONST              14 ('Investigate provider outage or API-key failure. Likely culprits: Anthropic / OpenAI / Twilio / Deepgram / Cal.com.')

 316            LOAD_GLOBAL             18 (_SOURCE)

 317            LOAD_CONST              15 ('provider_failed_count')
                LOAD_FAST_BORROW         3 (provider_fails)
                BUILD_MAP                1

 307            LOAD_CONST               5 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 321    L5:     BUILD_MAP                0
                STORE_FAST               4 (seen)

 322            BUILD_LIST               0
                STORE_FAST               5 (duplicates)

 323            LOAD_FAST_BORROW         0 (events)
                GET_ITER
        L6:     FOR_ITER                90 (to L10)
                STORE_FAST               6 (e)

 324            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (e)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN

 325            JUMP_BACKWARD           27 (to L6)

 326    L7:     LOAD_FAST_BORROW         6 (e)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              16 ('event_id')
                CALL                     1
                STORE_FAST               7 (eid)

 327            LOAD_FAST_BORROW         7 (eid)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           54 (to L6)

 328    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (eid, seen)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       27 (to L9)
                NOT_TAKEN

 329            LOAD_FAST_BORROW         5 (duplicates)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_GLOBAL             35 (str + NULL)
                LOAD_FAST_BORROW         7 (eid)
                CALL                     1
                CALL                     1
                POP_TOP

 330    L9:     LOAD_CONST              17 (True)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (seen, eid)
                STORE_SUBSCR
                JUMP_BACKWARD           92 (to L6)

 323   L10:     END_FOR
                POP_ITER

 331            LOAD_FAST_BORROW         5 (duplicates)
                TO_BOOL
                POP_JUMP_IF_FALSE       85 (to L11)
                NOT_TAKEN

 332            LOAD_GLOBAL              7 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL              9 (_try_alert + NULL)

 333            LOAD_CONST              18 ('ingestion_duplicate_event_ids')

 334            LOAD_GLOBAL             10 (Category)
                LOAD_ATTR               12 (INGESTION)

 335            LOAD_GLOBAL             14 (Severity)
                LOAD_ATTR               16 (HIGH)

 336            LOAD_CONST              19 ('Duplicate event_ids detected (')
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         5 (duplicates)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              20 (')')
                BUILD_STRING             3

 338            LOAD_CONST              21 ('Possible double-write or replay corruption. Confirm the UNIQUE INDEX on pas_events.event_id is in place.')

 341            LOAD_GLOBAL             18 (_SOURCE)

 342            LOAD_CONST              22 ('duplicate_count')
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         5 (duplicates)
                CALL                     1
                BUILD_MAP                1

 332            LOAD_CONST               5 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 348   L11:     BUILD_MAP                0
                STORE_FAST               8 (by_call)

 349            LOAD_FAST_BORROW         0 (events)
                GET_ITER
       L12:     FOR_ITER               110 (to L15)
                STORE_FAST               6 (e)

 350            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (e)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

 351            JUMP_BACKWARD           27 (to L12)

 352   L13:     LOAD_FAST_BORROW         6 (e)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              23 ('call_id')
                CALL                     1
                STORE_FAST               9 (cid)

 353            LOAD_FAST_BORROW         9 (cid)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           54 (to L12)

 354   L14:     LOAD_FAST_BORROW         8 (by_call)
                LOAD_ATTR               37 (setdefault + NULL|self)
                LOAD_FAST_BORROW         9 (cid)
                LOAD_GLOBAL             39 (set + NULL)
                CALL                     0
                CALL                     2
                LOAD_ATTR               41 (add + NULL|self)
                LOAD_FAST_BORROW         6 (e)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              24 ('event_type')
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          112 (to L12)

 349   L15:     END_FOR
                POP_ITER

 356            LOAD_FAST_BORROW         8 (by_call)
                LOAD_ATTR               43 (items + NULL|self)
                CALL                     0
                GET_ITER

 355            LOAD_FAST_AND_CLEAR      9 (cid)
                LOAD_FAST_AND_CLEAR     10 (types)
                SWAP                     3
       L16:     BUILD_LIST               0
                SWAP                     2

 356   L17:     FOR_ITER                35 (to L22)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  154 (cid, types)

 357            LOAD_CONST              25 ('call.ended')
                LOAD_FAST_BORROW        10 (types)
                CONTAINS_OP              0 (in)

 356   L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           14 (to L17)

 358   L19:     LOAD_FAST_BORROW        10 (types)
                LOAD_CONST              26 ('lead.uttered')
                LOAD_CONST              27 ('pas.uttered')
                BUILD_SET                2
                BINARY_OP                1 (&)
                TO_BOOL

 356   L20:     POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           33 (to L17)
       L21:     LOAD_FAST_BORROW         9 (cid)
                LIST_APPEND              2
                JUMP_BACKWARD           37 (to L17)
       L22:     END_FOR
                POP_ITER

 355   L23:     STORE_FAST              11 (calls_missing_turns)
                STORE_FAST               9 (cid)
                STORE_FAST              10 (types)

 360            LOAD_FAST_BORROW        11 (calls_missing_turns)
                TO_BOOL
                POP_JUMP_IF_FALSE       84 (to L24)
                NOT_TAKEN

 361            LOAD_GLOBAL              7 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL              9 (_try_alert + NULL)

 362            LOAD_CONST              28 ('ingestion_missing_turn_events')

 363            LOAD_GLOBAL             10 (Category)
                LOAD_ATTR               12 (INGESTION)

 364            LOAD_GLOBAL             14 (Severity)
                LOAD_ATTR               22 (MEDIUM)

 365            LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW        11 (calls_missing_turns)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              29 (' completed call(s) lack turn events')
                BUILD_STRING             2

 367            LOAD_CONST              30 ('Calls completed without lead.uttered / pas.uttered rows. PAS_EVENT_TURN_LOGGING may be off or a write path is dropping turns.')

 370            LOAD_GLOBAL             18 (_SOURCE)

 371            LOAD_CONST              31 ('affected_calls')
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW        11 (calls_missing_turns)
                CALL                     1
                BUILD_MAP                1

 361            LOAD_CONST               5 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 374   L24:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L25:     SWAP                     2
                POP_TOP

 355            SWAP                     3
                STORE_FAST              10 (types)
                STORE_FAST               9 (cid)
                RERAISE                  0
ExceptionTable:
  L16 to L18 -> L25 [3]
  L19 to L20 -> L25 [3]
  L21 to L23 -> L25 [3]

Disassembly of <code object <genexpr> at 0x0000018C18010B30, file "app\services\monitoring\detectors.py", line 302>:
 302           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 303   L2:     FOR_ITER                55 (to L7)
               STORE_FAST               1 (e)

 304           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (e)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL

 303   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)

 304   L4:     LOAD_FAST_BORROW         1 (e)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               0 ('event_type')
               CALL                     1
               LOAD_CONST               1 ('provider.failed')
               COMPARE_OP              88 (bool(==))

 303   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           51 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           57 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\monitoring\detectors.py", line 381>:
381           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('error_or_event')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_tenant_scope_violation at 0x0000018C17D8BE60, file "app\services\monitoring\detectors.py", line 381>:
381            RESUME                   0

394            BUILD_LIST               0
               STORE_FAST               1 (out)

395            LOAD_FAST_BORROW         0 (error_or_event)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

396            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

398    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_GLOBAL              2 (TenantScopingError)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       83 (to L2)
               NOT_TAKEN

399            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               CALL                     1
               STORE_FAST               2 (msg)

400            LOAD_GLOBAL              7 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL              9 (_try_alert + NULL)

401            LOAD_CONST               2 ('tenant_scoping_error')

402            LOAD_GLOBAL             10 (Category)
               LOAD_ATTR               12 (TENANT_ISOLATION)

403            LOAD_GLOBAL             14 (Severity)
               LOAD_ATTR               16 (CRITICAL)

404            LOAD_CONST               3 ('Tenant scoping violation: TenantScopingError raised')

405            LOAD_FAST_BORROW         2 (msg)
               LOAD_CONST               4 (slice(None, 500, None))
               BINARY_OP               26 ([])

406            LOAD_GLOBAL             18 (_SOURCE)

407            LOAD_CONST               5 ('error_class')
               LOAD_CONST               6 ('TenantScopingError')
               BUILD_MAP                1

400            LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

409            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

411    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_GLOBAL             20 (BaseException)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      132 (to L5)
               NOT_TAKEN

412            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               CALL                     1
               STORE_FAST               2 (msg)

413            LOAD_FAST_BORROW         2 (msg)
               LOAD_ATTR               23 (lower + NULL|self)
               CALL                     0
               STORE_FAST               3 (m_l)

414            LOAD_CONST               8 ('brokerage')
               LOAD_FAST_BORROW         3 (m_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         8 (to L3)
               NOT_TAKEN
               LOAD_CONST               9 ('tenant')
               LOAD_FAST_BORROW         3 (m_l)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       89 (to L4)
               NOT_TAKEN

415    L3:     LOAD_GLOBAL              7 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL              9 (_try_alert + NULL)

416            LOAD_CONST              10 ('tenant_unknown_exception')

417            LOAD_GLOBAL             10 (Category)
               LOAD_ATTR               12 (TENANT_ISOLATION)

418            LOAD_GLOBAL             14 (Severity)
               LOAD_ATTR               16 (CRITICAL)

419            LOAD_CONST              11 ('Tenant-related exception raised')

420            LOAD_FAST_BORROW         2 (msg)
               LOAD_CONST               4 (slice(None, 500, None))
               BINARY_OP               26 ([])

421            LOAD_GLOBAL             18 (_SOURCE)

422            LOAD_CONST               5 ('error_class')
               LOAD_GLOBAL             25 (type + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               CALL                     1
               LOAD_ATTR               26 (__name__)
               BUILD_MAP                1

415            LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

424    L4:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

426    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_GLOBAL             28 (dict)
               CALL                     2
               TO_BOOL
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      363 (to L15)
               NOT_TAKEN

427            LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               31 (get + NULL|self)
               LOAD_CONST              12 ('context')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('')
       L6:     LOAD_ATTR               23 (lower + NULL|self)
               CALL                     0
               STORE_FAST               4 (ctx)

428            LOAD_GLOBAL             33 (bool + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               31 (get + NULL|self)
               LOAD_CONST              14 ('unscoped')
               CALL                     1
               CALL                     1
               STORE_FAST               5 (unscoped)

429            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               31 (get + NULL|self)
               LOAD_CONST              15 ('message')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              13 ('')
       L7:     CALL                     1
               STORE_FAST               2 (msg)

430            LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               31 (get + NULL|self)
               LOAD_CONST              16 ('brokerage_id')
               CALL                     1
               STORE_FAST               6 (bid)

432            LOAD_FAST_BORROW         4 (ctx)
               LOAD_CONST              17 ('portal')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       98 (to L10)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (unscoped)
               TO_BOOL
               POP_JUMP_IF_FALSE       90 (to L10)
               NOT_TAKEN

435            LOAD_GLOBAL              7 (_push + NULL)
               LOAD_FAST                1 (out)
               LOAD_GLOBAL              9 (_try_alert + NULL)

436            LOAD_CONST              18 ('tenant_unscoped_in_portal')

437            LOAD_GLOBAL             10 (Category)
               LOAD_ATTR               12 (TENANT_ISOLATION)

438            LOAD_GLOBAL             14 (Severity)
               LOAD_ATTR               16 (CRITICAL)

439            LOAD_CONST              19 ('Unscoped read attempted in portal context')

441            LOAD_CONST              20 ('A portal-context call attempted an unscoped data access. Stop tenant memory writes immediately and investigate the call site.')

445            LOAD_GLOBAL             18 (_SOURCE)

446            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (bid)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_FAST                6 (bid)
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               1 (None)

447    L9:     LOAD_CONST              12 ('context')
               LOAD_FAST_BORROW         4 (ctx)
               BUILD_MAP                1

435            LOAD_CONST              21 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
               CALL_KW                  8
               CALL                     2
               POP_TOP

449            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

451   L10:     LOAD_FAST_BORROW         2 (msg)
               TO_BOOL
               POP_JUMP_IF_FALSE      129 (to L14)
               NOT_TAKEN

452            LOAD_GLOBAL              7 (_push + NULL)
               LOAD_FAST                1 (out)
               LOAD_GLOBAL              9 (_try_alert + NULL)

453            LOAD_CONST              22 ('tenant_scoping_dict')

454            LOAD_GLOBAL             10 (Category)
               LOAD_ATTR               12 (TENANT_ISOLATION)

455            LOAD_GLOBAL             14 (Severity)
               LOAD_ATTR               16 (CRITICAL)

456            LOAD_CONST              23 ('Tenant scoping signal received')

457            LOAD_FAST_BORROW         2 (msg)
               LOAD_CONST               4 (slice(None, 500, None))
               BINARY_OP               26 ([])

458            LOAD_GLOBAL              5 (str + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               31 (get + NULL|self)
               LOAD_CONST              24 ('source')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         7 (to L11)
               NOT_TAKEN
               POP_TOP
               LOAD_GLOBAL             18 (_SOURCE)
      L11:     CALL                     1

459            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (bid)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_FAST                6 (bid)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               1 (None)

460   L13:     LOAD_CONST              12 ('context')
               LOAD_FAST_BORROW         4 (ctx)
               BUILD_MAP                1

452            LOAD_CONST              21 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
               CALL_KW                  8
               CALL                     2
               POP_TOP

462   L14:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

464   L15:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       90 (to L16)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_ATTR               35 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       68 (to L16)
               NOT_TAKEN

465            LOAD_GLOBAL              7 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL              9 (_try_alert + NULL)

466            LOAD_CONST              25 ('tenant_scoping_message')

467            LOAD_GLOBAL             10 (Category)
               LOAD_ATTR               12 (TENANT_ISOLATION)

468            LOAD_GLOBAL             14 (Severity)
               LOAD_ATTR               16 (CRITICAL)

469            LOAD_CONST              23 ('Tenant scoping signal received')

470            LOAD_FAST_BORROW         0 (error_or_event)
               LOAD_CONST               4 (slice(None, 500, None))
               BINARY_OP               26 ([])

471            LOAD_GLOBAL             18 (_SOURCE)

472            BUILD_MAP                0

465            LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

474   L16:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\monitoring\detectors.py", line 486>:
486           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('replay_or_reconstruction')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_replay_quality at 0x0000018C17D81A00, file "app\services\monitoring\detectors.py", line 486>:
486           RESUME                   0

492           BUILD_LIST               0
              STORE_FAST               1 (out)

493           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (replay_or_reconstruction)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

494           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

495   L1:     LOAD_FAST                0 (replay_or_reconstruction)
              STORE_FAST               2 (r)

498           LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('replay_score')
              CALL                     1
              STORE_FAST               3 (score)

499           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (score)
              LOAD_GLOBAL              6 (int)
              LOAD_GLOBAL              8 (float)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       81 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (score)
              LOAD_SMALL_INT           0
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE         8 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (score)
              LOAD_SMALL_INT         100
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       67 (to L3)
              NOT_TAKEN

500   L2:     LOAD_GLOBAL             11 (_push + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_GLOBAL             13 (_try_alert + NULL)

501           LOAD_CONST               2 ('replay_score_out_of_range')

502           LOAD_GLOBAL             14 (Category)
              LOAD_ATTR               16 (REPLAY)

503           LOAD_GLOBAL             18 (Severity)
              LOAD_ATTR               20 (HIGH)

504           LOAD_CONST               3 ('Replay score ')
              LOAD_FAST_BORROW         3 (score)
              FORMAT_SIMPLE
              LOAD_CONST               4 (' outside [0, 100]')
              BUILD_STRING             3

506           LOAD_CONST               5 ('The evaluator returned an out-of-range score. Likely a bug in evaluate_reconstruction or corrupted reconstruction input.')

509           LOAD_GLOBAL             22 (_SOURCE)

510           LOAD_CONST               6 ('score')
              LOAD_FAST_BORROW         3 (score)
              BUILD_MAP                1

500           LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
              CALL_KW                  7
              CALL                     2
              POP_TOP

515   L3:     LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               8 ('is_replayable')
              CALL                     1
              STORE_FAST               4 (is_replayable)

516           LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               9 ('final_outcome')
              CALL                     1
              STORE_FAST               5 (final_outcome)

517           LOAD_FAST_BORROW         4 (is_replayable)
              LOAD_CONST              10 (False)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       78 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         5 (final_outcome)
              LOAD_GLOBAL             24 (_TERMINAL_OUTCOMES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       67 (to L4)
              NOT_TAKEN

518           LOAD_GLOBAL             11 (_push + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_GLOBAL             13 (_try_alert + NULL)

519           LOAD_CONST              11 ('replay_unreplayable_terminal')

520           LOAD_GLOBAL             14 (Category)
              LOAD_ATTR               16 (REPLAY)

521           LOAD_GLOBAL             18 (Severity)
              LOAD_ATTR               26 (MEDIUM)

522           LOAD_CONST              12 ("Call had terminal outcome '")
              LOAD_FAST_BORROW         5 (final_outcome)
              FORMAT_SIMPLE
              LOAD_CONST              13 ("' but is not replayable")
              BUILD_STRING             3

524           LOAD_CONST              14 ("Lifecycle gaps prevent reconstruction. Audit the call's event stream — usually means lead.uttered / pas.uttered rows are missing.")

527           LOAD_GLOBAL             22 (_SOURCE)

528           LOAD_CONST              15 ('outcome')
              LOAD_FAST_BORROW         5 (final_outcome)
              BUILD_MAP                1

518           LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
              CALL_KW                  7
              CALL                     2
              POP_TOP

532   L4:     LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              16 ('missing_steps')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        28 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST              17 ('missing_lifecycle_steps')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     STORE_FAST               6 (missing)

533           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         6 (missing)
              LOAD_GLOBAL             28 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       77 (to L6)
              NOT_TAKEN
              LOAD_CONST              18 ('completed')
              LOAD_FAST_BORROW         6 (missing)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       70 (to L6)
              NOT_TAKEN

534           LOAD_GLOBAL             11 (_push + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_GLOBAL             13 (_try_alert + NULL)

535           LOAD_CONST              19 ('replay_missing_completed_step')

536           LOAD_GLOBAL             14 (Category)
              LOAD_ATTR               16 (REPLAY)

537           LOAD_GLOBAL             18 (Severity)
              LOAD_ATTR               26 (MEDIUM)

538           LOAD_CONST              20 ("Reconstruction missing 'completed' step")

540           LOAD_CONST              21 ('No terminal event (call.ended / call.ended_with_callback / call.failed) was found in the event stream. Operators should audit recent calls for missing terminal events.')

544           LOAD_GLOBAL             22 (_SOURCE)

545           LOAD_CONST              16 ('missing_steps')
              LOAD_FAST_BORROW         6 (missing)
              LOAD_CONST              22 (slice(None, 10, None))
              BINARY_OP               26 ([])
              BUILD_MAP                1

534           LOAD_CONST               7 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
              CALL_KW                  7
              CALL                     2
              POP_TOP

547   L6:     LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\monitoring\detectors.py", line 561>:
561           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('restore_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_restore_drill_failures at 0x0000018C17F7D8D0, file "app\services\monitoring\detectors.py", line 561>:
561            RESUME                   0

571            BUILD_LIST               0
               STORE_FAST               1 (out)

572            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (restore_report)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

573            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

575    L1:     LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('restore_success')
               CALL                     1
               LOAD_CONST               2 (False)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE      179 (to L5)
               NOT_TAKEN

578            LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('failures')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L2:     STORE_FAST               2 (fails)

579            LOAD_CONST               4 ('; ')
               LOAD_ATTR                7 (join + NULL|self)
               LOAD_CONST               5 (<code object <genexpr> at 0x0000018C180531B0, file "app\services\monitoring\detectors.py", line 579>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         2 (fails)
               LOAD_CONST               6 (slice(None, 3, None))
               BINARY_OP               26 ([])
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               3 (summary)

580            LOAD_GLOBAL              9 (_push + NULL)
               LOAD_FAST                1 (out)
               LOAD_GLOBAL             11 (_try_alert + NULL)

581            LOAD_CONST               7 ('backup_restore_drill_failed')

582            LOAD_GLOBAL             12 (Category)
               LOAD_ATTR               14 (BACKUP)

583            LOAD_GLOBAL             16 (Severity)
               LOAD_ATTR               18 (CRITICAL)

584            LOAD_CONST               8 ('Restore drill failed')

586            LOAD_CONST               9 ('The drill could not reconstruct the backup. Investigate the failure list before relying on this archive for production restore. Summary: ')

588            LOAD_FAST                3 (summary)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              10 ('see restore_drill_report.json')
       L3:     FORMAT_SIMPLE

586            BUILD_STRING             2

590            LOAD_GLOBAL             20 (_SOURCE)

592            LOAD_CONST              11 ('archive')
               LOAD_GLOBAL             23 (str + NULL)
               LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('archive')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              12 ('')
       L4:     CALL                     1

593            LOAD_CONST              13 ('failure_count')
               LOAD_GLOBAL             25 (len + NULL)
               LOAD_FAST_BORROW         2 (fails)
               CALL                     1

591            BUILD_MAP                2

580            LOAD_CONST              14 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

597    L5:     LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('integrity_status')
               CALL                     1
               STORE_FAST               4 (integrity)

598            LOAD_FAST_BORROW         4 (integrity)
               LOAD_CONST              32 ((None, 'skipped', 'pass'))
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       63 (to L6)
               NOT_TAKEN

599            LOAD_GLOBAL              9 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL             11 (_try_alert + NULL)

600            LOAD_CONST              17 ('backup_restore_drill_integrity_fail')

601            LOAD_GLOBAL             12 (Category)
               LOAD_ATTR               14 (BACKUP)

602            LOAD_GLOBAL             16 (Severity)
               LOAD_ATTR               26 (HIGH)

603            LOAD_CONST              18 ('Integrity check failed during restore drill')

605            LOAD_CONST              19 ('The restored backup did not pass the integrity check. The archive may be from a substrate version that has since drifted; treat the backup as suspect until investigated.')

609            LOAD_GLOBAL             20 (_SOURCE)

610            LOAD_CONST              15 ('integrity_status')
               LOAD_FAST_BORROW         4 (integrity)
               BUILD_MAP                1

599            LOAD_CONST              14 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

613    L6:     LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              20 ('monitoring_status')
               CALL                     1
               STORE_FAST               5 (monitoring)

614            LOAD_FAST_BORROW         5 (monitoring)
               LOAD_CONST              32 ((None, 'skipped', 'pass'))
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       63 (to L7)
               NOT_TAKEN

615            LOAD_GLOBAL              9 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL             11 (_try_alert + NULL)

616            LOAD_CONST              21 ('backup_restore_drill_monitoring_fail')

617            LOAD_GLOBAL             12 (Category)
               LOAD_ATTR               14 (BACKUP)

618            LOAD_GLOBAL             16 (Severity)
               LOAD_ATTR               26 (HIGH)

619            LOAD_CONST              22 ('Monitoring check failed during restore drill')

621            LOAD_CONST              23 ('Running the monitoring check inside the drill workspace produced HIGH/CRITICAL alerts. The backup itself may be fine, but the substrate that produced it had open issues.')

625            LOAD_GLOBAL             20 (_SOURCE)

626            LOAD_CONST              20 ('monitoring_status')
               LOAD_FAST_BORROW         5 (monitoring)
               BUILD_MAP                1

615            LOAD_CONST              14 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

629    L7:     LOAD_FAST_BORROW         0 (restore_report)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              24 ('durations')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L8:     STORE_FAST               6 (durations)

630            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (durations)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (durations)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              25 ('total_s')
               CALL                     1
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              16 (None)
      L10:     STORE_FAST               7 (total_s)

631            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (total_s)
               LOAD_GLOBAL             28 (int)
               LOAD_GLOBAL             30 (float)
               BUILD_TUPLE              2
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       85 (to L11)
               NOT_TAKEN
               LOAD_FAST_BORROW         7 (total_s)
               LOAD_GLOBAL             32 (_RESTORE_DRILL_SLOW_S)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       74 (to L11)
               NOT_TAKEN

632            LOAD_GLOBAL              9 (_push + NULL)
               LOAD_FAST_BORROW         1 (out)
               LOAD_GLOBAL             11 (_try_alert + NULL)

633            LOAD_CONST              26 ('backup_restore_drill_slow')

634            LOAD_GLOBAL             12 (Category)
               LOAD_ATTR               14 (BACKUP)

635            LOAD_GLOBAL             16 (Severity)
               LOAD_ATTR               34 (MEDIUM)

636            LOAD_CONST              27 ('Restore drill ran slowly (')
               LOAD_FAST_BORROW         7 (total_s)
               LOAD_CONST              28 ('.1f')
               FORMAT_WITH_SPEC
               LOAD_CONST              29 ('s)')
               BUILD_STRING             3

638            LOAD_CONST              30 ('Drill exceeded the comfort threshold. Right-size the backup, prune historic dumps, or move the workspace to faster storage.')

642            LOAD_GLOBAL             20 (_SOURCE)

643            LOAD_CONST              25 ('total_s')
               LOAD_FAST_BORROW         7 (total_s)
               LOAD_CONST              31 ('threshold_s')
               LOAD_GLOBAL             32 (_RESTORE_DRILL_SLOW_S)
               BUILD_MAP                2

632            LOAD_CONST              14 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
               CALL_KW                  7
               CALL                     2
               POP_TOP

646   L11:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "app\services\monitoring\detectors.py", line 579>:
 579           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                23 (to L3)
               STORE_FAST               1 (f)
               LOAD_GLOBAL              1 (str + NULL)
               LOAD_FAST_BORROW         1 (f)
               CALL                     1
               LOAD_CONST               0 (slice(None, 120, None))
               BINARY_OP               26 ([])
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           25 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\monitoring\detectors.py", line 653>:
653           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('optimization_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object detect_optimization_health at 0x0000018C17E04B30, file "app\services\monitoring\detectors.py", line 653>:
  --            MAKE_CELL               11 (head)

 653            RESUME                   0

 657            BUILD_LIST               0
                STORE_FAST               1 (out)

 658            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (optimization_report)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 659            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 661    L1:     LOAD_FAST_BORROW         0 (optimization_report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('metrics')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L2:     STORE_FAST               2 (metrics)

 662            LOAD_FAST_BORROW         0 (optimization_report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('ranked_strategies')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L3:     STORE_FAST               3 (ranked)

 665            BUILD_LIST               0
                STORE_FAST               4 (bad_keys)

 666            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (metrics)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       82 (to L8)
                NOT_TAKEN

 667            LOAD_FAST_BORROW         2 (metrics)
                LOAD_ATTR                7 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                61 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (k, v)

 668            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (v)
                LOAD_GLOBAL              8 (int)
                LOAD_GLOBAL             10 (float)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           35 (to L4)
        L5:     LOAD_FAST_BORROW         6 (v)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           44 (to L4)

 669    L6:     LOAD_FAST_BORROW         4 (bad_keys)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         5 (k)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           63 (to L4)

 667    L7:     END_FOR
                POP_ITER

 670    L8:     LOAD_FAST_BORROW         4 (bad_keys)
                TO_BOOL
                POP_JUMP_IF_FALSE       82 (to L9)
                NOT_TAKEN

 671            LOAD_GLOBAL             15 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL             17 (_try_alert + NULL)

 672            LOAD_CONST               3 ('optimization_negative_metrics')

 673            LOAD_GLOBAL             18 (Category)
                LOAD_ATTR               20 (OPTIMIZATION)

 674            LOAD_GLOBAL             22 (Severity)
                LOAD_ATTR               24 (HIGH)

 675            LOAD_CONST               4 ('Negative aggregate metric value(s): ')
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         4 (bad_keys)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2

 677            LOAD_CONST               5 ('Aggregation bug — every metric in compute_matrix_metrics should be non-negative.')

 680            LOAD_GLOBAL             28 (_SOURCE)

 681            LOAD_CONST               6 ('negative_keys')
                LOAD_FAST_BORROW         4 (bad_keys)
                LOAD_CONST               7 (slice(None, 10, None))
                BINARY_OP               26 ([])
                BUILD_MAP                1

 671            LOAD_CONST               8 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 685    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (metrics)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (metrics)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               9 ('total_runs')
                CALL                     1
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_SMALL_INT           0
       L11:     COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L12:     STORE_FAST               7 (total_runs)

 686            LOAD_FAST_BORROW         7 (total_runs)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       63 (to L13)
                NOT_TAKEN

 687            LOAD_GLOBAL             15 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL             17 (_try_alert + NULL)

 688            LOAD_CONST              10 ('optimization_empty_matrix')

 689            LOAD_GLOBAL             18 (Category)
                LOAD_ATTR               20 (OPTIMIZATION)

 690            LOAD_GLOBAL             22 (Severity)
                LOAD_ATTR               30 (MEDIUM)

 691            LOAD_CONST              11 ('Optimization matrix is empty (no runs)')

 693            LOAD_CONST              12 ('No cells in the matrix — check the scenario/strategy filters or registry contents.')

 696            LOAD_GLOBAL             28 (_SOURCE)

 697            LOAD_CONST               9 ('total_runs')
                LOAD_SMALL_INT           0
                BUILD_MAP                1

 687            LOAD_CONST               8 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 701   L13:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (ranked)
                LOAD_GLOBAL             32 (list)
                CALL                     2
                TO_BOOL
                EXTENDED_ARG             2
                POP_JUMP_IF_FALSE      513 (to L31)
                NOT_TAKEN
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         3 (ranked)
                CALL                     1
                LOAD_SMALL_INT           2
                COMPARE_OP             188 (bool(>=))
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      496 (to L31)
                NOT_TAKEN

 702            BUILD_LIST               0
                STORE_FAST               8 (scores)

 703            LOAD_FAST_BORROW         3 (ranked)
                GET_ITER
       L14:     FOR_ITER               120 (to L16)
                STORE_FAST               9 (r)

 704            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (r)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       79 (to L15)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         9 (r)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              13 ('score')
                CALL                     1
                LOAD_GLOBAL              8 (int)
                LOAD_GLOBAL             10 (float)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L15)
                NOT_TAKEN

 705            LOAD_FAST_BORROW         8 (scores)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_GLOBAL             11 (float + NULL)
                LOAD_FAST_BORROW         9 (r)
                LOAD_CONST              13 ('score')
                BINARY_OP               26 ([])
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          103 (to L14)

 707   L15:     LOAD_FAST_BORROW         8 (scores)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_CONST              14 (None)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          122 (to L14)

 703   L16:     END_FOR
                POP_ITER

 708            LOAD_GLOBAL             34 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L20)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              15 (<code object <genexpr> at 0x0000018C18025130, file "app\services\monitoring\detectors.py", line 708>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (scores)
                GET_ITER
                CALL                     0
       L17:     FOR_ITER                12 (to L19)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L17)
       L18:     POP_ITER
                LOAD_CONST              16 (False)
                JUMP_FORWARD            17 (to L21)
       L19:     END_FOR
                POP_ITER
                LOAD_CONST              17 (True)
                JUMP_FORWARD            13 (to L21)
       L20:     PUSH_NULL
                LOAD_CONST              15 (<code object <genexpr> at 0x0000018C18025130, file "app\services\monitoring\detectors.py", line 708>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         8 (scores)
                GET_ITER
                CALL                     0
                CALL                     1
       L21:     TO_BOOL
                POP_JUMP_IF_FALSE      139 (to L25)
                NOT_TAKEN

 709            LOAD_GLOBAL             37 (range + NULL)
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         8 (scores)
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                CALL                     1
                GET_ITER
       L22:     FOR_ITER               107 (to L24)
                STORE_FAST              10 (i)

 710            LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (scores, i)
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (scores, i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                BINARY_OP               26 ([])
                LOAD_CONST              18 (1e-09)
                BINARY_OP               10 (-)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           38 (to L22)

 711   L23:     LOAD_GLOBAL             15 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL             17 (_try_alert + NULL)

 712            LOAD_CONST              19 ('optimization_ranking_invalid')

 713            LOAD_GLOBAL             18 (Category)
                LOAD_ATTR               20 (OPTIMIZATION)

 714            LOAD_GLOBAL             22 (Severity)
                LOAD_ATTR               24 (HIGH)

 715            LOAD_CONST              20 ('Strategy ranking not monotonically descending')

 717            LOAD_CONST              21 ('rank_strategies returned scores out of order — investigate the sort key.')

 720            LOAD_GLOBAL             28 (_SOURCE)

 721            LOAD_CONST              22 ('first_5_scores')
                LOAD_FAST_BORROW         8 (scores)
                LOAD_CONST              23 (slice(None, 5, None))
                BINARY_OP               26 ([])
                BUILD_MAP                1

 711            LOAD_CONST               8 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 723            POP_TOP
                JUMP_FORWARD             2 (to L25)

 709   L24:     END_FOR
                POP_ITER

 726   L25:     LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         3 (ranked)
                CALL                     1
                LOAD_SMALL_INT           3
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE      156 (to L31)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (scores)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                POP_JUMP_IF_NONE       145 (to L31)
                NOT_TAKEN

 727            LOAD_FAST_BORROW         8 (scores)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_DEREF             11 (head)

 728            LOAD_GLOBAL             34 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L29)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (head)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18038CB0, file "app\services\monitoring\detectors.py", line 728>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (scores)
                GET_ITER
                CALL                     0
       L26:     FOR_ITER                12 (to L28)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L27)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L26)
       L27:     POP_ITER
                LOAD_CONST              16 (False)
                JUMP_FORWARD            20 (to L30)
       L28:     END_FOR
                POP_ITER
                LOAD_CONST              17 (True)
                JUMP_FORWARD            16 (to L30)
       L29:     PUSH_NULL
                LOAD_FAST_BORROW        11 (head)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18038CB0, file "app\services\monitoring\detectors.py", line 728>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         8 (scores)
                GET_ITER
                CALL                     0
                CALL                     1
       L30:     TO_BOOL
                POP_JUMP_IF_FALSE       72 (to L31)
                NOT_TAKEN

 729            LOAD_GLOBAL             15 (_push + NULL)
                LOAD_FAST_BORROW         1 (out)
                LOAD_GLOBAL             17 (_try_alert + NULL)

 730            LOAD_CONST              25 ('optimization_all_strategies_tied')

 731            LOAD_GLOBAL             18 (Category)
                LOAD_ATTR               20 (OPTIMIZATION)

 732            LOAD_GLOBAL             22 (Severity)
                LOAD_ATTR               38 (LOW)

 733            LOAD_CONST              26 ('All strategies tied at top score')

 735            LOAD_CONST              27 ('Scenarios may not exercise the strategy axes. Add more scenarios that target distinct personalities.')

 738            LOAD_GLOBAL             28 (_SOURCE)

 739            LOAD_CONST              28 ('strategies_count')
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         3 (ranked)
                CALL                     1
                BUILD_MAP                1

 729            LOAD_CONST               8 (('id', 'category', 'severity', 'title', 'description', 'source', 'metadata'))
                CALL_KW                  7
                CALL                     2
                POP_TOP

 741   L31:     LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025130, file "app\services\monitoring\detectors.py", line 708>:
 708           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 8 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_CONST               0 (None)
               IS_OP                    1 (is not)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           10 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18038CB0, file "app\services\monitoring\detectors.py", line 728>:
  --           COPY_FREE_VARS           1

 728           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                36 (to L6)
               STORE_FAST               1 (s)
               LOAD_GLOBAL              1 (abs + NULL)
               LOAD_FAST                1 (s)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               LOAD_CONST               0 (0.0)
       L5:     LOAD_DEREF               2 (head)
               BINARY_OP               10 (-)
               CALL                     1
               LOAD_CONST               1 (1e-06)
               COMPARE_OP               2 (<)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           38 (to L2)
       L6:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti
```
