# monitoring/contracts

- **pyc:** `app\services\monitoring\__pycache__\contracts.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/contracts.py`
- **co_filename (from bytecode):** `app\services\monitoring\contracts.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS143F1 — Monitoring alert contracts.

Pure data only. No engine, no dispatcher, no I/O. PAS143F2 will add a
runtime that consumes these structures.

Severity levels mirror the security audit (PAS143E):
  CRITICAL > HIGH > MEDIUM > LOW > INFO

Categories cover the surfaces the substrate cares about today:
  SECURITY            — credential leakage, suspicious access
  INTEGRITY           — checksum failures, malformed events
  BACKUP              — backup absent / failed / unverified
  INGESTION           — write-side failures (Supabase, providers)
  TENANT_ISOLATION    — cross-tenant access attempts
  RUNTIME             — engine errors, route failures
  REPLAY              — reconstruction inconsistency
  OPTIMIZATION        — matrix runner / metrics anomaly
```

## Imports

`Any`, `Dict`, `FrozenSet`, `Optional`, `__future__`, `annotations`, `asdict`, `dataclass`, `dataclasses`, `datetime`, `field`, `json`, `timezone`, `typing`

## Classes

`Alert`, `Category`, `Severity`

## Functions / methods

`__annotate__`, `severity_at_or_above`

## Env-key candidates

`BACKUP`, `CATEGORY_VALUES`, `CRITICAL`, `HIGH`, `INFO`, `INGESTION`, `INTEGRITY`, `LOW`, `MEDIUM`, `OPTIMIZATION`, `REPLAY`, `RUNTIME`, `SECURITY`, `SEVERITY_RANK`, `SEVERITY_VALUES`, `TENANT_ISOLATION`

## String constants (redacted where noted)

- '\nPAS143F1 — Monitoring alert contracts.\n\nPure data only. No engine, no dispatcher, no I/O. PAS143F2 will add a\nruntime that consumes these structures.\n\nSeverity levels mirror the security audit (PAS143E):\n  CRITICAL > HIGH > MEDIUM > LOW > INFO\n\nCategories cover the surfaces the substrate cares about today:\n  SECURITY            — credential leakage, suspicious access\n  INTEGRITY           — checksum failures, malformed events\n  BACKUP              — backup absent / failed / unverified\n  INGESTION           — write-side failures (Supabase, providers)\n  TENANT_ISOLATION    — cross-tenant access attempts\n  RUNTIME             — engine errors, route failures\n  REPLAY              — reconstruction inconsistency\n  OPTIMIZATION        — matrix runner / metrics anomaly\n'
- 'Severity'
- 'FrozenSet[str]'
- 'SEVERITY_VALUES'
- 'Dict[str, int]'
- 'SEVERITY_RANK'
- 'Category'
- 'CATEGORY_VALUES'
- 'Alert'
- 'CRITICAL'
- 'str'
- 'HIGH'
- 'MEDIUM'
- 'LOW'
- 'INFO'
- 'SECURITY'
- 'INTEGRITY'
- 'BACKUP'
- 'INGESTION'
- 'TENANT_ISOLATION'
- 'RUNTIME'
- 'REPLAY'
- 'OPTIMIZATION'
- '\nNormalized alert shape every PAS surface emits.\n\nRequired:\n  id           — stable identifier; idempotent across restarts.\n  category     — one of CATEGORY_VALUES.\n  severity     — one of SEVERITY_VALUES.\n  title        — one-line, human-readable, NO secrets.\n  description  — multi-line allowed; NO secrets.\n  source       — module / file emitting the alert (e.g.\n                 "app.services.intelligence.queries").\n\nOptional:\n  affected_brokerage — tenant id when the alert is tenant-scoped;\n                       None for global / system alerts.\n  metadata           — small dict of structured extras. Must be\n                       JSON-serialisable. NEVER contains raw\n                       transcripts, payloads, or credential values.\n  created_at         — ISO timestamp; defaults to now (UTC).\n'
- 'category'
- 'severity'
- 'title'
- 'description'
- 'source'
- 'Optional[str]'
- 'affected_brokerage'
- 'Dict[str, Any]'
- 'metadata'
- 'created_at'
- 'return'
- 'None'
- 'Alert.severity must be one of '
- 'Alert.category must be one of '
- 'Alert.id must be a non-empty string'
- 'Alert.title must be a non-empty string'
- 'Alert.metadata must be a dict'
- 'Serialise to a JSON-friendly dict.'
- 'Serialise to JSON string. Never raises — uses default=str\nfor any unexpected non-serializable nested type.'
- 'value'
- 'threshold'
- 'bool'
- '\nReturn True iff `value` is at or above `threshold` in severity.\nUnknown values compare as "below" everything (False).\n\nPure function. Never raises.\n'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS143F1 — Monitoring alert contracts.\n\nPure data only. No engine, no dispatcher, no I/O. PAS143F2 will add a\nruntime that consumes these structures.\n\nSeverity levels mirror the security audit (PAS143E):\n  CRITICAL > HIGH > MEDIUM > LOW > INFO\n\nCategories cover the surfaces the substrate cares about today:\n  SECURITY            — credential leakage, suspicious access\n  INTEGRITY           — checksum failures, malformed events\n  BACKUP              — backup absent / failed / unverified\n  INGESTION           — write-side failures (Supabase, providers)\n  TENANT_ISOLATION    — cross-tenant access attempts\n  RUNTIME             — engine errors, route failures\n  REPLAY              — reconstruction inconsistency\n  OPTIMIZATION        — matrix runner / metrics anomaly\n')
               STORE_NAME               1 (__doc__)

  21           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  23           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  24           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('asdict', 'dataclass', 'field'))
               IMPORT_NAME              5 (dataclasses)
               IMPORT_FROM              6 (asdict)
               STORE_NAME               6 (asdict)
               IMPORT_FROM              7 (dataclass)
               STORE_NAME               7 (dataclass)
               IMPORT_FROM              8 (field)
               STORE_NAME               8 (field)
               POP_TOP

  25           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('datetime', 'timezone'))
               IMPORT_NAME              9 (datetime)
               IMPORT_FROM              9 (datetime)
               STORE_NAME               9 (datetime)
               IMPORT_FROM             10 (timezone)
               STORE_NAME              10 (timezone)
               POP_TOP

  26           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Any', 'Dict', 'FrozenSet', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (Any)
               STORE_NAME              12 (Any)
               IMPORT_FROM             13 (Dict)
               STORE_NAME              13 (Dict)
               IMPORT_FROM             14 (FrozenSet)
               STORE_NAME              14 (FrozenSet)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  33           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               6 (<code object Severity at 0x0000018C17C49B80, file "app\services\monitoring\contracts.py", line 33>)
               MAKE_FUNCTION
               LOAD_CONST               7 ('Severity')
               CALL                     2
               STORE_NAME              16 (Severity)

  41           LOAD_NAME               17 (frozenset)
               PUSH_NULL

  42           LOAD_NAME               16 (Severity)
               LOAD_ATTR               36 (CRITICAL)
               LOAD_NAME               16 (Severity)
               LOAD_ATTR               38 (HIGH)
               LOAD_NAME               16 (Severity)
               LOAD_ATTR               40 (MEDIUM)
               LOAD_NAME               16 (Severity)
               LOAD_ATTR               42 (LOW)
               LOAD_NAME               16 (Severity)
               LOAD_ATTR               44 (INFO)
               BUILD_SET                5

  41           CALL                     1
               STORE_NAME              23 (SEVERITY_VALUES)
               LOAD_CONST               8 ('FrozenSet[str]')
               LOAD_NAME               24 (__annotations__)
               LOAD_CONST               9 ('SEVERITY_VALUES')
               STORE_SUBSCR

  47           LOAD_NAME               16 (Severity)
               LOAD_ATTR               36 (CRITICAL)
               LOAD_SMALL_INT           0

  48           LOAD_NAME               16 (Severity)
               LOAD_ATTR               38 (HIGH)
               LOAD_SMALL_INT           1

  49           LOAD_NAME               16 (Severity)
               LOAD_ATTR               40 (MEDIUM)
               LOAD_SMALL_INT           2

  50           LOAD_NAME               16 (Severity)
               LOAD_ATTR               42 (LOW)
               LOAD_SMALL_INT           3

  51           LOAD_NAME               16 (Severity)
               LOAD_ATTR               44 (INFO)
               LOAD_SMALL_INT           4

  46           BUILD_MAP                5
               STORE_NAME              25 (SEVERITY_RANK)
               LOAD_CONST              10 ('Dict[str, int]')
               LOAD_NAME               24 (__annotations__)
               LOAD_CONST              11 ('SEVERITY_RANK')
               STORE_SUBSCR

  59           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST              12 (<code object Category at 0x0000018C17972550, file "app\services\monitoring\contracts.py", line 59>)
               MAKE_FUNCTION
               LOAD_CONST              13 ('Category')
               CALL                     2
               STORE_NAME              26 (Category)

  70           LOAD_NAME               17 (frozenset)
               PUSH_NULL

  71           LOAD_NAME               26 (Category)
               LOAD_ATTR               54 (SECURITY)

  72           LOAD_NAME               26 (Category)
               LOAD_ATTR               56 (INTEGRITY)

  73           LOAD_NAME               26 (Category)
               LOAD_ATTR               58 (BACKUP)

  74           LOAD_NAME               26 (Category)
               LOAD_ATTR               60 (INGESTION)

  75           LOAD_NAME               26 (Category)
               LOAD_ATTR               62 (TENANT_ISOLATION)

  76           LOAD_NAME               26 (Category)
               LOAD_ATTR               64 (RUNTIME)

  77           LOAD_NAME               26 (Category)
               LOAD_ATTR               66 (REPLAY)

  78           LOAD_NAME               26 (Category)
               LOAD_ATTR               68 (OPTIMIZATION)

  70           BUILD_SET                8
               CALL                     1
               STORE_NAME              35 (CATEGORY_VALUES)
               LOAD_CONST               8 ('FrozenSet[str]')
               LOAD_NAME               24 (__annotations__)
               LOAD_CONST              14 ('CATEGORY_VALUES')
               STORE_SUBSCR

  86           LOAD_NAME                7 (dataclass)
               PUSH_NULL
               LOAD_CONST              15 (True)
               LOAD_CONST              16 (('frozen',))
               CALL_KW                  1

  87           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST              17 (<code object Alert at 0x0000018C1796DBD0, file "app\services\monitoring\contracts.py", line 86>)
               MAKE_FUNCTION
               LOAD_CONST              18 ('Alert')
               CALL                     2

  86           CALL                     0

  87           STORE_NAME              36 (Alert)

 149           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\monitoring\contracts.py", line 149>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object severity_at_or_above at 0x0000018C1802C620, file "app\services\monitoring\contracts.py", line 149>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (severity_at_or_above)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object Severity at 0x0000018C17C49B80, file "app\services\monitoring\contracts.py", line 33>:
 33           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('Severity')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          33
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 34           LOAD_CONST               1 ('CRITICAL')
              STORE_NAME               4 (CRITICAL)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               1 ('CRITICAL')
              STORE_SUBSCR

 35           LOAD_CONST               3 ('HIGH')
              STORE_NAME               6 (HIGH)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('HIGH')
              STORE_SUBSCR

 36           LOAD_CONST               4 ('MEDIUM')
              STORE_NAME               7 (MEDIUM)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('MEDIUM')
              STORE_SUBSCR

 37           LOAD_CONST               5 ('LOW')
              STORE_NAME               8 (LOW)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               5 ('LOW')
              STORE_SUBSCR

 38           LOAD_CONST               6 ('INFO')
              STORE_NAME               9 (INFO)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               6 ('INFO')
              STORE_SUBSCR
              LOAD_CONST               7 (())
              STORE_NAME              10 (__static_attributes__)
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object Category at 0x0000018C17972550, file "app\services\monitoring\contracts.py", line 59>:
 59           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('Category')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          59
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 60           LOAD_CONST               1 ('SECURITY')
              STORE_NAME               4 (SECURITY)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               1 ('SECURITY')
              STORE_SUBSCR

 61           LOAD_CONST               3 ('INTEGRITY')
              STORE_NAME               6 (INTEGRITY)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('INTEGRITY')
              STORE_SUBSCR

 62           LOAD_CONST               4 ('BACKUP')
              STORE_NAME               7 (BACKUP)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('BACKUP')
              STORE_SUBSCR

 63           LOAD_CONST               5 ('INGESTION')
              STORE_NAME               8 (INGESTION)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               5 ('INGESTION')
              STORE_SUBSCR

 64           LOAD_CONST               6 ('TENANT_ISOLATION')
              STORE_NAME               9 (TENANT_ISOLATION)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               6 ('TENANT_ISOLATION')
              STORE_SUBSCR

 65           LOAD_CONST               7 ('RUNTIME')
              STORE_NAME              10 (RUNTIME)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               7 ('RUNTIME')
              STORE_SUBSCR

 66           LOAD_CONST               8 ('REPLAY')
              STORE_NAME              11 (REPLAY)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               8 ('REPLAY')
              STORE_SUBSCR

 67           LOAD_CONST               9 ('OPTIMIZATION')
              STORE_NAME              12 (OPTIMIZATION)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               9 ('OPTIMIZATION')
              STORE_SUBSCR
              LOAD_CONST              10 (())
              STORE_NAME              13 (__static_attributes__)
              LOAD_CONST              11 (None)
              RETURN_VALUE

Disassembly of <code object Alert at 0x0000018C1796DBD0, file "app\services\monitoring\contracts.py", line 86>:
 86           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('Alert')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          86
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 88           LOAD_CONST               1 ('\nNormalized alert shape every PAS surface emits.\n\nRequired:\n  id           — stable identifier; idempotent across restarts.\n  category     — one of CATEGORY_VALUES.\n  severity     — one of SEVERITY_VALUES.\n  title        — one-line, human-readable, NO secrets.\n  description  — multi-line allowed; NO secrets.\n  source       — module / file emitting the alert (e.g.\n                 "app.services.intelligence.queries").\n\nOptional:\n  affected_brokerage — tenant id when the alert is tenant-scoped;\n                       None for global / system alerts.\n  metadata           — small dict of structured extras. Must be\n                       JSON-serialisable. NEVER contains raw\n                       transcripts, payloads, or credential values.\n  created_at         — ISO timestamp; defaults to now (UTC).\n')
              STORE_NAME               4 (__doc__)

108           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('id')
              STORE_SUBSCR

109           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('category')
              STORE_SUBSCR

110           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               5 ('severity')
              STORE_SUBSCR

111           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               6 ('title')
              STORE_SUBSCR

112           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               7 ('description')
              STORE_SUBSCR

113           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               8 ('source')
              STORE_SUBSCR

114           LOAD_CONST               9 (None)
              STORE_NAME               6 (affected_brokerage)
              LOAD_CONST              10 ('Optional[str]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              11 ('affected_brokerage')
              STORE_SUBSCR

115           LOAD_NAME                7 (field)
              PUSH_NULL
              LOAD_NAME                8 (dict)
              LOAD_CONST              12 (('default_factory',))
              CALL_KW                  1
              STORE_NAME               9 (metadata)
              LOAD_CONST              13 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              14 ('metadata')
              STORE_SUBSCR

116           LOAD_NAME                7 (field)
              PUSH_NULL

117           LOAD_CONST              15 (<code object <lambda> at 0x0000018C18038B70, file "app\services\monitoring\contracts.py", line 117>)
              MAKE_FUNCTION

116           LOAD_CONST              12 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              10 (created_at)
              LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              16 ('created_at')
              STORE_SUBSCR

123           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\monitoring\contracts.py", line 123>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object __post_init__ at 0x0000018C181A09B0, file "app\services\monitoring\contracts.py", line 123>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              11 (__post_init__)

135           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\monitoring\contracts.py", line 135>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object to_dict at 0x0000018C17FA2100, file "app\services\monitoring\contracts.py", line 135>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (to_dict)

139           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\contracts.py", line 139>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object to_json at 0x0000018C1802CAE0, file "app\services\monitoring\contracts.py", line 139>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              13 (to_json)
              LOAD_CONST              23 (())
              STORE_NAME              14 (__static_attributes__)
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18038B70, file "app\services\monitoring\contracts.py", line 117>:
117           RESUME                   0
              LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\monitoring\contracts.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('None')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object __post_init__ at 0x0000018C181A09B0, file "app\services\monitoring\contracts.py", line 123>:
123           RESUME                   0

124           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (severity)
              LOAD_GLOBAL              2 (SEVERITY_VALUES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       28 (to L1)
              NOT_TAKEN

125           LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               0 ('Alert.severity must be one of ')
              LOAD_GLOBAL              7 (sorted + NULL)
              LOAD_GLOBAL              2 (SEVERITY_VALUES)
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              RAISE_VARARGS            1

126   L1:     LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (category)
              LOAD_GLOBAL             10 (CATEGORY_VALUES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       28 (to L2)
              NOT_TAKEN

127           LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               1 ('Alert.category must be one of ')
              LOAD_GLOBAL              7 (sorted + NULL)
              LOAD_GLOBAL             10 (CATEGORY_VALUES)
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              RAISE_VARARGS            1

128   L2:     LOAD_GLOBAL             13 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (id)
              LOAD_GLOBAL             16 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (id)
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L4)
              NOT_TAKEN

129   L3:     LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               2 ('Alert.id must be a non-empty string')
              CALL                     1
              RAISE_VARARGS            1

130   L4:     LOAD_GLOBAL             13 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               18 (title)
              LOAD_GLOBAL             16 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       19 (to L5)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               18 (title)
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L6)
              NOT_TAKEN

131   L5:     LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               3 ('Alert.title must be a non-empty string')
              CALL                     1
              RAISE_VARARGS            1

132   L6:     LOAD_GLOBAL             13 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               20 (metadata)
              LOAD_GLOBAL             22 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L7)
              NOT_TAKEN

133           LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               4 ('Alert.metadata must be a dict')
              CALL                     1
              RAISE_VARARGS            1

132   L7:     LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\monitoring\contracts.py", line 135>:
135           RESUME                   0
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

Disassembly of <code object to_dict at 0x0000018C17FA2100, file "app\services\monitoring\contracts.py", line 135>:
135           RESUME                   0

137           LOAD_GLOBAL              1 (asdict + NULL)
              LOAD_FAST_BORROW         0 (self)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\contracts.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object to_json at 0x0000018C1802CAE0, file "app\services\monitoring\contracts.py", line 139>:
139           RESUME                   0

142           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                5 (to_dict + NULL|self)
              CALL                     0
              LOAD_GLOBAL              6 (str)
              LOAD_CONST               1 (True)
              LOAD_CONST               2 (('default', 'sort_keys'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\monitoring\contracts.py", line 149>:
149           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('threshold')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               5 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object severity_at_or_above at 0x0000018C1802C620, file "app\services\monitoring\contracts.py", line 149>:
 149           RESUME                   0

 156           NOP

 157   L1:     LOAD_GLOBAL              0 (SEVERITY_RANK)
               LOAD_FAST_BORROW         0 (value)
               BINARY_OP               26 ([])
               LOAD_GLOBAL              0 (SEVERITY_RANK)
               LOAD_FAST_BORROW         1 (threshold)
               BINARY_OP               26 ([])
               COMPARE_OP              42 (<=)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 158           LOAD_GLOBAL              2 (KeyError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 159   L4:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

 158   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti
```
