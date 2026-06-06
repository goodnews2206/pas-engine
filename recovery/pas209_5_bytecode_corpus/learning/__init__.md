# learning/__init__

- **pyc:** `app\services\learning\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\learning/__init__.py`
- **co_filename (from bytecode):** `app/services/learning/__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** learning

## Module docstring

```
PAS179 — Controlled learning architecture (locked-by-default).

This package contains the controlled-learning surfaces:

* ``learning_policy``     — manual-vs-automatic mode resolution.
* ``scenario_contracts``  — closed deterministic scenario shapes.
* ``outcome_feedback``    — bounded structural feedback scoring.
* ``recommendation_engine`` — CANDIDATE-only generator + persister.
* ``guardrails``          — forbidden-field scanner + safety validators.

PAS179 doctrine:

* **Manual is the default.** Automatic mode is structurally
  representable but locked — no PAS179 helper enables it.
* **No auto-approval.** Recommendations land as ``CANDIDATE``;
  operator transitions them to ``APPROVED_FOR_MANUAL_TEST`` /
  ``REJECTED`` / ``EXPIRED`` through an explicit review path.
* **No live behavior mutation.** Nothing here writes to the
  outbound FSM, memory store, booking engine, or any other
  live PAS surface. PAS179 only produces records.
* **No LLM calls.** Scoring is deterministic.
* **NEVER raises.** All helpers collapse to structural
  envelopes on failure.
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

- 'PAS179 — Controlled learning architecture (locked-by-default).\n\nThis package contains the controlled-learning surfaces:\n\n* ``learning_policy``     — manual-vs-automatic mode resolution.\n* ``scenario_contracts``  — closed deterministic scenario shapes.\n* ``outcome_feedback``    — bounded structural feedback scoring.\n* ``recommendation_engine`` — CANDIDATE-only generator + persister.\n* ``guardrails``          — forbidden-field scanner + safety validators.\n\nPAS179 doctrine:\n\n* **Manual is the default.** Automatic mode is structurally\n  representable but locked — no PAS179 helper enables it.\n* **No auto-approval.** Recommendations land as ``CANDIDATE``;\n  operator transitions them to ``APPROVED_FOR_MANUAL_TEST`` /\n  ``REJECTED`` / ``EXPIRED`` through an explicit review path.\n* **No live behavior mutation.** Nothing here writes to the\n  outbound FSM, memory store, booking engine, or any other\n  live PAS surface. PAS179 only produces records.\n* **No LLM calls.** Scoring is deterministic.\n* **NEVER raises.** All helpers collapse to structural\n  envelopes on failure.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('PAS179 — Controlled learning architecture (locked-by-default).\n\nThis package contains the controlled-learning surfaces:\n\n* ``learning_policy``     — manual-vs-automatic mode resolution.\n* ``scenario_contracts``  — closed deterministic scenario shapes.\n* ``outcome_feedback``    — bounded structural feedback scoring.\n* ``recommendation_engine`` — CANDIDATE-only generator + persister.\n* ``guardrails``          — forbidden-field scanner + safety validators.\n\nPAS179 doctrine:\n\n* **Manual is the default.** Automatic mode is structurally\n  representable but locked — no PAS179 helper enables it.\n* **No auto-approval.** Recommendations land as ``CANDIDATE``;\n  operator transitions them to ``APPROVED_FOR_MANUAL_TEST`` /\n  ``REJECTED`` / ``EXPIRED`` through an explicit review path.\n* **No live behavior mutation.** Nothing here writes to the\n  outbound FSM, memory store, booking engine, or any other\n  live PAS surface. PAS179 only produces records.\n* **No LLM calls.** Scoring is deterministic.\n* **NEVER raises.** All helpers collapse to structural\n  envelopes on failure.\n')
              STORE_NAME               0 (__doc__)
              LOAD_CONST               1 (None)
              RETURN_VALUE
```
