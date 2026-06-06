# memory/rollout

- **pyc:** `app\services\memory\__pycache__\rollout.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/rollout.py`
- **co_filename (from bytecode):** `C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS144K — Operator-approved memory-rollout controller.

Pure planning layer that turns the PAS144J impact summary into a
*proposed* feature-flag action per brokerage. It does **not** apply
anything to Supabase, never imports the DB client, and never writes
to ``pas_brokerages``. PAS144K is planning-only.

Hard contract:
  * every helper is pure or planning-only — no I/O, no LLM, no
    Supabase, no embedding/vector usage, and no brokerage-row
    write path is reached. The module imports nothing from the DB
    layer, and module-surface tests assert that explicitly;
  * input dicts are read-only — never mutated. Output dicts are
    freshly constructed;
  * structural metrics only: the ``evidence`` field surfaces a closed
    whitelist of PAS144J summary fields and nothing else. Memory
    content, prompts, transcripts, evidence payloads, lineage,
    metadata, and lead utterances cannot enter the plan;
  * ``apply_rollout_plan`` NEVER writes regardless of the ``approve``
    flag in this phase. With ``approve=True`` it returns
    ``status="approved_but_not_applied"`` so the operator can see the
    "go" intent without the side effect.

Action taxonomy (closed set):
  * ``no_change``           — current config already matches the
                              recommendation;
  * ``propose_enable``      — flip the feature flag to True;
  * ``propose_disable``     — flip the feature flag to False;
  * ``propose_hold``        — keep the current config; sample too
                              small / neutral signal;
  * ``propose_investigate`` — booking rate underperforms; needs
                              human review before any change.

Decision matrix (from PAS144J ``rollout_recommendation`` × current
``memory_injection_enabled``):

    recommendation        enabled  →  action
    ----------------------------------------------------
    expand_cautiously     False     →  propose_enable
    expand_cautiously     True      →  no_change
    disable_for_now       True      →  propose_disable
    disable_for_now       False     →  no_change
    investigate           any       →  propose_investigate
    hold                  any       →  propose_hold
    <malformed input>     any       →  propose_hold + warning

Public surface (deliberately small):
  - ACTION_*                                       (constants)
  - VALID_ACTIONS                                  (frozenset)
  - build_rollout_plan(impact_report, current_config=None)  -> dict
  - decide_rollout_action(impact_summary, current_enabled)  -> dict
  - validate_rollout_plan(plan)                             -> list[str]
  - apply_rollout_plan(plan, *, approve=False)              -> dict
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_extract_brokerage_id`, `_extract_summary`, `_read_current_enabled`, `_safe_evidence`, `apply_rollout_plan`, `build_rollout_plan`, `decide_rollout_action`, `validate_rollout_plan`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS144K — Operator-approved memory-rollout controller.\n\nPure planning layer that turns the PAS144J impact summary into a\n*proposed* feature-flag action per brokerage. It does **not** apply\nanything to Supabase, never imports the DB client, and never writes\nto ``pas_brokerages``. PAS144K is planning-only.\n\nHard contract:\n  * every helper is pure or planning-only — no I/O, no LLM, no\n    Supabase, no embedding/vector usage, and no brokerage-row\n    write path is reached. The module imports nothing from the DB\n    layer, and module-surface tests assert that explicitly;\n  * input dicts are read-only — never mutated. Output dicts are\n    freshly constructed;\n  * structural metrics only: the ``evidence`` field surfaces a closed\n    whitelist of PAS144J summary fields and nothing else. Memory\n    content, prompts, transcripts, evidence payloads, lineage,\n    metadata, and lead utterances cannot enter the plan;\n  * ``apply_rollout_plan`` NEVER writes regardless of the ``approve``\n    flag in this phase. With ``approve=True`` it returns\n    ``status="approved_but_not_applied"`` so the operator can see the\n    "go" intent without the side effect.\n\nAction taxonomy (closed set):\n  * ``no_change``           — current config already matches the\n                              recommendation;\n  * ``propose_enable``      — flip the feature flag to True;\n  * ``propose_disable``     — flip the feature flag to False;\n  * ``propose_hold``        — keep the current config; sample too\n                              small / neutral signal;\n  * ``propose_investigate`` — booking rate underperforms; needs\n                              human review before any change.\n\nDecision matrix (from PAS144J ``rollout_recommendation`` × current\n``memory_injection_enabled``):\n\n    recommendation        enabled  →  action\n    ----------------------------------------------------\n    expand_cautiously     False     →  propose_enable\n    expand_cautiously     True      →  no_change\n    disable_for_now       True      →  propose_disable\n    disable_for_now       False     →  no_change\n    investigate           any       →  propose_investigate\n    hold                  any       →  propose_hold\n    <malformed input>     any       →  propose_hold + warning\n\nPublic surface (deliberately small):\n  - ACTION_*                                       (constants)\n  - VALID_ACTIONS                                  (frozenset)\n  - build_rollout_plan(impact_report, current_config=None)  -> dict\n  - decide_rollout_action(impact_summary, current_enabled)  -> dict\n  - validate_rollout_plan(plan)                             -> list[str]\n  - apply_rollout_plan(plan, *, approve=False)              -> dict\n'
- 'no_change'
- 'propose_enable'
- 'propose_disable'
- 'propose_hold'
- 'propose_investigate'
- 'memory_injection_enabled'
- 'approve'
- 'current_config'
- 'Any'
- 'return'
- 'bool'
- 'Strict-literal-True read of the feature flag.\n\nMatches PAS144F\'s resolver: only literal ``True`` (top-level or\nunder ``features.``) counts as enabled. ``"true"`` / ``1`` / ``"yes"``\nare explicitly NOT enabled. Non-dict input is False.\n'
- 'features'
- 'impact_summary'
- 'Dict[str, Any]'
- 'Project the PAS144J summary through a closed whitelist.'
- 'impact_report'
- 'str'
- 'Pull ``brokerage_id`` from a PAS144J impact report envelope.\n\nAccepts either the full report shape (``{"brokerage_id": ..., "summary": ...}``)\nor a bare summary dict. Returns ``""`` when missing or non-string.\n'
- 'brokerage_id'
- 'Optional[Dict[str, Any]]'
- 'Pull the impact summary out of an envelope.\n\nAccepts:\n  * the full PAS144J report (looks at ``report["summary"]``);\n  * a bare summary dict (``rollout_recommendation`` at the top\n    level — used by ``decide_rollout_action`` directly).\nReturns ``None`` when nothing usable is present.\n'
- 'summary'
- 'rollout_recommendation'
- 'current_enabled'
- 'Return a decision dict for one tenant.\n\nShape:\n    {\n        "recommended_action": <one of VALID_ACTIONS>,\n        "reason":             "<short structural string>",\n        "warnings":           [..],\n    }\n\nPure. Never raises. Malformed input → propose_hold + warning.\n'
- 'recommended_action'
- 'reason'
- 'malformed_or_missing_impact_summary'
- 'warnings'
- 'expand_cautiously'
- 'expand_cautiously_while_disabled'
- 'expand_cautiously_already_enabled'
- 'disable_for_now'
- 'disable_for_now_while_enabled'
- 'disable_for_now_already_disabled'
- 'investigate'
- 'investigate_recommended'
- 'hold_recommended'
- 'Compose a full rollout plan dict for one brokerage.\n\nInputs:\n  * ``impact_report``   — the PAS144J envelope (or a bare summary).\n  * ``current_config``  — the brokerage row (or any dict that\n                          carries ``memory_injection_enabled``);\n                          ``None`` is treated as "feature off".\n\nOutput plan shape:\n    {\n        "brokerage_id":               <str>,\n        "current_enabled":            <bool>,\n        "recommended_action":         <ACTION_*>,\n        "proposed_config_patch":      {} | {"features": {...}},\n        "reason":                     <str>,\n        "evidence":                   {<safe PAS144J fields>},\n        "requires_operator_approval": <bool>,\n        "safe_to_apply":              False,   # PAS144K never auto-applies\n        "warnings":                   [<str>, ...],\n    }\n\nPure. Never raises.\n'
- 'missing_brokerage_id'
- 'proposed_config_patch'
- 'evidence'
- 'requires_operator_approval'
- 'safe_to_apply'
- 'plan'
- 'List[str]'
- "Return a list of human-readable blockers for the given plan.\n\nAn empty list means the plan is structurally well-formed (it\ndoes NOT guarantee the recommendation is the right one — that\nis the operator's call).\n\nPure. Never raises.\n"
- 'plan_must_be_dict'
- 'invalid_recommended_action:'
- 'invalid_current_enabled'
- 'invalid_proposed_config_patch'
- 'invalid_proposed_config_patch_features'
- 'invalid_proposed_config_patch_flag'
- 'invalid_warnings'
- 'invalid_evidence'
- 'invalid_requires_operator_approval'
- 'invalid_safe_to_apply'
- 'Return the result of applying a rollout plan.\n\nPAS144K is **planning-only**. Regardless of the ``approve`` flag\nthis function NEVER:\n  * imports Supabase;\n  * invokes the brokerage-row write helper;\n  * writes to ``pas_brokerages`` or any other table;\n  * mutates the input plan dict.\n\nBehaviour:\n  * ``approve=False`` (default): ``status="dry_run"``.\n  * ``approve=True``           : ``status="approved_but_not_applied"``.\n  * structurally invalid plan  : ``status="invalid_plan"``,\n                                 populated ``errors`` list.\n\n``applied`` is always ``False`` in PAS144K.\n'
- 'status'
- 'invalid_plan'
- 'applied'
- 'errors'
- 'action'
- 'would_patch'
- 'phase'
- 'PAS144K_planning_only'
- 'dry_run'
- 'approved_but_not_applied'
- 'PAS144K is planning-only; flag writes are deferred to a later phase. The plan has been recorded as approved but no config change has been made.'
- 'note'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS144K — Operator-approved memory-rollout controller.\n\nPure planning layer that turns the PAS144J impact summary into a\n*proposed* feature-flag action per brokerage. It does **not** apply\nanything to Supabase, never imports the DB client, and never writes\nto ``pas_brokerages``. PAS144K is planning-only.\n\nHard contract:\n  * every helper is pure or planning-only — no I/O, no LLM, no\n    Supabase, no embedding/vector usage, and no brokerage-row\n    write path is reached. The module imports nothing from the DB\n    layer, and module-surface tests assert that explicitly;\n  * input dicts are read-only — never mutated. Output dicts are\n    freshly constructed;\n  * structural metrics only: the ``evidence`` field surfaces a closed\n    whitelist of PAS144J summary fields and nothing else. Memory\n    content, prompts, transcripts, evidence payloads, lineage,\n    metadata, and lead utterances cannot enter the plan;\n  * ``apply_rollout_plan`` NEVER writes regardless of the ``approve``\n    flag in this phase. With ``approve=True`` it returns\n    ``status="approved_but_not_applied"`` so the operator can see the\n    "go" intent without the side effect.\n\nAction taxonomy (closed set):\n  * ``no_change``           — current config already matches the\n                              recommendation;\n  * ``propose_enable``      — flip the feature flag to True;\n  * ``propose_disable``     — flip the feature flag to False;\n  * ``propose_hold``        — keep the current config; sample too\n                              small / neutral signal;\n  * ``propose_investigate`` — booking rate underperforms; needs\n                              human review before any change.\n\nDecision matrix (from PAS144J ``rollout_recommendation`` × current\n``memory_injection_enabled``):\n\n    recommendation        enabled  →  action\n    ----------------------------------------------------\n    expand_cautiously     False     →  propose_enable\n    expand_cautiously     True      →  no_change\n    disable_for_now       True      →  propose_disable\n    disable_for_now       False     →  no_change\n    investigate           any       →  propose_investigate\n    hold                  any       →  propose_hold\n    <malformed input>     any       →  propose_hold + warning\n\nPublic surface (deliberately small):\n  - ACTION_*                                       (constants)\n  - VALID_ACTIONS                                  (frozenset)\n  - build_rollout_plan(impact_report, current_config=None)  -> dict\n  - decide_rollout_action(impact_summary, current_enabled)  -> dict\n  - validate_rollout_plan(plan)                             -> list[str]\n  - apply_rollout_plan(plan, *, approve=False)              -> dict\n')
              STORE_NAME               0 (__doc__)

 57           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 59           LOAD_SMALL_INT           0
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

 66           LOAD_CONST               3 ('no_change')
              STORE_NAME               8 (ACTION_NO_CHANGE)

 67           LOAD_CONST               4 ('propose_enable')
              STORE_NAME               9 (ACTION_PROPOSE_ENABLE)

 68           LOAD_CONST               5 ('propose_disable')
              STORE_NAME              10 (ACTION_PROPOSE_DISABLE)

 69           LOAD_CONST               6 ('propose_hold')
              STORE_NAME              11 (ACTION_PROPOSE_HOLD)

 70           LOAD_CONST               7 ('propose_investigate')
              STORE_NAME              12 (ACTION_PROPOSE_INVESTIGATE)

 72           LOAD_NAME               13 (frozenset)
              PUSH_NULL

 73           LOAD_NAME                8 (ACTION_NO_CHANGE)

 74           LOAD_NAME                9 (ACTION_PROPOSE_ENABLE)

 75           LOAD_NAME               10 (ACTION_PROPOSE_DISABLE)

 76           LOAD_NAME               11 (ACTION_PROPOSE_HOLD)

 77           LOAD_NAME               12 (ACTION_PROPOSE_INVESTIGATE)

 72           BUILD_SET                5
              CALL                     1
              STORE_NAME              14 (VALID_ACTIONS)

 84           LOAD_NAME               13 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              28 (frozenset({'disable_for_now', 'investigate', 'hold', 'expand_cautiously'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              15 (_KNOWN_RECOMMENDATIONS)

 91           LOAD_CONST              29 (('total_calls', 'memory_succeeded_calls', 'non_memory_calls', 'booking_rate_with_memory', 'booking_rate_without_memory', 'callback_rate_with_memory', 'callback_rate_without_memory', 'provider_failure_rate_with_memory', 'provider_failure_rate_without_memory', 'lift_booking_rate', 'lift_callback_rate', 'health_status', 'rollout_recommendation'))
              STORE_NAME              16 (_SAFE_EVIDENCE_FIELDS)

109           LOAD_CONST               8 ('memory_injection_enabled')
              STORE_NAME              17 (_FLAG_KEY)

116           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _read_current_enabled at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_read_current_enabled)

133           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 133>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object _safe_evidence at 0x0000018C17F95E60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 133>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_safe_evidence)

144           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 144>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _extract_brokerage_id at 0x0000018C1804CB90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 144>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_extract_brokerage_id)

157           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 157>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _extract_summary at 0x0000018C17F96420, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 157>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_extract_summary)

180           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 180>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object decide_rollout_action at 0x0000018C17CC1CE0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 180>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (decide_rollout_action)

257           LOAD_CONST              30 ((None,))
              LOAD_CONST              20 (<code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 257>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object build_rollout_plan at 0x0000018C17CD0F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 257>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              23 (build_rollout_plan)

325           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 325>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object validate_rollout_plan at 0x0000018C17D8B490, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 325>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (validate_rollout_plan)

383           LOAD_CONST              24 ('approve')

386           LOAD_CONST              25 (False)

383           BUILD_MAP                1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 383>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object apply_rollout_plan at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 383>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              25 (apply_rollout_plan)
              LOAD_CONST              19 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('current_config')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_current_enabled at 0x0000018C180483B0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 116>:
116           RESUME                   0

123           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (current_config)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

124           LOAD_CONST               1 (False)
              RETURN_VALUE

125   L1:     LOAD_FAST_BORROW         0 (current_config)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_FLAG_KEY)
              CALL                     1
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

126           LOAD_CONST               2 (True)
              RETURN_VALUE

127   L2:     LOAD_FAST_BORROW         0 (current_config)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('features')
              CALL                     1
              STORE_FAST               1 (features)

128           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (features)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       28 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (features)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL              6 (_FLAG_KEY)
              CALL                     1
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

129           LOAD_CONST               2 (True)
              RETURN_VALUE

130   L3:     LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('impact_summary')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_evidence at 0x0000018C17F95E60, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 133>:
 133           RESUME                   0

 135           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (impact_summary)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 136           BUILD_MAP                0
               RETURN_VALUE

 139   L1:     LOAD_GLOBAL              4 (_SAFE_EVIDENCE_FIELDS)
               GET_ITER

 137           LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L2:     BUILD_MAP                0
               SWAP                     2

 139   L3:     FOR_ITER                28 (to L6)
               STORE_FAST               1 (k)

 140           LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, impact_summary)
               CONTAINS_OP              0 (in)

 138   L4:     POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, impact_summary)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L3)

 139   L6:     END_FOR
               POP_ITER

 137   L7:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L8:     SWAP                     2
               POP_TOP

 137           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L2 to L4 -> L8 [2]
  L5 to L7 -> L8 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 144>:
144           RESUME                   0
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

Disassembly of <code object _extract_brokerage_id at 0x0000018C1804CB90, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 144>:
144           RESUME                   0

150           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (impact_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L1)
              NOT_TAKEN

151           LOAD_FAST_BORROW         0 (impact_report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('brokerage_id')
              CALL                     1
              STORE_FAST               1 (bid)

152           LOAD_GLOBAL              1 (isinstance + NULL)
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

153           LOAD_FAST_BORROW         1 (bid)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

154   L1:     LOAD_CONST               2 ('')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 157>:
157           RESUME                   0
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
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _extract_summary at 0x0000018C17F96420, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 157>:
157           RESUME                   0

166           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (impact_report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

167           LOAD_CONST               1 (None)
              RETURN_VALUE

168   L1:     LOAD_FAST_BORROW         0 (impact_report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('summary')
              CALL                     1
              STORE_FAST               1 (summary)

169           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (summary)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

170           LOAD_FAST_BORROW         1 (summary)
              RETURN_VALUE

171   L2:     LOAD_CONST               3 ('rollout_recommendation')
              LOAD_FAST_BORROW         0 (impact_report)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

172           LOAD_FAST_BORROW         0 (impact_report)
              RETURN_VALUE

173   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 180>:
180           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('impact_summary')

181           LOAD_CONST               2 ('Any')

180           LOAD_CONST               3 ('current_enabled')

182           LOAD_CONST               2 ('Any')

180           LOAD_CONST               4 ('return')

183           LOAD_CONST               5 ('Dict[str, Any]')

180           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object decide_rollout_action at 0x0000018C17CC1CE0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 180>:
180           RESUME                   0

195           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (impact_summary)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        14 (to L1)
              NOT_TAKEN

197           LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL              4 (ACTION_PROPOSE_HOLD)

198           LOAD_CONST               2 ('reason')
              LOAD_CONST               3 ('malformed_or_missing_impact_summary')

199           LOAD_CONST               4 ('warnings')
              LOAD_CONST               3 ('malformed_or_missing_impact_summary')
              BUILD_LIST               1

196           BUILD_MAP                3
              RETURN_VALUE

202   L1:     LOAD_FAST_BORROW         0 (impact_summary)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               5 ('rollout_recommendation')
              CALL                     1
              STORE_FAST               2 (rec)

203           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (rec)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (rec)
              LOAD_GLOBAL             10 (_KNOWN_RECOMMENDATIONS)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       14 (to L3)
              NOT_TAKEN

205   L2:     LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL              4 (ACTION_PROPOSE_HOLD)

206           LOAD_CONST               2 ('reason')
              LOAD_CONST               3 ('malformed_or_missing_impact_summary')

207           LOAD_CONST               4 ('warnings')
              LOAD_CONST               3 ('malformed_or_missing_impact_summary')
              BUILD_LIST               1

204           BUILD_MAP                3
              RETURN_VALUE

210   L3:     LOAD_FAST_BORROW         1 (current_enabled)
              LOAD_CONST               6 (True)
              IS_OP                    0 (is)
              STORE_FAST               3 (enabled)

212           LOAD_FAST_BORROW         2 (rec)
              LOAD_CONST               7 ('expand_cautiously')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       33 (to L5)
              NOT_TAKEN

213           LOAD_FAST_BORROW         3 (enabled)
              TO_BOOL
              POP_JUMP_IF_TRUE        13 (to L4)
              NOT_TAKEN

215           LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL             12 (ACTION_PROPOSE_ENABLE)

216           LOAD_CONST               2 ('reason')
              LOAD_CONST               8 ('expand_cautiously_while_disabled')

217           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

214           BUILD_MAP                3
              RETURN_VALUE

220   L4:     LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL             14 (ACTION_NO_CHANGE)

221           LOAD_CONST               2 ('reason')
              LOAD_CONST               9 ('expand_cautiously_already_enabled')

222           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

219           BUILD_MAP                3
              RETURN_VALUE

225   L5:     LOAD_FAST_BORROW         2 (rec)
              LOAD_CONST              10 ('disable_for_now')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       33 (to L7)
              NOT_TAKEN

226           LOAD_FAST_BORROW         3 (enabled)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L6)
              NOT_TAKEN

228           LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL             16 (ACTION_PROPOSE_DISABLE)

229           LOAD_CONST               2 ('reason')
              LOAD_CONST              11 ('disable_for_now_while_enabled')

230           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

227           BUILD_MAP                3
              RETURN_VALUE

233   L6:     LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL             14 (ACTION_NO_CHANGE)

234           LOAD_CONST               2 ('reason')
              LOAD_CONST              12 ('disable_for_now_already_disabled')

235           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

232           BUILD_MAP                3
              RETURN_VALUE

238   L7:     LOAD_FAST_BORROW         2 (rec)
              LOAD_CONST              13 ('investigate')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       13 (to L8)
              NOT_TAKEN

240           LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL             18 (ACTION_PROPOSE_INVESTIGATE)

241           LOAD_CONST               2 ('reason')
              LOAD_CONST              14 ('investigate_recommended')

242           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

239           BUILD_MAP                3
              RETURN_VALUE

247   L8:     LOAD_CONST               1 ('recommended_action')
              LOAD_GLOBAL              4 (ACTION_PROPOSE_HOLD)

248           LOAD_CONST               2 ('reason')
              LOAD_CONST              15 ('hold_recommended')

249           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

246           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 257>:
257           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('impact_report')

258           LOAD_CONST               2 ('Any')

257           LOAD_CONST               3 ('current_config')

259           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

257           LOAD_CONST               5 ('return')

260           LOAD_CONST               6 ('Dict[str, Any]')

257           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object build_rollout_plan at 0x0000018C17CD0F70, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 257>:
257           RESUME                   0

284           LOAD_GLOBAL              1 (_extract_brokerage_id + NULL)
              LOAD_FAST_BORROW         0 (impact_report)
              CALL                     1
              STORE_FAST               2 (brokerage_id)

285           LOAD_GLOBAL              3 (_extract_summary + NULL)
              LOAD_FAST_BORROW         0 (impact_report)
              CALL                     1
              STORE_FAST               3 (summary)

286           LOAD_GLOBAL              5 (_read_current_enabled + NULL)
              LOAD_FAST_BORROW         1 (current_config)
              CALL                     1
              STORE_FAST               4 (current_enabled)

288           LOAD_GLOBAL              7 (decide_rollout_action + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (summary, current_enabled)
              CALL                     2
              STORE_FAST               5 (decision)

289           LOAD_FAST_BORROW         5 (decision)
              LOAD_CONST               1 ('recommended_action')
              BINARY_OP               26 ([])
              STORE_FAST               6 (action)

290           LOAD_FAST_BORROW         5 (decision)
              LOAD_CONST               2 ('reason')
              BINARY_OP               26 ([])
              STORE_FAST               7 (reason)

291           LOAD_GLOBAL              9 (list + NULL)
              LOAD_FAST_BORROW         5 (decision)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_CONST               3 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1
              STORE_FAST               8 (warnings)

294           BUILD_MAP                0
              STORE_FAST               9 (patch)

295           LOAD_FAST_BORROW         6 (action)
              LOAD_GLOBAL             12 (ACTION_PROPOSE_ENABLE)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       12 (to L2)
              NOT_TAKEN

296           LOAD_CONST               4 ('features')
              LOAD_GLOBAL             14 (_FLAG_KEY)
              LOAD_CONST               5 (True)
              BUILD_MAP                1
              BUILD_MAP                1
              STORE_FAST               9 (patch)
              JUMP_FORWARD            21 (to L3)

297   L2:     LOAD_FAST_BORROW         6 (action)
              LOAD_GLOBAL             16 (ACTION_PROPOSE_DISABLE)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       11 (to L3)
              NOT_TAKEN

298           LOAD_CONST               4 ('features')
              LOAD_GLOBAL             14 (_FLAG_KEY)
              LOAD_CONST               6 (False)
              BUILD_MAP                1
              BUILD_MAP                1
              STORE_FAST               9 (patch)

300   L3:     LOAD_FAST_BORROW         2 (brokerage_id)
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L4)
              NOT_TAKEN

301           LOAD_FAST_BORROW         8 (warnings)
              LOAD_ATTR               19 (append + NULL|self)
              LOAD_CONST               7 ('missing_brokerage_id')
              CALL                     1
              POP_TOP

304   L4:     LOAD_CONST               8 ('brokerage_id')
              LOAD_FAST_BORROW         2 (brokerage_id)

305           LOAD_CONST               9 ('current_enabled')
              LOAD_GLOBAL             21 (bool + NULL)
              LOAD_FAST_BORROW         4 (current_enabled)
              CALL                     1

306           LOAD_CONST               1 ('recommended_action')
              LOAD_FAST_BORROW         6 (action)

307           LOAD_CONST              10 ('proposed_config_patch')
              LOAD_FAST_BORROW         9 (patch)

308           LOAD_CONST               2 ('reason')
              LOAD_FAST_BORROW         7 (reason)

309           LOAD_CONST              11 ('evidence')
              LOAD_GLOBAL             23 (_safe_evidence + NULL)
              LOAD_FAST_BORROW         3 (summary)
              CALL                     1

313           LOAD_CONST              12 ('requires_operator_approval')
              LOAD_FAST_BORROW         6 (action)
              LOAD_GLOBAL             24 (ACTION_NO_CHANGE)
              COMPARE_OP             103 (!=)

316           LOAD_CONST              13 ('safe_to_apply')
              LOAD_CONST               6 (False)

317           LOAD_CONST               3 ('warnings')
              LOAD_FAST_BORROW         8 (warnings)

303           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 325>:
325           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object validate_rollout_plan at 0x0000018C17D8B490, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 325>:
325            RESUME                   0

334            BUILD_LIST               0
               STORE_FAST               1 (errors)

336            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L1)
               NOT_TAKEN

337            LOAD_CONST               1 ('plan_must_be_dict')
               BUILD_LIST               1
               RETURN_VALUE

339    L1:     LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               2 ('brokerage_id')
               CALL                     1
               STORE_FAST               2 (bid)

340            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (bid)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (bid)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L3)
               NOT_TAKEN

341    L2:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               3 ('missing_brokerage_id')
               CALL                     1
               POP_TOP

343    L3:     LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               4 ('recommended_action')
               CALL                     1
               STORE_FAST               3 (action)

344            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (action)
               LOAD_GLOBAL              6 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       12 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         3 (action)
               LOAD_GLOBAL             12 (VALID_ACTIONS)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       22 (to L5)
               NOT_TAKEN

345    L4:     LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               5 ('invalid_recommended_action:')
               LOAD_FAST_BORROW         3 (action)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

347    L5:     LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               6 ('current_enabled')
               CALL                     1
               STORE_FAST               4 (ce)

348            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (ce)
               LOAD_GLOBAL             14 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L6)
               NOT_TAKEN

349            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               7 ('invalid_current_enabled')
               CALL                     1
               POP_TOP

351    L6:     LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               8 ('proposed_config_patch')
               CALL                     1
               STORE_FAST               5 (patch)

352            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         5 (patch)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L7)
               NOT_TAKEN

353            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST               9 ('invalid_proposed_config_patch')
               CALL                     1
               POP_TOP
               JUMP_FORWARD           125 (to L9)

357    L7:     LOAD_FAST_BORROW         5 (patch)
               TO_BOOL
               POP_JUMP_IF_FALSE      118 (to L9)
               NOT_TAKEN

358            LOAD_FAST_BORROW         5 (patch)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              10 ('features')
               CALL                     1
               STORE_FAST               6 (features)

359            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (features)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L8)
               NOT_TAKEN

360            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              11 ('invalid_proposed_config_patch_features')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            60 (to L9)

362    L8:     LOAD_FAST_BORROW         6 (features)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_GLOBAL             16 (_FLAG_KEY)
               CALL                     1
               STORE_FAST               7 (flag)

363            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         7 (flag)
               LOAD_GLOBAL             14 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L9)
               NOT_TAKEN

364            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              12 ('invalid_proposed_config_patch_flag')
               CALL                     1
               POP_TOP

366    L9:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              13 ('warnings')
               CALL                     1
               LOAD_GLOBAL             18 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L10)
               NOT_TAKEN

367            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              14 ('invalid_warnings')
               CALL                     1
               POP_TOP

368   L10:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              15 ('evidence')
               CALL                     1
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L11)
               NOT_TAKEN

369            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              16 ('invalid_evidence')
               CALL                     1
               POP_TOP

370   L11:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              17 ('requires_operator_approval')
               CALL                     1
               LOAD_GLOBAL             14 (bool)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L12)
               NOT_TAKEN

371            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              18 ('invalid_requires_operator_approval')
               CALL                     1
               POP_TOP

372   L12:     LOAD_FAST_BORROW         0 (plan)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST              19 ('safe_to_apply')
               CALL                     1
               LOAD_CONST              20 (False)
               IS_OP                    1 (is not)
               POP_JUMP_IF_FALSE       18 (to L13)
               NOT_TAKEN

374            LOAD_FAST_BORROW         1 (errors)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_CONST              21 ('invalid_safe_to_apply')
               CALL                     1
               POP_TOP

376   L13:     LOAD_FAST_BORROW         1 (errors)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 383>:
383           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plan')

384           LOAD_CONST               2 ('Dict[str, Any]')

383           LOAD_CONST               3 ('approve')

386           LOAD_CONST               4 ('bool')

383           LOAD_CONST               5 ('return')

387           LOAD_CONST               2 ('Dict[str, Any]')

383           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object apply_rollout_plan at 0x0000018C1794ED80, file "C:\Users\hp\Downloads\pas-engine\pas-engine\app\services\memory\rollout.py", line 383>:
383           RESUME                   0

405           LOAD_GLOBAL              1 (validate_rollout_plan + NULL)
              LOAD_FAST_BORROW         0 (plan)
              CALL                     1
              STORE_FAST               2 (errors)

406           LOAD_FAST_BORROW         2 (errors)
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN

408           LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('invalid_plan')

409           LOAD_CONST               3 ('applied')
              LOAD_CONST               4 (False)

410           LOAD_CONST               5 ('errors')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         2 (errors)
              CALL                     1

407           BUILD_MAP                3
              RETURN_VALUE

414   L1:     LOAD_CONST               3 ('applied')
              LOAD_CONST               4 (False)

415           LOAD_CONST               6 ('brokerage_id')
              LOAD_FAST_BORROW         0 (plan)
              LOAD_CONST               6 ('brokerage_id')
              BINARY_OP               26 ([])

416           LOAD_CONST               7 ('action')
              LOAD_FAST_BORROW         0 (plan)
              LOAD_CONST               8 ('recommended_action')
              BINARY_OP               26 ([])

417           LOAD_CONST               9 ('would_patch')
              LOAD_GLOBAL              5 (dict + NULL)
              LOAD_FAST_BORROW         0 (plan)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST              10 ('proposed_config_patch')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L2:     CALL                     1

418           LOAD_CONST              11 ('phase')
              LOAD_CONST              12 ('PAS144K_planning_only')

413           BUILD_MAP                5
              STORE_FAST               3 (out)

421           LOAD_FAST_BORROW         1 (approve)
              TO_BOOL
              POP_JUMP_IF_TRUE         8 (to L3)
              NOT_TAKEN

422           LOAD_CONST              13 ('dry_run')
              LOAD_FAST_BORROW         3 (out)
              LOAD_CONST               1 ('status')
              STORE_SUBSCR

423           LOAD_FAST_BORROW         3 (out)
              RETURN_VALUE

425   L3:     LOAD_CONST              14 ('approved_but_not_applied')
              LOAD_FAST_BORROW         3 (out)
              LOAD_CONST               1 ('status')
              STORE_SUBSCR

427           LOAD_CONST              15 ('PAS144K is planning-only; flag writes are deferred to a later phase. The plan has been recorded as approved but no config change has been made.')

426           LOAD_FAST_BORROW         3 (out)
              LOAD_CONST              16 ('note')
              STORE_SUBSCR

431           LOAD_FAST_BORROW         3 (out)
              RETURN_VALUE
```
