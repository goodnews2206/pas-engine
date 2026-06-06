# security/error_safety

- **pyc:** `app\services\security\__pycache__\error_safety.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/error_safety.py`
- **co_filename (from bytecode):** `app/services/security/error_safety.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-01 — Public-response error-safety helpers.

Defensive helpers that collapse raw exceptions to a closed
structural error envelope and scan response envelopes for any
content that would leak server-side detail to the client.

Doctrine:

* **No raw exception text in public responses.** ``to_public_error(e)``
  returns a closed envelope whose ``error_code`` is
  ``unexpected:<ExceptionTypeName>`` — never ``str(e)``, never
  ``repr(e)``, never the traceback.
* **No stack traces in public responses.** ``scan_response_for_leaks``
  walks an envelope and flags any field whose value contains a
  stack-trace marker (``Traceback (most recent call last)``,
  ``File "...py", line N``, etc.).
* **No secrets in public responses.** The scanner also rejects
  any field whose lowercased key matches the closed
  ``FORBIDDEN_RESPONSE_FIELDS`` blocklist (token / api_key /
  secret / signature / env_value / ...).
* **NEVER raises.** All helpers return structural envelopes.

Public surface:

  * ``FORBIDDEN_RESPONSE_FIELDS``                — PII / secret blocklist.
  * ``STACK_TRACE_MARKERS``                      — substring blocklist.
  * ``to_public_error(exc)``                     — structural error envelope.
  * ``scan_response_for_leaks(envelope)``        — verdict envelope.
  * ``redact_response(envelope)``                — drops forbidden keys.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_safe_class_name`, `_walk_dict_keys`, `_walk_strings`, `redact_response`, `scan_response_for_leaks`, `to_public_error`

## Env-key candidates

`FORBIDDEN_RESPONSE_FIELDS`, `STACK_TRACE_MARKERS`

## String constants (redacted where noted)

- '\nPAS-SECURITY-01 — Public-response error-safety helpers.\n\nDefensive helpers that collapse raw exceptions to a closed\nstructural error envelope and scan response envelopes for any\ncontent that would leak server-side detail to the client.\n\nDoctrine:\n\n* **No raw exception text in public responses.** ``to_public_error(e)``\n  returns a closed envelope whose ``error_code`` is\n  ``unexpected:<ExceptionTypeName>`` — never ``str(e)``, never\n  ``repr(e)``, never the traceback.\n* **No stack traces in public responses.** ``scan_response_for_leaks``\n  walks an envelope and flags any field whose value contains a\n  stack-trace marker (``Traceback (most recent call last)``,\n  ``File "...py", line N``, etc.).\n* **No secrets in public responses.** The scanner also rejects\n  any field whose lowercased key matches the closed\n  ``FORBIDDEN_RESPONSE_FIELDS`` blocklist (token / api_key /\n  secret / signature / env_value / ...).\n* **NEVER raises.** All helpers return structural envelopes.\n\nPublic surface:\n\n  * ``FORBIDDEN_RESPONSE_FIELDS``                — PII / secret blocklist.\n  * ``STACK_TRACE_MARKERS``                      — substring blocklist.\n  * ``to_public_error(exc)``                     — structural error envelope.\n  * ``scan_response_for_leaks(envelope)``        — verdict envelope.\n  * ``redact_response(envelope)``                — drops forbidden keys.\n'
- 'pas.security.error_safety'
- 'Tuple[str, ...]'
- 'FORBIDDEN_RESPONSE_FIELDS'
- 'STACK_TRACE_MARKERS'
- 'surface'
- 'path'
- 'out'
- 'exc'
- 'Any'
- 'return'
- 'str'
- 'UnknownError'
- 'Optional[str]'
- 'Dict[str, Any]'
- "Return a closed-shape public error envelope. NEVER\nraises. NEVER returns the exception's message body."
- 'status'
- 'failed'
- 'error_code'
- 'unexpected:'
- 'warnings'
- 'unexpected:UnknownError'
- 'envelope'
- 'Optional[List[Tuple[str, str]]]'
- 'List[Tuple[str, str]]'
- 'Walk every string leaf in the envelope. Returns\n[(path, value)] list. NEVER raises.'
- 'Walk an envelope and return a verdict envelope listing\nany forbidden-key or stack-trace leaks. NEVER raises.'
- 'forbidden_response_field'
- 'stack_trace_in_response'
- 'valid'
- 'found'
- 'scan_response_for_leaks error type='
- 'Return a shallow copy of ``envelope`` with any forbidden\ntop-level keys dropped. NEVER raises.'
- 'redact_response error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-01 — Public-response error-safety helpers.\n\nDefensive helpers that collapse raw exceptions to a closed\nstructural error envelope and scan response envelopes for any\ncontent that would leak server-side detail to the client.\n\nDoctrine:\n\n* **No raw exception text in public responses.** ``to_public_error(e)``\n  returns a closed envelope whose ``error_code`` is\n  ``unexpected:<ExceptionTypeName>`` — never ``str(e)``, never\n  ``repr(e)``, never the traceback.\n* **No stack traces in public responses.** ``scan_response_for_leaks``\n  walks an envelope and flags any field whose value contains a\n  stack-trace marker (``Traceback (most recent call last)``,\n  ``File "...py", line N``, etc.).\n* **No secrets in public responses.** The scanner also rejects\n  any field whose lowercased key matches the closed\n  ``FORBIDDEN_RESPONSE_FIELDS`` blocklist (token / api_key /\n  secret / signature / env_value / ...).\n* **NEVER raises.** All helpers return structural envelopes.\n\nPublic surface:\n\n  * ``FORBIDDEN_RESPONSE_FIELDS``                — PII / secret blocklist.\n  * ``STACK_TRACE_MARKERS``                      — substring blocklist.\n  * ``to_public_error(exc)``                     — structural error envelope.\n  * ``scan_response_for_leaks(envelope)``        — verdict envelope.\n  * ``redact_response(envelope)``                — drops forbidden keys.\n')
               STORE_NAME               1 (__doc__)

  33           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  35           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  36           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (List)
               STORE_NAME               8 (List)
               IMPORT_FROM              9 (Optional)
               STORE_NAME               9 (Optional)
               IMPORT_FROM             10 (Tuple)
               STORE_NAME              10 (Tuple)
               POP_TOP

  39           LOAD_NAME                4 (logging)
               LOAD_ATTR               22 (getLogger)
               PUSH_NULL
               LOAD_CONST               4 ('pas.security.error_safety')
               CALL                     1
               STORE_NAME              12 (logger)

  44           LOAD_CONST              24 (('phone', 'email', 'name', 'address', 'street', 'raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'summary', 'secret', 'signature', 'token', 'api_key', 'env_value', 'env_values', 'dedupe_key', 'callback_notes', 'stack_trace', 'traceback', 'rationale_text', 'rationale_freeform', 'prompt_text', 'live_mutation_payload', 'evidence_raw'))
               STORE_NAME              13 (FORBIDDEN_RESPONSE_FIELDS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               14 (__annotations__)
               LOAD_CONST               6 ('FORBIDDEN_RESPONSE_FIELDS')
               STORE_SUBSCR

  80           LOAD_CONST              25 (('Traceback (most recent call last)', 'File "', '  File ', 'Traceback:', 'self.fail(', 'raise ', 'Stacktrace:', '    at '))
               STORE_NAME              15 (STACK_TRACE_MARKERS)
               LOAD_CONST               5 ('Tuple[str, ...]')
               LOAD_NAME               14 (__annotations__)
               LOAD_CONST               7 ('STACK_TRACE_MARKERS')
               STORE_SUBSCR

  92           LOAD_SMALL_INT          64
               STORE_NAME              16 (_EXC_TYPE_MAX_LEN)

  95           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/error_safety.py", line 95>)
               MAKE_FUNCTION
               LOAD_CONST               9 (<code object _safe_class_name at 0x0000018C17E7D9A0, file "app/services/security/error_safety.py", line 95>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              17 (_safe_class_name)

 111           LOAD_CONST              10 ('surface')

 114           LOAD_CONST               2 (None)

 111           BUILD_MAP                1
               LOAD_CONST              11 (<code object __annotate__ at 0x0000018C18025C30, file "app/services/security/error_safety.py", line 111>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object to_public_error at 0x0000018C17FEDC30, file "app/services/security/error_safety.py", line 111>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              18 (to_public_error)

 135           LOAD_CONST              13 ('path')

 138           LOAD_CONST              14 ('')

 135           LOAD_CONST              15 ('out')

 139           LOAD_CONST               2 (None)

 135           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18026430, file "app/services/security/error_safety.py", line 135>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _walk_strings at 0x0000018C17CD0CE0, file "app/services/security/error_safety.py", line 135>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              19 (_walk_strings)

 159           LOAD_CONST              13 ('path')

 162           LOAD_CONST              14 ('')

 159           LOAD_CONST              15 ('out')

 163           LOAD_CONST               2 (None)

 159           BUILD_MAP                2
               LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/security/error_safety.py", line 159>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _walk_dict_keys at 0x0000018C17CD2160, file "app/services/security/error_safety.py", line 159>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              20 (_walk_dict_keys)

 181           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/error_safety.py", line 181>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object scan_response_for_leaks at 0x0000018C182F49F0, file "app/services/security/error_safety.py", line 181>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (scan_response_for_leaks)

 226           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/error_safety.py", line 226>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object redact_response at 0x0000018C17D8E300, file "app/services/security/error_safety.py", line 226>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              22 (redact_response)

 252           BUILD_LIST               0
               LOAD_CONST              26 (('FORBIDDEN_RESPONSE_FIELDS', 'STACK_TRACE_MARKERS', 'to_public_error', 'scan_response_for_leaks', 'redact_response'))
               LIST_EXTEND              1
               STORE_NAME              23 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/error_safety.py", line 95>:
 95           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('exc')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_class_name at 0x0000018C17E7D9A0, file "app/services/security/error_safety.py", line 95>:
  95            RESUME                   0

  96            NOP

  97    L1:     LOAD_GLOBAL              1 (type + NULL)
                LOAD_FAST_BORROW         0 (exc)
                CALL                     1
                LOAD_ATTR                2 (__name__)
                STORE_FAST               1 (name)

  98            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (name)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (name)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN

  99    L3:     LOAD_CONST               0 ('UnknownError')
                RETURN_VALUE

 101    L4:     BUILD_LIST               0
                STORE_FAST               2 (keep)

 102            LOAD_FAST_BORROW         1 (name)
                LOAD_CONST               1 (None)
                LOAD_GLOBAL              8 (_EXC_TYPE_MAX_LEN)
                BINARY_SLICE
                GET_ITER
        L5:     FOR_ITER                51 (to L8)
                STORE_FAST               3 (ch)

 103            LOAD_FAST_BORROW         3 (ch)
                LOAD_ATTR               11 (isalnum + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (ch)
                LOAD_CONST               2 ('_')
                COMPARE_OP              88 (bool(==))
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           34 (to L5)

 104    L7:     LOAD_FAST_BORROW         2 (keep)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         3 (ch)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           53 (to L5)

 102    L8:     END_FOR
                POP_ITER

 105            LOAD_CONST               3 ('')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         2 (keep)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
        L9:     NOT_TAKEN
       L10:     POP_TOP
                LOAD_CONST               0 ('UnknownError')
       L11:     STORE_FAST               4 (cleaned)

 106            LOAD_FAST_BORROW         4 (cleaned)
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 107            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L15)
                NOT_TAKEN
                POP_TOP

 108   L14:     POP_EXCEPT
                LOAD_CONST               0 ('UnknownError')
                RETURN_VALUE

 107   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L4 to L6 -> L13 [0]
  L7 to L9 -> L13 [0]
  L10 to L12 -> L13 [0]
  L13 to L14 -> L16 [1] lasti
  L15 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app/services/security/error_safety.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('exc')

112           LOAD_CONST               2 ('Any')

111           LOAD_CONST               3 ('surface')

114           LOAD_CONST               4 ('Optional[str]')

111           LOAD_CONST               5 ('return')

115           LOAD_CONST               6 ('Dict[str, Any]')

111           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object to_public_error at 0x0000018C17FEDC30, file "app/services/security/error_safety.py", line 111>:
 111            RESUME                   0

 118            NOP

 119    L1:     LOAD_GLOBAL              1 (_safe_class_name + NULL)
                LOAD_FAST_BORROW         0 (exc)
                CALL                     1
                STORE_FAST               2 (cls)

 121            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 122            LOAD_CONST               3 ('surface')
                LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (surface)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (surface)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
        L2:     NOT_TAKEN
        L3:     LOAD_FAST                1 (surface)
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               4 (None)

 123    L5:     LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('unexpected:')
                LOAD_FAST_BORROW         2 (cls)
                FORMAT_SIMPLE
                BUILD_STRING             2

 124            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 120            BUILD_MAP                4
        L6:     RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 126            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       60 (to L13)
                NOT_TAKEN
                POP_TOP

 128            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 129            LOAD_CONST               3 ('surface')
                LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST                1 (surface)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN
                LOAD_FAST                1 (surface)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
        L8:     NOT_TAKEN
        L9:     LOAD_FAST                1 (surface)
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               4 (None)

 130   L11:     LOAD_CONST               5 ('error_code')
                LOAD_CONST               8 ('unexpected:UnknownError')

 131            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 127            BUILD_MAP                4
                SWAP                     2
       L12:     POP_EXCEPT
                RETURN_VALUE

 126   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L3 to L6 -> L7 [0]
  L7 to L8 -> L14 [1] lasti
  L9 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app/services/security/error_safety.py", line 135>:
135           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')

136           LOAD_CONST               2 ('Any')

135           LOAD_CONST               3 ('path')

138           LOAD_CONST               4 ('str')

135           LOAD_CONST               5 ('out')

139           LOAD_CONST               6 ('Optional[List[Tuple[str, str]]]')

135           LOAD_CONST               7 ('return')

140           LOAD_CONST               8 ('List[Tuple[str, str]]')

135           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _walk_strings at 0x0000018C17CD0CE0, file "app/services/security/error_safety.py", line 135>:
 135            RESUME                   0

 143            LOAD_FAST_BORROW         2 (out)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 144            BUILD_LIST               0
                STORE_FAST               2 (out)

 145    L1:     NOP

 146    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       65 (to L8)
                NOT_TAKEN

 147            LOAD_FAST_BORROW         0 (envelope)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L3:     FOR_ITER                42 (to L6)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (k, v)

 148            LOAD_GLOBAL              7 (_walk_strings + NULL)
                LOAD_FAST_LOAD_FAST     65 (v, path)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (path)
                FORMAT_SIMPLE
                LOAD_CONST               1 ('.')
                LOAD_FAST_BORROW         3 (k)
                FORMAT_SIMPLE
                BUILD_STRING             3
                JUMP_FORWARD            10 (to L5)
        L4:     LOAD_GLOBAL              9 (str + NULL)
                LOAD_FAST_BORROW         3 (k)
                CALL                     1
        L5:     LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           44 (to L3)

 147    L6:     END_FOR
                POP_ITER

 156    L7:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 149    L8:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL             10 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L12)
                NOT_TAKEN

 150            LOAD_GLOBAL             13 (enumerate + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                GET_ITER
        L9:     FOR_ITER                24 (to L10)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   84 (i, v)

 151            LOAD_GLOBAL              7 (_walk_strings + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (v, path)
                FORMAT_SIMPLE
                LOAD_CONST               3 ('[')
                LOAD_FAST_BORROW         5 (i)
                FORMAT_SIMPLE
                LOAD_CONST               4 (']')
                BUILD_STRING             4
                LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           26 (to L9)

 150   L10:     END_FOR
                POP_ITER

 156   L11:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 152   L12:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
                NOT_TAKEN

 153            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (path, envelope)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP

 156   L13:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 154            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L16)
                NOT_TAKEN
                POP_TOP

 155   L15:     POP_EXCEPT

 156            LOAD_FAST                2 (out)
                RETURN_VALUE

 154   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L7 -> L14 [0]
  L8 to L11 -> L14 [0]
  L12 to L13 -> L14 [0]
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/security/error_safety.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')

160           LOAD_CONST               2 ('Any')

159           LOAD_CONST               3 ('path')

162           LOAD_CONST               4 ('str')

159           LOAD_CONST               5 ('out')

163           LOAD_CONST               6 ('Optional[List[Tuple[str, str]]]')

159           LOAD_CONST               7 ('return')

164           LOAD_CONST               8 ('List[Tuple[str, str]]')

159           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _walk_dict_keys at 0x0000018C17CD2160, file "app/services/security/error_safety.py", line 159>:
 159            RESUME                   0

 165            LOAD_FAST_BORROW         2 (out)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 166            BUILD_LIST               0
                STORE_FAST               2 (out)

 167    L1:     NOP

 168    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      105 (to L9)
                NOT_TAKEN

 169            LOAD_FAST_BORROW         0 (envelope)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L3:     FOR_ITER                82 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (k, v)

 170            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L4)
                NOT_TAKEN

 171            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (path, k)
                BUILD_TUPLE              2
                CALL                     1
                POP_TOP

 172    L4:     LOAD_GLOBAL             11 (_walk_dict_keys + NULL)
                LOAD_FAST_LOAD_FAST     65 (v, path)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (path)
                FORMAT_SIMPLE
                LOAD_CONST               1 ('.')
                LOAD_FAST_BORROW         3 (k)
                FORMAT_SIMPLE
                BUILD_STRING             3
                JUMP_FORWARD            10 (to L6)
        L5:     LOAD_GLOBAL              7 (str + NULL)
                LOAD_FAST_BORROW         3 (k)
                CALL                     1
        L6:     LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           84 (to L3)

 169    L7:     END_FOR
                POP_ITER

 178    L8:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 173    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL             12 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       40 (to L12)
                NOT_TAKEN

 174            LOAD_GLOBAL             15 (enumerate + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                GET_ITER
       L10:     FOR_ITER                24 (to L11)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   84 (i, v)

 175            LOAD_GLOBAL             11 (_walk_dict_keys + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (v, path)
                FORMAT_SIMPLE
                LOAD_CONST               3 ('[')
                LOAD_FAST_BORROW         5 (i)
                FORMAT_SIMPLE
                LOAD_CONST               4 (']')
                BUILD_STRING             4
                LOAD_FAST_BORROW         2 (out)
                LOAD_CONST               2 (('path', 'out'))
                CALL_KW                  3
                POP_TOP
                JUMP_BACKWARD           26 (to L10)

 174   L11:     END_FOR
                POP_ITER

 178   L12:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 176            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L15)
                NOT_TAKEN
                POP_TOP

 177   L14:     POP_EXCEPT

 178            LOAD_FAST                2 (out)
                RETURN_VALUE

 176   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L8 -> L13 [0]
  L9 to L12 -> L13 [0]
  L13 to L14 -> L16 [1] lasti
  L15 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/security/error_safety.py", line 181>:
181           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object scan_response_for_leaks at 0x0000018C182F49F0, file "app/services/security/error_safety.py", line 181>:
 181            RESUME                   0

 184            NOP

 186    L1:     LOAD_GLOBAL              1 (_walk_dict_keys + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                STORE_FAST               1 (keys)

 187            BUILD_LIST               0
                STORE_FAST               2 (bad_keys)

 188            LOAD_FAST_BORROW         1 (keys)
                GET_ITER
        L2:     FOR_ITER                75 (to L11)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (path, k)

 189            LOAD_FAST_BORROW         4 (k)
                LOAD_ATTR                3 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (kl)

 190            LOAD_GLOBAL              4 (FORBIDDEN_RESPONSE_FIELDS)
                GET_ITER
        L3:     FOR_ITER                44 (to L10)
                STORE_FAST               6 (forb)

 191            LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (forb, kl)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)

 192    L5:     LOAD_FAST                2 (bad_keys)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_FAST_BORROW         3 (path)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L8)
        L6:     NOT_TAKEN
        L7:     LOAD_FAST_BORROW         3 (path)
                FORMAT_SIMPLE
                LOAD_CONST               1 ('.')
                LOAD_FAST_BORROW         4 (k)
                FORMAT_SIMPLE
                BUILD_STRING             3
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_FAST                4 (k)
        L9:     CALL                     1
                POP_TOP

 193            POP_TOP
                JUMP_BACKWARD           73 (to L2)

 190   L10:     END_FOR
                POP_ITER
                JUMP_BACKWARD           77 (to L2)

 188   L11:     END_FOR
                POP_ITER

 195            BUILD_LIST               0
                STORE_FAST               7 (bad_traces)

 196            LOAD_GLOBAL              9 (_walk_strings + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                CALL                     1
                STORE_FAST               8 (leaves)

 197            LOAD_FAST_BORROW         8 (leaves)
                GET_ITER
       L12:     FOR_ITER                44 (to L17)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   57 (path, v)

 198            LOAD_GLOBAL             10 (STACK_TRACE_MARKERS)
                GET_ITER
       L13:     FOR_ITER                29 (to L16)
                STORE_FAST              10 (marker)

 199            LOAD_FAST_BORROW_LOAD_FAST_BORROW 169 (marker, v)
                CONTAINS_OP              0 (in)
       L14:     POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L13)

 200   L15:     LOAD_FAST_BORROW         7 (bad_traces)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_FAST_BORROW         3 (path)
                CALL                     1
                POP_TOP

 201            POP_TOP
                JUMP_BACKWARD           42 (to L12)

 198   L16:     END_FOR
                POP_ITER
                JUMP_BACKWARD           46 (to L12)

 197   L17:     END_FOR
                POP_ITER

 202            LOAD_FAST_BORROW         2 (bad_keys)
                TO_BOOL
                UNARY_NOT
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                LOAD_FAST_BORROW         7 (bad_traces)
                TO_BOOL
                UNARY_NOT
       L20:     STORE_FAST              11 (valid)

 203            LOAD_CONST               2 (None)
                STORE_FAST              12 (error_code)

 204            LOAD_FAST_BORROW         2 (bad_keys)
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L23)
       L21:     NOT_TAKEN

 205   L22:     LOAD_CONST               3 ('forbidden_response_field')
                STORE_FAST              12 (error_code)
                JUMP_FORWARD            10 (to L26)

 206   L23:     LOAD_FAST_BORROW         7 (bad_traces)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
       L24:     NOT_TAKEN

 207   L25:     LOAD_CONST               4 ('stack_trace_in_response')
                STORE_FAST              12 (error_code)

 209   L26:     LOAD_CONST               5 ('valid')
                LOAD_FAST_BORROW        11 (valid)

 210            LOAD_CONST               6 ('error_code')
                LOAD_FAST_BORROW        12 (error_code)

 211            LOAD_CONST               7 ('found')
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL             15 (set + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (bad_keys, bad_traces)
                BINARY_OP                0 (+)
                CALL                     1
                CALL                     1
                LOAD_CONST               8 (slice(None, 25, None))
                BINARY_OP               26 ([])

 212            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 208            BUILD_MAP                4
       L27:     RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 214            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      109 (to L33)
                NOT_TAKEN
                STORE_FAST              13 (e)

 215   L29:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 216            LOAD_CONST              10 ('scan_response_for_leaks error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 215            CALL                     1
                POP_TOP

 219            LOAD_CONST               5 ('valid')
                LOAD_CONST              11 (False)

 220            LOAD_CONST               6 ('error_code')
                LOAD_CONST              12 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 221            LOAD_CONST               7 ('found')
                BUILD_LIST               0

 222            LOAD_CONST               9 ('warnings')
                LOAD_CONST              12 ('unexpected:')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 218            BUILD_MAP                4
       L30:     SWAP                     2
       L31:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L32:     LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 214   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L4 -> L28 [0]
  L5 to L6 -> L28 [0]
  L7 to L14 -> L28 [0]
  L15 to L18 -> L28 [0]
  L19 to L21 -> L28 [0]
  L22 to L24 -> L28 [0]
  L25 to L27 -> L28 [0]
  L28 to L29 -> L34 [1] lasti
  L29 to L30 -> L32 [1] lasti
  L30 to L31 -> L34 [1] lasti
  L32 to L34 -> L34 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app/services/security/error_safety.py", line 226>:
226           RESUME                   0
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
              LOAD_CONST               2 ('Any')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object redact_response at 0x0000018C17D8E300, file "app/services/security/error_safety.py", line 226>:
 226            RESUME                   0

 229            NOP

 230    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 231            LOAD_FAST_BORROW         0 (envelope)
        L2:     RETURN_VALUE

 232    L3:     BUILD_MAP                0
                STORE_FAST               1 (out)

 233            LOAD_FAST_BORROW         0 (envelope)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                84 (to L13)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (k, v)

 234            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 235            JUMP_BACKWARD           29 (to L4)

 236    L5:     LOAD_FAST_BORROW         2 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               4 (kl)

 237            LOAD_CONST               1 (True)
                STORE_FAST               5 (keep)

 238            LOAD_GLOBAL             10 (FORBIDDEN_RESPONSE_FIELDS)
                GET_ITER
        L6:     FOR_ITER                13 (to L9)
                STORE_FAST               6 (forb)

 239            LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (forb, kl)
                CONTAINS_OP              0 (in)
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L6)

 240    L8:     LOAD_CONST               2 (False)
                STORE_FAST               5 (keep)

 241            POP_TOP
                JUMP_FORWARD             2 (to L10)

 238    L9:     END_FOR
                POP_ITER

 242   L10:     LOAD_FAST_BORROW         5 (keep)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           80 (to L4)

 243   L12:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
                LOAD_FAST_BORROW         2 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           86 (to L4)

 233   L13:     END_FOR
                POP_ITER

 244            LOAD_FAST_BORROW         1 (out)
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 245            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 246   L16:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 247            LOAD_CONST               3 ('redact_response error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 246            CALL                     1
                POP_TOP

 249            LOAD_FAST                0 (envelope)
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               4 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 245   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L15 [0]
  L3 to L7 -> L15 [0]
  L8 to L11 -> L15 [0]
  L12 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
```
