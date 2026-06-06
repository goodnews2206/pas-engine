# operator/circuit_breaker_policy

- **pyc:** `app\services\operator\__pycache__\circuit_breaker_policy.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/circuit_breaker_policy.py`
- **co_filename (from bytecode):** `app\services\operator\circuit_breaker_policy.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS189 — Circuit-breaker policy (advisory read-through).

Thin **read-only** policy layer over PAS188's
``circuit_breaker`` ledger. Other parts of PAS call this
module to decide whether to block new outbound /
pending-call activity for a brokerage whose breaker is
TRIPPED.

Doctrine (sacrosanct):

* **Advisory only.** This module never trips, resets,
  or otherwise mutates breaker state. It only **reads**
  the most-recent ``pas_brokerage_circuit_breakers`` row
  via PAS188's ``current_breaker_state``.
* **No auto-trip.** PAS189 contains NO logic that
  observes a metric and trips a breaker. PAS surfaces
  never auto-trip.
* **No auto-reset.** PAS189 contains NO logic that
  observes a metric and resets a breaker.
* **No autonomous remediation.** Reading TRIPPED state
  causes upstream callers to return a structural skip /
  block envelope; this module itself takes NO further
  action. No retry queue. No paging. No notification.
* **Fail-open.** If the policy check raises for any
  reason (DB unavailable, import error, malformed row),
  the module returns ``should_block=False`` plus a
  ``policy_check_failed_fail_open`` warning. The
  doctrine prefers leads through over silently
  swallowing them.
* **No PII.** The envelope carries ``brokerage_id``,
  ``status``, ``reason_code``, ``warning_count``,
  ``error_code``, and a structural ``warnings`` list
  only.
* **NEVER raises.** Any internal exception collapses to
  a fail-open envelope.

Public surface:

  * ``brokerage_circuit_breaker_status(brokerage_id)``
        Returns the closed-projection state envelope.
  * ``should_block_new_outbound_for_brokerage(brokerage_id)``
        Returns a bool. ``True`` ONLY when the most-recent
        breaker row reports ``status == "TRIPPED"``. Fail-
        open: any policy failure returns ``False``.
  * ``circuit_breaker_public_warning(brokerage_id)``
        Returns a single short structural warning string
        ("brokerage_circuit_breaker_tripped" or ""), for
        callers that want to surface a warning to the
        operator UI.
  * ``circuit_breaker_policy_report(...)``
        Read-only fleet-wide policy summary suitable for
        the operator surface. Bounded.
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `Optional`, `__future__`, `annotations`, `app.services.operator.circuit_breaker`, `current_breaker_state`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_final`, `_project_state_row`, `_read_current_state`, `_safe_brokerage`, `_safe_brokerage_iter`, `_scan_for_forbidden`, `brokerage_circuit_breaker_status`, `circuit_breaker_policy_report`, `circuit_breaker_public_warning`, `should_block_new_outbound_for_brokerage`

## Env-key candidates

`TRIPPED`

## String constants (redacted where noted)

- '\nPAS189 — Circuit-breaker policy (advisory read-through).\n\nThin **read-only** policy layer over PAS188\'s\n``circuit_breaker`` ledger. Other parts of PAS call this\nmodule to decide whether to block new outbound /\npending-call activity for a brokerage whose breaker is\nTRIPPED.\n\nDoctrine (sacrosanct):\n\n* **Advisory only.** This module never trips, resets,\n  or otherwise mutates breaker state. It only **reads**\n  the most-recent ``pas_brokerage_circuit_breakers`` row\n  via PAS188\'s ``current_breaker_state``.\n* **No auto-trip.** PAS189 contains NO logic that\n  observes a metric and trips a breaker. PAS surfaces\n  never auto-trip.\n* **No auto-reset.** PAS189 contains NO logic that\n  observes a metric and resets a breaker.\n* **No autonomous remediation.** Reading TRIPPED state\n  causes upstream callers to return a structural skip /\n  block envelope; this module itself takes NO further\n  action. No retry queue. No paging. No notification.\n* **Fail-open.** If the policy check raises for any\n  reason (DB unavailable, import error, malformed row),\n  the module returns ``should_block=False`` plus a\n  ``policy_check_failed_fail_open`` warning. The\n  doctrine prefers leads through over silently\n  swallowing them.\n* **No PII.** The envelope carries ``brokerage_id``,\n  ``status``, ``reason_code``, ``warning_count``,\n  ``error_code``, and a structural ``warnings`` list\n  only.\n* **NEVER raises.** Any internal exception collapses to\n  a fail-open envelope.\n\nPublic surface:\n\n  * ``brokerage_circuit_breaker_status(brokerage_id)``\n        Returns the closed-projection state envelope.\n  * ``should_block_new_outbound_for_brokerage(brokerage_id)``\n        Returns a bool. ``True`` ONLY when the most-recent\n        breaker row reports ``status == "TRIPPED"``. Fail-\n        open: any policy failure returns ``False``.\n  * ``circuit_breaker_public_warning(brokerage_id)``\n        Returns a single short structural warning string\n        ("brokerage_circuit_breaker_tripped" or ""), for\n        callers that want to surface a warning to the\n        operator UI.\n  * ``circuit_breaker_policy_report(...)``\n        Read-only fleet-wide policy summary suitable for\n        the operator surface. Bounded.\n'
- 'pas.operator.circuit_breaker_policy'
- 'brokerage_circuit_breaker_tripped'
- 'policy_check_failed_fail_open'
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
- 'circuit_breaker_policy surface='
- ' collapsed — forbidden token leaked'
- 'status'
- 'failed'
- 'error_code'
- 'policy_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'brokerage_id'
- 'Optional[Dict[str, Any]]'
- 'Read the current breaker state via PAS188. Returns\nNone on any error (caller treats None as fail-open).'
- 'circuit_breaker_policy read brokerage='
- ' error type='
- 'Closed-projection state envelope for one brokerage.\n\nReturns::\n\n    {\n      "status":       "ok" | "skipped" | "failed",\n      "surface":      "ops.circuit_breaker.policy.status",\n      "brokerage_id": "<bid>",\n      "row":          { ...closed allow-list... },\n      "warnings":     [...],\n      "error_code":   null | "<closed code>",\n    }\n'
- 'ops.circuit_breaker.policy.status'
- 'invalid_brokerage_id'
- 'skipped'
- 'reason_code'
- 'policy_check_failed'
- 'brokerage_circuit_breaker_status error type='
- 'unexpected:'
- 'bool'
- 'Returns True ONLY when the most-recent breaker row\nreports ``status == "TRIPPED"``. Fail-open: any policy\nerror returns False.\n\nThis function is the canonical wire-through point for\nupstream callers (pending-call creation / outbound\ndial). It is read-only. It never raises. It never\nblocks on fail-open.\n'
- 'TRIPPED'
- 'should_block_new_outbound_for_brokerage error type='
- 'Returns a single short structural warning string for\noperator UI surfaces. Empty string when not tripped.'
- 'Fleet-wide policy summary. Composes per-brokerage\n``brokerage_circuit_breaker_status`` envelopes into a\nbounded report.'
- 'ops.circuit_breaker.policy.report'
- 'rows'
- 'count'
- 'no_brokerage_ids_supplied'
- 'tripped_count'
- 'circuit_breaker_policy_report error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS189 — Circuit-breaker policy (advisory read-through).\n\nThin **read-only** policy layer over PAS188\'s\n``circuit_breaker`` ledger. Other parts of PAS call this\nmodule to decide whether to block new outbound /\npending-call activity for a brokerage whose breaker is\nTRIPPED.\n\nDoctrine (sacrosanct):\n\n* **Advisory only.** This module never trips, resets,\n  or otherwise mutates breaker state. It only **reads**\n  the most-recent ``pas_brokerage_circuit_breakers`` row\n  via PAS188\'s ``current_breaker_state``.\n* **No auto-trip.** PAS189 contains NO logic that\n  observes a metric and trips a breaker. PAS surfaces\n  never auto-trip.\n* **No auto-reset.** PAS189 contains NO logic that\n  observes a metric and resets a breaker.\n* **No autonomous remediation.** Reading TRIPPED state\n  causes upstream callers to return a structural skip /\n  block envelope; this module itself takes NO further\n  action. No retry queue. No paging. No notification.\n* **Fail-open.** If the policy check raises for any\n  reason (DB unavailable, import error, malformed row),\n  the module returns ``should_block=False`` plus a\n  ``policy_check_failed_fail_open`` warning. The\n  doctrine prefers leads through over silently\n  swallowing them.\n* **No PII.** The envelope carries ``brokerage_id``,\n  ``status``, ``reason_code``, ``warning_count``,\n  ``error_code``, and a structural ``warnings`` list\n  only.\n* **NEVER raises.** Any internal exception collapses to\n  a fail-open envelope.\n\nPublic surface:\n\n  * ``brokerage_circuit_breaker_status(brokerage_id)``\n        Returns the closed-projection state envelope.\n  * ``should_block_new_outbound_for_brokerage(brokerage_id)``\n        Returns a bool. ``True`` ONLY when the most-recent\n        breaker row reports ``status == "TRIPPED"``. Fail-\n        open: any policy failure returns ``False``.\n  * ``circuit_breaker_public_warning(brokerage_id)``\n        Returns a single short structural warning string\n        ("brokerage_circuit_breaker_tripped" or ""), for\n        callers that want to surface a warning to the\n        operator UI.\n  * ``circuit_breaker_policy_report(...)``\n        Read-only fleet-wide policy summary suitable for\n        the operator surface. Bounded.\n')
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 59           LOAD_SMALL_INT           0
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

 62           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.operator.circuit_breaker_policy')
              CALL                     1
              STORE_NAME              11 (logger)

 69           LOAD_SMALL_INT         200
              STORE_NAME              12 (_BROKERAGE_ID_MAX_LEN)

 70           LOAD_SMALL_INT          50
              STORE_NAME              13 (_LIMIT_DEFAULT)

 71           LOAD_SMALL_INT           1
              STORE_NAME              14 (_LIMIT_MIN)

 72           LOAD_SMALL_INT         200
              STORE_NAME              15 (_LIMIT_MAX)

 74           LOAD_CONST               5 ('brokerage_circuit_breaker_tripped')
              STORE_NAME              16 (_WARNING_TRIPPED)

 75           LOAD_CONST               6 ('policy_check_failed_fail_open')
              STORE_NAME              17 (_WARNING_FAIL_OPEN)

 77           LOAD_CONST              29 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values', 'operator_notes'))
              STORE_NAME              18 (_FORBIDDEN_RESPONSE_TOKENS)

 85           LOAD_CONST              30 (('brokerage_id', 'status', 'reason_code'))
              STORE_NAME              19 (_STATE_ROW_ALLOWLIST)

 96           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\circuit_breaker_policy.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _safe_brokerage at 0x0000018C17F95CF0, file "app\services\operator\circuit_breaker_policy.py", line 96>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_safe_brokerage)

105           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\circuit_breaker_policy.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _safe_brokerage_iter at 0x0000018C180488F0, file "app\services\operator\circuit_breaker_policy.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_safe_brokerage_iter)

120           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\circuit_breaker_policy.py", line 120>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scan_for_forbidden at 0x0000018C18025530, file "app\services\operator\circuit_breaker_policy.py", line 120>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_scan_for_forbidden)

144           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025130, file "app\services\operator\circuit_breaker_policy.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _final at 0x0000018C17FE1680, file "app\services\operator\circuit_breaker_policy.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_final)

160           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\circuit_breaker_policy.py", line 160>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _project_state_row at 0x0000018C18053630, file "app\services\operator\circuit_breaker_policy.py", line 160>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_project_state_row)

168           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\circuit_breaker_policy.py", line 168>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _read_current_state at 0x0000018C179A7290, file "app\services\operator\circuit_breaker_policy.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_read_current_state)

194           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\circuit_breaker_policy.py", line 194>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object brokerage_circuit_breaker_status at 0x0000018C17D78310, file "app\services\operator\circuit_breaker_policy.py", line 194>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (brokerage_circuit_breaker_status)

255           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\circuit_breaker_policy.py", line 255>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object should_block_new_outbound_for_brokerage at 0x0000018C17CC1F60, file "app\services\operator\circuit_breaker_policy.py", line 255>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (should_block_new_outbound_for_brokerage)

286           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\circuit_breaker_policy.py", line 286>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object circuit_breaker_public_warning at 0x0000018C1802C9B0, file "app\services\operator\circuit_breaker_policy.py", line 286>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (circuit_breaker_public_warning)

295           LOAD_CONST              25 ('brokerage_ids')

297           LOAD_CONST               2 (None)

295           LOAD_CONST              26 ('limit')

298           LOAD_NAME               13 (_LIMIT_DEFAULT)

295           BUILD_MAP                2
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\circuit_breaker_policy.py", line 295>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object circuit_breaker_policy_report at 0x0000018C17E7F990, file "app\services\operator\circuit_breaker_policy.py", line 295>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (circuit_breaker_policy_report)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\operator\circuit_breaker_policy.py", line 96>:
 96           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F95CF0, file "app\services\operator\circuit_breaker_policy.py", line 96>:
 96           RESUME                   0

 97           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 98           LOAD_CONST               0 (None)
              RETURN_VALUE

 99   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

100           LOAD_FAST_BORROW         1 (s)
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

101   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

102   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\operator\circuit_breaker_policy.py", line 105>:
105           RESUME                   0
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

Disassembly of <code object _safe_brokerage_iter at 0x0000018C180488F0, file "app\services\operator\circuit_breaker_policy.py", line 105>:
105           RESUME                   0

106           LOAD_FAST_BORROW         0 (brokerage_ids)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

107           BUILD_LIST               0
              RETURN_VALUE

108   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

109           LOAD_GLOBAL              1 (set + NULL)
              CALL                     0
              STORE_FAST               2 (seen)

110           LOAD_FAST_BORROW         0 (brokerage_ids)
              GET_ITER
      L2:     FOR_ITER                85 (to L5)
              STORE_FAST               3 (v)

111           LOAD_GLOBAL              3 (_safe_brokerage + NULL)
              LOAD_FAST_BORROW         3 (v)
              CALL                     1
              STORE_FAST               4 (s)

112           LOAD_FAST_BORROW         4 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       41 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (s, seen)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       35 (to L3)
              NOT_TAKEN

113           LOAD_FAST_BORROW         2 (seen)
              LOAD_ATTR                5 (add + NULL|self)
              LOAD_FAST_BORROW         4 (s)
              CALL                     1
              POP_TOP

114           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         4 (s)
              CALL                     1
              POP_TOP

115   L3:     LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              LOAD_GLOBAL             10 (_LIMIT_MAX)
              COMPARE_OP             188 (bool(>=))
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           84 (to L2)

116   L4:     POP_TOP

117           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

110   L5:     END_FOR
              POP_ITER

117           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\circuit_breaker_policy.py", line 120>:
120           RESUME                   0
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

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025530, file "app\services\operator\circuit_breaker_policy.py", line 120>:
  --           MAKE_CELL                1 (walk)

 120           RESUME                   0

 121           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\circuit_breaker_policy.py", line 121>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC1CE0, file "app\services\operator\circuit_breaker_policy.py", line 121>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 141           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\operator\circuit_breaker_policy.py", line 121>:
121           RESUME                   0
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

Disassembly of <code object walk at 0x0000018C17CC1CE0, file "app\services\operator\circuit_breaker_policy.py", line 121>:
  --            COPY_FREE_VARS           1

 121            RESUME                   0

 122            NOP

 123    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 124    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 125            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 126            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 127            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 128            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 129    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 127    L9:     END_FOR
                POP_ITER

 130   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 131            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 132   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 124   L14:     END_FOR
                POP_ITER

 140   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 133   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 134            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 135            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 136            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 137   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 134   L21:     END_FOR
                POP_ITER

 140   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 138            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 139   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 138   L25:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\operator\circuit_breaker_policy.py", line 144>:
144           RESUME                   0
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

Disassembly of <code object _final at 0x0000018C17FE1680, file "app\services\operator\circuit_breaker_policy.py", line 144>:
144           RESUME                   0

145           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

146           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

147           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

148           LOAD_CONST               0 ('circuit_breaker_policy surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

147           CALL                     1
              POP_TOP

152           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

153           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

154           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('policy_envelope_forbidden_token')

155           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('policy_envelope_forbidden_token')
              BUILD_LIST               1

151           BUILD_MAP                4
              RETURN_VALUE

157   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\operator\circuit_breaker_policy.py", line 160>:
160           RESUME                   0
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

Disassembly of <code object _project_state_row at 0x0000018C18053630, file "app\services\operator\circuit_breaker_policy.py", line 160>:
160           RESUME                   0

161           BUILD_MAP                0
              STORE_FAST               1 (out)

162           LOAD_GLOBAL              0 (_STATE_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

163           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

164   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

162   L3:     END_FOR
              POP_ITER

165           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app\services\operator\circuit_breaker_policy.py", line 168>:
168           RESUME                   0
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
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_current_state at 0x0000018C179A7290, file "app\services\operator\circuit_breaker_policy.py", line 168>:
 168            RESUME                   0

 171            NOP

 172    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('current_breaker_state',))
                IMPORT_NAME              0 (app.services.operator.circuit_breaker)
                IMPORT_FROM              1 (current_breaker_state)
                STORE_FAST               1 (current_breaker_state)
                POP_TOP

 177    L2:     NOP

 178    L3:     LOAD_FAST                1 (current_breaker_state)
                PUSH_NULL
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               3 (('brokerage_id',))
                CALL_KW                  1
                STORE_FAST               2 (env)

 185    L4:     LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                2 (env)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 186            LOAD_CONST               2 (None)
                RETURN_VALUE

 187    L5:     LOAD_FAST                2 (env)
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 175            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L8)
                NOT_TAKEN
                POP_TOP

 176    L7:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 175    L8:     RERAISE                  0

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 179            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       65 (to L14)
                NOT_TAKEN
                STORE_FAST               3 (e)

 180   L11:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 181            LOAD_CONST               4 ('circuit_breaker_policy read brokerage=')
                LOAD_FAST                0 (brokerage_id)
                LOAD_CONST               5 (slice(None, 32, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST               6 (' error type=')

 182            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 181            BUILD_STRING             4

 180            CALL                     1
                POP_TOP

 184   L12:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L13:     LOAD_CONST               2 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 179   L14:     RERAISE                  0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\operator\circuit_breaker_policy.py", line 194>:
194           RESUME                   0
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

Disassembly of <code object brokerage_circuit_breaker_status at 0x0000018C17D78310, file "app\services\operator\circuit_breaker_policy.py", line 194>:
 194            RESUME                   0

 208            LOAD_CONST               1 ('ops.circuit_breaker.policy.status')
                STORE_FAST               1 (surface)

 209            NOP

 210    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               2 (bid)

 211            LOAD_FAST_BORROW         2 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 212            LOAD_GLOBAL              3 (_final + NULL)

 213            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 214            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 215            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 216            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 212            BUILD_MAP                4

 217            LOAD_FAST_BORROW         1 (surface)

 212            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 218    L3:     LOAD_GLOBAL              5 (_read_current_state + NULL)
                LOAD_FAST_BORROW         2 (bid)
                CALL                     1
                STORE_FAST               3 (env)

 219            LOAD_FAST_BORROW         3 (env)
                POP_JUMP_IF_NOT_NONE    37 (to L5)
                NOT_TAKEN

 221            LOAD_GLOBAL              3 (_final + NULL)

 222            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 223            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         1 (surface)

 224            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 225            LOAD_CONST              12 ('row')

 226            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)

 227            LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('OK')

 228            LOAD_CONST              14 ('reason_code')
                LOAD_CONST               9 (None)

 225            BUILD_MAP                3

 230            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL              6 (_WARNING_FAIL_OPEN)
                BUILD_LIST               1

 231            LOAD_CONST               5 ('error_code')
                LOAD_CONST              15 ('policy_check_failed')

 221            BUILD_MAP                6

 232            LOAD_FAST_BORROW         1 (surface)

 221            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L4:     RETURN_VALUE

 233    L5:     LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              12 ('row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_MAP                0
        L8:     STORE_FAST               4 (row)

 234            LOAD_GLOBAL              3 (_final + NULL)

 235            LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               2 ('status')
                LOAD_CONST              16 ('ok')
                CALL                     2

 236            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 237            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST                2 (bid)

 238            LOAD_CONST              12 ('row')
                LOAD_GLOBAL             11 (_project_state_row + NULL)
                LOAD_FAST_BORROW         4 (row)
                CALL                     1

 239            LOAD_CONST               7 ('warnings')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                BUILD_LIST               0
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                BUILD_LIST               0

 240   L11:     LOAD_CONST               5 ('error_code')
                LOAD_FAST_BORROW         3 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               5 ('error_code')
                CALL                     1

 234            BUILD_MAP                6

 241            LOAD_FAST_BORROW         1 (surface)

 234            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 242            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      102 (to L18)
                NOT_TAKEN
                STORE_FAST               5 (e)

 243   L14:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 244            LOAD_CONST              17 ('brokerage_circuit_breaker_status error type=')

 245            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 244            BUILD_STRING             2

 243            CALL                     1
                POP_TOP

 247            LOAD_GLOBAL              3 (_final + NULL)

 248            LOAD_CONST               2 ('status')
                LOAD_CONST              10 ('skipped')

 249            LOAD_CONST               4 ('surface')
                LOAD_FAST                1 (surface)

 250            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL              6 (_WARNING_FAIL_OPEN)
                BUILD_LIST               1

 251            LOAD_CONST               5 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 247            BUILD_MAP                4

 252            LOAD_FAST                1 (surface)

 247            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L17:     LOAD_CONST               9 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 242   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L4 -> L13 [0]
  L5 to L6 -> L13 [0]
  L7 to L9 -> L13 [0]
  L10 to L12 -> L13 [0]
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L17 [1] lasti
  L15 to L16 -> L19 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\operator\circuit_breaker_policy.py", line 255>:
255           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object should_block_new_outbound_for_brokerage at 0x0000018C17CC1F60, file "app\services\operator\circuit_breaker_policy.py", line 255>:
 255            RESUME                   0

 265            NOP

 266    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               1 (bid)

 267            LOAD_FAST_BORROW         1 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 268    L2:     LOAD_CONST               1 (False)
                RETURN_VALUE

 269    L3:     LOAD_GLOBAL              3 (_read_current_state + NULL)
                LOAD_FAST_BORROW         1 (bid)
                CALL                     1
                STORE_FAST               2 (env)

 270            LOAD_FAST_BORROW         2 (env)
                POP_JUMP_IF_NOT_NONE     3 (to L5)
                NOT_TAKEN

 271    L4:     LOAD_CONST               1 (False)
                RETURN_VALUE

 274    L5:     LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1
                LOAD_CONST               4 ('skipped')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 275    L6:     LOAD_CONST               1 (False)
                RETURN_VALUE

 276    L7:     LOAD_FAST_BORROW         2 (env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_MAP                0
       L10:     STORE_FAST               3 (row)

 277            LOAD_GLOBAL              7 (str + NULL)
                LOAD_FAST_BORROW         3 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_CONST               6 ('')
       L13:     CALL                     1
                LOAD_ATTR                9 (upper + NULL|self)
                CALL                     0
                LOAD_CONST               7 ('TRIPPED')
                COMPARE_OP              72 (==)
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 278            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L19)
                NOT_TAKEN
                STORE_FAST               4 (e)

 279   L16:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 280            LOAD_CONST               8 ('should_block_new_outbound_for_brokerage error type=')

 281            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 280            BUILD_STRING             2

 279            CALL                     1
                POP_TOP

 283   L17:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                LOAD_CONST               1 (False)
                RETURN_VALUE

  --   L18:     LOAD_CONST               2 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 278   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L15 [0]
  L3 to L4 -> L15 [0]
  L5 to L6 -> L15 [0]
  L7 to L8 -> L15 [0]
  L9 to L11 -> L15 [0]
  L12 to L14 -> L15 [0]
  L15 to L16 -> L20 [1] lasti
  L16 to L17 -> L18 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app\services\operator\circuit_breaker_policy.py", line 286>:
286           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object circuit_breaker_public_warning at 0x0000018C1802C9B0, file "app\services\operator\circuit_breaker_policy.py", line 286>:
 286           RESUME                   0

 289           NOP

 290   L1:     LOAD_GLOBAL              1 (should_block_new_outbound_for_brokerage + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN
               LOAD_GLOBAL              2 (_WARNING_TRIPPED)
       L2:     RETURN_VALUE
       L3:     LOAD_CONST               1 ('')
       L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 291           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 292   L6:     POP_EXCEPT
               LOAD_CONST               1 ('')
               RETURN_VALUE

 291   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\operator\circuit_breaker_policy.py", line 295>:
295           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

297           LOAD_CONST               2 ('Optional[Iterable[Any]]')

295           LOAD_CONST               3 ('limit')

298           LOAD_CONST               4 ('Any')

295           LOAD_CONST               5 ('return')

299           LOAD_CONST               6 ('Dict[str, Any]')

295           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object circuit_breaker_policy_report at 0x0000018C17E7F990, file "app\services\operator\circuit_breaker_policy.py", line 295>:
 295            RESUME                   0

 303            LOAD_CONST               1 ('ops.circuit_breaker.policy.report')
                STORE_FAST               2 (surface)

 304            NOP

 305            NOP

 306    L1:     LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         1 (limit)
                CALL                     1
                STORE_FAST               3 (cap)

 309    L2:     LOAD_FAST_BORROW         3 (cap)
                LOAD_GLOBAL              8 (_LIMIT_MIN)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        7 (to L3)
                NOT_TAKEN

 310            LOAD_GLOBAL              8 (_LIMIT_MIN)
                STORE_FAST               3 (cap)

 311    L3:     LOAD_FAST_BORROW         3 (cap)
                LOAD_GLOBAL             10 (_LIMIT_MAX)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        7 (to L4)
                NOT_TAKEN

 312            LOAD_GLOBAL             10 (_LIMIT_MAX)
                STORE_FAST               3 (cap)

 313    L4:     LOAD_GLOBAL             13 (_safe_brokerage_iter + NULL)
                LOAD_FAST_BORROW         0 (brokerage_ids)
                CALL                     1
                STORE_FAST               4 (explicit)

 314            LOAD_FAST_BORROW         4 (explicit)
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L6)
                NOT_TAKEN

 318            LOAD_GLOBAL             15 (_final + NULL)

 319            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('ok')

 320            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 321            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 322            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 323            LOAD_CONST               7 ('warnings')
                LOAD_CONST               8 ('no_brokerage_ids_supplied')
                BUILD_LIST               1

 324            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 (None)

 318            BUILD_MAP                6

 325            LOAD_FAST_BORROW         2 (surface)

 318            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
        L5:     RETURN_VALUE

 326    L6:     LOAD_FAST_BORROW         4 (explicit)
                LOAD_CONST              10 (None)
                LOAD_FAST_BORROW         3 (cap)
                BINARY_SLICE
                STORE_FAST               4 (explicit)

 327            BUILD_LIST               0
                STORE_FAST               5 (rows)

 328            LOAD_SMALL_INT           0
                STORE_FAST               6 (tripped_count)

 329            LOAD_FAST_BORROW         4 (explicit)
                GET_ITER
        L7:     FOR_ITER               155 (to L18)
                STORE_FAST               7 (bid)

 330            LOAD_GLOBAL             17 (brokerage_circuit_breaker_status + NULL)
                LOAD_FAST_BORROW         7 (bid)
                CALL                     1
                STORE_FAST               8 (env)

 331            LOAD_FAST_BORROW         8 (env)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              12 ('row')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_MAP                0
       L10:     STORE_FAST               9 (row)

 332            LOAD_GLOBAL             21 (str + NULL)
                LOAD_FAST_BORROW         9 (row)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_CONST              13 ('')
       L13:     CALL                     1
                LOAD_ATTR               23 (upper + NULL|self)
                CALL                     0
                STORE_FAST              10 (status)

 333            LOAD_FAST_BORROW        10 (status)
                LOAD_CONST              14 ('TRIPPED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       10 (to L14)
                NOT_TAKEN

 334            LOAD_FAST_BORROW         6 (tripped_count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               6 (tripped_count)

 335   L14:     LOAD_FAST                5 (rows)
                LOAD_ATTR               25 (append + NULL|self)

 336            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST                7 (bid)

 337            LOAD_CONST               2 ('status')
                LOAD_FAST               10 (status)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                LOAD_CONST              16 ('OK')

 338   L17:     LOAD_CONST              17 ('reason_code')
                LOAD_FAST_BORROW         9 (row)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST              17 ('reason_code')
                CALL                     1

 335            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          157 (to L7)

 329   L18:     END_FOR
                POP_ITER

 340            LOAD_GLOBAL             15 (_final + NULL)

 341            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('ok')

 342            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 343            LOAD_CONST               6 ('count')
                LOAD_GLOBAL             27 (len + NULL)
                LOAD_FAST_BORROW         5 (rows)
                CALL                     1

 344            LOAD_CONST              18 ('tripped_count')
                LOAD_FAST_BORROW         6 (tripped_count)

 345            LOAD_CONST               5 ('rows')
                LOAD_FAST_BORROW         5 (rows)

 346            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 347            LOAD_CONST               9 ('error_code')
                LOAD_CONST              10 (None)

 340            BUILD_MAP                7

 348            LOAD_FAST_BORROW         2 (surface)

 340            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 307            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L22)
                NOT_TAKEN
                POP_TOP

 308            LOAD_GLOBAL              6 (_LIMIT_DEFAULT)
                STORE_FAST               3 (cap)
       L21:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 311 (to L2)

 307   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L24:     PUSH_EXC_INFO

 349            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      106 (to L29)
                NOT_TAKEN
                STORE_FAST              11 (e)

 350   L25:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 351            LOAD_CONST              19 ('circuit_breaker_policy_report error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 350            CALL                     1
                POP_TOP

 353            LOAD_GLOBAL             15 (_final + NULL)

 354            LOAD_CONST               2 ('status')
                LOAD_CONST              20 ('skipped')

 355            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 356            LOAD_CONST               5 ('rows')
                BUILD_LIST               0

 357            LOAD_CONST               6 ('count')
                LOAD_SMALL_INT           0

 358            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             38 (_WARNING_FAIL_OPEN)
                BUILD_LIST               1

 359            LOAD_CONST               9 ('error_code')
                LOAD_CONST              21 ('unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 353            BUILD_MAP                6

 360            LOAD_FAST                2 (surface)

 353            LOAD_CONST              11 (('surface',))
                CALL_KW                  2
       L26:     SWAP                     2
       L27:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L28:     LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 349   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L20 [0]
  L2 to L5 -> L24 [0]
  L6 to L8 -> L24 [0]
  L9 to L11 -> L24 [0]
  L12 to L15 -> L24 [0]
  L16 to L19 -> L24 [0]
  L20 to L21 -> L23 [1] lasti
  L21 to L22 -> L24 [0]
  L22 to L23 -> L23 [1] lasti
  L23 to L24 -> L24 [0]
  L24 to L25 -> L30 [1] lasti
  L25 to L26 -> L28 [1] lasti
  L26 to L27 -> L30 [1] lasti
  L28 to L30 -> L30 [1] lasti
```
