# monitoring/__init__

- **pyc:** `app\services\monitoring\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/__init__.py`
- **co_filename (from bytecode):** `app\services\monitoring\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS143F1 — Monitoring contracts package.

Contains ONLY constants + dataclasses describing the alert shape PAS
will emit once the monitoring runtime lands in PAS143F2. No engine,
no dispatcher, no I/O. Importing this package must have zero
side effects.

Usage (from PAS143F2 onwards):

    from app.services.monitoring.contracts import (
        Alert, Severity, Category,
    )

    alert = Alert(
        id="alert_xxx",
        category=Category.TENANT_ISOLATION,
        severity=Severity.HIGH,
        title="Cross-tenant read attempted",
        description="Caller invoked recent_events without brokerage_id "
                    "and without allow_unscoped.",
        source="app.services.intelligence.queries",
    )
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

- '\nPAS143F1 — Monitoring contracts package.\n\nContains ONLY constants + dataclasses describing the alert shape PAS\nwill emit once the monitoring runtime lands in PAS143F2. No engine,\nno dispatcher, no I/O. Importing this package must have zero\nside effects.\n\nUsage (from PAS143F2 onwards):\n\n    from app.services.monitoring.contracts import (\n        Alert, Severity, Category,\n    )\n\n    alert = Alert(\n        id="alert_xxx",\n        category=Category.TENANT_ISOLATION,\n        severity=Severity.HIGH,\n        title="Cross-tenant read attempted",\n        description="Caller invoked recent_events without brokerage_id "\n                    "and without allow_unscoped.",\n        source="app.services.intelligence.queries",\n    )\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS143F1 — Monitoring contracts package.\n\nContains ONLY constants + dataclasses describing the alert shape PAS\nwill emit once the monitoring runtime lands in PAS143F2. No engine,\nno dispatcher, no I/O. Importing this package must have zero\nside effects.\n\nUsage (from PAS143F2 onwards):\n\n    from app.services.monitoring.contracts import (\n        Alert, Severity, Category,\n    )\n\n    alert = Alert(\n        id="alert_xxx",\n        category=Category.TENANT_ISOLATION,\n        severity=Severity.HIGH,\n        title="Cross-tenant read attempted",\n        description="Caller invoked recent_events without brokerage_id "\n                    "and without allow_unscoped.",\n        source="app.services.intelligence.queries",\n    )\n')
              STORE_NAME               0 (__doc__)
              LOAD_CONST               1 (None)
              RETURN_VALUE
```
