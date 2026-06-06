# scripts_readiness/integrity_check

- **pyc:** `scripts\__pycache__\integrity_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/integrity_check.py`
- **co_filename (from bytecode):** `scripts\integrity_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143E — Offline integrity checker.

Validates that the deterministic substrate behaves as advertised by
running canonical fixtures through the live code paths (replay,
optimization, simulation) and asserting structural invariants.

No DB access. No external APIs. Uses small synthetic fixtures so the
check is fast and reproducible on any developer laptop.

Categories:
  - replay reconstruction consistency  (event stream → expected stages)
  - event normalization consistency    (top-level + payload-fallback parity)
  - missing lifecycle stage detection
  - impossible outcome detection       (e.g. booked + dropping state)
  - invalid strategy ID detection
  - invalid personality ID detection
  - malformed event row detection
  - duplicate event_id detection
  - replay score range validity        (must be in [0, 100])
  - optimization ranking validity      (sorted, ranks consecutive)
  - negative metric detection
  - matrix shape consistency

Usage:
  python scripts/integrity_check.py
  python scripts/integrity_check.py --strict   # exit 1 on any failure
  python scripts/integrity_check.py --json

Exit codes:
    0  — all checks passed
    1  — at least one failure (always with --strict; otherwise unless 0
         hard failures)
    2  — bad CLI arguments
```

## Imports

`BEHAVIOR_STATES`, `List`, `Optional`, `PERSONALITIES`, `SCENARIOS`, `STRATEGIES`, `__future__`, `annotations`, `app.services.optimization.metrics`, `app.services.optimization.ranking`, `app.services.optimization.strategies`, `app.services.replay.evaluator`, `app.services.replay.event_reader`, `app.services.replay.reconstruction`, `app.services.simulation.behavior`, `app.services.simulation.scenarios`, `argparse`, `asdict`, `compute_matrix_metrics`, `dataclass`, `dataclasses`, `datetime`, `evaluate_reconstruction`, `field`, `get_contract_value`, `json`, `normalize_event`, `os`, `rank_strategies`, `reconstruct_call`, `sys`, `timezone`, `typing`

## Classes

`CheckResult`, `IntegrityReport`

## Functions / methods

`__annotate__`, `_canonical_buyer_event_stream`, `_norm_row`, `check_behavior_state_in_known_set`, `check_duplicate_event_id_detection`, `check_evaluator_empty_input`, `check_evaluator_score_range`, `check_full_buyer_lifecycle_replay`, `check_get_contract_value_returns_none_for_garbage`, `check_malformed_row_does_not_crash`, `check_missing_lifecycle_stage_detection`, `check_no_negative_metric_values`, `check_normalization_top_level_vs_fallback`, `check_outcome_state_consistency`, `check_personality_registry_ids_unique_and_known`, `check_ranking_is_sorted_and_ranks_consecutive`, `check_scenario_personalities_resolve`, `check_strategy_registry_ids_unique_and_known`, `main`, `run_integrity_checks`

## Env-key candidates

`BUDGET`, `FAIL`, `GREETING`, `INTENT`, `PASS`, `TIMELINE`

## String constants (redacted where noted)

- '\nPAS143E — Offline integrity checker.\n\nValidates that the deterministic substrate behaves as advertised by\nrunning canonical fixtures through the live code paths (replay,\noptimization, simulation) and asserting structural invariants.\n\nNo DB access. No external APIs. Uses small synthetic fixtures so the\ncheck is fast and reproducible on any developer laptop.\n\nCategories:\n  - replay reconstruction consistency  (event stream → expected stages)\n  - event normalization consistency    (top-level + payload-fallback parity)\n  - missing lifecycle stage detection\n  - impossible outcome detection       (e.g. booked + dropping state)\n  - invalid strategy ID detection\n  - invalid personality ID detection\n  - malformed event row detection\n  - duplicate event_id detection\n  - replay score range validity        (must be in [0, 100])\n  - optimization ranking validity      (sorted, ranks consecutive)\n  - negative metric detection\n  - matrix shape consistency\n\nUsage:\n  python scripts/integrity_check.py\n  python scripts/integrity_check.py --strict   # exit 1 on any failure\n  python scripts/integrity_check.py --json\n\nExit codes:\n    0  — all checks passed\n    1  — at least one failure (always with --strict; otherwise unless 0\n         hard failures)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'CheckResult'
- 'IntegrityReport'
- 'str'
- 'name'
- 'bool'
- 'passed'
- 'detail'
- 'category'
- 'return'
- 'dict'
- 'generated_at'
- 'List[CheckResult]'
- 'results'
- 'total'
- 'failed'
- 'None'
- 'tool'
- 'pas143e.integrity_check'
- 'counts'
- 'Build a minimal pas_events-shaped row through normalize_event.'
- 'event_type'
- 'created_at'
- 'brokerage_id'
- 'brk-test'
- 'call_id'
- 'SIM-INT-1'
- 'lead_id'
- 'actor'
- 'workflow_stage'
- 'input_text'
- 'output_text'
- 'extracted_field'
- 'extracted_value'
- 'confidence_score'
- 'outcome_state'
- 'source'
- 'simulated'
- 'state'
- 'payload'
- 'list'
- 'call.started'
- 'system'
- 'lead_received'
- 'lead.uttered'
- 'lead'
- 'GREETING'
- 'speaker'
- 'pas.uttered'
- 'pas'
- 'hello'
- 'lead.extracted'
- 'INTENT'
- 'intent'
- 'buying'
- 'BUDGET'
- 'budget'
- '$400k'
- 'TIMELINE'
- 'timeline'
- '3 months'
- 'booking.confirmed'
- 'booking_confirmed'
- 'booked'
- 'call.ended'
- 'completed'
- 'outcome'
- 'report'
- "The same logical event, expressed as v8 top-level columns or via\npayload['contract'] fallback, must normalize to the same key data."
- 'voice'
- 'raw_text'
- 'field'
- 'value'
- 'contract'
- 'normalization: v8 top-level == payload[contract] fallback'
- 'diffs='
- 'normalization'
- 'The contract value reader must never raise on weird input.'
- 'anything'
- 'normalization: get_contract_value handles garbage'
- 'final_outcome'
- 'missing_lifecycle_steps'
- 'turns'
- 'extracted_fields'
- 'replay: full buyer lifecycle reconstructs cleanly'
- 'missing='
- ' outcome='
- 'replay'
- 'replay_score'
- 'evaluator: replay_score in [0, 100]'
- 'score='
- 'evaluator'
- 'Empty / garbage input must not produce out-of-range scores.'
- 'is_replayable'
- 'evaluator: empty/None input bounded + non-replayable'
- "Drop the call.ended event and confirm 'completed' shows missing."
- 'replay: missing lifecycle stage surfaces'
- 'missing_lifecycle_steps='
- 'garbage'
- 'events_count'
- 'replay: malformed rows handled without raising'
- 'robustness'
- 'Walk a fixture stream and verify duplicate-id detection logic\nworks. (event_id is None in synthetic fixtures, so this also tests\nthat absent ids are *not* mistakenly flagged.)'
- 'abc'
- 'event_id'
- 'events: duplicate event_id detection works'
- 'duplicates='
- 'events'
- 'optimization: strategy ids unique + non-empty'
- 'optimization'
- 'behaviour: personality ids unique + non-empty'
- 'behaviour'
- 'Every scenario.personality_id must point to a known personality\nOR be None — no dangling references.'
- 'scenarios: personality_id references resolve'
- 'unknown personality refs: '
- 'scenarios'
- 'by_strategy'
- 'pass_rate'
- 'avg_replay_score'
- 'avg_turns'
- 'errors'
- 'outcome_counts'
- 'booked_rate'
- 'callback_rate'
- 'not_booked_rate'
- 'transferred_rate'
- 'effective'
- 'trust_avg'
- 'frustration_avg'
- 'divergence_count'
- 'not_booked'
- 'rank'
- 'ranking: scores monotone + ranks consecutive'
- 'scores='
- 'score'
- ' ranks='
- 'Compute_matrix_metrics on a 1-cell matrix must produce sane\nnon-negative aggregates.'
- 'matrix_id'
- 'MTX-T'
- 'total_runs'
- 'scenarios_count'
- 'strategies_count'
- 'demo'
- 'started_at'
- 'now'
- 'duration_ms'
- 'scenario_id'
- 'scenario_title'
- 'scenario_category'
- 'core'
- 'scenario_tags'
- 'call_sid'
- 'SIM-1'
- 'expected_outcome'
- 'actual_outcome'
- 'transcript'
- 'reconstruction'
- 'evaluation'
- 'missing_steps'
- 'error'
- 'strategy_id'
- 'strategy_name'
- 'strategy_category'
- 'greeting'
- 'strategy_overrides'
- 'strategy_effective'
- 'cell_error'
- 'personality_id'
- 'motivated'
- 'personality_name'
- 'Motivated'
- 'final_behavior_state'
- 'engaged'
- 'trust_score'
- 'frustration_score'
- 'divergence_triggered'
- 'divergence_actions'
- 'metrics: no negative aggregate values'
- 'negative keys: '
- 'Every BEHAVIOR_STATES value must be a non-empty string.'
- 'behaviour: BEHAVIOR_STATES are valid strings'
- 'An impossible-outcome guard: a row that says outcome=booked but\nfinal_behavior_state=hostile + dropping should never appear in real\ndata. Here we only assert the *checker* would catch it.'
- 'dropping'
- 'events: impossible-outcome detection logic operates'
- 'argv'
- 'Optional[list]'
- 'int'
- 'integrity_check'
- 'PAS143E — offline integrity checker for the substrate.'
- '--strict'
- 'store_true'
- 'Exit non-zero on any failed check.'
- '--json'
- 'Emit the report as JSON.'
- 'integrity_check_report.json'
- 'WARNING: could not write report: '
- 'PAS143E — INTEGRITY CHECK'
- ' checks passed'
- 'PASS'
- 'FAIL'
- '  ['
- ' — '
- '  report: '
- '========================================================================'
- '------------------------------------------------------------------------'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143E — Offline integrity checker.\n\nValidates that the deterministic substrate behaves as advertised by\nrunning canonical fixtures through the live code paths (replay,\noptimization, simulation) and asserting structural invariants.\n\nNo DB access. No external APIs. Uses small synthetic fixtures so the\ncheck is fast and reproducible on any developer laptop.\n\nCategories:\n  - replay reconstruction consistency  (event stream → expected stages)\n  - event normalization consistency    (top-level + payload-fallback parity)\n  - missing lifecycle stage detection\n  - impossible outcome detection       (e.g. booked + dropping state)\n  - invalid strategy ID detection\n  - invalid personality ID detection\n  - malformed event row detection\n  - duplicate event_id detection\n  - replay score range validity        (must be in [0, 100])\n  - optimization ranking validity      (sorted, ranks consecutive)\n  - negative metric detection\n  - matrix shape consistency\n\nUsage:\n  python scripts/integrity_check.py\n  python scripts/integrity_check.py --strict   # exit 1 on any failure\n  python scripts/integrity_check.py --json\n\nExit codes:\n    0  — all checks passed\n    1  — at least one failure (always with --strict; otherwise unless 0\n         hard failures)\n    2  — bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  37            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  39            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  40            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  41            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  42            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  43            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('asdict', 'dataclass', 'field'))
                IMPORT_NAME              7 (dataclasses)
                IMPORT_FROM              8 (asdict)
                STORE_NAME               8 (asdict)
                IMPORT_FROM              9 (dataclass)
                STORE_NAME               9 (dataclass)
                IMPORT_FROM             10 (field)
                STORE_NAME              10 (field)
                POP_TOP

  44            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('datetime', 'timezone'))
                IMPORT_NAME             11 (datetime)
                IMPORT_FROM             11 (datetime)
                STORE_NAME              11 (datetime)
                IMPORT_FROM             12 (timezone)
                STORE_NAME              12 (timezone)
                POP_TOP

  45            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('List', 'Optional'))
                IMPORT_NAME             13 (typing)
                IMPORT_FROM             14 (List)
                STORE_NAME              14 (List)
                IMPORT_FROM             15 (Optional)
                STORE_NAME              15 (Optional)
                POP_TOP

  49            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  50            NOP

  51    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  49    L4:     END_FOR
                POP_ITER

  56            LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               45 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               47 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               49 (dirname + NULL|self)
                LOAD_NAME               25 (__file__)
                CALL                     1
                LOAD_CONST               8 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              26 (_REPO_ROOT)

  57            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  58            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  63    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('normalize_event', 'get_contract_value'))
                IMPORT_NAME             28 (app.services.replay.event_reader)
                IMPORT_FROM             29 (normalize_event)
                STORE_NAME              29 (normalize_event)
                IMPORT_FROM             30 (get_contract_value)
                STORE_NAME              30 (get_contract_value)
                POP_TOP

  64            LOAD_SMALL_INT           0
                LOAD_CONST              10 (('reconstruct_call',))
                IMPORT_NAME             31 (app.services.replay.reconstruction)
                IMPORT_FROM             32 (reconstruct_call)
                STORE_NAME              32 (reconstruct_call)
                POP_TOP

  65            LOAD_SMALL_INT           0
                LOAD_CONST              11 (('evaluate_reconstruction',))
                IMPORT_NAME             33 (app.services.replay.evaluator)
                IMPORT_FROM             34 (evaluate_reconstruction)
                STORE_NAME              34 (evaluate_reconstruction)
                POP_TOP

  66            LOAD_SMALL_INT           0
                LOAD_CONST              12 (('compute_matrix_metrics',))
                IMPORT_NAME             35 (app.services.optimization.metrics)
                IMPORT_FROM             36 (compute_matrix_metrics)
                STORE_NAME              36 (compute_matrix_metrics)
                POP_TOP

  67            LOAD_SMALL_INT           0
                LOAD_CONST              13 (('rank_strategies',))
                IMPORT_NAME             37 (app.services.optimization.ranking)
                IMPORT_FROM             38 (rank_strategies)
                STORE_NAME              38 (rank_strategies)
                POP_TOP

  68            LOAD_SMALL_INT           0
                LOAD_CONST              14 (('STRATEGIES',))
                IMPORT_NAME             39 (app.services.optimization.strategies)
                IMPORT_FROM             40 (STRATEGIES)
                STORE_NAME              40 (STRATEGIES)
                POP_TOP

  69            LOAD_SMALL_INT           0
                LOAD_CONST              15 (('SCENARIOS',))
                IMPORT_NAME             41 (app.services.simulation.scenarios)
                IMPORT_FROM             42 (SCENARIOS)
                STORE_NAME              42 (SCENARIOS)
                POP_TOP

  70            LOAD_SMALL_INT           0
                LOAD_CONST              16 (('PERSONALITIES', 'BEHAVIOR_STATES'))
                IMPORT_NAME             43 (app.services.simulation.behavior)
                IMPORT_FROM             44 (PERSONALITIES)
                STORE_NAME              44 (PERSONALITIES)
                IMPORT_FROM             45 (BEHAVIOR_STATES)
                STORE_NAME              45 (BEHAVIOR_STATES)
                POP_TOP

  79            LOAD_NAME                9 (dataclass)

  80            LOAD_BUILD_CLASS
                PUSH_NULL
                LOAD_CONST              17 (<code object CheckResult at 0x0000018C1802C620, file "scripts\integrity_check.py", line 79>)
                MAKE_FUNCTION
                LOAD_CONST              18 ('CheckResult')
                CALL                     2

  79            CALL                     0

  80            STORE_NAME              46 (CheckResult)

  90            LOAD_NAME                9 (dataclass)

  91            LOAD_BUILD_CLASS
                PUSH_NULL
                LOAD_CONST              19 (<code object IntegrityReport at 0x0000018C17972550, file "scripts\integrity_check.py", line 90>)
                MAKE_FUNCTION
                LOAD_CONST              20 ('IntegrityReport')
                CALL                     2

  90            CALL                     0

  91            STORE_NAME              47 (IntegrityReport)

 122            LOAD_CONST              59 (('2026-01-01T00:00:00+00:00',))
                LOAD_CONST              21 (<code object _norm_row at 0x0000018C1800AA60, file "scripts\integrity_check.py", line 122>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              48 (_norm_row)

 146            LOAD_CONST              60 (('SIM-INT-1',))
                LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\integrity_check.py", line 146>)
                MAKE_FUNCTION
                LOAD_CONST              23 (<code object _canonical_buyer_event_stream at 0x0000018C179A7290, file "scripts\integrity_check.py", line 146>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              49 (_canonical_buyer_event_stream)

 178            LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\integrity_check.py", line 178>)
                MAKE_FUNCTION
                LOAD_CONST              25 (<code object check_normalization_top_level_vs_fallback at 0x0000018C17F63C30, file "scripts\integrity_check.py", line 178>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              50 (check_normalization_top_level_vs_fallback)

 212            LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\integrity_check.py", line 212>)
                MAKE_FUNCTION
                LOAD_CONST              27 (<code object check_get_contract_value_returns_none_for_garbage at 0x0000018C17FF13B0, file "scripts\integrity_check.py", line 212>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              51 (check_get_contract_value_returns_none_for_garbage)

 225            LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\integrity_check.py", line 225>)
                MAKE_FUNCTION
                LOAD_CONST              29 (<code object check_full_buyer_lifecycle_replay at 0x0000018C17F01250, file "scripts\integrity_check.py", line 225>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              52 (check_full_buyer_lifecycle_replay)

 242            LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\integrity_check.py", line 242>)
                MAKE_FUNCTION
                LOAD_CONST              31 (<code object check_evaluator_score_range at 0x0000018C179C3A50, file "scripts\integrity_check.py", line 242>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              53 (check_evaluator_score_range)

 255            LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\integrity_check.py", line 255>)
                MAKE_FUNCTION
                LOAD_CONST              33 (<code object check_evaluator_empty_input at 0x0000018C17EA4B40, file "scripts\integrity_check.py", line 255>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              54 (check_evaluator_empty_input)

 271            LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\integrity_check.py", line 271>)
                MAKE_FUNCTION
                LOAD_CONST              35 (<code object check_missing_lifecycle_stage_detection at 0x0000018C1804CD30, file "scripts\integrity_check.py", line 271>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              55 (check_missing_lifecycle_stage_detection)

 285            LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\integrity_check.py", line 285>)
                MAKE_FUNCTION
                LOAD_CONST              37 (<code object check_malformed_row_does_not_crash at 0x0000018C17FF10B0, file "scripts\integrity_check.py", line 285>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              56 (check_malformed_row_does_not_crash)

 294            LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\integrity_check.py", line 294>)
                MAKE_FUNCTION
                LOAD_CONST              39 (<code object check_duplicate_event_id_detection at 0x0000018C1801C9E0, file "scripts\integrity_check.py", line 294>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              57 (check_duplicate_event_id_detection)

 318            LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\integrity_check.py", line 318>)
                MAKE_FUNCTION
                LOAD_CONST              41 (<code object check_strategy_registry_ids_unique_and_known at 0x0000018C17E589A0, file "scripts\integrity_check.py", line 318>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              58 (check_strategy_registry_ids_unique_and_known)

 329            LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\integrity_check.py", line 329>)
                MAKE_FUNCTION
                LOAD_CONST              43 (<code object check_personality_registry_ids_unique_and_known at 0x0000018C17E58770, file "scripts\integrity_check.py", line 329>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              59 (check_personality_registry_ids_unique_and_known)

 340            LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\integrity_check.py", line 340>)
                MAKE_FUNCTION
                LOAD_CONST              45 (<code object check_scenario_personalities_resolve at 0x0000018C17FEDA30, file "scripts\integrity_check.py", line 340>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              60 (check_scenario_personalities_resolve)

 354            LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\integrity_check.py", line 354>)
                MAKE_FUNCTION
                LOAD_CONST              47 (<code object check_ranking_is_sorted_and_ranks_consecutive at 0x0000018C17D7CA80, file "scripts\integrity_check.py", line 354>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              61 (check_ranking_is_sorted_and_ranks_consecutive)

 394            LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\integrity_check.py", line 394>)
                MAKE_FUNCTION
                LOAD_CONST              49 (<code object check_no_negative_metric_values at 0x0000018C17CD4970, file "scripts\integrity_check.py", line 394>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              62 (check_no_negative_metric_values)

 425            LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\integrity_check.py", line 425>)
                MAKE_FUNCTION
                LOAD_CONST              51 (<code object check_behavior_state_in_known_set at 0x0000018C17FF0C30, file "scripts\integrity_check.py", line 425>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              63 (check_behavior_state_in_known_set)

 434            LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\integrity_check.py", line 434>)
                MAKE_FUNCTION
                LOAD_CONST              53 (<code object check_outcome_state_consistency at 0x0000018C17FE13E0, file "scripts\integrity_check.py", line 434>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              64 (check_outcome_state_consistency)

 454            LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\integrity_check.py", line 454>)
                MAKE_FUNCTION
                LOAD_CONST              55 (<code object run_integrity_checks at 0x0000018C17F63990, file "scripts\integrity_check.py", line 454>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              65 (run_integrity_checks)

 476            LOAD_CONST              61 ((None,))
                LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\integrity_check.py", line 476>)
                MAKE_FUNCTION
                LOAD_CONST              57 (<code object main at 0x0000018C17D50FF0, file "scripts\integrity_check.py", line 476>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              66 (main)

 519            LOAD_NAME               67 (__name__)
                LOAD_CONST              58 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 520            LOAD_NAME               68 (SystemExit)
                PUSH_NULL
                LOAD_NAME               66 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 519    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  52            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  53    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          381 (to L1)

  52    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object CheckResult at 0x0000018C1802C620, file "scripts\integrity_check.py", line 79>:
 79           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('CheckResult')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          79
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 81           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               2 ('name')
              STORE_SUBSCR

 82           LOAD_CONST               3 ('bool')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               4 ('passed')
              STORE_SUBSCR

 83           LOAD_CONST               5 ('')
              STORE_NAME               5 (detail)
              LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               6 ('detail')
              STORE_SUBSCR

 84           LOAD_CONST               5 ('')
              STORE_NAME               6 (category)
              LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               7 ('category')
              STORE_SUBSCR

 86           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\integrity_check.py", line 86>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object to_dict at 0x0000018C17FA34B0, file "scripts\integrity_check.py", line 86>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME               7 (to_dict)
              LOAD_CONST              10 (())
              STORE_NAME               8 (__static_attributes__)
              LOAD_CONST              11 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\integrity_check.py", line 86>:
 86           RESUME                   0
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

Disassembly of <code object to_dict at 0x0000018C17FA34B0, file "scripts\integrity_check.py", line 86>:
 86           RESUME                   0

 87           LOAD_GLOBAL              1 (asdict + NULL)
              LOAD_FAST_BORROW         0 (self)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object IntegrityReport at 0x0000018C17972550, file "scripts\integrity_check.py", line 90>:
 90           RESUME                   0
              LOAD_NAME                0 (__name__)
              STORE_NAME               1 (__module__)
              LOAD_CONST               0 ('IntegrityReport')
              STORE_NAME               2 (__qualname__)
              LOAD_SMALL_INT          90
              STORE_NAME               3 (__firstlineno__)
              SETUP_ANNOTATIONS

 92           LOAD_CONST               1 ('str')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               2 ('generated_at')
              STORE_SUBSCR

 93           LOAD_NAME                5 (field)
              PUSH_NULL
              LOAD_NAME                6 (list)
              LOAD_CONST               3 (('default_factory',))
              CALL_KW                  1
              STORE_NAME               7 (results)
              LOAD_CONST               4 ('List[CheckResult]')
              LOAD_NAME                4 (__annotations__)
              LOAD_CONST               5 ('results')
              STORE_SUBSCR

 95           LOAD_NAME                8 (property)

 96           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\integrity_check.py", line 96>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object passed at 0x0000018C17F95E60, file "scripts\integrity_check.py", line 95>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)

 95           CALL                     0

 96           STORE_NAME               9 (passed)

 99           LOAD_NAME                8 (property)

100           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\integrity_check.py", line 100>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object counts at 0x0000018C17FE1920, file "scripts\integrity_check.py", line 99>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)

 99           CALL                     0

100           STORE_NAME              10 (counts)

105           LOAD_CONST              16 (('', ''))
              LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18024C30, file "scripts\integrity_check.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object add at 0x0000018C1802CC10, file "scripts\integrity_check.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              11 (add)

108           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\integrity_check.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object to_dict at 0x0000018C17FF1230, file "scripts\integrity_check.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              12 (to_dict)
              LOAD_CONST              14 (())
              STORE_NAME              13 (__static_attributes__)
              LOAD_CONST              15 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\integrity_check.py", line 96>:
 96           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('bool')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object passed at 0x0000018C17F95E60, file "scripts\integrity_check.py", line 95>:
 95           RESUME                   0

 97           LOAD_GLOBAL              0 (all)
              COPY                     1
              LOAD_COMMON_CONSTANT     3 (<built-in function all>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       38 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4250, file "scripts\integrity_check.py", line 97>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (results)
              GET_ITER
              CALL                     0
      L1:     FOR_ITER                12 (to L3)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)
      L2:     POP_ITER
              LOAD_CONST               1 (False)
              RETURN_VALUE
      L3:     END_FOR
              POP_ITER
              LOAD_CONST               2 (True)
              RETURN_VALUE
      L4:     PUSH_NULL
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4250, file "scripts\integrity_check.py", line 97>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (results)
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180F4250, file "scripts\integrity_check.py", line 97>:
  97           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                0 (passed)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\integrity_check.py", line 100>:
100           RESUME                   0
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

Disassembly of <code object counts at 0x0000018C17FE1920, file "scripts\integrity_check.py", line 99>:
 99           RESUME                   0

101           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (results)
              CALL                     1
              STORE_FAST               1 (n)

102           LOAD_GLOBAL              5 (sum + NULL)
              LOAD_CONST               0 (<code object <genexpr> at 0x0000018C18053E10, file "scripts\integrity_check.py", line 102>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                2 (results)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               2 (passed)

103           LOAD_CONST               1 ('total')
              LOAD_FAST_BORROW         1 (n)
              LOAD_CONST               2 ('passed')
              LOAD_FAST_BORROW         2 (passed)
              LOAD_CONST               3 ('failed')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (n, passed)
              BINARY_OP               10 (-)
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053E10, file "scripts\integrity_check.py", line 102>:
 102           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                26 (to L5)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                0 (passed)
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           22 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           28 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts\integrity_check.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('name')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('passed')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('category')
              LOAD_CONST               2 ('str')
              LOAD_CONST               7 ('return')
              LOAD_CONST               8 ('None')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object add at 0x0000018C1802CC10, file "scripts\integrity_check.py", line 105>:
105           RESUME                   0

106           LOAD_FAST_BORROW         0 (self)
              LOAD_ATTR                0 (results)
              LOAD_ATTR                3 (append + NULL|self)
              LOAD_GLOBAL              5 (CheckResult + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (name, passed)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (detail, category)
              LOAD_CONST               0 (('name', 'passed', 'detail', 'category'))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\integrity_check.py", line 108>:
108           RESUME                   0
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

Disassembly of <code object to_dict at 0x0000018C17FF1230, file "scripts\integrity_check.py", line 108>:
 108           RESUME                   0

 110           LOAD_CONST               0 ('tool')
               LOAD_CONST               1 ('pas143e.integrity_check')

 111           LOAD_CONST               2 ('generated_at')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                0 (generated_at)

 112           LOAD_CONST               3 ('counts')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                2 (counts)

 113           LOAD_CONST               4 ('passed')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                4 (passed)

 114           LOAD_CONST               5 ('results')
               LOAD_FAST_BORROW         0 (self)
               LOAD_ATTR                6 (results)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (r)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                18 (to L3)
               STORE_FAST_LOAD_FAST    17 (r, r)
               LOAD_ATTR                9 (to_dict + NULL|self)
               CALL                     0
               LIST_APPEND              2
               JUMP_BACKWARD           20 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               1 (r)

 109           BUILD_MAP                5
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

 114           SWAP                     2
               STORE_FAST               1 (r)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [11]

Disassembly of <code object _norm_row at 0x0000018C1800AA60, file "scripts\integrity_check.py", line 122>:
122           RESUME                   0

124           BUILD_MAP                0

125           LOAD_CONST               1 ('event_type')
              LOAD_FAST_BORROW         0 (et)

124           MAP_ADD                  1

126           LOAD_CONST               2 ('created_at')
              LOAD_FAST_BORROW         1 (ts)

124           MAP_ADD                  1

127           LOAD_CONST               3 ('brokerage_id')
              LOAD_CONST               4 ('brk-test')

124           MAP_ADD                  1

128           LOAD_CONST               5 ('call_id')
              LOAD_FAST_BORROW         2 (kw)
              LOAD_ATTR                1 (pop + NULL|self)
              LOAD_CONST               5 ('call_id')
              LOAD_CONST               6 ('SIM-INT-1')
              CALL                     2

124           MAP_ADD                  1

129           LOAD_CONST               7 ('lead_id')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

130           LOAD_CONST               9 ('actor')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

131           LOAD_CONST              10 ('workflow_stage')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

132           LOAD_CONST              11 ('input_text')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

133           LOAD_CONST              12 ('output_text')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

134           LOAD_CONST              13 ('extracted_field')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

135           LOAD_CONST              14 ('extracted_value')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

136           LOAD_CONST              15 ('confidence_score')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

137           LOAD_CONST              16 ('outcome_state')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

138           LOAD_CONST              17 ('source')
              LOAD_CONST              18 ('simulated')

124           MAP_ADD                  1

139           LOAD_CONST              19 ('state')
              LOAD_CONST               8 (None)

124           MAP_ADD                  1

140           LOAD_CONST              20 ('payload')
              BUILD_MAP                0

124           MAP_ADD                  1
              STORE_FAST               3 (base)

142           LOAD_FAST_BORROW         3 (base)
              LOAD_ATTR                3 (update + NULL|self)
              LOAD_FAST_BORROW         2 (kw)
              CALL                     1
              POP_TOP

143           LOAD_GLOBAL              5 (normalize_event + NULL)
              LOAD_FAST_BORROW         3 (base)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\integrity_check.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('list')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _canonical_buyer_event_stream at 0x0000018C179A7290, file "scripts\integrity_check.py", line 146>:
146           RESUME                   0

148           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST               0 ('call.started')
              LOAD_CONST               1 ('system')

149           LOAD_CONST               2 ('lead_received')
              LOAD_FAST_BORROW         0 (call_id)

148           LOAD_CONST               3 (('actor', 'workflow_stage', 'call_id'))
              CALL_KW                  4

150           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST               4 ('lead.uttered')
              LOAD_CONST               5 ('lead')
              LOAD_CONST               6 ('GREETING')

151           LOAD_CONST               7 ('hi')
              LOAD_CONST               8 ('speaker')
              LOAD_CONST               5 ('lead')
              BUILD_MAP                1

152           LOAD_FAST_BORROW         0 (call_id)

150           LOAD_CONST               9 (('actor', 'state', 'input_text', 'payload', 'call_id'))
              CALL_KW                  6

153           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              10 ('pas.uttered')
              LOAD_CONST              11 ('pas')
              LOAD_CONST               6 ('GREETING')

154           LOAD_CONST              12 ('hello')
              LOAD_CONST               8 ('speaker')
              LOAD_CONST              11 ('pas')
              BUILD_MAP                1

155           LOAD_FAST_BORROW         0 (call_id)

153           LOAD_CONST              13 (('actor', 'state', 'output_text', 'payload', 'call_id'))
              CALL_KW                  6

156           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              14 ('lead.extracted')
              LOAD_CONST              11 ('pas')
              LOAD_CONST              15 ('INTENT')

157           LOAD_CONST              16 ('intent')
              LOAD_CONST              17 ('buying')

158           LOAD_CONST              18 (1.0)
              LOAD_FAST_BORROW         0 (call_id)

156           LOAD_CONST              19 (('actor', 'state', 'extracted_field', 'extracted_value', 'confidence_score', 'call_id'))
              CALL_KW                  7

159           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              14 ('lead.extracted')
              LOAD_CONST              11 ('pas')
              LOAD_CONST              20 ('BUDGET')

160           LOAD_CONST              21 ('budget')
              LOAD_CONST              22 ('$400k')

161           LOAD_CONST              18 (1.0)
              LOAD_FAST_BORROW         0 (call_id)

159           LOAD_CONST              19 (('actor', 'state', 'extracted_field', 'extracted_value', 'confidence_score', 'call_id'))
              CALL_KW                  7

162           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              14 ('lead.extracted')
              LOAD_CONST              11 ('pas')
              LOAD_CONST              23 ('TIMELINE')

163           LOAD_CONST              24 ('timeline')
              LOAD_CONST              25 ('3 months')

164           LOAD_CONST              18 (1.0)
              LOAD_FAST_BORROW         0 (call_id)

162           LOAD_CONST              19 (('actor', 'state', 'extracted_field', 'extracted_value', 'confidence_score', 'call_id'))
              CALL_KW                  7

165           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              26 ('booking.confirmed')
              LOAD_CONST              11 ('pas')

166           LOAD_CONST              27 ('booking_confirmed')
              LOAD_CONST              28 ('booked')

167           LOAD_FAST_BORROW         0 (call_id)

165           LOAD_CONST              29 (('actor', 'workflow_stage', 'outcome_state', 'call_id'))
              CALL_KW                  5

168           LOAD_GLOBAL              1 (_norm_row + NULL)
              LOAD_CONST              30 ('call.ended')
              LOAD_CONST               1 ('system')

169           LOAD_CONST              31 ('completed')
              LOAD_CONST              28 ('booked')

170           LOAD_CONST              32 ('outcome')
              LOAD_CONST              28 ('booked')
              BUILD_MAP                1
              LOAD_FAST_BORROW         0 (call_id)

168           LOAD_CONST              33 (('actor', 'workflow_stage', 'outcome_state', 'payload', 'call_id'))
              CALL_KW                  6

147           BUILD_LIST               8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\integrity_check.py", line 178>:
178           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_normalization_top_level_vs_fallback at 0x0000018C17F63C30, file "scripts\integrity_check.py", line 178>:
  --            MAKE_CELL                6 (a)
                MAKE_CELL                7 (b)

 178            RESUME                   0

 182            LOAD_CONST               1 ('event_type')
                LOAD_CONST               2 ('lead.extracted')

 183            LOAD_CONST               3 ('actor')
                LOAD_CONST               4 ('pas')

 184            LOAD_CONST               5 ('extracted_field')
                LOAD_CONST               6 ('budget')

 185            LOAD_CONST               7 ('extracted_value')
                LOAD_CONST               8 ('$400k')

 186            LOAD_CONST               9 ('confidence_score')
                LOAD_CONST              10 (0.92)

 187            LOAD_CONST              11 ('source')
                LOAD_CONST              12 ('voice')

 188            LOAD_CONST              13 ('payload')
                LOAD_CONST              14 ('raw_text')
                LOAD_CONST              15 ('x')
                BUILD_MAP                1

 181            BUILD_MAP                7
                STORE_FAST               1 (top)

 191            LOAD_CONST               1 ('event_type')
                LOAD_CONST               2 ('lead.extracted')

 192            LOAD_CONST              13 ('payload')

 193            LOAD_CONST              16 ('field')
                LOAD_CONST               6 ('budget')
                LOAD_CONST              17 ('value')
                LOAD_CONST               8 ('$400k')

 194            LOAD_CONST              18 ('contract')

 195            LOAD_CONST               3 ('actor')
                LOAD_CONST               4 ('pas')
                LOAD_CONST               5 ('extracted_field')
                LOAD_CONST               6 ('budget')

 196            LOAD_CONST               7 ('extracted_value')
                LOAD_CONST               8 ('$400k')
                LOAD_CONST               9 ('confidence_score')
                LOAD_CONST              10 (0.92)

 197            LOAD_CONST              11 ('source')
                LOAD_CONST              12 ('voice')

 194            BUILD_MAP                5

 192            BUILD_MAP                3

 190            BUILD_MAP                2
                STORE_FAST               2 (nest)

 201            LOAD_GLOBAL              1 (normalize_event + NULL)
                LOAD_FAST_BORROW         1 (top)
                CALL                     1
                LOAD_GLOBAL              1 (normalize_event + NULL)
                LOAD_FAST_BORROW         2 (nest)
                CALL                     1
                SWAP                     2
                STORE_DEREF              6 (a)
                STORE_DEREF              7 (b)

 202            LOAD_CONST              28 (('actor', 'extracted_field', 'extracted_value', 'confidence_score', 'source'))
                STORE_FAST               3 (keys)

 203            LOAD_GLOBAL              2 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       32 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         6 (a)
                LOAD_FAST_BORROW         7 (b)
                BUILD_TUPLE              2
                LOAD_CONST              19 (<code object <genexpr> at 0x0000018C18039070, file "scripts\integrity_check.py", line 203>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         3 (keys)
                GET_ITER
                CALL                     0
        L1:     FOR_ITER                12 (to L3)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L1)
        L2:     POP_ITER
                LOAD_CONST              20 (False)
                JUMP_FORWARD            21 (to L5)
        L3:     END_FOR
                POP_ITER
                LOAD_CONST              21 (True)
                JUMP_FORWARD            17 (to L5)
        L4:     PUSH_NULL
                LOAD_FAST_BORROW         6 (a)
                LOAD_FAST_BORROW         7 (b)
                BUILD_TUPLE              2
                LOAD_CONST              19 (<code object <genexpr> at 0x0000018C18039070, file "scripts\integrity_check.py", line 203>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         3 (keys)
                GET_ITER
                CALL                     0
                CALL                     1
        L5:     STORE_FAST               4 (same)

 204            LOAD_FAST                0 (report)
                LOAD_ATTR                5 (add + NULL|self)

 205            LOAD_CONST              22 ('normalization: v8 top-level == payload[contract] fallback')

 206            LOAD_FAST                4 (same)

 207            LOAD_FAST_BORROW         4 (same)
                TO_BOOL
                POP_JUMP_IF_TRUE        61 (to L12)
                NOT_TAKEN
                LOAD_CONST              23 ('diffs=')
                LOAD_FAST_BORROW         3 (keys)
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (k)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                44 (to L10)
                STORE_FAST               5 (k)
                LOAD_DEREF               6 (a)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         5 (k)
                CALL                     1
                LOAD_DEREF               7 (b)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_FAST_BORROW         5 (k)
                CALL                     1
                COMPARE_OP             119 (bool(!=))
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           42 (to L7)
        L9:     LOAD_FAST_BORROW         5 (k)
                LIST_APPEND              2
                JUMP_BACKWARD           46 (to L7)
       L10:     END_FOR
                POP_ITER
       L11:     SWAP                     2
                STORE_FAST               5 (k)
                FORMAT_SIMPLE
                BUILD_STRING             2
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              24 ('')

 208   L13:     LOAD_CONST              25 ('normalization')

 204            LOAD_CONST              26 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST              27 (None)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 207            SWAP                     2
                STORE_FAST               5 (k)
                RERAISE                  0
ExceptionTable:
  L6 to L8 -> L14 [7]
  L9 to L11 -> L14 [7]

Disassembly of <code object <genexpr> at 0x0000018C18039070, file "scripts\integrity_check.py", line 203>:
  --           COPY_FREE_VARS           2

 203           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                40 (to L3)
               STORE_FAST               1 (k)
               LOAD_DEREF               2 (a)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               LOAD_DEREF               3 (b)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               COMPARE_OP              72 (==)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           42 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\integrity_check.py", line 212>:
212           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_get_contract_value_returns_none_for_garbage at 0x0000018C17FF13B0, file "scripts\integrity_check.py", line 212>:
212           RESUME                   0

215           LOAD_GLOBAL              1 (get_contract_value + NULL)
              LOAD_CONST               1 (None)
              LOAD_CONST               2 ('actor')
              CALL                     2
              LOAD_CONST               1 (None)
              IS_OP                    0 (is)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L1)
              NOT_TAKEN
              POP_TOP

216           LOAD_GLOBAL              1 (get_contract_value + NULL)
              BUILD_MAP                0
              LOAD_CONST               3 ('anything')
              CALL                     2
              LOAD_CONST               1 (None)
              IS_OP                    0 (is)

215           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN
              POP_TOP

217           LOAD_GLOBAL              1 (get_contract_value + NULL)
              LOAD_CONST               2 ('actor')
              LOAD_CONST               1 (None)
              BUILD_MAP                1
              LOAD_CONST               2 ('actor')
              CALL                     2
              LOAD_CONST               1 (None)
              IS_OP                    0 (is)

214   L1:     STORE_FAST               1 (ok)

219           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (add + NULL|self)

220           LOAD_CONST               4 ('normalization: get_contract_value handles garbage')

221           LOAD_FAST_BORROW         1 (ok)
              LOAD_CONST               5 ('normalization')

219           LOAD_CONST               6 (('passed', 'category'))
              CALL_KW                  3
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\integrity_check.py", line 225>:
225           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_full_buyer_lifecycle_replay at 0x0000018C17F01250, file "scripts\integrity_check.py", line 225>:
225           RESUME                   0

226           LOAD_GLOBAL              1 (reconstruct_call + NULL)
              LOAD_GLOBAL              3 (_canonical_buyer_event_stream + NULL)
              CALL                     0
              CALL                     1
              STORE_FAST               1 (rec)

228           LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               0 ('final_outcome')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('booked')
              COMPARE_OP              72 (==)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       62 (to L1)
              NOT_TAKEN
              POP_TOP

229           LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               2 ('missing_lifecycle_steps')
              BINARY_OP               26 ([])
              BUILD_LIST               0
              COMPARE_OP              72 (==)

228           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L1)
              NOT_TAKEN
              POP_TOP

230           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               3 ('turns')
              BINARY_OP               26 ([])
              CALL                     1
              LOAD_SMALL_INT           2
              COMPARE_OP              72 (==)

228           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L1)
              NOT_TAKEN
              POP_TOP

231           LOAD_CONST               4 ('intent')
              LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               5 ('extracted_fields')
              BINARY_OP               26 ([])
              CONTAINS_OP              0 (in)

227   L1:     STORE_FAST               2 (ok)

233           LOAD_FAST                0 (report)
              LOAD_ATTR                7 (add + NULL|self)

234           LOAD_CONST               6 ('replay: full buyer lifecycle reconstructs cleanly')

235           LOAD_FAST                2 (ok)

237           LOAD_FAST_BORROW         2 (ok)
              TO_BOOL
              POP_JUMP_IF_TRUE        23 (to L2)
              NOT_TAKEN

236           LOAD_CONST               7 ('missing=')
              LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               2 ('missing_lifecycle_steps')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' outcome=')
              LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               0 ('final_outcome')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             4
              JUMP_FORWARD             1 (to L3)

237   L2:     LOAD_CONST               9 ('')

238   L3:     LOAD_CONST              10 ('replay')

233           LOAD_CONST              11 (('passed', 'detail', 'category'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST              12 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\integrity_check.py", line 242>:
242           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_evaluator_score_range at 0x0000018C179C3A50, file "scripts\integrity_check.py", line 242>:
242           RESUME                   0

243           LOAD_GLOBAL              1 (reconstruct_call + NULL)
              LOAD_GLOBAL              3 (_canonical_buyer_event_stream + NULL)
              CALL                     0
              CALL                     1
              STORE_FAST               1 (rec)

244           LOAD_GLOBAL              5 (evaluate_reconstruction + NULL)
              LOAD_FAST_BORROW         1 (rec)
              CALL                     1
              STORE_FAST               2 (ev)

245           LOAD_FAST_BORROW         2 (ev)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               0 ('replay_score')
              CALL                     1
              STORE_FAST               3 (s)

246           LOAD_GLOBAL              9 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (s)
              LOAD_GLOBAL             10 (int)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT           0
              LOAD_FAST                3 (s)
              SWAP                     2
              COPY                     2
              COMPARE_OP              42 (<=)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT         100
              COMPARE_OP              42 (<=)
              JUMP_FORWARD             2 (to L2)
      L1:     SWAP                     2
              POP_TOP
      L2:     STORE_FAST               4 (ok)

247           LOAD_FAST                0 (report)
              LOAD_ATTR               13 (add + NULL|self)

248           LOAD_CONST               1 ('evaluator: replay_score in [0, 100]')

249           LOAD_FAST                4 (ok)

250           LOAD_FAST_BORROW         4 (ok)
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L3)
              NOT_TAKEN
              LOAD_CONST               2 ('score=')
              LOAD_FAST_BORROW         3 (s)
              FORMAT_SIMPLE
              BUILD_STRING             2
              JUMP_FORWARD             4 (to L4)
      L3:     LOAD_CONST               2 ('score=')
              LOAD_FAST_BORROW         3 (s)
              FORMAT_SIMPLE
              BUILD_STRING             2

251   L4:     LOAD_CONST               3 ('evaluator')

247           LOAD_CONST               4 (('passed', 'detail', 'category'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\integrity_check.py", line 255>:
255           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_evaluator_empty_input at 0x0000018C17EA4B40, file "scripts\integrity_check.py", line 255>:
255           RESUME                   0

257           LOAD_GLOBAL              1 (evaluate_reconstruction + NULL)
              LOAD_GLOBAL              3 (reconstruct_call + NULL)
              BUILD_LIST               0
              CALL                     1
              CALL                     1
              STORE_FAST               1 (out_empty)

258           LOAD_GLOBAL              1 (evaluate_reconstruction + NULL)
              LOAD_CONST               1 (None)
              CALL                     1
              STORE_FAST               2 (out_none)

260           LOAD_SMALL_INT           0
              LOAD_FAST_BORROW         1 (out_empty)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('replay_score')
              LOAD_CONST               8 (-1)
              CALL                     2
              SWAP                     2
              COPY                     2
              COMPARE_OP              42 (<=)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT         100
              COMPARE_OP              42 (<=)
              JUMP_FORWARD             2 (to L2)
      L1:     SWAP                     2
              POP_TOP
      L2:     COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN
              POP_TOP

261           LOAD_SMALL_INT           0
              LOAD_FAST_BORROW         2 (out_none)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('replay_score')
              LOAD_CONST               8 (-1)
              CALL                     2
              SWAP                     2
              COPY                     2
              COMPARE_OP              42 (<=)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        6 (to L3)
              NOT_TAKEN
              POP_TOP
              LOAD_SMALL_INT         100
              COMPARE_OP              42 (<=)
              JUMP_FORWARD             2 (to L4)
      L3:     SWAP                     2
              POP_TOP

260   L4:     COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       47 (to L5)
              NOT_TAKEN
              POP_TOP

262           LOAD_FAST_BORROW         1 (out_empty)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('is_replayable')
              CALL                     1
              LOAD_CONST               4 (False)
              IS_OP                    0 (is)

260           COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       20 (to L5)
              NOT_TAKEN
              POP_TOP

263           LOAD_FAST_BORROW         2 (out_none)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('is_replayable')
              CALL                     1
              LOAD_CONST               4 (False)
              IS_OP                    0 (is)

259   L5:     STORE_FAST               3 (ok)

265           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                7 (add + NULL|self)

266           LOAD_CONST               5 ('evaluator: empty/None input bounded + non-replayable')

267           LOAD_FAST_BORROW         3 (ok)
              LOAD_CONST               6 ('evaluator')

265           LOAD_CONST               7 (('passed', 'category'))
              CALL_KW                  3
              POP_TOP
              LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\integrity_check.py", line 271>:
271           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_missing_lifecycle_stage_detection at 0x0000018C1804CD30, file "scripts\integrity_check.py", line 271>:
 271           RESUME                   0

 273           LOAD_GLOBAL              1 (_canonical_buyer_event_stream + NULL)
               CALL                     0
               STORE_FAST               1 (stream)

 274           LOAD_FAST_BORROW         1 (stream)
               GET_ITER
               LOAD_FAST_AND_CLEAR      2 (r)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                20 (to L5)
               STORE_FAST_LOAD_FAST    34 (r, r)
               LOAD_CONST               1 ('event_type')
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('call.ended')
               COMPARE_OP             119 (bool(!=))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_FAST_BORROW         2 (r)
               LIST_APPEND              2
               JUMP_BACKWARD           22 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     STORE_FAST               1 (stream)
               STORE_FAST               2 (r)

 275           LOAD_GLOBAL              3 (reconstruct_call + NULL)
               LOAD_FAST_BORROW         1 (stream)
               CALL                     1
               STORE_FAST               3 (rec)

 276           LOAD_CONST               3 ('completed')
               LOAD_FAST_BORROW         3 (rec)
               LOAD_CONST               4 ('missing_lifecycle_steps')
               BINARY_OP               26 ([])
               CONTAINS_OP              0 (in)
               STORE_FAST               4 (ok)

 277           LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                5 (add + NULL|self)

 278           LOAD_CONST               5 ('replay: missing lifecycle stage surfaces')

 279           LOAD_FAST_BORROW         4 (ok)

 280           LOAD_CONST               6 ('missing_lifecycle_steps=')
               LOAD_FAST_BORROW         3 (rec)
               LOAD_CONST               4 ('missing_lifecycle_steps')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

 281           LOAD_CONST               7 ('replay')

 277           LOAD_CONST               8 (('passed', 'detail', 'category'))
               CALL_KW                  4
               POP_TOP
               LOAD_CONST               9 (None)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 274           SWAP                     2
               STORE_FAST               2 (r)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [2]
  L4 to L6 -> L7 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\integrity_check.py", line 285>:
285           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_malformed_row_does_not_crash at 0x0000018C17FF10B0, file "scripts\integrity_check.py", line 285>:
285           RESUME                   0

286           LOAD_GLOBAL              1 (reconstruct_call + NULL)
              LOAD_CONST               0 (None)
              LOAD_CONST               1 ('garbage')
              LOAD_SMALL_INT          42
              LOAD_GLOBAL              3 (_norm_row + NULL)
              LOAD_CONST               2 ('call.started')
              CALL                     1
              BUILD_LIST               4
              CALL                     1
              STORE_FAST               1 (rec)

287           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (rec)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_FAST_BORROW         1 (rec)
              LOAD_CONST               3 ('events_count')
              BINARY_OP               26 ([])
              LOAD_SMALL_INT           4
              COMPARE_OP              72 (==)
      L1:     STORE_FAST               2 (ok)

288           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                9 (add + NULL|self)

289           LOAD_CONST               4 ('replay: malformed rows handled without raising')

290           LOAD_FAST_BORROW         2 (ok)
              LOAD_CONST               5 ('robustness')

288           LOAD_CONST               6 (('passed', 'category'))
              CALL_KW                  3
              POP_TOP
              LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\integrity_check.py", line 294>:
294           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_duplicate_event_id_detection at 0x0000018C1801C9E0, file "scripts\integrity_check.py", line 294>:
294           RESUME                   0

298           LOAD_GLOBAL              1 (_canonical_buyer_event_stream + NULL)
              CALL                     0
              STORE_FAST               1 (stream)

300           LOAD_CONST               1 ('abc')
              LOAD_FAST_BORROW         1 (stream)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('event_id')
              STORE_SUBSCR

301           LOAD_CONST               1 ('abc')
              LOAD_FAST_BORROW         1 (stream)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('event_id')
              STORE_SUBSCR

302           BUILD_MAP                0
              STORE_FAST               2 (seen)

303           BUILD_LIST               0
              STORE_FAST               3 (duplicates)

304           LOAD_FAST_BORROW         1 (stream)
              GET_ITER
      L1:     FOR_ITER                57 (to L4)
              STORE_FAST               4 (r)

305           LOAD_FAST_BORROW         4 (r)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               2 ('event_id')
              CALL                     1
              STORE_FAST               5 (eid)

306           LOAD_FAST_BORROW         5 (eid)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

307           JUMP_BACKWARD           30 (to L1)

308   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 82 (eid, seen)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

309           LOAD_FAST_BORROW         3 (duplicates)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         5 (eid)
              CALL                     1
              POP_TOP

310   L3:     LOAD_CONST               3 (True)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (seen, eid)
              STORE_SUBSCR
              JUMP_BACKWARD           59 (to L1)

304   L4:     END_FOR
              POP_ITER

311           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                7 (add + NULL|self)

312           LOAD_CONST               4 ('events: duplicate event_id detection works')

313           LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         3 (duplicates)
              CALL                     1
              LOAD_SMALL_INT           1
              COMPARE_OP              72 (==)

314           LOAD_CONST               5 ('duplicates=')
              LOAD_FAST_BORROW         3 (duplicates)
              FORMAT_SIMPLE
              BUILD_STRING             2
              LOAD_CONST               6 ('events')

311           LOAD_CONST               7 (('passed', 'detail', 'category'))
              CALL_KW                  4
              POP_TOP
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\integrity_check.py", line 318>:
318           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_strategy_registry_ids_unique_and_known at 0x0000018C17E589A0, file "scripts\integrity_check.py", line 318>:
 318            RESUME                   0

 319            LOAD_GLOBAL              0 (STRATEGIES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (s)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                14 (to L3)
                STORE_FAST_LOAD_FAST    17 (s, s)
                LOAD_ATTR                2 (id)
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     STORE_FAST               2 (ids)
                STORE_FAST               1 (s)

 320            LOAD_GLOBAL              5 (len + NULL)
                LOAD_GLOBAL              7 (set + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                CALL                     1
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                COMPARE_OP              72 (==)
                STORE_FAST               3 (unique)

 321            LOAD_GLOBAL              8 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4140, file "scripts\integrity_check.py", line 321>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (ids)
                GET_ITER
                CALL                     0
        L5:     FOR_ITER                12 (to L7)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L6:     POP_ITER
                LOAD_CONST               1 (False)
                JUMP_FORWARD            17 (to L9)
        L7:     END_FOR
                POP_ITER
                LOAD_CONST               2 (True)
                JUMP_FORWARD            13 (to L9)
        L8:     PUSH_NULL
                LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4140, file "scripts\integrity_check.py", line 321>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (ids)
                GET_ITER
                CALL                     0
                CALL                     1
        L9:     STORE_FAST               4 (nonempty)

 322            LOAD_FAST                0 (report)
                LOAD_ATTR               11 (add + NULL|self)

 323            LOAD_CONST               3 ('optimization: strategy ids unique + non-empty')

 324            LOAD_FAST                3 (unique)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                4 (nonempty)

 325   L10:     LOAD_CONST               4 ('n=')
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST               5 ('optimization')

 322            LOAD_CONST               6 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST               7 (None)
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 319            SWAP                     2
                STORE_FAST               1 (s)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L11 [2]

Disassembly of <code object <genexpr> at 0x0000018C180F4140, file "scripts\integrity_check.py", line 321>:
 321           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (i)
               LOAD_GLOBAL              1 (bool + NULL)
               LOAD_FAST_BORROW         1 (i)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\integrity_check.py", line 329>:
329           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_personality_registry_ids_unique_and_known at 0x0000018C17E58770, file "scripts\integrity_check.py", line 329>:
 329            RESUME                   0

 330            LOAD_GLOBAL              0 (PERSONALITIES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (p)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                14 (to L3)
                STORE_FAST_LOAD_FAST    17 (p, p)
                LOAD_ATTR                2 (id)
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     STORE_FAST               2 (ids)
                STORE_FAST               1 (p)

 331            LOAD_GLOBAL              5 (len + NULL)
                LOAD_GLOBAL              7 (set + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                CALL                     1
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                COMPARE_OP              72 (==)
                STORE_FAST               3 (unique)

 332            LOAD_GLOBAL              8 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4030, file "scripts\integrity_check.py", line 332>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (ids)
                GET_ITER
                CALL                     0
        L5:     FOR_ITER                12 (to L7)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L6:     POP_ITER
                LOAD_CONST               1 (False)
                JUMP_FORWARD            17 (to L9)
        L7:     END_FOR
                POP_ITER
                LOAD_CONST               2 (True)
                JUMP_FORWARD            13 (to L9)
        L8:     PUSH_NULL
                LOAD_CONST               0 (<code object <genexpr> at 0x0000018C180F4030, file "scripts\integrity_check.py", line 332>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         2 (ids)
                GET_ITER
                CALL                     0
                CALL                     1
        L9:     STORE_FAST               4 (nonempty)

 333            LOAD_FAST                0 (report)
                LOAD_ATTR               11 (add + NULL|self)

 334            LOAD_CONST               3 ('behaviour: personality ids unique + non-empty')

 335            LOAD_FAST                3 (unique)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                4 (nonempty)

 336   L10:     LOAD_CONST               4 ('n=')
                LOAD_GLOBAL              5 (len + NULL)
                LOAD_FAST_BORROW         2 (ids)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST               5 ('behaviour')

 333            LOAD_CONST               6 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST               7 (None)
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 330            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L11 [2]

Disassembly of <code object <genexpr> at 0x0000018C180F4030, file "scripts\integrity_check.py", line 332>:
 332           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (i)
               LOAD_GLOBAL              1 (bool + NULL)
               LOAD_FAST_BORROW         1 (i)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           18 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\integrity_check.py", line 340>:
340           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_scenario_personalities_resolve at 0x0000018C17FEDA30, file "scripts\integrity_check.py", line 340>:
 340            RESUME                   0

 343            LOAD_GLOBAL              0 (PERSONALITIES)
                GET_ITER
                LOAD_FAST_AND_CLEAR      1 (p)
                SWAP                     2
        L1:     BUILD_SET                0
                SWAP                     2
        L2:     FOR_ITER                14 (to L3)
                STORE_FAST_LOAD_FAST    17 (p, p)
                LOAD_ATTR                2 (id)
                SET_ADD                  2
                JUMP_BACKWARD           16 (to L2)
        L3:     END_FOR
                POP_ITER
        L4:     STORE_FAST               2 (known)
                STORE_FAST               1 (p)

 344            LOAD_GLOBAL              4 (SCENARIOS)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (s)
                SWAP                     2
        L5:     BUILD_LIST               0
                SWAP                     2
        L6:     FOR_ITER                50 (to L11)
                STORE_FAST               3 (s)

 345            LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR                6 (personality_id)

 344    L7:     POP_JUMP_IF_NOT_NONE     3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L6)

 345    L8:     LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR                6 (personality_id)
                LOAD_FAST_BORROW         2 (known)
                CONTAINS_OP              1 (not in)

 344    L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           38 (to L6)
       L10:     LOAD_FAST_BORROW         3 (s)
                LOAD_ATTR                2 (id)
                LIST_APPEND              2
                JUMP_BACKWARD           52 (to L6)
       L11:     END_FOR
                POP_ITER
       L12:     STORE_FAST               4 (bad)
                STORE_FAST               3 (s)

 346            LOAD_FAST                0 (report)
                LOAD_ATTR                9 (add + NULL|self)

 347            LOAD_CONST               2 ('scenarios: personality_id references resolve')

 348            LOAD_FAST_BORROW         4 (bad)
                TO_BOOL
                UNARY_NOT

 349            LOAD_FAST_BORROW         4 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L13)
                NOT_TAKEN
                LOAD_CONST               3 ('unknown personality refs: ')
                LOAD_FAST_BORROW         4 (bad)
                FORMAT_SIMPLE
                BUILD_STRING             2
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               4 ('')

 350   L14:     LOAD_CONST               5 ('scenarios')

 346            LOAD_CONST               6 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 343            SWAP                     2
                STORE_FAST               1 (p)
                RERAISE                  0

  --   L16:     SWAP                     2
                POP_TOP

 344            SWAP                     2
                STORE_FAST               3 (s)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L15 [2]
  L5 to L7 -> L16 [2]
  L8 to L9 -> L16 [2]
  L10 to L12 -> L16 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\integrity_check.py", line 354>:
354           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_ranking_is_sorted_and_ranks_consecutive at 0x0000018C17D7CA80, file "scripts\integrity_check.py", line 354>:
  --            MAKE_CELL                5 (ranked)

 354            RESUME                   0

 356            LOAD_CONST               0 ('by_strategy')

 357            LOAD_CONST               1 ('A')
                LOAD_CONST               2 ('n')
                LOAD_SMALL_INT           1
                LOAD_CONST               3 ('passed')
                LOAD_SMALL_INT           1
                LOAD_CONST               4 ('pass_rate')
                LOAD_CONST               5 (1.0)

 358            LOAD_CONST               6 ('avg_replay_score')
                LOAD_SMALL_INT         100
                LOAD_CONST               7 ('avg_turns')
                LOAD_SMALL_INT           5

 359            LOAD_CONST               8 ('errors')
                LOAD_SMALL_INT           0
                LOAD_CONST               9 ('outcome_counts')
                LOAD_CONST              10 ('booked')
                LOAD_SMALL_INT           1
                BUILD_MAP                1

 360            LOAD_CONST              11 ('booked_rate')
                LOAD_CONST               5 (1.0)
                LOAD_CONST              12 ('callback_rate')
                LOAD_CONST              13 (0.0)

 361            LOAD_CONST              14 ('not_booked_rate')
                LOAD_CONST              13 (0.0)
                LOAD_CONST              15 ('transferred_rate')
                LOAD_CONST              13 (0.0)

 362            LOAD_CONST              16 ('effective')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 ('trust_avg')
                LOAD_CONST              19 (0.7)

 363            LOAD_CONST              20 ('frustration_avg')
                LOAD_CONST              21 (0.1)
                LOAD_CONST              22 ('divergence_count')
                LOAD_SMALL_INT           0

 357            BUILD_MAP               15

 364            LOAD_CONST              23 ('B')
                LOAD_CONST               2 ('n')
                LOAD_SMALL_INT           1
                LOAD_CONST               3 ('passed')
                LOAD_SMALL_INT           0
                LOAD_CONST               4 ('pass_rate')
                LOAD_CONST              13 (0.0)

 365            LOAD_CONST               6 ('avg_replay_score')
                LOAD_SMALL_INT          50
                LOAD_CONST               7 ('avg_turns')
                LOAD_SMALL_INT           5

 366            LOAD_CONST               8 ('errors')
                LOAD_SMALL_INT           0
                LOAD_CONST               9 ('outcome_counts')
                LOAD_CONST              24 ('not_booked')
                LOAD_SMALL_INT           1
                BUILD_MAP                1

 367            LOAD_CONST              11 ('booked_rate')
                LOAD_CONST              13 (0.0)
                LOAD_CONST              12 ('callback_rate')
                LOAD_CONST              13 (0.0)

 368            LOAD_CONST              14 ('not_booked_rate')
                LOAD_CONST               5 (1.0)
                LOAD_CONST              15 ('transferred_rate')
                LOAD_CONST              13 (0.0)

 369            LOAD_CONST              16 ('effective')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 ('trust_avg')
                LOAD_CONST              25 (0.5)

 370            LOAD_CONST              20 ('frustration_avg')
                LOAD_CONST              26 (0.3)
                LOAD_CONST              22 ('divergence_count')
                LOAD_SMALL_INT           0

 364            BUILD_MAP               15

 371            LOAD_CONST              27 ('C')
                LOAD_CONST               2 ('n')
                LOAD_SMALL_INT           1
                LOAD_CONST               3 ('passed')
                LOAD_SMALL_INT           1
                LOAD_CONST               4 ('pass_rate')
                LOAD_CONST               5 (1.0)

 372            LOAD_CONST               6 ('avg_replay_score')
                LOAD_SMALL_INT          80
                LOAD_CONST               7 ('avg_turns')
                LOAD_SMALL_INT           6

 373            LOAD_CONST               8 ('errors')
                LOAD_SMALL_INT           0
                LOAD_CONST               9 ('outcome_counts')
                LOAD_CONST              10 ('booked')
                LOAD_SMALL_INT           1
                BUILD_MAP                1

 374            LOAD_CONST              11 ('booked_rate')
                LOAD_CONST               5 (1.0)
                LOAD_CONST              12 ('callback_rate')
                LOAD_CONST              13 (0.0)

 375            LOAD_CONST              14 ('not_booked_rate')
                LOAD_CONST              13 (0.0)
                LOAD_CONST              15 ('transferred_rate')
                LOAD_CONST              13 (0.0)

 376            LOAD_CONST              16 ('effective')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 ('trust_avg')
                LOAD_CONST              28 (0.6)

 377            LOAD_CONST              20 ('frustration_avg')
                LOAD_CONST              29 (0.2)
                LOAD_CONST              22 ('divergence_count')
                LOAD_SMALL_INT           0

 371            BUILD_MAP               15

 356            BUILD_MAP                3

 355            BUILD_MAP                1
                STORE_FAST               1 (metrics)

 380            LOAD_GLOBAL              1 (rank_strategies + NULL)
                LOAD_FAST_BORROW         1 (metrics)
                CALL                     1
                STORE_DEREF              5 (ranked)

 381            LOAD_GLOBAL              2 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       56 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         5 (ranked)
                BUILD_TUPLE              1
                LOAD_CONST              30 (<code object <genexpr> at 0x0000018C17FE1290, file "scripts\integrity_check.py", line 381>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 383            LOAD_GLOBAL              5 (range + NULL)
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_DEREF               5 (ranked)
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                CALL                     1
                GET_ITER

 381            CALL                     0
        L1:     FOR_ITER                12 (to L3)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L1)
        L2:     POP_ITER
                LOAD_CONST              31 (False)
                JUMP_FORWARD            45 (to L5)
        L3:     END_FOR
                POP_ITER
                LOAD_CONST              17 (True)
                JUMP_FORWARD            41 (to L5)
        L4:     PUSH_NULL
                LOAD_FAST_BORROW         5 (ranked)
                BUILD_TUPLE              1
                LOAD_CONST              30 (<code object <genexpr> at 0x0000018C17FE1290, file "scripts\integrity_check.py", line 381>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 383            LOAD_GLOBAL              5 (range + NULL)
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_DEREF               5 (ranked)
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                CALL                     1
                GET_ITER

 381            CALL                     0
                CALL                     1
        L5:     STORE_FAST               2 (sorted_correctly)

 385            LOAD_DEREF               5 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (r)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                11 (to L8)
                STORE_FAST_LOAD_FAST    51 (r, r)
                LOAD_CONST              32 ('rank')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           13 (to L7)
        L8:     END_FOR
                POP_ITER
        L9:     SWAP                     2
                STORE_FAST               3 (r)
                LOAD_GLOBAL              9 (list + NULL)
                LOAD_GLOBAL              5 (range + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              7 (len + NULL)
                LOAD_DEREF               5 (ranked)
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                CALL                     2
                CALL                     1
                COMPARE_OP              72 (==)
                STORE_FAST               4 (ranks_consecutive)

 386            LOAD_FAST                0 (report)
                LOAD_ATTR               11 (add + NULL|self)

 387            LOAD_CONST              33 ('ranking: scores monotone + ranks consecutive')

 388            LOAD_FAST                2 (sorted_correctly)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST                4 (ranks_consecutive)

 389   L10:     LOAD_CONST              34 ('scores=')
                LOAD_DEREF               5 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (r)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2
       L12:     FOR_ITER                11 (to L13)
                STORE_FAST_LOAD_FAST    51 (r, r)
                LOAD_CONST              35 ('score')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           13 (to L12)
       L13:     END_FOR
                POP_ITER
       L14:     SWAP                     2
                STORE_FAST               3 (r)
                FORMAT_SIMPLE
                LOAD_CONST              36 (' ranks=')
                LOAD_DEREF               5 (ranked)
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (r)
                SWAP                     2
       L15:     BUILD_LIST               0
                SWAP                     2
       L16:     FOR_ITER                11 (to L17)
                STORE_FAST_LOAD_FAST    51 (r, r)
                LOAD_CONST              32 ('rank')
                BINARY_OP               26 ([])
                LIST_APPEND              2
                JUMP_BACKWARD           13 (to L16)
       L17:     END_FOR
                POP_ITER
       L18:     SWAP                     2
                STORE_FAST               3 (r)
                FORMAT_SIMPLE
                BUILD_STRING             4

 390            LOAD_CONST              37 ('optimization')

 386            LOAD_CONST              38 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST              39 (None)
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 385            SWAP                     2
                STORE_FAST               3 (r)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 389            SWAP                     2
                STORE_FAST               3 (r)
                RERAISE                  0

  --   L21:     SWAP                     2
                POP_TOP

 389            SWAP                     2
                STORE_FAST               3 (r)
                RERAISE                  0
ExceptionTable:
  L6 to L9 -> L19 [2]
  L11 to L14 -> L20 [7]
  L15 to L18 -> L21 [9]

Disassembly of <code object <genexpr> at 0x0000018C17FE1290, file "scripts\integrity_check.py", line 381>:
  --           COPY_FREE_VARS           1

 381           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 383   L2:     FOR_ITER                45 (to L3)
               STORE_FAST               1 (i)

 382           LOAD_DEREF               2 (ranked)
               LOAD_FAST_BORROW         1 (i)
               BINARY_OP               26 ([])
               LOAD_CONST               0 ('score')
               BINARY_OP               26 ([])
               LOAD_DEREF               2 (ranked)
               LOAD_FAST_BORROW         1 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               BINARY_OP               26 ([])
               LOAD_CONST               0 ('score')
               BINARY_OP               26 ([])
               COMPARE_OP             172 (>=)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           47 (to L2)

 383   L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\integrity_check.py", line 394>:
394           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_negative_metric_values at 0x0000018C17CD4970, file "scripts\integrity_check.py", line 394>:
 394            RESUME                   0

 398            LOAD_CONST               1 ('matrix_id')
                LOAD_CONST               2 ('MTX-T')
                LOAD_CONST               3 ('total_runs')
                LOAD_SMALL_INT           1

 399            LOAD_CONST               4 ('scenarios_count')
                LOAD_SMALL_INT           1
                LOAD_CONST               5 ('strategies_count')
                LOAD_SMALL_INT           1
                LOAD_CONST               6 ('brokerage_id')
                LOAD_CONST               7 ('demo')

 400            LOAD_CONST               8 ('started_at')
                LOAD_CONST               9 ('now')
                LOAD_CONST              10 ('generated_at')
                LOAD_CONST               9 ('now')
                LOAD_CONST              11 ('duration_ms')
                LOAD_SMALL_INT           0

 401            LOAD_CONST              12 ('results')
                BUILD_MAP                0

 402            LOAD_CONST              13 ('scenario_id')
                LOAD_CONST              14 ('s1')

 401            MAP_ADD                  1

 402            LOAD_CONST              15 ('scenario_title')
                LOAD_CONST              14 ('s1')

 401            MAP_ADD                  1

 402            LOAD_CONST              16 ('scenario_category')
                LOAD_CONST              17 ('core')

 401            MAP_ADD                  1

 403            LOAD_CONST              18 ('scenario_tags')
                BUILD_LIST               0

 401            MAP_ADD                  1

 403            LOAD_CONST              19 ('call_sid')
                LOAD_CONST              20 ('SIM-1')

 401            MAP_ADD                  1

 403            LOAD_CONST               6 ('brokerage_id')
                LOAD_CONST               7 ('demo')

 401            MAP_ADD                  1

 404            LOAD_CONST              21 ('expected_outcome')
                LOAD_CONST              22 ('booked')

 401            MAP_ADD                  1

 404            LOAD_CONST              23 ('actual_outcome')
                LOAD_CONST              22 ('booked')

 401            MAP_ADD                  1

 404            LOAD_CONST              24 ('passed')
                LOAD_CONST              25 (True)

 401            MAP_ADD                  1

 405            LOAD_CONST              26 ('events_count')
                LOAD_SMALL_INT           5

 401            MAP_ADD                  1

 405            LOAD_CONST              27 ('transcript')
                LOAD_CONST              28 ('speaker')
                LOAD_CONST              29 ('lead')
                BUILD_MAP                1
                BUILD_LIST               1

 401            MAP_ADD                  1

 406            LOAD_CONST              30 ('reconstruction')
                BUILD_MAP                0

 401            MAP_ADD                  1

 406            LOAD_CONST              31 ('evaluation')
                LOAD_CONST              32 ('replay_score')
                LOAD_SMALL_INT          80
                LOAD_CONST              33 ('missing_steps')
                BUILD_LIST               0
                BUILD_MAP                2

 401            MAP_ADD                  1

 407            LOAD_CONST              11 ('duration_ms')
                LOAD_SMALL_INT           1

 401            MAP_ADD                  1

 407            LOAD_CONST              34 ('error')
                LOAD_CONST              35 (None)

 401            MAP_ADD                  1

 408            LOAD_CONST              36 ('strategy_id')
                LOAD_CONST              37 ('A')

 401            MAP_ADD                  1

 408            LOAD_CONST              38 ('strategy_name')
                LOAD_CONST              37 ('A')

 401            MAP_ADD                  1

 408            LOAD_CONST              39 ('strategy_category')
                LOAD_CONST              40 ('greeting')

 409            LOAD_CONST              41 ('strategy_overrides')
                BUILD_MAP                0
                LOAD_CONST              42 ('strategy_effective')
                LOAD_CONST              25 (True)
                LOAD_CONST              43 ('cell_error')
                LOAD_CONST              35 (None)

 410            LOAD_CONST              44 ('personality_id')
                LOAD_CONST              45 ('motivated')
                LOAD_CONST              46 ('personality_name')
                LOAD_CONST              47 ('Motivated')

 411            LOAD_CONST              48 ('final_behavior_state')
                LOAD_CONST              49 ('engaged')
                LOAD_CONST              50 ('trust_score')
                LOAD_CONST              51 (0.7)

 412            LOAD_CONST              52 ('frustration_score')
                LOAD_CONST              53 (0.1)
                LOAD_CONST              54 ('divergence_triggered')
                LOAD_CONST              55 (False)

 413            LOAD_CONST              56 ('divergence_actions')
                BUILD_LIST               0

 401            BUILD_MAP               11
                DICT_UPDATE              1
                BUILD_LIST               1

 397            BUILD_MAP                9
                STORE_FAST               1 (matrix)

 416            LOAD_GLOBAL              1 (compute_matrix_metrics + NULL)
                LOAD_FAST_BORROW         1 (matrix)
                CALL                     1
                STORE_FAST               2 (m)

 417            LOAD_FAST_BORROW         2 (m)
                LOAD_ATTR                3 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (k)
                LOAD_FAST_AND_CLEAR      4 (v)
                SWAP                     3
        L1:     BUILD_LIST               0
                SWAP                     2
        L2:     FOR_ITER                46 (to L7)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (k, v)
                LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (v)
                LOAD_GLOBAL              6 (int)
                LOAD_GLOBAL              8 (float)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
        L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           35 (to L2)
        L4:     LOAD_FAST_BORROW         4 (v)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
        L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           44 (to L2)
        L6:     LOAD_FAST_BORROW         3 (k)
                LIST_APPEND              2
                JUMP_BACKWARD           48 (to L2)
        L7:     END_FOR
                POP_ITER
        L8:     STORE_FAST               5 (bad)
                STORE_FAST               3 (k)
                STORE_FAST               4 (v)

 418            LOAD_FAST                0 (report)
                LOAD_ATTR               11 (add + NULL|self)

 419            LOAD_CONST              57 ('metrics: no negative aggregate values')

 420            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                UNARY_NOT
                LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                LOAD_CONST              58 ('negative keys: ')
                LOAD_FAST_BORROW         5 (bad)
                FORMAT_SIMPLE
                BUILD_STRING             2
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              59 ('')

 421   L10:     LOAD_CONST              60 ('optimization')

 418            LOAD_CONST              61 (('passed', 'detail', 'category'))
                CALL_KW                  4
                POP_TOP
                LOAD_CONST              35 (None)
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 417            SWAP                     3
                STORE_FAST               4 (v)
                STORE_FAST               3 (k)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [3]
  L4 to L5 -> L11 [3]
  L6 to L8 -> L11 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\integrity_check.py", line 425>:
425           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_behavior_state_in_known_set at 0x0000018C17FF0C30, file "scripts\integrity_check.py", line 425>:
425           RESUME                   0

427           LOAD_GLOBAL              0 (all)
              COPY                     1
              LOAD_COMMON_CONSTANT     3 (<built-in function all>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       32 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802CAE0, file "scripts\integrity_check.py", line 427>)
              MAKE_FUNCTION
              LOAD_GLOBAL              2 (BEHAVIOR_STATES)
              GET_ITER
              CALL                     0
      L1:     FOR_ITER                12 (to L3)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)
      L2:     POP_ITER
              LOAD_CONST               2 (False)
              JUMP_FORWARD            21 (to L5)
      L3:     END_FOR
              POP_ITER
              LOAD_CONST               3 (True)
              JUMP_FORWARD            17 (to L5)
      L4:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C1802CAE0, file "scripts\integrity_check.py", line 427>)
              MAKE_FUNCTION
              LOAD_GLOBAL              2 (BEHAVIOR_STATES)
              GET_ITER
              CALL                     0
              CALL                     1
      L5:     STORE_FAST               1 (ok)

428           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                5 (add + NULL|self)

429           LOAD_CONST               4 ('behaviour: BEHAVIOR_STATES are valid strings')

430           LOAD_FAST_BORROW         1 (ok)
              LOAD_CONST               5 ('behaviour')

428           LOAD_CONST               6 (('passed', 'category'))
              CALL_KW                  3
              POP_TOP
              LOAD_CONST               7 (None)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C1802CAE0, file "scripts\integrity_check.py", line 427>:
 427           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                31 (to L6)
               STORE_FAST               1 (s)
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
       L3:     NOT_TAKEN
       L4:     POP_TOP
               LOAD_FAST                1 (s)
       L5:     YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           33 (to L2)
       L6:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L7:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L7 [0] lasti
  L4 to L7 -> L7 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\integrity_check.py", line 434>:
434           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('IntegrityReport')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_outcome_state_consistency at 0x0000018C17FE13E0, file "scripts\integrity_check.py", line 434>:
434           RESUME                   0

439           LOAD_CONST               1 ('actual_outcome')
              LOAD_CONST               2 ('booked')

440           LOAD_CONST               3 ('final_behavior_state')
              LOAD_CONST               4 ('dropping')

438           BUILD_MAP                2
              STORE_FAST               1 (bad_row)

442           LOAD_FAST_BORROW         1 (bad_row)
              LOAD_CONST               1 ('actual_outcome')
              BINARY_OP               26 ([])
              LOAD_CONST               2 ('booked')
              COMPARE_OP              72 (==)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L1)
              NOT_TAKEN
              POP_TOP

443           LOAD_FAST_BORROW         1 (bad_row)
              LOAD_CONST               3 ('final_behavior_state')
              BINARY_OP               26 ([])
              LOAD_CONST               4 ('dropping')
              COMPARE_OP              72 (==)

442   L1:     STORE_FAST               2 (impossible)

444           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (add + NULL|self)

445           LOAD_CONST               5 ('events: impossible-outcome detection logic operates')

446           LOAD_FAST_BORROW         2 (impossible)
              LOAD_CONST               6 ('events')

444           LOAD_CONST               7 (('passed', 'category'))
              CALL_KW                  3
              POP_TOP
              LOAD_CONST               8 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\integrity_check.py", line 454>:
454           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('IntegrityReport')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object run_integrity_checks at 0x0000018C17F63990, file "scripts\integrity_check.py", line 454>:
454           RESUME                   0

455           LOAD_GLOBAL              1 (IntegrityReport + NULL)
              LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR                4 (now)
              PUSH_NULL
              LOAD_GLOBAL              6 (timezone)
              LOAD_ATTR                8 (utc)
              CALL                     1
              LOAD_ATTR               11 (isoformat + NULL|self)
              CALL                     0
              LOAD_CONST               0 (('generated_at',))
              CALL_KW                  1
              STORE_FAST               0 (report)

457           LOAD_GLOBAL             13 (check_normalization_top_level_vs_fallback + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

458           LOAD_GLOBAL             15 (check_get_contract_value_returns_none_for_garbage + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

459           LOAD_GLOBAL             17 (check_full_buyer_lifecycle_replay + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

460           LOAD_GLOBAL             19 (check_evaluator_score_range + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

461           LOAD_GLOBAL             21 (check_evaluator_empty_input + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

462           LOAD_GLOBAL             23 (check_missing_lifecycle_stage_detection + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

463           LOAD_GLOBAL             25 (check_malformed_row_does_not_crash + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

464           LOAD_GLOBAL             27 (check_duplicate_event_id_detection + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

465           LOAD_GLOBAL             29 (check_strategy_registry_ids_unique_and_known + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

466           LOAD_GLOBAL             31 (check_personality_registry_ids_unique_and_known + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

467           LOAD_GLOBAL             33 (check_scenario_personalities_resolve + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

468           LOAD_GLOBAL             35 (check_ranking_is_sorted_and_ranks_consecutive + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

469           LOAD_GLOBAL             37 (check_no_negative_metric_values + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

470           LOAD_GLOBAL             39 (check_behavior_state_in_known_set + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

471           LOAD_GLOBAL             41 (check_outcome_state_consistency + NULL)
              LOAD_FAST_BORROW         0 (report)
              CALL                     1
              POP_TOP

473           LOAD_FAST_BORROW         0 (report)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\integrity_check.py", line 476>:
476           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[list]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17D50FF0, file "scripts\integrity_check.py", line 476>:
 476            RESUME                   0

 477            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 478            LOAD_CONST               0 ('integrity_check')

 479            LOAD_CONST               1 ('PAS143E — offline integrity checker for the substrate.')

 477            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 481            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('--strict')
                LOAD_CONST               4 ('store_true')

 482            LOAD_CONST               5 ('Exit non-zero on any failed check.')

 481            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 483            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               7 ('--json')
                LOAD_CONST               4 ('store_true')

 484            LOAD_CONST               8 ('Emit the report as JSON.')

 483            LOAD_CONST               6 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 485            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 487            LOAD_GLOBAL              9 (run_integrity_checks + NULL)
                CALL                     0
                STORE_FAST               3 (report)

 490            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             10 (os)
                LOAD_ATTR               16 (getcwd)
                PUSH_NULL
                CALL                     0
                LOAD_CONST               9 ('integrity_check_report.json')
                CALL                     2
                STORE_FAST               4 (out_path)

 491            NOP

 492    L1:     LOAD_GLOBAL             19 (open + NULL)
                LOAD_FAST_BORROW         4 (out_path)
                LOAD_CONST              10 ('w')
                LOAD_CONST              11 ('utf-8')
                LOAD_CONST              12 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_FAST               5 (f)

 493            LOAD_GLOBAL             20 (json)
                LOAD_ATTR               22 (dump)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR               25 (to_dict + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW         5 (f)
                LOAD_SMALL_INT           2
                LOAD_CONST              13 (('indent',))
                CALL_KW                  3
                POP_TOP

 492    L3:     LOAD_CONST              14 (None)
                LOAD_CONST              14 (None)
                LOAD_CONST              14 (None)
                CALL                     3
                POP_TOP

 497    L4:     LOAD_FAST                2 (args)
                LOAD_ATTR               20 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       49 (to L5)
                NOT_TAKEN

 498            LOAD_GLOBAL             29 (print + NULL)
                LOAD_GLOBAL             20 (json)
                LOAD_ATTR               34 (dumps)
                PUSH_NULL
                LOAD_FAST                3 (report)
                LOAD_ATTR               25 (to_dict + NULL|self)
                CALL                     0
                LOAD_SMALL_INT           2
                LOAD_CONST              13 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD           212 (to L11)

 500    L5:     LOAD_FAST                3 (report)
                LOAD_ATTR               36 (counts)
                STORE_FAST               7 (c)

 501            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              29 ('========================================================================')
                CALL                     1
                POP_TOP

 502            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              17 ('PAS143E — INTEGRITY CHECK')
                CALL                     1
                POP_TOP

 503            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              18 ('  ')
                LOAD_FAST                7 (c)
                LOAD_CONST              19 ('passed')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              20 ('/')
                LOAD_FAST                7 (c)
                LOAD_CONST              21 ('total')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              22 (' checks passed')
                BUILD_STRING             5
                CALL                     1
                POP_TOP

 504            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              30 ('------------------------------------------------------------------------')
                CALL                     1
                POP_TOP

 505            LOAD_FAST                3 (report)
                LOAD_ATTR               38 (results)
                GET_ITER
        L6:     FOR_ITER                94 (to L10)
                STORE_FAST               8 (r)

 506            LOAD_FAST                8 (r)
                LOAD_ATTR               40 (passed)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_CONST              23 ('PASS')
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST              24 ('FAIL')
        L8:     STORE_FAST               9 (tag)

 507            LOAD_CONST              25 ('  [')
                LOAD_FAST                9 (tag)
                FORMAT_SIMPLE
                LOAD_CONST              26 ('] ')
                LOAD_FAST                8 (r)
                LOAD_ATTR               42 (name)
                FORMAT_SIMPLE
                BUILD_STRING             4
                STORE_FAST              10 (line)

 508            LOAD_FAST                8 (r)
                LOAD_ATTR               44 (detail)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L9)
                NOT_TAKEN

 509            LOAD_FAST               10 (line)
                LOAD_CONST              27 (' — ')
                LOAD_FAST                8 (r)
                LOAD_ATTR               44 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BINARY_OP               13 (+=)
                STORE_FAST              10 (line)

 510    L9:     LOAD_GLOBAL             29 (print + NULL)
                LOAD_FAST               10 (line)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           96 (to L6)

 505   L10:     END_FOR
                POP_ITER

 511            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              29 ('========================================================================')
                CALL                     1
                POP_TOP

 512            LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              28 ('  report: ')
                LOAD_FAST                4 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 514   L11:     LOAD_FAST                2 (args)
                LOAD_ATTR               46 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       21 (to L12)
                NOT_TAKEN
                LOAD_FAST                3 (report)
                LOAD_ATTR               40 (passed)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

 515            LOAD_SMALL_INT           1
                RETURN_VALUE

 516   L12:     LOAD_FAST                3 (report)
                LOAD_ATTR               40 (passed)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
       L13:     LOAD_SMALL_INT           1
                RETURN_VALUE

 492   L14:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L15)
                NOT_TAKEN
                RERAISE                  2
       L15:     POP_TOP
       L16:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
       L17:     EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 355 (to L4)

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 494            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       42 (to L23)
                NOT_TAKEN
                STORE_FAST               6 (e)

 495   L20:     LOAD_GLOBAL             29 (print + NULL)
                LOAD_CONST              15 ('WARNING: could not write report: ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             30 (sys)
                LOAD_ATTR               32 (stderr)
                LOAD_CONST              16 (('file',))
                CALL_KW                  2
                POP_TOP
       L21:     POP_EXCEPT
                LOAD_CONST              14 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 405 (to L4)

  --   L22:     LOAD_CONST              14 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 494   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L19 [0]
  L2 to L3 -> L14 [2] lasti
  L3 to L4 -> L19 [0]
  L14 to L16 -> L18 [4] lasti
  L16 to L17 -> L19 [0]
  L18 to L19 -> L19 [0]
  L19 to L20 -> L24 [1] lasti
  L20 to L21 -> L22 [1] lasti
  L22 to L24 -> L24 [1] lasti
```
