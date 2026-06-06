# monitoring/report

- **pyc:** `app\services\monitoring\__pycache__\report.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/report.py`
- **co_filename (from bytecode):** `app\services\monitoring\report.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS143F2 — Monitoring report aggregation.

Pure deterministic aggregation. Same input → same output. The report
is the operator-facing artefact: it tells a human what happened and
what to do next.

Doctrine:
  - safe_to_continue is False iff any CRITICAL alert is present.
  - recommended_actions are plain English. They reference categories,
    not file paths. The detail is in critical_alerts / high_alerts.
  - All alert payloads are passed through dispatcher.alert_to_safe_dict
    before being included so PII / secrets cannot leak.
```

## Imports

`Alert`, `Any`, `Category`, `Counter`, `Dict`, `List`, `SEVERITY_RANK`, `Severity`, `__future__`, `alert_to_safe_dict`, `annotations`, `app.services.monitoring.contracts`, `app.services.monitoring.dispatcher`, `collections`, `datetime`, `normalize_alert`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_normalize_all`, `_recommendations_for`, `generate_monitoring_report`, `summarize_monitoring_report`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143F2 — Monitoring report aggregation.\n\nPure deterministic aggregation. Same input → same output. The report\nis the operator-facing artefact: it tells a human what happened and\nwhat to do next.\n\nDoctrine:\n  - safe_to_continue is False iff any CRITICAL alert is present.\n  - recommended_actions are plain English. They reference categories,\n    not file paths. The detail is in critical_alerts / high_alerts.\n  - All alert payloads are passed through dispatcher.alert_to_safe_dict\n    before being included so PII / secrets cannot leak.\n'
- 'Stop tenant memory writes until the tenant-scope alert is resolved. Investigate the call site that attempted unscoped access.'
- 'Block deploys until CRITICAL security findings are remediated. Rotate any leaked credentials immediately.'
- 'Resolve HIGH security findings before persisting brain memory.'
- 'Restore from the last verified backup if checksum mismatch is confirmed. Re-run scripts/verify_backup.py --strict before trusting the next backup.'
- 'Re-take the affected backup and verify it before depending on it.'
- 'Re-run scripts/integrity_check.py --strict; investigate the failing case before accepting new event writes.'
- 'Audit the failing integrity check; widen test coverage for that path.'
- 'Investigate provider outage or API-key failure. Confirm Supabase service-role key + provider credentials are valid.'
- 'Check whether PAS_EVENT_TURN_LOGGING is on and the engine is emitting turn events for completed calls.'
- 'Pause replay-based optimization until the evaluator bug is fixed.'
- 'Audit recent calls for missing terminal events; re-run the replay/evaluator on a known-good call to confirm the substrate.'
- 'Pause matrix-based recommendations; investigate ranking + metrics.'
- 'Verify scenario / strategy registry filters before re-running.'
- 'Add scenarios that target distinct personalities so strategies differentiate.'
- 'Stop the engine pod and inspect runtime logs before re-enabling.'
- 'Investigate the runtime error; widen test coverage for that path.'
- 'Dict[tuple, str]'
- '_RECOMMENDATION_LIBRARY'
- 'alerts'
- 'List[Alert]'
- 'return'
- 'List[str]'
- '\nPick the right action sentence for each (category, severity) seen.\nDeduplicated, sorted by severity then category, then alphabetical.\n'
- 'Any'
- 'Coerce any iterable of Alerts/dicts into a list of valid Alerts.'
- 'Dict[str, Any]'
- '\nAggregate alerts into the operator-facing monitoring report.\n\nReturns the JSON-safe shape:\n  {\n    "tool":                "pas143f2.monitoring",\n    "generated_at":        ISO timestamp,\n    "total_alerts":        int,\n    "by_severity":         {sev: count},\n    "by_category":         {cat: count},\n    "critical_alerts":     [safe_alert_dict, ...],\n    "high_alerts":         [safe_alert_dict, ...],\n    "recommended_actions": [str, ...],\n    "safe_to_continue":    bool,\n  }\n\nEmpty / None input produces a coherent zero-shape report\n(safe_to_continue=True, no recommendations).\n'
- 'tool'
- 'pas143f2.monitoring'
- 'generated_at'
- 'total_alerts'
- 'by_severity'
- 'by_category'
- 'critical_alerts'
- 'high_alerts'
- 'recommended_actions'
- 'safe_to_continue'
- 'report'
- 'str'
- 'Render the report as a human-readable block for CLI output.'
- 'Monitoring report unavailable.'
- 'PAS143F2 — MONITORING REPORT'
- '  total alerts:     '
- '          '
- '  STATUS: safe_to_continue = TRUE'
- '  STATUS: safe_to_continue = FALSE  ← CRITICAL alert(s) active'
- 'CRITICAL ALERTS'
- '  • ['
- 'category'
- 'title'
- '        '
- 'description'
- 'HIGH ALERTS'
- 'RECOMMENDED ACTIONS'
- '  → '
- '========================================================================'
- '------------------------------------------------------------------------'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS143F2 — Monitoring report aggregation.\n\nPure deterministic aggregation. Same input → same output. The report\nis the operator-facing artefact: it tells a human what happened and\nwhat to do next.\n\nDoctrine:\n  - safe_to_continue is False iff any CRITICAL alert is present.\n  - recommended_actions are plain English. They reference categories,\n    not file paths. The detail is in critical_alerts / high_alerts.\n  - All alert payloads are passed through dispatcher.alert_to_safe_dict\n    before being included so PII / secrets cannot leak.\n')
               STORE_NAME               1 (__doc__)

  16           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  18           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('Counter',))
               IMPORT_NAME              4 (collections)
               IMPORT_FROM              5 (Counter)
               STORE_NAME               5 (Counter)
               POP_TOP

  19           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              6 (datetime)
               IMPORT_FROM              6 (datetime)
               STORE_NAME               6 (datetime)
               IMPORT_FROM              7 (timezone)
               STORE_NAME               7 (timezone)
               POP_TOP

  20           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List'))
               IMPORT_NAME              8 (typing)
               IMPORT_FROM              9 (Any)
               STORE_NAME               9 (Any)
               IMPORT_FROM             10 (Dict)
               STORE_NAME              10 (Dict)
               IMPORT_FROM             11 (List)
               STORE_NAME              11 (List)
               POP_TOP

  22           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Alert', 'Category', 'Severity', 'SEVERITY_RANK'))
               IMPORT_NAME             12 (app.services.monitoring.contracts)
               IMPORT_FROM             13 (Alert)
               STORE_NAME              13 (Alert)
               IMPORT_FROM             14 (Category)
               STORE_NAME              14 (Category)
               IMPORT_FROM             15 (Severity)
               STORE_NAME              15 (Severity)
               IMPORT_FROM             16 (SEVERITY_RANK)
               STORE_NAME              16 (SEVERITY_RANK)
               POP_TOP

  25           LOAD_SMALL_INT           0
               LOAD_CONST               6 (('alert_to_safe_dict', 'normalize_alert'))
               IMPORT_NAME             17 (app.services.monitoring.dispatcher)
               IMPORT_FROM             18 (alert_to_safe_dict)
               STORE_NAME              18 (alert_to_safe_dict)
               IMPORT_FROM             19 (normalize_alert)
               STORE_NAME              19 (normalize_alert)
               POP_TOP

  35           BUILD_MAP                0

  36           LOAD_NAME               14 (Category)
               LOAD_ATTR               40 (TENANT_ISOLATION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               42 (CRITICAL)
               BUILD_TUPLE              2

  37           LOAD_CONST               7 ('Stop tenant memory writes until the tenant-scope alert is resolved. Investigate the call site that attempted unscoped access.')

  35           MAP_ADD                  1

  40           LOAD_NAME               14 (Category)
               LOAD_ATTR               44 (SECURITY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               42 (CRITICAL)
               BUILD_TUPLE              2

  41           LOAD_CONST               8 ('Block deploys until CRITICAL security findings are remediated. Rotate any leaked credentials immediately.')

  35           MAP_ADD                  1

  44           LOAD_NAME               14 (Category)
               LOAD_ATTR               44 (SECURITY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  45           LOAD_CONST               9 ('Resolve HIGH security findings before persisting brain memory.')

  35           MAP_ADD                  1

  47           LOAD_NAME               14 (Category)
               LOAD_ATTR               48 (BACKUP)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               42 (CRITICAL)
               BUILD_TUPLE              2

  48           LOAD_CONST              10 ('Restore from the last verified backup if checksum mismatch is confirmed. Re-run scripts/verify_backup.py --strict before trusting the next backup.')

  35           MAP_ADD                  1

  52           LOAD_NAME               14 (Category)
               LOAD_ATTR               48 (BACKUP)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  53           LOAD_CONST              11 ('Re-take the affected backup and verify it before depending on it.')

  35           MAP_ADD                  1

  55           LOAD_NAME               14 (Category)
               LOAD_ATTR               50 (INTEGRITY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  56           LOAD_CONST              12 ('Re-run scripts/integrity_check.py --strict; investigate the failing case before accepting new event writes.')

  35           MAP_ADD                  1

  59           LOAD_NAME               14 (Category)
               LOAD_ATTR               50 (INTEGRITY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               52 (MEDIUM)
               BUILD_TUPLE              2

  60           LOAD_CONST              13 ('Audit the failing integrity check; widen test coverage for that path.')

  35           MAP_ADD                  1

  62           LOAD_NAME               14 (Category)
               LOAD_ATTR               54 (INGESTION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  63           LOAD_CONST              14 ('Investigate provider outage or API-key failure. Confirm Supabase service-role key + provider credentials are valid.')

  35           MAP_ADD                  1

  66           LOAD_NAME               14 (Category)
               LOAD_ATTR               54 (INGESTION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               52 (MEDIUM)
               BUILD_TUPLE              2

  67           LOAD_CONST              15 ('Check whether PAS_EVENT_TURN_LOGGING is on and the engine is emitting turn events for completed calls.')

  35           MAP_ADD                  1

  70           LOAD_NAME               14 (Category)
               LOAD_ATTR               56 (REPLAY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  71           LOAD_CONST              16 ('Pause replay-based optimization until the evaluator bug is fixed.')

  35           MAP_ADD                  1

  73           LOAD_NAME               14 (Category)
               LOAD_ATTR               56 (REPLAY)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               52 (MEDIUM)
               BUILD_TUPLE              2

  74           LOAD_CONST              17 ('Audit recent calls for missing terminal events; re-run the replay/evaluator on a known-good call to confirm the substrate.')

  35           MAP_ADD                  1

  77           LOAD_NAME               14 (Category)
               LOAD_ATTR               58 (OPTIMIZATION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  78           LOAD_CONST              18 ('Pause matrix-based recommendations; investigate ranking + metrics.')

  35           MAP_ADD                  1

  80           LOAD_NAME               14 (Category)
               LOAD_ATTR               58 (OPTIMIZATION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               52 (MEDIUM)
               BUILD_TUPLE              2

  81           LOAD_CONST              19 ('Verify scenario / strategy registry filters before re-running.')

  35           MAP_ADD                  1

  83           LOAD_NAME               14 (Category)
               LOAD_ATTR               58 (OPTIMIZATION)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               60 (LOW)
               BUILD_TUPLE              2

  84           LOAD_CONST              20 ('Add scenarios that target distinct personalities so strategies differentiate.')

  35           MAP_ADD                  1

  87           LOAD_NAME               14 (Category)
               LOAD_ATTR               62 (RUNTIME)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               42 (CRITICAL)
               BUILD_TUPLE              2

  88           LOAD_CONST              21 ('Stop the engine pod and inspect runtime logs before re-enabling.')

  35           MAP_ADD                  1

  90           LOAD_NAME               14 (Category)
               LOAD_ATTR               62 (RUNTIME)
               LOAD_NAME               15 (Severity)
               LOAD_ATTR               46 (HIGH)
               BUILD_TUPLE              2

  91           LOAD_CONST              22 ('Investigate the runtime error; widen test coverage for that path.')

  35           MAP_ADD                  1
               STORE_NAME              32 (_RECOMMENDATION_LIBRARY)
               LOAD_CONST              23 ('Dict[tuple, str]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              24 ('_RECOMMENDATION_LIBRARY')
               STORE_SUBSCR

  95           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\monitoring\report.py", line 95>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object _recommendations_for at 0x0000018C179A7290, file "app\services\monitoring\report.py", line 95>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_recommendations_for)

 121           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\monitoring\report.py", line 121>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object _normalize_all at 0x0000018C17FE17D0, file "app\services\monitoring\report.py", line 121>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_normalize_all)

 133           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\monitoring\report.py", line 133>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object generate_monitoring_report at 0x0000018C17D7CA60, file "app\services\monitoring\report.py", line 133>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (generate_monitoring_report)

 189           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\monitoring\report.py", line 189>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object summarize_monitoring_report at 0x0000018C17E89F30, file "app\services\monitoring\report.py", line 189>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (summarize_monitoring_report)
               LOAD_CONST              33 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\monitoring\report.py", line 95>:
 95           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')
              LOAD_CONST               2 ('List[Alert]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _recommendations_for at 0x0000018C179A7290, file "app\services\monitoring\report.py", line 95>:
 95           RESUME                   0

100           LOAD_GLOBAL              1 (set + NULL)
              CALL                     0
              STORE_FAST               1 (seen_pairs)

101           LOAD_FAST_BORROW         0 (alerts)
              GET_ITER
      L1:     FOR_ITER                42 (to L2)
              STORE_FAST               2 (a)

102           LOAD_FAST_BORROW         1 (seen_pairs)
              LOAD_ATTR                3 (add + NULL|self)
              LOAD_FAST_BORROW         2 (a)
              LOAD_ATTR                4 (category)
              LOAD_FAST_BORROW         2 (a)
              LOAD_ATTR                6 (severity)
              BUILD_TUPLE              2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           44 (to L1)

101   L2:     END_FOR
              POP_ITER

105           LOAD_GLOBAL              9 (sorted + NULL)

106           LOAD_FAST_BORROW         1 (seen_pairs)

107           LOAD_CONST               1 (<code object <lambda> at 0x0000018C18052F70, file "app\services\monitoring\report.py", line 107>)
              MAKE_FUNCTION

105           LOAD_CONST               2 (('key',))
              CALL_KW                  2
              STORE_FAST               3 (sorted_pairs)

109           BUILD_LIST               0
              STORE_FAST               4 (out)

110           LOAD_FAST_BORROW         3 (sorted_pairs)
              GET_ITER
      L3:     FOR_ITER                59 (to L6)
              STORE_FAST               5 (pair)

111           LOAD_GLOBAL             10 (_RECOMMENDATION_LIBRARY)
              LOAD_ATTR               13 (get + NULL|self)
              LOAD_FAST_BORROW         5 (pair)
              CALL                     1
              STORE_FAST               6 (msg)

112           LOAD_FAST_BORROW         6 (msg)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           34 (to L3)
      L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (msg, out)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           42 (to L3)

113   L5:     LOAD_FAST_BORROW         4 (out)
              LOAD_ATTR               15 (append + NULL|self)
              LOAD_FAST_BORROW         6 (msg)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           61 (to L3)

110   L6:     END_FOR
              POP_ITER

114           LOAD_FAST_BORROW         4 (out)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18052F70, file "app\services\monitoring\report.py", line 107>:
107           RESUME                   0
              LOAD_GLOBAL              0 (SEVERITY_RANK)
              LOAD_ATTR                2 (get)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (p)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              LOAD_SMALL_INT          99
              CALL                     2
              LOAD_FAST_BORROW         0 (p)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\monitoring\report.py", line 121>:
121           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalize_all at 0x0000018C17FE17D0, file "app\services\monitoring\report.py", line 121>:
121           RESUME                   0

123           LOAD_FAST_BORROW         0 (alerts)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

124           BUILD_LIST               0
              RETURN_VALUE

125   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

126           LOAD_FAST_BORROW         0 (alerts)
              GET_ITER
      L2:     FOR_ITER                37 (to L4)
              STORE_FAST               2 (a)

127           LOAD_GLOBAL              1 (normalize_alert + NULL)
              LOAD_FAST_BORROW         2 (a)
              CALL                     1
              STORE_FAST               3 (n)

128           LOAD_FAST_BORROW         3 (n)
              POP_JUMP_IF_NOT_NONE     3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           20 (to L2)

129   L3:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         3 (n)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           39 (to L2)

126   L4:     END_FOR
              POP_ITER

130           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\monitoring\report.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object generate_monitoring_report at 0x0000018C17D7CA60, file "app\services\monitoring\report.py", line 133>:
 133            RESUME                   0

 153            LOAD_GLOBAL              1 (_normalize_all + NULL)
                LOAD_FAST_BORROW         0 (alerts)
                CALL                     1
                STORE_FAST               1 (normalized)

 155            LOAD_GLOBAL              3 (Counter + NULL)
                CALL                     0
                STORE_FAST               2 (by_severity)

 156            LOAD_GLOBAL              3 (Counter + NULL)
                CALL                     0
                STORE_FAST               3 (by_category)

 157            LOAD_FAST_BORROW         1 (normalized)
                GET_ITER
        L1:     FOR_ITER                63 (to L2)
                STORE_FAST               4 (a)

 158            LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (by_severity, a)
                LOAD_ATTR                4 (severity)
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR

 159            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (by_category, a)
                LOAD_ATTR                6 (category)
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                JUMP_BACKWARD           65 (to L1)

 157    L2:     END_FOR
                POP_ITER

 162            LOAD_FAST_BORROW         1 (normalized)
                GET_ITER

 161            LOAD_FAST_AND_CLEAR      4 (a)
                SWAP                     2
        L3:     BUILD_LIST               0
                SWAP                     2

 162    L4:     FOR_ITER                47 (to L7)
                STORE_FAST               4 (a)

 163            LOAD_FAST_BORROW         4 (a)
                LOAD_ATTR                4 (severity)
                LOAD_GLOBAL              8 (Severity)
                LOAD_ATTR               10 (CRITICAL)
                COMPARE_OP              88 (bool(==))

 162    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           36 (to L4)
        L6:     LOAD_GLOBAL             13 (alert_to_safe_dict + NULL)
                LOAD_FAST_BORROW         4 (a)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           49 (to L4)
        L7:     END_FOR
                POP_ITER

 161    L8:     STORE_FAST               5 (critical)
                STORE_FAST               4 (a)

 166            LOAD_FAST_BORROW         1 (normalized)
                GET_ITER

 165            LOAD_FAST_AND_CLEAR      4 (a)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 166   L10:     FOR_ITER                47 (to L13)
                STORE_FAST               4 (a)

 167            LOAD_FAST_BORROW         4 (a)
                LOAD_ATTR                4 (severity)
                LOAD_GLOBAL              8 (Severity)
                LOAD_ATTR               14 (HIGH)
                COMPARE_OP              88 (bool(==))

 166   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           36 (to L10)
       L12:     LOAD_GLOBAL             13 (alert_to_safe_dict + NULL)
                LOAD_FAST_BORROW         4 (a)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           49 (to L10)
       L13:     END_FOR
                POP_ITER

 165   L14:     STORE_FAST               6 (high)
                STORE_FAST               4 (a)

 170            LOAD_FAST_BORROW         2 (by_severity)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_GLOBAL              8 (Severity)
                LOAD_ATTR               10 (CRITICAL)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           0
                COMPARE_OP              72 (==)
                STORE_FAST               7 (safe_to_continue)

 173            LOAD_CONST               1 ('tool')
                LOAD_CONST               2 ('pas143f2.monitoring')

 174            LOAD_CONST               3 ('generated_at')
                LOAD_GLOBAL             18 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL             22 (timezone)
                LOAD_ATTR               24 (utc)
                CALL                     1
                LOAD_ATTR               27 (isoformat + NULL|self)
                CALL                     0

 175            LOAD_CONST               4 ('total_alerts')
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST_BORROW         1 (normalized)
                CALL                     1

 176            LOAD_CONST               5 ('by_severity')
                LOAD_GLOBAL             31 (dict + NULL)
                LOAD_FAST_BORROW         2 (by_severity)
                CALL                     1

 177            LOAD_CONST               6 ('by_category')
                LOAD_GLOBAL             31 (dict + NULL)
                LOAD_FAST_BORROW         3 (by_category)
                CALL                     1

 178            LOAD_CONST               7 ('critical_alerts')
                LOAD_FAST_BORROW         5 (critical)

 179            LOAD_CONST               8 ('high_alerts')
                LOAD_FAST_BORROW         6 (high)

 180            LOAD_CONST               9 ('recommended_actions')
                LOAD_GLOBAL             33 (_recommendations_for + NULL)
                LOAD_FAST_BORROW         1 (normalized)
                CALL                     1

 181            LOAD_CONST              10 ('safe_to_continue')
                LOAD_FAST_BORROW         7 (safe_to_continue)

 172            BUILD_MAP                9
                RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 161            SWAP                     2
                STORE_FAST               4 (a)
                RERAISE                  0

  --   L16:     SWAP                     2
                POP_TOP

 165            SWAP                     2
                STORE_FAST               4 (a)
                RERAISE                  0
ExceptionTable:
  L3 to L5 -> L15 [2]
  L6 to L8 -> L15 [2]
  L9 to L11 -> L16 [2]
  L12 to L14 -> L16 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\monitoring\report.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object summarize_monitoring_report at 0x0000018C17E89F30, file "app\services\monitoring\report.py", line 189>:
189            RESUME                   0

191            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (report)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

192            LOAD_CONST               1 ('Monitoring report unavailable.')
               RETURN_VALUE

194    L1:     BUILD_LIST               0
               STORE_FAST               1 (lines)

195            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              28 ('========================================================================')
               CALL                     1
               POP_TOP

196            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               2 ('PAS143F2 — MONITORING REPORT')
               CALL                     1
               POP_TOP

197            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              29 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

198            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               3 ('  total alerts:     ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               4 ('total_alerts')
               LOAD_SMALL_INT           0
               CALL                     2
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

199            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               5 ('by_severity')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     STORE_FAST               2 (by_sev)

200            LOAD_CONST              30 (('CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO'))
               GET_ITER
       L3:     FOR_ITER                55 (to L5)
               STORE_FAST               3 (sev)

201            LOAD_FAST_BORROW         2 (by_sev)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         3 (sev)
               LOAD_SMALL_INT           0
               CALL                     2
               STORE_FAST               4 (n)

202            LOAD_FAST_BORROW         4 (n)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           31 (to L3)

203    L4:     LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               6 ('  ')
               LOAD_FAST_BORROW         3 (sev)
               LOAD_CONST               7 ('<8')
               FORMAT_WITH_SPEC
               LOAD_CONST               8 ('          ')
               LOAD_FAST_BORROW         4 (n)
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           57 (to L3)

200    L5:     END_FOR
               POP_ITER

204            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('')
               CALL                     1
               POP_TOP

206            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              10 ('safe_to_continue')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L6)
               NOT_TAKEN

207            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              11 ('  STATUS: safe_to_continue = TRUE')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            17 (to L7)

209    L6:     LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              12 ('  STATUS: safe_to_continue = FALSE  ← CRITICAL alert(s) active')
               CALL                     1
               POP_TOP

210    L7:     LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('')
               CALL                     1
               POP_TOP

212            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              13 ('critical_alerts')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L8:     STORE_FAST               5 (crit)

213            LOAD_FAST_BORROW         5 (crit)
               TO_BOOL
               POP_JUMP_IF_FALSE      140 (to L11)
               NOT_TAKEN

214            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              14 ('CRITICAL ALERTS')
               CALL                     1
               POP_TOP

215            LOAD_FAST_BORROW         5 (crit)
               GET_ITER
       L9:     FOR_ITER                99 (to L10)
               STORE_FAST               6 (a)

216            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              15 ('  • [')
               LOAD_FAST_BORROW         6 (a)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              16 ('category')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              17 ('] ')
               LOAD_FAST_BORROW         6 (a)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              18 ('title')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP

217            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              19 ('        ')
               LOAD_FAST_BORROW         6 (a)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              20 ('description')
               LOAD_CONST               9 ('')
               CALL                     2
               LOAD_CONST              21 (slice(None, 300, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          101 (to L9)

215   L10:     END_FOR
               POP_ITER

218            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('')
               CALL                     1
               POP_TOP

220   L11:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              22 ('high_alerts')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L12:     STORE_FAST               7 (high)

221            LOAD_FAST_BORROW         7 (high)
               TO_BOOL
               POP_JUMP_IF_FALSE       97 (to L15)
               NOT_TAKEN

222            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              23 ('HIGH ALERTS')
               CALL                     1
               POP_TOP

223            LOAD_FAST_BORROW         7 (high)
               GET_ITER
      L13:     FOR_ITER                56 (to L14)
               STORE_FAST               6 (a)

224            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              15 ('  • [')
               LOAD_FAST_BORROW         6 (a)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              16 ('category')
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              17 ('] ')
               LOAD_FAST_BORROW         6 (a)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              18 ('title')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           58 (to L13)

223   L14:     END_FOR
               POP_ITER

225            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('')
               CALL                     1
               POP_TOP

227   L15:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              24 ('recommended_actions')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L16)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L16:     STORE_FAST               8 (recs)

228            LOAD_FAST_BORROW         8 (recs)
               TO_BOOL
               POP_JUMP_IF_FALSE       64 (to L19)
               NOT_TAKEN

229            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              25 ('RECOMMENDED ACTIONS')
               CALL                     1
               POP_TOP

230            LOAD_FAST_BORROW         8 (recs)
               GET_ITER
      L17:     FOR_ITER                23 (to L18)
               STORE_FAST               9 (r)

231            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              26 ('  → ')
               LOAD_FAST_BORROW         9 (r)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           25 (to L17)

230   L18:     END_FOR
               POP_ITER

232            LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               9 ('')
               CALL                     1
               POP_TOP

234   L19:     LOAD_FAST_BORROW         1 (lines)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST              28 ('========================================================================')
               CALL                     1
               POP_TOP

235            LOAD_CONST              27 ('\n')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (lines)
               CALL                     1
               RETURN_VALUE
```
