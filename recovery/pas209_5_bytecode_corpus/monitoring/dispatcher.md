# monitoring/dispatcher

- **pyc:** `app\services\monitoring\__pycache__\dispatcher.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/dispatcher.py`
- **co_filename (from bytecode):** `app\services\monitoring\dispatcher.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS143F2 — Monitoring dispatcher.

Pure in-process dispatch only. No Slack, no email, no webhooks. The
dispatcher's job is to:

  1. normalize whatever input a detector hands it into a valid Alert,
  2. apply PII redaction (phone/email patterns) to title/description/
     metadata strings BEFORE the alert leaves Python memory,
  3. return a JSON-safe dict the caller can persist.

PAS143G will add transport (webhook / Slack / pager). This file
intentionally does NOT touch the network.

Doctrine: never raise. A misbehaving detector should produce an empty
alert dict, not crash the monitoring loop.
```

## Imports

`Alert`, `Any`, `Category`, `Dict`, `List`, `Optional`, `Severity`, `__future__`, `annotations`, `app.services.monitoring.contracts`, `app.services.monitoring.slack_alert_transport`, `app.utils.safe_log`, `redact_pii`, `send_alerts_to_slack`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_redact_string_values`, `alert_to_safe_dict`, `emit_alert`, `emit_alerts`, `emit_alerts_to_slack`, `normalize_alert`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS143F2 — Monitoring dispatcher.\n\nPure in-process dispatch only. No Slack, no email, no webhooks. The\ndispatcher's job is to:\n\n  1. normalize whatever input a detector hands it into a valid Alert,\n  2. apply PII redaction (phone/email patterns) to title/description/\n     metadata strings BEFORE the alert leaves Python memory,\n  3. return a JSON-safe dict the caller can persist.\n\nPAS143G will add transport (webhook / Slack / pager). This file\nintentionally does NOT touch the network.\n\nDoctrine: never raise. A misbehaving detector should produce an empty\nalert dict, not crash the monitoring loop.\n"
- 'webhook_url'
- 'brokerage'
- 'include_metadata'
- 'alert_or_dict'
- 'Any'
- 'return'
- 'Optional[Alert]'
- '\nCoerce input to an Alert. Returns None on bad input.\n\nAccepts:\n  - Alert instance              (returned unchanged)\n  - dict with required keys     (constructed via Alert(**...))\n  - anything else               → None\n\nNever raises. Validation errors from Alert.__post_init__ are caught\nand result in None — the caller decides what to do.\n'
- '\nWalk a dict/list structure and replace string values with their\nPII-redacted form. Non-string scalars are passed through.\nBounded depth via recursion (safe for the small dicts our alerts\ncarry; we cap recursion implicitly by not calling on cycles).\n'
- 'alert'
- 'Dict[str, Any]'
- '\nRender an Alert (or dict) as a JSON-safe dict with all string\nvalues redacted of phone/email patterns.\n\nReturns {} on bad input. Never raises.\n'
- 'title'
- 'description'
- 'metadata'
- '_invalid_metadata_type'
- '\nPublic API. Returns the JSON-safe, PII-redacted dict.\n\nPAS143F2: in-process only. PAS143G will swap this for a transport.\n\nNever raises. Returns {} on any failure.\n'
- 'alerts'
- 'List[Any]'
- 'List[Dict[str, Any]]'
- '\nConvenience: emit each alert and drop empties (the result of\nbad input). Order-preserving.\n'
- 'Optional[str]'
- 'bool'
- 'Optional bridge from the in-process Alert pipeline to a\nSlack webhook destination (PAS170).\n\nEach alert is normalised + PII-redacted via the existing\n``alert_to_safe_dict`` path, then handed to\n:mod:`app.services.monitoring.slack_alert_transport`. The\nSlack transport is fail-soft — a missing webhook / HTTP\nerror returns a structural envelope, never raises.\n\nPAS170 ships this as an **opt-in seam**. The monitoring\ndetectors do NOT call this automatically; an operator\nscript or readiness check is the canonical caller.\n\nReturns one structural envelope per input alert. Never\nraises.\n'
- 'status'
- 'failed'
- 'warnings'
- 'transport_import_failed:'
- 'error_code'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS143F2 — Monitoring dispatcher.\n\nPure in-process dispatch only. No Slack, no email, no webhooks. The\ndispatcher's job is to:\n\n  1. normalize whatever input a detector hands it into a valid Alert,\n  2. apply PII redaction (phone/email patterns) to title/description/\n     metadata strings BEFORE the alert leaves Python memory,\n  3. return a JSON-safe dict the caller can persist.\n\nPAS143G will add transport (webhook / Slack / pager). This file\nintentionally does NOT touch the network.\n\nDoctrine: never raise. A misbehaving detector should produce an empty\nalert dict, not crash the monitoring loop.\n")
              STORE_NAME               0 (__doc__)

 19           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 21           LOAD_SMALL_INT           0
              LOAD_CONST               2 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              3 (typing)
              IMPORT_FROM              4 (Any)
              STORE_NAME               4 (Any)
              IMPORT_FROM              5 (Dict)
              STORE_NAME               5 (Dict)
              IMPORT_FROM              6 (List)
              STORE_NAME               6 (List)
              IMPORT_FROM              7 (Optional)
              STORE_NAME               7 (Optional)
              POP_TOP

 23           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Alert', 'Severity', 'Category'))
              IMPORT_NAME              8 (app.services.monitoring.contracts)
              IMPORT_FROM              9 (Alert)
              STORE_NAME               9 (Alert)
              IMPORT_FROM             10 (Severity)
              STORE_NAME              10 (Severity)
              IMPORT_FROM             11 (Category)
              STORE_NAME              11 (Category)
              POP_TOP

 24           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('redact_pii',))
              IMPORT_NAME             12 (app.utils.safe_log)
              IMPORT_FROM             13 (redact_pii)
              STORE_NAME              13 (redact_pii)
              POP_TOP

 31           LOAD_CONST               5 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\monitoring\dispatcher.py", line 31>)
              MAKE_FUNCTION
              LOAD_CONST               6 (<code object normalize_alert at 0x0000018C17F95CF0, file "app\services\monitoring\dispatcher.py", line 31>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (normalize_alert)

 57           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\monitoring\dispatcher.py", line 57>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _redact_string_values at 0x0000018C17EC57C0, file "app\services\monitoring\dispatcher.py", line 57>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_redact_string_values)

 73           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\dispatcher.py", line 73>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object alert_to_safe_dict at 0x0000018C17CC2460, file "app\services\monitoring\dispatcher.py", line 73>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (alert_to_safe_dict)

105           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\monitoring\dispatcher.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object emit_alert at 0x0000018C180C4470, file "app\services\monitoring\dispatcher.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (emit_alert)

119           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\monitoring\dispatcher.py", line 119>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object emit_alerts at 0x0000018C17FE1290, file "app\services\monitoring\dispatcher.py", line 119>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (emit_alerts)

138           LOAD_CONST              15 ('webhook_url')

141           LOAD_CONST              16 (None)

138           LOAD_CONST              17 ('brokerage')

142           LOAD_CONST              16 (None)

138           LOAD_CONST              18 ('include_metadata')

143           LOAD_CONST              19 (False)

138           BUILD_MAP                3
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\monitoring\dispatcher.py", line 138>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object emit_alerts_to_slack at 0x0000018C1796DBD0, file "app\services\monitoring\dispatcher.py", line 138>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              19 (emit_alerts_to_slack)
              LOAD_CONST              16 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\monitoring\dispatcher.py", line 31>:
 31           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert_or_dict')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Alert]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object normalize_alert at 0x0000018C17F95CF0, file "app\services\monitoring\dispatcher.py", line 31>:
  31           RESUME                   0

  43           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (alert_or_dict)
               LOAD_GLOBAL              2 (Alert)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN

  44           LOAD_FAST_BORROW         0 (alert_or_dict)
               RETURN_VALUE

  45   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (alert_or_dict)
               LOAD_GLOBAL              4 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L4)
               NOT_TAKEN

  46           NOP

  47   L2:     LOAD_GLOBAL              3 (Alert + NULL)
               LOAD_CONST               2 (())
               BUILD_MAP                0
               LOAD_FAST_BORROW         0 (alert_or_dict)
               DICT_MERGE               1
               CALL_FUNCTION_EX
       L3:     RETURN_VALUE

  50   L4:     LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  48           LOAD_GLOBAL              6 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

  49   L6:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

  48   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\monitoring\dispatcher.py", line 57>:
 57           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('d')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Any')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _redact_string_values at 0x0000018C17EC57C0, file "app\services\monitoring\dispatcher.py", line 57>:
  57            RESUME                   0

  64            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (d)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       47 (to L5)
                NOT_TAKEN

  65            LOAD_FAST_BORROW         0 (d)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (k)
                LOAD_FAST_AND_CLEAR      2 (v)
                SWAP                     3
        L1:     BUILD_MAP                0
                SWAP                     2
        L2:     FOR_ITER                17 (to L3)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              7 (_redact_string_values + NULL)
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                MAP_ADD                  2
                JUMP_BACKWARD           19 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     SWAP                     3
                STORE_FAST               2 (v)
                STORE_FAST               1 (k)
                RETURN_VALUE

  66    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (d)
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L10)
                NOT_TAKEN

  67            LOAD_FAST_BORROW         0 (d)
                GET_ITER
                LOAD_FAST_AND_CLEAR      2 (v)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                14 (to L8)
                STORE_FAST               2 (v)
                LOAD_GLOBAL              7 (_redact_string_values + NULL)
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L7)
        L8:     END_FOR
                POP_ITER
        L9:     SWAP                     2
                STORE_FAST               2 (v)
                RETURN_VALUE

  68   L10:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (d)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L11)
                NOT_TAKEN

  69            LOAD_GLOBAL             13 (redact_pii + NULL)
                LOAD_FAST_BORROW         0 (d)
                CALL                     1
                RETURN_VALUE

  70   L11:     LOAD_FAST_BORROW         0 (d)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

  65            SWAP                     3
                STORE_FAST               2 (v)
                STORE_FAST               1 (k)
                RERAISE                  0

  --   L13:     SWAP                     2
                POP_TOP

  67            SWAP                     2
                STORE_FAST               2 (v)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L12 [3]
  L6 to L9 -> L13 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\dispatcher.py", line 73>:
 73           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object alert_to_safe_dict at 0x0000018C17CC2460, file "app\services\monitoring\dispatcher.py", line 73>:
  73           RESUME                   0

  80           LOAD_GLOBAL              1 (normalize_alert + NULL)
               LOAD_FAST_BORROW         0 (alert)
               CALL                     1
               STORE_FAST               1 (a)

  81           LOAD_FAST_BORROW         1 (a)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

  82           BUILD_MAP                0
               RETURN_VALUE

  83   L1:     NOP

  84   L2:     LOAD_FAST_BORROW         1 (a)
               LOAD_ATTR                3 (to_dict + NULL|self)
               CALL                     0
               STORE_FAST               2 (d)

  88   L3:     LOAD_GLOBAL              7 (redact_pii + NULL)
               LOAD_FAST                2 (d)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               1 ('title')
               LOAD_CONST               2 ('')
               CALL                     2
               CALL                     1
               LOAD_FAST                2 (d)
               LOAD_CONST               1 ('title')
               STORE_SUBSCR

  89           LOAD_GLOBAL              7 (redact_pii + NULL)
               LOAD_FAST                2 (d)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               3 ('description')
               LOAD_CONST               2 ('')
               CALL                     2
               CALL                     1
               LOAD_FAST                2 (d)
               LOAD_CONST               3 ('description')
               STORE_SUBSCR

  90           LOAD_FAST                2 (d)
               LOAD_ATTR                9 (get + NULL|self)
               LOAD_CONST               4 ('metadata')
               CALL                     1
               STORE_FAST               3 (md)

  91           LOAD_GLOBAL             11 (isinstance + NULL)
               LOAD_FAST                3 (md)
               LOAD_GLOBAL             12 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L4)
               NOT_TAKEN

  92           LOAD_GLOBAL             15 (_redact_string_values + NULL)
               LOAD_FAST                3 (md)
               CALL                     1
               LOAD_FAST                2 (d)
               LOAD_CONST               4 ('metadata')
               STORE_SUBSCR

  98           LOAD_FAST                2 (d)
               RETURN_VALUE

  93   L4:     LOAD_FAST                3 (md)
               POP_JUMP_IF_NOT_NONE     8 (to L5)
               NOT_TAKEN

  94           BUILD_MAP                0
               LOAD_FAST                2 (d)
               LOAD_CONST               4 ('metadata')
               STORE_SUBSCR

  98           LOAD_FAST                2 (d)
               RETURN_VALUE

  97   L5:     LOAD_CONST               5 ('_invalid_metadata_type')
               LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST                3 (md)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               BUILD_MAP                1
               LOAD_FAST                2 (d)
               LOAD_CONST               4 ('metadata')
               STORE_SUBSCR

  98           LOAD_FAST                2 (d)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  85           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  86           BUILD_MAP                0
               SWAP                     2
       L7:     POP_EXCEPT
               RETURN_VALUE

  85   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\monitoring\dispatcher.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object emit_alert at 0x0000018C180C4470, file "app\services\monitoring\dispatcher.py", line 105>:
 105           RESUME                   0

 113           NOP

 114   L1:     LOAD_GLOBAL              1 (alert_to_safe_dict + NULL)
               LOAD_FAST_BORROW         0 (alert)
               CALL                     1
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 115           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L5)
               NOT_TAKEN
               POP_TOP

 116           BUILD_MAP                0
               SWAP                     2
       L4:     POP_EXCEPT
               RETURN_VALUE

 115   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\monitoring\dispatcher.py", line 119>:
119           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')
              LOAD_CONST               2 ('List[Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object emit_alerts at 0x0000018C17FE1290, file "app\services\monitoring\dispatcher.py", line 119>:
119           RESUME                   0

124           LOAD_FAST_BORROW         0 (alerts)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

125           BUILD_LIST               0
              RETURN_VALUE

126   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

127           LOAD_FAST_BORROW         0 (alerts)
              GET_ITER
      L2:     FOR_ITER                41 (to L4)
              STORE_FAST               2 (a)

128           LOAD_GLOBAL              1 (emit_alert + NULL)
              LOAD_FAST_BORROW         2 (a)
              CALL                     1
              STORE_FAST               3 (d)

129           LOAD_FAST_BORROW         3 (d)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           24 (to L2)

130   L3:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_FAST_BORROW         3 (d)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           43 (to L2)

127   L4:     END_FOR
              POP_ITER

131           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\monitoring\dispatcher.py", line 138>:
138           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')

139           LOAD_CONST               2 ('List[Any]')

138           LOAD_CONST               3 ('webhook_url')

141           LOAD_CONST               4 ('Optional[str]')

138           LOAD_CONST               5 ('brokerage')

142           LOAD_CONST               6 ('Any')

138           LOAD_CONST               7 ('include_metadata')

143           LOAD_CONST               8 ('bool')

138           LOAD_CONST               9 ('return')

144           LOAD_CONST              10 ('List[Dict[str, Any]]')

138           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object emit_alerts_to_slack at 0x0000018C1796DBD0, file "app\services\monitoring\dispatcher.py", line 138>:
 138           RESUME                   0

 164           NOP

 165   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('send_alerts_to_slack',))
               IMPORT_NAME              0 (app.services.monitoring.slack_alert_transport)
               IMPORT_FROM              1 (send_alerts_to_slack)
               STORE_FAST               4 (send_alerts_to_slack)
               POP_TOP

 174   L2:     LOAD_FAST                4 (send_alerts_to_slack)
               PUSH_NULL

 175           LOAD_FAST                0 (alerts)

 176           LOAD_FAST                1 (webhook_url)

 177           LOAD_FAST                2 (brokerage)

 178           LOAD_FAST                3 (include_metadata)

 174           LOAD_CONST               8 (('webhook_url', 'brokerage', 'include_metadata'))
               CALL_KW                  4
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 168           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       65 (to L8)
               NOT_TAKEN
               STORE_FAST               5 (e)

 170   L4:     LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('failed')

 171           LOAD_CONST               4 ('warnings')
               LOAD_CONST               5 ('transport_import_failed:')
               LOAD_GLOBAL              7 (type + NULL)
               LOAD_FAST                5 (e)
               CALL                     1
               LOAD_ATTR                8 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2
               BUILD_LIST               1

 172           LOAD_CONST               6 ('error_code')
               LOAD_CONST               5 ('transport_import_failed:')
               LOAD_GLOBAL              7 (type + NULL)
               LOAD_FAST                5 (e)
               CALL                     1
               LOAD_ATTR                8 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

 169           BUILD_MAP                3
               BUILD_LIST               1
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               7 (None)
               STORE_FAST               5 (e)
               DELETE_FAST              5 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               7 (None)
               STORE_FAST               5 (e)
               DELETE_FAST              5 (e)
               RERAISE                  1

 168   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti
```
