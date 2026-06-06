# ingestion/contracts

- **pyc:** `app\services\ingestion\__pycache__\contracts.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/contracts.py`
- **co_filename (from bytecode):** `app\services\ingestion\contracts.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS161 — Canonical normalized lead contract.

This is the ONE shape every provider normalizer must produce
and the only shape ``enqueue_pending_call`` will accept.

Hard doctrine:

* ``phone`` is required.
* ``source`` is required.
* ``brokerage_id`` is **never** a field on the normalized lead.
  Tenant scope is resolved from auth; carrying it here would
  invite a payload-trust regression.
* No ``raw_payload`` / ``full_payload`` / ``transcript`` /
  ``evidence`` / ``messages`` / ``utterances`` / ``lineage``
  keys. Period. The normalizers physically refuse to write
  them; the source-text test enforces it.
* ``metadata`` is a small dict allow-listed via
  ``ALLOWED_METADATA_KEYS``. Anything outside that allow-list
  is dropped during normalization.
```

## Imports

`Any`, `Dict`, `Optional`, `Tuple`, `__future__`, `annotations`, `asdict`, `dataclass`, `dataclasses`, `field`, `typing`

## Classes

`NormalizedLead`

## Functions / methods

_none_

## Env-key candidates

`ALLOWED_METADATA_KEYS`, `FORBIDDEN_NORMALIZED_KEYS`

## String constants (redacted where noted)

- '\nPAS161 — Canonical normalized lead contract.\n\nThis is the ONE shape every provider normalizer must produce\nand the only shape ``enqueue_pending_call`` will accept.\n\nHard doctrine:\n\n* ``phone`` is required.\n* ``source`` is required.\n* ``brokerage_id`` is **never** a field on the normalized lead.\n  Tenant scope is resolved from auth; carrying it here would\n  invite a payload-trust regression.\n* No ``raw_payload`` / ``full_payload`` / ``transcript`` /\n  ``evidence`` / ``messages`` / ``utterances`` / ``lineage``\n  keys. Period. The normalizers physically refuse to write\n  them; the source-text test enforces it.\n* ``metadata`` is a small dict allow-listed via\n  ``ALLOWED_METADATA_KEYS``. Anything outside that allow-list\n  is dropped during normalization.\n'
- 'Tuple[str, ...]'
- 'ALLOWED_METADATA_KEYS'
- 'FORBIDDEN_NORMALIZED_KEYS'
- 'NormalizedLead'
- 'Canonical normalized lead shape.\n\nEvery provider normalizer (generic / Zapier / FUB / GHL)\nproduces this exact shape. Routes accept ONLY this shape\nfrom the normalizers and hand it to ``enqueue_pending_call``.\n\n``phone`` is the only field treated as load-bearing — every\nother field is informational and may be ``None``.\n'
- 'str'
- 'phone'
- 'source'
- 'Optional[str]'
- 'lead_id'
- 'full_name'
- 'first_name'
- 'last_name'
- 'email'
- 'intent'
- 'property_address'
- 'city'
- 'state'
- 'budget'
- 'timeline'
- 'notes'
- 'raw_source_ref'
- 'Dict[str, Any]'
- 'metadata'
- 'return'
- 'Return a JSON-safe dict. Defensively drops any key in\n``FORBIDDEN_NORMALIZED_KEYS`` and trims ``metadata`` to\nthe closed allow-list.\n\nThis is the only sanctioned serialisation path. Routes\nshould NEVER call ``asdict()`` directly because that\npath bypasses the forbidden-key check.\n'
- 'bool'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS161 — Canonical normalized lead contract.\n\nThis is the ONE shape every provider normalizer must produce\nand the only shape ``enqueue_pending_call`` will accept.\n\nHard doctrine:\n\n* ``phone`` is required.\n* ``source`` is required.\n* ``brokerage_id`` is **never** a field on the normalized lead.\n  Tenant scope is resolved from auth; carrying it here would\n  invite a payload-trust regression.\n* No ``raw_payload`` / ``full_payload`` / ``transcript`` /\n  ``evidence`` / ``messages`` / ``utterances`` / ``lineage``\n  keys. Period. The normalizers physically refuse to write\n  them; the source-text test enforces it.\n* ``metadata`` is a small dict allow-listed via\n  ``ALLOWED_METADATA_KEYS``. Anything outside that allow-list\n  is dropped during normalization.\n')
               STORE_NAME               1 (__doc__)

  23           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  25           LOAD_SMALL_INT           0
               LOAD_CONST               2 (('dataclass', 'field', 'asdict'))
               IMPORT_NAME              4 (dataclasses)
               IMPORT_FROM              5 (dataclass)
               STORE_NAME               5 (dataclass)
               IMPORT_FROM              6 (field)
               STORE_NAME               6 (field)
               IMPORT_FROM              7 (asdict)
               STORE_NAME               7 (asdict)
               POP_TOP

  26           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Optional', 'Tuple'))
               IMPORT_NAME              8 (typing)
               IMPORT_FROM              9 (Any)
               STORE_NAME               9 (Any)
               IMPORT_FROM             10 (Dict)
               STORE_NAME              10 (Dict)
               IMPORT_FROM             11 (Optional)
               STORE_NAME              11 (Optional)
               IMPORT_FROM             12 (Tuple)
               STORE_NAME              12 (Tuple)
               POP_TOP

  33           LOAD_CONST              10 (('campaign', 'source_id', 'lead_source', 'property_type'))
               STORE_NAME              13 (ALLOWED_METADATA_KEYS)
               LOAD_CONST               4 ('Tuple[str, ...]')
               LOAD_NAME               14 (__annotations__)
               LOAD_CONST               5 ('ALLOWED_METADATA_KEYS')
               STORE_SUBSCR

  46           LOAD_CONST              11 (('raw_payload', 'full_payload', 'payload', 'transcript', 'raw_transcript', 'full_transcript', 'evidence', 'lineage', 'metadata_blob', 'messages', 'utterances', 'input_text', 'output_text', 'memory_content', 'raw_text', 'raw_prompt', 'injected_prompt', 'brokerage_id', 'api_key', 'X-API-Key'))
               STORE_NAME              15 (FORBIDDEN_NORMALIZED_KEYS)
               LOAD_CONST               4 ('Tuple[str, ...]')
               LOAD_NAME               14 (__annotations__)
               LOAD_CONST               6 ('FORBIDDEN_NORMALIZED_KEYS')
               STORE_SUBSCR

  73           LOAD_NAME                5 (dataclass)

  74           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               7 (<code object NormalizedLead at 0x0000018C17F003E0, file "app\services\ingestion\contracts.py", line 73>)
               MAKE_FUNCTION
               LOAD_CONST               8 ('NormalizedLead')
               CALL                     2

  73           CALL                     0

  74           STORE_NAME              16 (NormalizedLead)
               LOAD_CONST               9 (None)
               RETURN_VALUE

Disassembly of <code object NormalizedLead at 0x0000018C17F003E0, file "app\services\ingestion\contracts.py", line 73>:
 73           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('NormalizedLead')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          73
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 75           LOAD_CONST               1 ('Canonical normalized lead shape.\n\nEvery provider normalizer (generic / Zapier / FUB / GHL)\nproduces this exact shape. Routes accept ONLY this shape\nfrom the normalizers and hand it to ``enqueue_pending_call``.\n\n``phone`` is the only field treated as load-bearing — every\nother field is informational and may be ``None``.\n')
              STORE_NAME               4 (__doc__)

 86           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('phone')
              STORE_SUBSCR

 87           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('source')
              STORE_SUBSCR

 90           LOAD_CONST               5 (None)
              STORE_NAME               6 (lead_id)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               7 ('lead_id')
              STORE_SUBSCR

 91           LOAD_CONST               5 (None)
              STORE_NAME               7 (full_name)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               8 ('full_name')
              STORE_SUBSCR

 92           LOAD_CONST               5 (None)
              STORE_NAME               8 (first_name)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               9 ('first_name')
              STORE_SUBSCR

 93           LOAD_CONST               5 (None)
              STORE_NAME               9 (last_name)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              10 ('last_name')
              STORE_SUBSCR

 94           LOAD_CONST               5 (None)
              STORE_NAME              10 (email)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              11 ('email')
              STORE_SUBSCR

 97           LOAD_CONST               5 (None)
              STORE_NAME              11 (intent)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              12 ('intent')
              STORE_SUBSCR

 98           LOAD_CONST               5 (None)
              STORE_NAME              12 (property_address)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              13 ('property_address')
              STORE_SUBSCR

 99           LOAD_CONST               5 (None)
              STORE_NAME              13 (city)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              14 ('city')
              STORE_SUBSCR

100           LOAD_CONST               5 (None)
              STORE_NAME              14 (state)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              15 ('state')
              STORE_SUBSCR

101           LOAD_CONST               5 (None)
              STORE_NAME              15 (budget)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              16 ('budget')
              STORE_SUBSCR

102           LOAD_CONST               5 (None)
              STORE_NAME              16 (timeline)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              17 ('timeline')
              STORE_SUBSCR

103           LOAD_CONST               5 (None)
              STORE_NAME              17 (notes)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              18 ('notes')
              STORE_SUBSCR

109           LOAD_CONST               5 (None)
              STORE_NAME              18 (raw_source_ref)
              LOAD_CONST               6 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              19 ('raw_source_ref')
              STORE_SUBSCR

113           LOAD_NAME               19 (field)
              PUSH_NULL
              LOAD_NAME               20 (dict)
              LOAD_CONST              20 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              21 (metadata)
              LOAD_CONST              21 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              22 ('metadata')
              STORE_SUBSCR

115           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\contracts.py", line 115>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object to_dict at 0x0000018C179A7290, file "app\services\ingestion\contracts.py", line 115>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (to_dict)

143           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\contracts.py", line 143>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object has_email at 0x0000018C18038A30, file "app\services\ingestion\contracts.py", line 143>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (has_email)

146           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\contracts.py", line 146>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object has_budget at 0x0000018C18038CB0, file "app\services\ingestion\contracts.py", line 146>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (has_budget)

149           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\contracts.py", line 149>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object has_timeline at 0x0000018C18038B70, file "app\services\ingestion\contracts.py", line 149>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (has_timeline)
              LOAD_CONST              31 (())
              STORE_NAME              26 (__static_attributes__)
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\ingestion\contracts.py", line 115>:
115           RESUME                   0
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

Disassembly of <code object to_dict at 0x0000018C179A7290, file "app\services\ingestion\contracts.py", line 115>:
 115            RESUME                   0

 124            LOAD_GLOBAL              1 (asdict + NULL)
                LOAD_FAST_BORROW         0 (self)
                CALL                     1
                STORE_FAST               1 (raw)

 130            LOAD_GLOBAL              2 (FORBIDDEN_NORMALIZED_KEYS)
                GET_ITER
        L1:     FOR_ITER                21 (to L2)
                STORE_FAST               2 (k)

 131            LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR                5 (pop + NULL|self)
                LOAD_FAST_BORROW         2 (k)
                LOAD_CONST               1 (None)
                CALL                     2
                POP_TOP
                JUMP_BACKWARD           23 (to L1)

 130    L2:     END_FOR
                POP_ITER

 133            LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L3:     STORE_FAST               3 (meta)

 134            LOAD_GLOBAL              9 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (meta)
                LOAD_GLOBAL             10 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN

 135            BUILD_MAP                0
                STORE_FAST               3 (meta)

 138    L4:     LOAD_GLOBAL             12 (ALLOWED_METADATA_KEYS)
                GET_ITER

 136            LOAD_FAST_AND_CLEAR      2 (k)
                SWAP                     2
        L5:     BUILD_MAP                0
                SWAP                     2

 138    L6:     FOR_ITER                20 (to L9)
                STORE_FAST               2 (k)

 139            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (k, meta)
                CONTAINS_OP              0 (in)

 137    L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L6)
        L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (k, meta)
                LOAD_FAST_BORROW         2 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           22 (to L6)

 138    L9:     END_FOR
                POP_ITER

 136   L10:     SWAP                     2
                STORE_FAST               2 (k)
                LOAD_FAST_BORROW         1 (raw)
                LOAD_CONST               2 ('metadata')
                STORE_SUBSCR

 141            LOAD_FAST_BORROW         1 (raw)
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 136            SWAP                     2
                STORE_FAST               2 (k)
                RERAISE                  0
ExceptionTable:
  L5 to L7 -> L11 [2]
  L8 to L10 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\ingestion\contracts.py", line 143>:
143           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object has_email at 0x0000018C18038A30, file "app\services\ingestion\contracts.py", line 143>:
143           RESUME                   0

144           LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (email)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (email)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
      L1:     CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\contracts.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object has_budget at 0x0000018C18038CB0, file "app\services\ingestion\contracts.py", line 146>:
146           RESUME                   0

147           LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (budget)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (budget)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
      L1:     CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\contracts.py", line 149>:
149           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object has_timeline at 0x0000018C18038B70, file "app\services\ingestion\contracts.py", line 149>:
149           RESUME                   0

150           LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (timeline)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (timeline)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
      L1:     CALL                     1
              RETURN_VALUE
```
