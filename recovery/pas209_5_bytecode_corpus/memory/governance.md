# memory/governance

- **pyc:** `app\services\memory\__pycache__\governance.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/governance.py`
- **co_filename (from bytecode):** `app\services\memory\governance.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144A — Memory governance.

Pure decision functions on `MemoryRecord` objects. Governance never
performs I/O, never calls a database, and never mutates its input —
`apply_memory_governance` returns a new record via
`dataclasses.replace`.

The persistence pipeline (built in PAS144B) is expected to:
  1. call `apply_memory_governance(record)` to derive the corrected
     record (auto-quarantine, default TTL, computed expires_at);
  2. call `validate_memory_record(corrected)` to collect blockers;
  3. call `should_persist_memory(corrected)` to make the final
     gate decision; and
  4. only then send the record to the storage layer.

Public surface:
  - validate_memory_record(record)        -> list[str]
  - should_persist_memory(record)         -> bool
  - should_quarantine_memory(record)      -> bool
  - memory_ttl_for_kind(kind)             -> int | None
  - apply_memory_governance(record)       -> MemoryRecord
```

## Imports

`CANDIDATE_CONFIDENCE_THRESHOLD`, `DEFAULT_TTL_DAYS`, `List`, `MemoryKind`, `MemoryRecord`, `MemorySource`, `MemoryStatus`, `OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD`, `Optional`, `__future__`, `annotations`, `contracts`, `dataclasses`, `datetime`, `has_forbidden_transcript_field`, `timedelta`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `apply_memory_governance`, `memory_ttl_for_kind`, `should_persist_memory`, `should_quarantine_memory`, `validate_memory_record`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144A — Memory governance.\n\nPure decision functions on `MemoryRecord` objects. Governance never\nperforms I/O, never calls a database, and never mutates its input —\n`apply_memory_governance` returns a new record via\n`dataclasses.replace`.\n\nThe persistence pipeline (built in PAS144B) is expected to:\n  1. call `apply_memory_governance(record)` to derive the corrected\n     record (auto-quarantine, default TTL, computed expires_at);\n  2. call `validate_memory_record(corrected)` to collect blockers;\n  3. call `should_persist_memory(corrected)` to make the final\n     gate decision; and\n  4. only then send the record to the storage layer.\n\nPublic surface:\n  - validate_memory_record(record)        -> list[str]\n  - should_persist_memory(record)         -> bool\n  - should_quarantine_memory(record)      -> bool\n  - memory_ttl_for_kind(kind)             -> int | None\n  - apply_memory_governance(record)       -> MemoryRecord\n'
- 'kind'
- 'MemoryKind'
- 'return'
- 'Optional[int]'
- 'Default TTL (in days) for *kind*. None means "no expiry by\ndefault" — currently only COMPLIANCE.'
- 'record'
- 'MemoryRecord'
- 'List[str]'
- 'Return a list of human-readable persistence blockers. An empty\nlist means the record is structurally fit for persistence (the\nfinal go/no-go is `should_persist_memory`, which layers status +\nthreshold rules on top of these structural checks).'
- 'not a MemoryRecord'
- 'missing brokerage_id'
- 'invalid kind'
- 'invalid source'
- 'invalid status'
- 'confidence out of range [0.0, 1.0]'
- 'outcome_weight out of range [0.0, 1.0]'
- 'missing lineage'
- 'evidence/metadata contains a forbidden raw-transcript field'
- 'compliance memory requires source SYSTEM or OPERATOR'
- 'strategic memory requires operator/source approval'
- 'bool'
- 'True iff *record* must be quarantined regardless of caller\nintent. Currently: every DANGEROUS-kind record.'
- 'Final go/no-go on whether the storage layer should accept this\nrecord. Returns False when:\n\n  - the record is not structurally valid (see validate_memory_record),\n  - the record is QUARANTINED / REJECTED / EXPIRED,\n  - the record is DANGEROUS (forced quarantine — never persists\n    through the normal candidate path),\n  - the record is OPERATIONAL but its outcome_weight is below the\n    threshold (anecdotal — would not improve the runtime),\n  - the record is CANDIDATE and its confidence is below threshold.\n'
- 'Return a corrected copy of *record* with policy applied:\n\n  - DANGEROUS records have status forced to QUARANTINED.\n  - COMPLIANCE records keep ttl_days = None (no default expiry).\n  - Other kinds inherit `memory_ttl_for_kind(kind)` when\n    ttl_days was not explicitly set.\n  - expires_at is computed from created_at + ttl_days when not\n    already set and ttl_days is now resolved.\n\nPure: never mutates *record*; never raises on a well-formed\nrecord. Re-validates invariants via the dataclass constructor.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144A — Memory governance.\n\nPure decision functions on `MemoryRecord` objects. Governance never\nperforms I/O, never calls a database, and never mutates its input —\n`apply_memory_governance` returns a new record via\n`dataclasses.replace`.\n\nThe persistence pipeline (built in PAS144B) is expected to:\n  1. call `apply_memory_governance(record)` to derive the corrected\n     record (auto-quarantine, default TTL, computed expires_at);\n  2. call `validate_memory_record(corrected)` to collect blockers;\n  3. call `should_persist_memory(corrected)` to make the final\n     gate decision; and\n  4. only then send the record to the storage layer.\n\nPublic surface:\n  - validate_memory_record(record)        -> list[str]\n  - should_persist_memory(record)         -> bool\n  - should_quarantine_memory(record)      -> bool\n  - memory_ttl_for_kind(kind)             -> int | None\n  - apply_memory_governance(record)       -> MemoryRecord\n')
              STORE_NAME               0 (__doc__)

 25           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 27           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (dataclasses)
              STORE_NAME               3 (dataclasses)

 28           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('timedelta',))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              5 (timedelta)
              STORE_NAME               5 (timedelta)
              POP_TOP

 29           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 31           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('CANDIDATE_CONFIDENCE_THRESHOLD', 'DEFAULT_TTL_DAYS', 'MemoryKind', 'MemoryRecord', 'MemorySource', 'MemoryStatus', 'OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD', 'has_forbidden_transcript_field'))
              IMPORT_NAME              9 (contracts)
              IMPORT_FROM             10 (CANDIDATE_CONFIDENCE_THRESHOLD)
              STORE_NAME              10 (CANDIDATE_CONFIDENCE_THRESHOLD)
              IMPORT_FROM             11 (DEFAULT_TTL_DAYS)
              STORE_NAME              11 (DEFAULT_TTL_DAYS)
              IMPORT_FROM             12 (MemoryKind)
              STORE_NAME              12 (MemoryKind)
              IMPORT_FROM             13 (MemoryRecord)
              STORE_NAME              13 (MemoryRecord)
              IMPORT_FROM             14 (MemorySource)
              STORE_NAME              14 (MemorySource)
              IMPORT_FROM             15 (MemoryStatus)
              STORE_NAME              15 (MemoryStatus)
              IMPORT_FROM             16 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)
              STORE_NAME              16 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)
              IMPORT_FROM             17 (has_forbidden_transcript_field)
              STORE_NAME              17 (has_forbidden_transcript_field)
              POP_TOP

 47           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\governance.py", line 47>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object memory_ttl_for_kind at 0x0000018C18024F30, file "app\services\memory\governance.py", line 47>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (memory_ttl_for_kind)

 57           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\governance.py", line 57>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object validate_memory_record at 0x0000018C17E94570, file "app\services\memory\governance.py", line 57>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (validate_memory_record)

110           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\governance.py", line 110>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object should_quarantine_memory at 0x0000018C18038DF0, file "app\services\memory\governance.py", line 110>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (should_quarantine_memory)

118           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\governance.py", line 118>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object should_persist_memory at 0x0000018C17EDAB80, file "app\services\memory\governance.py", line 118>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (should_persist_memory)

163           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\governance.py", line 163>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object apply_memory_governance at 0x0000018C17ED8620, file "app\services\memory\governance.py", line 163>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (apply_memory_governance)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\governance.py", line 47>:
 47           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kind')
              LOAD_CONST               2 ('MemoryKind')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object memory_ttl_for_kind at 0x0000018C18024F30, file "app\services\memory\governance.py", line 47>:
 47           RESUME                   0

 50           LOAD_GLOBAL              0 (DEFAULT_TTL_DAYS)
              LOAD_ATTR                2 (get)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (kind)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\governance.py", line 57>:
 57           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_memory_record at 0x0000018C17E94570, file "app\services\memory\governance.py", line 57>:
 57            RESUME                   0

 62            BUILD_LIST               0
               STORE_FAST               1 (errors)

 64            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_GLOBAL              2 (MemoryRecord)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

 65            LOAD_CONST               1 ('not a MemoryRecord')
               BUILD_LIST               1
               RETURN_VALUE

 67    L1:     LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR                4 (brokerage_id)
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR                4 (brokerage_id)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

 68    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               2 ('missing brokerage_id')
               CALL                     1
               POP_TOP

 70    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               10 (kind)
               LOAD_GLOBAL             12 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L4)
               NOT_TAKEN

 71            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               3 ('invalid kind')
               CALL                     1
               POP_TOP

 72    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               14 (source)
               LOAD_GLOBAL             16 (MemorySource)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L5)
               NOT_TAKEN

 73            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               4 ('invalid source')
               CALL                     1
               POP_TOP

 74    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               18 (status)
               LOAD_GLOBAL             20 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L6)
               NOT_TAKEN

 75            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               5 ('invalid status')
               CALL                     1
               POP_TOP

 77    L6:     LOAD_CONST               6 (0.0)
               LOAD_GLOBAL             23 (float + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               24 (confidence)
               CALL                     1
               SWAP                     2
               COPY                     2
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        8 (to L7)
               NOT_TAKEN
               LOAD_CONST               7 (1.0)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE        20 (to L9)
               NOT_TAKEN
               JUMP_FORWARD             1 (to L8)
       L7:     POP_TOP

 78    L8:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               8 ('confidence out of range [0.0, 1.0]')
               CALL                     1
               POP_TOP

 79    L9:     LOAD_CONST               6 (0.0)
               LOAD_GLOBAL             23 (float + NULL)
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               26 (outcome_weight)
               CALL                     1
               SWAP                     2
               COPY                     2
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        8 (to L10)
               NOT_TAKEN
               LOAD_CONST               7 (1.0)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE        20 (to L12)
               NOT_TAKEN
               JUMP_FORWARD             1 (to L11)
      L10:     POP_TOP

 80   L11:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST               9 ('outcome_weight out of range [0.0, 1.0]')
               CALL                     1
               POP_TOP

 82   L12:     LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               28 (lineage)
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L13)
               NOT_TAKEN

 83            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              10 ('missing lineage')
               CALL                     1
               POP_TOP

 85   L13:     LOAD_GLOBAL             31 (has_forbidden_transcript_field + NULL)
               LOAD_FAST_BORROW         0 (record)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L14)
               NOT_TAKEN

 86            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              11 ('evidence/metadata contains a forbidden raw-transcript field')
               CALL                     1
               POP_TOP

 88   L14:     LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               10 (kind)
               LOAD_GLOBAL             12 (MemoryKind)
               LOAD_ATTR               32 (COMPLIANCE)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       65 (to L15)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               14 (source)

 89            LOAD_GLOBAL             16 (MemorySource)
               LOAD_ATTR               34 (SYSTEM)
               LOAD_GLOBAL             16 (MemorySource)
               LOAD_ATTR               36 (OPERATOR)

 88            BUILD_TUPLE              2
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       18 (to L15)
               NOT_TAKEN

 91            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              12 ('compliance memory requires source SYSTEM or OPERATOR')
               CALL                     1
               POP_TOP

 93   L15:     LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               10 (kind)
               LOAD_GLOBAL             12 (MemoryKind)
               LOAD_ATTR               38 (STRATEGIC)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       80 (to L16)
               NOT_TAKEN

 98            LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               18 (status)
               LOAD_GLOBAL             20 (MemoryStatus)
               LOAD_ATTR               40 (APPROVED)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        49 (to L16)
               NOT_TAKEN

 99            LOAD_FAST_BORROW         0 (record)
               LOAD_ATTR               14 (source)
               LOAD_GLOBAL             16 (MemorySource)
               LOAD_ATTR               36 (OPERATOR)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        18 (to L16)
               NOT_TAKEN

101            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR                9 (append + NULL|self)
               LOAD_CONST              13 ('strategic memory requires operator/source approval')
               CALL                     1
               POP_TOP

103   L16:     LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\governance.py", line 110>:
110           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object should_quarantine_memory at 0x0000018C18038DF0, file "app\services\memory\governance.py", line 110>:
110           RESUME                   0

113           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

114           LOAD_CONST               1 (False)
              RETURN_VALUE

115   L1:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                4 (kind)
              LOAD_GLOBAL              6 (MemoryKind)
              LOAD_ATTR                8 (DANGEROUS)
              COMPARE_OP              72 (==)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\governance.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object should_persist_memory at 0x0000018C17EDAB80, file "app\services\memory\governance.py", line 118>:
118           RESUME                   0

130           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

131           LOAD_CONST               1 (False)
              RETURN_VALUE

133   L1:     LOAD_GLOBAL              5 (validate_memory_record + NULL)
              LOAD_FAST_BORROW         0 (record)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

134           LOAD_CONST               1 (False)
              RETURN_VALUE

136   L2:     LOAD_GLOBAL              7 (should_quarantine_memory + NULL)
              LOAD_FAST_BORROW         0 (record)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

137           LOAD_CONST               1 (False)
              RETURN_VALUE

139   L3:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                8 (status)

140           LOAD_GLOBAL             10 (MemoryStatus)
              LOAD_ATTR               12 (QUARANTINED)
              LOAD_GLOBAL             10 (MemoryStatus)
              LOAD_ATTR               14 (REJECTED)
              LOAD_GLOBAL             10 (MemoryStatus)
              LOAD_ATTR               16 (EXPIRED)

139           BUILD_TUPLE              3
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

142           LOAD_CONST               1 (False)
              RETURN_VALUE

145   L4:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               18 (kind)
              LOAD_GLOBAL             20 (MemoryKind)
              LOAD_ATTR               22 (OPERATIONAL)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       33 (to L5)
              NOT_TAKEN

146           LOAD_GLOBAL             25 (float + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               26 (outcome_weight)
              CALL                     1
              LOAD_GLOBAL             28 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

148           LOAD_CONST               1 (False)
              RETURN_VALUE

151   L5:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                8 (status)
              LOAD_GLOBAL             10 (MemoryStatus)
              LOAD_ATTR               30 (CANDIDATE)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       33 (to L6)
              NOT_TAKEN

152           LOAD_GLOBAL             25 (float + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               32 (confidence)
              CALL                     1
              LOAD_GLOBAL             34 (CANDIDATE_CONFIDENCE_THRESHOLD)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN

154           LOAD_CONST               1 (False)
              RETURN_VALUE

156   L6:     LOAD_CONST               2 (True)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\governance.py", line 163>:
163           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record')
              LOAD_CONST               2 ('MemoryRecord')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('MemoryRecord')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object apply_memory_governance at 0x0000018C17ED8620, file "app\services\memory\governance.py", line 163>:
163           RESUME                   0

176           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

177           LOAD_FAST_BORROW         0 (record)
              RETURN_VALUE

179   L1:     LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                4 (status)
              STORE_FAST               1 (new_status)

180           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                6 (ttl_days)
              STORE_FAST               2 (new_ttl_days)

181           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                8 (expires_at)
              STORE_FAST               3 (new_expires_at)

183           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               10 (kind)
              LOAD_GLOBAL             12 (MemoryKind)
              LOAD_ATTR               14 (DANGEROUS)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

184           LOAD_GLOBAL             16 (MemoryStatus)
              LOAD_ATTR               18 (QUARANTINED)
              STORE_FAST               1 (new_status)

186   L2:     LOAD_FAST_BORROW         2 (new_ttl_days)
              POP_JUMP_IF_NOT_NONE    59 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               10 (kind)
              LOAD_GLOBAL             12 (MemoryKind)
              LOAD_ATTR               20 (COMPLIANCE)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE       28 (to L3)
              NOT_TAKEN

187           LOAD_GLOBAL             23 (memory_ttl_for_kind + NULL)
              LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               10 (kind)
              CALL                     1
              STORE_FAST               4 (default_ttl)

188           LOAD_FAST_BORROW         4 (default_ttl)
              POP_JUMP_IF_NONE         3 (to L3)
              NOT_TAKEN

189           LOAD_FAST                4 (default_ttl)
              STORE_FAST               2 (new_ttl_days)

191   L3:     LOAD_FAST_BORROW         3 (new_expires_at)
              POP_JUMP_IF_NOT_NONE    34 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (new_ttl_days)
              POP_JUMP_IF_NONE        30 (to L4)
              NOT_TAKEN

192           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               24 (created_at)
              LOAD_GLOBAL             27 (timedelta + NULL)
              LOAD_FAST_BORROW         2 (new_ttl_days)
              LOAD_CONST               1 (('days',))
              CALL_KW                  1
              BINARY_OP                0 (+)
              STORE_FAST               3 (new_expires_at)

194   L4:     LOAD_GLOBAL             28 (dataclasses)
              LOAD_ATTR               30 (replace)
              PUSH_NULL

195           LOAD_FAST_BORROW         0 (record)

196           LOAD_FAST_BORROW         1 (new_status)

197           LOAD_FAST_BORROW         2 (new_ttl_days)

198           LOAD_FAST_BORROW         3 (new_expires_at)

194           LOAD_CONST               2 (('status', 'ttl_days', 'expires_at'))
              CALL_KW                  4
              RETURN_VALUE
```
