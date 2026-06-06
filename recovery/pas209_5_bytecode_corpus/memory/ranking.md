# memory/ranking

- **pyc:** `app\services\memory\__pycache__\ranking.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/ranking.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144E — Deterministic memory ranking.

Pure scoring helpers used by ``app/services/memory/retrieval.py``.
Given a list of ``pas_memory_records`` row dicts (or :class:`MemoryRecord`
instances), produces a deterministic ordering suitable for operator-
facing review surfaces and for the eventual PAS Brain runtime
injection that PAS144F will introduce — but does NOT itself perform
that injection.

Hard contract — everything in this module is pure:
  * no I/O, no logging side effects;
  * no LLM calls, no embedding generation, no semantic-similarity
    libraries, no external-vendor calls — and the module-surface
    tests assert that explicitly so this stays true under future
    edits;
  * never raises on malformed input. A row missing fields scores 0.0
    and is filtered or kept depending on the active-memory predicate.

Scoring intent (explicit so it is reviewable in one place):

    score = 0.45 * confidence
          + 0.30 * outcome_weight
          + 0.10 * recency_decay
          + 0.15 * compliance_bonus

  * ``confidence``       — governance signal that the memory survived
                           the candidate threshold.
  * ``outcome_weight``   — operational impact signal. OPERATIONAL
                           memory leans on this.
  * ``recency_decay``    — ``exp(-age_days / 180)``; modest weight so a
                           strong old record still beats a weak new one.
  * ``compliance_bonus`` — flat +0.15 for COMPLIANCE-kind records.
                           Regulatory facts should surface high when
                           they are eligible for retrieval at all.

The numerator weights deliberately sum to 1.00 so the maximum score is
exactly 1.0 (a COMPLIANCE-kind record with confidence=1, outcome_weight=1
and zero age). This makes the scale comparable across kinds and stable
across releases. Non-active rows score 0.0 unconditionally.

Public surface (deliberately small):
  - score_memory_record(record_or_row)             -> float
  - memory_is_approved(row)                         -> bool
  - memory_is_active(row, now=None)                 -> bool
  - rank_memory_records(records, *, kind=None,
                        max_items=10)               -> list[dict]

PAS144E explicitly does NOT build:
  * embeddings / vector helpers
  * semantic similarity
  * autonomous learning
  * runtime injection — that is PAS144F's job
  * any unscoped helper (ranking is pure; tenant scope lives in
    retrieval.py)
```

## Imports

`Any`, `Dict`, `Iterable`, `List`, `MemoryKind`, `MemoryRecord`, `MemoryStatus`, `Optional`, `Union`, `__future__`, `annotations`, `contracts`, `datetime`, `math`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_as_row`, `_coerce_kind_value`, `_now`, `_parse_datetime`, `_safe_float`, `memory_is_active`, `memory_is_approved`, `rank_memory_records`, `score_memory_record`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS144E — Deterministic memory ranking.\n\nPure scoring helpers used by ``app/services/memory/retrieval.py``.\nGiven a list of ``pas_memory_records`` row dicts (or :class:`MemoryRecord`\ninstances), produces a deterministic ordering suitable for operator-\nfacing review surfaces and for the eventual PAS Brain runtime\ninjection that PAS144F will introduce — but does NOT itself perform\nthat injection.\n\nHard contract — everything in this module is pure:\n  * no I/O, no logging side effects;\n  * no LLM calls, no embedding generation, no semantic-similarity\n    libraries, no external-vendor calls — and the module-surface\n    tests assert that explicitly so this stays true under future\n    edits;\n  * never raises on malformed input. A row missing fields scores 0.0\n    and is filtered or kept depending on the active-memory predicate.\n\nScoring intent (explicit so it is reviewable in one place):\n\n    score = 0.45 * confidence\n          + 0.30 * outcome_weight\n          + 0.10 * recency_decay\n          + 0.15 * compliance_bonus\n\n  * ``confidence``       — governance signal that the memory survived\n                           the candidate threshold.\n  * ``outcome_weight``   — operational impact signal. OPERATIONAL\n                           memory leans on this.\n  * ``recency_decay``    — ``exp(-age_days / 180)``; modest weight so a\n                           strong old record still beats a weak new one.\n  * ``compliance_bonus`` — flat +0.15 for COMPLIANCE-kind records.\n                           Regulatory facts should surface high when\n                           they are eligible for retrieval at all.\n\nThe numerator weights deliberately sum to 1.00 so the maximum score is\nexactly 1.0 (a COMPLIANCE-kind record with confidence=1, outcome_weight=1\nand zero age). This makes the scale comparable across kinds and stable\nacross releases. Non-active rows score 0.0 unconditionally.\n\nPublic surface (deliberately small):\n  - score_memory_record(record_or_row)             -> float\n  - memory_is_approved(row)                         -> bool\n  - memory_is_active(row, now=None)                 -> bool\n  - rank_memory_records(records, *, kind=None,\n                        max_items=10)               -> list[dict]\n\nPAS144E explicitly does NOT build:\n  * embeddings / vector helpers\n  * semantic similarity\n  * autonomous learning\n  * runtime injection — that is PAS144F's job\n  * any unscoped helper (ranking is pure; tenant scope lives in\n    retrieval.py)\n"
- 'default'
- 'now'
- 'kind'
- 'max_items'
- 'record_or_row'
- 'Any'
- 'return'
- 'Dict[str, Any]'
- 'Accept either a :class:`MemoryRecord` or a plain row dict.\n\nReturns a *copy* of the row so callers cannot mutate the source.\nA non-dict, non-MemoryRecord input becomes an empty dict — every\ndownstream check then degrades to "missing fields", which scores 0\nand fails the active-memory predicate.\n'
- 'Optional[str]'
- 'value'
- 'Optional[datetime]'
- 'Parse a stringified or datetime timestamp. None on failure.'
- '+00:00'
- 'float'
- 'Clamp a numeric field into [0, 1]. None/garbage → default.'
- 'datetime'
- 'row'
- 'bool'
- "True iff the row's status is APPROVED.\n\nPure, never raises. Non-dict / non-MemoryRecord input is False.\n"
- 'status'
- 'True iff the row is APPROVED AND has not yet expired.\n\n"Active" mirrors the runtime-eligibility predicate elsewhere in\nthe codebase: status==APPROVED, AND (expires_at is None OR\nexpires_at > now). Quarantined / Rejected / Expired rows return\nFalse. Pure, never raises.\n'
- 'expires_at'
- 'Compute a deterministic score in ``[0.0, 1.0]`` for one memory.\n\nNon-active records (not APPROVED, or expired) score exactly\n``0.0``. The score formula is documented in the module docstring;\ntreat it as the load-bearing contract — tests pin specific\nnumeric outputs.\n\nPure, never raises. Missing fields are treated as 0.\n'
- 'confidence'
- 'outcome_weight'
- 'created_at'
- 'records'
- 'Iterable[Any]'
- 'Union[None, str, MemoryKind]'
- 'int'
- 'List[Dict[str, Any]]'
- 'Filter to active memory and return up to ``max_items`` rows\nsorted by score desc, then by ``memory_id`` ascending for a\nstable, deterministic tiebreak.\n\nRules:\n  * ``records`` may be any iterable of dicts / MemoryRecord\n    instances. ``None`` and non-iterables return ``[]``.\n  * Non-active records (not APPROVED, or expired) are dropped.\n  * If ``kind`` is provided, only matching rows survive. Unknown\n    kind strings are *not* silently ignored here — they yield\n    ``[]`` because the caller has explicitly narrowed the request\n    and we should not widen it for them. (This is the inverse of\n    the queue/queries helpers, where the same scenario falls back\n    to "no kind filter". Ranking is the last step before the data\n    is consumed; we should be strict.)\n  * ``max_items`` is clamped to ``[0, MAX_RANK_ITEMS]``. A value of\n    0 returns ``[]``; a negative value coerces to 0.\n\nReturns plain dicts (copies of the input rows). The retrieval\nlayer applies the safety-field filter on top; this helper does\nNOT scrub forbidden transcript keys — that is retrieval\'s job, so\ncallers using ``rank_memory_records`` directly remain responsible\nfor not leaking raw fields.\n\nPure, never raises.\n'
- 'memory_id'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS144E — Deterministic memory ranking.\n\nPure scoring helpers used by ``app/services/memory/retrieval.py``.\nGiven a list of ``pas_memory_records`` row dicts (or :class:`MemoryRecord`\ninstances), produces a deterministic ordering suitable for operator-\nfacing review surfaces and for the eventual PAS Brain runtime\ninjection that PAS144F will introduce — but does NOT itself perform\nthat injection.\n\nHard contract — everything in this module is pure:\n  * no I/O, no logging side effects;\n  * no LLM calls, no embedding generation, no semantic-similarity\n    libraries, no external-vendor calls — and the module-surface\n    tests assert that explicitly so this stays true under future\n    edits;\n  * never raises on malformed input. A row missing fields scores 0.0\n    and is filtered or kept depending on the active-memory predicate.\n\nScoring intent (explicit so it is reviewable in one place):\n\n    score = 0.45 * confidence\n          + 0.30 * outcome_weight\n          + 0.10 * recency_decay\n          + 0.15 * compliance_bonus\n\n  * ``confidence``       — governance signal that the memory survived\n                           the candidate threshold.\n  * ``outcome_weight``   — operational impact signal. OPERATIONAL\n                           memory leans on this.\n  * ``recency_decay``    — ``exp(-age_days / 180)``; modest weight so a\n                           strong old record still beats a weak new one.\n  * ``compliance_bonus`` — flat +0.15 for COMPLIANCE-kind records.\n                           Regulatory facts should surface high when\n                           they are eligible for retrieval at all.\n\nThe numerator weights deliberately sum to 1.00 so the maximum score is\nexactly 1.0 (a COMPLIANCE-kind record with confidence=1, outcome_weight=1\nand zero age). This makes the scale comparable across kinds and stable\nacross releases. Non-active rows score 0.0 unconditionally.\n\nPublic surface (deliberately small):\n  - score_memory_record(record_or_row)             -> float\n  - memory_is_approved(row)                         -> bool\n  - memory_is_active(row, now=None)                 -> bool\n  - rank_memory_records(records, *, kind=None,\n                        max_items=10)               -> list[dict]\n\nPAS144E explicitly does NOT build:\n  * embeddings / vector helpers\n  * semantic similarity\n  * autonomous learning\n  * runtime injection — that is PAS144F's job\n  * any unscoped helper (ranking is pure; tenant scope lives in\n    retrieval.py)\n")
              STORE_NAME               0 (__doc__)

 58           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 60           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (math)
              STORE_NAME               3 (math)

 61           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 62           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Union'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (Iterable)
              STORE_NAME               9 (Iterable)
              IMPORT_FROM             10 (List)
              STORE_NAME              10 (List)
              IMPORT_FROM             11 (Optional)
              STORE_NAME              11 (Optional)
              IMPORT_FROM             12 (Union)
              STORE_NAME              12 (Union)
              POP_TOP

 64           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('MemoryKind', 'MemoryRecord', 'MemoryStatus'))
              IMPORT_NAME             13 (contracts)
              IMPORT_FROM             14 (MemoryKind)
              STORE_NAME              14 (MemoryKind)
              IMPORT_FROM             15 (MemoryRecord)
              STORE_NAME              15 (MemoryRecord)
              IMPORT_FROM             16 (MemoryStatus)
              STORE_NAME              16 (MemoryStatus)
              POP_TOP

 69           LOAD_CONST               6 (0.45)
              STORE_NAME              17 (_W_CONFIDENCE)

 70           LOAD_CONST               7 (0.3)
              STORE_NAME              18 (_W_OUTCOME)

 71           LOAD_CONST               8 (0.1)
              STORE_NAME              19 (_W_RECENCY)

 72           LOAD_CONST               9 (0.15)
              STORE_NAME              20 (_W_COMPLIANCE)

 75           LOAD_CONST              10 (180.0)
              STORE_NAME              21 (_RECENCY_TAU_DAYS)

 80           LOAD_SMALL_INT         200
              STORE_NAME              22 (MAX_RANK_ITEMS)

 87           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 87>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _as_row at 0x0000018C17FF10B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 87>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_as_row)

102           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 102>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _coerce_kind_value at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 102>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_coerce_kind_value)

115           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 115>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _parse_datetime at 0x0000018C17CC2460, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 115>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_parse_datetime)

132           LOAD_CONST              17 ('default')
              LOAD_CONST              18 (0.0)
              BUILD_MAP                1
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 132>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_float at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (_safe_float)

147           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 147>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _now at 0x0000018C180608A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 147>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_now)

159           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 159>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object memory_is_approved at 0x0000018C18039070, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 159>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (memory_is_approved)

168           LOAD_CONST              25 ('now')
              LOAD_CONST               2 (None)
              BUILD_MAP                1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 168>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object memory_is_active at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (memory_is_active)

189           LOAD_CONST              25 ('now')

192           LOAD_CONST               2 (None)

189           BUILD_MAP                1
              LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 189>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object score_memory_record at 0x0000018C17E91980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 189>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (score_memory_record)

248           LOAD_CONST              30 ('kind')

251           LOAD_CONST               2 (None)

248           LOAD_CONST              31 ('max_items')

252           LOAD_SMALL_INT          10

248           LOAD_CONST              25 ('now')

253           LOAD_CONST               2 (None)

248           BUILD_MAP                3
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 248>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object rank_memory_records at 0x0000018C17D7C560, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 248>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (rank_memory_records)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 87>:
 87           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record_or_row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _as_row at 0x0000018C17FF10B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 87>:
 87           RESUME                   0

 95           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record_or_row)
              LOAD_GLOBAL              2 (MemoryRecord)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       26 (to L1)
              NOT_TAKEN

 96           LOAD_GLOBAL              5 (dict + NULL)
              LOAD_FAST_BORROW         0 (record_or_row)
              LOAD_ATTR                7 (to_dict + NULL|self)
              CALL                     0
              CALL                     1
              RETURN_VALUE

 97   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (record_or_row)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L2)
              NOT_TAKEN

 98           LOAD_GLOBAL              5 (dict + NULL)
              LOAD_FAST_BORROW         0 (record_or_row)
              CALL                     1
              RETURN_VALUE

 99   L2:     BUILD_MAP                0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kind')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_kind_value at 0x0000018C1794E810, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 102>:
 102           RESUME                   0

 103           LOAD_FAST_BORROW         0 (kind)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 104           LOAD_CONST               0 (None)
               RETURN_VALUE

 105   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              2 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

 106           LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

 107   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       45 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L5)
               NOT_TAKEN

 108           NOP

 109   L3:     LOAD_GLOBAL              3 (MemoryKind + NULL)
               LOAD_FAST_BORROW         0 (kind)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

 112   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 110           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L8)
               NOT_TAKEN
               POP_TOP

 111   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 110   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 115>:
115           RESUME                   0
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
              LOAD_CONST               4 ('Optional[datetime]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_datetime at 0x0000018C17CC2460, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 115>:
 115            RESUME                   0

 117            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L2)
                NOT_TAKEN

 118            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

 119            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               2 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

 120    L1:     LOAD_FAST_BORROW         0 (value)
                RETURN_VALUE

 121    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL             12 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       96 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (value)
                TO_BOOL
                POP_JUMP_IF_FALSE       88 (to L6)
                NOT_TAKEN

 122            NOP

 123    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               14 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               3 ('Z')
                LOAD_CONST               4 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (ts)

 126    L4:     LOAD_FAST                1 (ts)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L5)
                NOT_TAKEN

 127            LOAD_FAST                1 (ts)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               2 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (ts)

 128    L5:     LOAD_FAST                1 (ts)
                RETURN_VALUE

 129    L6:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 124            LOAD_GLOBAL             16 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 125    L8:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 124    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 132>:
132           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('default')
              LOAD_CONST               4 ('float')
              LOAD_CONST               5 ('return')
              LOAD_CONST               4 ('float')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _safe_float at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 132>:
 132            RESUME                   0

 134            NOP

 135    L1:     LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST_BORROW         0 (value)
                CALL                     1
                STORE_FAST               2 (n)

 138    L2:     LOAD_GLOBAL              6 (math)
                LOAD_ATTR                8 (isnan)
                PUSH_NULL
                LOAD_FAST                2 (n)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        29 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              6 (math)
                LOAD_ATTR               10 (isinf)
                PUSH_NULL
                LOAD_FAST                2 (n)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 139    L3:     LOAD_FAST                1 (default)
                RETURN_VALUE

 140    L4:     LOAD_FAST                2 (n)
                LOAD_CONST               1 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 141            LOAD_CONST               1 (0.0)
                RETURN_VALUE

 142    L5:     LOAD_FAST                2 (n)
                LOAD_CONST               2 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 143            LOAD_CONST               2 (1.0)
                RETURN_VALUE

 144    L6:     LOAD_FAST                2 (n)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 136            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

 137            LOAD_FAST                1 (default)
                SWAP                     2
        L8:     POP_EXCEPT
                RETURN_VALUE

 136    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 147>:
147           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Optional[datetime]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now at 0x0000018C180608A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 147>:
147           RESUME                   0

148           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       49 (to L2)
              NOT_TAKEN

149           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

150           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

151   L1:     LOAD_FAST_BORROW         0 (now)
              RETURN_VALUE

152   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               12 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 159>:
159           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object memory_is_approved at 0x0000018C18039070, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 159>:
159           RESUME                   0

164           LOAD_GLOBAL              1 (_as_row + NULL)
              LOAD_FAST_BORROW         0 (row)
              CALL                     1
              STORE_FAST               1 (r)

165           LOAD_FAST_BORROW         1 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              LOAD_GLOBAL              4 (MemoryStatus)
              LOAD_ATTR                6 (APPROVED)
              LOAD_ATTR                8 (value)
              COMPARE_OP              72 (==)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 168>:
168           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('now')
              LOAD_CONST               4 ('Optional[datetime]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object memory_is_active at 0x0000018C180606F0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 168>:
168           RESUME                   0

176           LOAD_GLOBAL              1 (_as_row + NULL)
              LOAD_FAST_BORROW         0 (row)
              CALL                     1
              STORE_FAST               2 (r)

177           LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              LOAD_GLOBAL              4 (MemoryStatus)
              LOAD_ATTR                6 (APPROVED)
              LOAD_ATTR                8 (value)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

178           LOAD_CONST               2 (False)
              RETURN_VALUE

179   L1:     LOAD_GLOBAL             11 (_parse_datetime + NULL)
              LOAD_FAST_BORROW         2 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               3 ('expires_at')
              CALL                     1
              CALL                     1
              STORE_FAST               3 (exp)

180           LOAD_FAST_BORROW         3 (exp)
              POP_JUMP_IF_NOT_NONE     3 (to L2)
              NOT_TAKEN

181           LOAD_CONST               4 (True)
              RETURN_VALUE

182   L2:     LOAD_FAST_BORROW         3 (exp)
              LOAD_GLOBAL             13 (_now + NULL)
              LOAD_FAST_BORROW         1 (now)
              CALL                     1
              COMPARE_OP             132 (>)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('record_or_row')

190           LOAD_CONST               2 ('Any')

189           LOAD_CONST               3 ('now')

192           LOAD_CONST               4 ('Optional[datetime]')

189           LOAD_CONST               5 ('return')

193           LOAD_CONST               6 ('float')

189           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object score_memory_record at 0x0000018C17E91980, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 189>:
 189            RESUME                   0

 203            LOAD_GLOBAL              1 (_as_row + NULL)
                LOAD_FAST_BORROW         0 (record_or_row)
                CALL                     1
                STORE_FAST               2 (r)

 206            LOAD_GLOBAL              3 (memory_is_active + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (r, now)
                LOAD_CONST               1 (('now',))
                CALL_KW                  2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 207            LOAD_CONST               2 (0.0)
                RETURN_VALUE

 209    L1:     LOAD_GLOBAL              5 (_safe_float + NULL)
                LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               3 ('confidence')
                CALL                     1
                CALL                     1
                STORE_FAST               3 (confidence)

 210            LOAD_GLOBAL              5 (_safe_float + NULL)
                LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               4 ('outcome_weight')
                CALL                     1
                CALL                     1
                STORE_FAST               4 (outcome)

 212            LOAD_GLOBAL              9 (_parse_datetime + NULL)
                LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               5 ('created_at')
                CALL                     1
                CALL                     1
                STORE_FAST               5 (created_at)

 213            LOAD_FAST_BORROW         5 (created_at)
                POP_JUMP_IF_NOT_NONE     4 (to L2)
                NOT_TAKEN

 214            LOAD_CONST               2 (0.0)
                STORE_FAST               6 (recency_decay)
                JUMP_FORWARD           105 (to L6)

 216    L2:     LOAD_GLOBAL             11 (_now + NULL)
                LOAD_FAST_BORROW         1 (now)
                CALL                     1
                LOAD_FAST_BORROW         5 (created_at)
                BINARY_OP               10 (-)
                LOAD_ATTR               13 (total_seconds + NULL|self)
                CALL                     0
                STORE_FAST               7 (age_seconds)

 217            LOAD_GLOBAL             15 (max + NULL)
                LOAD_CONST               2 (0.0)
                LOAD_FAST_BORROW         7 (age_seconds)
                LOAD_CONST               6 (86400.0)
                BINARY_OP               11 (/)
                CALL                     2
                STORE_FAST               8 (age_days)

 218            NOP

 219    L3:     LOAD_GLOBAL             16 (math)
                LOAD_ATTR               18 (exp)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (age_days)
                UNARY_NEGATIVE
                LOAD_GLOBAL             20 (_RECENCY_TAU_DAYS)
                BINARY_OP               11 (/)
                CALL                     1
                STORE_FAST               6 (recency_decay)

 222    L4:     LOAD_FAST_BORROW         6 (recency_decay)
                LOAD_CONST               2 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        4 (to L5)
                NOT_TAKEN

 223            LOAD_CONST               2 (0.0)
                STORE_FAST               6 (recency_decay)
                JUMP_FORWARD             9 (to L6)

 224    L5:     LOAD_FAST_BORROW         6 (recency_decay)
                LOAD_CONST               7 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 225            LOAD_CONST               7 (1.0)
                STORE_FAST               6 (recency_decay)

 227    L6:     LOAD_FAST_BORROW         2 (r)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('kind')
                CALL                     1
                LOAD_GLOBAL             24 (MemoryKind)
                LOAD_ATTR               26 (COMPLIANCE)
                LOAD_ATTR               28 (value)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_CONST               7 (1.0)
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST               2 (0.0)
        L8:     STORE_FAST               9 (compliance_bonus)

 230            LOAD_GLOBAL             30 (_W_CONFIDENCE)
                LOAD_FAST_BORROW         3 (confidence)
                BINARY_OP                5 (*)

 231            LOAD_GLOBAL             32 (_W_OUTCOME)
                LOAD_FAST_BORROW         4 (outcome)
                BINARY_OP                5 (*)

 230            BINARY_OP                0 (+)

 232            LOAD_GLOBAL             34 (_W_RECENCY)
                LOAD_FAST_BORROW         6 (recency_decay)
                BINARY_OP                5 (*)

 230            BINARY_OP                0 (+)

 233            LOAD_GLOBAL             36 (_W_COMPLIANCE)
                LOAD_FAST_BORROW         9 (compliance_bonus)
                BINARY_OP                5 (*)

 230            BINARY_OP                0 (+)

 229            STORE_FAST              10 (score)

 237            LOAD_FAST_BORROW        10 (score)
                LOAD_CONST               2 (0.0)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 238            LOAD_CONST               2 (0.0)
                RETURN_VALUE

 239    L9:     LOAD_FAST_BORROW        10 (score)
                LOAD_CONST               7 (1.0)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN

 240            LOAD_CONST               7 (1.0)
                RETURN_VALUE

 241   L10:     LOAD_FAST_BORROW        10 (score)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 220            LOAD_GLOBAL             22 (OverflowError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L13)
                NOT_TAKEN
                POP_TOP

 221            LOAD_CONST               2 (0.0)
                STORE_FAST               6 (recency_decay)
       L12:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 171 (to L4)

 220   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 248>:
248           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('records')

249           LOAD_CONST               2 ('Iterable[Any]')

248           LOAD_CONST               3 ('kind')

251           LOAD_CONST               4 ('Union[None, str, MemoryKind]')

248           LOAD_CONST               5 ('max_items')

252           LOAD_CONST               6 ('int')

248           LOAD_CONST               7 ('now')

253           LOAD_CONST               8 ('Optional[datetime]')

248           LOAD_CONST               9 ('return')

254           LOAD_CONST              10 ('List[Dict[str, Any]]')

248           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object rank_memory_records at 0x0000018C17D7C560, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 248>:
 248            RESUME                   0

 281            LOAD_FAST_BORROW         0 (records)
                POP_JUMP_IF_NOT_NONE     3 (to L1)
                NOT_TAKEN

 282            BUILD_LIST               0
                RETURN_VALUE

 283    L1:     NOP

 284    L2:     LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST_BORROW         0 (records)
                CALL                     1
                STORE_FAST               4 (candidates)

 295    L3:     LOAD_GLOBAL              5 (_now + NULL)
                LOAD_FAST                3 (now)
                CALL                     1
                STORE_FAST               5 (fixed_now)

 298            NOP

 299    L4:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST                2 (max_items)
                CALL                     1
                STORE_FAST               6 (cap)

 302    L5:     LOAD_FAST                6 (cap)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 303            BUILD_LIST               0
                RETURN_VALUE

 304    L6:     LOAD_FAST                6 (cap)
                LOAD_GLOBAL             10 (MAX_RANK_ITEMS)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        7 (to L7)
                NOT_TAKEN

 305            LOAD_GLOBAL             10 (MAX_RANK_ITEMS)
                STORE_FAST               6 (cap)

 308    L7:     LOAD_FAST                1 (kind)
                POP_JUMP_IF_NONE        19 (to L9)
                NOT_TAKEN

 309            LOAD_GLOBAL             13 (_coerce_kind_value + NULL)
                LOAD_FAST                1 (kind)
                CALL                     1
                STORE_FAST               7 (kind_value)

 310            LOAD_FAST                7 (kind_value)
                POP_JUMP_IF_NOT_NONE     3 (to L8)
                NOT_TAKEN

 311            BUILD_LIST               0
                RETURN_VALUE

 310    L8:     JUMP_FORWARD             2 (to L10)

 313    L9:     LOAD_CONST               1 (None)
                STORE_FAST               7 (kind_value)

 315   L10:     BUILD_LIST               0
                STORE_FAST               8 (scored)

 316            LOAD_FAST                4 (candidates)
                GET_ITER
       L11:     FOR_ITER               140 (to L16)
                STORE_FAST               9 (raw)

 317            LOAD_GLOBAL             15 (_as_row + NULL)
                LOAD_FAST                9 (raw)
                CALL                     1
                STORE_FAST              10 (row)

 318            LOAD_FAST               10 (row)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

 319            JUMP_BACKWARD           24 (to L11)

 320   L12:     LOAD_GLOBAL             17 (memory_is_active + NULL)
                LOAD_FAST_LOAD_FAST    165 (row, fixed_now)
                LOAD_CONST               2 (('now',))
                CALL_KW                  2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

 321            JUMP_BACKWARD           44 (to L11)

 322   L13:     LOAD_FAST                7 (kind_value)
                POP_JUMP_IF_NONE        25 (to L14)
                NOT_TAKEN
                LOAD_FAST               10 (row)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               3 ('kind')
                CALL                     1
                LOAD_FAST                7 (kind_value)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 323            JUMP_BACKWARD           72 (to L11)

 324   L14:     LOAD_GLOBAL             21 (score_memory_record + NULL)
                LOAD_FAST_LOAD_FAST    165 (row, fixed_now)
                LOAD_CONST               2 (('now',))
                CALL_KW                  2
                STORE_FAST              11 (s)

 327            LOAD_FAST               10 (row)
                LOAD_ATTR               19 (get + NULL|self)
                LOAD_CONST               4 ('memory_id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
       L15:     STORE_FAST              12 (mid)

 328            LOAD_FAST                8 (scored)
                LOAD_ATTR               23 (append + NULL|self)
                LOAD_FAST               11 (s)
                LOAD_GLOBAL             25 (str + NULL)
                LOAD_FAST               12 (mid)
                CALL                     1
                LOAD_FAST               10 (row)
                BUILD_TUPLE              3
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          142 (to L11)

 316   L16:     END_FOR
                POP_ITER

 332            LOAD_FAST                8 (scored)
                LOAD_ATTR               27 (sort + NULL|self)
                LOAD_CONST               6 (<code object <lambda> at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 332>)
                MAKE_FUNCTION
                LOAD_CONST               7 (('key',))
                CALL_KW                  1
                POP_TOP

 333            LOAD_FAST                8 (scored)
                LOAD_CONST               1 (None)
                LOAD_FAST                6 (cap)
                BINARY_SLICE
                GET_ITER
                LOAD_FAST_AND_CLEAR     13 (_)
                LOAD_FAST_AND_CLEAR     10 (row)
                SWAP                     3
       L17:     BUILD_LIST               0
                SWAP                     2
       L18:     FOR_ITER                 8 (to L19)
                UNPACK_SEQUENCE          3
                POP_TOP
                STORE_FAST_STORE_FAST  218 (_, row)
                LOAD_FAST               10 (row)
                LIST_APPEND              2
                JUMP_BACKWARD           10 (to L18)
       L19:     END_FOR
                POP_ITER
       L20:     SWAP                     3
                STORE_FAST              10 (row)
                STORE_FAST              13 (_)
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 285            LOAD_GLOBAL              2 (TypeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L23)
                NOT_TAKEN
                POP_TOP

 286            BUILD_LIST               0
                SWAP                     2
       L22:     POP_EXCEPT
                RETURN_VALUE

 285   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 300            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              8 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L27)
                NOT_TAKEN
                POP_TOP

 301            LOAD_SMALL_INT          10
                STORE_FAST               6 (cap)
       L26:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 284 (to L5)

 300   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     SWAP                     2
                POP_TOP

 333            SWAP                     3
                STORE_FAST              10 (row)
                STORE_FAST              13 (_)
                RERAISE                  0
ExceptionTable:
  L2 to L3 -> L21 [0]
  L4 to L5 -> L25 [0]
  L17 to L20 -> L29 [3]
  L21 to L22 -> L24 [1] lasti
  L23 to L24 -> L24 [1] lasti
  L25 to L26 -> L28 [1] lasti
  L27 to L28 -> L28 [1] lasti

Disassembly of <code object <lambda> at 0x0000018C18024B30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\ranking.py", line 332>:
332           RESUME                   0
              LOAD_FAST_BORROW         0 (t)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              UNARY_NEGATIVE
              LOAD_FAST_BORROW         0 (t)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE
```
