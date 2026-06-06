# replay/__init__

- **pyc:** `app\services\replay\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\replay/__init__.py`
- **co_filename (from bytecode):** `app\services\replay\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** replay

## Module docstring

```
PAS141 — Replay + Evaluation scaffold.

Read-only service that reconstructs a call's conversation and
operational lifecycle from `pas_events` rows. Designed to work whether
or not Settings.PAS_EVENT_CONTRACT_V8_ENABLED is true — the normalizer
prefers v8 top-level columns, then falls back to payload["contract"]
(PAS140D legacy fallback nest), then to event-specific payload keys.

Public surface:
  - event_reader.normalize_event(row)        → unified dict
  - event_reader.get_contract_value(row, k)  → single field with fallback
  - event_reader.load_call_events(call_id)   → chronological events
  - reconstruction.reconstruct_call(events)  → structured replay
  - evaluator.evaluate_reconstruction(rec)   → score + warnings + summary

This is a foundation layer, not PAS Brain. No LLMs. No state mutation.
No I/O outside event_reader.load_call_events (which only reads
pas_events through the existing Supabase client).
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

- '\nPAS141 — Replay + Evaluation scaffold.\n\nRead-only service that reconstructs a call\'s conversation and\noperational lifecycle from `pas_events` rows. Designed to work whether\nor not Settings.PAS_EVENT_CONTRACT_V8_ENABLED is true — the normalizer\nprefers v8 top-level columns, then falls back to payload["contract"]\n(PAS140D legacy fallback nest), then to event-specific payload keys.\n\nPublic surface:\n  - event_reader.normalize_event(row)        → unified dict\n  - event_reader.get_contract_value(row, k)  → single field with fallback\n  - event_reader.load_call_events(call_id)   → chronological events\n  - reconstruction.reconstruct_call(events)  → structured replay\n  - evaluator.evaluate_reconstruction(rec)   → score + warnings + summary\n\nThis is a foundation layer, not PAS Brain. No LLMs. No state mutation.\nNo I/O outside event_reader.load_call_events (which only reads\npas_events through the existing Supabase client).\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS141 — Replay + Evaluation scaffold.\n\nRead-only service that reconstructs a call\'s conversation and\noperational lifecycle from `pas_events` rows. Designed to work whether\nor not Settings.PAS_EVENT_CONTRACT_V8_ENABLED is true — the normalizer\nprefers v8 top-level columns, then falls back to payload["contract"]\n(PAS140D legacy fallback nest), then to event-specific payload keys.\n\nPublic surface:\n  - event_reader.normalize_event(row)        → unified dict\n  - event_reader.get_contract_value(row, k)  → single field with fallback\n  - event_reader.load_call_events(call_id)   → chronological events\n  - reconstruction.reconstruct_call(events)  → structured replay\n  - evaluator.evaluate_reconstruction(rec)   → score + warnings + summary\n\nThis is a foundation layer, not PAS Brain. No LLMs. No state mutation.\nNo I/O outside event_reader.load_call_events (which only reads\npas_events through the existing Supabase client).\n')
              STORE_NAME               0 (__doc__)
              LOAD_CONST               1 (None)
              RETURN_VALUE
```
