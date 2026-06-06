# ingestion/worker

- **pyc:** `app\services\ingestion\__pycache__\worker.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/worker.py`
- **co_filename (from bytecode):** `app\services\ingestion\worker.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS162 — Pending-call auto-dial worker.

Doctrine:

* **Off by default.** The worker only runs when the strict
  ``PENDING_CALLS_WORKER_ENABLED`` boolean is set.
  Acceptable enable forms:
    - config dict with the **literal Python ``True``** value
      (``{"PENDING_CALLS_WORKER_ENABLED": True}``),
    - environment variable with the **exact lower-case string
      ``"true"``** (``PENDING_CALLS_WORKER_ENABLED=true``).
  Anything else — ``"True"``, ``"1"``, ``"yes"``, ``True``-ish
  string with whitespace, integer ``1``, etc. — is treated as
  disabled.

* **Operator-run CLI only in this phase.** The worker is NOT
  scheduled by the FastAPI application's startup events. There
  is no background loop inside the web process. The companion
  CLI ``scripts/run_pending_calls_worker.py`` is the operator's
  trigger.

* **No fake success.** If the actual outbound-dial adapter is
  not wired in this build, the worker emits the structural
  warning ``outbound_dial_adapter_missing`` and marks the row
  FAILED. It NEVER returns DIALED unless the adapter actually
  placed the call.

* **No raw payload anywhere.** Logs use structural identifiers
  only (pending_call_id, source, error code class). The
  ``build_outbound_call_payload`` helper hands the dial adapter
  the minimum field set the existing LeadPayload shape needs;
  the worker NEVER prints / logs the phone / email / name.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.ingestion.pending_calls`, `app.services.outbound.dial`, `list_due_pending_calls`, `logging`, `mark_pending_call_dialed`, `mark_pending_call_dialing`, `mark_pending_call_failed`, `os`, `place_outbound_call`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_resolve_outbound_dial_adapter`, `build_outbound_call_payload`, `dry_run_pending_calls`, `pending_calls_worker_enabled`, `process_pending_call`, `run_pending_calls_once`

## Env-key candidates

`PENDING_CALLS_WORKER_ENABLED`

## String constants (redacted where noted)

- '\nPAS162 — Pending-call auto-dial worker.\n\nDoctrine:\n\n* **Off by default.** The worker only runs when the strict\n  ``PENDING_CALLS_WORKER_ENABLED`` boolean is set.\n  Acceptable enable forms:\n    - config dict with the **literal Python ``True``** value\n      (``{"PENDING_CALLS_WORKER_ENABLED": True}``),\n    - environment variable with the **exact lower-case string\n      ``"true"``** (``PENDING_CALLS_WORKER_ENABLED=true``).\n  Anything else — ``"True"``, ``"1"``, ``"yes"``, ``True``-ish\n  string with whitespace, integer ``1``, etc. — is treated as\n  disabled.\n\n* **Operator-run CLI only in this phase.** The worker is NOT\n  scheduled by the FastAPI application\'s startup events. There\n  is no background loop inside the web process. The companion\n  CLI ``scripts/run_pending_calls_worker.py`` is the operator\'s\n  trigger.\n\n* **No fake success.** If the actual outbound-dial adapter is\n  not wired in this build, the worker emits the structural\n  warning ``outbound_dial_adapter_missing`` and marks the row\n  FAILED. It NEVER returns DIALED unless the adapter actually\n  placed the call.\n\n* **No raw payload anywhere.** Logs use structural identifiers\n  only (pending_call_id, source, error code class). The\n  ``build_outbound_call_payload`` helper hands the dial adapter\n  the minimum field set the existing LeadPayload shape needs;\n  the worker NEVER prints / logs the phone / email / name.\n'
- 'pas.ingestion.worker'
- 'PENDING_CALLS_WORKER_ENABLED'
- 'true'
- 'enabled_override'
- 'config_or_env'
- 'Any'
- 'return'
- 'bool'
- 'Return True only on the strict enable form.\n\nAccepts either:\n  * a config dict — must contain ``PENDING_CALLS_WORKER_\n    ENABLED`` set to the literal Python boolean ``True``.\n    Anything else (including ``"true"`` string, ``1`` int)\n    is disabled.\n  * ``None`` (default) — reads ``os.environ``. The env var\n    must equal the exact lower-case string ``"true"``.\n\nStrict-by-design — half-true / typo / casing variants all\ndisable the worker. The cost of accidentally enabling\nTwilio dial in production is far higher than the cost of\nrequiring a precise enable form.\n'
- "Resolve a callable that places the outbound Twilio call.\n\nPAS163 wires ``app/services/outbound/dial.py:place_outbound_\ncall`` into this resolver. The function is reachable as a\nplain Python callable (no FastAPI request forging), so the\nworker can dial directly without weakening the existing\n``POST /outbound/call`` route's rate-limit + auth gates.\n\nWhen the module is missing or the symbol is not callable,\nthe resolver returns ``None`` and the worker surfaces\n``outbound_dial_adapter_missing`` rather than fabricating\nsuccess.\n"
- 'pending_call_row'
- 'Dict[str, Any]'
- 'brokerage_row'
- 'Optional[Dict[str, Any]]'
- 'Project a pending-call row into the dict shape the\nexisting outbound dial path expects.\n\nThe output mirrors ``app/routes/outbound.py:LeadPayload``\nbut is a plain dict (no Pydantic validation) so the\nadapter can decide whether to validate. We never copy the\nraw ``metadata`` JSONB unmodified; we lift only the\nclosed-allow-list metadata keys the normalizer permitted.\n\n``brokerage_row`` is optional — currently unused but kept\nin the signature so a future adapter that wants to read\ne.g. ``twilio_phone`` per tenant has the seat.\n'
- 'metadata'
- 'phone'
- 'lead_phone'
- 'brokerage_id'
- 'name'
- 'lead_name'
- 'email'
- 'lead_email'
- 'intent'
- 'budget'
- 'timeline'
- 'source'
- 'pending_call_worker'
- 'property_interest'
- 'property_address'
- 'row'
- 'worker_id'
- 'Optional[str]'
- 'Process a single due pending-call row.\n\nLifecycle:\n  1. mark DIALING (pin tenant).\n  2. resolve outbound dial adapter.\n  3. if adapter missing → mark FAILED with\n     ``outbound_dial_adapter_missing`` and return warning.\n  4. if adapter call raises → mark FAILED with\n     ``outbound_dial_failed:<Type>`` (class name only).\n  5. if adapter returns success → mark DIALED with the\n     call_sid surfaced in the envelope.\n\nReturns a closed-shape per-row result. Never raises.\nPhone / email / name never appear in this result.\n'
- 'pending_call_id'
- 'attempts'
- 'max_attempts'
- 'attempt'
- 'status'
- 'failed'
- 'warnings'
- 'error_code'
- 'call_sid'
- 'invalid_row_shape'
- 'lock_failed'
- 'outbound_dial_adapter_missing'
- 'outbound_dial_failed:'
- 'pending_call adapter exception id='
- ' type='
- 'outbound_dial_adapter_bad_return'
- 'dialed'
- 'outbound_dial_missing_call_sid'
- 'outbound_dial_returned_non_success'
- 'limit'
- 'Optional[bool]'
- 'Drain at most ``limit`` due pending-call rows. Disabled\nby default — caller must either set\n``PENDING_CALLS_WORKER_ENABLED=true`` in the env OR pass\n``enabled_override=True`` (for the CLI dry-run path that\ndeliberately bypasses the flag for inspection).\n\nReturns::\n\n    {\n      "status":  "ok" | "disabled" | "warning" | "failed",\n      "checked": <int>,        # rows considered\n      "dialed":  <int>,        # rows DIALED\n      "failed":  <int>,        # rows FAILED\n      "results": [\n        {\n          "pending_call_id": ...,\n          "source":          ...,\n          "attempt":         ...,\n          "max_attempts":    ...,\n          "status":          "dialed" | "failed",\n          "error_code":      None | "<structural-token>",\n          "warnings":        [...],\n          "call_sid":        None | "<str>",\n        },\n        ...\n      ],\n    }\n\nNever raises. Never logs raw phone/email/name.\n'
- 'pas162-worker-'
- 'disabled'
- 'checked'
- 'results'
- 'worker_disabled_by_flag'
- 'run_pending_calls_once list_due failed type='
- 'list_due_failed:'
- 'warning'
- "List due pending-call rows WITHOUT mutating anything.\nPhone / email / name are NEVER returned. Returns a\nstructural summary suitable for CLI print.\n\nUsed by the CLI's ``--dry-run`` mode to preview what would\nbe dialed if the flag were on.\n"
- 'pas162-dry-'
- 'next_attempt_at'
- 'dry_run'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS162 — Pending-call auto-dial worker.\n\nDoctrine:\n\n* **Off by default.** The worker only runs when the strict\n  ``PENDING_CALLS_WORKER_ENABLED`` boolean is set.\n  Acceptable enable forms:\n    - config dict with the **literal Python ``True``** value\n      (``{"PENDING_CALLS_WORKER_ENABLED": True}``),\n    - environment variable with the **exact lower-case string\n      ``"true"``** (``PENDING_CALLS_WORKER_ENABLED=true``).\n  Anything else — ``"True"``, ``"1"``, ``"yes"``, ``True``-ish\n  string with whitespace, integer ``1``, etc. — is treated as\n  disabled.\n\n* **Operator-run CLI only in this phase.** The worker is NOT\n  scheduled by the FastAPI application\'s startup events. There\n  is no background loop inside the web process. The companion\n  CLI ``scripts/run_pending_calls_worker.py`` is the operator\'s\n  trigger.\n\n* **No fake success.** If the actual outbound-dial adapter is\n  not wired in this build, the worker emits the structural\n  warning ``outbound_dial_adapter_missing`` and marks the row\n  FAILED. It NEVER returns DIALED unless the adapter actually\n  placed the call.\n\n* **No raw payload anywhere.** Logs use structural identifiers\n  only (pending_call_id, source, error code class). The\n  ``build_outbound_call_payload`` helper hands the dial adapter\n  the minimum field set the existing LeadPayload shape needs;\n  the worker NEVER prints / logs the phone / email / name.\n')
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
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 40           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (uuid)
              STORE_NAME               5 (uuid)

 41           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 43           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('list_due_pending_calls', 'mark_pending_call_dialed', 'mark_pending_call_dialing', 'mark_pending_call_failed'))
              IMPORT_NAME             11 (app.services.ingestion.pending_calls)
              IMPORT_FROM             12 (list_due_pending_calls)
              STORE_NAME              12 (list_due_pending_calls)
              IMPORT_FROM             13 (mark_pending_call_dialed)
              STORE_NAME              13 (mark_pending_call_dialed)
              IMPORT_FROM             14 (mark_pending_call_dialing)
              STORE_NAME              14 (mark_pending_call_dialing)
              IMPORT_FROM             15 (mark_pending_call_failed)
              STORE_NAME              15 (mark_pending_call_failed)
              POP_TOP

 50           LOAD_NAME                3 (logging)
              LOAD_ATTR               32 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.ingestion.worker')
              CALL                     1
              STORE_NAME              17 (logger)

 54           LOAD_CONST               6 ('PENDING_CALLS_WORKER_ENABLED')
              STORE_NAME              18 (_ENV_FLAG_NAME)

 55           LOAD_CONST               7 ('true')
              STORE_NAME              19 (_ENV_FLAG_ENABLED_LITERAL)

 58           LOAD_CONST              20 ((None,))
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\worker.py", line 58>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object pending_calls_worker_enabled at 0x0000018C1796DBD0, file "app\services\ingestion\worker.py", line 58>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (pending_calls_worker_enabled)

 91           LOAD_CONST              10 (<code object _resolve_outbound_dial_adapter at 0x0000018C1802C4F0, file "app\services\ingestion\worker.py", line 91>)
              MAKE_FUNCTION
              STORE_NAME              21 (_resolve_outbound_dial_adapter)

114           LOAD_CONST              20 ((None,))
              LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\worker.py", line 114>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object build_outbound_call_payload at 0x0000018C17D78680, file "app\services\ingestion\worker.py", line 114>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              22 (build_outbound_call_payload)

159           LOAD_CONST              20 ((None,))
              LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18025930, file "app\services\ingestion\worker.py", line 159>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object process_pending_call at 0x0000018C17ED78C0, file "app\services\ingestion\worker.py", line 159>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              23 (process_pending_call)

310           LOAD_CONST              21 ((25, None))
              LOAD_CONST              15 ('enabled_override')

314           LOAD_CONST               2 (None)

310           BUILD_MAP                1
              LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\worker.py", line 310>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object run_pending_calls_once at 0x0000018C17ED8380, file "app\services\ingestion\worker.py", line 310>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              24 (run_pending_calls_once)

439           LOAD_CONST              21 ((25, None))
              LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\worker.py", line 439>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object dry_run_pending_calls at 0x0000018C17EDAAF0, file "app\services\ingestion\worker.py", line 439>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              25 (dry_run_pending_calls)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\worker.py", line 58>:
 58           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')

 59           LOAD_CONST               2 ('Any')

 58           LOAD_CONST               3 ('return')

 60           LOAD_CONST               4 ('bool')

 58           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object pending_calls_worker_enabled at 0x0000018C1796DBD0, file "app\services\ingestion\worker.py", line 58>:
 58           RESUME                   0

 76           LOAD_FAST_BORROW         0 (config_or_env)
              POP_JUMP_IF_NOT_NONE    45 (to L1)
              NOT_TAKEN

 77           LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_ENV_FLAG_NAME)
              CALL                     1
              STORE_FAST               1 (raw)

 78           LOAD_FAST_BORROW         1 (raw)
              LOAD_GLOBAL              8 (_ENV_FLAG_ENABLED_LITERAL)
              COMPARE_OP              72 (==)
              RETURN_VALUE

 79   L1:     LOAD_GLOBAL             11 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL             12 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       26 (to L2)
              NOT_TAKEN

 80           LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_ENV_FLAG_NAME)
              CALL                     1
              STORE_FAST               2 (val)

 81           LOAD_FAST_BORROW         2 (val)
              LOAD_CONST               1 (True)
              IS_OP                    0 (is)
              RETURN_VALUE

 84   L2:     LOAD_CONST               2 (False)
              RETURN_VALUE

Disassembly of <code object _resolve_outbound_dial_adapter at 0x0000018C1802C4F0, file "app\services\ingestion\worker.py", line 91>:
  91           RESUME                   0

 105           NOP

 106   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('place_outbound_call',))
               IMPORT_NAME              0 (app.services.outbound.dial)
               IMPORT_FROM              1 (place_outbound_call)
               STORE_FAST               0 (place_outbound_call)
               POP_TOP

 107           LOAD_GLOBAL              5 (callable + NULL)
               LOAD_FAST_BORROW         0 (place_outbound_call)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 108           LOAD_FAST_BORROW         0 (place_outbound_call)
       L2:     RETURN_VALUE

 107   L3:     NOP

 111           LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 109           LOAD_GLOBAL              6 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 110   L5:     POP_EXCEPT

 111           LOAD_CONST               2 (None)
               RETURN_VALUE

 109   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\worker.py", line 114>:
114           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('pending_call_row')

115           LOAD_CONST               2 ('Dict[str, Any]')

114           LOAD_CONST               3 ('brokerage_row')

116           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

114           LOAD_CONST               5 ('return')

117           LOAD_CONST               2 ('Dict[str, Any]')

114           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_outbound_call_payload at 0x0000018C17D78680, file "app\services\ingestion\worker.py", line 114>:
114            RESUME                   0

131            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

132            BUILD_MAP                0
               RETURN_VALUE

133    L1:     LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('metadata')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     STORE_FAST               2 (metadata_in)

134            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (metadata_in)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

135            BUILD_MAP                0
               STORE_FAST               2 (metadata_in)

136    L3:     BUILD_MAP                0
               STORE_FAST               3 (safe_meta)

137            LOAD_CONST              17 (('campaign', 'source_id', 'lead_source', 'property_type'))
               GET_ITER
       L4:     FOR_ITER                21 (to L6)
               STORE_FAST               4 (k)

138            LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (k, metadata_in)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

139    L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (metadata_in, k)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (safe_meta, k)
               STORE_SUBSCR
               JUMP_BACKWARD           23 (to L4)

137    L6:     END_FOR
               POP_ITER

142            LOAD_CONST               2 ('phone')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('lead_phone')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

143    L7:     LOAD_CONST               5 ('brokerage_id')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('brokerage_id')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

144    L8:     LOAD_CONST               6 ('name')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               7 ('lead_name')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

145    L9:     LOAD_CONST               8 ('email')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               9 ('lead_email')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

146   L10:     LOAD_CONST              10 ('intent')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('intent')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

147   L11:     LOAD_CONST              11 ('budget')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              11 ('budget')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

148   L12:     LOAD_CONST              12 ('timeline')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              12 ('timeline')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

149   L13:     LOAD_CONST              13 ('source')
               LOAD_CONST              14 ('pending_call_worker')

150            LOAD_CONST              15 ('property_interest')
               LOAD_FAST_BORROW         0 (pending_call_row)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              16 ('property_address')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')

151   L14:     LOAD_CONST               1 ('metadata')
               LOAD_FAST_BORROW         3 (safe_meta)

141            BUILD_MAP               10
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\ingestion\worker.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')

160           LOAD_CONST               2 ('Dict[str, Any]')

159           LOAD_CONST               3 ('worker_id')

161           LOAD_CONST               4 ('Optional[str]')

159           LOAD_CONST               5 ('return')

162           LOAD_CONST               2 ('Dict[str, Any]')

159           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object process_pending_call at 0x0000018C17ED78C0, file "app\services\ingestion\worker.py", line 159>:
 159            RESUME                   0

 178            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('pending_call_id')
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               2 (None)
        L2:     STORE_FAST               2 (pending_call_id)

 179            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                CALL                     1
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               2 (None)
        L4:     STORE_FAST               3 (brokerage_id)

 180            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               4 ('source')
                CALL                     1
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               2 (None)
        L6:     STORE_FAST               4 (source)

 181            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('attempts')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L7:     LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_SMALL_INT           0
        L9:     STORE_FAST               5 (attempt)

 182            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('max_attempts')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           1

  --   L10:     JUMP_FORWARD             1 (to L12)

 182   L11:     LOAD_SMALL_INT           1
       L12:     STORE_FAST               6 (max_attempts)

 185            LOAD_CONST               1 ('pending_call_id')
                LOAD_FAST_BORROW         2 (pending_call_id)

 186            LOAD_CONST               4 ('source')
                LOAD_FAST_BORROW         4 (source)

 187            LOAD_CONST               7 ('attempt')
                LOAD_FAST_BORROW         5 (attempt)

 188            LOAD_CONST               6 ('max_attempts')
                LOAD_FAST_BORROW         6 (max_attempts)

 189            LOAD_CONST               8 ('status')
                LOAD_CONST               9 ('failed')

 190            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 191            LOAD_CONST              11 ('error_code')
                LOAD_CONST               2 (None)

 192            LOAD_CONST              12 ('call_sid')
                LOAD_CONST               2 (None)

 184            BUILD_MAP                8
                STORE_FAST               7 (base_result)

 195            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (pending_call_id)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L13)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (brokerage_id)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L14)
                NOT_TAKEN

 196   L13:     LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              13 ('invalid_row_shape')
                CALL                     1
                POP_TOP

 197            LOAD_CONST              13 ('invalid_row_shape')
                LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 198            LOAD_FAST_BORROW         7 (base_result)
                RETURN_VALUE

 201   L14:     LOAD_GLOBAL             11 (mark_pending_call_dialing + NULL)

 202            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (pending_call_id, brokerage_id)
                LOAD_FAST_BORROW         1 (worker_id)

 201            LOAD_CONST              14 (('worker_id',))
                CALL_KW                  3
                STORE_FAST               8 (lock_env)

 204            LOAD_FAST_BORROW         8 (lock_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                LOAD_CONST              15 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       48 (to L15)
                NOT_TAKEN

 205            LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST_BORROW         8 (lock_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 206            LOAD_CONST              16 ('lock_failed')
                LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 207            LOAD_FAST_BORROW         7 (base_result)
                RETURN_VALUE

 210   L15:     LOAD_GLOBAL             15 (_resolve_outbound_dial_adapter + NULL)
                CALL                     0
                STORE_FAST               9 (adapter)

 211            LOAD_FAST_BORROW         9 (adapter)
                POP_JUMP_IF_NOT_NONE    86 (to L16)
                NOT_TAKEN

 214            LOAD_GLOBAL             17 (mark_pending_call_failed + NULL)

 215            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (pending_call_id, brokerage_id)

 216            LOAD_CONST              17 ('outbound_dial_adapter_missing')

 217            LOAD_CONST              18 (False)

 214            LOAD_CONST              19 (('error_code', 'retry'))
                CALL_KW                  4
                STORE_FAST              10 (fail_env)

 219            LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              17 ('outbound_dial_adapter_missing')
                CALL                     1
                POP_TOP

 220            LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST_BORROW        10 (fail_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 221            LOAD_CONST              17 ('outbound_dial_adapter_missing')
                LOAD_FAST_BORROW         7 (base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 222            LOAD_FAST_BORROW         7 (base_result)
                RETURN_VALUE

 227   L16:     LOAD_GLOBAL             19 (build_outbound_call_payload + NULL)
                LOAD_FAST_BORROW         0 (row)
                CALL                     1
                STORE_FAST              11 (payload)

 232            LOAD_CONST              20 ('id')
                LOAD_FAST_BORROW         3 (brokerage_id)
                BUILD_MAP                1
                STORE_FAST              12 (brokerage_pin)

 235            NOP

 236   L17:     LOAD_FAST_BORROW         9 (adapter)
                PUSH_NULL

 237            LOAD_FAST_BORROW        12 (brokerage_pin)

 238            LOAD_FAST_BORROW        11 (payload)

 239            LOAD_CONST              21 ('pending_call_worker')

 240            LOAD_FAST_BORROW         1 (worker_id)

 236            LOAD_CONST              22 (('brokerage', 'lead_payload', 'source', 'worker_id'))
                CALL_KW                  4
                STORE_FAST              13 (adapter_result)

 258   L18:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               13 (adapter_result)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        62 (to L19)
                NOT_TAKEN

 259            LOAD_GLOBAL             17 (mark_pending_call_failed + NULL)

 260            LOAD_FAST_LOAD_FAST     35 (pending_call_id, brokerage_id)

 261            LOAD_CONST              26 ('outbound_dial_adapter_bad_return')

 262            LOAD_CONST              18 (False)

 259            LOAD_CONST              19 (('error_code', 'retry'))
                CALL_KW                  4
                STORE_FAST              10 (fail_env)

 264            LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST               10 (fail_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 265            LOAD_CONST              26 ('outbound_dial_adapter_bad_return')
                LOAD_FAST                7 (base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 266            LOAD_FAST                7 (base_result)
                RETURN_VALUE

 268   L19:     LOAD_FAST               13 (adapter_result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('status')
                CALL                     1
                STORE_FAST              16 (adapter_status)

 269            LOAD_FAST               13 (adapter_result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              12 ('call_sid')
                CALL                     1
                STORE_FAST              17 (call_sid)

 271            LOAD_FAST               16 (adapter_status)
                LOAD_CONST              15 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE      222 (to L25)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               17 (call_sid)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      200 (to L25)
                NOT_TAKEN
                LOAD_FAST               17 (call_sid)
                LOAD_ATTR               31 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      178 (to L25)
                NOT_TAKEN

 272            LOAD_GLOBAL             33 (mark_pending_call_dialed + NULL)

 273            LOAD_FAST_LOAD_FAST     35 (pending_call_id, brokerage_id)
                LOAD_FAST               17 (call_sid)

 272            LOAD_CONST              27 (('call_sid',))
                CALL_KW                  3
                STORE_FAST              18 (ok_env)

 275            LOAD_CONST              28 ('dialed')
                LOAD_FAST                7 (base_result)
                LOAD_CONST               8 ('status')
                STORE_SUBSCR

 276            LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST               18 (ok_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 277            LOAD_FAST               17 (call_sid)
                LOAD_ATTR               31 (strip + NULL|self)
                CALL                     0
                LOAD_FAST                7 (base_result)
                LOAD_CONST              12 ('call_sid')
                STORE_SUBSCR

 279            LOAD_FAST               13 (adapter_result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L20:     GET_ITER
       L21:     FOR_ITER                67 (to L24)
                STORE_FAST              19 (w)

 280            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               19 (w)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L21)
       L22:     LOAD_FAST               19 (w)
                LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           43 (to L21)

 281   L23:     LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST               19 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           69 (to L21)

 279   L24:     END_FOR
                POP_ITER

 282            LOAD_FAST                7 (base_result)
                RETURN_VALUE

 287   L25:     LOAD_FAST               13 (adapter_result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              11 ('error_code')
                CALL                     1
                STORE_FAST              20 (err_code)

 288            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               20 (err_code)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L26)
                NOT_TAKEN
                LOAD_FAST               20 (err_code)
                LOAD_ATTR               31 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L29)
                NOT_TAKEN

 291   L26:     LOAD_FAST               16 (adapter_status)
                LOAD_CONST              15 ('ok')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L27)
                NOT_TAKEN

 290            LOAD_CONST              29 ('outbound_dial_missing_call_sid')
                JUMP_FORWARD             1 (to L28)

 292   L27:     LOAD_CONST              30 ('outbound_dial_returned_non_success')

 289   L28:     STORE_FAST              20 (err_code)

 294   L29:     LOAD_GLOBAL             17 (mark_pending_call_failed + NULL)

 295            LOAD_FAST_LOAD_FAST     35 (pending_call_id, brokerage_id)

 296            LOAD_FAST               20 (err_code)
                LOAD_CONST              18 (False)

 294            LOAD_CONST              19 (('error_code', 'retry'))
                CALL_KW                  4
                STORE_FAST              10 (fail_env)

 298            LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST               10 (fail_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 299            LOAD_FAST               13 (adapter_result)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L30:     GET_ITER
       L31:     FOR_ITER                67 (to L34)
                STORE_FAST              19 (w)

 300            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               19 (w)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L32)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L31)
       L32:     LOAD_FAST               19 (w)
                LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_TRUE         3 (to L33)
                NOT_TAKEN
                JUMP_BACKWARD           43 (to L31)

 301   L33:     LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST               19 (w)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           69 (to L31)

 299   L34:     END_FOR
                POP_ITER

 302            LOAD_FAST               20 (err_code)
                LOAD_FAST                7 (base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 303            LOAD_FAST                7 (base_result)
                RETURN_VALUE

  --   L35:     PUSH_EXC_INFO

 242            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      141 (to L40)
                NOT_TAKEN
                STORE_FAST              14 (e)

 243   L36:     LOAD_CONST              23 ('outbound_dial_failed:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              15 (err)

 244            LOAD_GLOBAL             17 (mark_pending_call_failed + NULL)

 245            LOAD_FAST_LOAD_FAST     35 (pending_call_id, brokerage_id)

 246            LOAD_FAST               15 (err)
                LOAD_CONST              18 (False)

 244            LOAD_CONST              19 (('error_code', 'retry'))
                CALL_KW                  4
                STORE_FAST              10 (fail_env)

 248            LOAD_GLOBAL             26 (logger)
                LOAD_ATTR               29 (warning + NULL|self)

 249            LOAD_CONST              24 ('pending_call adapter exception id=')
                LOAD_FAST                2 (pending_call_id)
                FORMAT_SIMPLE
                LOAD_CONST              25 (' type=')

 250            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 249            BUILD_STRING             4

 248            CALL                     1
                POP_TOP

 252            LOAD_FAST                7 (base_result)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (extend + NULL|self)
                LOAD_FAST               10 (fail_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                BUILD_LIST               0
                CALL                     2
                CALL                     1
                POP_TOP

 253            LOAD_FAST_LOAD_FAST    247 (err, base_result)
                LOAD_CONST              11 ('error_code')
                STORE_SUBSCR

 254            LOAD_FAST                7 (base_result)
       L37:     SWAP                     2
       L38:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L39:     LOAD_CONST               2 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 242   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L17 to L18 -> L35 [0]
  L35 to L36 -> L41 [1] lasti
  L36 to L37 -> L39 [1] lasti
  L37 to L38 -> L41 [1] lasti
  L39 to L41 -> L41 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\ingestion\worker.py", line 310>:
310           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

311           LOAD_CONST               2 ('Any')

310           LOAD_CONST               3 ('worker_id')

312           LOAD_CONST               4 ('Optional[str]')

310           LOAD_CONST               5 ('enabled_override')

314           LOAD_CONST               6 ('Optional[bool]')

310           LOAD_CONST               7 ('return')

315           LOAD_CONST               8 ('Dict[str, Any]')

310           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object run_pending_calls_once at 0x0000018C17ED8380, file "app\services\ingestion\worker.py", line 310>:
 310            RESUME                   0

 346            LOAD_FAST                1 (worker_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        42 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('pas162-worker-')
                LOAD_GLOBAL              0 (uuid)
                LOAD_ATTR                2 (uuid4)
                PUSH_NULL
                CALL                     0
                LOAD_ATTR                4 (hex)
                LOAD_CONST               2 (slice(None, 8, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2
        L1:     STORE_FAST               3 (wid)

 348            LOAD_FAST_BORROW         2 (enabled_override)
                POP_JUMP_IF_NOT_NONE    12 (to L2)
                NOT_TAKEN

 349            LOAD_GLOBAL              7 (pending_calls_worker_enabled + NULL)
                CALL                     0
                STORE_FAST               4 (enabled)
                JUMP_FORWARD            11 (to L3)

 351    L2:     LOAD_GLOBAL              9 (bool + NULL)
                LOAD_FAST_BORROW         2 (enabled_override)
                CALL                     1
                STORE_FAST               4 (enabled)

 352    L3:     LOAD_FAST_BORROW         4 (enabled)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L4)
                NOT_TAKEN

 354            LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('disabled')

 355            LOAD_CONST               6 ('checked')
                LOAD_SMALL_INT           0

 356            LOAD_CONST               7 ('dialed')
                LOAD_SMALL_INT           0

 357            LOAD_CONST               8 ('failed')
                LOAD_SMALL_INT           0

 358            LOAD_CONST               9 ('results')
                BUILD_LIST               0

 359            LOAD_CONST              10 ('warnings')
                LOAD_CONST              11 ('worker_disabled_by_flag')
                BUILD_LIST               1

 353            BUILD_MAP                6
                RETURN_VALUE

 362    L4:     NOP

 363    L5:     LOAD_GLOBAL             11 (list_due_pending_calls + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (limit, wid)
                LOAD_CONST              12 (('limit', 'worker_id'))
                CALL_KW                  2
                STORE_FAST               5 (rows)

 378    L6:     LOAD_FAST                5 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L7)
                NOT_TAKEN

 380            LOAD_CONST               4 ('status')
                LOAD_CONST              15 ('ok')

 381            LOAD_CONST               6 ('checked')
                LOAD_SMALL_INT           0

 382            LOAD_CONST               7 ('dialed')
                LOAD_SMALL_INT           0

 383            LOAD_CONST               8 ('failed')
                LOAD_SMALL_INT           0

 384            LOAD_CONST               9 ('results')
                BUILD_LIST               0

 385            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 379            BUILD_MAP                6
                RETURN_VALUE

 388    L7:     BUILD_LIST               0
                STORE_FAST               7 (results)

 389            LOAD_SMALL_INT           0
                STORE_FAST               8 (dialed)

 390            LOAD_SMALL_INT           0
                STORE_FAST               9 (failed)

 391            LOAD_CONST              16 (False)
                STORE_FAST              10 (adapter_missing)

 392            LOAD_FAST                5 (rows)
                GET_ITER
        L8:     FOR_ITER               100 (to L11)
                STORE_FAST              11 (row)

 393            LOAD_GLOBAL             23 (process_pending_call + NULL)
                LOAD_FAST_LOAD_FAST    179 (row, wid)
                LOAD_CONST              17 (('worker_id',))
                CALL_KW                  2
                STORE_FAST              12 (r)

 394            LOAD_FAST                7 (results)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_FAST               12 (r)
                CALL                     1
                POP_TOP

 395            LOAD_FAST               12 (r)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST               4 ('status')
                CALL                     1
                LOAD_CONST               7 ('dialed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L9)
                NOT_TAKEN

 396            LOAD_FAST                8 (dialed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               8 (dialed)
                JUMP_BACKWARD           65 (to L8)

 398    L9:     LOAD_FAST                9 (failed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               9 (failed)

 399            LOAD_FAST               12 (r)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              18 ('error_code')
                CALL                     1
                LOAD_CONST              19 ('outbound_dial_adapter_missing')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           98 (to L8)

 400   L10:     LOAD_CONST              20 (True)
                STORE_FAST              10 (adapter_missing)
                JUMP_BACKWARD          102 (to L8)

 392   L11:     END_FOR
                POP_ITER

 402            LOAD_FAST               10 (adapter_missing)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN

 409            LOAD_CONST               4 ('status')
                LOAD_CONST              21 ('warning')

 410            LOAD_CONST               6 ('checked')
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1

 411            LOAD_CONST               7 ('dialed')
                LOAD_FAST                8 (dialed)

 412            LOAD_CONST               8 ('failed')
                LOAD_FAST                9 (failed)

 413            LOAD_CONST               9 ('results')
                LOAD_FAST                7 (results)

 414            LOAD_CONST              10 ('warnings')
                LOAD_CONST              19 ('outbound_dial_adapter_missing')
                BUILD_LIST               1

 408            BUILD_MAP                6
                RETURN_VALUE

 416   L12:     LOAD_FAST                9 (failed)
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L13)
                NOT_TAKEN
                LOAD_FAST                8 (dialed)
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L13)
                NOT_TAKEN

 418            LOAD_CONST               4 ('status')
                LOAD_CONST               8 ('failed')

 419            LOAD_CONST               6 ('checked')
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1

 420            LOAD_CONST               7 ('dialed')
                LOAD_FAST                8 (dialed)

 421            LOAD_CONST               8 ('failed')
                LOAD_FAST                9 (failed)

 422            LOAD_CONST               9 ('results')
                LOAD_FAST                7 (results)

 423            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 417            BUILD_MAP                6
                RETURN_VALUE

 426   L13:     LOAD_CONST               4 ('status')
                LOAD_CONST              15 ('ok')

 427            LOAD_CONST               6 ('checked')
                LOAD_GLOBAL             29 (len + NULL)
                LOAD_FAST                5 (rows)
                CALL                     1

 428            LOAD_CONST               7 ('dialed')
                LOAD_FAST                8 (dialed)

 429            LOAD_CONST               8 ('failed')
                LOAD_FAST                9 (failed)

 430            LOAD_CONST               9 ('results')
                LOAD_FAST                7 (results)

 431            LOAD_CONST              10 ('warnings')
                BUILD_LIST               0

 425            BUILD_MAP                6
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 364            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L19)
                NOT_TAKEN
                STORE_FAST               6 (e)

 365   L15:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 366            LOAD_CONST              13 ('run_pending_calls_once list_due failed type=')

 367            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 366            BUILD_STRING             2

 365            CALL                     1
                POP_TOP

 370            LOAD_CONST               4 ('status')
                LOAD_CONST               8 ('failed')

 371            LOAD_CONST               6 ('checked')
                LOAD_SMALL_INT           0

 372            LOAD_CONST               7 ('dialed')
                LOAD_SMALL_INT           0

 373            LOAD_CONST               8 ('failed')
                LOAD_SMALL_INT           0

 374            LOAD_CONST               9 ('results')
                BUILD_LIST               0

 375            LOAD_CONST              10 ('warnings')
                LOAD_CONST              14 ('list_due_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 369            BUILD_MAP                6
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST               3 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 364   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L14 [0]
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\ingestion\worker.py", line 439>:
439           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')

440           LOAD_CONST               2 ('Any')

439           LOAD_CONST               3 ('worker_id')

441           LOAD_CONST               4 ('Optional[str]')

439           LOAD_CONST               5 ('return')

442           LOAD_CONST               6 ('Dict[str, Any]')

439           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object dry_run_pending_calls at 0x0000018C17EDAAF0, file "app\services\ingestion\worker.py", line 439>:
 439            RESUME                   0

 450            LOAD_FAST                1 (worker_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        42 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('pas162-dry-')
                LOAD_GLOBAL              0 (uuid)
                LOAD_ATTR                2 (uuid4)
                PUSH_NULL
                CALL                     0
                LOAD_ATTR                4 (hex)
                LOAD_CONST               2 (slice(None, 8, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2
        L1:     STORE_FAST               2 (wid)

 451            NOP

 452    L2:     LOAD_GLOBAL              7 (list_due_pending_calls + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (limit, wid)
                LOAD_CONST               3 (('limit', 'worker_id'))
                CALL_KW                  2
                STORE_FAST               3 (rows)

 460    L3:     BUILD_LIST               0
                STORE_FAST               5 (summary)

 461            LOAD_FAST                3 (rows)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L4:     GET_ITER
        L5:     FOR_ITER               129 (to L7)
                STORE_FAST               6 (row)

 462            LOAD_GLOBAL             15 (isinstance + NULL)
                LOAD_FAST                6 (row)
                LOAD_GLOBAL             16 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 463            JUMP_BACKWARD           27 (to L5)

 464    L6:     LOAD_FAST                5 (summary)
                LOAD_ATTR               19 (append + NULL|self)

 465            LOAD_CONST              11 ('pending_call_id')
                LOAD_FAST                6 (row)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST              11 ('pending_call_id')
                CALL                     1

 466            LOAD_CONST              12 ('source')
                LOAD_FAST                6 (row)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST              12 ('source')
                CALL                     1

 467            LOAD_CONST              13 ('attempt')
                LOAD_FAST                6 (row)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST              14 ('attempts')
                CALL                     1

 468            LOAD_CONST              15 ('max_attempts')
                LOAD_FAST                6 (row)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST              15 ('max_attempts')
                CALL                     1

 469            LOAD_CONST              16 ('next_attempt_at')
                LOAD_FAST                6 (row)
                LOAD_ATTR               21 (get + NULL|self)
                LOAD_CONST              16 ('next_attempt_at')
                CALL                     1

 464            BUILD_MAP                5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          131 (to L5)

 461    L7:     END_FOR
                POP_ITER

 473            LOAD_CONST               4 ('status')
                LOAD_CONST              17 ('ok')

 474            LOAD_CONST               6 ('checked')
                LOAD_GLOBAL             23 (len + NULL)
                LOAD_FAST                5 (summary)
                CALL                     1

 475            LOAD_CONST               7 ('results')
                LOAD_FAST                5 (summary)

 476            LOAD_CONST               8 ('warnings')
                LOAD_CONST              18 ('dry_run')
                BUILD_LIST               1

 472            BUILD_MAP                4
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 453            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       44 (to L13)
                NOT_TAKEN
                STORE_FAST               4 (e)

 455    L9:     LOAD_CONST               4 ('status')
                LOAD_CONST               5 ('failed')

 456            LOAD_CONST               6 ('checked')
                LOAD_SMALL_INT           0

 457            LOAD_CONST               7 ('results')
                BUILD_LIST               0

 458            LOAD_CONST               8 ('warnings')
                LOAD_CONST               9 ('list_due_failed:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 454            BUILD_MAP                4
       L10:     SWAP                     2
       L11:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --   L12:     LOAD_CONST              10 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 453   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L8 [0]
  L8 to L9 -> L14 [1] lasti
  L9 to L10 -> L12 [1] lasti
  L10 to L11 -> L14 [1] lasti
  L12 to L14 -> L14 [1] lasti
```
