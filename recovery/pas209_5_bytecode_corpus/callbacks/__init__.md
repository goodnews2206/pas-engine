# callbacks/__init__

- **pyc:** `app\services\callbacks\__pycache__\__init__.cpython-314.pyc`
- **expected source path (absent):** `app\services\callbacks/__init__.py`
- **co_filename (from bytecode):** `app\services\callbacks\__init__.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** callbacks

## Module docstring

```
PAS170 — Callback lifecycle minimum surface.

Closes the PAS-AUDIT-01 callback gap:
* lead asks "call me back at 3pm";
* PAS records ``callback.requested`` event;
* …nothing reminds the brokerage agent;
* lead waits, gets nothing, blames PAS.

PAS170 ships the **interface** + the in-memory fallback so a
pilot brokerage's operator dashboard can show "you have N
callbacks due in the next hour" before the durable
``pas_callback_schedule`` table (proposal SQL at
``scripts/migrate_v17_callback_schedule.sql``) is promoted.

Public surface intended to be imported only from operator
scripts + (eventually) ``app/routes/portal.py`` callbacks
endpoint:

* ``schedule_callback(...)``            — propose a callback row
* ``list_pending_callbacks(...)``       — operator pending-list
* ``reminder_report(...)``              — "due within next N min"
* ``mark_callback_completed(...)``      — agent dialed lead back
* ``mark_callback_overdue(...)``        — operator-driven cleanup

Hard doctrine carried by every helper here:

* No raw transcript / summary / message text persisted.
* No phone / email / name in any return envelope.
* PAS170 does NOT auto-dial callbacks. Reminder helpers
  surface structural reports only; an outbound dial requires
  the operator-driven worker (PAS162 doctrine intact).
* No Memory Review modification.
```

## Imports

`app.services.callbacks.callback_schedule`, `list_pending_callbacks`, `mark_callback_completed`, `mark_callback_overdue`, `reminder_report`, `reset_callback_registry_for_tests`, `schedule_callback`

## Classes

_none_

## Functions / methods

_none_

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS170 — Callback lifecycle minimum surface.\n\nCloses the PAS-AUDIT-01 callback gap:\n* lead asks "call me back at 3pm";\n* PAS records ``callback.requested`` event;\n* …nothing reminds the brokerage agent;\n* lead waits, gets nothing, blames PAS.\n\nPAS170 ships the **interface** + the in-memory fallback so a\npilot brokerage\'s operator dashboard can show "you have N\ncallbacks due in the next hour" before the durable\n``pas_callback_schedule`` table (proposal SQL at\n``scripts/migrate_v17_callback_schedule.sql``) is promoted.\n\nPublic surface intended to be imported only from operator\nscripts + (eventually) ``app/routes/portal.py`` callbacks\nendpoint:\n\n* ``schedule_callback(...)``            — propose a callback row\n* ``list_pending_callbacks(...)``       — operator pending-list\n* ``reminder_report(...)``              — "due within next N min"\n* ``mark_callback_completed(...)``      — agent dialed lead back\n* ``mark_callback_overdue(...)``        — operator-driven cleanup\n\nHard doctrine carried by every helper here:\n\n* No raw transcript / summary / message text persisted.\n* No phone / email / name in any return envelope.\n* PAS170 does NOT auto-dial callbacks. Reminder helpers\n  surface structural reports only; an outbound dial requires\n  the operator-driven worker (PAS162 doctrine intact).\n* No Memory Review modification.\n'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS170 — Callback lifecycle minimum surface.\n\nCloses the PAS-AUDIT-01 callback gap:\n* lead asks "call me back at 3pm";\n* PAS records ``callback.requested`` event;\n* …nothing reminds the brokerage agent;\n* lead waits, gets nothing, blames PAS.\n\nPAS170 ships the **interface** + the in-memory fallback so a\npilot brokerage\'s operator dashboard can show "you have N\ncallbacks due in the next hour" before the durable\n``pas_callback_schedule`` table (proposal SQL at\n``scripts/migrate_v17_callback_schedule.sql``) is promoted.\n\nPublic surface intended to be imported only from operator\nscripts + (eventually) ``app/routes/portal.py`` callbacks\nendpoint:\n\n* ``schedule_callback(...)``            — propose a callback row\n* ``list_pending_callbacks(...)``       — operator pending-list\n* ``reminder_report(...)``              — "due within next N min"\n* ``mark_callback_completed(...)``      — agent dialed lead back\n* ``mark_callback_overdue(...)``        — operator-driven cleanup\n\nHard doctrine carried by every helper here:\n\n* No raw transcript / summary / message text persisted.\n* No phone / email / name in any return envelope.\n* PAS170 does NOT auto-dial callbacks. Reminder helpers\n  surface structural reports only; an outbound dial requires\n  the operator-driven worker (PAS162 doctrine intact).\n* No Memory Review modification.\n')
              STORE_NAME               0 (__doc__)

 36           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('list_pending_callbacks', 'mark_callback_completed', 'mark_callback_overdue', 'reminder_report', 'reset_callback_registry_for_tests', 'schedule_callback'))
              IMPORT_NAME              1 (app.services.callbacks.callback_schedule)
              IMPORT_FROM              2 (list_pending_callbacks)
              STORE_NAME               2 (list_pending_callbacks)
              IMPORT_FROM              3 (mark_callback_completed)
              STORE_NAME               3 (mark_callback_completed)
              IMPORT_FROM              4 (mark_callback_overdue)
              STORE_NAME               4 (mark_callback_overdue)
              IMPORT_FROM              5 (reminder_report)
              STORE_NAME               5 (reminder_report)
              IMPORT_FROM              6 (reset_callback_registry_for_tests)
              STORE_NAME               6 (reset_callback_registry_for_tests)
              IMPORT_FROM              7 (schedule_callback)
              STORE_NAME               7 (schedule_callback)
              POP_TOP

 46           BUILD_LIST               0
              LOAD_CONST               3 (('schedule_callback', 'list_pending_callbacks', 'reminder_report', 'mark_callback_completed', 'mark_callback_overdue', 'reset_callback_registry_for_tests'))
              LIST_EXTEND              1
              STORE_NAME               8 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE
```
