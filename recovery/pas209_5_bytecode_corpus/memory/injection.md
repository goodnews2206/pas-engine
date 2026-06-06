# memory/injection

- **pyc:** `app\services\memory\__pycache__\injection.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/injection.py`
- **co_filename (from bytecode):** `app\services\memory\injection.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144F — Operator-gated runtime memory injection.

The first place in the codebase where approved tenant memory can
influence call-runtime behaviour. Everything here is *opt-in*,
*audited*, and *defensive*:

  * the feature is OFF by default — nothing changes unless the
    brokerage's config explicitly carries ``memory_injection_enabled:
    true`` (top-level or under ``features.``);
  * retrieval is the PAS144E surface (approved + active only — no
    candidate / quarantined / rejected / dangerous);
  * formatting is the PAS144F formatter, which keeps only the seven
    runtime-safe fields and re-scrubs raw-transcript / raw-payload
    keys;
  * a retrieval / formatting failure returns a context whose
    ``enabled`` flag is False so the call flow proceeds **unchanged**;
  * ``inject_memory_into_prompt`` never mutates the base prompt — it
    returns a new string with the injected block appended, and
    returns the base prompt unchanged when the context is empty or
    disabled.

This phase deliberately does NOT modify ``app/engine/state_machine.py``
or any prompt builder. The hooks PAS144G will use are documented
below so the integration point is unambiguous.

Public surface:
  - memory_injection_enabled(brokerage_config)         -> bool
  - build_memory_context(brokerage_id, brokerage_config=None,
                         kinds=None, limit=5)          -> dict
  - inject_memory_into_prompt(base_prompt,
                              memory_context)          -> str

Integration points PAS144G should wire into (verified by inspection
of the call-runtime; this list is the contract PAS144G will lean on
— do NOT edit those files in this phase):

  * ``app/engine/state_machine.py``
        - ``self.prompts[State.X]`` — per-state prompt strings
          assembled from ``training`` config + defaults. PAS144G
          should wrap each prompt with ``inject_memory_into_prompt``
          when ``memory_injection_enabled`` is True for the brokerage.
        - Objection / booking / qualification paths each pull from
          ``self.prompts``; injecting at the dictionary boundary
          covers all three without bespoke per-state wiring.
  * Call-prompt builder (wherever ``state_machine.prompts`` is
        consumed by the Claude / LLM call) — apply injection just
        before the model receives the system prompt.

Hard constraints honoured:
  * additive only — no existing file is touched;
  * no DANGEROUS / QUARANTINED / CANDIDATE memory ever reaches the
    formatter (PAS144E retrieval only surfaces APPROVED, non-expired);
  * no raw transcript fields can enter the prompt (formatter +
    retrieval each strip them, defence in depth);
  * no embeddings, no vector search, no external vendors, no LLM
    calls in this module.

Return shape of ``build_memory_context`` (stable, machine-readable):

    {
        "enabled":      True | False,
        "brokerage_id": "<tenant>",
        "kinds":        [...kind values, deterministic order],
        "items":        [{... PAS144E safe envelope ...}, ...],
        "formatted":    "<delimited block, possibly empty>",
        "warnings":     [...non-fatal notes (e.g. retrieval_failed)],
    }
```

## Imports

``, `Any`, `Dict`, `Iterable`, `List`, `MemoryKind`, `Optional`, `Union`, `__future__`, `annotations`, `contracts`, `formatter`, `logging`, `retrieval`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_coerce_kinds`, `_empty_context`, `_resolve_flag`, `_truthy`, `build_memory_context`, `inject_memory_into_prompt`, `memory_injection_enabled`

## Env-key candidates

`APPROVED`, `DEFAULT_INJECTION_KINDS`

## String constants (redacted where noted)

- '\nPAS144F — Operator-gated runtime memory injection.\n\nThe first place in the codebase where approved tenant memory can\ninfluence call-runtime behaviour. Everything here is *opt-in*,\n*audited*, and *defensive*:\n\n  * the feature is OFF by default — nothing changes unless the\n    brokerage\'s config explicitly carries ``memory_injection_enabled:\n    true`` (top-level or under ``features.``);\n  * retrieval is the PAS144E surface (approved + active only — no\n    candidate / quarantined / rejected / dangerous);\n  * formatting is the PAS144F formatter, which keeps only the seven\n    runtime-safe fields and re-scrubs raw-transcript / raw-payload\n    keys;\n  * a retrieval / formatting failure returns a context whose\n    ``enabled`` flag is False so the call flow proceeds **unchanged**;\n  * ``inject_memory_into_prompt`` never mutates the base prompt — it\n    returns a new string with the injected block appended, and\n    returns the base prompt unchanged when the context is empty or\n    disabled.\n\nThis phase deliberately does NOT modify ``app/engine/state_machine.py``\nor any prompt builder. The hooks PAS144G will use are documented\nbelow so the integration point is unambiguous.\n\nPublic surface:\n  - memory_injection_enabled(brokerage_config)         -> bool\n  - build_memory_context(brokerage_id, brokerage_config=None,\n                         kinds=None, limit=5)          -> dict\n  - inject_memory_into_prompt(base_prompt,\n                              memory_context)          -> str\n\nIntegration points PAS144G should wire into (verified by inspection\nof the call-runtime; this list is the contract PAS144G will lean on\n— do NOT edit those files in this phase):\n\n  * ``app/engine/state_machine.py``\n        - ``self.prompts[State.X]`` — per-state prompt strings\n          assembled from ``training`` config + defaults. PAS144G\n          should wrap each prompt with ``inject_memory_into_prompt``\n          when ``memory_injection_enabled`` is True for the brokerage.\n        - Objection / booking / qualification paths each pull from\n          ``self.prompts``; injecting at the dictionary boundary\n          covers all three without bespoke per-state wiring.\n  * Call-prompt builder (wherever ``state_machine.prompts`` is\n        consumed by the Claude / LLM call) — apply injection just\n        before the model receives the system prompt.\n\nHard constraints honoured:\n  * additive only — no existing file is touched;\n  * no DANGEROUS / QUARANTINED / CANDIDATE memory ever reaches the\n    formatter (PAS144E retrieval only surfaces APPROVED, non-expired);\n  * no raw transcript fields can enter the prompt (formatter +\n    retrieval each strip them, defence in depth);\n  * no embeddings, no vector search, no external vendors, no LLM\n    calls in this module.\n\nReturn shape of ``build_memory_context`` (stable, machine-readable):\n\n    {\n        "enabled":      True | False,\n        "brokerage_id": "<tenant>",\n        "kinds":        [...kind values, deterministic order],\n        "items":        [{... PAS144E safe envelope ...}, ...],\n        "formatted":    "<delimited block, possibly empty>",\n        "warnings":     [...non-fatal notes (e.g. retrieval_failed)],\n    }\n'
- 'pas.memory.injection'
- 'memory_injection_enabled'
- 'tuple'
- 'DEFAULT_INJECTION_KINDS'
- 'enabled'
- 'warnings'
- 'kinds'
- 'limit'
- 'value'
- 'Any'
- 'return'
- 'bool'
- 'Strict True-only interpreter. ``"true"``/``1`` do not count —\na flag this load-bearing should require an explicit boolean.'
- 'brokerage_config'
- 'Read the injection flag out of a brokerage config dict.\n\nSupports both shapes used elsewhere in the repo:\n  * top-level: ``brokerage_config["memory_injection_enabled"]``\n  * nested:    ``brokerage_config["features"][...]``  (the new-\n               style feature dict from brokerage_store).\nEither path must evaluate to literal ``True``. Anything else\n(False / missing / truthy strings / non-bool) keeps the feature\noff.\n'
- 'features'
- 'List[str]'
- 'Coerce ``kinds`` into a deduplicated, deterministic list of\nclosed-enum strings. Drops unknown / forbidden entries silently.\n\nNone / empty → the documented default\n(``DEFAULT_INJECTION_KINDS``).\n'
- 'brokerage_id'
- 'str'
- 'Optional[List[str]]'
- 'Dict[str, Any]'
- 'items'
- 'formatted'
- 'Return True iff the brokerage config opts into runtime memory\ninjection.\n\nThe feature is OFF by default. Only an explicit\n``memory_injection_enabled: True`` (top-level or under\n``features.``) turns it on. Non-dict input is False.\n\nPure, never raises.\n'
- 'Union[None, str, MemoryKind, Iterable]'
- 'int'
- 'Build a runtime memory-injection context for ``brokerage_id``.\n\nSteps:\n  1. Reject missing brokerage_id (returns a disabled context).\n  2. Read the feature flag; if absent / False, return a disabled\n     context immediately (no retrieval call — saves DB round\n     trips when the feature is off, which is the default).\n  3. Resolve the requested kinds (defaults to COMPLIANCE +\n     OPERATIONAL + OPTIMIZATION).\n  4. For each kind, call ``retrieval.retrieve_active_memory``\n     tenant-scoped. PAS144E already filters to APPROVED + active +\n     safety envelope. We bundle the results in kind-declaration\n     order so COMPLIANCE always lands first.\n  5. Format via ``formatter.format_memory_for_prompt``.\n\nFailure modes — none raise:\n  * missing brokerage_id  → ``enabled=False`` + warning.\n  * feature flag off      → ``enabled=False`` (no warning;\n    normal state).\n  * retrieval failure     → ``enabled=False`` + warning\n    ``retrieval_failed:<kind>``. The base prompt is unchanged.\n  * formatter failure     → ``enabled=False`` + warning\n    ``formatter_failed`` (defensive — the formatter is pure and\n    does not normally raise).\n'
- 'missing_brokerage_id'
- 'build_memory_context retrieval failed (non-critical) | brokerage='
- ' | kind='
- ' | error_type='
- 'retrieval_failed:'
- 'status'
- 'APPROVED'
- 'kind'
- 'build_memory_context formatter failed (non-critical) | brokerage='
- 'formatter_failed'
- 'base_prompt'
- 'memory_context'
- 'Optional[Dict[str, Any]]'
- 'Return a new prompt string with the formatted memory block\nappended *below* ``base_prompt``.\n\nHard rules:\n  * The base prompt is NEVER mutated; this function returns a new\n    string. Callers that compare ``id(new) is id(base)`` should\n    get False whenever a block is appended.\n  * If the context is None / missing ``enabled`` / disabled, the\n    base prompt is returned **unchanged** (same string instance is\n    acceptable here — the caller can rely on byte equality).\n  * The delimiter pair from\n    ``formatter.{DELIMITER_OPEN,DELIMITER_CLOSE}`` is part of the\n    contract so PAS Brain can recognise (and audit) the block.\n  * No system / developer instruction is ever rewritten — the\n    memory block is *appended* below, with a blank line of\n    separation, and the preamble in the block itself explicitly\n    states that memory is guidance.\n\nPure, never raises.\n'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS144F — Operator-gated runtime memory injection.\n\nThe first place in the codebase where approved tenant memory can\ninfluence call-runtime behaviour. Everything here is *opt-in*,\n*audited*, and *defensive*:\n\n  * the feature is OFF by default — nothing changes unless the\n    brokerage\'s config explicitly carries ``memory_injection_enabled:\n    true`` (top-level or under ``features.``);\n  * retrieval is the PAS144E surface (approved + active only — no\n    candidate / quarantined / rejected / dangerous);\n  * formatting is the PAS144F formatter, which keeps only the seven\n    runtime-safe fields and re-scrubs raw-transcript / raw-payload\n    keys;\n  * a retrieval / formatting failure returns a context whose\n    ``enabled`` flag is False so the call flow proceeds **unchanged**;\n  * ``inject_memory_into_prompt`` never mutates the base prompt — it\n    returns a new string with the injected block appended, and\n    returns the base prompt unchanged when the context is empty or\n    disabled.\n\nThis phase deliberately does NOT modify ``app/engine/state_machine.py``\nor any prompt builder. The hooks PAS144G will use are documented\nbelow so the integration point is unambiguous.\n\nPublic surface:\n  - memory_injection_enabled(brokerage_config)         -> bool\n  - build_memory_context(brokerage_id, brokerage_config=None,\n                         kinds=None, limit=5)          -> dict\n  - inject_memory_into_prompt(base_prompt,\n                              memory_context)          -> str\n\nIntegration points PAS144G should wire into (verified by inspection\nof the call-runtime; this list is the contract PAS144G will lean on\n— do NOT edit those files in this phase):\n\n  * ``app/engine/state_machine.py``\n        - ``self.prompts[State.X]`` — per-state prompt strings\n          assembled from ``training`` config + defaults. PAS144G\n          should wrap each prompt with ``inject_memory_into_prompt``\n          when ``memory_injection_enabled`` is True for the brokerage.\n        - Objection / booking / qualification paths each pull from\n          ``self.prompts``; injecting at the dictionary boundary\n          covers all three without bespoke per-state wiring.\n  * Call-prompt builder (wherever ``state_machine.prompts`` is\n        consumed by the Claude / LLM call) — apply injection just\n        before the model receives the system prompt.\n\nHard constraints honoured:\n  * additive only — no existing file is touched;\n  * no DANGEROUS / QUARANTINED / CANDIDATE memory ever reaches the\n    formatter (PAS144E retrieval only surfaces APPROVED, non-expired);\n  * no raw transcript fields can enter the prompt (formatter +\n    retrieval each strip them, defence in depth);\n  * no embeddings, no vector search, no external vendors, no LLM\n    calls in this module.\n\nReturn shape of ``build_memory_context`` (stable, machine-readable):\n\n    {\n        "enabled":      True | False,\n        "brokerage_id": "<tenant>",\n        "kinds":        [...kind values, deterministic order],\n        "items":        [{... PAS144E safe envelope ...}, ...],\n        "formatted":    "<delimited block, possibly empty>",\n        "warnings":     [...non-fatal notes (e.g. retrieval_failed)],\n    }\n')
               STORE_NAME               1 (__doc__)

  71           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  73           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  74           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'Iterable', 'List', 'Optional', 'Union'))
               IMPORT_NAME              5 (typing)
               IMPORT_FROM              6 (Any)
               STORE_NAME               6 (Any)
               IMPORT_FROM              7 (Dict)
               STORE_NAME               7 (Dict)
               IMPORT_FROM              8 (Iterable)
               STORE_NAME               8 (Iterable)
               IMPORT_FROM              9 (List)
               STORE_NAME               9 (List)
               IMPORT_FROM             10 (Optional)
               STORE_NAME              10 (Optional)
               IMPORT_FROM             11 (Union)
               STORE_NAME              11 (Union)
               POP_TOP

  76           LOAD_SMALL_INT           1
               LOAD_CONST               4 (('formatter',))
               IMPORT_NAME             12
               IMPORT_FROM             13 (formatter)
               STORE_NAME              14 (formatter_mod)
               POP_TOP

  77           LOAD_SMALL_INT           1
               LOAD_CONST               5 (('retrieval',))
               IMPORT_NAME             12
               IMPORT_FROM             15 (retrieval)
               STORE_NAME              16 (retrieval_mod)
               POP_TOP

  78           LOAD_SMALL_INT           1
               LOAD_CONST               6 (('MemoryKind',))
               IMPORT_NAME             17 (contracts)
               IMPORT_FROM             18 (MemoryKind)
               STORE_NAME              18 (MemoryKind)
               POP_TOP

  80           LOAD_NAME                4 (logging)
               LOAD_ATTR               38 (getLogger)
               PUSH_NULL
               LOAD_CONST               7 ('pas.memory.injection')
               CALL                     1
               STORE_NAME              20 (logger)

  88           LOAD_CONST               8 ('memory_injection_enabled')
               STORE_NAME              21 (INJECTION_FLAG_KEY)

  93           LOAD_NAME               18 (MemoryKind)
               LOAD_ATTR               44 (COMPLIANCE)
               LOAD_ATTR               46 (value)

  94           LOAD_NAME               18 (MemoryKind)
               LOAD_ATTR               48 (OPERATIONAL)
               LOAD_ATTR               46 (value)

  95           LOAD_NAME               18 (MemoryKind)
               LOAD_ATTR               50 (OPTIMIZATION)
               LOAD_ATTR               46 (value)

  92           BUILD_TUPLE              3
               STORE_NAME              26 (DEFAULT_INJECTION_KINDS)
               LOAD_CONST               9 ('tuple')
               LOAD_NAME               27 (__annotations__)
               LOAD_CONST              10 ('DEFAULT_INJECTION_KINDS')
               STORE_SUBSCR

 102           LOAD_NAME               28 (frozenset)
               PUSH_NULL

 103           LOAD_NAME               18 (MemoryKind)
               LOAD_ATTR               58 (DANGEROUS)
               LOAD_ATTR               46 (value)

 104           LOAD_NAME               18 (MemoryKind)
               LOAD_ATTR               60 (EPHEMERAL)
               LOAD_ATTR               46 (value)

 102           BUILD_SET                2
               CALL                     1
               STORE_NAME              31 (_FORBIDDEN_INJECTION_KINDS)

 112           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\injection.py", line 112>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _truthy at 0x0000018C180691B0, file "app\services\memory\injection.py", line 112>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_truthy)

 118           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\injection.py", line 118>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _resolve_flag at 0x0000018C179A7290, file "app\services\memory\injection.py", line 118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_resolve_flag)

 139           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\injection.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _coerce_kinds at 0x0000018C17D78680, file "app\services\memory\injection.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_coerce_kinds)

 179           LOAD_CONST              17 ('enabled')

 182           LOAD_CONST              18 (False)

 179           LOAD_CONST              19 ('warnings')

 183           LOAD_CONST               2 (None)

 179           LOAD_CONST              20 ('kinds')

 184           LOAD_CONST               2 (None)

 179           BUILD_MAP                3
               LOAD_CONST              21 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\injection.py", line 179>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _empty_context at 0x0000018C18010F50, file "app\services\memory\injection.py", line 179>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              35 (_empty_context)

 200           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\injection.py", line 200>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object memory_injection_enabled at 0x0000018C17FA3B40, file "app\services\memory\injection.py", line 200>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (memory_injection_enabled)

 217           LOAD_CONST              30 ((None,))
               LOAD_CONST              20 ('kinds')

 221           LOAD_CONST               2 (None)

 217           LOAD_CONST              25 ('limit')

 222           LOAD_SMALL_INT           5

 217           BUILD_MAP                2
               LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025730, file "app\services\memory\injection.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object build_memory_context at 0x0000018C17ED8320, file "app\services\memory\injection.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              37 (build_memory_context)

 341           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024930, file "app\services\memory\injection.py", line 341>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object inject_memory_into_prompt at 0x0000018C17ECDD80, file "app\services\memory\injection.py", line 341>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (inject_memory_into_prompt)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\memory\injection.py", line 112>:
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _truthy at 0x0000018C180691B0, file "app\services\memory\injection.py", line 112>:
112           RESUME                   0

115           LOAD_FAST_BORROW         0 (value)
              LOAD_CONST               1 (True)
              IS_OP                    0 (is)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\memory\injection.py", line 118>:
118           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_config')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_flag at 0x0000018C179A7290, file "app\services\memory\injection.py", line 118>:
118           RESUME                   0

129           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage_config)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

130           LOAD_CONST               1 (False)
              RETURN_VALUE

131   L1:     LOAD_GLOBAL              5 (_truthy + NULL)
              LOAD_FAST_BORROW         0 (brokerage_config)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_GLOBAL              8 (INJECTION_FLAG_KEY)
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

132           LOAD_CONST               2 (True)
              RETURN_VALUE

133   L2:     LOAD_FAST_BORROW         0 (brokerage_config)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('features')
              CALL                     1
              STORE_FAST               1 (features)

134           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              5 (_truthy + NULL)
              LOAD_FAST_BORROW         1 (features)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_GLOBAL              8 (INJECTION_FLAG_KEY)
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

135           LOAD_CONST               2 (True)
              RETURN_VALUE

136   L3:     LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\injection.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kinds')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_kinds at 0x0000018C17D78680, file "app\services\memory\injection.py", line 139>:
 139            RESUME                   0

 146            LOAD_FAST_BORROW         0 (kinds)
                POP_JUMP_IF_NOT_NONE    16 (to L1)
                NOT_TAKEN

 147            LOAD_GLOBAL              1 (list + NULL)
                LOAD_GLOBAL              2 (DEFAULT_INJECTION_KINDS)
                CALL                     1
                RETURN_VALUE

 148    L1:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (kinds)
                LOAD_GLOBAL              6 (str)
                LOAD_GLOBAL              8 (MemoryKind)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        4 (to L2)
                NOT_TAKEN

 149            LOAD_FAST_BORROW         0 (kinds)
                BUILD_LIST               1
                STORE_FAST               0 (kinds)

 150    L2:     NOP

 151    L3:     LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST_BORROW         0 (kinds)
                CALL                     1
                STORE_FAST               1 (raw)

 154    L4:     LOAD_GLOBAL             13 (set + NULL)
                CALL                     0
                STORE_FAST               2 (seen)

 155            BUILD_LIST               0
                STORE_FAST               3 (out)

 156            LOAD_FAST                1 (raw)
                GET_ITER
        L5:     FOR_ITER               176 (to L13)
                STORE_FAST               4 (k)

 157            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                4 (k)
                LOAD_GLOBAL              8 (MemoryKind)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 158            LOAD_FAST                4 (k)
                LOAD_ATTR               14 (value)
                STORE_FAST               5 (value)
                JUMP_FORWARD            83 (to L10)

 159    L6:     LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                4 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       60 (to L9)
                NOT_TAKEN
                LOAD_FAST                4 (k)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       38 (to L9)
                NOT_TAKEN

 160            NOP

 161    L7:     LOAD_GLOBAL              9 (MemoryKind + NULL)
                LOAD_FAST                4 (k)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                CALL                     1
                LOAD_ATTR               14 (value)
                STORE_FAST               5 (value)
        L8:     JUMP_FORWARD             2 (to L10)

 165    L9:     JUMP_BACKWARD          121 (to L5)

 166   L10:     LOAD_FAST                5 (value)
                LOAD_GLOBAL             20 (_FORBIDDEN_INJECTION_KINDS)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 169            JUMP_BACKWARD          134 (to L5)

 170   L11:     LOAD_FAST_LOAD_FAST     82 (value, seen)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN

 171            JUMP_BACKWARD          142 (to L5)

 172   L12:     LOAD_FAST                2 (seen)
                LOAD_ATTR               23 (add + NULL|self)
                LOAD_FAST                5 (value)
                CALL                     1
                POP_TOP

 173            LOAD_FAST                3 (out)
                LOAD_ATTR               25 (append + NULL|self)
                LOAD_FAST                5 (value)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          178 (to L5)

 156   L13:     END_FOR
                POP_ITER

 174            LOAD_FAST                3 (out)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L14)
                NOT_TAKEN

 175            LOAD_GLOBAL              1 (list + NULL)
                LOAD_GLOBAL              2 (DEFAULT_INJECTION_KINDS)
                CALL                     1
                RETURN_VALUE

 176   L14:     LOAD_FAST                3 (out)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 152            LOAD_GLOBAL             10 (TypeError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       19 (to L17)
                NOT_TAKEN
                POP_TOP

 153            LOAD_GLOBAL              1 (list + NULL)
                LOAD_GLOBAL              2 (DEFAULT_INJECTION_KINDS)
                CALL                     1
                SWAP                     2
       L16:     POP_EXCEPT
                RETURN_VALUE

 152   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 162            LOAD_GLOBAL             18 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L21)
                NOT_TAKEN
                POP_TOP

 163   L20:     POP_EXCEPT
                JUMP_BACKWARD          251 (to L5)

 162   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L15 [0]
  L7 to L8 -> L19 [1]
  L15 to L16 -> L18 [1] lasti
  L17 to L18 -> L18 [1] lasti
  L19 to L20 -> L22 [2] lasti
  L21 to L22 -> L22 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\memory\injection.py", line 179>:
179           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

181           LOAD_CONST               2 ('str')

179           LOAD_CONST               3 ('enabled')

182           LOAD_CONST               4 ('bool')

179           LOAD_CONST               5 ('warnings')

183           LOAD_CONST               6 ('Optional[List[str]]')

179           LOAD_CONST               7 ('kinds')

184           LOAD_CONST               6 ('Optional[List[str]]')

179           LOAD_CONST               8 ('return')

185           LOAD_CONST               9 ('Dict[str, Any]')

179           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _empty_context at 0x0000018C18010F50, file "app\services\memory\injection.py", line 179>:
179           RESUME                   0

187           LOAD_CONST               0 ('enabled')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         1 (enabled)
              CALL                     1

188           LOAD_CONST               1 ('brokerage_id')
              LOAD_FAST                0 (brokerage_id)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')

189   L1:     LOAD_CONST               3 ('kinds')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                3 (kinds)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

190           LOAD_CONST               4 ('items')
              BUILD_LIST               0

191           LOAD_CONST               5 ('formatted')
              LOAD_CONST               2 ('')

192           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L3:     CALL                     1

186           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\memory\injection.py", line 200>:
200           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_config')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object memory_injection_enabled at 0x0000018C17FA3B40, file "app\services\memory\injection.py", line 200>:
200           RESUME                   0

210           LOAD_GLOBAL              1 (_resolve_flag + NULL)
              LOAD_FAST_BORROW         0 (brokerage_config)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\memory\injection.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

218           LOAD_CONST               2 ('Any')

217           LOAD_CONST               3 ('brokerage_config')

219           LOAD_CONST               2 ('Any')

217           LOAD_CONST               4 ('kinds')

221           LOAD_CONST               5 ('Union[None, str, MemoryKind, Iterable]')

217           LOAD_CONST               6 ('limit')

222           LOAD_CONST               7 ('int')

217           LOAD_CONST               8 ('return')

223           LOAD_CONST               9 ('Dict[str, Any]')

217           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object build_memory_context at 0x0000018C17ED8320, file "app\services\memory\injection.py", line 217>:
 217            RESUME                   0

 249            LOAD_GLOBAL              1 (isinstance + NULL)
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
                POP_JUMP_IF_TRUE        16 (to L2)
                NOT_TAKEN

 250    L1:     LOAD_GLOBAL              7 (_empty_context + NULL)

 251            LOAD_CONST               1 ('')

 252            LOAD_CONST               2 (False)

 253            LOAD_CONST               3 ('missing_brokerage_id')
                BUILD_LIST               1

 250            LOAD_CONST               4 (('brokerage_id', 'enabled', 'warnings'))
                CALL_KW                  3
                RETURN_VALUE

 256    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 258            LOAD_GLOBAL              9 (memory_injection_enabled + NULL)
                LOAD_FAST_BORROW         1 (brokerage_config)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L3)
                NOT_TAKEN

 259            LOAD_GLOBAL              7 (_empty_context + NULL)

 260            LOAD_FAST_BORROW         4 (bid)

 261            LOAD_CONST               2 (False)

 259            LOAD_CONST               5 (('brokerage_id', 'enabled'))
                CALL_KW                  2
                RETURN_VALUE

 264    L3:     NOP

 265    L4:     LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         3 (limit)
                CALL                     1
                STORE_FAST               5 (capped)

 268    L5:     LOAD_FAST_BORROW         5 (capped)
                LOAD_SMALL_INT           0
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 269            LOAD_SMALL_INT           5
                STORE_FAST               5 (capped)

 271    L6:     LOAD_GLOBAL             17 (_coerce_kinds + NULL)
                LOAD_FAST_BORROW         2 (kinds)
                CALL                     1
                STORE_FAST               6 (kind_values)

 273            BUILD_LIST               0
                STORE_FAST               7 (items)

 274            BUILD_LIST               0
                STORE_FAST               8 (warnings)

 278            LOAD_FAST_BORROW         6 (kind_values)
                GET_ITER
        L7:     FOR_ITER                55 (to L11)
                STORE_FAST               9 (kind_value)

 279            NOP

 280    L8:     LOAD_GLOBAL             18 (retrieval_mod)
                LOAD_ATTR               20 (retrieve_active_memory)
                PUSH_NULL

 281            LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (bid, kind_value)
                LOAD_FAST_BORROW         5 (capped)

 280            LOAD_CONST               6 (('kind', 'limit'))
                CALL_KW                  3
                STORE_FAST              10 (slice_items)

 293    L9:     LOAD_FAST               10 (slice_items)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           38 (to L7)

 294   L10:     LOAD_FAST                7 (items)
                LOAD_ATTR               35 (extend + NULL|self)
                LOAD_FAST               10 (slice_items)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           57 (to L7)

 278   L11:     END_FOR
                POP_ITER

 301            LOAD_FAST_BORROW         7 (items)
                GET_ITER

 300            LOAD_FAST_AND_CLEAR     12 (it)
                SWAP                     2
       L12:     BUILD_LIST               0
                SWAP                     2

 301   L13:     FOR_ITER                81 (to L20)
                STORE_FAST              12 (it)

 302            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW        12 (it)
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL

 301   L14:     POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L13)

 303   L15:     LOAD_FAST_BORROW        12 (it)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              13 ('APPROVED')
                COMPARE_OP              88 (bool(==))

 301   L16:     POP_JUMP_IF_TRUE         3 (to L17)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L13)

 304   L17:     LOAD_FAST_BORROW        12 (it)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              14 ('kind')
                CALL                     1
                LOAD_GLOBAL             40 (_FORBIDDEN_INJECTION_KINDS)
                CONTAINS_OP              1 (not in)

 301   L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           79 (to L13)
       L19:     LOAD_FAST_BORROW        12 (it)
                LIST_APPEND              2
                JUMP_BACKWARD           83 (to L13)
       L20:     END_FOR
                POP_ITER

 300   L21:     STORE_FAST               7 (items)
                STORE_FAST              12 (it)

 307            NOP

 308   L22:     LOAD_GLOBAL             42 (formatter_mod)
                LOAD_ATTR               44 (format_memory_for_prompt)
                PUSH_NULL

 309            LOAD_FAST_BORROW         7 (items)

 310            LOAD_FAST_BORROW         5 (capped)

 311            LOAD_GLOBAL             42 (formatter_mod)
                LOAD_ATTR               46 (DEFAULT_MAX_CHARS)

 308            LOAD_CONST              15 (('max_items', 'max_chars'))
                CALL_KW                  3
                STORE_FAST              13 (formatted)

 325   L23:     LOAD_GLOBAL             49 (bool + NULL)
                LOAD_FAST                7 (items)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L24)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             49 (bool + NULL)
                LOAD_FAST               13 (formatted)
                CALL                     1
       L24:     STORE_FAST              14 (enabled)

 328            LOAD_CONST              19 ('enabled')
                LOAD_FAST               14 (enabled)

 329            LOAD_CONST              20 ('brokerage_id')
                LOAD_FAST                4 (bid)

 330            LOAD_CONST              21 ('kinds')
                LOAD_FAST                6 (kind_values)

 331            LOAD_CONST              22 ('items')
                LOAD_FAST                7 (items)

 332            LOAD_CONST              23 ('formatted')
                LOAD_FAST               13 (formatted)

 333            LOAD_CONST              24 ('warnings')
                LOAD_FAST                8 (warnings)

 327            BUILD_MAP                6
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 266            LOAD_GLOBAL             12 (TypeError)
                LOAD_GLOBAL             14 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L27)
                NOT_TAKEN
                POP_TOP

 267            LOAD_SMALL_INT           5
                STORE_FAST               5 (capped)
       L26:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 284 (to L5)

 266   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 283            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       82 (to L33)
                NOT_TAKEN
                STORE_FAST              11 (e)

 286   L30:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 287            LOAD_CONST               7 ('build_memory_context retrieval failed (non-critical) | brokerage=')

 288            LOAD_FAST                4 (bid)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' | kind=')
                LOAD_FAST                9 (kind_value)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')

 289            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 287            BUILD_STRING             6

 286            CALL                     1
                POP_TOP

 291            LOAD_FAST                8 (warnings)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_CONST              10 ('retrieval_failed:')
                LOAD_FAST                9 (kind_value)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 292   L31:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD          349 (to L7)

  --   L32:     LOAD_CONST              11 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 283   L33:     RERAISE                  0

  --   L34:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L35:     SWAP                     2
                POP_TOP

 300            SWAP                     2
                STORE_FAST              12 (it)
                RERAISE                  0

  --   L36:     PUSH_EXC_INFO

 313            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       80 (to L41)
                NOT_TAKEN
                STORE_FAST              11 (e)

 314   L37:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 315            LOAD_CONST              16 ('build_memory_context formatter failed (non-critical) | brokerage=')

 316            LOAD_FAST                4 (bid)
                FORMAT_SIMPLE
                LOAD_CONST               9 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 315            BUILD_STRING             4

 314            CALL                     1
                POP_TOP

 318            LOAD_GLOBAL              7 (_empty_context + NULL)

 319            LOAD_FAST                4 (bid)

 320            LOAD_CONST               2 (False)

 321            LOAD_FAST                8 (warnings)
                LOAD_CONST              17 ('formatter_failed')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 322            LOAD_FAST                6 (kind_values)

 318            LOAD_CONST              18 (('brokerage_id', 'enabled', 'warnings', 'kinds'))
                CALL_KW                  4
       L38:     SWAP                     2
       L39:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L40:     LOAD_CONST              11 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 313   L41:     RERAISE                  0

  --   L42:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L25 [0]
  L8 to L9 -> L29 [1]
  L12 to L14 -> L35 [2]
  L15 to L16 -> L35 [2]
  L17 to L18 -> L35 [2]
  L19 to L21 -> L35 [2]
  L22 to L23 -> L36 [0]
  L25 to L26 -> L28 [1] lasti
  L27 to L28 -> L28 [1] lasti
  L29 to L30 -> L34 [2] lasti
  L30 to L31 -> L32 [2] lasti
  L32 to L34 -> L34 [2] lasti
  L36 to L37 -> L42 [1] lasti
  L37 to L38 -> L40 [1] lasti
  L38 to L39 -> L42 [1] lasti
  L40 to L42 -> L42 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\memory\injection.py", line 341>:
341           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('base_prompt')

342           LOAD_CONST               2 ('str')

341           LOAD_CONST               3 ('memory_context')

343           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

341           LOAD_CONST               5 ('return')

344           LOAD_CONST               2 ('str')

341           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object inject_memory_into_prompt at 0x0000018C17ECDD80, file "app\services\memory\injection.py", line 341>:
341           RESUME                   0

365           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (base_prompt)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

368           LOAD_CONST               1 ('')
              RETURN_VALUE

370   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (memory_context)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

371           LOAD_FAST_BORROW         0 (base_prompt)
              RETURN_VALUE

372   L2:     LOAD_FAST_BORROW         1 (memory_context)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               2 ('enabled')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

373           LOAD_FAST_BORROW         0 (base_prompt)
              RETURN_VALUE

374   L3:     LOAD_FAST_BORROW         1 (memory_context)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('formatted')
              CALL                     1
              STORE_FAST               2 (formatted)

375           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (formatted)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (formatted)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN

376   L4:     LOAD_FAST_BORROW         0 (base_prompt)
              RETURN_VALUE

382   L5:     LOAD_GLOBAL              8 (formatter_mod)
              LOAD_ATTR               10 (DELIMITER_OPEN)
              LOAD_FAST_BORROW         2 (formatted)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE        22 (to L6)
              NOT_TAKEN

383           LOAD_GLOBAL              8 (formatter_mod)
              LOAD_ATTR               12 (DELIMITER_CLOSE)
              LOAD_FAST_BORROW         2 (formatted)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L7)
              NOT_TAKEN

385   L6:     LOAD_FAST_BORROW         0 (base_prompt)
              RETURN_VALUE

389   L7:     LOAD_FAST_BORROW         0 (base_prompt)
              LOAD_CONST               4 ('\n\n')
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         2 (formatted)
              BINARY_OP                0 (+)
              RETURN_VALUE
```
