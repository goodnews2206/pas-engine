# outbound/__init__

- **pyc:** `app\services\outbound\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\outbound/__init__.py`
- **co_filename (from bytecode):** `app\services\outbound\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** outbound

## Module docstring

```
PAS163 — Outbound dial adapter package.

Exposes ``place_outbound_call`` so callers (worker, replay seed,
operator scripts) can place real Twilio outbound calls without
forging a FastAPI request against ``app/routes/outbound.py``.

The adapter is additive and never weakens the existing
``POST /outbound/call`` route. It reuses the same Twilio client
shape but is reachable as a plain function.
```

## Imports

`app.services.outbound.dial`, `place_outbound_call`

## Classes

_none_

## Functions / methods

_none_

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS163 — Outbound dial adapter package.\n\nExposes ``place_outbound_call`` so callers (worker, replay seed,\noperator scripts) can place real Twilio outbound calls without\nforging a FastAPI request against ``app/routes/outbound.py``.\n\nThe adapter is additive and never weakens the existing\n``POST /outbound/call`` route. It reuses the same Twilio client\nshape but is reachable as a plain function.\n'
- 'place_outbound_call'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS163 — Outbound dial adapter package.\n\nExposes ``place_outbound_call`` so callers (worker, replay seed,\noperator scripts) can place real Twilio outbound calls without\nforging a FastAPI request against ``app/routes/outbound.py``.\n\nThe adapter is additive and never weakens the existing\n``POST /outbound/call`` route. It reuses the same Twilio client\nshape but is reachable as a plain function.\n')
              STORE_NAME               0 (__doc__)

 13           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('place_outbound_call',))
              IMPORT_NAME              1 (app.services.outbound.dial)
              IMPORT_FROM              2 (place_outbound_call)
              STORE_NAME               2 (place_outbound_call)
              POP_TOP

 15           LOAD_CONST               2 ('place_outbound_call')
              BUILD_LIST               1
              STORE_NAME               3 (__all__)
              LOAD_CONST               3 (None)
              RETURN_VALUE
```
