# worker/__init__

- **pyc:** `app\services\worker\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\worker/__init__.py`
- **co_filename (from bytecode):** `app/services/worker\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** worker

## Module docstring

```
PAS172 — worker package.

Holds the durable-heartbeat service + monitor surfaces. Imports
are intentionally minimal so the PAS162 worker.py module (which
lives at app/services/ingestion/worker.py) can opt in to
heartbeat writes without dragging the heartbeat package into
the FastAPI startup path.
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

- 'PAS172 — worker package.\n\nHolds the durable-heartbeat service + monitor surfaces. Imports\nare intentionally minimal so the PAS162 worker.py module (which\nlives at app/services/ingestion/worker.py) can opt in to\nheartbeat writes without dragging the heartbeat package into\nthe FastAPI startup path.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('PAS172 — worker package.\n\nHolds the durable-heartbeat service + monitor surfaces. Imports\nare intentionally minimal so the PAS162 worker.py module (which\nlives at app/services/ingestion/worker.py) can opt in to\nheartbeat writes without dragging the heartbeat package into\nthe FastAPI startup path.\n')
              STORE_NAME               0 (__doc__)
              LOAD_CONST               1 (None)
              RETURN_VALUE
```
