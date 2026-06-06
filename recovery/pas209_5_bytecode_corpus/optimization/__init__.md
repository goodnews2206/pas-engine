# optimization/__init__

- **pyc:** `app\services\optimization\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\optimization/__init__.py`
- **co_filename (from bytecode):** `app\services\optimization\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** optimization

## Module docstring

```
PAS143A — Comparative optimization framework.

The substrate that PAS Brain (PAS143B+) will eventually use to learn
which operational strategies perform best per brokerage / per scenario.
This phase ships only the deterministic measurement layer:

  StrategyVariant registry → matrix_runner (scenario × strategy) →
  metrics → ranking → report

No LLMs. No PASEngine modification. Strategy "engine_overrides" are
applied through the brokerage dict (the existing safe configuration
seam) — see app/services/simulation/runner.py:run_scenario.

Public surface:
  - strategies.STRATEGIES                          canonical registry
  - strategies.StrategyVariant                     dataclass
  - matrix_runner.run_strategy_matrix(s, st)       grid execution
  - metrics.compute_matrix_metrics(matrix)         pure aggregation
  - ranking.rank_strategies(metrics)               weighted score
  - report.generate_optimization_report(matrix)    one-shot CLI report

PAS143A measures effectiveness honestly: the report records whether
each strategy's overrides actually exercised an engine seam, and warns
if no strategy produced an observable difference yet.
```

## Imports

_none discoverable_

## Classes

_none_

## Functions / methods

_none_

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143A — Comparative optimization framework.\n\nThe substrate that PAS Brain (PAS143B+) will eventually use to learn\nwhich operational strategies perform best per brokerage / per scenario.\nThis phase ships only the deterministic measurement layer:\n\n  StrategyVariant registry → matrix_runner (scenario × strategy) →\n  metrics → ranking → report\n\nNo LLMs. No PASEngine modification. Strategy "engine_overrides" are\napplied through the brokerage dict (the existing safe configuration\nseam) — see app/services/simulation/runner.py:run_scenario.\n\nPublic surface:\n  - strategies.STRATEGIES                          canonical registry\n  - strategies.StrategyVariant                     dataclass\n  - matrix_runner.run_strategy_matrix(s, st)       grid execution\n  - metrics.compute_matrix_metrics(matrix)         pure aggregation\n  - ranking.rank_strategies(metrics)               weighted score\n  - report.generate_optimization_report(matrix)    one-shot CLI report\n\nPAS143A measures effectiveness honestly: the report records whether\neach strategy\'s overrides actually exercised an engine seam, and warns\nif no strategy produced an observable difference yet.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143A — Comparative optimization framework.\n\nThe substrate that PAS Brain (PAS143B+) will eventually use to learn\nwhich operational strategies perform best per brokerage / per scenario.\nThis phase ships only the deterministic measurement layer:\n\n  StrategyVariant registry → matrix_runner (scenario × strategy) →\n  metrics → ranking → report\n\nNo LLMs. No PASEngine modification. Strategy "engine_overrides" are\napplied through the brokerage dict (the existing safe configuration\nseam) — see app/services/simulation/runner.py:run_scenario.\n\nPublic surface:\n  - strategies.STRATEGIES                          canonical registry\n  - strategies.StrategyVariant                     dataclass\n  - matrix_runner.run_strategy_matrix(s, st)       grid execution\n  - metrics.compute_matrix_metrics(matrix)         pure aggregation\n  - ranking.rank_strategies(metrics)               weighted score\n  - report.generate_optimization_report(matrix)    one-shot CLI report\n\nPAS143A measures effectiveness honestly: the report records whether\neach strategy\'s overrides actually exercised an engine seam, and warns\nif no strategy produced an observable difference yet.\n')
              STORE_NAME               0 (__doc__)
              LOAD_CONST               1 (None)
              RETURN_VALUE
```
