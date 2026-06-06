# memory/retrieval

- **pyc:** `app\services\memory\__pycache__\retrieval.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/retrieval.py`
- **co_filename (from bytecode):** `app\services\memory\retrieval.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144E — Controlled active-memory retrieval.

Tenant-scoped read layer that sits on top of PAS144B's tenant-scoped
query helpers and PAS144E's deterministic ranking. Every helper here
is a *read* helper — no writes, no transitions, no LLM calls, no
embeddings, no autonomous learning.

Hard contract — every public helper in this module:

  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is
     no unscoped retrieval helper. The closest thing in the codebase
     remains ``queries.list_memory_admin_unscoped`` (operator-only,
     not consumed by retrieval).
  2. Reads only through one of the audited PAS144B/D surfaces:
     ``queries.list_active_memory_for_brokerage`` (status / expiry
     filtered) — never raw table access here.
  3. Ranks results through ``ranking.rank_memory_records`` so the
     ordering is deterministic and operator-reviewable.
  4. Caps the caller-supplied ``limit`` at ``queries.MAX_QUERY_LIMIT``.
  5. Returns *safe* dicts only: a whitelisted subset of the row
     columns plus a scrubbed copy of ``evidence`` / ``lineage`` /
     ``metadata`` with forbidden raw-transcript keys removed. The
     migration does not model raw transcript columns at all, so the
     primary risk is an operator-supplied evidence key — the scrub
     defends against that.
  6. Never raises on Supabase / query failure. Returns ``[]``.

Public surface (deliberately small):
  - retrieve_active_memory(brokerage_id, kind=None, limit=10)
  - retrieve_operational_memory(brokerage_id, limit=10)
  - retrieve_compliance_memory(brokerage_id, limit=10)
  - retrieve_optimization_memory(brokerage_id, limit=10)

PAS144E explicitly does NOT build:
  * retrieval-by-similarity, embeddings, vector indices;
  * automatic injection of memory into the PAS Brain runtime (that
    arrives only in PAS144F, behind an explicit operator flag);
  * autonomous learning / memory writes from the retrieval surface;
  * any unscoped helper;
  * any path that surfaces raw transcript fields, even if a row
    somehow carries one.
```

## Imports

``, `Any`, `Dict`, `List`, `MemoryKind`, `Optional`, `Union`, `__future__`, `annotations`, `contracts`, `logging`, `queries`, `ranking`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_kind`, `_safe_memory`, `_scrub_nested`, `retrieve_active_memory`, `retrieve_compliance_memory`, `retrieve_operational_memory`, `retrieve_optimization_memory`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS144E — Controlled active-memory retrieval.\n\nTenant-scoped read layer that sits on top of PAS144B's tenant-scoped\nquery helpers and PAS144E's deterministic ranking. Every helper here\nis a *read* helper — no writes, no transitions, no LLM calls, no\nembeddings, no autonomous learning.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped retrieval helper. The closest thing in the codebase\n     remains ``queries.list_memory_admin_unscoped`` (operator-only,\n     not consumed by retrieval).\n  2. Reads only through one of the audited PAS144B/D surfaces:\n     ``queries.list_active_memory_for_brokerage`` (status / expiry\n     filtered) — never raw table access here.\n  3. Ranks results through ``ranking.rank_memory_records`` so the\n     ordering is deterministic and operator-reviewable.\n  4. Caps the caller-supplied ``limit`` at ``queries.MAX_QUERY_LIMIT``.\n  5. Returns *safe* dicts only: a whitelisted subset of the row\n     columns plus a scrubbed copy of ``evidence`` / ``lineage`` /\n     ``metadata`` with forbidden raw-transcript keys removed. The\n     migration does not model raw transcript columns at all, so the\n     primary risk is an operator-supplied evidence key — the scrub\n     defends against that.\n  6. Never raises on Supabase / query failure. Returns ``[]``.\n\nPublic surface (deliberately small):\n  - retrieve_active_memory(brokerage_id, kind=None, limit=10)\n  - retrieve_operational_memory(brokerage_id, limit=10)\n  - retrieve_compliance_memory(brokerage_id, limit=10)\n  - retrieve_optimization_memory(brokerage_id, limit=10)\n\nPAS144E explicitly does NOT build:\n  * retrieval-by-similarity, embeddings, vector indices;\n  * automatic injection of memory into the PAS Brain runtime (that\n    arrives only in PAS144F, behind an explicit operator flag);\n  * autonomous learning / memory writes from the retrieval surface;\n  * any unscoped helper;\n  * any path that surfaces raw transcript fields, even if a row\n    somehow carries one.\n"
- 'pas.memory.retrieval'
- 'kind'
- 'limit'
- 'Any'
- 'return'
- 'int'
- 'Mirror queries.MAX_QUERY_LIMIT — no helper here pulls past it.'
- 'value'
- 'Dict[str, Any]'
- 'Drop forbidden raw-transcript keys from a nested dict.\n\nNon-dict values become ``{}`` — we never propagate an opaque blob\ntype (list, string, bytes) through the retrieval boundary even if\nthe underlying column somehow carried one.\n'
- 'row'
- 'Project a row into the PAS144E safety envelope.\n\nTop-level: only whitelisted columns.\nNested:    evidence / lineage / metadata are *copied* through the\n           scrubber so the caller cannot mutate the source row,\n           and so forbidden raw-transcript keys are guaranteed\n           absent.\n'
- 'evidence'
- 'lineage'
- 'metadata'
- 'Optional[str]'
- 'retrieval: ignoring unknown kind='
- 'brokerage_id'
- 'str'
- 'Union[None, str, MemoryKind]'
- 'List[Dict[str, Any]]'
- 'Return up to ``limit`` active-and-approved memory rows for\n``brokerage_id``, deterministically ranked.\n\nThe pipeline is intentionally narrow:\n\n  1. ``queries.list_active_memory_for_brokerage`` does the\n     tenant-scoped read. It already drops EXPIRED / REJECTED /\n     QUARANTINED rows and filters past-expires_at client-side.\n  2. ``ranking.rank_memory_records`` re-asserts the active\n     predicate (defence in depth) and orders by the deterministic\n     score from PAS144E. Unknown kind strings become an empty\n     result — the caller asked for a specific narrow read.\n  3. Each surviving row passes through ``_safe_memory`` so the\n     caller only ever sees whitelisted columns and a scrubbed\n     copy of evidence/lineage/metadata.\n\nReturns ``[]`` on:\n  * missing / blank ``brokerage_id``;\n  * unknown ``kind`` string (strict by design — see ranking.py);\n  * any Supabase failure inside the queries helper.\nNever raises.\n'
- 'retrieve_active_memory dropped | reason=missing_brokerage_id'
- 'retrieve_active_memory failed (non-critical) | brokerage='
- ' | error_type='
- 'OPERATIONAL-kind slice of ``retrieve_active_memory``.\n\nOPERATIONAL memory captures broker-level levers the PAS Brain has\nobserved working in practice (e.g. callback windows that get\nanswered, scripts that complete). Always tenant-scoped.\n'
- 'COMPLIANCE-kind slice of ``retrieve_active_memory``.\n\nCOMPLIANCE memory carries regulatory facts (TCPA windows, opt-out\nlists, do-not-call directives). It does not decay on TTL and is\nboosted by ranking so an eligible COMPLIANCE memory tends to\nsurface near the top of any retrieval.\n'
- 'OPTIMIZATION-kind slice of ``retrieve_active_memory``.\n\nOPTIMIZATION memory captures replay / experiment learnings the\noperator promoted into the approved set. Tenant-scoped, ranked\ndeterministically.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS144E — Controlled active-memory retrieval.\n\nTenant-scoped read layer that sits on top of PAS144B's tenant-scoped\nquery helpers and PAS144E's deterministic ranking. Every helper here\nis a *read* helper — no writes, no transitions, no LLM calls, no\nembeddings, no autonomous learning.\n\nHard contract — every public helper in this module:\n\n  1. Requires ``brokerage_id`` (tenant isolation, mandatory). There is\n     no unscoped retrieval helper. The closest thing in the codebase\n     remains ``queries.list_memory_admin_unscoped`` (operator-only,\n     not consumed by retrieval).\n  2. Reads only through one of the audited PAS144B/D surfaces:\n     ``queries.list_active_memory_for_brokerage`` (status / expiry\n     filtered) — never raw table access here.\n  3. Ranks results through ``ranking.rank_memory_records`` so the\n     ordering is deterministic and operator-reviewable.\n  4. Caps the caller-supplied ``limit`` at ``queries.MAX_QUERY_LIMIT``.\n  5. Returns *safe* dicts only: a whitelisted subset of the row\n     columns plus a scrubbed copy of ``evidence`` / ``lineage`` /\n     ``metadata`` with forbidden raw-transcript keys removed. The\n     migration does not model raw transcript columns at all, so the\n     primary risk is an operator-supplied evidence key — the scrub\n     defends against that.\n  6. Never raises on Supabase / query failure. Returns ``[]``.\n\nPublic surface (deliberately small):\n  - retrieve_active_memory(brokerage_id, kind=None, limit=10)\n  - retrieve_operational_memory(brokerage_id, limit=10)\n  - retrieve_compliance_memory(brokerage_id, limit=10)\n  - retrieve_optimization_memory(brokerage_id, limit=10)\n\nPAS144E explicitly does NOT build:\n  * retrieval-by-similarity, embeddings, vector indices;\n  * automatic injection of memory into the PAS Brain runtime (that\n    arrives only in PAS144F, behind an explicit operator flag);\n  * autonomous learning / memory writes from the retrieval surface;\n  * any unscoped helper;\n  * any path that surfaces raw transcript fields, even if a row\n    somehow carries one.\n")
              STORE_NAME               0 (__doc__)

 45           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 47           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 48           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Union'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              IMPORT_FROM              9 (Union)
              STORE_NAME               9 (Union)
              POP_TOP

 50           LOAD_SMALL_INT           1
              LOAD_CONST               4 (('queries',))
              IMPORT_NAME             10
              IMPORT_FROM             11 (queries)
              STORE_NAME              12 (queries_mod)
              POP_TOP

 51           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('ranking',))
              IMPORT_NAME             10
              IMPORT_FROM             13 (ranking)
              STORE_NAME              14 (ranking_mod)
              POP_TOP

 52           LOAD_SMALL_INT           1
              LOAD_CONST               6 (('MemoryKind',))
              IMPORT_NAME             15 (contracts)
              IMPORT_FROM             16 (MemoryKind)
              STORE_NAME              16 (MemoryKind)
              POP_TOP

 54           LOAD_NAME                3 (logging)
              LOAD_ATTR               34 (getLogger)
              PUSH_NULL
              LOAD_CONST               7 ('pas.memory.retrieval')
              CALL                     1
              STORE_NAME              18 (logger)

 60           LOAD_CONST              26 (('memory_id', 'brokerage_id', 'kind', 'source', 'status', 'title', 'summary', 'confidence', 'outcome_weight', 'evidence', 'lineage', 'metadata', 'created_at', 'expires_at'))
              STORE_NAME              19 (_SAFE_TOP_LEVEL_FIELDS)

 83           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              27 (frozenset({'raw_payload', 'full_transcript', 'turns_text', 'raw_payloads', 'utterances', 'transcripts', 'raw_transcript', 'transcript', 'messages', 'raw_text'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              21 (_FORBIDDEN_NESTED_KEYS)

101           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\retrieval.py", line 101>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _clamp_limit at 0x0000018C1796DBD0, file "app\services\memory\retrieval.py", line 101>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_clamp_limit)

112           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\retrieval.py", line 112>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _scrub_nested at 0x0000018C18060DB0, file "app\services\memory\retrieval.py", line 112>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_scrub_nested)

129           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\retrieval.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _safe_memory at 0x0000018C17D77E00, file "app\services\memory\retrieval.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_safe_memory)

154           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\retrieval.py", line 154>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _coerce_kind at 0x0000018C17FED830, file "app\services\memory\retrieval.py", line 154>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_coerce_kind)

172           LOAD_CONST               8 ('kind')

175           LOAD_CONST               2 (None)

172           LOAD_CONST              17 ('limit')

176           LOAD_SMALL_INT          10

172           BUILD_MAP                2
              LOAD_CONST              18 (<code object __annotate__ at 0x0000018C18025030, file "app\services\memory\retrieval.py", line 172>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object retrieve_active_memory at 0x0000018C17D6DFC0, file "app\services\memory\retrieval.py", line 172>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (retrieve_active_memory)

243           LOAD_CONST              17 ('limit')

246           LOAD_SMALL_INT          10

243           BUILD_MAP                1
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025730, file "app\services\memory\retrieval.py", line 243>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object retrieve_operational_memory at 0x0000018C180C4140, file "app\services\memory\retrieval.py", line 243>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              27 (retrieve_operational_memory)

259           LOAD_CONST              17 ('limit')

262           LOAD_SMALL_INT          10

259           BUILD_MAP                1
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18025830, file "app\services\memory\retrieval.py", line 259>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object retrieve_compliance_memory at 0x0000018C180C4580, file "app\services\memory\retrieval.py", line 259>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (retrieve_compliance_memory)

276           LOAD_CONST              17 ('limit')

279           LOAD_SMALL_INT          10

276           BUILD_MAP                1
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\memory\retrieval.py", line 276>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object retrieve_optimization_memory at 0x0000018C180C4030, file "app\services\memory\retrieval.py", line 276>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (retrieve_optimization_memory)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\retrieval.py", line 101>:
101           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('limit')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C1796DBD0, file "app\services\memory\retrieval.py", line 101>:
 101           RESUME                   0

 103           NOP

 104   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (limit)
               CALL                     1
               STORE_FAST               1 (n)

 107   L2:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE       17 (to L3)
               NOT_TAKEN

 108           LOAD_GLOBAL              6 (queries_mod)
               LOAD_ATTR                8 (DEFAULT_QUERY_LIMIT)
               RETURN_VALUE

 109   L3:     LOAD_GLOBAL             11 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL              6 (queries_mod)
               LOAD_ATTR               12 (MAX_QUERY_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 105           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       20 (to L6)
               NOT_TAKEN
               POP_TOP

 106           LOAD_GLOBAL              6 (queries_mod)
               LOAD_ATTR                8 (DEFAULT_QUERY_LIMIT)
               SWAP                     2
       L5:     POP_EXCEPT
               RETURN_VALUE

 105   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\retrieval.py", line 112>:
112           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scrub_nested at 0x0000018C18060DB0, file "app\services\memory\retrieval.py", line 112>:
112           RESUME                   0

119           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

120           BUILD_MAP                0
              RETURN_VALUE

121   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

122           LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (items + NULL|self)
              CALL                     0
              GET_ITER
      L2:     FOR_ITER                58 (to L4)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   35 (k, v)

123           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (k)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       28 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (k)
              LOAD_ATTR                9 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             10 (_FORBIDDEN_NESTED_KEYS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

124           JUMP_BACKWARD           54 (to L2)

125   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
              LOAD_FAST_BORROW         2 (k)
              STORE_SUBSCR
              JUMP_BACKWARD           60 (to L2)

122   L4:     END_FOR
              POP_ITER

126           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\retrieval.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_memory at 0x0000018C17D77E00, file "app\services\memory\retrieval.py", line 129>:
129           RESUME                   0

138           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

139           BUILD_MAP                0
              RETURN_VALUE

141   L1:     BUILD_MAP                0
              STORE_FAST               1 (safe)

142           LOAD_GLOBAL              4 (_SAFE_TOP_LEVEL_FIELDS)
              GET_ITER
      L2:     FOR_ITER               136 (to L6)
              STORE_FAST               2 (field)

143           LOAD_FAST_BORROW         2 (field)
              LOAD_CONST               1 ('evidence')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       32 (to L3)
              NOT_TAKEN

144           LOAD_GLOBAL              7 (_scrub_nested + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('evidence')
              CALL                     1
              CALL                     1
              LOAD_FAST_BORROW         1 (safe)
              LOAD_CONST               1 ('evidence')
              STORE_SUBSCR
              JUMP_BACKWARD           41 (to L2)

145   L3:     LOAD_FAST_BORROW         2 (field)
              LOAD_CONST               2 ('lineage')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       32 (to L4)
              NOT_TAKEN

146           LOAD_GLOBAL              7 (_scrub_nested + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('lineage')
              CALL                     1
              CALL                     1
              LOAD_FAST_BORROW         1 (safe)
              LOAD_CONST               2 ('lineage')
              STORE_SUBSCR
              JUMP_BACKWARD           79 (to L2)

147   L4:     LOAD_FAST_BORROW         2 (field)
              LOAD_CONST               3 ('metadata')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       32 (to L5)
              NOT_TAKEN

148           LOAD_GLOBAL              7 (_scrub_nested + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('metadata')
              CALL                     1
              CALL                     1
              LOAD_FAST_BORROW         1 (safe)
              LOAD_CONST               3 ('metadata')
              STORE_SUBSCR
              JUMP_BACKWARD          117 (to L2)

150   L5:     LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_FAST_BORROW         2 (field)
              CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (safe, field)
              STORE_SUBSCR
              JUMP_BACKWARD          138 (to L2)

142   L6:     END_FOR
              POP_ITER

151           LOAD_FAST_BORROW         1 (safe)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\retrieval.py", line 154>:
154           RESUME                   0
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

Disassembly of <code object _coerce_kind at 0x0000018C17FED830, file "app\services\memory\retrieval.py", line 154>:
 154           RESUME                   0

 155           LOAD_FAST_BORROW         0 (kind)
               POP_JUMP_IF_NOT_NONE     3 (to L1)
               NOT_TAKEN

 156           LOAD_CONST               0 (None)
               RETURN_VALUE

 157   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (kind)
               LOAD_GLOBAL              2 (MemoryKind)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       13 (to L2)
               NOT_TAKEN

 158           LOAD_FAST_BORROW         0 (kind)
               LOAD_ATTR                4 (value)
               RETURN_VALUE

 159   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

 160           NOP

 161   L3:     LOAD_GLOBAL              3 (MemoryKind + NULL)
               LOAD_FAST_BORROW         0 (kind)
               CALL                     1
               LOAD_ATTR                4 (value)
       L4:     RETURN_VALUE

 165   L5:     LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

 162           LOAD_GLOBAL             10 (ValueError)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       30 (to L8)
               NOT_TAKEN
               POP_TOP

 163           LOAD_GLOBAL             12 (logger)
               LOAD_ATTR               15 (warning + NULL|self)
               LOAD_CONST               1 ('retrieval: ignoring unknown kind=')
               LOAD_FAST                0 (kind)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

 164   L7:     POP_EXCEPT
               LOAD_CONST               0 (None)
               RETURN_VALUE

 162   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [0]
  L6 to L7 -> L9 [1] lasti
  L8 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\memory\retrieval.py", line 172>:
172           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

173           LOAD_CONST               2 ('str')

172           LOAD_CONST               3 ('kind')

175           LOAD_CONST               4 ('Union[None, str, MemoryKind]')

172           LOAD_CONST               5 ('limit')

176           LOAD_CONST               6 ('int')

172           LOAD_CONST               7 ('return')

177           LOAD_CONST               8 ('List[Dict[str, Any]]')

172           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object retrieve_active_memory at 0x0000018C17D6DFC0, file "app\services\memory\retrieval.py", line 172>:
 172            RESUME                   0

 200            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        24 (to L2)
                NOT_TAKEN

 201    L1:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)
                LOAD_CONST               1 ('retrieve_active_memory dropped | reason=missing_brokerage_id')
                CALL                     1
                POP_TOP

 202            BUILD_LIST               0
                RETURN_VALUE

 204    L2:     LOAD_GLOBAL             11 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 205            LOAD_GLOBAL             13 (_coerce_kind + NULL)
                LOAD_FAST_BORROW         1 (kind)
                CALL                     1
                STORE_FAST               4 (kind_value)

 206            LOAD_FAST_BORROW         1 (kind)
                POP_JUMP_IF_NONE         7 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (kind_value)
                POP_JUMP_IF_NOT_NONE     3 (to L3)
                NOT_TAKEN

 209            BUILD_LIST               0
                RETURN_VALUE

 213    L3:     LOAD_GLOBAL             15 (min + NULL)
                LOAD_FAST_BORROW         3 (capped)
                LOAD_SMALL_INT           3
                BINARY_OP                5 (*)
                LOAD_GLOBAL             16 (queries_mod)
                LOAD_ATTR               18 (MAX_QUERY_LIMIT)
                CALL                     2
                STORE_FAST               5 (overscan)

 215            NOP

 216    L4:     LOAD_GLOBAL             16 (queries_mod)
                LOAD_ATTR               20 (list_active_memory_for_brokerage)
                PUSH_NULL

 217            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0

 218            LOAD_FAST_BORROW         4 (kind_value)

 219            LOAD_FAST_BORROW         5 (overscan)

 216            LOAD_CONST               3 (('kind', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (rows)

 228    L5:     LOAD_FAST                6 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 229            BUILD_LIST               0
                RETURN_VALUE

 231    L6:     LOAD_GLOBAL             28 (ranking_mod)
                LOAD_ATTR               30 (rank_memory_records)
                PUSH_NULL

 232            LOAD_FAST                6 (rows)

 233            LOAD_FAST                4 (kind_value)

 234            LOAD_FAST                3 (capped)

 231            LOAD_CONST               6 (('kind', 'max_items'))
                CALL_KW                  3
                STORE_FAST               8 (ranked)

 236            LOAD_FAST                8 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (r)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2
        L8:     FOR_ITER                14 (to L9)
                STORE_FAST               9 (r)
                LOAD_GLOBAL             33 (_safe_memory + NULL)
                LOAD_FAST                9 (r)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L8)
        L9:     END_FOR
                POP_ITER
       L10:     SWAP                     2
                STORE_FAST               9 (r)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 221            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       59 (to L16)
                NOT_TAKEN
                STORE_FAST               7 (e)

 222   L12:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 223            LOAD_CONST               4 ('retrieve_active_memory failed (non-critical) | brokerage=')

 224            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST               5 (' | error_type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE

 223            BUILD_STRING             4

 222            CALL                     1
                POP_TOP

 226            BUILD_LIST               0
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               2 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 221   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L18:     SWAP                     2
                POP_TOP

 236            SWAP                     2
                STORE_FAST               9 (r)
                RERAISE                  0
ExceptionTable:
  L4 to L5 -> L11 [0]
  L7 to L10 -> L18 [2]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\memory\retrieval.py", line 243>:
243           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

244           LOAD_CONST               2 ('str')

243           LOAD_CONST               3 ('limit')

246           LOAD_CONST               4 ('int')

243           LOAD_CONST               5 ('return')

247           LOAD_CONST               6 ('List[Dict[str, Any]]')

243           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object retrieve_operational_memory at 0x0000018C180C4140, file "app\services\memory\retrieval.py", line 243>:
243           RESUME                   0

254           LOAD_GLOBAL              1 (retrieve_active_memory + NULL)

255           LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              2 (MemoryKind)
              LOAD_ATTR                4 (OPERATIONAL)
              LOAD_FAST_BORROW         1 (limit)

254           LOAD_CONST               1 (('kind', 'limit'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app\services\memory\retrieval.py", line 259>:
259           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

260           LOAD_CONST               2 ('str')

259           LOAD_CONST               3 ('limit')

262           LOAD_CONST               4 ('int')

259           LOAD_CONST               5 ('return')

263           LOAD_CONST               6 ('List[Dict[str, Any]]')

259           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object retrieve_compliance_memory at 0x0000018C180C4580, file "app\services\memory\retrieval.py", line 259>:
259           RESUME                   0

271           LOAD_GLOBAL              1 (retrieve_active_memory + NULL)

272           LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              2 (MemoryKind)
              LOAD_ATTR                4 (COMPLIANCE)
              LOAD_FAST_BORROW         1 (limit)

271           LOAD_CONST               1 (('kind', 'limit'))
              CALL_KW                  3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\memory\retrieval.py", line 276>:
276           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

277           LOAD_CONST               2 ('str')

276           LOAD_CONST               3 ('limit')

279           LOAD_CONST               4 ('int')

276           LOAD_CONST               5 ('return')

280           LOAD_CONST               6 ('List[Dict[str, Any]]')

276           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object retrieve_optimization_memory at 0x0000018C180C4030, file "app\services\memory\retrieval.py", line 276>:
276           RESUME                   0

287           LOAD_GLOBAL              1 (retrieve_active_memory + NULL)

288           LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              2 (MemoryKind)
              LOAD_ATTR                4 (OPTIMIZATION)
              LOAD_FAST_BORROW         1 (limit)

287           LOAD_CONST               1 (('kind', 'limit'))
              CALL_KW                  3
              RETURN_VALUE
```
