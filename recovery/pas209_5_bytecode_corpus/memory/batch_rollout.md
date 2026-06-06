# memory/batch_rollout

- **pyc:** `app\services\memory\__pycache__\batch_rollout.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/batch_rollout.py`
- **co_filename (from bytecode):** `app\services\memory\batch_rollout.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144N — Batch rollout planner (pure).

Multi-brokerage extension of PAS144K's planning module. Takes a list
of PAS144J impact reports (one per brokerage) plus an optional map of
current brokerage configs and returns a batch plan: one PAS144K
rollout plan per brokerage, with aggregated action counts.

Hard contract — every public helper here is pure:
  * NO I/O, NO LLM, NO Supabase, NO embeddings, NO vector helpers.
    Imports are limited to :mod:`app.services.memory.rollout`.
  * Inputs are read-only — never mutated. Outputs are freshly
    constructed.
  * Structural-only outputs — the per-brokerage plan is the PAS144K
    plan with its already-filtered evidence whitelist. No raw memory,
    prompt, transcript, or evidence-payload content can enter.
  * Malformed inputs degrade gracefully — a report that cannot be
    matched to a brokerage_id, or whose summary cannot be parsed,
    collapses to a propose_hold plan with structural warnings.
  * No apply path. ``apply_batch_rollout_plan`` does not exist by
    design — applying a batch requires per-brokerage signed manifests,
    which is the PAS144L doctrine. PAS144N is planning-only.
  * No widening of allowed_patch — every child plan still carries the
    same ``features.memory_injection_enabled`` shape.

Public surface (deliberately small):
  - build_batch_rollout_plan(impact_reports, current_configs=None) -> dict
  - validate_batch_rollout_plan(batch_plan)                        -> list[str]
  - split_batch_actions(batch_plan)                                -> dict
  - batch_plan_summary(batch_plan)                                 -> dict
```

## Imports

``, `Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `datetime`, `rollout`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_extract_brokerage_id`, `_normalise_action_counts`, `_resolve_config`, `batch_plan_summary`, `build_batch_rollout_plan`, `split_batch_actions`, `validate_batch_rollout_plan`

## Env-key candidates

_none_

## String constants (redacted where noted)

- "\nPAS144N — Batch rollout planner (pure).\n\nMulti-brokerage extension of PAS144K's planning module. Takes a list\nof PAS144J impact reports (one per brokerage) plus an optional map of\ncurrent brokerage configs and returns a batch plan: one PAS144K\nrollout plan per brokerage, with aggregated action counts.\n\nHard contract — every public helper here is pure:\n  * NO I/O, NO LLM, NO Supabase, NO embeddings, NO vector helpers.\n    Imports are limited to :mod:`app.services.memory.rollout`.\n  * Inputs are read-only — never mutated. Outputs are freshly\n    constructed.\n  * Structural-only outputs — the per-brokerage plan is the PAS144K\n    plan with its already-filtered evidence whitelist. No raw memory,\n    prompt, transcript, or evidence-payload content can enter.\n  * Malformed inputs degrade gracefully — a report that cannot be\n    matched to a brokerage_id, or whose summary cannot be parsed,\n    collapses to a propose_hold plan with structural warnings.\n  * No apply path. ``apply_batch_rollout_plan`` does not exist by\n    design — applying a batch requires per-brokerage signed manifests,\n    which is the PAS144L doctrine. PAS144N is planning-only.\n  * No widening of allowed_patch — every child plan still carries the\n    same ``features.memory_injection_enabled`` shape.\n\nPublic surface (deliberately small):\n  - build_batch_rollout_plan(impact_reports, current_configs=None) -> dict\n  - validate_batch_rollout_plan(batch_plan)                        -> list[str]\n  - split_batch_actions(batch_plan)                                -> dict\n  - batch_plan_summary(batch_plan)                                 -> dict\n"
- 'impact_report'
- 'Any'
- 'return'
- 'str'
- 'Pull a non-empty brokerage_id from a PAS144J report envelope.'
- 'brokerage_id'
- 'current_configs'
- 'Optional[Dict[str, Any]]'
- 'Look up ``brokerage_id`` in the optional configs map.'
- 'plans'
- 'List[Dict[str, Any]]'
- 'Dict[str, int]'
- 'Return a complete action_counts dict over the closed set.'
- 'recommended_action'
- 'impact_reports'
- 'Optional[Dict[str, Dict[str, Any]]]'
- 'Dict[str, Any]'
- 'Build a batch plan from multiple PAS144J impact reports.\n\nInputs:\n  * ``impact_reports``   — iterable of PAS144J report envelopes\n                            (or bare summaries). Order is preserved\n                            in the output ``plans`` list.\n  * ``current_configs``  — optional map keyed by brokerage_id,\n                            value = brokerage row (or any dict\n                            carrying ``memory_injection_enabled``).\n\nOutput shape:\n    {\n        "batch_id":          <uuid4>,\n        "created_at":        <iso8601-utc>,\n        "total_brokerages":  <int>,\n        "plans":             [<PAS144K plan>, ...],\n        "action_counts":     {action: count, ...},\n        "warnings":          [<str>, ...],\n    }\n\nPure. Never raises. Malformed inputs degrade to propose_hold\nplans with structural warnings; the rollout module\'s evidence\nwhitelist closes the door on raw payload leakage.\n'
- 'impact_reports_not_iterable'
- 'current_configs_not_dict_ignored'
- 'duplicate_brokerage_id:'
- 'batch_id'
- 'created_at'
- 'total_brokerages'
- 'action_counts'
- 'warnings'
- 'batch_plan'
- 'List[str]'
- "Return a list of human-readable blockers for the batch plan.\n\nPure. Never raises. Empty list ⇒ batch is structurally well-formed\n(it does NOT guarantee any individual recommendation is the right\none — that is the operator's call).\n\nChecks:\n  * batch envelope shape;\n  * every plan inside ``plans`` validates via PAS144K\n    ``validate_rollout_plan`` — child blockers are prefixed with\n    ``plan[i]:`` so the caller can locate the offender;\n  * ``action_counts`` keys are the closed set and values are ints;\n  * ``total_brokerages`` matches len(plans).\n"
- 'batch_must_be_dict'
- 'missing_batch_id'
- 'missing_created_at'
- 'invalid_plans_type'
- 'plan['
- 'invalid_total_brokerages'
- 'total_brokerages_mismatch'
- 'invalid_action_counts_type'
- 'action_counts_has_disallowed_keys:'
- 'invalid_action_count_value:'
- 'invalid_warnings_type'
- 'Dict[str, List[Dict[str, Any]]]'
- 'Group child plans by ``recommended_action``.\n\nReturns a dict keyed by every action in the closed set (so callers\ncan rely on the schema regardless of the input). Each value is a\nlist of the original plan dicts in their original order. A\nmalformed batch returns the full-keyed dict with empty lists.\n\nPure. Never raises.\n'
- 'Return a counts-only summary of the batch plan.\n\nOutput shape:\n    {\n        "batch_id":          <str>,\n        "total_brokerages":  <int>,\n        "action_counts":     {action: count, ...},\n        "applyable_count":   <int>,     # propose_enable + propose_disable\n        "requires_approval_count": <int>,\n        "warning_count":     <int>,\n    }\n\nCarries NO raw evidence and NO per-brokerage detail — by design.\nUse ``split_batch_actions`` if you need the plan dicts grouped.\n\nPure. Never raises.\n'
- 'applyable_count'
- 'requires_approval_count'
- 'warning_count'
- 'requires_operator_approval'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ("\nPAS144N — Batch rollout planner (pure).\n\nMulti-brokerage extension of PAS144K's planning module. Takes a list\nof PAS144J impact reports (one per brokerage) plus an optional map of\ncurrent brokerage configs and returns a batch plan: one PAS144K\nrollout plan per brokerage, with aggregated action counts.\n\nHard contract — every public helper here is pure:\n  * NO I/O, NO LLM, NO Supabase, NO embeddings, NO vector helpers.\n    Imports are limited to :mod:`app.services.memory.rollout`.\n  * Inputs are read-only — never mutated. Outputs are freshly\n    constructed.\n  * Structural-only outputs — the per-brokerage plan is the PAS144K\n    plan with its already-filtered evidence whitelist. No raw memory,\n    prompt, transcript, or evidence-payload content can enter.\n  * Malformed inputs degrade gracefully — a report that cannot be\n    matched to a brokerage_id, or whose summary cannot be parsed,\n    collapses to a propose_hold plan with structural warnings.\n  * No apply path. ``apply_batch_rollout_plan`` does not exist by\n    design — applying a batch requires per-brokerage signed manifests,\n    which is the PAS144L doctrine. PAS144N is planning-only.\n  * No widening of allowed_patch — every child plan still carries the\n    same ``features.memory_injection_enabled`` shape.\n\nPublic surface (deliberately small):\n  - build_batch_rollout_plan(impact_reports, current_configs=None) -> dict\n  - validate_batch_rollout_plan(batch_plan)                        -> list[str]\n  - split_batch_actions(batch_plan)                                -> dict\n  - batch_plan_summary(batch_plan)                                 -> dict\n")
              STORE_NAME               0 (__doc__)

 33           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 35           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (uuid)
              STORE_NAME               3 (uuid)

 36           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 37           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 39           LOAD_SMALL_INT           1
              LOAD_CONST               5 (('rollout',))
              IMPORT_NAME             11
              IMPORT_FROM             12 (rollout)
              STORE_NAME              13 (rollout_mod)
              POP_TOP

 49           LOAD_NAME               13 (rollout_mod)
              LOAD_ATTR               28 (ACTION_NO_CHANGE)

 50           LOAD_NAME               13 (rollout_mod)
              LOAD_ATTR               30 (ACTION_PROPOSE_ENABLE)

 51           LOAD_NAME               13 (rollout_mod)
              LOAD_ATTR               32 (ACTION_PROPOSE_DISABLE)

 52           LOAD_NAME               13 (rollout_mod)
              LOAD_ATTR               34 (ACTION_PROPOSE_HOLD)

 53           LOAD_NAME               13 (rollout_mod)
              LOAD_ATTR               36 (ACTION_PROPOSE_INVESTIGATE)

 48           BUILD_TUPLE              5
              STORE_NAME              19 (_ALL_ACTIONS)

 58           LOAD_NAME               20 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              20 (frozenset({'provider_failure_rate_without_memory', 'memory_succeeded_calls', 'health_status', 'rollout_recommendation', 'total_calls', 'callback_rate_with_memory', 'callback_rate_without_memory', 'lift_callback_rate', 'lift_booking_rate', 'booking_rate_without_memory', 'booking_rate_with_memory', 'non_memory_calls', 'provider_failure_rate_with_memory'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              21 (_SAFE_EVIDENCE_FIELDS)

 79           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\batch_rollout.py", line 79>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _extract_brokerage_id at 0x0000018C1804CD30, file "app\services\memory\batch_rollout.py", line 79>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_extract_brokerage_id)

 88           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\batch_rollout.py", line 88>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _resolve_config at 0x0000018C17F96420, file "app\services\memory\batch_rollout.py", line 88>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_resolve_config)

 99           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\batch_rollout.py", line 99>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _normalise_action_counts at 0x0000018C179C3C30, file "app\services\memory\batch_rollout.py", line 99>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_normalise_action_counts)

113           LOAD_CONST              21 ((None,))
              LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18024930, file "app\services\memory\batch_rollout.py", line 113>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object build_batch_rollout_plan at 0x0000018C17D7E1D0, file "app\services\memory\batch_rollout.py", line 113>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              25 (build_batch_rollout_plan)

182           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\batch_rollout.py", line 182>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object validate_batch_rollout_plan at 0x0000018C177C69F0, file "app\services\memory\batch_rollout.py", line 182>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (validate_batch_rollout_plan)

247           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\batch_rollout.py", line 247>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object split_batch_actions at 0x0000018C17D8C5C0, file "app\services\memory\batch_rollout.py", line 247>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (split_batch_actions)

276           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\batch_rollout.py", line 276>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object batch_plan_summary at 0x0000018C17E952F0, file "app\services\memory\batch_rollout.py", line 276>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (batch_plan_summary)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\batch_rollout.py", line 79>:
 79           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('impact_report')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _extract_brokerage_id at 0x0000018C1804CD30, file "app\services\memory\batch_rollout.py", line 79>:
 79           RESUME                   0

 81           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (impact_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L1)
              NOT_TAKEN

 82           LOAD_FAST_BORROW         0 (impact_report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('brokerage_id')
              CALL                     1
              STORE_FAST               1 (bid)

 83           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (bid)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

 84           LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

 85   L1:     LOAD_CONST               2 ('')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\memory\batch_rollout.py", line 88>:
 88           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

 89           LOAD_CONST               2 ('str')

 88           LOAD_CONST               3 ('current_configs')

 90           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

 88           LOAD_CONST               5 ('return')

 91           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

 88           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _resolve_config at 0x0000018C17F96420, file "app\services\memory\batch_rollout.py", line 88>:
 88           RESUME                   0

 93           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (current_configs)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

 94   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

 95   L2:     LOAD_FAST_BORROW         1 (current_configs)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         0 (brokerage_id)
              CALL                     1
              STORE_FAST               2 (cfg)

 96           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (cfg)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (cfg)
              RETURN_VALUE
      L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app\services\memory\batch_rollout.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plans')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, int]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_action_counts at 0x0000018C179C3C30, file "app\services\memory\batch_rollout.py", line 99>:
  99            RESUME                   0

 101            LOAD_GLOBAL              0 (_ALL_ACTIONS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (a)
                SWAP                     2
        L1:     BUILD_MAP                0
                SWAP                     2
        L2:     FOR_ITER                 5 (to L3)
                STORE_FAST_LOAD_FAST    17 (a, a)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     STORE_FAST               2 (counts)
                STORE_FAST               1 (a)

 102            LOAD_FAST_BORROW         0 (plans)
                GET_ITER
        L5:     FOR_ITER                96 (to L10)
                STORE_FAST               3 (p)

 103            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (p)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (p)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('recommended_action')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               2 (None)
        L7:     STORE_FAST               4 (action)

 104            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (action)
                LOAD_GLOBAL              8 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L5)
        L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (action, counts)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           76 (to L5)

 105    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (counts, action)
                COPY                     2
                COPY                     2
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                SWAP                     3
                SWAP                     2
                STORE_SUBSCR
                JUMP_BACKWARD           98 (to L5)

 102   L10:     END_FOR
                POP_ITER

 106            LOAD_FAST_BORROW         2 (counts)
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 101            SWAP                     2
                STORE_FAST               1 (a)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\memory\batch_rollout.py", line 113>:
113           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('impact_reports')

114           LOAD_CONST               2 ('Any')

113           LOAD_CONST               3 ('current_configs')

115           LOAD_CONST               4 ('Optional[Dict[str, Dict[str, Any]]]')

113           LOAD_CONST               5 ('return')

116           LOAD_CONST               6 ('Dict[str, Any]')

113           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_batch_rollout_plan at 0x0000018C17D7E1D0, file "app\services\memory\batch_rollout.py", line 113>:
113           RESUME                   0

141           BUILD_LIST               0
              STORE_FAST               2 (warnings)

143           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (impact_reports)
              LOAD_GLOBAL              2 (list)
              LOAD_GLOBAL              4 (tuple)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        21 (to L1)
              NOT_TAKEN

144           LOAD_FAST_BORROW         2 (warnings)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               1 ('impact_reports_not_iterable')
              CALL                     1
              POP_TOP

145           BUILD_LIST               0
              STORE_FAST               3 (reports_iter)
              JUMP_FORWARD            11 (to L2)

147   L1:     LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         0 (impact_reports)
              CALL                     1
              STORE_FAST               3 (reports_iter)

149   L2:     LOAD_FAST_BORROW         1 (current_configs)
              POP_JUMP_IF_NONE        42 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (current_configs)
              LOAD_GLOBAL              8 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        20 (to L3)
              NOT_TAKEN

150           LOAD_FAST_BORROW         2 (warnings)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               3 ('current_configs_not_dict_ignored')
              CALL                     1
              POP_TOP

151           LOAD_CONST               2 (None)
              STORE_FAST               1 (current_configs)

153   L3:     BUILD_LIST               0
              STORE_FAST               4 (plans)

154           LOAD_GLOBAL             11 (set + NULL)
              CALL                     0
              STORE_FAST               5 (seen_ids)

156           LOAD_FAST_BORROW         3 (reports_iter)
              GET_ITER
      L4:     FOR_ITER               118 (to L7)
              STORE_FAST               6 (report)

157           LOAD_GLOBAL             13 (_extract_brokerage_id + NULL)
              LOAD_FAST_BORROW         6 (report)
              CALL                     1
              STORE_FAST               7 (brokerage_id)

158           LOAD_GLOBAL             15 (_resolve_config + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 113 (brokerage_id, current_configs)
              CALL                     2
              STORE_FAST               8 (config)

159           LOAD_GLOBAL             16 (rollout_mod)
              LOAD_ATTR               18 (build_rollout_plan)
              PUSH_NULL
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (report, config)
              LOAD_CONST               4 (('current_config',))
              CALL_KW                  2
              STORE_FAST               9 (plan)

160           LOAD_FAST_BORROW         4 (plans)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         9 (plan)
              CALL                     1
              POP_TOP

161           LOAD_FAST_BORROW         7 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           75 (to L4)

162   L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (brokerage_id, seen_ids)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       21 (to L6)
              NOT_TAKEN

163           LOAD_FAST_BORROW         2 (warnings)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('duplicate_brokerage_id:')
              LOAD_FAST_BORROW         7 (brokerage_id)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP

164   L6:     LOAD_FAST_BORROW         5 (seen_ids)
              LOAD_ATTR               21 (add + NULL|self)
              LOAD_FAST_BORROW         7 (brokerage_id)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          120 (to L4)

156   L7:     END_FOR
              POP_ITER

166           LOAD_GLOBAL             23 (_normalise_action_counts + NULL)
              LOAD_FAST_BORROW         4 (plans)
              CALL                     1
              STORE_FAST              10 (action_counts)

169           LOAD_CONST               6 ('batch_id')
              LOAD_GLOBAL             25 (str + NULL)
              LOAD_GLOBAL             26 (uuid)
              LOAD_ATTR               28 (uuid4)
              PUSH_NULL
              CALL                     0
              CALL                     1

170           LOAD_CONST               7 ('created_at')
              LOAD_GLOBAL             30 (datetime)
              LOAD_ATTR               32 (now)
              PUSH_NULL
              LOAD_GLOBAL             34 (timezone)
              LOAD_ATTR               36 (utc)
              CALL                     1
              LOAD_ATTR               39 (isoformat + NULL|self)
              CALL                     0

171           LOAD_CONST               8 ('total_brokerages')
              LOAD_GLOBAL             41 (len + NULL)
              LOAD_FAST_BORROW         4 (plans)
              CALL                     1

172           LOAD_CONST               9 ('plans')
              LOAD_FAST_BORROW         4 (plans)

173           LOAD_CONST              10 ('action_counts')
              LOAD_FAST_BORROW        10 (action_counts)

174           LOAD_CONST              11 ('warnings')
              LOAD_FAST_BORROW         2 (warnings)

168           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\batch_rollout.py", line 182>:
182           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('batch_plan')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_batch_rollout_plan at 0x0000018C177C69F0, file "app\services\memory\batch_rollout.py", line 182>:
182            RESUME                   0

197            BUILD_LIST               0
               STORE_FAST               1 (errors)

198            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

199            LOAD_CONST               1 ('batch_must_be_dict')
               BUILD_LIST               1
               RETURN_VALUE

201    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('batch_id')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_CONST               2 ('batch_id')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

202    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_batch_id')
               CALL                     1
               POP_TOP

203    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('created_at')
               CALL                     1
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_CONST               4 ('created_at')
               BINARY_OP               26 ([])
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L5)
               NOT_TAKEN

204    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('missing_created_at')
               CALL                     1
               POP_TOP

206    L5:     LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('plans')
               CALL                     1
               STORE_FAST               2 (plans)

207            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (plans)
               LOAD_GLOBAL             12 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L6)
               NOT_TAKEN

208            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('invalid_plans_type')
               CALL                     1
               POP_TOP

209            LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

211    L6:     LOAD_GLOBAL             15 (enumerate + NULL)
               LOAD_FAST_BORROW         2 (plans)
               CALL                     1
               GET_ITER
       L7:     FOR_ITER                57 (to L10)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   52 (i, plan)

212            LOAD_GLOBAL             16 (rollout_mod)
               LOAD_ATTR               18 (validate_rollout_plan)
               PUSH_NULL
               LOAD_FAST_BORROW         4 (plan)
               CALL                     1
               GET_ITER
       L8:     FOR_ITER                26 (to L9)
               STORE_FAST               5 (e)

213            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               8 ('plan[')
               LOAD_FAST_BORROW         3 (i)
               FORMAT_SIMPLE
               LOAD_CONST               9 (']:')
               LOAD_FAST_BORROW         5 (e)
               FORMAT_SIMPLE
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           28 (to L8)

212    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD           59 (to L7)

211   L10:     END_FOR
               POP_ITER

215            LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('total_brokerages')
               CALL                     1
               STORE_FAST               6 (total)

216            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (total)
               LOAD_GLOBAL             20 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L11)
               NOT_TAKEN
               LOAD_FAST_BORROW         6 (total)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       19 (to L12)
               NOT_TAKEN

217   L11:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('invalid_total_brokerages')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            33 (to L13)

218   L12:     LOAD_FAST_BORROW         6 (total)
               LOAD_GLOBAL             23 (len + NULL)
               LOAD_FAST_BORROW         2 (plans)
               CALL                     1
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE       18 (to L13)
               NOT_TAKEN

219            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('total_brokerages_mismatch')
               CALL                     1
               POP_TOP

221   L13:     LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('action_counts')
               CALL                     1
               STORE_FAST               7 (counts)

222            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (counts)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L14)
               NOT_TAKEN

223            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              14 ('invalid_action_counts_type')
               CALL                     1
               POP_TOP
               JUMP_FORWARD           160 (to L19)

226   L14:     LOAD_GLOBAL             25 (sorted + NULL)
               LOAD_CONST              15 (<code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\batch_rollout.py", line 226>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         7 (counts)
               LOAD_ATTR               27 (keys + NULL|self)
               CALL                     0
               GET_ITER
               CALL                     0
               CALL                     1
               STORE_FAST               8 (extra)

227            LOAD_FAST_BORROW         8 (extra)
               TO_BOOL
               POP_JUMP_IF_FALSE       40 (to L15)
               NOT_TAKEN

228            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)

229            LOAD_CONST              16 ('action_counts_has_disallowed_keys:')
               LOAD_CONST              17 (',')
               LOAD_ATTR               29 (join + NULL|self)
               LOAD_FAST_BORROW         8 (extra)
               CALL                     1
               BINARY_OP                0 (+)

228            CALL                     1
               POP_TOP

232   L15:     LOAD_GLOBAL             30 (_ALL_ACTIONS)
               GET_ITER
      L16:     FOR_ITER                71 (to L18)
               STORE_FAST               9 (action)

233            LOAD_FAST_BORROW         7 (counts)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_FAST_BORROW         9 (action)
               CALL                     1
               STORE_FAST              10 (v)

234            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        10 (v)
               LOAD_GLOBAL             20 (int)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       10 (to L17)
               NOT_TAKEN
               LOAD_FAST_BORROW        10 (v)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_TRUE         3 (to L17)
               NOT_TAKEN
               JUMP_BACKWARD           51 (to L16)

235   L17:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              18 ('invalid_action_count_value:')
               LOAD_FAST_BORROW         9 (action)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L16)

232   L18:     END_FOR
               POP_ITER

237   L19:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (batch_plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              19 ('warnings')
               CALL                     1
               LOAD_GLOBAL             12 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L20)
               NOT_TAKEN

238            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              20 ('invalid_warnings_type')
               CALL                     1
               POP_TOP

240   L20:     LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17FBFEE0, file "app\services\memory\batch_rollout.py", line 226>:
 226           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                19 (to L5)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_GLOBAL              0 (_ALL_ACTIONS)
               CONTAINS_OP              1 (not in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           15 (to L2)
       L4:     LOAD_FAST_BORROW         1 (k)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           21 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\memory\batch_rollout.py", line 247>:
247           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('batch_plan')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, List[Dict[str, Any]]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object split_batch_actions at 0x0000018C17D8C5C0, file "app\services\memory\batch_rollout.py", line 247>:
 247            RESUME                   0

 257            LOAD_GLOBAL              0 (_ALL_ACTIONS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (a)
                SWAP                     2
        L1:     BUILD_MAP                0
                SWAP                     2
        L2:     FOR_ITER                 5 (to L3)
                STORE_FAST_LOAD_FAST    17 (a, a)
                BUILD_LIST               0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     STORE_FAST               2 (out)
                STORE_FAST               1 (a)

 258            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN

 259            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 260    L5:     LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('plans')
                CALL                     1
                STORE_FAST               3 (plans)

 261            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (plans)
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN

 262            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

 263    L6:     LOAD_FAST_BORROW         3 (plans)
                GET_ITER
        L7:     FOR_ITER                99 (to L11)
                STORE_FAST               4 (plan)

 264            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (plan)
                LOAD_GLOBAL              4 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN

 265            JUMP_BACKWARD           27 (to L7)

 266    L8:     LOAD_FAST_BORROW         4 (plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('recommended_action')
                CALL                     1
                STORE_FAST               5 (action)

 267            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (action)
                LOAD_GLOBAL             10 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           68 (to L7)
        L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 82 (action, out)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           76 (to L7)

 268   L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (out, action)
                BINARY_OP               26 ([])
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         4 (plan)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          101 (to L7)

 263   L11:     END_FOR
                POP_ITER

 269            LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 257            SWAP                     2
                STORE_FAST               1 (a)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\memory\batch_rollout.py", line 276>:
276           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('batch_plan')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object batch_plan_summary at 0x0000018C17E952F0, file "app\services\memory\batch_rollout.py", line 276>:
 276            RESUME                   0

 294            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        35 (to L5)
                NOT_TAKEN

 296            LOAD_CONST               1 ('batch_id')
                LOAD_CONST               2 ('')

 297            LOAD_CONST               3 ('total_brokerages')
                LOAD_SMALL_INT           0

 298            LOAD_CONST               4 ('action_counts')
                LOAD_GLOBAL              4 (_ALL_ACTIONS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (a)
                SWAP                     2
        L1:     BUILD_MAP                0
                SWAP                     2
        L2:     FOR_ITER                 5 (to L3)
                STORE_FAST_LOAD_FAST    17 (a, a)
                LOAD_SMALL_INT           0
                MAP_ADD                  2
                JUMP_BACKWARD            7 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     SWAP                     2
                STORE_FAST               1 (a)

 299            LOAD_CONST               5 ('applyable_count')
                LOAD_SMALL_INT           0

 300            LOAD_CONST               6 ('requires_approval_count')
                LOAD_SMALL_INT           0

 301            LOAD_CONST               7 ('warning_count')
                LOAD_SMALL_INT           0

 295            BUILD_MAP                6
                RETURN_VALUE

 304    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('plans')
                CALL                     1
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               8 ('plans')
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     BUILD_LIST               0
        L7:     STORE_FAST               2 (plans)

 305            LOAD_GLOBAL             11 (_normalise_action_counts + NULL)
                LOAD_FAST_BORROW         2 (plans)
                CALL                     1
                STORE_FAST               3 (counts)

 308            LOAD_FAST_BORROW         3 (counts)
                LOAD_GLOBAL             12 (rollout_mod)
                LOAD_ATTR               14 (ACTION_PROPOSE_ENABLE)
                BINARY_OP               26 ([])

 309            LOAD_FAST_BORROW         3 (counts)
                LOAD_GLOBAL             12 (rollout_mod)
                LOAD_ATTR               16 (ACTION_PROPOSE_DISABLE)
                BINARY_OP               26 ([])

 308            BINARY_OP                0 (+)

 307            STORE_FAST               4 (applyable)

 311            LOAD_GLOBAL             19 (sum + NULL)
                LOAD_CONST               9 (<code object <genexpr> at 0x0000018C17972550, file "app\services\memory\batch_rollout.py", line 311>)
                MAKE_FUNCTION

 312            LOAD_FAST_BORROW         2 (plans)
                GET_ITER

 311            CALL                     0
                CALL                     1
                STORE_FAST               5 (requires_approval)

 315            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              10 ('warnings')
                CALL                     1
                LOAD_GLOBAL              8 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
                NOT_TAKEN
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_CONST              10 ('warnings')
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_SMALL_INT           0
        L9:     STORE_FAST               6 (warning_count)

 318            LOAD_CONST               1 ('batch_id')
                LOAD_FAST_BORROW         0 (batch_plan)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('batch_id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')

 319   L10:     LOAD_CONST               3 ('total_brokerages')
                LOAD_GLOBAL             21 (len + NULL)
                LOAD_FAST_BORROW         2 (plans)
                CALL                     1

 320            LOAD_CONST               4 ('action_counts')
                LOAD_FAST_BORROW         3 (counts)

 321            LOAD_CONST               5 ('applyable_count')
                LOAD_FAST_BORROW         4 (applyable)

 322            LOAD_CONST               6 ('requires_approval_count')
                LOAD_FAST_BORROW         5 (requires_approval)

 323            LOAD_CONST               7 ('warning_count')
                LOAD_FAST_BORROW         6 (warning_count)

 317            BUILD_MAP                6
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 298            SWAP                     2
                STORE_FAST               1 (a)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L11 [7]

Disassembly of <code object <genexpr> at 0x0000018C17972550, file "app\services\memory\batch_rollout.py", line 311>:
 311           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 312   L2:     FOR_ITER                54 (to L7)
               STORE_FAST               1 (p)

 313           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (p)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL

 312   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)

 313   L4:     LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               0 ('requires_operator_approval')
               CALL                     1
               LOAD_CONST               1 (True)
               IS_OP                    0 (is)

 312   L5:     POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           50 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           56 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti
```
