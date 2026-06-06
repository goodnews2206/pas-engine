# callbacks/callback_schedule

- **pyc:** `app\services\callbacks\__pycache__\callback_schedule.cpython-314.pyc`
- **expected source path (absent):** `app\services\callbacks/callback_schedule.py`
- **co_filename (from bytecode):** `app/services/callbacks/callback_schedule.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** callbacks

## Module docstring

```
PAS170 — Callback schedule service (process-local v1).

**PAS171 update:** each public helper now consults the
durable Supabase store first
(:mod:`app.services.callbacks.callback_schedule_store`). The
durable layer's ``status="ok"`` answer is authoritative; a
``status="warning"`` (DB unavailable) falls back to the
process-local registry below, mirroring the PAS166 ↔ PAS165
fallback for email dedupe. The public surface is unchanged
— callers still see the same closed-shape envelope, just
without the ``callback_schedule_store_is_process_local``
warning when the durable layer wins.

Operator-facing minimum viable surface:

* ``schedule_callback(brokerage_id, source_call_id, scheduled_for, ...)``
* ``list_pending_callbacks(brokerage_id, *, status="PENDING", limit=50)``
* ``reminder_report(brokerage_id, *, lookahead_minutes=60, now=None)``
* ``mark_callback_completed(callback_id, brokerage_id, *, completed_by=None)``
* ``mark_callback_overdue(callback_id, brokerage_id)``
* ``reset_callback_registry_for_tests()``

Doctrine carried by every helper here:

* Tenant-scoped. Every read + write is keyed by
  ``brokerage_id`` (resolved at the route layer from auth,
  never from a payload).
* No raw transcript / summary / message text persisted.
  ``source_call_id`` is the operator's pointer back to the
  source call record; PII lives there, not here.
* No phone / email / name in any return envelope.
* PAS170 does NOT auto-dial callbacks. Reminder helpers
  surface structural reports only — the operator chooses
  whether to fire a Slack alert or trigger an outbound dial
  via the PAS162 worker. The PAS162 worker default-OFF
  semantics are unchanged.
* Process-local registry (``_CALLBACK_REGISTRY``) with
  explicit ``callback_schedule_store_is_process_local``
  warning on every read / write so the operator dashboard
  can count "we are running on the fallback".
* Cross-restart durability is a follow-on phase (PAS171+).
  This module ships the **interface** + the in-memory
  fallback so a pilot operator dashboard works today; the
  durable backing table is the proposal SQL at
  ``scripts/migrate_v17_callback_schedule.sql``.
* Every public helper is non-raising.

Closed status enum (mirrors the SQL CHECK constraint):
``PENDING | REMINDED | COMPLETED | OVERDUE | CANCELLED | FAILED``.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.callbacks.callback_schedule_store`, `datetime`, `durable_callback_schedule_enabled`, `durable_reminder_report`, `list_durable_callbacks`, `logging`, `mark_durable_callback_cancelled`, `mark_durable_callback_completed`, `mark_durable_callback_failed`, `mark_durable_callback_overdue`, `mark_durable_callback_reminded`, `register_durable_callback`, `threading`, `timedelta`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_clamp_window`, `_coerce_scheduled_for`, `_durable_unavailable`, `_iso`, `_now_dt`, `_peek_callback_registry_for_tests`, `_project_durable`, `_project_durable_list`, `_project_durable_transition`, `_structural_row`, `_try_durable_transition`, `_update_status`, `list_pending_callbacks`, `mark_callback_completed`, `mark_callback_overdue`, `reminder_report`, `reset_callback_registry_for_tests`, `schedule_callback`

## Env-key candidates

`COMPLETED`, `OVERDUE`, `PENDING`

## String constants (redacted where noted)

- '\nPAS170 — Callback schedule service (process-local v1).\n\n**PAS171 update:** each public helper now consults the\ndurable Supabase store first\n(:mod:`app.services.callbacks.callback_schedule_store`). The\ndurable layer\'s ``status="ok"`` answer is authoritative; a\n``status="warning"`` (DB unavailable) falls back to the\nprocess-local registry below, mirroring the PAS166 ↔ PAS165\nfallback for email dedupe. The public surface is unchanged\n— callers still see the same closed-shape envelope, just\nwithout the ``callback_schedule_store_is_process_local``\nwarning when the durable layer wins.\n\nOperator-facing minimum viable surface:\n\n* ``schedule_callback(brokerage_id, source_call_id, scheduled_for, ...)``\n* ``list_pending_callbacks(brokerage_id, *, status="PENDING", limit=50)``\n* ``reminder_report(brokerage_id, *, lookahead_minutes=60, now=None)``\n* ``mark_callback_completed(callback_id, brokerage_id, *, completed_by=None)``\n* ``mark_callback_overdue(callback_id, brokerage_id)``\n* ``reset_callback_registry_for_tests()``\n\nDoctrine carried by every helper here:\n\n* Tenant-scoped. Every read + write is keyed by\n  ``brokerage_id`` (resolved at the route layer from auth,\n  never from a payload).\n* No raw transcript / summary / message text persisted.\n  ``source_call_id`` is the operator\'s pointer back to the\n  source call record; PII lives there, not here.\n* No phone / email / name in any return envelope.\n* PAS170 does NOT auto-dial callbacks. Reminder helpers\n  surface structural reports only — the operator chooses\n  whether to fire a Slack alert or trigger an outbound dial\n  via the PAS162 worker. The PAS162 worker default-OFF\n  semantics are unchanged.\n* Process-local registry (``_CALLBACK_REGISTRY``) with\n  explicit ``callback_schedule_store_is_process_local``\n  warning on every read / write so the operator dashboard\n  can count "we are running on the fallback".\n* Cross-restart durability is a follow-on phase (PAS171+).\n  This module ships the **interface** + the in-memory\n  fallback so a pilot operator dashboard works today; the\n  durable backing table is the proposal SQL at\n  ``scripts/migrate_v17_callback_schedule.sql``.\n* Every public helper is non-raising.\n\nClosed status enum (mirrors the SQL CHECK constraint):\n``PENDING | REMINDED | COMPLETED | OVERDUE | CANCELLED | FAILED``.\n'
- 'pas.callbacks.schedule'
- 'PENDING'
- 'Dict[str, Dict[str, Any]]'
- '_CALLBACK_REGISTRY'
- 'window_minutes'
- 'now'
- 'status'
- 'limit'
- 'lookahead_minutes'
- 'completed_by'
- 'error_code'
- 'bump_reminder'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'value'
- 'Optional[datetime]'
- 'int'
- 'row'
- 'Dict[str, Any]'
- 'Project an internal row dict into the closed-shape\noperator envelope. NEVER includes raw lead context.'
- 'callback_id'
- 'brokerage_id'
- 'source_call_id'
- 'scheduled_for'
- 'reminder_sent_count'
- 'last_reminder_at'
- 'completed_at'
- 'last_error_code'
- 'created_at'
- 'updated_at'
- 'env'
- 'Translate a durable-store envelope (lower-case status) to\nthe legacy PAS170 envelope shape (upper-case status). The\ndurable envelope already has the closed-shape columns; we\nupper-case the status for backward compat and surface the\n``…_store_is_durable`` warning so the operator dashboard\ncan confirm we are on the durable path.'
- 'warnings'
- 'callback'
- 'callback_schedule_store_is_durable'
- 'bool'
- "Return True if the durable envelope means 'fall back'."
- 'warning'
- 'durable_callback_schedule_unavailable'
- 'Optional[str]'
- 'Record a pending callback. Durable Supabase store is the\nprimary path; the process-local registry is the fallback.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":   "ok" | "failed",\n      "callback": <structural row> | None,\n      "warnings": [<structural tokens>],\n      "error_code": None | "<structural token>",\n    }\n\nNEVER raises. NEVER stores any raw lead context — only the\npointer ``source_call_id``.\n'
- 'schedule_callback durable register error type='
- 'callback_schedule_store_is_process_local'
- 'failed'
- 'missing_brokerage_id'
- 'missing_source_call_id'
- 'invalid_scheduled_for'
- 'last_error_at'
- 'callback_scheduled id='
- ' brokerage='
- ' source_call='
- ' scheduled_for='
- 'Translate a durable list-envelope into the legacy\nlist-envelope shape, upper-casing per-row statuses.'
- 'filter_status'
- 'count'
- 'callbacks'
- 'Return the brokerage\'s callback rows filtered by status,\nsorted by ``scheduled_for`` ASC.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":       "ok" | "failed",\n      "brokerage_id": "...",\n      "filter_status": "<closed enum>",\n      "limit":        int,\n      "count":        int,\n      "callbacks":    [<structural row>, ...],\n      "warnings":     [<structural tokens>],\n      "error_code":   None | "<structural token>",\n    }\n\nNEVER raises. NEVER includes raw lead context.\n'
- 'invalid_status_filter'
- 'list_pending_callbacks durable list error type='
- 'Return the brokerage\'s PENDING callbacks whose\n``scheduled_for`` falls within the next\n``lookahead_minutes`` window.\n\nPAS170 does NOT fire any external notification (Slack /\nSMS / email) from this helper. The operator dashboard\npolls this report and chooses how to surface it.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":            "ok" | "failed",\n      "brokerage_id":      "...",\n      "lookahead_minutes": int,\n      "now":               "<iso>",\n      "due_count":         int,\n      "due":               [<structural row>, ...],\n      "overdue_count":     int,\n      "overdue":           [<structural row>, ...],\n      "warnings":          [<structural tokens>],\n      "error_code":        None | "<structural token>",\n    }\n\nNEVER raises. NEVER auto-dials.\n'
- 'due_count'
- 'due'
- 'overdue_count'
- 'overdue'
- 'reminder_report durable read error type='
- 'rows'
- 'List[Dict[str, Any]]'
- 'new_status'
- 'missing_callback_id'
- 'invalid_status'
- 'callback_not_found_or_cross_tenant'
- 'COMPLETED'
- 'operator'
- 'Optional[Dict[str, Any]]'
- 'Try the durable transition path. Returns a projected\nenvelope on durable success, ``None`` when the caller\nshould fall back to process-local. NEVER raises.'
- 'completed'
- 'reminded'
- 'cancelled'
- '_try_durable_transition error type='
- 'denv'
- 'Translate durable transition envelope to the legacy\nupper-cased shape.'
- 'Operator action: agent dialed the lead back. Closes the\ncallback row. NEVER raises.'
- 'Operator (or reminder helper) marks a pending callback\nas overdue when its window has passed without action.\nNEVER raises.'
- 'OVERDUE'
- 'callback_window_passed'
- 'None'
- 'Test-only helper to flush the registry between tests.'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS170 — Callback schedule service (process-local v1).\n\n**PAS171 update:** each public helper now consults the\ndurable Supabase store first\n(:mod:`app.services.callbacks.callback_schedule_store`). The\ndurable layer\'s ``status="ok"`` answer is authoritative; a\n``status="warning"`` (DB unavailable) falls back to the\nprocess-local registry below, mirroring the PAS166 ↔ PAS165\nfallback for email dedupe. The public surface is unchanged\n— callers still see the same closed-shape envelope, just\nwithout the ``callback_schedule_store_is_process_local``\nwarning when the durable layer wins.\n\nOperator-facing minimum viable surface:\n\n* ``schedule_callback(brokerage_id, source_call_id, scheduled_for, ...)``\n* ``list_pending_callbacks(brokerage_id, *, status="PENDING", limit=50)``\n* ``reminder_report(brokerage_id, *, lookahead_minutes=60, now=None)``\n* ``mark_callback_completed(callback_id, brokerage_id, *, completed_by=None)``\n* ``mark_callback_overdue(callback_id, brokerage_id)``\n* ``reset_callback_registry_for_tests()``\n\nDoctrine carried by every helper here:\n\n* Tenant-scoped. Every read + write is keyed by\n  ``brokerage_id`` (resolved at the route layer from auth,\n  never from a payload).\n* No raw transcript / summary / message text persisted.\n  ``source_call_id`` is the operator\'s pointer back to the\n  source call record; PII lives there, not here.\n* No phone / email / name in any return envelope.\n* PAS170 does NOT auto-dial callbacks. Reminder helpers\n  surface structural reports only — the operator chooses\n  whether to fire a Slack alert or trigger an outbound dial\n  via the PAS162 worker. The PAS162 worker default-OFF\n  semantics are unchanged.\n* Process-local registry (``_CALLBACK_REGISTRY``) with\n  explicit ``callback_schedule_store_is_process_local``\n  warning on every read / write so the operator dashboard\n  can count "we are running on the fallback".\n* Cross-restart durability is a follow-on phase (PAS171+).\n  This module ships the **interface** + the in-memory\n  fallback so a pilot operator dashboard works today; the\n  durable backing table is the proposal SQL at\n  ``scripts/migrate_v17_callback_schedule.sql``.\n* Every public helper is non-raising.\n\nClosed status enum (mirrors the SQL CHECK constraint):\n``PENDING | REMINDED | COMPLETED | OVERDUE | CANCELLED | FAILED``.\n')
               STORE_NAME               1 (__doc__)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (threading)
               STORE_NAME               5 (threading)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (uuid)
               STORE_NAME               6 (uuid)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timedelta)
               STORE_NAME               8 (timedelta)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  59           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
               IMPORT_NAME             10 (typing)
               IMPORT_FROM             11 (Any)
               STORE_NAME              11 (Any)
               IMPORT_FROM             12 (Dict)
               STORE_NAME              12 (Dict)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               POP_TOP

  62           LOAD_NAME                4 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.callbacks.schedule')
               CALL                     1
               STORE_NAME              16 (logger)

  69           LOAD_CONST              56 (('PENDING', 'REMINDED', 'COMPLETED', 'OVERDUE', 'CANCELLED', 'FAILED'))
               STORE_NAME              17 (ALLOWED_CALLBACK_STATUSES)

  74           LOAD_SMALL_INT          15
               STORE_NAME              18 (DEFAULT_WINDOW_MINUTES)

  75           LOAD_SMALL_INT          60
               STORE_NAME              19 (DEFAULT_REMINDER_LOOKAHEAD_MINUTES)

  77           LOAD_SMALL_INT         200
               STORE_NAME              20 (_LIST_HARD_CAP)

  87           BUILD_MAP                0
               STORE_NAME              21 (_CALLBACK_REGISTRY)
               LOAD_CONST               7 ('Dict[str, Dict[str, Any]]')
               LOAD_NAME               22 (__annotations__)
               LOAD_CONST               8 ('_CALLBACK_REGISTRY')
               STORE_SUBSCR

  88           LOAD_NAME                5 (threading)
               LOAD_ATTR               46 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              24 (_CALLBACK_LOCK)

  91           LOAD_CONST              57 ((None,))
               LOAD_CONST               9 (<code object __annotate__ at 0x0000018C17FA2010, file "app/services/callbacks/callback_schedule.py", line 91>)
               MAKE_FUNCTION
               LOAD_CONST              10 (<code object _now_dt at 0x0000018C17D6DFC0, file "app/services/callbacks/callback_schedule.py", line 91>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              25 (_now_dt)

 107           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/callbacks/callback_schedule.py", line 107>)
               MAKE_FUNCTION
               LOAD_CONST              12 (<code object _iso at 0x0000018C18025030, file "app/services/callbacks/callback_schedule.py", line 107>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              26 (_iso)

 111           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2A60, file "app/services/callbacks/callback_schedule.py", line 111>)
               MAKE_FUNCTION
               LOAD_CONST              14 (<code object _coerce_scheduled_for at 0x0000018C17EDEBC0, file "app/services/callbacks/callback_schedule.py", line 111>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_coerce_scheduled_for)

 127           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2C40, file "app/services/callbacks/callback_schedule.py", line 127>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _clamp_window at 0x0000018C17FE13E0, file "app/services/callbacks/callback_schedule.py", line 127>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_clamp_window)

 139           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2D30, file "app/services/callbacks/callback_schedule.py", line 139>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _clamp_limit at 0x0000018C17972550, file "app/services/callbacks/callback_schedule.py", line 139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_clamp_limit)

 151           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2E20, file "app/services/callbacks/callback_schedule.py", line 151>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _structural_row at 0x0000018C1821ECE0, file "app/services/callbacks/callback_schedule.py", line 151>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_structural_row)

 175           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3000, file "app/services/callbacks/callback_schedule.py", line 175>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _project_durable at 0x0000018C17ED9FB0, file "app/services/callbacks/callback_schedule.py", line 175>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_project_durable)

 202           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/callbacks/callback_schedule.py", line 202>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _durable_unavailable at 0x0000018C17F95CF0, file "app/services/callbacks/callback_schedule.py", line 202>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_durable_unavailable)

 213           LOAD_CONST              25 ('window_minutes')

 218           LOAD_NAME               18 (DEFAULT_WINDOW_MINUTES)

 213           LOAD_CONST              26 ('now')

 219           LOAD_CONST               2 (None)

 213           BUILD_MAP                2
               LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18024C30, file "app/services/callbacks/callback_schedule.py", line 213>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object schedule_callback at 0x0000018C17F7C780, file "app/services/callbacks/callback_schedule.py", line 213>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              33 (schedule_callback)

 336           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA1D40, file "app/services/callbacks/callback_schedule.py", line 336>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object _project_durable_list at 0x0000018C17D3C0E0, file "app/services/callbacks/callback_schedule.py", line 336>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_project_durable_list)

 363           LOAD_CONST              31 ('status')

 366           LOAD_CONST               6 ('PENDING')

 363           LOAD_CONST              32 ('limit')

 367           LOAD_SMALL_INT          50

 363           BUILD_MAP                2
               LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18024B30, file "app/services/callbacks/callback_schedule.py", line 363>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object list_pending_callbacks at 0x0000018C17F7D0A0, file "app/services/callbacks/callback_schedule.py", line 363>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              35 (list_pending_callbacks)

 459           LOAD_CONST              35 ('lookahead_minutes')

 462           LOAD_NAME               19 (DEFAULT_REMINDER_LOOKAHEAD_MINUTES)

 459           LOAD_CONST              26 ('now')

 463           LOAD_CONST               2 (None)

 459           BUILD_MAP                2
               LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18024D30, file "app/services/callbacks/callback_schedule.py", line 459>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object reminder_report at 0x0000018C17F7E310, file "app/services/callbacks/callback_schedule.py", line 459>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (reminder_report)

 602           LOAD_CONST              38 ('completed_by')

 607           LOAD_CONST               2 (None)

 602           LOAD_CONST              39 ('error_code')

 608           LOAD_CONST               2 (None)

 602           LOAD_CONST              40 ('bump_reminder')

 609           LOAD_CONST              41 (False)

 602           LOAD_CONST              26 ('now')

 610           LOAD_CONST               2 (None)

 602           BUILD_MAP                4
               LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18090580, file "app/services/callbacks/callback_schedule.py", line 602>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object _update_status at 0x0000018C17EA6FA0, file "app/services/callbacks/callback_schedule.py", line 602>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (_update_status)

 672           LOAD_CONST              38 ('completed_by')

 677           LOAD_CONST               2 (None)

 672           LOAD_CONST              26 ('now')

 678           LOAD_CONST               2 (None)

 672           BUILD_MAP                2
               LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18024E30, file "app/services/callbacks/callback_schedule.py", line 672>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object _try_durable_transition at 0x0000018C17F7F180, file "app/services/callbacks/callback_schedule.py", line 672>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_try_durable_transition)

 729           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18024F30, file "app/services/callbacks/callback_schedule.py", line 729>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object _project_durable_transition at 0x0000018C17F7F440, file "app/services/callbacks/callback_schedule.py", line 729>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_project_durable_transition)

 752           LOAD_CONST              38 ('completed_by')

 756           LOAD_CONST               2 (None)

 752           LOAD_CONST              26 ('now')

 757           LOAD_CONST               2 (None)

 752           BUILD_MAP                2
               LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025530, file "app/services/callbacks/callback_schedule.py", line 752>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object mark_callback_completed at 0x0000018C18053630, file "app/services/callbacks/callback_schedule.py", line 752>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (mark_callback_completed)

 773           LOAD_CONST              26 ('now')

 777           LOAD_CONST               2 (None)

 773           BUILD_MAP                1
               LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18025830, file "app/services/callbacks/callback_schedule.py", line 773>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object mark_callback_overdue at 0x0000018C180532D0, file "app/services/callbacks/callback_schedule.py", line 773>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (mark_callback_overdue)

 800           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA25B0, file "app/services/callbacks/callback_schedule.py", line 800>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object reset_callback_registry_for_tests at 0x0000018C17972D90, file "app/services/callbacks/callback_schedule.py", line 800>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (reset_callback_registry_for_tests)

 806           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA26A0, file "app/services/callbacks/callback_schedule.py", line 806>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object _peek_callback_registry_for_tests at 0x0000018C17FA92F0, file "app/services/callbacks/callback_schedule.py", line 806>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_peek_callback_registry_for_tests)

 811           BUILD_LIST               0
               LOAD_CONST              58 (('ALLOWED_CALLBACK_STATUSES', 'DEFAULT_WINDOW_MINUTES', 'DEFAULT_REMINDER_LOOKAHEAD_MINUTES', 'schedule_callback', 'list_pending_callbacks', 'reminder_report', 'mark_callback_completed', 'mark_callback_overdue', 'reset_callback_registry_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              44 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "app/services/callbacks/callback_schedule.py", line 91>:
 91           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C17D6DFC0, file "app/services/callbacks/callback_schedule.py", line 91>:
  91            RESUME                   0

  92            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

  93            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

  94            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

  95    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  96    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

  97            NOP

  98    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

  99            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 100            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 101    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 104    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 102            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 103    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

 102    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/callbacks/callback_schedule.py", line 107>:
107           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iso at 0x0000018C18025030, file "app/services/callbacks/callback_schedule.py", line 107>:
107           RESUME                   0

108           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app/services/callbacks/callback_schedule.py", line 111>:
111           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[datetime]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_scheduled_for at 0x0000018C17EDEBC0, file "app/services/callbacks/callback_schedule.py", line 111>:
 111            RESUME                   0

 112            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

 113            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

 114            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

 115    L1:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

 116    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      139 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

 117            NOP

 118    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               18 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

 119            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 120            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 121    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 124    L6:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 122            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 123    L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 122    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app/services/callbacks/callback_schedule.py", line 127>:
127           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_window at 0x0000018C17FE13E0, file "app/services/callbacks/callback_schedule.py", line 127>:
 127           RESUME                   0

 128           NOP

 129   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 132   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 133           LOAD_SMALL_INT           1
               RETURN_VALUE

 134   L3:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT         240
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 135           LOAD_SMALL_INT         240
               RETURN_VALUE

 136   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 130           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 131           LOAD_GLOBAL              6 (DEFAULT_WINDOW_MINUTES)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 130   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app/services/callbacks/callback_schedule.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17972550, file "app/services/callbacks/callback_schedule.py", line 139>:
 139           RESUME                   0

 140           NOP

 141   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 144   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 145           LOAD_SMALL_INT           1
               RETURN_VALUE

 146   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              6 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 147           LOAD_GLOBAL              6 (_LIST_HARD_CAP)
               RETURN_VALUE

 148   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 142           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 143   L6:     POP_EXCEPT
               LOAD_SMALL_INT          50
               RETURN_VALUE

 142   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app/services/callbacks/callback_schedule.py", line 151>:
151           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _structural_row at 0x0000018C1821ECE0, file "app/services/callbacks/callback_schedule.py", line 151>:
151           RESUME                   0

155           LOAD_CONST               1 ('callback_id')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('callback_id')
              CALL                     1

156           LOAD_CONST               2 ('brokerage_id')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('brokerage_id')
              CALL                     1

157           LOAD_CONST               3 ('source_call_id')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('source_call_id')
              CALL                     1

158           LOAD_CONST               4 ('scheduled_for')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('scheduled_for')
              CALL                     1

159           LOAD_CONST               5 ('window_minutes')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('window_minutes')
              CALL                     1

160           LOAD_CONST               6 ('status')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               6 ('status')
              CALL                     1

161           LOAD_CONST               7 ('reminder_sent_count')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               7 ('reminder_sent_count')
              LOAD_SMALL_INT           0
              CALL                     2

162           LOAD_CONST               8 ('last_reminder_at')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               8 ('last_reminder_at')
              CALL                     1

163           LOAD_CONST               9 ('completed_at')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               9 ('completed_at')
              CALL                     1

164           LOAD_CONST              10 ('completed_by')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              10 ('completed_by')
              CALL                     1

165           LOAD_CONST              11 ('last_error_code')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              11 ('last_error_code')
              CALL                     1

166           LOAD_CONST              12 ('created_at')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              12 ('created_at')
              CALL                     1

167           LOAD_CONST              13 ('updated_at')
              LOAD_FAST_BORROW         0 (row)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              13 ('updated_at')
              CALL                     1

154           BUILD_MAP               13
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "app/services/callbacks/callback_schedule.py", line 175>:
175           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_durable at 0x0000018C17ED9FB0, file "app/services/callbacks/callback_schedule.py", line 175>:
175           RESUME                   0

183           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('ok')
              CALL                     2

184           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

185           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('error_code')
              CALL                     1

182           BUILD_MAP                3
              STORE_FAST               1 (out)

187           LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('callback')
              CALL                     1
              STORE_FAST               2 (cb)

188           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (cb)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       75 (to L3)
              NOT_TAKEN

189           LOAD_GLOBAL              7 (dict + NULL)
              LOAD_FAST_BORROW         2 (cb)
              CALL                     1
              STORE_FAST               2 (cb)

190           LOAD_FAST_BORROW         2 (cb)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              STORE_FAST               3 (st)

191           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (st)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       20 (to L2)
              NOT_TAKEN

192           LOAD_FAST_BORROW         3 (st)
              LOAD_ATTR               11 (upper + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         2 (cb)
              LOAD_CONST               1 ('status')
              STORE_SUBSCR

193   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (cb, out)
              LOAD_CONST               5 ('callback')
              STORE_SUBSCR
              JUMP_FORWARD             5 (to L4)

195   L3:     LOAD_CONST               6 (None)
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               5 ('callback')
              STORE_SUBSCR

197   L4:     LOAD_CONST               7 ('callback_schedule_store_is_durable')
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               3 ('warnings')
              BINARY_OP               26 ([])
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       25 (to L5)
              NOT_TAKEN

198           LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               3 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_CONST               7 ('callback_schedule_store_is_durable')
              CALL                     1
              POP_TOP

199   L5:     LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/callbacks/callback_schedule.py", line 202>:
202           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _durable_unavailable at 0x0000018C17F95CF0, file "app/services/callbacks/callback_schedule.py", line 202>:
202           RESUME                   0

204           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

205           LOAD_CONST               1 (True)
              RETURN_VALUE

206   L1:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('status')
              CALL                     1
              LOAD_CONST               3 ('warning')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

207           LOAD_CONST               1 (True)
              RETURN_VALUE

208   L2:     LOAD_FAST_BORROW         0 (env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               4 ('error_code')
              CALL                     1
              LOAD_CONST               5 ('durable_callback_schedule_unavailable')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

209           LOAD_CONST               1 (True)
              RETURN_VALUE

210   L3:     LOAD_CONST               6 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app/services/callbacks/callback_schedule.py", line 213>:
213           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

215           LOAD_CONST               2 ('Optional[str]')

213           LOAD_CONST               3 ('source_call_id')

216           LOAD_CONST               2 ('Optional[str]')

213           LOAD_CONST               4 ('scheduled_for')

217           LOAD_CONST               5 ('Any')

213           LOAD_CONST               6 ('window_minutes')

218           LOAD_CONST               5 ('Any')

213           LOAD_CONST               7 ('now')

219           LOAD_CONST               5 ('Any')

213           LOAD_CONST               8 ('return')

220           LOAD_CONST               9 ('Dict[str, Any]')

213           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object schedule_callback at 0x0000018C17F7C780, file "app/services/callbacks/callback_schedule.py", line 213>:
 213            RESUME                   0

 237            NOP

 238    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('durable_callback_schedule_enabled', 'register_durable_callback'))
                IMPORT_NAME              0 (app.services.callbacks.callback_schedule_store)
                IMPORT_FROM              1 (durable_callback_schedule_enabled)
                STORE_FAST               5 (durable_callback_schedule_enabled)
                IMPORT_FROM              2 (register_durable_callback)
                STORE_FAST               6 (register_durable_callback)
                POP_TOP

 242            LOAD_FAST_BORROW         5 (durable_callback_schedule_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L5)
        L2:     NOT_TAKEN

 243    L3:     LOAD_FAST_BORROW         6 (register_durable_callback)
                PUSH_NULL

 244            LOAD_FAST_BORROW         0 (brokerage_id)

 245            LOAD_FAST_BORROW         1 (source_call_id)

 246            LOAD_FAST_BORROW         2 (scheduled_for)

 247            LOAD_FAST_BORROW         3 (window_minutes)

 248            LOAD_FAST_BORROW         4 (now)

 243            LOAD_CONST               2 (('brokerage_id', 'source_call_id', 'scheduled_for', 'window_minutes', 'now'))
                CALL_KW                  5
                STORE_FAST               7 (denv)

 250            LOAD_GLOBAL              7 (_durable_unavailable + NULL)
                LOAD_FAST_BORROW         7 (denv)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L5)
                NOT_TAKEN

 251            LOAD_GLOBAL              9 (_project_durable + NULL)
                LOAD_FAST_BORROW         7 (denv)
                CALL                     1
        L4:     RETURN_VALUE

 258    L5:     LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1
                STORE_FAST               9 (warnings)

 262            LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                0 (brokerage_id)
                LOAD_GLOBAL             22 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L6)
                NOT_TAKEN
                LOAD_FAST                0 (brokerage_id)
                LOAD_ATTR               25 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L6)
                NOT_TAKEN

 261            LOAD_FAST                0 (brokerage_id)
                LOAD_ATTR               25 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L7)

 263    L6:     LOAD_CONST               4 (None)

 260    L7:     STORE_FAST              10 (bid)

 265            LOAD_FAST               10 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L8)
                NOT_TAKEN

 267            LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('failed')

 268            LOAD_CONST               8 ('callback')
                LOAD_CONST               4 (None)

 269            LOAD_CONST               9 ('warnings')
                LOAD_FAST                9 (warnings)

 270            LOAD_CONST              10 ('error_code')
                LOAD_CONST              11 ('missing_brokerage_id')

 266            BUILD_MAP                4
                RETURN_VALUE

 275    L8:     LOAD_GLOBAL             21 (isinstance + NULL)
                LOAD_FAST                1 (source_call_id)
                LOAD_GLOBAL             22 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L9)
                NOT_TAKEN
                LOAD_FAST                1 (source_call_id)
                LOAD_ATTR               25 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L9)
                NOT_TAKEN

 274            LOAD_FAST                1 (source_call_id)
                LOAD_ATTR               25 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L10)

 276    L9:     LOAD_CONST               4 (None)

 273   L10:     STORE_FAST              11 (sid)

 278            LOAD_FAST               11 (sid)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L11)
                NOT_TAKEN

 280            LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('failed')

 281            LOAD_CONST               8 ('callback')
                LOAD_CONST               4 (None)

 282            LOAD_CONST               9 ('warnings')
                LOAD_FAST                9 (warnings)

 283            LOAD_CONST              10 ('error_code')
                LOAD_CONST              12 ('missing_source_call_id')

 279            BUILD_MAP                4
                RETURN_VALUE

 286   L11:     LOAD_GLOBAL             27 (_coerce_scheduled_for + NULL)
                LOAD_FAST                2 (scheduled_for)
                CALL                     1
                STORE_FAST              12 (sched_dt)

 287            LOAD_FAST               12 (sched_dt)
                POP_JUMP_IF_NOT_NONE    11 (to L12)
                NOT_TAKEN

 289            LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('failed')

 290            LOAD_CONST               8 ('callback')
                LOAD_CONST               4 (None)

 291            LOAD_CONST               9 ('warnings')
                LOAD_FAST                9 (warnings)

 292            LOAD_CONST              10 ('error_code')
                LOAD_CONST              13 ('invalid_scheduled_for')

 288            BUILD_MAP                4
                RETURN_VALUE

 295   L12:     LOAD_GLOBAL             29 (_clamp_window + NULL)
                LOAD_FAST                3 (window_minutes)
                CALL                     1
                STORE_FAST              13 (win)

 296            LOAD_GLOBAL             31 (_now_dt + NULL)
                LOAD_FAST                4 (now)
                CALL                     1
                STORE_FAST              14 (now_dt)

 297            LOAD_GLOBAL             33 (_iso + NULL)
                LOAD_FAST               14 (now_dt)
                CALL                     1
                STORE_FAST              15 (iso_now)

 298            LOAD_GLOBAL             23 (str + NULL)
                LOAD_GLOBAL             34 (uuid)
                LOAD_ATTR               36 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1
                STORE_FAST              16 (callback_id)

 301            LOAD_CONST              14 ('callback_id')
                LOAD_FAST               16 (callback_id)

 302            LOAD_CONST              15 ('brokerage_id')
                LOAD_FAST               10 (bid)

 303            LOAD_CONST              16 ('source_call_id')
                LOAD_FAST               11 (sid)

 304            LOAD_CONST              17 ('scheduled_for')
                LOAD_GLOBAL             33 (_iso + NULL)
                LOAD_FAST               12 (sched_dt)
                CALL                     1

 305            LOAD_CONST              18 ('window_minutes')
                LOAD_FAST               13 (win)

 306            LOAD_CONST               6 ('status')
                LOAD_CONST              19 ('PENDING')

 307            LOAD_CONST              20 ('reminder_sent_count')
                LOAD_SMALL_INT           0

 308            LOAD_CONST              21 ('last_reminder_at')
                LOAD_CONST               4 (None)

 309            LOAD_CONST              22 ('completed_at')
                LOAD_CONST               4 (None)

 310            LOAD_CONST              23 ('completed_by')
                LOAD_CONST               4 (None)

 311            LOAD_CONST              24 ('last_error_code')
                LOAD_CONST               4 (None)

 312            LOAD_CONST              25 ('last_error_at')
                LOAD_CONST               4 (None)

 313            LOAD_CONST              26 ('created_at')
                LOAD_FAST               15 (iso_now)

 314            LOAD_CONST              27 ('updated_at')
                LOAD_FAST               15 (iso_now)

 300            BUILD_MAP               14
                STORE_FAST              17 (row)

 316            LOAD_GLOBAL             38 (_CALLBACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L13:     POP_TOP

 317            LOAD_FAST               17 (row)
                LOAD_GLOBAL             40 (_CALLBACK_REGISTRY)
                LOAD_FAST               16 (callback_id)
                STORE_SUBSCR

 316   L14:     LOAD_CONST               4 (None)
                LOAD_CONST               4 (None)
                LOAD_CONST               4 (None)
                CALL                     3
                POP_TOP

 319   L15:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               43 (info + NULL|self)

 320            LOAD_CONST              28 ('callback_scheduled id=')
                LOAD_FAST               16 (callback_id)
                FORMAT_SIMPLE
                LOAD_CONST              29 (' brokerage=')

 321            LOAD_FAST               10 (bid)
                FORMAT_SIMPLE
                LOAD_CONST              30 (' source_call=')
                LOAD_FAST               11 (sid)
                FORMAT_SIMPLE
                LOAD_CONST              31 (' scheduled_for=')

 322            LOAD_FAST               17 (row)
                LOAD_CONST              17 ('scheduled_for')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE

 320            BUILD_STRING             8

 319            CALL                     1
                POP_TOP

 325            LOAD_CONST               6 ('status')
                LOAD_CONST              32 ('ok')

 326            LOAD_CONST               8 ('callback')
                LOAD_GLOBAL             45 (_structural_row + NULL)
                LOAD_FAST               17 (row)
                CALL                     1

 327            LOAD_CONST               9 ('warnings')
                LOAD_FAST                9 (warnings)

 328            LOAD_CONST              10 ('error_code')
                LOAD_CONST               4 (None)

 324            BUILD_MAP                4
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 252            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L20)
                NOT_TAKEN
                STORE_FAST               8 (e)

 253   L17:     LOAD_GLOBAL             12 (logger)
                LOAD_ATTR               15 (warning + NULL|self)

 254            LOAD_CONST               3 ('schedule_callback durable register error type=')

 255            LOAD_GLOBAL             17 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               18 (__name__)
                FORMAT_SIMPLE

 254            BUILD_STRING             2

 253            CALL                     1
                POP_TOP
       L18:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 441 (to L5)

  --   L19:     LOAD_CONST               4 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 252   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 316   L22:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L23)
                NOT_TAKEN
                RERAISE                  2
       L23:     POP_TOP
       L24:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 143 (to L15)

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L16 [0]
  L3 to L4 -> L16 [0]
  L13 to L14 -> L22 [2] lasti
  L16 to L17 -> L21 [1] lasti
  L17 to L18 -> L19 [1] lasti
  L19 to L21 -> L21 [1] lasti
  L22 to L24 -> L25 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app/services/callbacks/callback_schedule.py", line 336>:
336           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_durable_list at 0x0000018C17D3C0E0, file "app/services/callbacks/callback_schedule.py", line 336>:
336            RESUME                   0

340            LOAD_CONST               1 ('status')
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('status')
               CALL                     1

341            LOAD_CONST               2 ('brokerage_id')
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('brokerage_id')
               CALL                     1

342            LOAD_CONST               3 ('filter_status')

343            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('filter_status')
               CALL                     1
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       42 (to L2)
               NOT_TAKEN

342            LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('filter_status')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     LOAD_ATTR                7 (upper + NULL|self)
               CALL                     0
               JUMP_FORWARD            16 (to L3)

344    L2:     LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               3 ('filter_status')
               CALL                     1

345    L3:     LOAD_CONST               5 ('limit')
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               5 ('limit')
               CALL                     1

346            LOAD_CONST               6 ('count')
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               6 ('count')
               CALL                     1

347            LOAD_CONST               7 ('callbacks')
               BUILD_LIST               0

348            LOAD_CONST               8 ('warnings')
               LOAD_GLOBAL              9 (list + NULL)
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               8 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L4:     CALL                     1

349            LOAD_CONST               9 ('error_code')
               LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               9 ('error_code')
               CALL                     1

339            BUILD_MAP                8
               STORE_FAST               1 (out)

351            LOAD_FAST_BORROW         0 (env)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               7 ('callbacks')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L5:     GET_ITER
       L6:     FOR_ITER               120 (to L9)
               STORE_FAST               2 (cb)

352            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         2 (cb)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L6)

353    L7:     LOAD_GLOBAL             11 (dict + NULL)
               LOAD_FAST_BORROW         2 (cb)
               CALL                     1
               STORE_FAST               3 (row)

354            LOAD_FAST_BORROW         3 (row)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               1 ('status')
               CALL                     1
               STORE_FAST               4 (st)

355            LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (st)
               LOAD_GLOBAL              4 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN

356            LOAD_FAST_BORROW         4 (st)
               LOAD_ATTR                7 (upper + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         3 (row)
               LOAD_CONST               1 ('status')
               STORE_SUBSCR

357    L8:     LOAD_FAST_BORROW         1 (out)
               LOAD_CONST               7 ('callbacks')
               BINARY_OP               26 ([])
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         3 (row)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          122 (to L6)

351    L9:     END_FOR
               POP_ITER

358            LOAD_CONST              10 ('callback_schedule_store_is_durable')
               LOAD_FAST_BORROW         1 (out)
               LOAD_CONST               8 ('warnings')
               BINARY_OP               26 ([])
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

359            LOAD_FAST_BORROW         1 (out)
               LOAD_CONST               8 ('warnings')
               BINARY_OP               26 ([])
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_CONST              10 ('callback_schedule_store_is_durable')
               CALL                     1
               POP_TOP

360   L10:     LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app/services/callbacks/callback_schedule.py", line 363>:
363           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

364           LOAD_CONST               2 ('Optional[str]')

363           LOAD_CONST               3 ('status')

366           LOAD_CONST               4 ('str')

363           LOAD_CONST               5 ('limit')

367           LOAD_CONST               6 ('Any')

363           LOAD_CONST               7 ('return')

368           LOAD_CONST               8 ('Dict[str, Any]')

363           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_pending_callbacks at 0x0000018C17F7D0A0, file "app/services/callbacks/callback_schedule.py", line 363>:
 363            RESUME                   0

 389            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 388            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 390    L1:     LOAD_CONST               1 (None)

 387    L2:     STORE_FAST               3 (bid)

 392            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        29 (to L3)
                NOT_TAKEN

 394            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 395            LOAD_CONST               4 ('brokerage_id')
                LOAD_CONST               1 (None)

 396            LOAD_CONST               5 ('filter_status')
                LOAD_FAST_BORROW         1 (status)

 397            LOAD_CONST               6 ('limit')
                LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 398            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 399            LOAD_CONST               8 ('callbacks')
                BUILD_LIST               0

 400            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 401            LOAD_CONST              11 ('error_code')
                LOAD_CONST              12 ('missing_brokerage_id')

 393            BUILD_MAP                8
                RETURN_VALUE

 403    L3:     LOAD_FAST_BORROW         1 (status)
                LOAD_GLOBAL              8 (ALLOWED_CALLBACK_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L4)
                NOT_TAKEN

 405            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 406            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 407            LOAD_CONST               5 ('filter_status')
                LOAD_FAST_BORROW         1 (status)

 408            LOAD_CONST               6 ('limit')
                LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 409            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 410            LOAD_CONST               8 ('callbacks')
                BUILD_LIST               0

 411            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 412            LOAD_CONST              11 ('error_code')
                LOAD_CONST              13 ('invalid_status_filter')

 404            BUILD_MAP                8
                RETURN_VALUE

 415    L4:     NOP

 416    L5:     LOAD_SMALL_INT           0
                LOAD_CONST              14 (('durable_callback_schedule_enabled', 'list_durable_callbacks'))
                IMPORT_NAME              5 (app.services.callbacks.callback_schedule_store)
                IMPORT_FROM              6 (durable_callback_schedule_enabled)
                STORE_FAST               4 (durable_callback_schedule_enabled)
                IMPORT_FROM              7 (list_durable_callbacks)
                STORE_FAST               5 (list_durable_callbacks)
                POP_TOP

 420            LOAD_FAST_BORROW         4 (durable_callback_schedule_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       53 (to L9)
        L6:     NOT_TAKEN

 421    L7:     LOAD_FAST_BORROW         5 (list_durable_callbacks)
                PUSH_NULL

 422            LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (bid, status)
                LOAD_ATTR               17 (lower + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW         2 (limit)

 421            LOAD_CONST              15 (('status', 'limit'))
                CALL_KW                  3
                STORE_FAST               6 (denv)

 424            LOAD_GLOBAL             19 (_durable_unavailable + NULL)
                LOAD_FAST_BORROW         6 (denv)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L9)
                NOT_TAKEN

 425            LOAD_GLOBAL             21 (_project_durable_list + NULL)
                LOAD_FAST_BORROW         6 (denv)
                CALL                     1
        L8:     RETURN_VALUE

 432    L9:     LOAD_GLOBAL              7 (_clamp_limit + NULL)
                LOAD_FAST                2 (limit)
                CALL                     1
                STORE_FAST               8 (capped)

 433            LOAD_GLOBAL             32 (_CALLBACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L10:     POP_TOP

 436            LOAD_GLOBAL             34 (_CALLBACK_REGISTRY)
                LOAD_ATTR               37 (values + NULL|self)
                CALL                     0
                GET_ITER

 434            LOAD_FAST_AND_CLEAR      9 (r)
                SWAP                     2
       L11:     BUILD_LIST               0
                SWAP                     2

 436   L12:     FOR_ITER                86 (to L19)
                STORE_FAST               9 (r)

 437            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST                9 (r)
                LOAD_GLOBAL             38 (dict)
                CALL                     2
                TO_BOOL

 435   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L12)

 438   L14:     LOAD_FAST                9 (r)
                LOAD_ATTR               41 (get + NULL|self)
                LOAD_CONST               4 ('brokerage_id')
                CALL                     1
                LOAD_FAST                3 (bid)
                COMPARE_OP              88 (bool(==))

 435   L15:     POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           51 (to L12)

 439   L16:     LOAD_FAST                9 (r)
                LOAD_ATTR               41 (get + NULL|self)
                LOAD_CONST               2 ('status')
                CALL                     1
                LOAD_FAST                1 (status)
                COMPARE_OP              88 (bool(==))

 435   L17:     POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                JUMP_BACKWARD           75 (to L12)
       L18:     LOAD_GLOBAL             43 (_structural_row + NULL)
                LOAD_FAST                9 (r)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           88 (to L12)

 436   L19:     END_FOR
                POP_ITER

 434   L20:     STORE_FAST              10 (rows)
                STORE_FAST               9 (r)

 433   L21:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 441   L22:     LOAD_FAST_CHECK         10 (rows)
                LOAD_ATTR               45 (sort + NULL|self)
                LOAD_CONST              17 (<code object <lambda> at 0x0000018C18090140, file "app/services/callbacks/callback_schedule.py", line 441>)
                MAKE_FUNCTION
                LOAD_CONST              18 (('key',))
                CALL_KW                  1
                POP_TOP

 442            LOAD_FAST               10 (rows)
                LOAD_CONST               1 (None)
                LOAD_FAST                8 (capped)
                BINARY_SLICE
                STORE_FAST              10 (rows)

 444            LOAD_CONST               2 ('status')
                LOAD_CONST              19 ('ok')

 445            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                3 (bid)

 446            LOAD_CONST               5 ('filter_status')
                LOAD_FAST                1 (status)

 447            LOAD_CONST               6 ('limit')
                LOAD_FAST                8 (capped)

 448            LOAD_CONST               7 ('count')
                LOAD_GLOBAL             47 (len + NULL)
                LOAD_FAST               10 (rows)
                CALL                     1

 449            LOAD_CONST               8 ('callbacks')
                LOAD_FAST               10 (rows)

 450            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 451            LOAD_CONST              11 ('error_code')
                LOAD_CONST               1 (None)

 443            BUILD_MAP                8
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 426            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L27)
                NOT_TAKEN
                STORE_FAST               7 (e)

 427   L24:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 428            LOAD_CONST              16 ('list_pending_callbacks durable list error type=')

 429            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 428            BUILD_STRING             2

 427            CALL                     1
                POP_TOP
       L25:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 262 (to L9)

  --   L26:     LOAD_CONST               1 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 426   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     SWAP                     2
                POP_TOP

 434            SWAP                     2
                STORE_FAST               9 (r)
                RERAISE                  0

 433   L30:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L31)
                NOT_TAKEN
                RERAISE                  2
       L31:     POP_TOP
       L32:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 141 (to L22)

  --   L33:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L23 [0]
  L7 to L8 -> L23 [0]
  L10 to L11 -> L30 [2] lasti
  L11 to L13 -> L29 [4]
  L14 to L15 -> L29 [4]
  L16 to L17 -> L29 [4]
  L18 to L20 -> L29 [4]
  L20 to L21 -> L30 [2] lasti
  L23 to L24 -> L28 [1] lasti
  L24 to L25 -> L26 [1] lasti
  L26 to L28 -> L28 [1] lasti
  L29 to L30 -> L30 [2] lasti
  L30 to L32 -> L33 [4] lasti

Disassembly of <code object <lambda> at 0x0000018C18090140, file "app/services/callbacks/callback_schedule.py", line 441>:
441           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('scheduled_for')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app/services/callbacks/callback_schedule.py", line 459>:
459           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

460           LOAD_CONST               2 ('Optional[str]')

459           LOAD_CONST               3 ('lookahead_minutes')

462           LOAD_CONST               4 ('Any')

459           LOAD_CONST               5 ('now')

463           LOAD_CONST               4 ('Any')

459           LOAD_CONST               6 ('return')

464           LOAD_CONST               7 ('Dict[str, Any]')

459           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object reminder_report at 0x0000018C17F7E310, file "app/services/callbacks/callback_schedule.py", line 459>:
 459            RESUME                   0

 492            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L1)
                NOT_TAKEN

 491            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L2)

 493    L1:     LOAD_CONST               1 (None)

 490    L2:     STORE_FAST               3 (bid)

 495            NOP

 496    L3:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         1 (lookahead_minutes)
                CALL                     1
                STORE_FAST               4 (lookahead)

 499    L4:     LOAD_FAST_BORROW         4 (lookahead)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 500            LOAD_SMALL_INT           1
                STORE_FAST               4 (lookahead)

 501    L5:     LOAD_FAST_BORROW         4 (lookahead)
                LOAD_CONST              28 (1440)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN

 502            LOAD_CONST              28 (1440)
                STORE_FAST               4 (lookahead)

 504    L6:     LOAD_GLOBAL             15 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               5 (now_dt)

 505            LOAD_FAST_BORROW         5 (now_dt)
                LOAD_GLOBAL             17 (timedelta + NULL)
                LOAD_FAST_BORROW         4 (lookahead)
                LOAD_CONST               2 (('minutes',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST               6 (upper)

 507            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L7)
                NOT_TAKEN

 509            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 510            LOAD_CONST               5 ('brokerage_id')
                LOAD_CONST               1 (None)

 511            LOAD_CONST               6 ('lookahead_minutes')
                LOAD_FAST_BORROW         4 (lookahead)

 512            LOAD_CONST               7 ('now')
                LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_FAST_BORROW         5 (now_dt)
                CALL                     1

 513            LOAD_CONST               8 ('due_count')
                LOAD_SMALL_INT           0

 514            LOAD_CONST               9 ('due')
                BUILD_LIST               0

 515            LOAD_CONST              10 ('overdue_count')
                LOAD_SMALL_INT           0

 516            LOAD_CONST              11 ('overdue')
                BUILD_LIST               0

 517            LOAD_CONST              12 ('warnings')
                LOAD_CONST              13 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 518            LOAD_CONST              14 ('error_code')
                LOAD_CONST              15 ('missing_brokerage_id')

 508            BUILD_MAP               10
                RETURN_VALUE

 522    L7:     NOP

 523    L8:     LOAD_SMALL_INT           0
                LOAD_CONST              16 (('durable_callback_schedule_enabled', 'durable_reminder_report'))
                IMPORT_NAME             10 (app.services.callbacks.callback_schedule_store)
                IMPORT_FROM             11 (durable_callback_schedule_enabled)
                STORE_FAST               7 (durable_callback_schedule_enabled)
                IMPORT_FROM             12 (durable_reminder_report)
                STORE_FAST               8 (durable_reminder_report)
                POP_TOP

 527            LOAD_FAST_BORROW         7 (durable_callback_schedule_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      254 (to L19)
        L9:     NOT_TAKEN

 528   L10:     LOAD_FAST_BORROW         8 (durable_reminder_report)
                PUSH_NULL

 529            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (bid, lookahead)
                LOAD_FAST_BORROW         2 (now)

 528            LOAD_CONST              17 (('lookahead_minutes', 'now'))
                CALL_KW                  3
                STORE_FAST               9 (denv)

 531            LOAD_GLOBAL             27 (_durable_unavailable + NULL)
                LOAD_FAST_BORROW         9 (denv)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE       227 (to L19)
                NOT_TAKEN

 533            LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA23D0, file "app/services/callbacks/callback_schedule.py", line 533>)
                MAKE_FUNCTION
                LOAD_CONST              19 (<code object _u at 0x0000018C1801C410, file "app/services/callbacks/callback_schedule.py", line 533>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_FAST              10 (_u)

 543            LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              12 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                BUILD_LIST               0
       L13:     CALL                     1
                STORE_FAST              11 (warnings)

 544            LOAD_CONST              20 ('callback_schedule_store_is_durable')
                LOAD_FAST_BORROW        11 (warnings)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       18 (to L14)
                NOT_TAKEN

 545            LOAD_FAST_BORROW        11 (warnings)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_CONST              20 ('callback_schedule_store_is_durable')
                CALL                     1
                POP_TOP

 547   L14:     LOAD_CONST               3 ('status')
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1

 548            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                3 (bid)

 549            LOAD_CONST               6 ('lookahead_minutes')
                LOAD_FAST                4 (lookahead)

 550            LOAD_CONST               7 ('now')
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               7 ('now')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_FAST_BORROW         5 (now_dt)
                CALL                     1

 551   L17:     LOAD_CONST               8 ('due_count')
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               8 ('due_count')
                LOAD_SMALL_INT           0
                CALL                     2

 552            LOAD_CONST               9 ('due')
                LOAD_FAST_BORROW        10 (_u)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               9 ('due')
                CALL                     1
                CALL                     1

 553            LOAD_CONST              10 ('overdue_count')
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              10 ('overdue_count')
                LOAD_SMALL_INT           0
                CALL                     2

 554            LOAD_CONST              11 ('overdue')
                LOAD_FAST_BORROW        10 (_u)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              11 ('overdue')
                CALL                     1
                CALL                     1

 555            LOAD_CONST              12 ('warnings')
                LOAD_FAST_BORROW        11 (warnings)

 556            LOAD_CONST              14 ('error_code')
                LOAD_FAST_BORROW         9 (denv)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              14 ('error_code')
                CALL                     1

 546            BUILD_MAP               10
       L18:     RETURN_VALUE

 564   L19:     BUILD_LIST               0
                STORE_FAST              13 (due)

 565            BUILD_LIST               0
                STORE_FAST              14 (overdue)

 566            LOAD_GLOBAL             44 (_CALLBACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L20:     POP_TOP

 567            LOAD_GLOBAL             46 (_CALLBACK_REGISTRY)
                LOAD_ATTR               49 (values + NULL|self)
                CALL                     0
                GET_ITER
       L21:     FOR_ITER               177 (to L29)
                STORE_FAST              15 (row)

 568            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST               15 (row)
                LOAD_GLOBAL             50 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L22)
                NOT_TAKEN

 569            JUMP_BACKWARD           27 (to L21)

 570   L22:     LOAD_FAST               15 (row)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1
                LOAD_FAST                3 (bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L23)
                NOT_TAKEN

 571            JUMP_BACKWARD           51 (to L21)

 572   L23:     LOAD_FAST               15 (row)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               3 ('status')
                CALL                     1
                LOAD_CONST              22 ('PENDING')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN

 573            JUMP_BACKWARD           75 (to L21)

 574   L24:     LOAD_GLOBAL             53 (_coerce_scheduled_for + NULL)
                LOAD_FAST               15 (row)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              23 ('scheduled_for')
                CALL                     1
                CALL                     1
                STORE_FAST              16 (sched)

 575            LOAD_FAST               16 (sched)
                POP_JUMP_IF_NOT_NONE     3 (to L25)
                NOT_TAKEN

 576            JUMP_BACKWARD          107 (to L21)

 577   L25:     LOAD_FAST               16 (sched)
                LOAD_FAST                5 (now_dt)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       29 (to L26)
                NOT_TAKEN

 578            LOAD_FAST               14 (overdue)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_GLOBAL             55 (_structural_row + NULL)
                LOAD_FAST               15 (row)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          142 (to L21)

 579   L26:     LOAD_FAST               16 (sched)
                LOAD_FAST                6 (upper)
                COMPARE_OP              58 (bool(<=))
       L27:     POP_JUMP_IF_TRUE         3 (to L28)
                NOT_TAKEN
                JUMP_BACKWARD          151 (to L21)

 580   L28:     LOAD_FAST               13 (due)
                LOAD_ATTR               33 (append + NULL|self)
                LOAD_GLOBAL             55 (_structural_row + NULL)
                LOAD_FAST               15 (row)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          179 (to L21)

 567   L29:     END_FOR
                POP_ITER

 566   L30:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP

 581   L31:     LOAD_FAST               13 (due)
                LOAD_ATTR               57 (sort + NULL|self)
                LOAD_CONST              24 (<code object <lambda> at 0x0000018C18090250, file "app/services/callbacks/callback_schedule.py", line 581>)
                MAKE_FUNCTION
                LOAD_CONST              25 (('key',))
                CALL_KW                  1
                POP_TOP

 582            LOAD_FAST               14 (overdue)
                LOAD_ATTR               57 (sort + NULL|self)
                LOAD_CONST              26 (<code object <lambda> at 0x0000018C18090360, file "app/services/callbacks/callback_schedule.py", line 582>)
                MAKE_FUNCTION
                LOAD_CONST              25 (('key',))
                CALL_KW                  1
                POP_TOP

 585            LOAD_CONST               3 ('status')
                LOAD_CONST              27 ('ok')

 586            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                3 (bid)

 587            LOAD_CONST               6 ('lookahead_minutes')
                LOAD_FAST                4 (lookahead)

 588            LOAD_CONST               7 ('now')
                LOAD_GLOBAL             19 (_iso + NULL)
                LOAD_FAST                5 (now_dt)
                CALL                     1

 589            LOAD_CONST               8 ('due_count')
                LOAD_GLOBAL             59 (len + NULL)
                LOAD_FAST               13 (due)
                CALL                     1

 590            LOAD_CONST               9 ('due')
                LOAD_FAST               13 (due)

 591            LOAD_CONST              10 ('overdue_count')
                LOAD_GLOBAL             59 (len + NULL)
                LOAD_FAST               14 (overdue)
                CALL                     1

 592            LOAD_CONST              11 ('overdue')
                LOAD_FAST               14 (overdue)

 593            LOAD_CONST              12 ('warnings')
                LOAD_CONST              13 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 594            LOAD_CONST              14 ('error_code')
                LOAD_CONST               1 (None)

 584            BUILD_MAP               10
                RETURN_VALUE

  --   L32:     PUSH_EXC_INFO

 497            LOAD_GLOBAL              8 (TypeError)
                LOAD_GLOBAL             10 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L34)
                NOT_TAKEN
                POP_TOP

 498            LOAD_GLOBAL             12 (DEFAULT_REMINDER_LOOKAHEAD_MINUTES)
                STORE_FAST               4 (lookahead)
       L33:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 705 (to L4)

 497   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L36:     PUSH_EXC_INFO

 558            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L40)
                NOT_TAKEN
                STORE_FAST              12 (e)

 559   L37:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 560            LOAD_CONST              21 ('reminder_report durable read error type=')

 561            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 560            BUILD_STRING             2

 559            CALL                     1
                POP_TOP
       L38:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 406 (to L19)

  --   L39:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 558   L40:     RERAISE                  0

  --   L41:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 566   L42:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L43)
                NOT_TAKEN
                RERAISE                  2
       L43:     POP_TOP
       L44:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 202 (to L31)

  --   L45:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L32 [0]
  L8 to L9 -> L36 [0]
  L10 to L11 -> L36 [0]
  L12 to L15 -> L36 [0]
  L16 to L18 -> L36 [0]
  L20 to L27 -> L42 [2] lasti
  L28 to L30 -> L42 [2] lasti
  L32 to L33 -> L35 [1] lasti
  L34 to L35 -> L35 [1] lasti
  L36 to L37 -> L41 [1] lasti
  L37 to L38 -> L39 [1] lasti
  L39 to L41 -> L41 [1] lasti
  L42 to L44 -> L45 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app/services/callbacks/callback_schedule.py", line 533>:
533           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _u at 0x0000018C1801C410, file "app/services/callbacks/callback_schedule.py", line 533>:
533           RESUME                   0

534           BUILD_LIST               0
              STORE_FAST               1 (out)

535           LOAD_FAST                0 (rows)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     GET_ITER
      L2:     FOR_ITER               118 (to L5)
              STORE_FAST               2 (r)

536           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (r)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

537           JUMP_BACKWARD           27 (to L2)

538   L3:     LOAD_GLOBAL              3 (dict + NULL)
              LOAD_FAST_BORROW         2 (r)
              CALL                     1
              STORE_FAST               3 (rr)

539           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (rr)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       27 (to L4)
              NOT_TAKEN

540           LOAD_FAST_BORROW         3 (rr)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_ATTR                9 (upper + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         3 (rr)
              LOAD_CONST               0 ('status')
              STORE_SUBSCR

541   L4:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_FAST_BORROW         3 (rr)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          120 (to L2)

535   L5:     END_FOR
              POP_ITER

542           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18090250, file "app/services/callbacks/callback_schedule.py", line 581>:
581           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('scheduled_for')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     RETURN_VALUE

Disassembly of <code object <lambda> at 0x0000018C18090360, file "app/services/callbacks/callback_schedule.py", line 582>:
582           RESUME                   0
              LOAD_FAST_BORROW         0 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('scheduled_for')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090580, file "app/services/callbacks/callback_schedule.py", line 602>:
602           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

603           LOAD_CONST               2 ('Optional[str]')

602           LOAD_CONST               3 ('brokerage_id')

604           LOAD_CONST               2 ('Optional[str]')

602           LOAD_CONST               4 ('new_status')

606           LOAD_CONST               5 ('str')

602           LOAD_CONST               6 ('completed_by')

607           LOAD_CONST               2 ('Optional[str]')

602           LOAD_CONST               7 ('error_code')

608           LOAD_CONST               2 ('Optional[str]')

602           LOAD_CONST               8 ('bump_reminder')

609           LOAD_CONST               9 ('bool')

602           LOAD_CONST              10 ('now')

610           LOAD_CONST              11 ('Any')

602           LOAD_CONST              12 ('return')

611           LOAD_CONST              13 ('Dict[str, Any]')

602           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _update_status at 0x0000018C17EA6FA0, file "app/services/callbacks/callback_schedule.py", line 602>:
 602            RESUME                   0

 612            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (callback_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (callback_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L2)
                NOT_TAKEN

 614    L1:     LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 615            LOAD_CONST               2 ('callback_id')
                LOAD_CONST               3 (None)

 616            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 617            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('missing_callback_id')

 613            BUILD_MAP                4
                RETURN_VALUE

 619    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L4)
                NOT_TAKEN

 621    L3:     LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 622            LOAD_CONST               2 ('callback_id')
                LOAD_FAST_BORROW         0 (callback_id)

 623            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 624            LOAD_CONST               6 ('error_code')
                LOAD_CONST               8 ('missing_brokerage_id')

 620            BUILD_MAP                4
                RETURN_VALUE

 626    L4:     LOAD_FAST_BORROW         2 (new_status)
                LOAD_GLOBAL              6 (ALLOWED_CALLBACK_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       12 (to L5)
                NOT_TAKEN

 628            LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 629            LOAD_CONST               2 ('callback_id')
                LOAD_FAST_BORROW         0 (callback_id)

 630            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 631            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('invalid_status')

 627            BUILD_MAP                4
                RETURN_VALUE

 633    L5:     LOAD_FAST_BORROW         0 (callback_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (cid)

 634            LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               8 (bid)

 635            LOAD_GLOBAL              9 (_now_dt + NULL)
                LOAD_FAST_BORROW         6 (now)
                CALL                     1
                STORE_FAST               9 (now_dt)

 636            LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         9 (now_dt)
                CALL                     1
                STORE_FAST              10 (iso_now)

 637            LOAD_GLOBAL             12 (_CALLBACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L6:     POP_TOP

 638            LOAD_GLOBAL             14 (_CALLBACK_REGISTRY)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_FAST_BORROW         7 (cid)
                CALL                     1
                STORE_FAST              11 (row)

 639            LOAD_FAST_BORROW        11 (row)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L7)
                NOT_TAKEN
                LOAD_FAST_BORROW        11 (row)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              10 ('brokerage_id')
                CALL                     1
                LOAD_FAST_BORROW         8 (bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       22 (to L9)
                NOT_TAKEN

 641    L7:     LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 642            LOAD_CONST               2 ('callback_id')
                LOAD_FAST_BORROW         7 (cid)

 643            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 644            LOAD_CONST               6 ('error_code')
                LOAD_CONST              11 ('callback_not_found_or_cross_tenant')

 640            BUILD_MAP                4

 637    L8:     SWAP                     3
                SWAP                     2
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

 646    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 43 (new_status, row)
                LOAD_CONST               0 ('status')
                STORE_SUBSCR

 647            LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (iso_now, row)
                LOAD_CONST              12 ('updated_at')
                STORE_SUBSCR

 648            LOAD_FAST_BORROW         2 (new_status)
                LOAD_CONST              13 ('COMPLETED')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       70 (to L14)
                NOT_TAKEN

 649            LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (iso_now, row)
                LOAD_CONST              14 ('completed_at')
                STORE_SUBSCR

 652            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (completed_by)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (completed_by)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L12)
       L10:     NOT_TAKEN

 651   L11:     LOAD_FAST_BORROW         3 (completed_by)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L13)

 653   L12:     LOAD_CONST              15 ('operator')

 650   L13:     LOAD_FAST_BORROW        11 (row)
                LOAD_CONST              16 ('completed_by')
                STORE_SUBSCR

 655   L14:     LOAD_FAST_BORROW         5 (bump_reminder)
                TO_BOOL
                POP_JUMP_IF_FALSE       51 (to L20)
       L15:     NOT_TAKEN

 657   L16:     LOAD_GLOBAL             19 (int + NULL)
                LOAD_FAST_BORROW        11 (row)
                LOAD_ATTR               17 (get + NULL|self)
                LOAD_CONST              17 ('reminder_sent_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
       L17:     NOT_TAKEN
       L18:     POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)

 656            LOAD_FAST_BORROW        11 (row)
                LOAD_CONST              17 ('reminder_sent_count')
                STORE_SUBSCR

 659            LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (iso_now, row)
                LOAD_CONST              18 ('last_reminder_at')
                STORE_SUBSCR

 660   L20:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (error_code)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       46 (to L23)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (error_code)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L23)
       L21:     NOT_TAKEN

 661   L22:     LOAD_FAST_BORROW         4 (error_code)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW        11 (row)
                LOAD_CONST              19 ('last_error_code')
                STORE_SUBSCR

 662            LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (iso_now, row)
                LOAD_CONST              20 ('last_error_at')
                STORE_SUBSCR

 664   L23:     LOAD_CONST               0 ('status')
                LOAD_CONST              21 ('ok')

 665            LOAD_CONST               2 ('callback_id')
                LOAD_FAST_BORROW         7 (cid)

 666            LOAD_CONST               4 ('warnings')
                LOAD_CONST               5 ('callback_schedule_store_is_process_local')
                BUILD_LIST               1

 667            LOAD_CONST               6 ('error_code')
                LOAD_CONST               3 (None)

 668            LOAD_CONST              22 ('callback')
                LOAD_GLOBAL             21 (_structural_row + NULL)
                LOAD_FAST_BORROW        11 (row)
                CALL                     1

 663            BUILD_MAP                5

 637   L24:     SWAP                     3
                SWAP                     2
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE
       L25:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L26)
                NOT_TAKEN
                RERAISE                  2
       L26:     POP_TOP
       L27:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L8 -> L25 [2] lasti
  L9 to L10 -> L25 [2] lasti
  L11 to L15 -> L25 [2] lasti
  L16 to L17 -> L25 [2] lasti
  L18 to L21 -> L25 [2] lasti
  L22 to L24 -> L25 [2] lasti
  L25 to L27 -> L28 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app/services/callbacks/callback_schedule.py", line 672>:
672           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

674           LOAD_CONST               2 ('str')

672           LOAD_CONST               3 ('brokerage_id')

675           LOAD_CONST               2 ('str')

672           LOAD_CONST               4 ('new_status')

676           LOAD_CONST               2 ('str')

672           LOAD_CONST               5 ('completed_by')

677           LOAD_CONST               6 ('Optional[str]')

672           LOAD_CONST               7 ('now')

678           LOAD_CONST               8 ('Any')

672           LOAD_CONST               9 ('return')

679           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

672           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _try_durable_transition at 0x0000018C17F7F180, file "app/services/callbacks/callback_schedule.py", line 672>:
 672            RESUME                   0

 683            NOP

 684    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('durable_callback_schedule_enabled', 'mark_durable_callback_reminded', 'mark_durable_callback_completed', 'mark_durable_callback_overdue', 'mark_durable_callback_cancelled', 'mark_durable_callback_failed'))
                IMPORT_NAME              0 (app.services.callbacks.callback_schedule_store)
                IMPORT_FROM              1 (durable_callback_schedule_enabled)
                STORE_FAST               5 (durable_callback_schedule_enabled)
                IMPORT_FROM              2 (mark_durable_callback_reminded)
                STORE_FAST               6 (mark_durable_callback_reminded)
                IMPORT_FROM              3 (mark_durable_callback_completed)
                STORE_FAST               7 (mark_durable_callback_completed)
                IMPORT_FROM              4 (mark_durable_callback_overdue)
                STORE_FAST               8 (mark_durable_callback_overdue)
                IMPORT_FROM              5 (mark_durable_callback_cancelled)
                STORE_FAST               9 (mark_durable_callback_cancelled)
                IMPORT_FROM              6 (mark_durable_callback_failed)
                STORE_FAST              10 (mark_durable_callback_failed)
                POP_TOP

 692            LOAD_FAST_BORROW         5 (durable_callback_schedule_enabled)
                PUSH_NULL
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
        L2:     NOT_TAKEN

 693            LOAD_CONST               2 (None)
                RETURN_VALUE

 694    L3:     LOAD_FAST_BORROW         2 (new_status)
                LOAD_ATTR               15 (lower + NULL|self)
                CALL                     0
                STORE_FAST              11 (ns)

 695            LOAD_FAST_BORROW        11 (ns)
                LOAD_CONST               3 ('completed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L4)
                NOT_TAKEN

 696            LOAD_FAST_BORROW         7 (mark_durable_callback_completed)
                PUSH_NULL

 697            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

 698            LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (completed_by, now)

 696            LOAD_CONST               4 (('completed_by', 'now'))
                CALL_KW                  4
                STORE_FAST              12 (denv)
                JUMP_FORWARD            74 (to L9)

 700    L4:     LOAD_FAST_BORROW        11 (ns)
                LOAD_CONST               5 ('overdue')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L5)
                NOT_TAKEN

 701            LOAD_FAST_BORROW         8 (mark_durable_callback_overdue)
                PUSH_NULL

 702            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)
                LOAD_FAST_BORROW         4 (now)

 701            LOAD_CONST               6 (('now',))
                CALL_KW                  3
                STORE_FAST              12 (denv)
                JUMP_FORWARD            56 (to L9)

 704    L5:     LOAD_FAST_BORROW        11 (ns)
                LOAD_CONST               7 ('reminded')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN

 705            LOAD_FAST_BORROW         6 (mark_durable_callback_reminded)
                PUSH_NULL

 706            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)
                LOAD_FAST_BORROW         4 (now)

 705            LOAD_CONST               6 (('now',))
                CALL_KW                  3
                STORE_FAST              12 (denv)
                JUMP_FORWARD            38 (to L9)

 708    L6:     LOAD_FAST_BORROW        11 (ns)
                LOAD_CONST               8 ('cancelled')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L7)
                NOT_TAKEN

 709            LOAD_FAST_BORROW         9 (mark_durable_callback_cancelled)
                PUSH_NULL

 710            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)
                LOAD_FAST_BORROW         4 (now)

 709            LOAD_CONST               6 (('now',))
                CALL_KW                  3
                STORE_FAST              12 (denv)
                JUMP_FORWARD            20 (to L9)

 712    L7:     LOAD_FAST_BORROW        11 (ns)
                LOAD_CONST               9 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L8)
                NOT_TAKEN

 713            LOAD_FAST_BORROW        10 (mark_durable_callback_failed)
                PUSH_NULL

 714            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)
                LOAD_FAST_BORROW         4 (now)

 713            LOAD_CONST               6 (('now',))
                CALL_KW                  3
                STORE_FAST              12 (denv)
                JUMP_FORWARD             2 (to L9)

 717    L8:     LOAD_CONST               2 (None)
                RETURN_VALUE

 718    L9:     LOAD_GLOBAL             17 (_durable_unavailable + NULL)
                LOAD_FAST_BORROW        12 (denv)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 719   L10:     LOAD_CONST               2 (None)
                RETURN_VALUE

 720   L11:     LOAD_GLOBAL             19 (_project_durable_transition + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 192 (denv, callback_id)
                CALL                     2
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 721            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L17)
                NOT_TAKEN
                STORE_FAST              13 (e)

 722   L14:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 723            LOAD_CONST              10 ('_try_durable_transition error type=')

 724            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 723            BUILD_STRING             2

 722            CALL                     1
                POP_TOP

 726   L15:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L16:     LOAD_CONST               2 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 721   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L3 to L8 -> L13 [0]
  L9 to L10 -> L13 [0]
  L11 to L12 -> L13 [0]
  L13 to L14 -> L18 [1] lasti
  L14 to L15 -> L16 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app/services/callbacks/callback_schedule.py", line 729>:
729           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('denv')

730           LOAD_CONST               2 ('Dict[str, Any]')

729           LOAD_CONST               3 ('callback_id')

730           LOAD_CONST               4 ('str')

729           LOAD_CONST               5 ('return')

731           LOAD_CONST               2 ('Dict[str, Any]')

729           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _project_durable_transition at 0x0000018C17F7F440, file "app/services/callbacks/callback_schedule.py", line 729>:
729           RESUME                   0

735           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         0 (denv)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1

736           LOAD_CONST               2 ('callback_id')
              LOAD_FAST                1 (callback_id)

737           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              3 (list + NULL)
              LOAD_FAST_BORROW         0 (denv)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

738           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         0 (denv)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('error_code')
              CALL                     1

734           BUILD_MAP                4
              STORE_FAST               2 (out)

740           LOAD_FAST_BORROW         0 (denv)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('callback')
              CALL                     1
              STORE_FAST               3 (cb)

741           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (cb)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       74 (to L3)
              NOT_TAKEN

742           LOAD_GLOBAL              7 (dict + NULL)
              LOAD_FAST_BORROW         3 (cb)
              CALL                     1
              STORE_FAST               3 (cb)

743           LOAD_FAST_BORROW         3 (cb)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('status')
              CALL                     1
              STORE_FAST               4 (st)

744           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (st)
              LOAD_GLOBAL              8 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       20 (to L2)
              NOT_TAKEN

745           LOAD_FAST_BORROW         4 (st)
              LOAD_ATTR               11 (upper + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         3 (cb)
              LOAD_CONST               1 ('status')
              STORE_SUBSCR

746   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (cb, out)
              LOAD_CONST               5 ('callback')
              STORE_SUBSCR

747   L3:     LOAD_CONST               6 ('callback_schedule_store_is_durable')
              LOAD_FAST_BORROW         2 (out)
              LOAD_CONST               3 ('warnings')
              BINARY_OP               26 ([])
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE       25 (to L4)
              NOT_TAKEN

748           LOAD_FAST_BORROW         2 (out)
              LOAD_CONST               3 ('warnings')
              BINARY_OP               26 ([])
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_CONST               6 ('callback_schedule_store_is_durable')
              CALL                     1
              POP_TOP

749   L4:     LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app/services/callbacks/callback_schedule.py", line 752>:
752           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

753           LOAD_CONST               2 ('str')

752           LOAD_CONST               3 ('brokerage_id')

754           LOAD_CONST               2 ('str')

752           LOAD_CONST               4 ('completed_by')

756           LOAD_CONST               5 ('Optional[str]')

752           LOAD_CONST               6 ('now')

757           LOAD_CONST               7 ('Any')

752           LOAD_CONST               8 ('return')

758           LOAD_CONST               9 ('Dict[str, Any]')

752           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object mark_callback_completed at 0x0000018C18053630, file "app/services/callbacks/callback_schedule.py", line 752>:
752           RESUME                   0

761           LOAD_GLOBAL              1 (_try_durable_transition + NULL)

762           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

763           LOAD_CONST               1 ('COMPLETED')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (completed_by, now)

761           LOAD_CONST               2 (('callback_id', 'brokerage_id', 'new_status', 'completed_by', 'now'))
              CALL_KW                  5
              STORE_FAST               4 (durable)

765           LOAD_FAST_BORROW         4 (durable)
              POP_JUMP_IF_NONE         3 (to L1)
              NOT_TAKEN

766           LOAD_FAST_BORROW         4 (durable)
              RETURN_VALUE

767   L1:     LOAD_GLOBAL              3 (_update_status + NULL)

768           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

769           LOAD_CONST               1 ('COMPLETED')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (completed_by, now)

767           LOAD_CONST               3 (('new_status', 'completed_by', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "app/services/callbacks/callback_schedule.py", line 773>:
773           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

774           LOAD_CONST               2 ('str')

773           LOAD_CONST               3 ('brokerage_id')

775           LOAD_CONST               2 ('str')

773           LOAD_CONST               4 ('now')

777           LOAD_CONST               5 ('Any')

773           LOAD_CONST               6 ('return')

778           LOAD_CONST               7 ('Dict[str, Any]')

773           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_callback_overdue at 0x0000018C180532D0, file "app/services/callbacks/callback_schedule.py", line 773>:
773           RESUME                   0

782           LOAD_GLOBAL              1 (_try_durable_transition + NULL)

783           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

784           LOAD_CONST               1 ('OVERDUE')
              LOAD_FAST_BORROW         2 (now)

782           LOAD_CONST               2 (('callback_id', 'brokerage_id', 'new_status', 'now'))
              CALL_KW                  4
              STORE_FAST               3 (durable)

786           LOAD_FAST_BORROW         3 (durable)
              POP_JUMP_IF_NONE         3 (to L1)
              NOT_TAKEN

787           LOAD_FAST_BORROW         3 (durable)
              RETURN_VALUE

788   L1:     LOAD_GLOBAL              3 (_update_status + NULL)

789           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

790           LOAD_CONST               1 ('OVERDUE')

791           LOAD_CONST               3 ('callback_window_passed')

792           LOAD_FAST_BORROW         2 (now)

788           LOAD_CONST               4 (('new_status', 'error_code', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "app/services/callbacks/callback_schedule.py", line 800>:
800           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('None')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object reset_callback_registry_for_tests at 0x0000018C17972D90, file "app/services/callbacks/callback_schedule.py", line 800>:
 800           RESUME                   0

 802           LOAD_GLOBAL              0 (_CALLBACK_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 803           LOAD_GLOBAL              2 (_CALLBACK_REGISTRY)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 802   L2:     LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               LOAD_CONST               1 (None)
               CALL                     3
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE
       L3:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L4)
               NOT_TAKEN
               RERAISE                  2
       L4:     POP_TOP
       L5:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "app/services/callbacks/callback_schedule.py", line 806>:
806           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[Dict[str, Any]]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _peek_callback_registry_for_tests at 0x0000018C17FA92F0, file "app/services/callbacks/callback_schedule.py", line 806>:
 806            RESUME                   0

 807            LOAD_GLOBAL              0 (_CALLBACK_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     POP_TOP

 808            LOAD_GLOBAL              2 (_CALLBACK_REGISTRY)
                LOAD_ATTR                5 (values + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      0 (r)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                14 (to L4)
                STORE_FAST               0 (r)
                LOAD_GLOBAL              7 (_structural_row + NULL)
                LOAD_FAST_BORROW         0 (r)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L3)
        L4:     END_FOR
                POP_ITER
        L5:     SWAP                     2
                STORE_FAST               0 (r)

 807    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
                RETURN_VALUE

  --    L7:     SWAP                     2
                POP_TOP

 808            SWAP                     2
                STORE_FAST               0 (r)
                RERAISE                  0

 807    L8:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L9)
                NOT_TAKEN
                RERAISE                  2
        L9:     POP_TOP
       L10:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [2] lasti
  L2 to L5 -> L7 [4]
  L5 to L6 -> L8 [2] lasti
  L7 to L8 -> L8 [2] lasti
  L8 to L10 -> L11 [4] lasti
```
