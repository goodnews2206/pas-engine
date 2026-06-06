# tenant/tenant_audit_dashboard

- **pyc:** `app\services\tenant\__pycache__\tenant_audit_dashboard.cpython-314.pyc`
- **expected source path (absent):** `app\services\tenant/tenant_audit_dashboard.py`
- **co_filename (from bytecode):** `app/services/tenant/tenant_audit_dashboard.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** tenant

## Module docstring

```
PAS178 — Tenant audit dashboard service.

Bounded brokerage-scoped read surface combining:

* The PAS178 cross-window chain status.
* The PAS178 durable verification-run history (summary).
* The PAS177 tenant-ack count.
* The PAS176 Merkle-window count.

Doctrine:

* **Brokerage-scoped only.** Every helper unpacks the
  brokerage_id from the brokerage dict resolved by auth.
* **Read-only.** No writes / mutations.
* **No PII.** Every envelope is bounded counts + closed
  status tokens + structural timestamps. NEVER raw audit
  metadata / transcript / raw payload / operator notes /
  secret / env_value / cross-brokerage data.
* **NEVER raises.** Failures collapse to ``status="skipped"``
  envelopes.
* **Closed allow-list for tenant-visible fields:**
  ``brokerage_id, latest_chain_status,
  latest_verification_status, last_verified_at,
  verification_count, acknowledgement_count,
  merkle_window_count, warning_count, action_required``.

Public surface:

  * ``tenant_audit_dashboard_summary(brokerage)``
  * ``tenant_chain_status_summary(brokerage)``
  * ``tenant_verification_history_summary(brokerage)``
  * ``tenant_non_repudiation_summary(brokerage)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.operator.audit_chain_verifier`, `app.services.operator.audit_verification_runs`, `app.services.operator.audit_window_chain`, `app.services.tenant.tenant_audit_ack_store`, `brokerage_chain_badge`, `datetime`, `logging`, `tenant_acknowledgement_summary`, `timedelta`, `timezone`, `typing`, `verification_run_summary`, `verify_window`

## Classes

_none_

## Functions / methods

`__annotate__`, `_now_dt`, `_parse_iso`, `_resolve_brokerage_id`, `_safe_envelope`, `tenant_audit_dashboard_summary`, `tenant_chain_status_summary`, `tenant_non_repudiation_summary`, `tenant_verification_history_summary`

## Env-key candidates

`NONE`

## String constants (redacted where noted)

- '\nPAS178 — Tenant audit dashboard service.\n\nBounded brokerage-scoped read surface combining:\n\n* The PAS178 cross-window chain status.\n* The PAS178 durable verification-run history (summary).\n* The PAS177 tenant-ack count.\n* The PAS176 Merkle-window count.\n\nDoctrine:\n\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the brokerage dict resolved by auth.\n* **Read-only.** No writes / mutations.\n* **No PII.** Every envelope is bounded counts + closed\n  status tokens + structural timestamps. NEVER raw audit\n  metadata / transcript / raw payload / operator notes /\n  secret / env_value / cross-brokerage data.\n* **NEVER raises.** Failures collapse to ``status="skipped"``\n  envelopes.\n* **Closed allow-list for tenant-visible fields:**\n  ``brokerage_id, latest_chain_status,\n  latest_verification_status, last_verified_at,\n  verification_count, acknowledgement_count,\n  merkle_window_count, warning_count, action_required``.\n\nPublic surface:\n\n  * ``tenant_audit_dashboard_summary(brokerage)``\n  * ``tenant_chain_status_summary(brokerage)``\n  * ``tenant_verification_history_summary(brokerage)``\n  * ``tenant_non_repudiation_summary(brokerage)``\n'
- 'pas.tenant.audit_dashboard'
- 'payload'
- 'warnings'
- 'error_code'
- 'brokerage'
- 'Any'
- 'return'
- 'Optional[str]'
- 'datetime'
- 'value'
- 'Optional[datetime]'
- '+00:00'
- 'status'
- 'str'
- 'brokerage_id'
- 'Optional[Dict[str, Any]]'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'Tenant-safe projection of the PAS178 cross-window\nchain status for the brokerage. Returns the latest\nchain status + count of Merkle windows. NEVER raises.'
- 'failed'
- 'missing_brokerage_id'
- 'entries_total'
- 'chain_status'
- 'broken'
- 'skipped'
- 'latest_chain_status'
- 'none'
- 'merkle_window_count'
- 'warning_count'
- 'last_window_end'
- 'latest_window_end'
- 'tenant_chain_status_summary error type='
- 'unexpected:'
- 'tenant_chain_status_unavailable'
- "Tenant-safe verification-run history summary. Returns\ncounts + the most recent run's status and timestamp.\nNEVER raises."
- 'verification_count'
- 'latest_verification_status'
- 'NONE'
- 'last_verified_at'
- 'latest_run'
- 'total'
- 'completed_at'
- 'started_at'
- 'tenant_verification_history_summary error type='
- 'tenant_verification_history_unavailable'
- 'Tenant-safe non-repudiation summary: ack counts +\nMerkle window count + chain status. NEVER raises.'
- 'acknowledgement_count'
- 'tenant_non_repudiation_summary error type='
- 'tenant_non_repudiation_unavailable'
- 'Combined dashboard summary. Returns the closed allow-\nlist of tenant-visible fields plus an ``action_required``\nboolean indicating whether the operator needs to act on a\nrecent break or stale verification. NEVER raises.'
- 'action_required'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS178 — Tenant audit dashboard service.\n\nBounded brokerage-scoped read surface combining:\n\n* The PAS178 cross-window chain status.\n* The PAS178 durable verification-run history (summary).\n* The PAS177 tenant-ack count.\n* The PAS176 Merkle-window count.\n\nDoctrine:\n\n* **Brokerage-scoped only.** Every helper unpacks the\n  brokerage_id from the brokerage dict resolved by auth.\n* **Read-only.** No writes / mutations.\n* **No PII.** Every envelope is bounded counts + closed\n  status tokens + structural timestamps. NEVER raw audit\n  metadata / transcript / raw payload / operator notes /\n  secret / env_value / cross-brokerage data.\n* **NEVER raises.** Failures collapse to ``status="skipped"``\n  envelopes.\n* **Closed allow-list for tenant-visible fields:**\n  ``brokerage_id, latest_chain_status,\n  latest_verification_status, last_verified_at,\n  verification_count, acknowledgement_count,\n  merkle_window_count, warning_count, action_required``.\n\nPublic surface:\n\n  * ``tenant_audit_dashboard_summary(brokerage)``\n  * ``tenant_chain_status_summary(brokerage)``\n  * ``tenant_verification_history_summary(brokerage)``\n  * ``tenant_non_repudiation_summary(brokerage)``\n')
              STORE_NAME               0 (__doc__)

 36           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 38           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              IMPORT_FROM              6 (timezone)
              STORE_NAME               6 (timezone)
              POP_TOP

 40           LOAD_SMALL_INT           0
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

 43           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.tenant.audit_dashboard')
              CALL                     1
              STORE_NAME              13 (logger)

 50           LOAD_CONST              25 (('brokerage_id', 'latest_chain_status', 'latest_verification_status', 'last_verified_at', 'verification_count', 'acknowledgement_count', 'merkle_window_count', 'warning_count', 'action_required'))
              STORE_NAME              14 (TENANT_DASHBOARD_PAYLOAD_KEYS)

 64           LOAD_SMALL_INT          36
              STORE_NAME              15 (_STALE_VERIFICATION_HOURS)

 71           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/tenant/tenant_audit_dashboard.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _resolve_brokerage_id at 0x0000018C1804D3B0, file "app/services/tenant/tenant_audit_dashboard.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_resolve_brokerage_id)

 80           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/tenant/tenant_audit_dashboard.py", line 80>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _now_dt at 0x0000018C18053CF0, file "app/services/tenant/tenant_audit_dashboard.py", line 80>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_now_dt)

 84           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2970, file "app/services/tenant/tenant_audit_dashboard.py", line 84>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _parse_iso at 0x0000018C181B1920, file "app/services/tenant/tenant_audit_dashboard.py", line 84>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_parse_iso)

 96           LOAD_CONST              12 ('payload')

100           LOAD_CONST               2 (None)

 96           LOAD_CONST              13 ('warnings')

101           LOAD_CONST               2 (None)

 96           LOAD_CONST              14 ('error_code')

102           LOAD_CONST               2 (None)

 96           BUILD_MAP                3
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025730, file "app/services/tenant/tenant_audit_dashboard.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C18128580, file "app/services/tenant/tenant_audit_dashboard.py", line 96>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              19 (_safe_envelope)

117           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3D20, file "app/services/tenant/tenant_audit_dashboard.py", line 117>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object tenant_chain_status_summary at 0x0000018C18646760, file "app/services/tenant/tenant_audit_dashboard.py", line 117>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (tenant_chain_status_summary)

169           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/services/tenant/tenant_audit_dashboard.py", line 169>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object tenant_verification_history_summary at 0x0000018C17D51E70, file "app/services/tenant/tenant_audit_dashboard.py", line 169>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (tenant_verification_history_summary)

224           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/tenant/tenant_audit_dashboard.py", line 224>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object tenant_non_repudiation_summary at 0x0000018C17D6DFC0, file "app/services/tenant/tenant_audit_dashboard.py", line 224>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (tenant_non_repudiation_summary)

262           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/tenant/tenant_audit_dashboard.py", line 262>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object tenant_audit_dashboard_summary at 0x0000018C18300610, file "app/services/tenant/tenant_audit_dashboard.py", line 262>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (tenant_audit_dashboard_summary)

321           BUILD_LIST               0
              LOAD_CONST              26 (('TENANT_DASHBOARD_PAYLOAD_KEYS', 'tenant_audit_dashboard_summary', 'tenant_chain_status_summary', 'tenant_verification_history_summary', 'tenant_non_repudiation_summary'))
              LIST_EXTEND              1
              STORE_NAME              24 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/tenant/tenant_audit_dashboard.py", line 71>:
 71           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_brokerage_id at 0x0000018C1804D3B0, file "app/services/tenant/tenant_audit_dashboard.py", line 71>:
 71           RESUME                   0

 72           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 73           LOAD_CONST               0 (None)
              RETURN_VALUE

 74   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('id')
              CALL                     1
              STORE_FAST               1 (bid)

 75           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

 76   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

 77   L3:     LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/tenant/tenant_audit_dashboard.py", line 80>:
 80           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('datetime')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C18053CF0, file "app/services/tenant/tenant_audit_dashboard.py", line 80>:
 80           RESUME                   0

 81           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app/services/tenant/tenant_audit_dashboard.py", line 84>:
 84           RESUME                   0
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
              LOAD_CONST               4 ('Optional[datetime]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_iso at 0x0000018C181B1920, file "app/services/tenant/tenant_audit_dashboard.py", line 84>:
  84           RESUME                   0

  85           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

  86   L1:     LOAD_CONST               0 (None)
               RETURN_VALUE

  87   L2:     NOP

  88   L3:     LOAD_GLOBAL              6 (datetime)
               LOAD_ATTR                8 (fromisoformat)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               11 (replace + NULL|self)
               LOAD_CONST               1 ('Z')
               LOAD_CONST               2 ('+00:00')
               CALL                     2
               CALL                     1
               STORE_FAST               1 (dt)

  89           LOAD_FAST_BORROW         1 (dt)
               LOAD_ATTR               12 (tzinfo)
               POP_JUMP_IF_NOT_NONE    33 (to L4)
               NOT_TAKEN

  90           LOAD_FAST_BORROW         1 (dt)
               LOAD_ATTR               11 (replace + NULL|self)
               LOAD_GLOBAL             14 (timezone)
               LOAD_ATTR               16 (utc)
               LOAD_CONST               3 (('tzinfo',))
               CALL_KW                  1
               STORE_FAST               1 (dt)

  91   L4:     LOAD_FAST_BORROW         1 (dt)
       L5:     RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  92           LOAD_GLOBAL             18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

  93   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

  92   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L5 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/tenant/tenant_audit_dashboard.py", line 96>:
 96           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 98           LOAD_CONST               2 ('str')

 96           LOAD_CONST               3 ('brokerage_id')

 99           LOAD_CONST               4 ('Optional[str]')

 96           LOAD_CONST               5 ('payload')

100           LOAD_CONST               6 ('Optional[Dict[str, Any]]')

 96           LOAD_CONST               7 ('warnings')

101           LOAD_CONST               8 ('Optional[List[str]]')

 96           LOAD_CONST               9 ('error_code')

102           LOAD_CONST               4 ('Optional[str]')

 96           LOAD_CONST              10 ('return')

103           LOAD_CONST              11 ('Dict[str, Any]')

 96           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18128580, file "app/services/tenant/tenant_audit_dashboard.py", line 96>:
 96           RESUME                   0

105           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

106           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                1 (brokerage_id)

107           LOAD_CONST               2 ('payload')
              LOAD_FAST                2 (payload)

108           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

109           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

104           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app/services/tenant/tenant_audit_dashboard.py", line 117>:
117           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_chain_status_summary at 0x0000018C18646760, file "app/services/tenant/tenant_audit_dashboard.py", line 117>:
 117            RESUME                   0

 121            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 122            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 123            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 124            LOAD_CONST               2 ('failed')
                LOAD_CONST               1 (None)

 125            LOAD_CONST               3 ('missing_brokerage_id')

 123            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 127    L1:     NOP

 128    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('brokerage_chain_badge',))
                IMPORT_NAME              2 (app.services.operator.audit_window_chain)
                IMPORT_FROM              3 (brokerage_chain_badge)
                STORE_FAST               2 (brokerage_chain_badge)
                POP_TOP

 131            LOAD_SMALL_INT           0
                LOAD_CONST               6 (('verify_window',))
                IMPORT_NAME              4 (app.services.operator.audit_chain_verifier)
                IMPORT_FROM              5 (verify_window)
                STORE_FAST               3 (verify_window)
                POP_TOP

 134            LOAD_FAST_BORROW         2 (brokerage_chain_badge)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                CALL                     1
                STORE_FAST               4 (badge)

 138            LOAD_SMALL_INT           0
                STORE_FAST               5 (merkle_count)

 139            LOAD_SMALL_INT           0
                STORE_FAST               6 (warning_count)

 140            LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       63 (to L8)
                NOT_TAKEN

 141            LOAD_GLOBAL             15 (int + NULL)
                LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               9 ('entries_total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_SMALL_INT           0
        L5:     CALL                     1
                STORE_FAST               5 (merkle_count)

 143            LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              10 ('chain_status')
                CALL                     1
                LOAD_CONST              11 ('broken')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_SMALL_INT           1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_SMALL_INT           0

 142    L7:     STORE_FAST               6 (warning_count)

 145    L8:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 146            LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST              12 ('skipped')

 147   L11:     LOAD_FAST                1 (bid)

 149            LOAD_CONST              13 ('latest_chain_status')
                LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              10 ('chain_status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                LOAD_CONST              14 ('none')

 150   L14:     LOAD_CONST              15 ('merkle_window_count')
                LOAD_FAST_BORROW         5 (merkle_count)

 151            LOAD_CONST              16 ('warning_count')
                LOAD_FAST_BORROW         6 (warning_count)

 152            LOAD_CONST              17 ('last_window_end')
                LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              18 ('latest_window_end')
                CALL                     1

 148            BUILD_MAP                4

 154            LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              19 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1

 155            LOAD_FAST_BORROW         4 (badge)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              20 ('error_code')
                CALL                     1

 145            LOAD_CONST              21 (('status', 'brokerage_id', 'payload', 'warnings', 'error_code'))
                CALL_KW                  5
       L18:     RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 157            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L24)
                NOT_TAKEN
                STORE_FAST               7 (e)

 158   L20:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 159            LOAD_CONST              22 ('tenant_chain_status_summary error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 158            CALL                     1
                POP_TOP

 161            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 162            LOAD_CONST              12 ('skipped')

 163            LOAD_FAST                1 (bid)

 164            LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 165            LOAD_CONST              24 ('tenant_chain_status_unavailable')

 161            LOAD_CONST              25 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L21:     SWAP                     2
       L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 157   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L19 [0]
  L4 to L9 -> L19 [0]
  L10 to L12 -> L19 [0]
  L13 to L15 -> L19 [0]
  L16 to L18 -> L19 [0]
  L19 to L20 -> L25 [1] lasti
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L25 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/services/tenant/tenant_audit_dashboard.py", line 169>:
169           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_verification_history_summary at 0x0000018C17D51E70, file "app/services/tenant/tenant_audit_dashboard.py", line 169>:
 169            RESUME                   0

 173            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 174            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 175            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 176            LOAD_CONST               2 ('failed')
                LOAD_CONST               1 (None)

 177            LOAD_CONST               3 ('missing_brokerage_id')

 175            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 179    L1:     NOP

 180    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('verification_run_summary',))
                IMPORT_NAME              2 (app.services.operator.audit_verification_runs)
                IMPORT_FROM              3 (verification_run_summary)
                STORE_FAST               2 (verification_run_summary)
                POP_TOP

 183            LOAD_FAST_BORROW         2 (verification_run_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                LOAD_CONST               6 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               3 (summary)

 184            LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                LOAD_CONST               8 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       97 (to L10)
                NOT_TAKEN

 185            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 186            LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                LOAD_CONST               9 ('skipped')

 187    L5:     LOAD_FAST                1 (bid)

 189            LOAD_CONST              10 ('verification_count')
                LOAD_SMALL_INT           0

 190            LOAD_CONST              11 ('latest_verification_status')
                LOAD_CONST              12 ('NONE')

 191            LOAD_CONST              13 ('last_verified_at')
                LOAD_CONST               1 (None)

 188            BUILD_MAP                3

 193            LOAD_GLOBAL             11 (list + NULL)
                LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              14 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1

 194            LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              15 ('error_code')
                CALL                     1

 185            LOAD_CONST              16 (('status', 'brokerage_id', 'payload', 'warnings', 'error_code'))
                CALL_KW                  5
        L9:     RETURN_VALUE

 196   L10:     LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              17 ('latest_run')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_MAP                0
       L13:     STORE_FAST               4 (latest)

 197            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 198            LOAD_CONST               8 ('ok')

 199            LOAD_FAST                1 (bid)

 201            LOAD_CONST              10 ('verification_count')
                LOAD_GLOBAL             13 (int + NULL)
                LOAD_FAST_BORROW         3 (summary)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              18 ('total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                LOAD_SMALL_INT           0
       L16:     CALL                     1

 202            LOAD_CONST              11 ('latest_verification_status')

 203            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (latest)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L17)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (latest)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('status')
                CALL                     1
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              12 ('NONE')

 202   L18:     COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L21)
       L19:     NOT_TAKEN
       L20:     POP_TOP

 204            LOAD_CONST              12 ('NONE')

 205   L21:     LOAD_CONST              13 ('last_verified_at')

 207            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (latest)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       43 (to L25)
                NOT_TAKEN

 206            LOAD_FAST_BORROW         4 (latest)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              19 ('completed_at')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L24)
       L22:     NOT_TAKEN
       L23:     POP_TOP
                LOAD_FAST_BORROW         4 (latest)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              20 ('started_at')
                CALL                     1

  --   L24:     JUMP_FORWARD             1 (to L26)

 207   L25:     LOAD_CONST               1 (None)

 200   L26:     BUILD_MAP                3

 197            LOAD_CONST              21 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L27:     RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 211            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L33)
                NOT_TAKEN
                STORE_FAST               5 (e)

 212   L29:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 213            LOAD_CONST              22 ('tenant_verification_history_summary error type=')

 214            LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 213            BUILD_STRING             2

 212            CALL                     1
                POP_TOP

 216            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 217            LOAD_CONST               9 ('skipped')

 218            LOAD_FAST                1 (bid)

 219            LOAD_CONST              23 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 220            LOAD_CONST              24 ('tenant_verification_history_unavailable')

 216            LOAD_CONST              25 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 211   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L28 [0]
  L4 to L6 -> L28 [0]
  L7 to L9 -> L28 [0]
  L10 to L11 -> L28 [0]
  L12 to L14 -> L28 [0]
  L15 to L19 -> L28 [0]
  L20 to L22 -> L28 [0]
  L23 to L27 -> L28 [0]
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/tenant/tenant_audit_dashboard.py", line 224>:
224           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_non_repudiation_summary at 0x0000018C17D6DFC0, file "app/services/tenant/tenant_audit_dashboard.py", line 224>:
 224            RESUME                   0

 227            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 228            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 229            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 230            LOAD_CONST               2 ('failed')
                LOAD_CONST               1 (None)

 231            LOAD_CONST               3 ('missing_brokerage_id')

 229            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 233    L1:     NOP

 234    L2:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('tenant_acknowledgement_summary',))
                IMPORT_NAME              2 (app.services.tenant.tenant_audit_ack_store)
                IMPORT_FROM              3 (tenant_acknowledgement_summary)
                STORE_FAST               2 (tenant_acknowledgement_summary)
                POP_TOP

 237            LOAD_FAST_BORROW         2 (tenant_acknowledgement_summary)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (bid)
                CALL                     1
                STORE_FAST               3 (ack)

 238            LOAD_GLOBAL              9 (tenant_chain_status_summary + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               4 (chain)

 239            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (chain)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (chain)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               6 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
        L3:     NOT_TAKEN
        L4:     POP_TOP
                BUILD_MAP                0

  --    L5:     JUMP_FORWARD             1 (to L7)

 239    L6:     BUILD_MAP                0
        L7:     STORE_FAST               5 (chain_payload)

 240            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (ack)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       37 (to L11)
                NOT_TAKEN
                LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         3 (ack)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               7 ('total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                LOAD_SMALL_INT           0
       L10:     CALL                     1
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_SMALL_INT           0
       L12:     STORE_FAST               6 (ack_total)

 241            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 242            LOAD_CONST               8 ('ok')

 243            LOAD_FAST                1 (bid)

 245            LOAD_CONST               9 ('acknowledgement_count')
                LOAD_FAST                6 (ack_total)

 246            LOAD_CONST              10 ('merkle_window_count')
                LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         5 (chain_payload)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('merkle_window_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_SMALL_INT           0
       L15:     CALL                     1

 247            LOAD_CONST              11 ('latest_chain_status')
                LOAD_FAST_BORROW         5 (chain_payload)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('latest_chain_status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST              12 ('none')

 244   L18:     BUILD_MAP                3

 241            LOAD_CONST              13 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 250            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       92 (to L25)
                NOT_TAKEN
                STORE_FAST               7 (e)

 251   L21:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 252            LOAD_CONST              14 ('tenant_non_repudiation_summary error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 251            CALL                     1
                POP_TOP

 254            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 255            LOAD_CONST              15 ('skipped')

 256            LOAD_FAST                1 (bid)

 257            LOAD_CONST              16 ('unexpected:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 258            LOAD_CONST              17 ('tenant_non_repudiation_unavailable')

 254            LOAD_CONST              18 (('status', 'brokerage_id', 'warnings', 'error_code'))
                CALL_KW                  4
       L22:     SWAP                     2
       L23:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L24:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 250   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L20 [0]
  L4 to L8 -> L20 [0]
  L9 to L13 -> L20 [0]
  L14 to L16 -> L20 [0]
  L17 to L19 -> L20 [0]
  L20 to L21 -> L26 [1] lasti
  L21 to L22 -> L24 [1] lasti
  L22 to L23 -> L26 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/tenant/tenant_audit_dashboard.py", line 262>:
262           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object tenant_audit_dashboard_summary at 0x0000018C18300610, file "app/services/tenant/tenant_audit_dashboard.py", line 262>:
 262            RESUME                   0

 267            LOAD_GLOBAL              1 (_resolve_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               1 (bid)

 268            LOAD_FAST_BORROW         1 (bid)
                POP_JUMP_IF_NOT_NONE    15 (to L1)
                NOT_TAKEN

 269            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 270            LOAD_CONST               2 ('failed')
                LOAD_CONST               1 (None)

 271            LOAD_CONST               3 ('missing_brokerage_id')

 269            LOAD_CONST               4 (('status', 'brokerage_id', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 273    L1:     LOAD_GLOBAL              5 (tenant_chain_status_summary + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               2 (chain)

 274            LOAD_GLOBAL              7 (tenant_verification_history_summary + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               3 (history)

 275            LOAD_GLOBAL              9 (tenant_non_repudiation_summary + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                STORE_FAST               4 (non_rep)

 276            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (chain)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (chain)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               5 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0

  --    L2:     JUMP_FORWARD             1 (to L4)

 276    L3:     BUILD_MAP                0
        L4:     STORE_FAST               5 (chain_pl)

 277            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (history)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (history)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               5 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0

  --    L5:     JUMP_FORWARD             1 (to L7)

 277    L6:     BUILD_MAP                0
        L7:     STORE_FAST               6 (history_pl)

 278            LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (non_rep)
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (non_rep)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               5 ('payload')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0

  --    L8:     JUMP_FORWARD             1 (to L10)

 278    L9:     BUILD_MAP                0
       L10:     STORE_FAST               7 (non_rep_pl)

 280            LOAD_FAST_BORROW         5 (chain_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               6 ('latest_chain_status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               7 ('none')
       L11:     STORE_FAST               8 (latest_chain_status)

 281            LOAD_FAST_BORROW         6 (history_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST               8 ('latest_verification_status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               9 ('NONE')
       L12:     STORE_FAST               9 (latest_verif_status)

 282            LOAD_FAST_BORROW         6 (history_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              10 ('last_verified_at')
                CALL                     1
                STORE_FAST              10 (last_verified_at_str)

 283            LOAD_GLOBAL             17 (_parse_iso + NULL)
                LOAD_FAST_BORROW        10 (last_verified_at_str)
                CALL                     1
                STORE_FAST              11 (last_verified_dt)

 284            LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         5 (chain_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              11 ('warning_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L13:     CALL                     1
                STORE_FAST              12 (warning_count)

 287            LOAD_CONST              12 (False)
                STORE_FAST              13 (action_required)

 288            LOAD_FAST_BORROW         8 (latest_chain_status)
                LOAD_CONST              13 ('broken')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 289            LOAD_CONST              14 (True)
                STORE_FAST              13 (action_required)

 290   L14:     LOAD_FAST_BORROW         9 (latest_verif_status)
                LOAD_CONST              23 (('FAILED', 'PARTIAL'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN

 291            LOAD_CONST              14 (True)
                STORE_FAST              13 (action_required)

 292   L15:     LOAD_FAST_BORROW        11 (last_verified_dt)
                POP_JUMP_IF_NOT_NONE    27 (to L16)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (history_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('verification_count')
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        4 (to L16)
                NOT_TAKEN

 294            LOAD_CONST              14 (True)
                STORE_FAST              13 (action_required)
                JUMP_FORWARD            44 (to L17)

 295   L16:     LOAD_FAST_BORROW        11 (last_verified_dt)
                POP_JUMP_IF_NONE        41 (to L17)
                NOT_TAKEN

 296            LOAD_GLOBAL             21 (_now_dt + NULL)
                CALL                     0
                LOAD_FAST_BORROW        11 (last_verified_dt)
                BINARY_OP               10 (-)
                STORE_FAST              14 (age)

 297            LOAD_FAST_BORROW        14 (age)
                LOAD_GLOBAL             23 (timedelta + NULL)
                LOAD_GLOBAL             24 (_STALE_VERIFICATION_HOURS)
                LOAD_CONST              16 (('hours',))
                CALL_KW                  1
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN

 298            LOAD_CONST              14 (True)
                STORE_FAST              13 (action_required)

 301   L17:     LOAD_CONST              17 ('brokerage_id')
                LOAD_FAST                1 (bid)

 302            LOAD_CONST               6 ('latest_chain_status')
                LOAD_FAST                8 (latest_chain_status)

 303            LOAD_CONST               8 ('latest_verification_status')
                LOAD_FAST                9 (latest_verif_status)

 304            LOAD_CONST              10 ('last_verified_at')
                LOAD_FAST               10 (last_verified_at_str)

 305            LOAD_CONST              15 ('verification_count')
                LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         6 (history_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              15 ('verification_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L18:     CALL                     1

 306            LOAD_CONST              18 ('acknowledgement_count')
                LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         7 (non_rep_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              18 ('acknowledgement_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1

 307            LOAD_CONST              19 ('merkle_window_count')
                LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW         7 (non_rep_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              19 ('merkle_window_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        28 (to L20)
                NOT_TAKEN
                POP_TOP

 308            LOAD_FAST_BORROW         5 (chain_pl)
                LOAD_ATTR               15 (get + NULL|self)
                LOAD_CONST              19 ('merkle_window_count')
                CALL                     1

 307            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP

 308            LOAD_SMALL_INT           0

 307   L20:     CALL                     1

 309            LOAD_CONST              11 ('warning_count')
                LOAD_FAST_BORROW        12 (warning_count)

 310            LOAD_CONST              20 ('action_required')
                LOAD_GLOBAL             27 (bool + NULL)
                LOAD_FAST_BORROW        13 (action_required)
                CALL                     1

 300            BUILD_MAP                9
                STORE_FAST              15 (payload)

 313            LOAD_GLOBAL             28 (TENANT_DASHBOARD_PAYLOAD_KEYS)
                GET_ITER
                LOAD_FAST_AND_CLEAR     16 (k)
                SWAP                     2
       L21:     BUILD_MAP                0
                SWAP                     2
       L22:     FOR_ITER                22 (to L25)
                STORE_FAST              16 (k)
                LOAD_FAST_BORROW        16 (k)
                LOAD_FAST_BORROW        15 (payload)
                CONTAINS_OP              0 (in)
       L23:     POP_JUMP_IF_TRUE         3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           12 (to L22)
       L24:     LOAD_FAST_BORROW        16 (k)
                LOAD_FAST_BORROW        15 (payload)
                LOAD_FAST_BORROW        16 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           24 (to L22)
       L25:     END_FOR
                POP_ITER
       L26:     STORE_FAST              17 (bounded)
                STORE_FAST              16 (k)

 314            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 315            LOAD_CONST              21 ('ok')

 316            LOAD_FAST_BORROW         1 (bid)

 317            LOAD_FAST_BORROW        17 (bounded)

 314            LOAD_CONST              22 (('status', 'brokerage_id', 'payload'))
                CALL_KW                  3
                RETURN_VALUE

  --   L27:     SWAP                     2
                POP_TOP

 313            SWAP                     2
                STORE_FAST              16 (k)
                RERAISE                  0
ExceptionTable:
  L21 to L23 -> L27 [2]
  L24 to L26 -> L27 [2]
```
