# outbound/dial

- **pyc:** `app\services\outbound\__pycache__\dial.cpython-314.pyc`
- **expected source path (absent):** `app\services\outbound/dial.py`
- **co_filename (from bytecode):** `app\services\outbound\dial.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** outbound

## Module docstring

```
PAS163 — Outbound dial adapter.

Doctrine:

* **No fake success.** If Twilio config or the Twilio client is
  unavailable, the adapter returns a structural ``failed`` envelope
  with a ``twilio_config_missing`` / ``twilio_unavailable`` error
  code. It never fabricates a ``call_sid``.

* **Tenant pin.** ``brokerage_id`` is read ONLY from the
  ``brokerage`` argument (resolved by the caller from auth). The
  adapter never reads ``brokerage_id`` from the ``lead_payload``
  dict — that dict is untrusted ingestion data.

* **No PII echo.** The envelope never returns phone / email / name
  back to the caller. The Twilio ``call_sid`` is the only
  identifying value the adapter surfaces.

* **No internal HTTP self-call.** The adapter does NOT POST to
  ``http://localhost:.../outbound/call``. It reuses the same
  ``twilio.rest.Client`` directly. That avoids forging request
  state against the existing route and keeps the route's
  rate-limit + auth gates intact for genuine external callers.

* **Closed-shape envelope.** Always returns::

      {
          "status":     "ok" | "failed",
          "call_sid":   "<str>" | None,
          "error_code": None | "<structural-token>",
          "warnings":   [<structural-token>, ...],
      }

  No exception escapes. No raw exception text is surfaced.

* **Idempotency hint.** ``idempotency_key`` is accepted but is
  informational only in this phase — Twilio does not de-duplicate
  on a client-supplied key, and adding a server-side dedup table
  is deferred. The token is surfaced back as a warning so the
  operator can correlate the attempt.
```

## Imports

`Any`, `Client`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.config`, `app.db.event_logger`, `app.services.operator.circuit_breaker_policy`, `get_settings`, `log_event_bg`, `logging`, `should_block_new_outbound_for_brokerage`, `twilio.rest`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_brokerage_id_from_brokerage`, `_envelope`, `_from_number`, `_resolve_settings`, `_resolve_twilio_client`, `_safe_short`, `_validate_phone`, `place_outbound_call`

## Env-key candidates

`BASE_URL`, `POST`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`

## String constants (redacted where noted)

- '\nPAS163 — Outbound dial adapter.\n\nDoctrine:\n\n* **No fake success.** If Twilio config or the Twilio client is\n  unavailable, the adapter returns a structural ``failed`` envelope\n  with a ``twilio_config_missing`` / ``twilio_unavailable`` error\n  code. It never fabricates a ``call_sid``.\n\n* **Tenant pin.** ``brokerage_id`` is read ONLY from the\n  ``brokerage`` argument (resolved by the caller from auth). The\n  adapter never reads ``brokerage_id`` from the ``lead_payload``\n  dict — that dict is untrusted ingestion data.\n\n* **No PII echo.** The envelope never returns phone / email / name\n  back to the caller. The Twilio ``call_sid`` is the only\n  identifying value the adapter surfaces.\n\n* **No internal HTTP self-call.** The adapter does NOT POST to\n  ``http://localhost:.../outbound/call``. It reuses the same\n  ``twilio.rest.Client`` directly. That avoids forging request\n  state against the existing route and keeps the route\'s\n  rate-limit + auth gates intact for genuine external callers.\n\n* **Closed-shape envelope.** Always returns::\n\n      {\n          "status":     "ok" | "failed",\n          "call_sid":   "<str>" | None,\n          "error_code": None | "<structural-token>",\n          "warnings":   [<structural-token>, ...],\n      }\n\n  No exception escapes. No raw exception text is surfaced.\n\n* **Idempotency hint.** ``idempotency_key`` is accepted but is\n  informational only in this phase — Twilio does not de-duplicate\n  on a client-supplied key, and adding a server-side dedup table\n  is deferred. The token is surfaced back as a warning so the\n  operator can correlate the attempt.\n'
- 'pas.outbound.dial'
- 'call_sid'
- 'error_code'
- 'warnings'
- 'source'
- 'pending_call_worker'
- 'idempotency_key'
- 'worker_id'
- 'brokerage_row'
- 'status'
- 'str'
- 'Optional[str]'
- 'Optional[List[str]]'
- 'return'
- 'Dict[str, Any]'
- 'brokerage'
- 'Any'
- 'Resolve the canonical brokerage id from auth-passed shapes.\nNever reads ``brokerage_id`` from a lead payload. Accepts a\ndict (current behaviour) or any object exposing ``.id``.'
- 'raw'
- 'Accept only E.164-shaped strings. Returns the cleaned phone\nor None. Defensive — the worker already passes a phone from\nthe row, but the adapter is the structural boundary.'
- 'Optional[Any]'
- 'Pull the existing app settings without exploding when the\nconfig module is missing in a stripped test environment.'
- 'dial settings unavailable type='
- 'account_sid'
- 'auth_token'
- 'Build a Twilio ``Client`` instance. Returns None when the\nTwilio library is missing or the credentials cannot construct\na client. Never raises into the caller.'
- 'dial twilio library missing type='
- 'dial twilio client construct failed type='
- 'settings'
- 'Resolve which Twilio phone number to dial *from*. Brokerage-\nspecific override wins; falls back to the global setting.'
- 'twilio_phone'
- 'TWILIO_PHONE_NUMBER'
- 'text'
- 'int'
- 'Tiny accidental-leak guard for fallback log lines. Never\nused as a return value — only for internal observability.'
- 'lead_payload'
- 'Optional[Dict[str, Any]]'
- 'Place an outbound Twilio call.\n\nInputs:\n  * ``brokerage``       — authenticated brokerage row (dict or\n                          object with ``.id``). MUST come from\n                          auth-resolved state. ``brokerage_row``\n                          is accepted as a synonym so the worker\n                          can pass the same row it already has.\n  * ``lead_payload``    — plain dict shaped like the existing\n                          ``LeadPayload``. Must include ``phone``.\n                          ``brokerage_id`` IN THIS DICT IS\n                          IGNORED — the adapter pins the tenant\n                          from ``brokerage`` only.\n  * ``source``          — structural origin tag (default\n                          ``pending_call_worker``).\n  * ``idempotency_key`` — informational only in this phase.\n  * ``worker_id``       — structural worker tag (no PII).\n\nReturns the closed-shape envelope::\n\n    {\n      "status":     "ok" | "failed",\n      "call_sid":   "<str>" | None,\n      "error_code": None | "<structural-token>",\n      "warnings":   [<structural-token>, ...],\n    }\n\nNever raises. Never returns phone / email / name. Never POSTs\nto localhost.\n'
- 'idempotency_key:'
- 'failed'
- 'brokerage_id_unresolved_from_auth'
- 'circuit_breaker.outbound_dial_blocked'
- 'brokerage_id'
- 'route'
- 'place_outbound_call'
- 'blocked'
- 'action_required'
- 'operator_must_reset_breaker_to_resume'
- 'brokerage_circuit_breaker_tripped'
- 'lead_payload_not_a_dict'
- 'phone'
- 'missing_phone'
- 'twilio_config_missing'
- 'TWILIO_ACCOUNT_SID'
- 'TWILIO_AUTH_TOKEN'
- 'twilio_from_number_missing'
- 'twilio_unavailable'
- 'BASE_URL'
- 'base_url_missing'
- '/twilio/voice'
- '/twilio/status'
- 'POST'
- 'Enable'
- 'twilio_create_failed:'
- 'dial twilio create failed brokerage='
- ' source='
- ' type='
- 'sid'
- 'twilio_returned_no_sid'
- 'dial twilio call created brokerage='
- ' sid='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS163 — Outbound dial adapter.\n\nDoctrine:\n\n* **No fake success.** If Twilio config or the Twilio client is\n  unavailable, the adapter returns a structural ``failed`` envelope\n  with a ``twilio_config_missing`` / ``twilio_unavailable`` error\n  code. It never fabricates a ``call_sid``.\n\n* **Tenant pin.** ``brokerage_id`` is read ONLY from the\n  ``brokerage`` argument (resolved by the caller from auth). The\n  adapter never reads ``brokerage_id`` from the ``lead_payload``\n  dict — that dict is untrusted ingestion data.\n\n* **No PII echo.** The envelope never returns phone / email / name\n  back to the caller. The Twilio ``call_sid`` is the only\n  identifying value the adapter surfaces.\n\n* **No internal HTTP self-call.** The adapter does NOT POST to\n  ``http://localhost:.../outbound/call``. It reuses the same\n  ``twilio.rest.Client`` directly. That avoids forging request\n  state against the existing route and keeps the route\'s\n  rate-limit + auth gates intact for genuine external callers.\n\n* **Closed-shape envelope.** Always returns::\n\n      {\n          "status":     "ok" | "failed",\n          "call_sid":   "<str>" | None,\n          "error_code": None | "<structural-token>",\n          "warnings":   [<structural-token>, ...],\n      }\n\n  No exception escapes. No raw exception text is surfaced.\n\n* **Idempotency hint.** ``idempotency_key`` is accepted but is\n  informational only in this phase — Twilio does not de-duplicate\n  on a client-supplied key, and adding a server-side dedup table\n  is deferred. The token is surfaced back as a warning so the\n  operator can correlate the attempt.\n')
              STORE_NAME               0 (__doc__)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 49           LOAD_NAME                3 (logging)
              LOAD_ATTR               18 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.outbound.dial')
              CALL                     1
              STORE_NAME              10 (logger)

 56           LOAD_CONST               5 ('call_sid')

 59           LOAD_CONST               2 (None)

 56           LOAD_CONST               6 ('error_code')

 60           LOAD_CONST               2 (None)

 56           LOAD_CONST               7 ('warnings')

 61           LOAD_CONST               2 (None)

 56           BUILD_MAP                3
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18025030, file "app\services\outbound\dial.py", line 56>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _envelope at 0x0000018C1794ED80, file "app\services\outbound\dial.py", line 56>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              11 (_envelope)

 75           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\outbound\dial.py", line 75>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _brokerage_id_from_brokerage at 0x0000018C17ECF6F0, file "app\services\outbound\dial.py", line 75>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (_brokerage_id_from_brokerage)

 92           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\outbound\dial.py", line 92>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _validate_phone at 0x0000018C179A7290, file "app\services\outbound\dial.py", line 92>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (_validate_phone)

113           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\outbound\dial.py", line 113>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _resolve_settings at 0x0000018C17FF13B0, file "app\services\outbound\dial.py", line 113>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (_resolve_settings)

126           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\outbound\dial.py", line 126>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _resolve_twilio_client at 0x0000018C17F00C20, file "app\services\outbound\dial.py", line 126>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_resolve_twilio_client)

146           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\outbound\dial.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _from_number at 0x0000018C17EC46C0, file "app\services\outbound\dial.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (_from_number)

159           LOAD_CONST              29 ((24,))
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025130, file "app\services\outbound\dial.py", line 159>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _safe_short at 0x0000018C1802C9B0, file "app\services\outbound\dial.py", line 159>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              17 (_safe_short)

171           LOAD_CONST              30 ((None, None))
              LOAD_CONST              22 ('source')

175           LOAD_CONST              23 ('pending_call_worker')

171           LOAD_CONST              24 ('idempotency_key')

176           LOAD_CONST               2 (None)

171           LOAD_CONST              25 ('worker_id')

177           LOAD_CONST               2 (None)

171           LOAD_CONST              26 ('brokerage_row')

182           LOAD_CONST               2 (None)

171           BUILD_MAP                4
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C180E8030, file "app\services\outbound\dial.py", line 171>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object place_outbound_call at 0x0000018C17D49030, file "app\services\outbound\dial.py", line 171>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              18 (place_outbound_call)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\outbound\dial.py", line 56>:
 56           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

 57           LOAD_CONST               2 ('str')

 56           LOAD_CONST               3 ('call_sid')

 59           LOAD_CONST               4 ('Optional[str]')

 56           LOAD_CONST               5 ('error_code')

 60           LOAD_CONST               4 ('Optional[str]')

 56           LOAD_CONST               6 ('warnings')

 61           LOAD_CONST               7 ('Optional[List[str]]')

 56           LOAD_CONST               8 ('return')

 62           LOAD_CONST               9 ('Dict[str, Any]')

 56           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _envelope at 0x0000018C1794ED80, file "app\services\outbound\dial.py", line 56>:
 56           RESUME                   0

 64           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

 65           LOAD_CONST               1 ('call_sid')
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (call_sid)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (call_sid)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST                1 (call_sid)
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 (None)

 66   L2:     LOAD_CONST               3 ('error_code')
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (error_code)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (error_code)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_FAST                2 (error_code)
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               2 (None)

 67   L4:     LOAD_CONST               4 ('warnings')
              LOAD_GLOBAL              7 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L5:     CALL                     1

 63           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\outbound\dial.py", line 75>:
 75           RESUME                   0
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

Disassembly of <code object _brokerage_id_from_brokerage at 0x0000018C17ECF6F0, file "app\services\outbound\dial.py", line 75>:
 75           RESUME                   0

 79           LOAD_FAST_BORROW         0 (brokerage)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

 80           LOAD_CONST               1 (None)
              RETURN_VALUE

 81   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       80 (to L3)
              NOT_TAKEN

 82           LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('id')
              CALL                     1
              STORE_FAST               1 (v)

 83           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

 84           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

 85   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

 86   L3:     LOAD_GLOBAL             11 (getattr + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_CONST               2 ('id')
              LOAD_CONST               1 (None)
              CALL                     3
              STORE_FAST               2 (bid)

 87           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L4)
              NOT_TAKEN

 88           LOAD_FAST_BORROW         2 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

 89   L4:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\outbound\dial.py", line 92>:
 92           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('raw')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_phone at 0x0000018C179A7290, file "app\services\outbound\dial.py", line 92>:
 92           RESUME                   0

 96           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (raw)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 97           LOAD_CONST               1 (None)
              RETURN_VALUE

 98   L1:     LOAD_FAST_BORROW         0 (raw)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (p)

 99           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                7 (startswith + NULL|self)
              LOAD_CONST               2 ('+')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

100           LOAD_CONST               1 (None)
              RETURN_VALUE

101   L2:     LOAD_FAST_BORROW         1 (p)
              LOAD_CONST               3 (slice(1, None, None))
              BINARY_OP               26 ([])
              STORE_FAST               2 (digits)

102           LOAD_FAST_BORROW         2 (digits)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (digits)
              LOAD_ATTR                9 (isdigit + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN

103   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

104   L4:     LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         2 (digits)
              CALL                     1
              LOAD_SMALL_INT           8
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE        17 (to L5)
              NOT_TAKEN
              LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         2 (digits)
              CALL                     1
              LOAD_SMALL_INT          15
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN

105   L5:     LOAD_CONST               1 (None)
              RETURN_VALUE

106   L6:     LOAD_FAST_BORROW         1 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\outbound\dial.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Optional[Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _resolve_settings at 0x0000018C17FF13B0, file "app\services\outbound\dial.py", line 113>:
 113           RESUME                   0

 116           NOP

 117   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_settings',))
               IMPORT_NAME              0 (app.config)
               IMPORT_FROM              1 (get_settings)
               STORE_FAST               0 (get_settings)
               POP_TOP

 118           LOAD_FAST_BORROW         0 (get_settings)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 119           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 120   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 121           LOAD_CONST               2 ('dial settings unavailable type=')
               LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 120           CALL                     1
               POP_TOP

 123   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 119   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\outbound\dial.py", line 126>:
126           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('account_sid')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('auth_token')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Optional[Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _resolve_twilio_client at 0x0000018C17F00C20, file "app\services\outbound\dial.py", line 126>:
 126            RESUME                   0

 130            NOP

 131    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('Client',))
                IMPORT_NAME              0 (twilio.rest)
                IMPORT_FROM              1 (Client)
                STORE_FAST               2 (Client)
                POP_TOP

 137    L2:     NOP

 138    L3:     LOAD_FAST                2 (Client)
                PUSH_NULL
                LOAD_FAST_LOAD_FAST      1 (account_sid, auth_token)
                CALL                     2
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 132            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 133    L6:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 134            LOAD_CONST               2 ('dial twilio library missing type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 133            CALL                     1
                POP_TOP

 136    L7:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --    L8:     LOAD_CONST               3 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 132    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L11:     PUSH_EXC_INFO

 139            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L15)
                NOT_TAKEN
                STORE_FAST               3 (e)

 140   L12:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 141            LOAD_CONST               4 ('dial twilio client construct failed type=')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 140            CALL                     1
                POP_TOP

 143   L13:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L14:     LOAD_CONST               3 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 139   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L11 [0]
  L5 to L6 -> L10 [1] lasti
  L6 to L7 -> L8 [1] lasti
  L8 to L10 -> L10 [1] lasti
  L11 to L12 -> L16 [1] lasti
  L12 to L13 -> L14 [1] lasti
  L14 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\outbound\dial.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('settings')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _from_number at 0x0000018C17EC46C0, file "app\services\outbound\dial.py", line 146>:
146           RESUME                   0

149           LOAD_CONST               1 (None)
              STORE_FAST               2 (candidate)

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN

151           LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('twilio_phone')
              CALL                     1
              STORE_FAST               2 (candidate)

152   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (candidate)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (candidate)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L3)
              NOT_TAKEN

153   L2:     LOAD_GLOBAL             11 (getattr + NULL)
              LOAD_FAST_BORROW         1 (settings)
              LOAD_CONST               3 ('TWILIO_PHONE_NUMBER')
              LOAD_CONST               4 ('')
              CALL                     3
              STORE_FAST               2 (candidate)

154   L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (candidate)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (candidate)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L4)
              NOT_TAKEN

155           LOAD_FAST_BORROW         2 (candidate)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

156   L4:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\outbound\dial.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('n')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_short at 0x0000018C1802C9B0, file "app\services\outbound\dial.py", line 159>:
159           RESUME                   0

162           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (text)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

163           LOAD_CONST               1 ('')
              RETURN_VALUE

164   L1:     LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         0 (text)
              CALL                     1
              LOAD_FAST_BORROW         1 (n)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (text)
              RETURN_VALUE
      L2:     LOAD_FAST_BORROW         0 (text)
              LOAD_CONST               2 (None)
              LOAD_FAST_BORROW         1 (n)
              BINARY_SLICE
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180E8030, file "app\services\outbound\dial.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

172           LOAD_CONST               2 ('Any')

171           LOAD_CONST               3 ('lead_payload')

173           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

171           LOAD_CONST               5 ('source')

175           LOAD_CONST               6 ('str')

171           LOAD_CONST               7 ('idempotency_key')

176           LOAD_CONST               8 ('Optional[str]')

171           LOAD_CONST               9 ('worker_id')

177           LOAD_CONST               8 ('Optional[str]')

171           LOAD_CONST              10 ('brokerage_row')

182           LOAD_CONST               2 ('Any')

171           LOAD_CONST              11 ('return')

183           LOAD_CONST              12 ('Dict[str, Any]')

171           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object place_outbound_call at 0x0000018C17D49030, file "app\services\outbound\dial.py", line 171>:
 171            RESUME                   0

 214            BUILD_LIST               0
                STORE_FAST               6 (warnings)

 215            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (idempotency_key)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       53 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (idempotency_key)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       31 (to L1)
                NOT_TAKEN

 219            LOAD_FAST_BORROW         6 (warnings)
                LOAD_ATTR                7 (append + NULL|self)

 220            LOAD_CONST               1 ('idempotency_key:')
                LOAD_GLOBAL              9 (_safe_short + NULL)
                LOAD_FAST_BORROW         3 (idempotency_key)
                LOAD_SMALL_INT          48
                CALL                     2
                FORMAT_SIMPLE
                BUILD_STRING             2

 219            CALL                     1
                POP_TOP

 224    L1:     LOAD_FAST_BORROW         0 (brokerage)
                POP_JUMP_IF_NONE         3 (to L2)
                NOT_TAKEN
                LOAD_FAST                0 (brokerage)
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_FAST                5 (brokerage_row)
        L3:     STORE_FAST               7 (eff_brokerage)

 225            LOAD_GLOBAL             11 (_brokerage_id_from_brokerage + NULL)
                LOAD_FAST_BORROW         7 (eff_brokerage)
                CALL                     1
                STORE_FAST               8 (brokerage_id)

 226            LOAD_FAST_BORROW         8 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L4)
                NOT_TAKEN

 227            LOAD_GLOBAL             13 (_envelope + NULL)

 228            LOAD_CONST               3 ('failed')

 229            LOAD_CONST               4 ('brokerage_id_unresolved_from_auth')

 230            LOAD_FAST_BORROW         6 (warnings)

 227            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 242    L4:     NOP

 243    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               6 (('should_block_new_outbound_for_brokerage',))
                IMPORT_NAME              7 (app.services.operator.circuit_breaker_policy)
                IMPORT_FROM              8 (should_block_new_outbound_for_brokerage)
                STORE_FAST               9 (should_block_new_outbound_for_brokerage)
                POP_TOP

 246            LOAD_FAST_BORROW         9 (should_block_new_outbound_for_brokerage)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L10)
        L6:     NOT_TAKEN

 247            NOP

 248    L7:     LOAD_SMALL_INT           0
                LOAD_CONST               7 (('log_event_bg',))
                IMPORT_NAME              9 (app.db.event_logger)
                IMPORT_FROM             10 (log_event_bg)
                STORE_FAST              10 (log_event_bg)
                POP_TOP

 249            LOAD_FAST_BORROW        10 (log_event_bg)
                PUSH_NULL
                LOAD_CONST               8 ('circuit_breaker.outbound_dial_blocked')

 250            LOAD_CONST               9 ('brokerage_id')
                LOAD_FAST_BORROW         8 (brokerage_id)

 251            LOAD_CONST              10 ('route')
                LOAD_CONST              11 ('place_outbound_call')

 252            LOAD_CONST              12 ('status')
                LOAD_CONST              13 ('blocked')

 253            LOAD_CONST              14 ('action_required')
                LOAD_CONST              15 ('operator_must_reset_breaker_to_resume')

 249            BUILD_MAP                4
                CALL                     2
                POP_TOP

 257    L8:     LOAD_GLOBAL             13 (_envelope + NULL)

 258            LOAD_CONST               3 ('failed')

 259            LOAD_CONST              16 ('brokerage_circuit_breaker_tripped')

 260            LOAD_FAST_BORROW         6 (warnings)

 257            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
        L9:     RETURN_VALUE

 246   L10:     NOP

 269   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (lead_payload)
                LOAD_GLOBAL             24 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L12)
                NOT_TAKEN

 270            LOAD_GLOBAL             13 (_envelope + NULL)

 271            LOAD_CONST               3 ('failed')

 272            LOAD_CONST              17 ('lead_payload_not_a_dict')

 273            LOAD_FAST_BORROW         6 (warnings)

 270            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 277   L12:     LOAD_GLOBAL             27 (_validate_phone + NULL)
                LOAD_FAST_BORROW         1 (lead_payload)
                LOAD_ATTR               29 (get + NULL|self)
                LOAD_CONST              18 ('phone')
                CALL                     1
                CALL                     1
                STORE_FAST              11 (phone)

 278            LOAD_FAST_BORROW        11 (phone)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L13)
                NOT_TAKEN

 279            LOAD_GLOBAL             13 (_envelope + NULL)

 280            LOAD_CONST               3 ('failed')

 281            LOAD_CONST              19 ('missing_phone')

 282            LOAD_FAST_BORROW         6 (warnings)

 279            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 286   L13:     LOAD_GLOBAL             31 (_resolve_settings + NULL)
                CALL                     0
                STORE_FAST              12 (settings)

 287            LOAD_FAST_BORROW        12 (settings)
                POP_JUMP_IF_NOT_NONE    15 (to L14)
                NOT_TAKEN

 288            LOAD_GLOBAL             13 (_envelope + NULL)

 289            LOAD_CONST               3 ('failed')

 290            LOAD_CONST              20 ('twilio_config_missing')

 291            LOAD_FAST_BORROW         6 (warnings)

 288            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 294   L14:     LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        12 (settings)
                LOAD_CONST              21 ('TWILIO_ACCOUNT_SID')
                LOAD_CONST              22 ('')
                CALL                     3
                STORE_FAST              13 (account_sid)

 295            LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        12 (settings)
                LOAD_CONST              23 ('TWILIO_AUTH_TOKEN')
                LOAD_CONST              22 ('')
                CALL                     3
                STORE_FAST              14 (auth_token)

 296            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (account_sid)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       67 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW        13 (account_sid)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L15)
                NOT_TAKEN

 297            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        14 (auth_token)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW        14 (auth_token)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L16)
                NOT_TAKEN

 298   L15:     LOAD_GLOBAL             13 (_envelope + NULL)

 299            LOAD_CONST               3 ('failed')

 300            LOAD_CONST              20 ('twilio_config_missing')

 301            LOAD_FAST_BORROW         6 (warnings)

 298            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 304   L16:     LOAD_GLOBAL             35 (_from_number + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 124 (eff_brokerage, settings)
                CALL                     2
                STORE_FAST              15 (from_number)

 305            LOAD_FAST_BORROW        15 (from_number)
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L17)
                NOT_TAKEN

 306            LOAD_GLOBAL             13 (_envelope + NULL)

 307            LOAD_CONST               3 ('failed')

 308            LOAD_CONST              24 ('twilio_from_number_missing')

 309            LOAD_FAST_BORROW         6 (warnings)

 306            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 312   L17:     LOAD_GLOBAL             37 (_resolve_twilio_client + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (account_sid, auth_token)
                CALL                     2
                STORE_FAST              16 (client)

 313            LOAD_FAST_BORROW        16 (client)
                POP_JUMP_IF_NOT_NONE    15 (to L18)
                NOT_TAKEN

 314            LOAD_GLOBAL             13 (_envelope + NULL)

 315            LOAD_CONST               3 ('failed')

 316            LOAD_CONST              25 ('twilio_unavailable')

 317            LOAD_FAST_BORROW         6 (warnings)

 314            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 320   L18:     LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        12 (settings)
                LOAD_CONST              26 ('BASE_URL')
                LOAD_CONST              22 ('')
                CALL                     3
                STORE_FAST              17 (base_url)

 321            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        17 (base_url)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L19)
                NOT_TAKEN
                LOAD_FAST_BORROW        17 (base_url)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L20)
                NOT_TAKEN

 322   L19:     LOAD_GLOBAL             13 (_envelope + NULL)

 323            LOAD_CONST               3 ('failed')

 324            LOAD_CONST              27 ('base_url_missing')

 325            LOAD_FAST_BORROW         6 (warnings)

 322            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 329   L20:     NOP

 330   L21:     LOAD_FAST_BORROW        16 (client)
                LOAD_ATTR               38 (calls)
                LOAD_ATTR               41 (create + NULL|self)

 331            LOAD_FAST_BORROW        11 (phone)

 332            LOAD_FAST_BORROW        15 (from_number)

 333            LOAD_FAST_BORROW        17 (base_url)
                LOAD_ATTR               43 (rstrip + NULL|self)
                LOAD_CONST              28 ('/')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              29 ('/twilio/voice')
                BUILD_STRING             2

 334            LOAD_FAST_BORROW        17 (base_url)
                LOAD_ATTR               43 (rstrip + NULL|self)
                LOAD_CONST              28 ('/')
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              30 ('/twilio/status')
                BUILD_STRING             2

 335            LOAD_CONST              31 ('POST')

 336            LOAD_CONST              32 ('Enable')

 337            LOAD_SMALL_INT           4

 330            LOAD_CONST              33 (('to', 'from_', 'url', 'status_callback', 'status_callback_method', 'machine_detection', 'machine_detection_timeout'))
                CALL_KW                  7
                STORE_FAST              18 (call)

 352   L22:     LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST               18 (call)
                LOAD_CONST              38 ('sid')
                LOAD_CONST               2 (None)
                CALL                     3
                STORE_FAST              21 (call_sid)

 353            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               21 (call_sid)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L23)
                NOT_TAKEN
                LOAD_FAST               21 (call_sid)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        15 (to L24)
                NOT_TAKEN

 354   L23:     LOAD_GLOBAL             13 (_envelope + NULL)

 355            LOAD_CONST               3 ('failed')

 356            LOAD_CONST              39 ('twilio_returned_no_sid')

 357            LOAD_FAST                6 (warnings)

 354            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 360   L24:     LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               53 (info + NULL|self)

 361            LOAD_CONST              40 ('dial twilio call created brokerage=')
                LOAD_FAST                8 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              36 (' source=')

 362            LOAD_FAST                2 (source)
                FORMAT_SIMPLE
                LOAD_CONST              41 (' sid=')
                LOAD_FAST               21 (call_sid)
                FORMAT_SIMPLE

 361            BUILD_STRING             6

 360            CALL                     1
                POP_TOP

 364            LOAD_GLOBAL             13 (_envelope + NULL)

 365            LOAD_CONST              42 ('ok')

 366            LOAD_FAST               21 (call_sid)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0

 367            LOAD_FAST                6 (warnings)

 364            LOAD_CONST              43 (('call_sid', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 255            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L27)
                NOT_TAKEN
                POP_TOP

 256   L26:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 602 (to L8)

 255   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 262            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L31)
                NOT_TAKEN
                POP_TOP

 266   L30:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 605 (to L11)

 262   L31:     RERAISE                  0

  --   L32:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L33:     PUSH_EXC_INFO

 339            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       98 (to L38)
                NOT_TAKEN
                STORE_FAST              19 (e)

 341   L34:     LOAD_CONST              34 ('twilio_create_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                STORE_FAST              20 (err)

 342            LOAD_GLOBAL             48 (logger)
                LOAD_ATTR               51 (warning + NULL|self)

 343            LOAD_CONST              35 ('dial twilio create failed brokerage=')
                LOAD_FAST                8 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              36 (' source=')

 344            LOAD_FAST                2 (source)
                FORMAT_SIMPLE
                LOAD_CONST              37 (' type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE

 343            BUILD_STRING             6

 342            CALL                     1
                POP_TOP

 346            LOAD_GLOBAL             13 (_envelope + NULL)

 347            LOAD_CONST               3 ('failed')

 348            LOAD_FAST               20 (err)

 349            LOAD_FAST                6 (warnings)

 346            LOAD_CONST               5 (('error_code', 'warnings'))
                CALL_KW                  3
       L35:     SWAP                     2
       L36:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RETURN_VALUE

  --   L37:     LOAD_CONST               2 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 339   L38:     RERAISE                  0

  --   L39:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L29 [0]
  L7 to L8 -> L25 [0]
  L8 to L9 -> L29 [0]
  L21 to L22 -> L33 [0]
  L25 to L26 -> L28 [1] lasti
  L26 to L27 -> L29 [0]
  L27 to L28 -> L28 [1] lasti
  L28 to L29 -> L29 [0]
  L29 to L30 -> L32 [1] lasti
  L31 to L32 -> L32 [1] lasti
  L33 to L34 -> L39 [1] lasti
  L34 to L35 -> L37 [1] lasti
  L35 to L36 -> L39 [1] lasti
  L37 to L39 -> L39 [1] lasti
```
