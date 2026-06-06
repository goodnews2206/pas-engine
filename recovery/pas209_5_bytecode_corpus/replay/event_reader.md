# replay/event_reader

- **pyc:** `app\services\replay\__pycache__\event_reader.cpython-314.pyc`
- **expected source path (absent):** `app\services\replay/event_reader.py`
- **co_filename (from bytecode):** `app\services\replay\event_reader.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** replay

## Module docstring

```
PAS141 — Read + normalize pas_events rows for replay.

Reads tolerate three storage shapes (in priority order):
  1. v8 top-level column          (PAS140A schema, post-migration)
  2. payload["contract"][key]     (PAS140D legacy fallback nest)
  3. event-specific payload key   (pre-PAS140 legacy emission)

Never raises on malformed rows — returns the row in its best
interpretable state. Callers can rely on every key in the normalized
dict to be either a string/scalar or None (no nested dicts in the
top-level shape, except `payload` and `created_at`).
```

## Imports

`Any`, `Optional`, `app.db.tenant_safe`, `app.services.intelligence.queries`, `events_for_call`, `require_tenant_or_unscoped`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_contract_nest`, `_safe_payload`, `get_contract_value`, `load_call_events`, `load_call_events_unscoped`, `normalize_event`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS141 — Read + normalize pas_events rows for replay.\n\nReads tolerate three storage shapes (in priority order):\n  1. v8 top-level column          (PAS140A schema, post-migration)\n  2. payload["contract"][key]     (PAS140D legacy fallback nest)\n  3. event-specific payload key   (pre-PAS140 legacy emission)\n\nNever raises on malformed rows — returns the row in its best\ninterpretable state. Callers can rely on every key in the normalized\ndict to be either a string/scalar or None (no nested dicts in the\ntop-level shape, except `payload` and `created_at`).\n'
- 'brokerage_id'
- 'extracted_field'
- 'extracted_value'
- 'outcome_state'
- 'field'
- 'value'
- 'outcome'
- 'allow_unscoped'
- 'row'
- 'return'
- "Return row['payload'] coerced to a plain dict (never None / wrong type)."
- 'payload'
- 'contract'
- 'key'
- '\nSingle-field reader with the full PAS140D fallback chain.\n\nPriority:\n  1. row[key]                         — v8 top-level\n  2. payload["contract"][key]         — v8 nested fallback\n  3. event-specific payload key       — legacy fallback\n  4. None\n\nNever raises. Returns None for unknown keys.\n'
- 'event_type'
- 'input_text'
- 'lead.uttered'
- 'excerpt'
- 'output_text'
- 'pas.uttered'
- '\nProject one pas_events row into the normalized replay shape.\n\nThe result has every key in NORMALIZED_KEYS — None when not\npresent in any layer. payload is the original payload dict\n(or {} if missing). created_at is passed through verbatim\nso callers can do ISO-string comparison or parse it themselves.\n\nNever raises.\n'
- 'created_at'
- 'state'
- 'call_id'
- '\nFetch every pas_events row for a single call, oldest first, then\nnormalize each one through `normalize_event`.\n\nThin wrapper around app.services.intelligence.queries.events_for_call\nso all replay-side reads have a single seam tests can monkey-patch.\n\nPAS143F1 — `brokerage_id` is required unless `allow_unscoped=True`.\nReplay tools that legitimately read across tenants (admin debug\nsessions, the `replay_call.py` CLI when no brokerage is supplied)\nmust use the explicit `load_call_events_unscoped` wrapper below.\n\nReturns [] for empty / unknown calls. Never raises.\n'
- 'load_call_events'
- 'Admin / CLI helper: replay any call without requiring a tenant scope.\n\nPass `brokerage_id` to scope to one tenant; pass None for the\noperator-investigates-anything flow. The unsafe shape is opt-in\nvia this name so `grep _unscoped` audits the access pattern.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS141 — Read + normalize pas_events rows for replay.\n\nReads tolerate three storage shapes (in priority order):\n  1. v8 top-level column          (PAS140A schema, post-migration)\n  2. payload["contract"][key]     (PAS140D legacy fallback nest)\n  3. event-specific payload key   (pre-PAS140 legacy emission)\n\nNever raises on malformed rows — returns the row in its best\ninterpretable state. Callers can rely on every key in the normalized\ndict to be either a string/scalar or None (no nested dicts in the\ntop-level shape, except `payload` and `created_at`).\n')
              STORE_NAME               0 (__doc__)

 15           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('Any', 'Optional'))
              IMPORT_NAME              1 (typing)
              IMPORT_FROM              2 (Any)
              STORE_NAME               2 (Any)
              IMPORT_FROM              3 (Optional)
              STORE_NAME               3 (Optional)
              POP_TOP

 17           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('require_tenant_or_unscoped',))
              IMPORT_NAME              4 (app.db.tenant_safe)
              IMPORT_FROM              5 (require_tenant_or_unscoped)
              STORE_NAME               5 (require_tenant_or_unscoped)
              POP_TOP

 18           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('events_for_call',))
              IMPORT_NAME              6 (app.services.intelligence.queries)
              IMPORT_FROM              7 (events_for_call)
              STORE_NAME               7 (events_for_call)
              POP_TOP

 22           LOAD_CONST              26 (('event_id', 'event_type', 'brokerage_id', 'call_id', 'lead_id', 'actor', 'workflow_stage', 'input_text', 'output_text', 'extracted_field', 'extracted_value', 'confidence_score', 'outcome_state', 'source', 'state', 'payload', 'created_at'))
              STORE_NAME               8 (NORMALIZED_KEYS)

 51           LOAD_CONST               5 ('extracted_field')
              LOAD_CONST               8 ('field')

 52           LOAD_CONST               6 ('extracted_value')
              LOAD_CONST               9 ('value')

 53           LOAD_CONST               7 ('outcome_state')
              LOAD_CONST              10 ('outcome')

 50           BUILD_MAP                3
              STORE_NAME               9 (_PAYLOAD_FALLBACK_KEYS)

 60           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\replay\event_reader.py", line 60>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _safe_payload at 0x0000018C17972550, file "app\services\replay\event_reader.py", line 60>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              10 (_safe_payload)

 66           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\replay\event_reader.py", line 66>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _safe_contract_nest at 0x0000018C18038170, file "app\services\replay\event_reader.py", line 66>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (_safe_contract_nest)

 72           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C180E4250, file "app\services\replay\event_reader.py", line 72>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object get_contract_value at 0x0000018C17EDA440, file "app\services\replay\event_reader.py", line 72>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (get_contract_value)

117           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025130, file "app\services\replay\event_reader.py", line 117>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object normalize_event at 0x0000018C17ECEDB0, file "app\services\replay\event_reader.py", line 117>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (normalize_event)

146           LOAD_CONST               4 ('brokerage_id')

149           LOAD_CONST              19 (None)

146           LOAD_CONST              20 ('allow_unscoped')

150           LOAD_CONST              21 (False)

146           BUILD_MAP                2
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C1802CAE0, file "app\services\replay\event_reader.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object load_call_events at 0x0000018C17F95E60, file "app\services\replay\event_reader.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              14 (load_call_events)

175           LOAD_CONST               4 ('brokerage_id')

178           LOAD_CONST              19 (None)

175           BUILD_MAP                1
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C1802C750, file "app\services\replay\event_reader.py", line 175>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object load_call_events_unscoped at 0x0000018C17FA3960, file "app\services\replay\event_reader.py", line 175>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              15 (load_call_events_unscoped)
              LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\replay\event_reader.py", line 60>:
 60           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_payload at 0x0000018C17972550, file "app\services\replay\event_reader.py", line 60>:
 60           RESUME                   0

 62           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('payload')
              CALL                     1
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 (None)
      L2:     STORE_FAST               1 (p)

 63           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (p)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (p)
              RETURN_VALUE
      L3:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\replay\event_reader.py", line 66>:
 66           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_contract_nest at 0x0000018C18038170, file "app\services\replay\event_reader.py", line 66>:
 66           RESUME                   0

 67           LOAD_GLOBAL              1 (_safe_payload + NULL)
              LOAD_FAST_BORROW         0 (row)
              CALL                     1
              STORE_FAST               1 (p)

 68           LOAD_FAST_BORROW         1 (p)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               0 ('contract')
              CALL                     1
              STORE_FAST               2 (nest)

 69           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (nest)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (nest)
              RETURN_VALUE
      L1:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180E4250, file "app\services\replay\event_reader.py", line 72>:
 72           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('key')
              LOAD_GLOBAL              2 (str)
              LOAD_CONST               3 ('return')
              LOAD_GLOBAL              4 (Any)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_contract_value at 0x0000018C17EDA440, file "app\services\replay\event_reader.py", line 72>:
 72           RESUME                   0

 84           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (key)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 85   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

 88   L2:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         1 (key)
              CALL                     1
              STORE_FAST               2 (top)

 89           LOAD_FAST_BORROW         2 (top)
              POP_JUMP_IF_NONE         3 (to L3)
              NOT_TAKEN

 90           LOAD_FAST_BORROW         2 (top)
              RETURN_VALUE

 93   L3:     LOAD_GLOBAL              7 (_safe_contract_nest + NULL)
              LOAD_FAST_BORROW         0 (row)
              CALL                     1
              STORE_FAST               3 (nest)

 94           LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (key, nest)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       19 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (nest, key)
              BINARY_OP               26 ([])
              POP_JUMP_IF_NONE         9 (to L4)
              NOT_TAKEN

 95           LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (nest, key)
              BINARY_OP               26 ([])
              RETURN_VALUE

 98   L4:     LOAD_GLOBAL              9 (_safe_payload + NULL)
              LOAD_FAST_BORROW         0 (row)
              CALL                     1
              STORE_FAST               4 (payload)

 99           LOAD_GLOBAL             10 (_PAYLOAD_FALLBACK_KEYS)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         1 (key)
              CALL                     1
              STORE_FAST               5 (fallback_key)

100           LOAD_FAST_BORROW         5 (fallback_key)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (fallback_key, payload)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       19 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (payload, fallback_key)
              BINARY_OP               26 ([])
              POP_JUMP_IF_NONE         9 (to L5)
              NOT_TAKEN

101           LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (payload, fallback_key)
              BINARY_OP               26 ([])
              RETURN_VALUE

104   L5:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('event_type')
              CALL                     1
              STORE_FAST               6 (et)

105           LOAD_FAST_BORROW         1 (key)
              LOAD_CONST               3 ('input_text')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       31 (to L6)
              NOT_TAKEN
              LOAD_FAST_BORROW         6 (et)
              LOAD_CONST               4 ('lead.uttered')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       24 (to L6)
              NOT_TAKEN

106           LOAD_FAST_BORROW         4 (payload)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('excerpt')
              CALL                     1
              STORE_FAST               7 (excerpt)

107           LOAD_FAST_BORROW         7 (excerpt)
              POP_JUMP_IF_NONE         3 (to L6)
              NOT_TAKEN

108           LOAD_FAST_BORROW         7 (excerpt)
              RETURN_VALUE

109   L6:     LOAD_FAST_BORROW         1 (key)
              LOAD_CONST               6 ('output_text')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       31 (to L7)
              NOT_TAKEN
              LOAD_FAST_BORROW         6 (et)
              LOAD_CONST               7 ('pas.uttered')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       24 (to L7)
              NOT_TAKEN

110           LOAD_FAST_BORROW         4 (payload)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               5 ('excerpt')
              CALL                     1
              STORE_FAST               7 (excerpt)

111           LOAD_FAST_BORROW         7 (excerpt)
              POP_JUMP_IF_NONE         3 (to L7)
              NOT_TAKEN

112           LOAD_FAST_BORROW         7 (excerpt)
              RETURN_VALUE

114   L7:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "app\services\replay\event_reader.py", line 117>:
117           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_GLOBAL              0 (dict)
              LOAD_CONST               2 ('return')
              LOAD_GLOBAL              0 (dict)
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_event at 0x0000018C17ECEDB0, file "app\services\replay\event_reader.py", line 117>:
 117            RESUME                   0

 128            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        32 (to L5)
                NOT_TAKEN

 129            LOAD_GLOBAL              4 (NORMALIZED_KEYS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (k)
                SWAP                     2
        L1:     BUILD_MAP                0
                SWAP                     2
        L2:     FOR_ITER                 5 (to L3)
                STORE_FAST_LOAD_FAST    17 (k, k)
                LOAD_CONST               1 (None)
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     SWAP                     2
                STORE_FAST               1 (k)
                LOAD_CONST               2 ('payload')
                BUILD_MAP                0
                BUILD_MAP                1
                BINARY_OP                7 (|)
                RETURN_VALUE

 131    L5:     BUILD_MAP                0
                STORE_FAST               2 (out)

 132            LOAD_GLOBAL              4 (NORMALIZED_KEYS)
                GET_ITER
        L6:     FOR_ITER               108 (to L11)
                STORE_FAST               1 (k)

 133            LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               2 ('payload')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       16 (to L7)
                NOT_TAKEN

 134            LOAD_GLOBAL              7 (_safe_payload + NULL)
                LOAD_FAST_BORROW         0 (row)
                CALL                     1
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (out, k)
                STORE_SUBSCR
                JUMP_BACKWARD           25 (to L6)

 135    L7:     LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               3 ('created_at')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE        15 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               4 ('event_type')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         8 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               5 ('state')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       22 (to L9)
                NOT_TAKEN

 137    L8:     LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_FAST_BORROW         1 (k)
                CALL                     1
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (out, k)
                STORE_SUBSCR
                JUMP_BACKWARD           67 (to L6)

 138    L9:     LOAD_FAST_BORROW         1 (k)
                LOAD_CONST               6 (('brokerage_id', 'call_id', 'lead_id'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       22 (to L10)
                NOT_TAKEN

 140            LOAD_FAST_BORROW         0 (row)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_FAST_BORROW         1 (k)
                CALL                     1
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (out, k)
                STORE_SUBSCR
                JUMP_BACKWARD           95 (to L6)

 142   L10:     LOAD_GLOBAL             11 (get_contract_value + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (row, k)
                CALL                     2
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (out, k)
                STORE_SUBSCR
                JUMP_BACKWARD          110 (to L6)

 132   L11:     END_FOR
                POP_ITER

 143            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 129            SWAP                     2
                STORE_FAST               1 (k)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C1802CAE0, file "app\services\replay\event_reader.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('call_id')

147           LOAD_GLOBAL              0 (str)

146           LOAD_CONST               2 ('brokerage_id')

149           LOAD_GLOBAL              2 (Optional)
              LOAD_GLOBAL              0 (str)
              BINARY_OP               26 ([])

146           LOAD_CONST               3 ('allow_unscoped')

150           LOAD_GLOBAL              4 (bool)

146           LOAD_CONST               4 ('return')

151           LOAD_GLOBAL              6 (list)

146           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object load_call_events at 0x0000018C17F95E60, file "app\services\replay\event_reader.py", line 146>:
 146           RESUME                   0

 166           LOAD_GLOBAL              1 (require_tenant_or_unscoped + NULL)
               LOAD_CONST               1 ('load_call_events')
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (brokerage_id, allow_unscoped)
               CALL                     3
               POP_TOP

 167           LOAD_FAST_BORROW         0 (call_id)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 168           BUILD_LIST               0
               RETURN_VALUE

 169   L1:     LOAD_GLOBAL              3 (events_for_call + NULL)

 170           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (call_id, brokerage_id)
               LOAD_FAST_BORROW         2 (allow_unscoped)

 169           LOAD_CONST               2 (('brokerage_id', 'allow_unscoped'))
               CALL_KW                  3
               STORE_FAST               3 (raw)

 172           LOAD_FAST                3 (raw)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L2:     GET_ITER
               LOAD_FAST_AND_CLEAR      4 (r)
               SWAP                     2
       L3:     BUILD_LIST               0
               SWAP                     2
       L4:     FOR_ITER                14 (to L5)
               STORE_FAST               4 (r)
               LOAD_GLOBAL              5 (normalize_event + NULL)
               LOAD_FAST_BORROW         4 (r)
               CALL                     1
               LIST_APPEND              2
               JUMP_BACKWARD           16 (to L4)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST               4 (r)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 172           SWAP                     2
               STORE_FAST               4 (r)
               RERAISE                  0
ExceptionTable:
  L3 to L6 -> L7 [2]

Disassembly of <code object __annotate__ at 0x0000018C1802C750, file "app\services\replay\event_reader.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('call_id')

176           LOAD_GLOBAL              0 (str)

175           LOAD_CONST               2 ('brokerage_id')

178           LOAD_GLOBAL              2 (Optional)
              LOAD_GLOBAL              0 (str)
              BINARY_OP               26 ([])

175           LOAD_CONST               3 ('return')

179           LOAD_GLOBAL              4 (list)

175           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object load_call_events_unscoped at 0x0000018C17FA3960, file "app\services\replay\event_reader.py", line 175>:
175           RESUME                   0

186           LOAD_GLOBAL              1 (load_call_events + NULL)

187           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (call_id, brokerage_id)
              LOAD_CONST               1 (True)

186           LOAD_CONST               2 (('brokerage_id', 'allow_unscoped'))
              CALL_KW                  3
              RETURN_VALUE
```
