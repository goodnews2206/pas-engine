# memory/audit

- **pyc:** `app\services\memory\__pycache__\audit.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/audit.py`
- **co_filename (from bytecode):** `app\services\memory\audit.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144C — Memory review audit helpers (pure).

Pure helpers used by ``app/services/memory/review.py`` to build, sanitize,
and validate review events for the ``pas_memory_review_events`` table
created by ``scripts/migrate_v11_memory_review_audit.sql``.

Hard contract — everything in this module is pure:
  * no I/O, no database, no logging side effects;
  * inputs are validated structurally and returned as ``list[str]`` of
    blockers — invalid transitions DO NOT raise unless explicitly
    requested by the caller via the optional ``raise_on_invalid`` flag
    on ``validate_review_transition`` (kept for future use, default
    False — never raises today);
  * reason text is truncated to 500 chars and run through
    ``safe_log.redact_pii`` so obvious phone/email patterns are
    replaced before the audit row is built;
  * raw transcript text never enters a review event — the audit schema
    has no column for it, and ``build_review_event`` rejects any
    metadata key on the same denylist as the MemoryRecord contract.

Public surface (deliberately small):
  - ALLOWED_ACTOR_TYPES                                       (frozenset)
  - VALID_TRANSITIONS                                         (dict)
  - SECURITY_ONLY_TRANSITIONS                                 (dict)
  - REVIEW_REASON_MAX_LEN                                     (int)
  - sanitize_review_reason(reason)                            -> str
  - validate_review_transition(from_status, to_status, ...)   -> list[str]
  - build_review_event(...)                                   -> dict
  - review_event_to_row(event)                                -> dict

PAS144C explicitly does NOT build here:
  * retrieval / similarity search
  * embeddings / vector helpers
  * autonomous learning
  * any path that auto-approves CANDIDATE memory
```

## Imports

`Any`, `Dict`, `List`, `MemoryStatus`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.utils.safe_log`, `contracts`, `datetime`, `redact_pii`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_coerce_status_value`, `_has_forbidden_transcript_key`, `build_review_event`, `review_event_to_row`, `sanitize_review_reason`, `validate_review_transition`

## Env-key candidates

`ADMIN`, `SECURITY`, `SECURITY_ONLY_TRANSITIONS`, `VALID_TRANSITIONS`

## String constants (redacted where noted)

- '\nPAS144C — Memory review audit helpers (pure).\n\nPure helpers used by ``app/services/memory/review.py`` to build, sanitize,\nand validate review events for the ``pas_memory_review_events`` table\ncreated by ``scripts/migrate_v11_memory_review_audit.sql``.\n\nHard contract — everything in this module is pure:\n  * no I/O, no database, no logging side effects;\n  * inputs are validated structurally and returned as ``list[str]`` of\n    blockers — invalid transitions DO NOT raise unless explicitly\n    requested by the caller via the optional ``raise_on_invalid`` flag\n    on ``validate_review_transition`` (kept for future use, default\n    False — never raises today);\n  * reason text is truncated to 500 chars and run through\n    ``safe_log.redact_pii`` so obvious phone/email patterns are\n    replaced before the audit row is built;\n  * raw transcript text never enters a review event — the audit schema\n    has no column for it, and ``build_review_event`` rejects any\n    metadata key on the same denylist as the MemoryRecord contract.\n\nPublic surface (deliberately small):\n  - ALLOWED_ACTOR_TYPES                                       (frozenset)\n  - VALID_TRANSITIONS                                         (dict)\n  - SECURITY_ONLY_TRANSITIONS                                 (dict)\n  - REVIEW_REASON_MAX_LEN                                     (int)\n  - sanitize_review_reason(reason)                            -> str\n  - validate_review_transition(from_status, to_status, ...)   -> list[str]\n  - build_review_event(...)                                   -> dict\n  - review_event_to_row(event)                                -> dict\n\nPAS144C explicitly does NOT build here:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning\n  * any path that auto-approves CANDIDATE memory\n'
- 'ADMIN'
- 'SECURITY'
- 'Dict[str, frozenset]'
- 'VALID_TRANSITIONS'
- 'Dict[Tuple[str, str], frozenset]'
- 'SECURITY_ONLY_TRANSITIONS'
- 'actor_type'
- 'actor_id'
- 'reason'
- 'metadata'
- 'review_id'
- 'created_at'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Coerce a MemoryStatus or string to the closed-enum string value.\nReturns None for unknown / unparsable input.'
- 'Dict[str, Any]'
- 'bool'
- 'str'
- 'Return a log-safe, length-capped reason string.\n\nPipeline:\n  1. coerce to string (None and non-strings become "");\n  2. run through ``safe_log.redact_pii`` so obvious phone/email\n     patterns are replaced with ``[phone]`` / ``[email]``;\n  3. truncate to ``REVIEW_REASON_MAX_LEN``.\n\nPure. Never raises. Empty input yields ``""``.\n'
- 'from_status'
- 'to_status'
- 'List[str]'
- 'Return a list of human-readable blockers for the requested\ntransition. An empty list means the transition is legal.\n\nRules:\n  * ``to_status`` must be a known MemoryStatus.\n  * ``from_status`` may be None (used when the prior row is\n    missing) — in that case we treat the transition as illegal.\n  * The ``(from_status, to_status)`` pair must appear in\n    ``VALID_TRANSITIONS``.\n  * Privileged transitions (see ``SECURITY_ONLY_TRANSITIONS``)\n    additionally require an allowed ``actor_type``.\n\nPure. Never raises (the caller decides what to do with the\nreturned errors).\n'
- 'unknown to_status: '
- 'unknown from_status: '
- 'invalid transition: '
- ' -> '
- 'transition '
- ' requires actor_type in '
- '; got '
- 'memory_id'
- 'brokerage_id'
- 'Optional[Dict[str, Any]]'
- 'Optional[datetime]'
- 'Build a single review-event dict ready for serialisation.\n\nHard requirements (raise ``ValueError`` — these are caller bugs,\nnot policy decisions):\n  * memory_id non-empty string;\n  * brokerage_id non-empty string (tenant isolation);\n  * actor_type in ``ALLOWED_ACTOR_TYPES``;\n  * to_status is a known MemoryStatus value;\n  * metadata, if provided, is a dict and carries no raw-transcript\n    keys.\n\n``from_status`` may be None (e.g. for a SYSTEM transition that\ndiscovers the prior row missing). Transition LEGALITY is NOT\nvalidated here — call ``validate_review_transition`` first if you\nwant a strict gate. This separation keeps the builder usable for\n"record what actually happened" cases even when the transition is\nbeing recorded as a failure.\n\nPure: no I/O, no logging.\n'
- 'memory_id is required (non-empty string)'
- 'brokerage_id is required (tenant isolation)'
- 'actor_type must be one of '
- 'metadata must be a dict if provided'
- 'metadata contains a forbidden raw-transcript key; review events never carry raw conversation text'
- 'actor_id must be a string if provided'
- 'event'
- 'Serialise a built event dict into a row ready for\n``pas_memory_review_events`` INSERT.\n\nThe only non-trivial step is ``created_at`` ISO-8601 conversion;\neverything else is a pass-through. Kept separate from\n``build_review_event`` so callers (and tests) can hold an in-memory\nPython event without forcing a string conversion.\n'
- 'review_event_to_row requires a dict'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS144C — Memory review audit helpers (pure).\n\nPure helpers used by ``app/services/memory/review.py`` to build, sanitize,\nand validate review events for the ``pas_memory_review_events`` table\ncreated by ``scripts/migrate_v11_memory_review_audit.sql``.\n\nHard contract — everything in this module is pure:\n  * no I/O, no database, no logging side effects;\n  * inputs are validated structurally and returned as ``list[str]`` of\n    blockers — invalid transitions DO NOT raise unless explicitly\n    requested by the caller via the optional ``raise_on_invalid`` flag\n    on ``validate_review_transition`` (kept for future use, default\n    False — never raises today);\n  * reason text is truncated to 500 chars and run through\n    ``safe_log.redact_pii`` so obvious phone/email patterns are\n    replaced before the audit row is built;\n  * raw transcript text never enters a review event — the audit schema\n    has no column for it, and ``build_review_event`` rejects any\n    metadata key on the same denylist as the MemoryRecord contract.\n\nPublic surface (deliberately small):\n  - ALLOWED_ACTOR_TYPES                                       (frozenset)\n  - VALID_TRANSITIONS                                         (dict)\n  - SECURITY_ONLY_TRANSITIONS                                 (dict)\n  - REVIEW_REASON_MAX_LEN                                     (int)\n  - sanitize_review_reason(reason)                            -> str\n  - validate_review_transition(from_status, to_status, ...)   -> list[str]\n  - build_review_event(...)                                   -> dict\n  - review_event_to_row(event)                                -> dict\n\nPAS144C explicitly does NOT build here:\n  * retrieval / similarity search\n  * embeddings / vector helpers\n  * autonomous learning\n  * any path that auto-approves CANDIDATE memory\n')
               STORE_NAME               1 (__doc__)

  39           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (uuid)
               STORE_NAME               4 (uuid)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              5 (datetime)
               IMPORT_FROM              5 (datetime)
               STORE_NAME               5 (datetime)
               IMPORT_FROM              6 (timezone)
               STORE_NAME               6 (timezone)
               POP_TOP

  43           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              7 (typing)
               IMPORT_FROM              8 (Any)
               STORE_NAME               8 (Any)
               IMPORT_FROM              9 (Dict)
               STORE_NAME               9 (Dict)
               IMPORT_FROM             10 (List)
               STORE_NAME              10 (List)
               IMPORT_FROM             11 (Optional)
               STORE_NAME              11 (Optional)
               IMPORT_FROM             12 (Tuple)
               STORE_NAME              12 (Tuple)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('redact_pii',))
               IMPORT_NAME             13 (app.utils.safe_log)
               IMPORT_FROM             14 (redact_pii)
               STORE_NAME              14 (redact_pii)
               POP_TOP

  47           LOAD_SMALL_INT           1
               LOAD_CONST               6 (('MemoryStatus',))
               IMPORT_NAME             15 (contracts)
               IMPORT_FROM             16 (MemoryStatus)
               STORE_NAME              16 (MemoryStatus)
               POP_TOP

  58           LOAD_NAME               17 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              32 (frozenset({'ADMIN', 'SECURITY', 'OPERATOR', 'SYSTEM'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              18 (ALLOWED_ACTOR_TYPES)

  68           LOAD_CONST               9 (500)
               STORE_NAME              19 (REVIEW_REASON_MAX_LEN)

  96           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               40 (CANDIDATE)
               LOAD_ATTR               42 (value)
               LOAD_NAME               17 (frozenset)
               PUSH_NULL

  97           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               44 (APPROVED)
               LOAD_ATTR               42 (value)

  98           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               46 (REJECTED)
               LOAD_ATTR               42 (value)

  96           BUILD_SET                2
               CALL                     1

 100           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               44 (APPROVED)
               LOAD_ATTR               42 (value)
               LOAD_NAME               17 (frozenset)
               PUSH_NULL

 101           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               48 (EXPIRED)
               LOAD_ATTR               42 (value)

 100           BUILD_SET                1
               CALL                     1

 103           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               50 (QUARANTINED)
               LOAD_ATTR               42 (value)
               LOAD_NAME               17 (frozenset)
               PUSH_NULL

 104           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               46 (REJECTED)
               LOAD_ATTR               42 (value)

 105           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               44 (APPROVED)
               LOAD_ATTR               42 (value)

 103           BUILD_SET                2
               CALL                     1

  95           BUILD_MAP                3
               STORE_NAME              26 (VALID_TRANSITIONS)
               LOAD_CONST              10 ('Dict[str, frozenset]')
               LOAD_NAME               27 (__annotations__)
               LOAD_CONST              11 ('VALID_TRANSITIONS')
               STORE_SUBSCR

 113           LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               50 (QUARANTINED)
               LOAD_ATTR               42 (value)
               LOAD_NAME               16 (MemoryStatus)
               LOAD_ATTR               44 (APPROVED)
               LOAD_ATTR               42 (value)
               BUILD_TUPLE              2

 114           LOAD_NAME               17 (frozenset)
               PUSH_NULL
               LOAD_CONST               8 ('SECURITY')
               LOAD_CONST               7 ('ADMIN')
               BUILD_SET                2
               CALL                     1

 112           BUILD_MAP                1
               STORE_NAME              28 (SECURITY_ONLY_TRANSITIONS)
               LOAD_CONST              12 ('Dict[Tuple[str, str], frozenset]')
               LOAD_NAME               27 (__annotations__)
               LOAD_CONST              13 ('SECURITY_ONLY_TRANSITIONS')
               STORE_SUBSCR

 120           LOAD_NAME               17 (frozenset)
               PUSH_NULL
               BUILD_SET                0
               LOAD_CONST              33 (frozenset({'full_transcript', 'turns_text', 'utterances', 'transcripts', 'raw_transcript', 'transcript', 'messages', 'raw_text'}))
               SET_UPDATE               1
               CALL                     1
               STORE_NAME              29 (_FORBIDDEN_TRANSCRIPT_KEYS)

 131           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\audit.py", line 131>)
               MAKE_FUNCTION
               LOAD_CONST              15 (<code object _coerce_status_value at 0x0000018C179A7290, file "app\services\memory\audit.py", line 131>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_coerce_status_value)

 146           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\audit.py", line 146>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _has_forbidden_transcript_key at 0x0000018C17F95CF0, file "app\services\memory\audit.py", line 146>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_has_forbidden_transcript_key)

 157           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\audit.py", line 157>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object sanitize_review_reason at 0x0000018C180608A0, file "app\services\memory\audit.py", line 157>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (sanitize_review_reason)

 187           LOAD_CONST              20 ('actor_type')

 191           LOAD_CONST               2 (None)

 187           BUILD_MAP                1
               LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\audit.py", line 187>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object validate_review_transition at 0x0000018C17E956B0, file "app\services\memory\audit.py", line 187>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              33 (validate_review_transition)

 246           LOAD_CONST              23 ('actor_id')

 253           LOAD_CONST               2 (None)

 246           LOAD_CONST              24 ('reason')

 254           LOAD_CONST               2 (None)

 246           LOAD_CONST              25 ('metadata')

 255           LOAD_CONST               2 (None)

 246           LOAD_CONST              26 ('review_id')

 256           LOAD_CONST               2 (None)

 246           LOAD_CONST              27 ('created_at')

 257           LOAD_CONST               2 (None)

 246           BUILD_MAP                5
               LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18053090, file "app\services\memory\audit.py", line 246>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object build_review_event at 0x0000018C17D82BE0, file "app\services\memory\audit.py", line 246>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              34 (build_review_event)

 331           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\audit.py", line 331>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object review_event_to_row at 0x0000018C17D7E5C0, file "app\services\memory\audit.py", line 331>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (review_event_to_row)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\audit.py", line 131>:
131           RESUME                   0
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

Disassembly of <code object _coerce_status_value at 0x0000018C179A7290, file "app\services\memory\audit.py", line 131>:
 131           RESUME                   0

 134           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 135           LOAD_CONST               1 (None)
               RETURN_VALUE

 136   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (MemoryStatus)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

 137           LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

 138   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       59 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       37 (to L5)
               NOT_TAKEN

 139           NOP

 140   L3:     LOAD_GLOBAL              3 (MemoryStatus + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

 143   L5:     LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 141           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 142   L7:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

 141   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\audit.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('metadata')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _has_forbidden_transcript_key at 0x0000018C17F95CF0, file "app\services\memory\audit.py", line 146>:
146           RESUME                   0

147           LOAD_FAST_BORROW         0 (metadata)
              LOAD_ATTR                1 (keys + NULL|self)
              CALL                     0
              GET_ITER
      L1:     FOR_ITER                55 (to L4)
              STORE_FAST               1 (key)

148           LOAD_GLOBAL              3 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (key)
              LOAD_GLOBAL              4 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L1)
      L2:     LOAD_FAST_BORROW         1 (key)
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL              8 (_FORBIDDEN_TRANSCRIPT_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           54 (to L1)

149   L3:     POP_TOP
              LOAD_CONST               0 (True)
              RETURN_VALUE

147   L4:     END_FOR
              POP_ITER

150           LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\audit.py", line 157>:
157           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('reason')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object sanitize_review_reason at 0x0000018C180608A0, file "app\services\memory\audit.py", line 157>:
 157           RESUME                   0

 168           LOAD_FAST_BORROW         0 (reason)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 169           LOAD_CONST               2 ('')
               RETURN_VALUE

 170   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (reason)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        13 (to L3)
               NOT_TAKEN

 171           NOP

 172   L2:     LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         0 (reason)
               CALL                     1
               STORE_FAST               0 (reason)

 175   L3:     LOAD_FAST_BORROW         0 (reason)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN

 176           LOAD_CONST               2 ('')
               RETURN_VALUE

 177   L4:     LOAD_GLOBAL              7 (redact_pii + NULL)
               LOAD_FAST_BORROW         0 (reason)
               CALL                     1
               STORE_FAST               1 (redacted)

 178           LOAD_GLOBAL              9 (len + NULL)
               LOAD_FAST_BORROW         1 (redacted)
               CALL                     1
               LOAD_GLOBAL             10 (REVIEW_REASON_MAX_LEN)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       10 (to L5)
               NOT_TAKEN

 179           LOAD_FAST_BORROW         1 (redacted)
               LOAD_CONST               1 (None)
               LOAD_GLOBAL             10 (REVIEW_REASON_MAX_LEN)
               BINARY_SLICE
               RETURN_VALUE

 180   L5:     LOAD_FAST_BORROW         1 (redacted)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 173           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 174   L7:     POP_EXCEPT
               LOAD_CONST               2 ('')
               RETURN_VALUE

 173   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\memory\audit.py", line 187>:
187           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('from_status')

188           LOAD_CONST               2 ('Any')

187           LOAD_CONST               3 ('to_status')

189           LOAD_CONST               2 ('Any')

187           LOAD_CONST               4 ('actor_type')

191           LOAD_CONST               5 ('Optional[str]')

187           LOAD_CONST               6 ('return')

192           LOAD_CONST               7 ('List[str]')

187           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object validate_review_transition at 0x0000018C17E956B0, file "app\services\memory\audit.py", line 187>:
187           RESUME                   0

208           BUILD_LIST               0
              STORE_FAST               3 (errors)

210           LOAD_GLOBAL              1 (_coerce_status_value + NULL)
              LOAD_FAST_BORROW         1 (to_status)
              CALL                     1
              STORE_FAST               4 (to_value)

211           LOAD_FAST_BORROW         4 (to_value)
              POP_JUMP_IF_NOT_NONE    22 (to L1)
              NOT_TAKEN

212           LOAD_FAST_BORROW         3 (errors)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               1 ('unknown to_status: ')
              LOAD_FAST_BORROW         1 (to_status)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

214   L1:     LOAD_GLOBAL              1 (_coerce_status_value + NULL)
              LOAD_FAST_BORROW         0 (from_status)
              CALL                     1
              STORE_FAST               5 (from_value)

215           LOAD_FAST_BORROW         0 (from_status)
              POP_JUMP_IF_NONE         5 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         5 (from_value)
              POP_JUMP_IF_NOT_NONE    22 (to L3)
              NOT_TAKEN

218   L2:     LOAD_FAST_BORROW         3 (errors)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_CONST               2 ('unknown from_status: ')
              LOAD_FAST_BORROW         0 (from_status)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

221   L3:     LOAD_FAST_BORROW         4 (to_value)
              POP_JUMP_IF_NONE         5 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         5 (from_value)
              POP_JUMP_IF_NOT_NONE     3 (to L5)
              NOT_TAKEN

222   L4:     LOAD_FAST_BORROW         3 (errors)
              RETURN_VALUE

224   L5:     LOAD_GLOBAL              4 (VALID_TRANSITIONS)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_FAST_BORROW         5 (from_value)
              CALL                     1
              STORE_FAST               6 (allowed)

225           LOAD_FAST_BORROW         6 (allowed)
              TO_BOOL
              POP_JUMP_IF_FALSE        7 (to L6)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (to_value, allowed)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       26 (to L7)
              NOT_TAKEN

226   L6:     LOAD_FAST_BORROW         3 (errors)
              LOAD_ATTR                3 (append + NULL|self)

227           LOAD_CONST               3 ('invalid transition: ')
              LOAD_FAST_BORROW         5 (from_value)
              FORMAT_SIMPLE
              LOAD_CONST               4 (' -> ')
              LOAD_FAST_BORROW         4 (to_value)
              FORMAT_SIMPLE
              BUILD_STRING             4

226           CALL                     1
              POP_TOP

229           LOAD_FAST_BORROW         3 (errors)
              RETURN_VALUE

231   L7:     LOAD_GLOBAL              8 (SECURITY_ONLY_TRANSITIONS)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (from_value, to_value)
              BUILD_TUPLE              2
              CALL                     1
              STORE_FAST               7 (privileged)

232           LOAD_FAST_BORROW         7 (privileged)
              TO_BOOL
              POP_JUMP_IF_FALSE       50 (to L9)
              NOT_TAKEN

233           LOAD_FAST_BORROW         2 (actor_type)
              POP_JUMP_IF_NONE         7 (to L8)
              NOT_TAKEN
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (actor_type, privileged)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       40 (to L9)
              NOT_TAKEN

234   L8:     LOAD_FAST_BORROW         3 (errors)
              LOAD_ATTR                3 (append + NULL|self)

235           LOAD_CONST               5 ('transition ')
              LOAD_FAST_BORROW         5 (from_value)
              FORMAT_SIMPLE
              LOAD_CONST               4 (' -> ')
              LOAD_FAST_BORROW         4 (to_value)
              FORMAT_SIMPLE
              LOAD_CONST               6 (' requires actor_type in ')

236           LOAD_GLOBAL             11 (sorted + NULL)
              LOAD_FAST_BORROW         7 (privileged)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               7 ('; got ')
              LOAD_FAST_BORROW         2 (actor_type)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE

235           BUILD_STRING             8

234           CALL                     1
              POP_TOP

239   L9:     LOAD_FAST_BORROW         3 (errors)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053090, file "app\services\memory\audit.py", line 246>:
246           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('memory_id')

248           LOAD_CONST               2 ('str')

246           LOAD_CONST               3 ('brokerage_id')

249           LOAD_CONST               2 ('str')

246           LOAD_CONST               4 ('from_status')

250           LOAD_CONST               5 ('Any')

246           LOAD_CONST               6 ('to_status')

251           LOAD_CONST               5 ('Any')

246           LOAD_CONST               7 ('actor_type')

252           LOAD_CONST               2 ('str')

246           LOAD_CONST               8 ('actor_id')

253           LOAD_CONST               9 ('Optional[str]')

246           LOAD_CONST              10 ('reason')

254           LOAD_CONST               9 ('Optional[str]')

246           LOAD_CONST              11 ('metadata')

255           LOAD_CONST              12 ('Optional[Dict[str, Any]]')

246           LOAD_CONST              13 ('review_id')

256           LOAD_CONST               9 ('Optional[str]')

246           LOAD_CONST              14 ('created_at')

257           LOAD_CONST              15 ('Optional[datetime]')

246           LOAD_CONST              16 ('return')

258           LOAD_CONST              17 ('Dict[str, Any]')

246           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object build_review_event at 0x0000018C17D82BE0, file "app\services\memory\audit.py", line 246>:
246            RESUME                   0

279            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (memory_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (memory_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L2)
               NOT_TAKEN

280    L1:     LOAD_GLOBAL              7 (ValueError + NULL)
               LOAD_CONST               1 ('memory_id is required (non-empty string)')
               CALL                     1
               RAISE_VARARGS            1

281    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (brokerage_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         1 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L4)
               NOT_TAKEN

282    L3:     LOAD_GLOBAL              7 (ValueError + NULL)
               LOAD_CONST               2 ('brokerage_id is required (tenant isolation)')
               CALL                     1
               RAISE_VARARGS            1

283    L4:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (actor_type)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         4 (actor_type)
               LOAD_GLOBAL              8 (ALLOWED_ACTOR_TYPES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       32 (to L6)
               NOT_TAKEN

284    L5:     LOAD_GLOBAL              7 (ValueError + NULL)

285            LOAD_CONST               3 ('actor_type must be one of ')
               LOAD_GLOBAL             11 (sorted + NULL)
               LOAD_GLOBAL              8 (ALLOWED_ACTOR_TYPES)
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST               4 ('; got ')

286            LOAD_FAST_BORROW         4 (actor_type)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE

285            BUILD_STRING             4

284            CALL                     1
               RAISE_VARARGS            1

289    L6:     LOAD_GLOBAL             13 (_coerce_status_value + NULL)
               LOAD_FAST_BORROW         3 (to_status)
               CALL                     1
               STORE_FAST              10 (to_value)

290            LOAD_FAST_BORROW        10 (to_value)
               POP_JUMP_IF_NOT_NONE    16 (to L7)
               NOT_TAKEN

291            LOAD_GLOBAL              7 (ValueError + NULL)
               LOAD_CONST               6 ('unknown to_status: ')
               LOAD_FAST_BORROW         3 (to_status)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               RAISE_VARARGS            1

292    L7:     LOAD_GLOBAL             13 (_coerce_status_value + NULL)
               LOAD_FAST_BORROW         2 (from_status)
               CALL                     1
               STORE_FAST              11 (from_value)

294            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (metadata)
               LOAD_GLOBAL             14 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN
               LOAD_GLOBAL             15 (dict + NULL)
               LOAD_FAST_BORROW         7 (metadata)
               CALL                     1
               JUMP_FORWARD             1 (to L9)
       L8:     BUILD_MAP                0
       L9:     STORE_FAST              12 (meta)

295            LOAD_FAST_BORROW         7 (metadata)
               POP_JUMP_IF_NONE        34 (to L10)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (metadata)
               LOAD_GLOBAL             14 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L10)
               NOT_TAKEN

296            LOAD_GLOBAL              7 (ValueError + NULL)
               LOAD_CONST               7 ('metadata must be a dict if provided')
               CALL                     1
               RAISE_VARARGS            1

297   L10:     LOAD_GLOBAL             17 (_has_forbidden_transcript_key + NULL)
               LOAD_FAST_BORROW        12 (meta)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L11)
               NOT_TAKEN

298            LOAD_GLOBAL              7 (ValueError + NULL)

299            LOAD_CONST               8 ('metadata contains a forbidden raw-transcript key; review events never carry raw conversation text')

298            CALL                     1
               RAISE_VARARGS            1

303   L11:     LOAD_CONST               5 (None)
               STORE_FAST              13 (safe_actor_id)

304            LOAD_FAST_BORROW         5 (actor_id)
               POP_JUMP_IF_NONE        60 (to L14)
               NOT_TAKEN

305            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (actor_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L12)
               NOT_TAKEN

306            LOAD_GLOBAL              7 (ValueError + NULL)
               LOAD_CONST               9 ('actor_id must be a string if provided')
               CALL                     1
               RAISE_VARARGS            1

307   L12:     LOAD_FAST_BORROW         5 (actor_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 (None)
      L13:     STORE_FAST              13 (safe_actor_id)

309   L14:     LOAD_FAST_BORROW         6 (reason)
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L15)
               NOT_TAKEN
               LOAD_GLOBAL             19 (sanitize_review_reason + NULL)
               LOAD_FAST_BORROW         6 (reason)
               CALL                     1
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST              10 ('')
      L16:     STORE_FAST              14 (safe_reason)

311            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         8 (review_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L17)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (review_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_FAST                8 (review_id)
               JUMP_FORWARD            29 (to L18)

312   L17:     LOAD_GLOBAL              3 (str + NULL)
               LOAD_GLOBAL             20 (uuid)
               LOAD_ATTR               22 (uuid4)
               PUSH_NULL
               CALL                     0
               CALL                     1

311   L18:     STORE_FAST              15 (rid)

313            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         9 (created_at)
               LOAD_GLOBAL             24 (datetime)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_FAST                9 (created_at)
               JUMP_FORWARD            35 (to L20)
      L19:     LOAD_GLOBAL             24 (datetime)
               LOAD_ATTR               26 (now)
               PUSH_NULL
               LOAD_GLOBAL             28 (timezone)
               LOAD_ATTR               30 (utc)
               CALL                     1
      L20:     STORE_FAST              16 (ts)

314            LOAD_FAST_BORROW        16 (ts)
               LOAD_ATTR               32 (tzinfo)
               POP_JUMP_IF_NOT_NONE    33 (to L21)
               NOT_TAKEN

315            LOAD_FAST_BORROW        16 (ts)
               LOAD_ATTR               35 (replace + NULL|self)
               LOAD_GLOBAL             28 (timezone)
               LOAD_ATTR               30 (utc)
               LOAD_CONST              11 (('tzinfo',))
               CALL_KW                  1
               STORE_FAST              16 (ts)

318   L21:     LOAD_CONST              12 ('review_id')
               LOAD_FAST               15 (rid)

319            LOAD_CONST              13 ('memory_id')
               LOAD_FAST_BORROW         0 (memory_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0

320            LOAD_CONST              14 ('brokerage_id')
               LOAD_FAST_BORROW         1 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0

321            LOAD_CONST              15 ('from_status')
               LOAD_FAST               11 (from_value)

322            LOAD_CONST              16 ('to_status')
               LOAD_FAST               10 (to_value)

323            LOAD_CONST              17 ('actor_type')
               LOAD_FAST                4 (actor_type)

324            LOAD_CONST              18 ('actor_id')
               LOAD_FAST               13 (safe_actor_id)

325            LOAD_CONST              19 ('reason')
               LOAD_FAST               14 (safe_reason)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L22)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 (None)

326   L22:     LOAD_CONST              20 ('metadata')
               LOAD_FAST_BORROW        12 (meta)

327            LOAD_CONST              21 ('created_at')
               LOAD_FAST_BORROW        16 (ts)

317            BUILD_MAP               10
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\audit.py", line 331>:
331           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('event')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object review_event_to_row at 0x0000018C17D7E5C0, file "app\services\memory\audit.py", line 331>:
331           RESUME                   0

340           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (event)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

341           LOAD_GLOBAL              5 (TypeError + NULL)
              LOAD_CONST               1 ('review_event_to_row requires a dict')
              CALL                     1
              RAISE_VARARGS            1

343   L1:     LOAD_GLOBAL              3 (dict + NULL)
              LOAD_FAST_BORROW         0 (event)
              CALL                     1
              STORE_FAST               1 (row)

344           LOAD_FAST_BORROW         1 (row)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('created_at')
              CALL                     1
              STORE_FAST               2 (created_at)

345           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (created_at)
              LOAD_GLOBAL              8 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       67 (to L3)
              NOT_TAKEN

346           LOAD_FAST_BORROW         2 (created_at)
              LOAD_ATTR               10 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L2)
              NOT_TAKEN

347           LOAD_FAST_BORROW         2 (created_at)
              LOAD_ATTR               13 (replace + NULL|self)
              LOAD_GLOBAL             14 (timezone)
              LOAD_ATTR               16 (utc)
              LOAD_CONST               3 (('tzinfo',))
              CALL_KW                  1
              STORE_FAST               2 (created_at)

348   L2:     LOAD_FAST_BORROW         2 (created_at)
              LOAD_ATTR               19 (isoformat + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         1 (row)
              LOAD_CONST               2 ('created_at')
              STORE_SUBSCR
              JUMP_FORWARD            57 (to L4)

349   L3:     LOAD_FAST_BORROW         2 (created_at)
              POP_JUMP_IF_NOT_NONE    54 (to L4)
              NOT_TAKEN

350           LOAD_GLOBAL              8 (datetime)
              LOAD_ATTR               20 (now)
              PUSH_NULL
              LOAD_GLOBAL             14 (timezone)
              LOAD_ATTR               16 (utc)
              CALL                     1
              LOAD_ATTR               19 (isoformat + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         1 (row)
              LOAD_CONST               2 ('created_at')
              STORE_SUBSCR

353   L4:     LOAD_FAST_BORROW         1 (row)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               4 ('metadata')
              CALL                     1
              STORE_FAST               3 (md)

354           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (md)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L5)
              NOT_TAKEN
              LOAD_GLOBAL              3 (dict + NULL)
              LOAD_FAST_BORROW         3 (md)
              CALL                     1
              JUMP_FORWARD             1 (to L6)
      L5:     BUILD_MAP                0
      L6:     LOAD_FAST_BORROW         1 (row)
              LOAD_CONST               4 ('metadata')
              STORE_SUBSCR

355           LOAD_FAST_BORROW         1 (row)
              RETURN_VALUE
```
