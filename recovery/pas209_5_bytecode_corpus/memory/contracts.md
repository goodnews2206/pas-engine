# memory/contracts

- **pyc:** `app\services\memory\__pycache__\contracts.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/contracts.py`
- **co_filename (from bytecode):** `app\services\memory\contracts.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144A — Operational Memory Contracts.

Pure dataclasses, enums, and constants. No I/O, no storage, no LLM,
no embeddings, no learning loop. Defines the shape of every memory
record before any storage layer (PAS144B) or retrieval layer
(later) is built.

Doctrine: PAS Brain learns from outcomes, not raw conversation
volume. A `MemoryRecord` therefore never carries raw transcript text;
it carries summaries, evidence, and lineage. The taxonomy
(`MemoryKind`) is the lever the runtime uses to decide what is even
eligible to persist.

Public surface:
  - MemoryKind, MemorySource, MemoryStatus  (enums)
  - MemoryRecord                            (dataclass)
  - DEFAULT_TTL_DAYS                        (kind → days | None)
  - CANDIDATE_CONFIDENCE_THRESHOLD          (float)
  - OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD    (float)
  - new_memory_id()                         (str factory)
  - has_forbidden_transcript_field()        (predicate)
```

## Imports

`Any`, `Dict`, `Enum`, `Optional`, `__future__`, `annotations`, `dataclass`, `dataclasses`, `datetime`, `enum`, `field`, `timezone`, `typing`, `uuid`

## Classes

`MemoryKind`, `MemoryRecord`, `MemorySource`, `MemoryStatus`

## Functions / methods

`__annotate__`, `has_forbidden_transcript_field`, `new_memory_id`

## Env-key candidates

`APPROVED`, `CALL`, `CANDIDATE`, `COMPLIANCE`, `DANGEROUS`, `DEFAULT_TTL_DAYS`, `EPHEMERAL`, `EXPIRED`, `OPERATIONAL`, `OPERATOR`, `OPTIMIZATION`, `QUARANTINED`, `REJECTED`, `REPLAY`, `SIMULATION`, `STRATEGIC`, `SYSTEM`

## String constants (redacted where noted)

- '\nPAS144A — Operational Memory Contracts.\n\nPure dataclasses, enums, and constants. No I/O, no storage, no LLM,\nno embeddings, no learning loop. Defines the shape of every memory\nrecord before any storage layer (PAS144B) or retrieval layer\n(later) is built.\n\nDoctrine: PAS Brain learns from outcomes, not raw conversation\nvolume. A `MemoryRecord` therefore never carries raw transcript text;\nit carries summaries, evidence, and lineage. The taxonomy\n(`MemoryKind`) is the lever the runtime uses to decide what is even\neligible to persist.\n\nPublic surface:\n  - MemoryKind, MemorySource, MemoryStatus  (enums)\n  - MemoryRecord                            (dataclass)\n  - DEFAULT_TTL_DAYS                        (kind → days | None)\n  - CANDIDATE_CONFIDENCE_THRESHOLD          (float)\n  - OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD    (float)\n  - new_memory_id()                         (str factory)\n  - has_forbidden_transcript_field()        (predicate)\n'
- 'MemoryKind'
- 'MemorySource'
- 'MemoryStatus'
- 'Dict[MemoryKind, Optional[int]]'
- 'DEFAULT_TTL_DAYS'
- 'MemoryRecord'
- 'What kind of operational lever this memory represents.'
- 'EPHEMERAL'
- 'OPERATIONAL'
- 'STRATEGIC'
- 'COMPLIANCE'
- 'OPTIMIZATION'
- 'DANGEROUS'
- 'Where the candidate memory was distilled from.'
- 'CALL'
- 'REPLAY'
- 'SIMULATION'
- 'OPERATOR'
- 'SYSTEM'
- 'Lifecycle position; a memory only influences the runtime when\nits status is APPROVED (and not yet expired).'
- 'CANDIDATE'
- 'APPROVED'
- 'QUARANTINED'
- 'EXPIRED'
- 'REJECTED'
- 'A single PAS Brain memory candidate or approved fact.\n\nHard invariants (enforced in __post_init__, never silently fixed):\n  - brokerage_id is non-empty (tenant isolation requirement)\n  - confidence ∈ [0.0, 1.0]\n  - outcome_weight ∈ [0.0, 1.0]\n  - kind/source/status are enum members\n  - ttl_days is None or non-negative\nSoft policy (handled in governance.py):\n  - DANGEROUS auto-quarantine\n  - COMPLIANCE TTL exemption\n  - lineage / outcome / source-approval requirements for persistence\n'
- 'str'
- 'memory_id'
- 'brokerage_id'
- 'kind'
- 'source'
- 'status'
- 'title'
- 'summary'
- 'Dict[str, Any]'
- 'evidence'
- 'float'
- 'confidence'
- 'outcome_weight'
- 'Optional[int]'
- 'ttl_days'
- 'datetime'
- 'created_at'
- 'Optional[datetime]'
- 'expires_at'
- 'lineage'
- 'metadata'
- 'return'
- 'None'
- 'brokerage_id is required and must be a non-empty string'
- 'kind must be MemoryKind, got '
- 'source must be MemorySource, got '
- 'status must be MemoryStatus, got '
- 'confidence must be numeric'
- 'confidence must be in [0.0, 1.0], got '
- 'outcome_weight must be numeric'
- 'outcome_weight must be in [0.0, 1.0], got '
- 'ttl_days must be a non-negative int or None'
- 'dict'
- 'Round-trippable dict. Enums collapse to their string values;\ndatetimes collapse to ISO-8601.'
- 'payload'
- "'MemoryRecord'"
- 'Rebuild a MemoryRecord from its serialized dict. Enforces\nthe same invariants as direct construction.'
- 'from_dict requires a dict payload'
- 'Opaque memory identifier; stable, URL-safe, no PII.'
- 'mem_'
- 'record'
- 'bool'
- 'True iff *record* carries any evidence/metadata key that is on\nthe raw-transcript denylist. PAS Brain never persists raw text;\ncallers should inspect this before sending to storage.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS144A — Operational Memory Contracts.\n\nPure dataclasses, enums, and constants. No I/O, no storage, no LLM,\nno embeddings, no learning loop. Defines the shape of every memory\nrecord before any storage layer (PAS144B) or retrieval layer\n(later) is built.\n\nDoctrine: PAS Brain learns from outcomes, not raw conversation\nvolume. A `MemoryRecord` therefore never carries raw transcript text;\nit carries summaries, evidence, and lineage. The taxonomy\n(`MemoryKind`) is the lever the runtime uses to decide what is even\neligible to persist.\n\nPublic surface:\n  - MemoryKind, MemorySource, MemoryStatus  (enums)\n  - MemoryRecord                            (dataclass)\n  - DEFAULT_TTL_DAYS                        (kind → days | None)\n  - CANDIDATE_CONFIDENCE_THRESHOLD          (float)\n  - OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD    (float)\n  - new_memory_id()                         (str factory)\n  - has_forbidden_transcript_field()        (predicate)\n')
               STORE_NAME               1 (__doc__)

  25           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  27           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (uuid)
               STORE_NAME               4 (uuid)

  28           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('dataclass', 'field'))
               IMPORT_NAME              5 (dataclasses)
               IMPORT_FROM              6 (dataclass)
               STORE_NAME               6 (dataclass)
               IMPORT_FROM              7 (field)
               STORE_NAME               7 (field)
               POP_TOP

  29           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('datetime', 'timezone'))
               IMPORT_NAME              8 (datetime)
               IMPORT_FROM              8 (datetime)
               STORE_NAME               8 (datetime)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  30           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Enum',))
               IMPORT_NAME             10 (enum)
               IMPORT_FROM             11 (Enum)
               STORE_NAME              11 (Enum)
               POP_TOP

  31           LOAD_SMALL_INT           0
               LOAD_CONST               6 (('Any', 'Dict', 'Optional'))
               IMPORT_NAME             12 (typing)
               IMPORT_FROM             13 (Any)
               STORE_NAME              13 (Any)
               IMPORT_FROM             14 (Dict)
               STORE_NAME              14 (Dict)
               IMPORT_FROM             15 (Optional)
               STORE_NAME              15 (Optional)
               POP_TOP

  38           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               7 (<code object MemoryKind at 0x0000018C17FBFEE0, file "app\services\memory\contracts.py", line 38>)
               MAKE_FUNCTION
               LOAD_CONST               8 ('MemoryKind')
               LOAD_NAME               16 (str)
               LOAD_NAME               11 (Enum)
               CALL                     4
               STORE_NAME              17 (MemoryKind)

  49           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST               9 (<code object MemorySource at 0x0000018C18090690, file "app\services\memory\contracts.py", line 49>)
               MAKE_FUNCTION
               LOAD_CONST              10 ('MemorySource')
               LOAD_NAME               16 (str)
               LOAD_NAME               11 (Enum)
               CALL                     4
               STORE_NAME              18 (MemorySource)

  60           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST              11 (<code object MemoryStatus at 0x0000018C18025230, file "app\services\memory\contracts.py", line 60>)
               MAKE_FUNCTION
               LOAD_CONST              12 ('MemoryStatus')
               LOAD_NAME               16 (str)
               LOAD_NAME               11 (Enum)
               CALL                     4
               STORE_NAME              19 (MemoryStatus)

  79           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               40 (EPHEMERAL)
               LOAD_SMALL_INT           7

  80           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               42 (OPERATIONAL)
               LOAD_SMALL_INT          90

  81           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               44 (STRATEGIC)
               LOAD_CONST              13 (365)

  82           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               46 (COMPLIANCE)
               LOAD_CONST               2 (None)

  83           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               48 (OPTIMIZATION)
               LOAD_SMALL_INT         180

  86           LOAD_NAME               17 (MemoryKind)
               LOAD_ATTR               50 (DANGEROUS)
               LOAD_SMALL_INT          30

  78           BUILD_MAP                6
               STORE_NAME              26 (DEFAULT_TTL_DAYS)
               LOAD_CONST              14 ('Dict[MemoryKind, Optional[int]]')
               LOAD_NAME               27 (__annotations__)
               LOAD_CONST              15 ('DEFAULT_TTL_DAYS')
               STORE_SUBSCR

  91           LOAD_CONST              16 (0.6)
               STORE_NAME              28 (CANDIDATE_CONFIDENCE_THRESHOLD)

  95           LOAD_CONST              17 (0.5)
               STORE_NAME              29 (OPERATIONAL_OUTCOME_WEIGHT_THRESHOLD)

 102           LOAD_NAME               30 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              24 (frozenset({'full_transcript', 'turns_text', 'utterances', 'transcripts', 'raw_transcript', 'transcript', 'messages', 'raw_text'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              31 (_FORBIDDEN_TRANSCRIPT_KEYS)

 113           LOAD_NAME                6 (dataclass)

 114           LOAD_BUILD_CLASS
               PUSH_NULL
               LOAD_CONST              18 (<code object MemoryRecord at 0x0000018C17EC5380, file "app\services\memory\contracts.py", line 113>)
               MAKE_FUNCTION
               LOAD_CONST              19 ('MemoryRecord')
               CALL                     2

 113           CALL                     0

 114           STORE_NAME              32 (MemoryRecord)

 250           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\contracts.py", line 250>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object new_memory_id at 0x0000018C1802C4F0, file "app\services\memory\contracts.py", line 250>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (new_memory_id)

 255           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\contracts.py", line 255>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object has_forbidden_transcript_field at 0x0000018C17D76C00, file "app\services\memory\contracts.py", line 255>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (has_forbidden_transcript_field)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object MemoryKind at 0x0000018C17FBFEE0, file "app\services\memory\contracts.py", line 38>:
 38           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('MemoryKind')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          38
              STORE_NAME               3 (__firstlineno__)

 39           LOAD_CONST               1 ('What kind of operational lever this memory represents.')
              STORE_NAME               4 (__doc__)

 41           LOAD_CONST               2 ('EPHEMERAL')
              STORE_NAME               5 (EPHEMERAL)

 42           LOAD_CONST               3 ('OPERATIONAL')
              STORE_NAME               6 (OPERATIONAL)

 43           LOAD_CONST               4 ('STRATEGIC')
              STORE_NAME               7 (STRATEGIC)

 44           LOAD_CONST               5 ('COMPLIANCE')
              STORE_NAME               8 (COMPLIANCE)

 45           LOAD_CONST               6 ('OPTIMIZATION')
              STORE_NAME               9 (OPTIMIZATION)

 46           LOAD_CONST               7 ('DANGEROUS')
              STORE_NAME              10 (DANGEROUS)
              LOAD_CONST               8 (())
              STORE_NAME              11 (__static_attributes__)
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object MemorySource at 0x0000018C18090690, file "app\services\memory\contracts.py", line 49>:
 49           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('MemorySource')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          49
              STORE_NAME               3 (__firstlineno__)

 50           LOAD_CONST               1 ('Where the candidate memory was distilled from.')
              STORE_NAME               4 (__doc__)

 52           LOAD_CONST               2 ('CALL')
              STORE_NAME               5 (CALL)

 53           LOAD_CONST               3 ('REPLAY')
              STORE_NAME               6 (REPLAY)

 54           LOAD_CONST               4 ('SIMULATION')
              STORE_NAME               7 (SIMULATION)

 55           LOAD_CONST               5 ('OPTIMIZATION')
              STORE_NAME               8 (OPTIMIZATION)

 56           LOAD_CONST               6 ('OPERATOR')
              STORE_NAME               9 (OPERATOR)

 57           LOAD_CONST               7 ('SYSTEM')
              STORE_NAME              10 (SYSTEM)
              LOAD_CONST               8 (())
              STORE_NAME              11 (__static_attributes__)
              LOAD_CONST               9 (None)
              RETURN_VALUE

Disassembly of <code object MemoryStatus at 0x0000018C18025230, file "app\services\memory\contracts.py", line 60>:
 60           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('MemoryStatus')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          60
              STORE_NAME               3 (__firstlineno__)

 61           LOAD_CONST               1 ('Lifecycle position; a memory only influences the runtime when\nits status is APPROVED (and not yet expired).')
              STORE_NAME               4 (__doc__)

 64           LOAD_CONST               2 ('CANDIDATE')
              STORE_NAME               5 (CANDIDATE)

 65           LOAD_CONST               3 ('APPROVED')
              STORE_NAME               6 (APPROVED)

 66           LOAD_CONST               4 ('QUARANTINED')
              STORE_NAME               7 (QUARANTINED)

 67           LOAD_CONST               5 ('EXPIRED')
              STORE_NAME               8 (EXPIRED)

 68           LOAD_CONST               6 ('REJECTED')
              STORE_NAME               9 (REJECTED)
              LOAD_CONST               7 (())
              STORE_NAME              10 (__static_attributes__)
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object MemoryRecord at 0x0000018C17EC5380, file "app\services\memory\contracts.py", line 113>:
113           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('MemoryRecord')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT         113
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

115           LOAD_CONST               1 ('A single PAS Brain memory candidate or approved fact.\n\nHard invariants (enforced in __post_init__, never silently fixed):\n  - brokerage_id is non-empty (tenant isolation requirement)\n  - confidence ∈ [0.0, 1.0]\n  - outcome_weight ∈ [0.0, 1.0]\n  - kind/source/status are enum members\n  - ttl_days is None or non-negative\nSoft policy (handled in governance.py):\n  - DANGEROUS auto-quarantine\n  - COMPLIANCE TTL exemption\n  - lineage / outcome / source-approval requirements for persistence\n')
              STORE_NAME               4 (__doc__)

129           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               3 ('memory_id')
              STORE_SUBSCR

130           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               4 ('brokerage_id')
              STORE_SUBSCR

131           LOAD_CONST               5 ('MemoryKind')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               6 ('kind')
              STORE_SUBSCR

132           LOAD_CONST               7 ('MemorySource')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST               8 ('source')
              STORE_SUBSCR

133           LOAD_CONST               9 ('MemoryStatus')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              10 ('status')
              STORE_SUBSCR

134           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              11 ('title')
              STORE_SUBSCR

135           LOAD_CONST               2 ('str')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              12 ('summary')
              STORE_SUBSCR

136           LOAD_NAME                6 (field)
              PUSH_NULL
              LOAD_NAME                7 (dict)
              LOAD_CONST              13 (('default_factory',))
              CALL_KW                  1
              STORE_NAME               8 (evidence)
              LOAD_CONST              14 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              15 ('evidence')
              STORE_SUBSCR

137           LOAD_CONST              16 (0.0)
              STORE_NAME               9 (confidence)
              LOAD_CONST              17 ('float')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              18 ('confidence')
              STORE_SUBSCR

138           LOAD_CONST              16 (0.0)
              STORE_NAME              10 (outcome_weight)
              LOAD_CONST              17 ('float')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              19 ('outcome_weight')
              STORE_SUBSCR

139           LOAD_CONST              20 (None)
              STORE_NAME              11 (ttl_days)
              LOAD_CONST              21 ('Optional[int]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              22 ('ttl_days')
              STORE_SUBSCR

140           LOAD_NAME                6 (field)
              PUSH_NULL

141           LOAD_CONST              23 (<code object <lambda> at 0x0000018C18053510, file "app\services\memory\contracts.py", line 141>)
              MAKE_FUNCTION

140           LOAD_CONST              13 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              12 (created_at)
              LOAD_CONST              24 ('datetime')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              25 ('created_at')
              STORE_SUBSCR

143           LOAD_CONST              20 (None)
              STORE_NAME              13 (expires_at)
              LOAD_CONST              26 ('Optional[datetime]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              27 ('expires_at')
              STORE_SUBSCR

144           LOAD_NAME                6 (field)
              PUSH_NULL
              LOAD_NAME                7 (dict)
              LOAD_CONST              13 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              14 (lineage)
              LOAD_CONST              14 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              28 ('lineage')
              STORE_SUBSCR

145           LOAD_NAME                6 (field)
              PUSH_NULL
              LOAD_NAME                7 (dict)
              LOAD_CONST              13 (('default_factory',))
              CALL_KW                  1
              STORE_NAME              15 (metadata)
              LOAD_CONST              14 ('Dict[str, Any]')
              LOAD_NAME                5 (__annotations__)
              LOAD_CONST              29 ('metadata')
              STORE_SUBSCR

147           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\contracts.py", line 147>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object __post_init__ at 0x0000018C17ED68D0, file "app\services\memory\contracts.py", line 147>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (__post_init__)

179           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\contracts.py", line 179>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object to_dict at 0x0000018C17D6DFC0, file "app\services\memory\contracts.py", line 179>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (to_dict)

200           LOAD_NAME               18 (classmethod)

201           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\contracts.py", line 201>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object from_dict at 0x0000018C17E91980, file "app\services\memory\contracts.py", line 200>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)

200           CALL                     0

201           STORE_NAME              19 (from_dict)
              LOAD_CONST              36 (('created_at', 'expires_at'))
              STORE_NAME              20 (__static_attributes__)
              LOAD_CONST              20 (None)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18053510, file "app\services\memory\contracts.py", line 141>:
141           RESUME                   0
              LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\contracts.py", line 147>:
147           RESUME                   0
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

Disassembly of <code object __post_init__ at 0x0000018C17ED68D0, file "app\services\memory\contracts.py", line 147>:
147            RESUME                   0

148            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (brokerage_id)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (brokerage_id)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L2)
               NOT_TAKEN

149    L1:     LOAD_GLOBAL              9 (ValueError + NULL)
               LOAD_CONST               0 ('brokerage_id is required and must be a non-empty string')
               CALL                     1
               RAISE_VARARGS            1

150    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               10 (kind)
               LOAD_GLOBAL             12 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        44 (to L3)
               NOT_TAKEN

151            LOAD_GLOBAL             15 (TypeError + NULL)
               LOAD_CONST               1 ('kind must be MemoryKind, got ')
               LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               10 (kind)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               RAISE_VARARGS            1

152    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               20 (source)
               LOAD_GLOBAL             22 (MemorySource)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        44 (to L4)
               NOT_TAKEN

153            LOAD_GLOBAL             15 (TypeError + NULL)
               LOAD_CONST               2 ('source must be MemorySource, got ')
               LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               20 (source)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               RAISE_VARARGS            1

154    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               24 (status)
               LOAD_GLOBAL             26 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        44 (to L5)
               NOT_TAKEN

155            LOAD_GLOBAL             15 (TypeError + NULL)
               LOAD_CONST               3 ('status must be MemoryStatus, got ')
               LOAD_GLOBAL             17 (type + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               24 (status)
               CALL                     1
               LOAD_ATTR               18 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               RAISE_VARARGS            1

156    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               28 (confidence)
               LOAD_GLOBAL             30 (int)
               LOAD_GLOBAL             32 (float)
               BUILD_TUPLE              2
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L6)
               NOT_TAKEN

157            LOAD_GLOBAL             15 (TypeError + NULL)
               LOAD_CONST               4 ('confidence must be numeric')
               CALL                     1
               RAISE_VARARGS            1

158    L6:     LOAD_CONST               5 (0.0)
               LOAD_GLOBAL             33 (float + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               28 (confidence)
               CALL                     1
               SWAP                     2
               COPY                     2
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        8 (to L7)
               NOT_TAKEN
               LOAD_CONST               6 (1.0)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE        27 (to L9)
               NOT_TAKEN
               JUMP_FORWARD             1 (to L8)
       L7:     POP_TOP

159    L8:     LOAD_GLOBAL              9 (ValueError + NULL)

160            LOAD_CONST               7 ('confidence must be in [0.0, 1.0], got ')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               28 (confidence)
               FORMAT_SIMPLE
               BUILD_STRING             2

159            CALL                     1
               RAISE_VARARGS            1

162    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               34 (outcome_weight)
               LOAD_GLOBAL             30 (int)
               LOAD_GLOBAL             32 (float)
               BUILD_TUPLE              2
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L10)
               NOT_TAKEN

163            LOAD_GLOBAL             15 (TypeError + NULL)
               LOAD_CONST               8 ('outcome_weight must be numeric')
               CALL                     1
               RAISE_VARARGS            1

164   L10:     LOAD_CONST               5 (0.0)
               LOAD_GLOBAL             33 (float + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               34 (outcome_weight)
               CALL                     1
               SWAP                     2
               COPY                     2
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        8 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 (1.0)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE        27 (to L13)
               NOT_TAKEN
               JUMP_FORWARD             1 (to L12)
      L11:     POP_TOP

165   L12:     LOAD_GLOBAL              9 (ValueError + NULL)

166            LOAD_CONST               9 ('outcome_weight must be in [0.0, 1.0], got ')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               34 (outcome_weight)
               FORMAT_SIMPLE
               BUILD_STRING             2

165            CALL                     1
               RAISE_VARARGS            1

168   L13:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               36 (ttl_days)
               POP_JUMP_IF_NONE        61 (to L15)
               NOT_TAKEN

169            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               36 (ttl_days)
               LOAD_GLOBAL             30 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L14)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               36 (ttl_days)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       12 (to L15)
               NOT_TAKEN

170   L14:     LOAD_GLOBAL              9 (ValueError + NULL)
               LOAD_CONST              11 ('ttl_days must be a non-negative int or None')
               CALL                     1
               RAISE_VARARGS            1

171   L15:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               38 (created_at)
               LOAD_ATTR               40 (tzinfo)
               POP_JUMP_IF_NOT_NONE    48 (to L16)
               NOT_TAKEN

173            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               38 (created_at)
               LOAD_ATTR               43 (replace + NULL|self)
               LOAD_GLOBAL             44 (timezone)
               LOAD_ATTR               46 (utc)
               LOAD_CONST              12 (('tzinfo',))
               CALL_KW                  1
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR              19 (created_at)

174   L16:     LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               48 (expires_at)
               POP_JUMP_IF_NONE        76 (to L18)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               48 (expires_at)
               LOAD_ATTR               40 (tzinfo)
               POP_JUMP_IF_NOT_NONE    50 (to L17)
               NOT_TAKEN

175            LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR               48 (expires_at)
               LOAD_ATTR               43 (replace + NULL|self)
               LOAD_GLOBAL             44 (timezone)
               LOAD_ATTR               46 (utc)
               LOAD_CONST              12 (('tzinfo',))
               CALL_KW                  1
               LOAD_FAST_BORROW         0 (self)
               STORE_ATTR              24 (expires_at)
               LOAD_CONST              10 (None)
               RETURN_VALUE

174   L17:     LOAD_CONST              10 (None)
               RETURN_VALUE
      L18:     LOAD_CONST              10 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\contracts.py", line 179>:
179           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('dict')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object to_dict at 0x0000018C17D6DFC0, file "app\services\memory\contracts.py", line 179>:
179           RESUME                   0

183           LOAD_CONST               1 ('memory_id')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (memory_id)

184           LOAD_CONST               2 ('brokerage_id')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (brokerage_id)

185           LOAD_CONST               3 ('kind')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                4 (kind)
              LOAD_ATTR                6 (value)

186           LOAD_CONST               4 ('source')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                8 (source)
              LOAD_ATTR                6 (value)

187           LOAD_CONST               5 ('status')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               10 (status)
              LOAD_ATTR                6 (value)

188           LOAD_CONST               6 ('title')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               12 (title)

189           LOAD_CONST               7 ('summary')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               14 (summary)

190           LOAD_CONST               8 ('evidence')
              LOAD_GLOBAL             17 (dict + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               18 (evidence)
              CALL                     1

191           LOAD_CONST               9 ('confidence')
              LOAD_GLOBAL             21 (float + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               22 (confidence)
              CALL                     1

192           LOAD_CONST              10 ('outcome_weight')
              LOAD_GLOBAL             21 (float + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               24 (outcome_weight)
              CALL                     1

193           LOAD_CONST              11 ('ttl_days')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               26 (ttl_days)

194           LOAD_CONST              12 ('created_at')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               28 (created_at)
              LOAD_ATTR               31 (isoformat + NULL|self)
              CALL                     0

195           LOAD_CONST              13 ('expires_at')
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               32 (expires_at)
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               32 (expires_at)
              LOAD_ATTR               31 (isoformat + NULL|self)
              CALL                     0
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST              14 (None)

196   L2:     LOAD_CONST              15 ('lineage')
              LOAD_GLOBAL             17 (dict + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               34 (lineage)
              CALL                     1

197           LOAD_CONST              16 ('metadata')
              LOAD_GLOBAL             17 (dict + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR               36 (metadata)
              CALL                     1

182           BUILD_MAP               15
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\contracts.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('payload')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ("'MemoryRecord'")
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object from_dict at 0x0000018C17E91980, file "app\services\memory\contracts.py", line 200>:
200            RESUME                   0

204            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L1)
               NOT_TAKEN

205            LOAD_GLOBAL              5 (TypeError + NULL)
               LOAD_CONST               1 ('from_dict requires a dict payload')
               CALL                     1
               RAISE_VARARGS            1

207    L1:     LOAD_FAST_BORROW         1 (payload)
               LOAD_CONST               2 ('kind')
               BINARY_OP               26 ([])
               STORE_FAST               2 (kind)

208            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (kind)
               LOAD_GLOBAL              6 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L2)
               NOT_TAKEN

209            LOAD_GLOBAL              7 (MemoryKind + NULL)
               LOAD_FAST_BORROW         2 (kind)
               CALL                     1
               STORE_FAST               2 (kind)

210    L2:     LOAD_FAST_BORROW         1 (payload)
               LOAD_CONST               3 ('source')
               BINARY_OP               26 ([])
               STORE_FAST               3 (source)

211            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (source)
               LOAD_GLOBAL              8 (MemorySource)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L3)
               NOT_TAKEN

212            LOAD_GLOBAL              9 (MemorySource + NULL)
               LOAD_FAST_BORROW         3 (source)
               CALL                     1
               STORE_FAST               3 (source)

213    L3:     LOAD_FAST_BORROW         1 (payload)
               LOAD_CONST               4 ('status')
               BINARY_OP               26 ([])
               STORE_FAST               4 (status)

214            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (status)
               LOAD_GLOBAL             10 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L4)
               NOT_TAKEN

215            LOAD_GLOBAL             11 (MemoryStatus + NULL)
               LOAD_FAST_BORROW         4 (status)
               CALL                     1
               STORE_FAST               4 (status)

217    L4:     LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               5 ('created_at')
               CALL                     1
               STORE_FAST               5 (created_at)

218            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (created_at)
               LOAD_GLOBAL             14 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L5)
               NOT_TAKEN

219            LOAD_GLOBAL             16 (datetime)
               LOAD_ATTR               18 (fromisoformat)
               PUSH_NULL
               LOAD_FAST_BORROW         5 (created_at)
               CALL                     1
               STORE_FAST               5 (created_at)
               JUMP_FORWARD            40 (to L6)

220    L5:     LOAD_FAST_BORROW         5 (created_at)
               POP_JUMP_IF_NOT_NONE    37 (to L6)
               NOT_TAKEN

221            LOAD_GLOBAL             16 (datetime)
               LOAD_ATTR               20 (now)
               PUSH_NULL
               LOAD_GLOBAL             22 (timezone)
               LOAD_ATTR               24 (utc)
               CALL                     1
               STORE_FAST               5 (created_at)

223    L6:     LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               6 ('expires_at')
               CALL                     1
               STORE_FAST               6 (expires_at)

224            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (expires_at)
               LOAD_GLOBAL             14 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L7)
               NOT_TAKEN

225            LOAD_GLOBAL             16 (datetime)
               LOAD_ATTR               18 (fromisoformat)
               PUSH_NULL
               LOAD_FAST_BORROW         6 (expires_at)
               CALL                     1
               STORE_FAST               6 (expires_at)

227    L7:     LOAD_FAST                0 (cls)
               PUSH_NULL

228            LOAD_FAST_BORROW         1 (payload)
               LOAD_CONST               7 ('memory_id')
               BINARY_OP               26 ([])

229            LOAD_FAST_BORROW         1 (payload)
               LOAD_CONST               8 ('brokerage_id')
               BINARY_OP               26 ([])

230            LOAD_FAST                2 (kind)

231            LOAD_FAST                3 (source)

232            LOAD_FAST                4 (status)

233            LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST               9 ('title')
               LOAD_CONST              10 ('')
               CALL                     2

234            LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              11 ('summary')
               LOAD_CONST              10 ('')
               CALL                     2

235            LOAD_GLOBAL              3 (dict + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              12 ('evidence')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L8:     CALL                     1

236            LOAD_GLOBAL             27 (float + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              13 ('confidence')
               LOAD_CONST              14 (0.0)
               CALL                     2
               CALL                     1

237            LOAD_GLOBAL             27 (float + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              15 ('outcome_weight')
               LOAD_CONST              14 (0.0)
               CALL                     2
               CALL                     1

238            LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              16 ('ttl_days')
               CALL                     1

239            LOAD_FAST                5 (created_at)

240            LOAD_FAST                6 (expires_at)

241            LOAD_GLOBAL              3 (dict + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              17 ('lineage')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L9:     CALL                     1

242            LOAD_GLOBAL              3 (dict + NULL)
               LOAD_FAST_BORROW         1 (payload)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              18 ('metadata')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L10)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
      L10:     CALL                     1

227            LOAD_CONST              19 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'evidence', 'confidence', 'outcome_weight', 'ttl_days', 'created_at', 'expires_at', 'lineage', 'metadata'))
               CALL_KW                 15
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\contracts.py", line 250>:
250           RESUME                   0
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

Disassembly of <code object new_memory_id at 0x0000018C1802C4F0, file "app\services\memory\contracts.py", line 250>:
250           RESUME                   0

252           LOAD_CONST               1 ('mem_')
              LOAD_GLOBAL              0 (uuid)
              LOAD_ATTR                2 (uuid4)
              PUSH_NULL
              CALL                     0
              LOAD_ATTR                4 (hex)
              LOAD_CONST               2 (slice(None, 24, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\contracts.py", line 255>:
255           RESUME                   0
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

Disassembly of <code object has_forbidden_transcript_field at 0x0000018C17D76C00, file "app\services\memory\contracts.py", line 255>:
255           RESUME                   0

259           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR                0 (evidence)
              LOAD_ATTR                3 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                55 (to L4)
              STORE_FAST               1 (key)

260           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (key)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L1)
      L2:     LOAD_FAST_BORROW         1 (key)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             10 (_FORBIDDEN_TRANSCRIPT_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           54 (to L1)

261   L3:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

259   L4:     END_FOR
              POP_ITER

262           LOAD_FAST_BORROW         0 (record)
              LOAD_ATTR               12 (metadata)
              LOAD_ATTR                3 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L5:     FOR_ITER                55 (to L8)
              STORE_FAST               1 (key)

263           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (key)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L5)
      L6:     LOAD_FAST_BORROW         1 (key)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             10 (_FORBIDDEN_TRANSCRIPT_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              JUMP_BACKWARD           54 (to L5)

264   L7:     POP_TOP
              LOAD_CONST               1 (True)
              RETURN_VALUE

262   L8:     END_FOR
              POP_ITER

265           LOAD_CONST               2 (False)
              RETURN_VALUE
```
