# callbacks/callback_schedule_store

- **pyc:** `app\services\callbacks\__pycache__\callback_schedule_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\callbacks/callback_schedule_store.py`
- **co_filename (from bytecode):** `app/services/callbacks/callback_schedule_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** callbacks

## Module docstring

```
PAS171 — Durable callback-schedule store (Supabase-backed v1).

Multi-replica-safe, restart-safe replacement for the PAS170
process-local registry in
:mod:`app.services.callbacks.callback_schedule`. The
process-local registry remains in place as a fallback when the
durable store is unavailable (table missing, DB unreachable,
client unconfigured).

Mirrors the PAS166 ↔ PAS165 pattern for *callbacks* — exactly
the same wrapper / fallback semantics, just for the callback
lifecycle.

Doctrine carried by every helper here:

* ``brokerage_id`` is REQUIRED on every read and write.
  NEVER read from any payload — resolved from auth in the
  calling layer and passed in as a kwarg.
* The ``source_call_id`` is the structural pointer back to
  the originating call. NEVER returns phone / email / name /
  notes / transcript / summary anywhere in the envelope.
* No exception escapes any public helper. DB unreachable /
  table missing / constraint conflict are all surfaced as
  structural envelopes; the caller can then fall back to the
  PAS170 process-local registry.
* The closed lifecycle status enum is the *lower-cased* v19
  enum: ``pending / reminded / completed / overdue /
  cancelled / failed``. The PAS170 in-process service still
  surfaces the upper-cased enum to legacy callers; the
  wrapper in :mod:`callback_schedule` translates at the
  boundary.
* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.
  No external vendor SDK. No embeddings / vector libs.

Public surface:

  * ``durable_callback_schedule_enabled(config_or_env=None)``
  * ``register_durable_callback(...)``
  * ``list_durable_callbacks(...)``
  * ``durable_reminder_report(...)``
  * ``mark_durable_callback_reminded(...)``
  * ``mark_durable_callback_completed(...)``
  * ``mark_durable_callback_overdue(...)``
  * ``mark_durable_callback_cancelled(...)``
  * ``mark_durable_callback_failed(...)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `os`, `timedelta`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_clamp_lookahead`, `_clamp_window`, `_coerce_scheduled_for`, `_get_db_safe`, `_is_unique_violation`, `_iso`, `_now_dt`, `_project`, `_safe_unavailable`, `_update_status`, `_validate_brokerage`, `_validate_status_for_filter`, `durable_callback_schedule_enabled`, `durable_reminder_report`, `list_durable_callbacks`, `mark_durable_callback_cancelled`, `mark_durable_callback_completed`, `mark_durable_callback_failed`, `mark_durable_callback_overdue`, `mark_durable_callback_reminded`, `register_durable_callback`

## Env-key candidates

`PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED`

## String constants (redacted where noted)

- '\nPAS171 — Durable callback-schedule store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the PAS170\nprocess-local registry in\n:mod:`app.services.callbacks.callback_schedule`. The\nprocess-local registry remains in place as a fallback when the\ndurable store is unavailable (table missing, DB unreachable,\nclient unconfigured).\n\nMirrors the PAS166 ↔ PAS165 pattern for *callbacks* — exactly\nthe same wrapper / fallback semantics, just for the callback\nlifecycle.\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The ``source_call_id`` is the structural pointer back to\n  the originating call. NEVER returns phone / email / name /\n  notes / transcript / summary anywhere in the envelope.\n* No exception escapes any public helper. DB unreachable /\n  table missing / constraint conflict are all surfaced as\n  structural envelopes; the caller can then fall back to the\n  PAS170 process-local registry.\n* The closed lifecycle status enum is the *lower-cased* v19\n  enum: ``pending / reminded / completed / overdue /\n  cancelled / failed``. The PAS170 in-process service still\n  surfaces the upper-cased enum to legacy callers; the\n  wrapper in :mod:`callback_schedule` translates at the\n  boundary.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n\nPublic surface:\n\n  * ``durable_callback_schedule_enabled(config_or_env=None)``\n  * ``register_durable_callback(...)``\n  * ``list_durable_callbacks(...)``\n  * ``durable_reminder_report(...)``\n  * ``mark_durable_callback_reminded(...)``\n  * ``mark_durable_callback_completed(...)``\n  * ``mark_durable_callback_overdue(...)``\n  * ``mark_durable_callback_cancelled(...)``\n  * ``mark_durable_callback_failed(...)``\n'
- 'pas.callbacks.schedule_store'
- 'pas_callback_schedule'
- 'pending'
- 'window_minutes'
- 'status'
- 'completed_by'
- 'PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED'
- 'extra_warning'
- 'now'
- 'error_code'
- 'bump_reminder'
- 'limit'
- 'lookahead_minutes'
- 'Any'
- 'return'
- 'datetime'
- '+00:00'
- 'str'
- 'seconds'
- 'value'
- 'Optional[datetime]'
- 'int'
- 'callback_schedule_store db client unavailable type='
- 'config_or_env'
- 'bool'
- 'Resolve whether durable callback schedule is enabled.\n\nPrecedence (first match wins):\n\n1. ``config_or_env`` — if it is a dict carrying the key\n   ``callback_schedule_durable_enabled`` (literal\n   True / False), that wins.\n2. ``PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED``: explicit\n   "false" / "0" / "no" / "off" / "disabled" disables.\n   Anything else (including unset) defaults to ENABLED.\n3. Default: ENABLED.\n\nNEVER raises.\n'
- 'callback_schedule_durable_enabled'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'Project a DB row dict into the structural envelope shape,\ndropping any column outside ``_STRUCTURAL_COLUMNS``. NEVER\nraises. Returns ``None`` on bad input.'
- 'brokerage_id'
- 'Optional[str]'
- 'missing_brokerage_id'
- 'invalid_status_filter'
- 'Dict[str, Any]'
- 'durable_callback_schedule_unavailable'
- 'warning'
- 'callback'
- 'callbacks'
- 'warnings'
- 'source_call_id'
- 'scheduled_for'
- 'Insert a callback row. Returns a structural envelope.\n\nOutcomes:\n\n* ``status="ok"`` with ``callback`` populated — fresh\n  insert.\n* ``status="ok"`` with ``duplicate=True`` — partial-unique\n  index conflict on\n  ``(brokerage_id, source_call_id) WHERE status IN (\n  pending, reminded)``; the caller should treat as\n  "already scheduled".\n* ``status="warning"`` — DB unavailable. Caller falls back\n  to the PAS170 process-local registry.\n* ``status="failed"`` — input validation error.\n\nNEVER raises. NEVER returns raw lead context.\n'
- 'failed'
- 'missing_source_call_id'
- 'invalid_scheduled_for'
- 'callback_id'
- 'reminder_sent_count'
- 'created_at'
- 'updated_at'
- 'data'
- 'duplicate'
- 'callback_already_scheduled'
- 'register_durable_callback db error type='
- 'db_write_failed:'
- 'exc'
- 'BaseException'
- '23505'
- 'duplicate key value violates unique constraint'
- 'already exists'
- 'new_status'
- 'missing_callback_id'
- 'invalid_status'
- 'completed'
- 'completed_at'
- 'operator'
- 'last_reminder_at'
- 'last_error_code'
- 'last_error_at'
- 'callback_not_found_or_cross_tenant'
- 'callback_schedule_store update error type='
- ' new_status='
- 'reminded'
- 'overdue'
- 'callback_window_passed'
- 'cancelled'
- 'callback_failed'
- "Return the brokerage's callback rows filtered by status,\nsorted by ``scheduled_for`` ASC.\n\nReturns a closed-shape envelope. NEVER raises. NEVER\nincludes raw lead context.\n"
- 'filter_status'
- 'count'
- 'list_durable_callbacks db error type='
- 'db_read_failed:'
- "Return the brokerage's pending callbacks split into\n``due`` (in the lookahead window) and ``overdue``\n(scheduled time has passed).\n\nReturns a closed-shape envelope. NEVER raises. NEVER\nauto-dials.\n"
- 'due_count'
- 'due'
- 'overdue_count'
- 'durable_reminder_report db error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS171 — Durable callback-schedule store (Supabase-backed v1).\n\nMulti-replica-safe, restart-safe replacement for the PAS170\nprocess-local registry in\n:mod:`app.services.callbacks.callback_schedule`. The\nprocess-local registry remains in place as a fallback when the\ndurable store is unavailable (table missing, DB unreachable,\nclient unconfigured).\n\nMirrors the PAS166 ↔ PAS165 pattern for *callbacks* — exactly\nthe same wrapper / fallback semantics, just for the callback\nlifecycle.\n\nDoctrine carried by every helper here:\n\n* ``brokerage_id`` is REQUIRED on every read and write.\n  NEVER read from any payload — resolved from auth in the\n  calling layer and passed in as a kwarg.\n* The ``source_call_id`` is the structural pointer back to\n  the originating call. NEVER returns phone / email / name /\n  notes / transcript / summary anywhere in the envelope.\n* No exception escapes any public helper. DB unreachable /\n  table missing / constraint conflict are all surfaced as\n  structural envelopes; the caller can then fall back to the\n  PAS170 process-local registry.\n* The closed lifecycle status enum is the *lower-cased* v19\n  enum: ``pending / reminded / completed / overdue /\n  cancelled / failed``. The PAS170 in-process service still\n  surfaces the upper-cased enum to legacy callers; the\n  wrapper in :mod:`callback_schedule` translates at the\n  boundary.\n* No Gmail / Google / inbox / OAuth / IMAP / POP3 import.\n  No external vendor SDK. No embeddings / vector libs.\n\nPublic surface:\n\n  * ``durable_callback_schedule_enabled(config_or_env=None)``\n  * ``register_durable_callback(...)``\n  * ``list_durable_callbacks(...)``\n  * ``durable_reminder_report(...)``\n  * ``mark_durable_callback_reminded(...)``\n  * ``mark_durable_callback_completed(...)``\n  * ``mark_durable_callback_overdue(...)``\n  * ``mark_durable_callback_cancelled(...)``\n  * ``mark_durable_callback_failed(...)``\n')
              STORE_NAME               0 (__doc__)

 49           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 51           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 52           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 53           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (uuid)
              STORE_NAME               5 (uuid)

 54           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              6 (datetime)
              IMPORT_FROM              6 (datetime)
              STORE_NAME               6 (datetime)
              IMPORT_FROM              7 (timedelta)
              STORE_NAME               7 (timedelta)
              IMPORT_FROM              8 (timezone)
              STORE_NAME               8 (timezone)
              POP_TOP

 55           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              9 (typing)
              IMPORT_FROM             10 (Any)
              STORE_NAME              10 (Any)
              IMPORT_FROM             11 (Dict)
              STORE_NAME              11 (Dict)
              IMPORT_FROM             12 (List)
              STORE_NAME              12 (List)
              IMPORT_FROM             13 (Optional)
              STORE_NAME              13 (Optional)
              POP_TOP

 58           LOAD_NAME                3 (logging)
              LOAD_ATTR               28 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.callbacks.schedule_store')
              CALL                     1
              STORE_NAME              15 (logger)

 65           LOAD_CONST               6 ('pas_callback_schedule')
              STORE_NAME              16 (_TABLE)

 67           LOAD_CONST              62 (('pending', 'reminded', 'completed', 'overdue', 'cancelled', 'failed'))
              STORE_NAME              17 (DURABLE_CALLBACK_STATUSES)

 77           LOAD_CONST              63 (('callback_id', 'brokerage_id', 'source_call_id', 'scheduled_for', 'window_minutes', 'status', 'reminder_sent_count', 'last_reminder_at', 'completed_at', 'completed_by', 'last_error_code', 'created_at', 'updated_at'))
              STORE_NAME              18 (_STRUCTURAL_COLUMNS)

 95           LOAD_CONST              11 ('PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED')
              STORE_NAME              19 (_ENV_ENABLE_FLAG)

 96           LOAD_CONST              64 (('false', '0', 'no', 'off', 'disabled'))
              STORE_NAME              20 (_ENV_DISABLE_FALSE_LITERALS)

 98           LOAD_SMALL_INT         200
              STORE_NAME              21 (_LIST_HARD_CAP)

105           LOAD_CONST              65 ((None,))
              LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA1E30, file "app/services/callbacks/callback_schedule_store.py", line 105>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _now_dt at 0x0000018C17ED0C70, file "app/services/callbacks/callback_schedule_store.py", line 105>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              22 (_now_dt)

121           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA33C0, file "app/services/callbacks/callback_schedule_store.py", line 121>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _iso at 0x0000018C18025A30, file "app/services/callbacks/callback_schedule_store.py", line 121>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_iso)

125           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA34B0, file "app/services/callbacks/callback_schedule_store.py", line 125>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _coerce_scheduled_for at 0x0000018C17EE25F0, file "app/services/callbacks/callback_schedule_store.py", line 125>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_coerce_scheduled_for)

141           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/callbacks/callback_schedule_store.py", line 141>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _clamp_window at 0x0000018C17FE1920, file "app/services/callbacks/callback_schedule_store.py", line 141>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_clamp_window)

153           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3780, file "app/services/callbacks/callback_schedule_store.py", line 153>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _clamp_limit at 0x0000018C18010DF0, file "app/services/callbacks/callback_schedule_store.py", line 153>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_clamp_limit)

165           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3870, file "app/services/callbacks/callback_schedule_store.py", line 165>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _clamp_lookahead at 0x0000018C17FE17D0, file "app/services/callbacks/callback_schedule_store.py", line 165>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_clamp_lookahead)

177           LOAD_CONST              24 (<code object _get_db_safe at 0x0000018C17FF0F30, file "app/services/callbacks/callback_schedule_store.py", line 177>)
              MAKE_FUNCTION
              STORE_NAME              28 (_get_db_safe)

189           LOAD_CONST              65 ((None,))
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3960, file "app/services/callbacks/callback_schedule_store.py", line 189>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object durable_callback_schedule_enabled at 0x0000018C17F01A90, file "app/services/callbacks/callback_schedule_store.py", line 189>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              29 (durable_callback_schedule_enabled)

217           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/callbacks/callback_schedule_store.py", line 217>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object _project at 0x0000018C17FE1290, file "app/services/callbacks/callback_schedule_store.py", line 217>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_project)

230           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3B40, file "app/services/callbacks/callback_schedule_store.py", line 230>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object _validate_brokerage at 0x0000018C180388F0, file "app/services/callbacks/callback_schedule_store.py", line 230>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_validate_brokerage)

236           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3C30, file "app/services/callbacks/callback_schedule_store.py", line 236>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object _validate_status_for_filter at 0x0000018C18010F50, file "app/services/callbacks/callback_schedule_store.py", line 236>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_validate_status_for_filter)

244           LOAD_CONST              33 ('extra_warning')

246           LOAD_CONST               2 (None)

244           BUILD_MAP                1
              LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3D20, file "app/services/callbacks/callback_schedule_store.py", line 244>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _safe_unavailable at 0x0000018C17C49B80, file "app/services/callbacks/callback_schedule_store.py", line 244>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              33 (_safe_unavailable)

264           LOAD_CONST               8 ('window_minutes')

269           LOAD_SMALL_INT          15

264           LOAD_CONST              36 ('now')

270           LOAD_CONST               2 (None)

264           BUILD_MAP                2
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025930, file "app/services/callbacks/callback_schedule_store.py", line 264>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object register_durable_callback at 0x0000018C1821CFB0, file "app/services/callbacks/callback_schedule_store.py", line 264>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              34 (register_durable_callback)

364           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA3E10, file "app/services/callbacks/callback_schedule_store.py", line 364>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object _is_unique_violation at 0x0000018C17F95FD0, file "app/services/callbacks/callback_schedule_store.py", line 364>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_is_unique_violation)

378           LOAD_CONST              10 ('completed_by')

383           LOAD_CONST               2 (None)

378           LOAD_CONST              41 ('error_code')

384           LOAD_CONST               2 (None)

378           LOAD_CONST              42 ('bump_reminder')

385           LOAD_CONST              43 (False)

378           LOAD_CONST              36 ('now')

386           LOAD_CONST               2 (None)

378           BUILD_MAP                4
              LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18090690, file "app/services/callbacks/callback_schedule_store.py", line 378>)
              MAKE_FUNCTION
              LOAD_CONST              45 (<code object _update_status at 0x0000018C1821DEE0, file "app/services/callbacks/callback_schedule_store.py", line 378>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (_update_status)

486           LOAD_CONST              36 ('now')

487           LOAD_CONST               2 (None)

486           BUILD_MAP                1
              LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/callbacks/callback_schedule_store.py", line 486>)
              MAKE_FUNCTION
              LOAD_CONST              47 (<code object mark_durable_callback_reminded at 0x0000018C17FA3F00, file "app/services/callbacks/callback_schedule_store.py", line 486>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              37 (mark_durable_callback_reminded)

495           LOAD_CONST              10 ('completed_by')

497           LOAD_CONST               2 (None)

495           LOAD_CONST              36 ('now')

497           LOAD_CONST               2 (None)

495           BUILD_MAP                2
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/callbacks/callback_schedule_store.py", line 495>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object mark_durable_callback_completed at 0x0000018C180B0030, file "app/services/callbacks/callback_schedule_store.py", line 495>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (mark_durable_callback_completed)

505           LOAD_CONST              36 ('now')

506           LOAD_CONST               2 (None)

505           BUILD_MAP                1
              LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18024930, file "app/services/callbacks/callback_schedule_store.py", line 505>)
              MAKE_FUNCTION
              LOAD_CONST              51 (<code object mark_durable_callback_overdue at 0x0000018C180B0120, file "app/services/callbacks/callback_schedule_store.py", line 505>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (mark_durable_callback_overdue)

514           LOAD_CONST              36 ('now')

515           LOAD_CONST               2 (None)

514           BUILD_MAP                1
              LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18025630, file "app/services/callbacks/callback_schedule_store.py", line 514>)
              MAKE_FUNCTION
              LOAD_CONST              53 (<code object mark_durable_callback_cancelled at 0x0000018C180B0210, file "app/services/callbacks/callback_schedule_store.py", line 514>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (mark_durable_callback_cancelled)

523           LOAD_CONST              41 ('error_code')

525           LOAD_CONST               2 (None)

523           LOAD_CONST              36 ('now')

525           LOAD_CONST               2 (None)

523           BUILD_MAP                2
              LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18025730, file "app/services/callbacks/callback_schedule_store.py", line 523>)
              MAKE_FUNCTION
              LOAD_CONST              55 (<code object mark_durable_callback_failed at 0x0000018C18090470, file "app/services/callbacks/callback_schedule_store.py", line 523>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (mark_durable_callback_failed)

539           LOAD_CONST               9 ('status')

542           LOAD_CONST               7 ('pending')

539           LOAD_CONST              56 ('limit')

543           LOAD_SMALL_INT          50

539           BUILD_MAP                2
              LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18025330, file "app/services/callbacks/callback_schedule_store.py", line 539>)
              MAKE_FUNCTION
              LOAD_CONST              58 (<code object list_durable_callbacks at 0x0000018C17D43500, file "app/services/callbacks/callback_schedule_store.py", line 539>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              42 (list_durable_callbacks)

619           LOAD_CONST              59 ('lookahead_minutes')

622           LOAD_SMALL_INT          60

619           LOAD_CONST              36 ('now')

623           LOAD_CONST               2 (None)

619           BUILD_MAP                2
              LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18025230, file "app/services/callbacks/callback_schedule_store.py", line 619>)
              MAKE_FUNCTION
              LOAD_CONST              61 (<code object durable_reminder_report at 0x0000018C17D43F80, file "app/services/callbacks/callback_schedule_store.py", line 619>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              43 (durable_reminder_report)

711           BUILD_LIST               0
              LOAD_CONST              66 (('DURABLE_CALLBACK_STATUSES', 'durable_callback_schedule_enabled', 'register_durable_callback', 'list_durable_callbacks', 'durable_reminder_report', 'mark_durable_callback_reminded', 'mark_durable_callback_completed', 'mark_durable_callback_overdue', 'mark_durable_callback_cancelled', 'mark_durable_callback_failed'))
              LIST_EXTEND              1
              STORE_NAME              44 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app/services/callbacks/callback_schedule_store.py", line 105>:
105           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C17ED0C70, file "app/services/callbacks/callback_schedule_store.py", line 105>:
 105            RESUME                   0

 106            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

 107            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

 108            LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

 109    L1:     LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

 110    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (now)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      117 (to L6)
                NOT_TAKEN

 111            NOP

 112    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               16 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (now)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

 113            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 114            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 115    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 118    L6:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               20 (now)
                PUSH_NULL
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 116            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L9)
                NOT_TAKEN
                POP_TOP

 117    L8:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 49 (to L6)

 116    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app/services/callbacks/callback_schedule_store.py", line 121>:
121           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025A30, file "app/services/callbacks/callback_schedule_store.py", line 121>:
121           RESUME                   0

122           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app/services/callbacks/callback_schedule_store.py", line 125>:
125           RESUME                   0
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

Disassembly of <code object _coerce_scheduled_for at 0x0000018C17EE25F0, file "app/services/callbacks/callback_schedule_store.py", line 125>:
 125            RESUME                   0

 126            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       78 (to L2)
                NOT_TAKEN

 127            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L1)
                NOT_TAKEN

 128            LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                RETURN_VALUE

 129    L1:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
                RETURN_VALUE

 130    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
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

 131            NOP

 132    L3:     LOAD_GLOBAL              2 (datetime)
                LOAD_ATTR               18 (fromisoformat)
                PUSH_NULL
                LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_CONST               2 ('Z')
                LOAD_CONST               3 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST               1 (dt)

 133            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                4 (tzinfo)
                POP_JUMP_IF_NOT_NONE    33 (to L4)
                NOT_TAKEN

 134            LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR                7 (replace + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                LOAD_CONST               1 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST               1 (dt)

 135    L4:     LOAD_FAST_BORROW         1 (dt)
                LOAD_ATTR               13 (astimezone + NULL|self)
                LOAD_GLOBAL              8 (timezone)
                LOAD_ATTR               10 (utc)
                CALL                     1
        L5:     RETURN_VALUE

 138    L6:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 136            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 137    L8:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 136    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L5 -> L7 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/callbacks/callback_schedule_store.py", line 141>:
141           RESUME                   0
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

Disassembly of <code object _clamp_window at 0x0000018C17FE1920, file "app/services/callbacks/callback_schedule_store.py", line 141>:
 141           RESUME                   0

 142           NOP

 143   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 146   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 147           LOAD_SMALL_INT           1
               RETURN_VALUE

 148   L3:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT         240
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 149           LOAD_SMALL_INT         240
               RETURN_VALUE

 150   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 144           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 145   L6:     POP_EXCEPT
               LOAD_SMALL_INT          15
               RETURN_VALUE

 144   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app/services/callbacks/callback_schedule_store.py", line 153>:
153           RESUME                   0
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

Disassembly of <code object _clamp_limit at 0x0000018C18010DF0, file "app/services/callbacks/callback_schedule_store.py", line 153>:
 153           RESUME                   0

 154           NOP

 155   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 158   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 159           LOAD_SMALL_INT           1
               RETURN_VALUE

 160   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              6 (_LIST_HARD_CAP)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 161           LOAD_GLOBAL              6 (_LIST_HARD_CAP)
               RETURN_VALUE

 162   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 156           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 157   L6:     POP_EXCEPT
               LOAD_SMALL_INT          50
               RETURN_VALUE

 156   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "app/services/callbacks/callback_schedule_store.py", line 165>:
165           RESUME                   0
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

Disassembly of <code object _clamp_lookahead at 0x0000018C17FE17D0, file "app/services/callbacks/callback_schedule_store.py", line 165>:
 165           RESUME                   0

 166           NOP

 167   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 170   L2:     LOAD_FAST                1 (v)
               LOAD_SMALL_INT           1
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 171           LOAD_SMALL_INT           1
               RETURN_VALUE

 172   L3:     LOAD_FAST                1 (v)
               LOAD_CONST               1 (1440)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 173           LOAD_CONST               1 (1440)
               RETURN_VALUE

 174   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 168           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 169   L6:     POP_EXCEPT
               LOAD_SMALL_INT          60
               RETURN_VALUE

 168   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object _get_db_safe at 0x0000018C17FF0F30, file "app/services/callbacks/callback_schedule_store.py", line 177>:
 177           RESUME                   0

 178           NOP

 179   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 180           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 181           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 182   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 183           LOAD_CONST               2 ('callback_schedule_store db client unavailable type=')

 184           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 183           BUILD_STRING             2

 182           CALL                     1
               POP_TOP

 186   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 181   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app/services/callbacks/callback_schedule_store.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object durable_callback_schedule_enabled at 0x0000018C17F01A90, file "app/services/callbacks/callback_schedule_store.py", line 189>:
189           RESUME                   0

204           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L2)
              NOT_TAKEN

205           LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               1 ('callback_schedule_durable_enabled')
              CALL                     1
              STORE_FAST               1 (explicit)

206           LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

207           LOAD_CONST               2 (True)
              RETURN_VALUE

208   L1:     LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               3 (False)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

209           LOAD_CONST               3 (False)
              RETURN_VALUE

210   L2:     LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL             10 (_ENV_ENABLE_FLAG)
              CALL                     1
              STORE_FAST               2 (raw)

211           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L3)
              NOT_TAKEN

212           LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               17 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             18 (_ENV_DISABLE_FALSE_LITERALS)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

213           LOAD_CONST               3 (False)
              RETURN_VALUE

214   L3:     LOAD_CONST               2 (True)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/callbacks/callback_schedule_store.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project at 0x0000018C17FE1290, file "app/services/callbacks/callback_schedule_store.py", line 217>:
217           RESUME                   0

221           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

222           LOAD_CONST               1 (None)
              RETURN_VALUE

223   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

224           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

225           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

226   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

224   L4:     END_FOR
              POP_ITER

227           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app/services/callbacks/callback_schedule_store.py", line 230>:
230           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_brokerage at 0x0000018C180388F0, file "app/services/callbacks/callback_schedule_store.py", line 230>:
230           RESUME                   0

231           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (brokerage_id)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

232   L1:     LOAD_CONST               0 ('missing_brokerage_id')
              RETURN_VALUE

233   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app/services/callbacks/callback_schedule_store.py", line 236>:
236           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_status_for_filter at 0x0000018C18010F50, file "app/services/callbacks/callback_schedule_store.py", line 236>:
236           RESUME                   0

237           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (status)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

238           LOAD_CONST               0 ('invalid_status_filter')
              RETURN_VALUE

239   L1:     LOAD_FAST_BORROW         0 (status)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL              8 (DURABLE_CALLBACK_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

240           LOAD_CONST               0 ('invalid_status_filter')
              RETURN_VALUE

241   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "app/services/callbacks/callback_schedule_store.py", line 244>:
244           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('extra_warning')

246           LOAD_CONST               2 ('Optional[str]')

244           LOAD_CONST               3 ('return')

247           LOAD_CONST               4 ('Dict[str, Any]')

244           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_unavailable at 0x0000018C17C49B80, file "app/services/callbacks/callback_schedule_store.py", line 244>:
244           RESUME                   0

248           LOAD_CONST               0 ('durable_callback_schedule_unavailable')
              BUILD_LIST               1
              STORE_FAST               1 (warnings)

249           LOAD_FAST_BORROW         0 (extra_warning)
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L1)
              NOT_TAKEN

250           LOAD_FAST_BORROW         1 (warnings)
              LOAD_ATTR                1 (append + NULL|self)
              LOAD_FAST_BORROW         0 (extra_warning)
              CALL                     1
              POP_TOP

252   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('warning')

253           LOAD_CONST               3 ('callback')
              LOAD_CONST               4 (None)

254           LOAD_CONST               5 ('callbacks')
              BUILD_LIST               0

255           LOAD_CONST               6 ('warnings')
              LOAD_FAST_BORROW         1 (warnings)

256           LOAD_CONST               7 ('error_code')
              LOAD_CONST               0 ('durable_callback_schedule_unavailable')

251           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app/services/callbacks/callback_schedule_store.py", line 264>:
264           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

266           LOAD_CONST               2 ('str')

264           LOAD_CONST               3 ('source_call_id')

267           LOAD_CONST               2 ('str')

264           LOAD_CONST               4 ('scheduled_for')

268           LOAD_CONST               5 ('Any')

264           LOAD_CONST               6 ('window_minutes')

269           LOAD_CONST               5 ('Any')

264           LOAD_CONST               7 ('now')

270           LOAD_CONST               5 ('Any')

264           LOAD_CONST               8 ('return')

271           LOAD_CONST               9 ('Dict[str, Any]')

264           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object register_durable_callback at 0x0000018C1821CFB0, file "app/services/callbacks/callback_schedule_store.py", line 264>:
 264            RESUME                   0

 289            LOAD_GLOBAL              1 (_validate_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L1)
                NOT_TAKEN

 291            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 292            LOAD_CONST               3 ('callback')
                LOAD_CONST               4 (None)

 293            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 294            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('missing_brokerage_id')

 290            BUILD_MAP                4
                RETURN_VALUE

 296    L1:     LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (source_call_id)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (source_call_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L3)
                NOT_TAKEN

 298    L2:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 299            LOAD_CONST               3 ('callback')
                LOAD_CONST               4 (None)

 300            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 301            LOAD_CONST               6 ('error_code')
                LOAD_CONST               8 ('missing_source_call_id')

 297            BUILD_MAP                4
                RETURN_VALUE

 303    L3:     LOAD_GLOBAL              9 (_coerce_scheduled_for + NULL)
                LOAD_FAST_BORROW         2 (scheduled_for)
                CALL                     1
                STORE_FAST               5 (sched_dt)

 304            LOAD_FAST_BORROW         5 (sched_dt)
                POP_JUMP_IF_NOT_NONE    11 (to L4)
                NOT_TAKEN

 306            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 307            LOAD_CONST               3 ('callback')
                LOAD_CONST               4 (None)

 308            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 309            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 ('invalid_scheduled_for')

 305            BUILD_MAP                4
                RETURN_VALUE

 311    L4:     LOAD_GLOBAL             11 (_clamp_window + NULL)
                LOAD_FAST_BORROW         3 (window_minutes)
                CALL                     1
                STORE_FAST               6 (win)

 312            LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (bid)

 313            LOAD_FAST_BORROW         1 (source_call_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               8 (sid)

 314            LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         4 (now)
                CALL                     1
                STORE_FAST               9 (now_dt)

 315            LOAD_GLOBAL             15 (_iso + NULL)
                LOAD_FAST_BORROW         9 (now_dt)
                CALL                     1
                STORE_FAST              10 (iso_now)

 316            LOAD_GLOBAL              5 (str + NULL)
                LOAD_GLOBAL             16 (uuid)
                LOAD_ATTR               18 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1
                STORE_FAST              11 (callback_id)

 318            LOAD_GLOBAL             21 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              12 (db)

 319            LOAD_FAST_BORROW        12 (db)
                POP_JUMP_IF_NOT_NONE    11 (to L5)
                NOT_TAKEN

 320            LOAD_GLOBAL             23 (_safe_unavailable + NULL)
                CALL                     0
                RETURN_VALUE

 323    L5:     LOAD_CONST              10 ('callback_id')
                LOAD_FAST_BORROW        11 (callback_id)

 324            LOAD_CONST              11 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)

 325            LOAD_CONST              12 ('source_call_id')
                LOAD_FAST_BORROW         8 (sid)

 326            LOAD_CONST              13 ('scheduled_for')
                LOAD_GLOBAL             15 (_iso + NULL)
                LOAD_FAST_BORROW         5 (sched_dt)
                CALL                     1

 327            LOAD_CONST              14 ('window_minutes')
                LOAD_FAST_BORROW         6 (win)

 328            LOAD_CONST               1 ('status')
                LOAD_CONST              15 ('pending')

 329            LOAD_CONST              16 ('reminder_sent_count')
                LOAD_SMALL_INT           0

 330            LOAD_CONST              17 ('created_at')
                LOAD_FAST_BORROW        10 (iso_now)

 331            LOAD_CONST              18 ('updated_at')
                LOAD_FAST_BORROW        10 (iso_now)

 322            BUILD_MAP                9
                STORE_FAST              13 (row)

 334            NOP

 335    L6:     LOAD_FAST_BORROW        12 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_TABLE)
                CALL                     1
                LOAD_ATTR               29 (insert + NULL|self)
                LOAD_FAST_BORROW        13 (row)
                CALL                     1
                LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0
                STORE_FAST              14 (result)

 336            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW        14 (result)
                LOAD_CONST              19 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST              15 (inserted)

 337            LOAD_FAST_BORROW        15 (inserted)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
        L8:     NOT_TAKEN
        L9:     LOAD_GLOBAL             37 (_project + NULL)
                LOAD_FAST_BORROW        15 (inserted)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L11)
       L10:     LOAD_GLOBAL             37 (_project + NULL)
                LOAD_FAST_BORROW        13 (row)
                CALL                     1
       L11:     STORE_FAST              16 (proj)

 339            LOAD_CONST               1 ('status')
                LOAD_CONST              20 ('ok')

 340            LOAD_CONST               3 ('callback')
                LOAD_FAST_BORROW        16 (proj)

 341            LOAD_CONST              21 ('duplicate')
                LOAD_CONST              22 (False)

 342            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 343            LOAD_CONST               6 ('error_code')
                LOAD_CONST               4 (None)

 338            BUILD_MAP                5
       L12:     RETURN_VALUE

  --   L13:     PUSH_EXC_INFO

 345            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      130 (to L21)
                NOT_TAKEN
                STORE_FAST              17 (e)

 346   L14:     LOAD_GLOBAL             41 (_is_unique_violation + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L17)
                NOT_TAKEN

 350            LOAD_CONST               1 ('status')
                LOAD_CONST              20 ('ok')

 351            LOAD_CONST               3 ('callback')
                LOAD_CONST               4 (None)

 352            LOAD_CONST              21 ('duplicate')
                LOAD_CONST              23 (True)

 353            LOAD_CONST               5 ('warnings')
                LOAD_CONST              24 ('callback_already_scheduled')
                BUILD_LIST               1

 354            LOAD_CONST               6 ('error_code')
                LOAD_CONST               4 (None)

 349            BUILD_MAP                5
       L15:     SWAP                     2
       L16:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

 356   L17:     LOAD_GLOBAL             42 (logger)
                LOAD_ATTR               45 (warning + NULL|self)

 357            LOAD_CONST              25 ('register_durable_callback db error type=')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 356            CALL                     1
                POP_TOP

 359            LOAD_GLOBAL             23 (_safe_unavailable + NULL)
                LOAD_CONST              26 ('db_write_failed:')
                LOAD_GLOBAL             47 (type + NULL)
                LOAD_FAST               17 (e)
                CALL                     1
                LOAD_ATTR               48 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST              27 (('extra_warning',))
                CALL_KW                  1
                STORE_FAST              18 (env)

 360            LOAD_CONST              22 (False)
                LOAD_FAST               18 (env)
                LOAD_CONST              21 ('duplicate')
                STORE_SUBSCR

 361            LOAD_FAST               18 (env)
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               4 (None)
                STORE_FAST              17 (e)
                DELETE_FAST             17 (e)
                RERAISE                  1

 345   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L8 -> L13 [0]
  L9 to L12 -> L13 [0]
  L13 to L14 -> L22 [1] lasti
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "app/services/callbacks/callback_schedule_store.py", line 364>:
364           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('exc')
              LOAD_CONST               2 ('BaseException')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_unique_violation at 0x0000018C17F95FD0, file "app/services/callbacks/callback_schedule_store.py", line 364>:
 364           RESUME                   0

 365           NOP

 366   L1:     LOAD_GLOBAL              1 (repr + NULL)
               LOAD_FAST_BORROW         0 (exc)
               CALL                     1
               STORE_FAST               1 (s)

 369   L2:     LOAD_CONST               1 ('23505')
               LOAD_FAST                1 (s)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 370           LOAD_CONST               2 (True)
               RETURN_VALUE

 371   L3:     LOAD_FAST                1 (s)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lowered)

 373           LOAD_CONST               3 ('duplicate key value violates unique constraint')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN
               POP_TOP

 374           LOAD_CONST               4 ('already exists')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)

 372   L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 367           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 368   L6:     POP_EXCEPT
               LOAD_CONST               0 (False)
               RETURN_VALUE

 367   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18090690, file "app/services/callbacks/callback_schedule_store.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

380           LOAD_CONST               2 ('str')

378           LOAD_CONST               3 ('brokerage_id')

381           LOAD_CONST               2 ('str')

378           LOAD_CONST               4 ('new_status')

382           LOAD_CONST               2 ('str')

378           LOAD_CONST               5 ('completed_by')

383           LOAD_CONST               6 ('Optional[str]')

378           LOAD_CONST               7 ('error_code')

384           LOAD_CONST               6 ('Optional[str]')

378           LOAD_CONST               8 ('bump_reminder')

385           LOAD_CONST               9 ('bool')

378           LOAD_CONST              10 ('now')

386           LOAD_CONST              11 ('Any')

378           LOAD_CONST              12 ('return')

387           LOAD_CONST              13 ('Dict[str, Any]')

378           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _update_status at 0x0000018C1821DEE0, file "app/services/callbacks/callback_schedule_store.py", line 378>:
 378            RESUME                   0

 388            LOAD_GLOBAL              1 (_validate_brokerage + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       11 (to L1)
                NOT_TAKEN

 390            LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 391            LOAD_CONST               2 ('callback')
                LOAD_CONST               3 (None)

 392            LOAD_CONST               4 ('warnings')
                BUILD_LIST               0

 393            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('missing_brokerage_id')

 389            BUILD_MAP                4
                RETURN_VALUE

 395    L1:     LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (callback_id)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (callback_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L3)
                NOT_TAKEN

 397    L2:     LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 398            LOAD_CONST               2 ('callback')
                LOAD_CONST               3 (None)

 399            LOAD_CONST               4 ('warnings')
                BUILD_LIST               0

 400            LOAD_CONST               5 ('error_code')
                LOAD_CONST               7 ('missing_callback_id')

 396            BUILD_MAP                4
                RETURN_VALUE

 402    L3:     LOAD_FAST_BORROW         2 (new_status)
                LOAD_GLOBAL              8 (DURABLE_CALLBACK_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       11 (to L4)
                NOT_TAKEN

 404            LOAD_CONST               0 ('status')
                LOAD_CONST               1 ('failed')

 405            LOAD_CONST               2 ('callback')
                LOAD_CONST               3 (None)

 406            LOAD_CONST               4 ('warnings')
                BUILD_LIST               0

 407            LOAD_CONST               5 ('error_code')
                LOAD_CONST               8 ('invalid_status')

 403            BUILD_MAP                4
                RETURN_VALUE

 409    L4:     LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (bid)

 410            LOAD_FAST_BORROW         0 (callback_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               8 (cid)

 411            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               9 (db)

 412            LOAD_FAST_BORROW         9 (db)
                POP_JUMP_IF_NOT_NONE    11 (to L5)
                NOT_TAKEN

 413            LOAD_GLOBAL             13 (_safe_unavailable + NULL)
                CALL                     0
                RETURN_VALUE

 415    L5:     LOAD_GLOBAL             15 (_now_dt + NULL)
                LOAD_FAST_BORROW         6 (now)
                CALL                     1
                STORE_FAST              10 (now_dt)

 416            LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        10 (now_dt)
                CALL                     1
                STORE_FAST              11 (iso_now)

 418            LOAD_CONST               0 ('status')
                LOAD_FAST_BORROW         2 (new_status)

 419            LOAD_CONST               9 ('updated_at')
                LOAD_FAST_BORROW        11 (iso_now)

 417            BUILD_MAP                2
                STORE_FAST              12 (patch)

 421            LOAD_FAST_BORROW         2 (new_status)
                LOAD_CONST              10 ('completed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       70 (to L8)
                NOT_TAKEN

 422            LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (iso_now, patch)
                LOAD_CONST              11 ('completed_at')
                STORE_SUBSCR

 425            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (completed_by)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (completed_by)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L6)
                NOT_TAKEN

 424            LOAD_FAST_BORROW         3 (completed_by)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L7)

 426    L6:     LOAD_CONST              12 ('operator')

 423    L7:     LOAD_FAST_BORROW        12 (patch)
                LOAD_CONST              13 ('completed_by')
                STORE_SUBSCR

 428    L8:     LOAD_FAST_BORROW         5 (bump_reminder)
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN

 429            LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (iso_now, patch)
                LOAD_CONST              14 ('last_reminder_at')
                STORE_SUBSCR

 430    L9:     LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (error_code)
                LOAD_GLOBAL              4 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       46 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (error_code)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       24 (to L10)
                NOT_TAKEN

 431            LOAD_FAST_BORROW         4 (error_code)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW        12 (patch)
                LOAD_CONST              15 ('last_error_code')
                STORE_SUBSCR

 432            LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (iso_now, patch)
                LOAD_CONST              16 ('last_error_at')
                STORE_SUBSCR

 434   L10:     NOP

 436   L11:     LOAD_FAST_BORROW         5 (bump_reminder)
                TO_BOOL
                POP_JUMP_IF_FALSE      216 (to L23)
       L12:     NOT_TAKEN

 438   L13:     LOAD_FAST_BORROW         9 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 439            LOAD_ATTR               23 (select + NULL|self)
                LOAD_CONST              17 ('reminder_sent_count')
                CALL                     1

 440            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              18 ('callback_id')
                LOAD_FAST_BORROW         8 (cid)
                CALL                     2

 441            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              19 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)
                CALL                     2

 442            LOAD_ATTR               27 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 443            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 437            STORE_FAST              13 (read)

 445            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        13 (read)
                LOAD_CONST              20 ('data')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              14 (read_rows)

 446            LOAD_FAST_BORROW        14 (read_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L20)
       L17:     NOT_TAKEN

 448   L18:     LOAD_CONST               0 ('status')
                LOAD_CONST              21 ('warning')

 449            LOAD_CONST               2 ('callback')
                LOAD_CONST               3 (None)

 450            LOAD_CONST               4 ('warnings')
                LOAD_CONST              22 ('callback_not_found_or_cross_tenant')
                BUILD_LIST               1

 451            LOAD_CONST               5 ('error_code')
                LOAD_CONST              22 ('callback_not_found_or_cross_tenant')

 447            BUILD_MAP                4
       L19:     RETURN_VALUE

 453   L20:     LOAD_FAST_BORROW        14 (read_rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_ATTR               35 (get + NULL|self)
                LOAD_CONST              17 ('reminder_sent_count')
                CALL                     1
                STORE_FAST              15 (current)

 454            LOAD_GLOBAL              3 (isinstance + NULL)
                LOAD_FAST_BORROW        15 (current)
                LOAD_GLOBAL             36 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L21)
                NOT_TAKEN
                LOAD_FAST_BORROW        15 (current)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN

 455   L21:     LOAD_SMALL_INT           0
                STORE_FAST              15 (current)

 456   L22:     LOAD_FAST_BORROW        15 (current)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW        12 (patch)
                LOAD_CONST              17 ('reminder_sent_count')
                STORE_SUBSCR

 458   L23:     LOAD_FAST_BORROW         9 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 459            LOAD_ATTR               39 (update + NULL|self)
                LOAD_FAST_BORROW        12 (patch)
                CALL                     1

 460            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              18 ('callback_id')
                LOAD_FAST_BORROW         8 (cid)
                CALL                     2

 461            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST              19 ('brokerage_id')
                LOAD_FAST_BORROW         7 (bid)
                CALL                     2

 462            LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0

 457            STORE_FAST              16 (result)

 464            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        16 (result)
                LOAD_CONST              20 ('data')
                LOAD_CONST               3 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L26)
       L24:     NOT_TAKEN
       L25:     POP_TOP
                BUILD_LIST               0
       L26:     CALL                     1
                STORE_FAST              17 (updated)

 465            LOAD_FAST_BORROW        17 (updated)
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L30)
       L27:     NOT_TAKEN

 467   L28:     LOAD_CONST               0 ('status')
                LOAD_CONST              21 ('warning')

 468            LOAD_CONST               2 ('callback')
                LOAD_CONST               3 (None)

 469            LOAD_CONST               4 ('warnings')
                LOAD_CONST              22 ('callback_not_found_or_cross_tenant')
                BUILD_LIST               1

 470            LOAD_CONST               5 ('error_code')
                LOAD_CONST              22 ('callback_not_found_or_cross_tenant')

 466            BUILD_MAP                4
       L29:     RETURN_VALUE

 473   L30:     LOAD_CONST               0 ('status')
                LOAD_CONST              23 ('ok')

 474            LOAD_CONST               2 ('callback')
                LOAD_GLOBAL             41 (_project + NULL)
                LOAD_FAST_BORROW        17 (updated)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1

 475            LOAD_CONST               4 ('warnings')
                BUILD_LIST               0

 476            LOAD_CONST               5 ('error_code')
                LOAD_CONST               3 (None)

 472            BUILD_MAP                4
       L31:     RETURN_VALUE

  --   L32:     PUSH_EXC_INFO

 478            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L37)
                NOT_TAKEN
                STORE_FAST              18 (e)

 479   L33:     LOAD_GLOBAL             44 (logger)
                LOAD_ATTR               47 (warning + NULL|self)

 480            LOAD_CONST              24 ('callback_schedule_store update error type=')

 481            LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              25 (' new_status=')
                LOAD_FAST                2 (new_status)
                FORMAT_SIMPLE

 480            BUILD_STRING             4

 479            CALL                     1
                POP_TOP

 483            LOAD_GLOBAL             13 (_safe_unavailable + NULL)
                LOAD_CONST              26 ('db_write_failed:')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST              27 (('extra_warning',))
                CALL_KW                  1
       L34:     SWAP                     2
       L35:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RETURN_VALUE

  --   L36:     LOAD_CONST               3 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 478   L37:     RERAISE                  0

  --   L38:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L11 to L12 -> L32 [0]
  L13 to L14 -> L32 [0]
  L15 to L17 -> L32 [0]
  L18 to L19 -> L32 [0]
  L20 to L24 -> L32 [0]
  L25 to L27 -> L32 [0]
  L28 to L29 -> L32 [0]
  L30 to L31 -> L32 [0]
  L32 to L33 -> L38 [1] lasti
  L33 to L34 -> L36 [1] lasti
  L34 to L35 -> L38 [1] lasti
  L36 to L38 -> L38 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/callbacks/callback_schedule_store.py", line 486>:
486           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

487           LOAD_CONST               2 ('str')

486           LOAD_CONST               3 ('brokerage_id')

487           LOAD_CONST               2 ('str')

486           LOAD_CONST               4 ('now')

487           LOAD_CONST               5 ('Any')

486           LOAD_CONST               6 ('return')

488           LOAD_CONST               7 ('Dict[str, Any]')

486           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_durable_callback_reminded at 0x0000018C17FA3F00, file "app/services/callbacks/callback_schedule_store.py", line 486>:
486           RESUME                   0

489           LOAD_GLOBAL              1 (_update_status + NULL)

490           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

491           LOAD_CONST               0 ('reminded')
              LOAD_CONST               1 (True)
              LOAD_FAST_BORROW         2 (now)

489           LOAD_CONST               2 (('callback_id', 'brokerage_id', 'new_status', 'bump_reminder', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/callbacks/callback_schedule_store.py", line 495>:
495           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

496           LOAD_CONST               2 ('str')

495           LOAD_CONST               3 ('brokerage_id')

496           LOAD_CONST               2 ('str')

495           LOAD_CONST               4 ('completed_by')

497           LOAD_CONST               5 ('Optional[str]')

495           LOAD_CONST               6 ('now')

497           LOAD_CONST               7 ('Any')

495           LOAD_CONST               8 ('return')

498           LOAD_CONST               9 ('Dict[str, Any]')

495           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object mark_durable_callback_completed at 0x0000018C180B0030, file "app/services/callbacks/callback_schedule_store.py", line 495>:
495           RESUME                   0

499           LOAD_GLOBAL              1 (_update_status + NULL)

500           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

501           LOAD_CONST               0 ('completed')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (completed_by, now)

499           LOAD_CONST               1 (('callback_id', 'brokerage_id', 'new_status', 'completed_by', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app/services/callbacks/callback_schedule_store.py", line 505>:
505           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

506           LOAD_CONST               2 ('str')

505           LOAD_CONST               3 ('brokerage_id')

506           LOAD_CONST               2 ('str')

505           LOAD_CONST               4 ('now')

506           LOAD_CONST               5 ('Any')

505           LOAD_CONST               6 ('return')

507           LOAD_CONST               7 ('Dict[str, Any]')

505           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_durable_callback_overdue at 0x0000018C180B0120, file "app/services/callbacks/callback_schedule_store.py", line 505>:
505           RESUME                   0

508           LOAD_GLOBAL              1 (_update_status + NULL)

509           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

510           LOAD_CONST               0 ('overdue')
              LOAD_CONST               1 ('callback_window_passed')
              LOAD_FAST_BORROW         2 (now)

508           LOAD_CONST               2 (('callback_id', 'brokerage_id', 'new_status', 'error_code', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025630, file "app/services/callbacks/callback_schedule_store.py", line 514>:
514           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

515           LOAD_CONST               2 ('str')

514           LOAD_CONST               3 ('brokerage_id')

515           LOAD_CONST               2 ('str')

514           LOAD_CONST               4 ('now')

515           LOAD_CONST               5 ('Any')

514           LOAD_CONST               6 ('return')

516           LOAD_CONST               7 ('Dict[str, Any]')

514           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_durable_callback_cancelled at 0x0000018C180B0210, file "app/services/callbacks/callback_schedule_store.py", line 514>:
514           RESUME                   0

517           LOAD_GLOBAL              1 (_update_status + NULL)

518           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (callback_id, brokerage_id)

519           LOAD_CONST               0 ('cancelled')
              LOAD_FAST_BORROW         2 (now)

517           LOAD_CONST               1 (('callback_id', 'brokerage_id', 'new_status', 'now'))
              CALL_KW                  4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/callbacks/callback_schedule_store.py", line 523>:
523           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('callback_id')

524           LOAD_CONST               2 ('str')

523           LOAD_CONST               3 ('brokerage_id')

524           LOAD_CONST               2 ('str')

523           LOAD_CONST               4 ('error_code')

525           LOAD_CONST               5 ('Optional[str]')

523           LOAD_CONST               6 ('now')

525           LOAD_CONST               7 ('Any')

523           LOAD_CONST               8 ('return')

526           LOAD_CONST               9 ('Dict[str, Any]')

523           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object mark_durable_callback_failed at 0x0000018C18090470, file "app/services/callbacks/callback_schedule_store.py", line 523>:
523           RESUME                   0

527           LOAD_GLOBAL              1 (_update_status + NULL)

528           LOAD_FAST_LOAD_FAST      1 (callback_id, brokerage_id)

529           LOAD_CONST               0 ('failed')

530           LOAD_FAST                2 (error_code)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('callback_failed')

531   L1:     LOAD_FAST_BORROW         3 (now)

527           LOAD_CONST               2 (('callback_id', 'brokerage_id', 'new_status', 'error_code', 'now'))
              CALL_KW                  5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app/services/callbacks/callback_schedule_store.py", line 539>:
539           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

540           LOAD_CONST               2 ('str')

539           LOAD_CONST               3 ('status')

542           LOAD_CONST               2 ('str')

539           LOAD_CONST               4 ('limit')

543           LOAD_CONST               5 ('Any')

539           LOAD_CONST               6 ('return')

544           LOAD_CONST               7 ('Dict[str, Any]')

539           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_durable_callbacks at 0x0000018C17D43500, file "app/services/callbacks/callback_schedule_store.py", line 539>:
 539            RESUME                   0

 551            LOAD_GLOBAL              1 (_validate_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       28 (to L1)
                NOT_TAKEN

 553            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 554            LOAD_CONST               3 ('brokerage_id')
                LOAD_CONST               4 (None)

 555            LOAD_CONST               5 ('filter_status')
                LOAD_FAST_BORROW         1 (status)

 556            LOAD_CONST               6 ('limit')
                LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 557            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 558            LOAD_CONST               8 ('callbacks')
                BUILD_LIST               0

 559            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 560            LOAD_CONST              10 ('error_code')
                LOAD_CONST              11 ('missing_brokerage_id')

 552            BUILD_MAP                8
                RETURN_VALUE

 562    L1:     LOAD_GLOBAL              5 (_validate_status_for_filter + NULL)
                LOAD_FAST_BORROW         1 (status)
                CALL                     1
                STORE_FAST               3 (err)

 563            LOAD_FAST_BORROW         3 (err)
                POP_JUMP_IF_NONE        42 (to L2)
                NOT_TAKEN

 565            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 566            LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0

 567            LOAD_CONST               5 ('filter_status')
                LOAD_FAST_BORROW         1 (status)

 568            LOAD_CONST               6 ('limit')
                LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 569            LOAD_CONST               7 ('count')
                LOAD_SMALL_INT           0

 570            LOAD_CONST               8 ('callbacks')
                BUILD_LIST               0

 571            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 572            LOAD_CONST              10 ('error_code')
                LOAD_FAST_BORROW         3 (err)

 564            BUILD_MAP                8
                RETURN_VALUE

 574    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (bid)

 575            LOAD_FAST_BORROW         1 (status)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (filter_status)

 576            LOAD_GLOBAL              3 (_clamp_limit + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               6 (capped)

 577            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 578            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE    30 (to L3)
                NOT_TAKEN

 579            LOAD_GLOBAL             13 (_safe_unavailable + NULL)
                CALL                     0
                STORE_FAST               8 (env)

 580            LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (bid, env)
                LOAD_CONST               3 ('brokerage_id')
                STORE_SUBSCR

 581            LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (filter_status, env)
                LOAD_CONST               5 ('filter_status')
                STORE_SUBSCR

 582            LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (capped, env)
                LOAD_CONST               6 ('limit')
                STORE_SUBSCR

 583            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST               7 ('count')
                STORE_SUBSCR

 584            LOAD_FAST_BORROW         8 (env)
                RETURN_VALUE

 585    L3:     NOP

 587    L4:     LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE)
                CALL                     1

 588            LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST              12 (',')
                LOAD_ATTR               21 (join + NULL|self)
                LOAD_GLOBAL             22 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 589            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)
                CALL                     2

 590            LOAD_ATTR               25 (eq + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW         5 (filter_status)
                CALL                     2

 591            LOAD_ATTR               27 (order + NULL|self)
                LOAD_CONST              13 ('scheduled_for')
                CALL                     1

 592            LOAD_ATTR               29 (limit + NULL|self)
                LOAD_FAST_BORROW         6 (capped)
                CALL                     1

 593            LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0

 586            STORE_FAST               9 (result)

 595            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              14 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST              10 (rows)

 596            LOAD_CONST              15 (<code object <genexpr> at 0x0000018C180907A0, file "app/services/callbacks/callback_schedule_store.py", line 596>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW        10 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR     11 (p)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                10 (to L12)
                STORE_FAST_LOAD_FAST   187 (p, p)
       L10:     POP_JUMP_IF_NOT_NONE     3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L9)
       L11:     LOAD_FAST_BORROW        11 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST              12 (projected)
                STORE_FAST              11 (p)

 598            LOAD_CONST               1 ('status')
                LOAD_CONST              16 ('ok')

 599            LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         4 (bid)

 600            LOAD_CONST               5 ('filter_status')
                LOAD_FAST_BORROW         5 (filter_status)

 601            LOAD_CONST               6 ('limit')
                LOAD_FAST_BORROW         6 (capped)

 602            LOAD_CONST               7 ('count')
                LOAD_GLOBAL             37 (len + NULL)
                LOAD_FAST_BORROW        12 (projected)
                CALL                     1

 603            LOAD_CONST               8 ('callbacks')
                LOAD_FAST_BORROW        12 (projected)

 604            LOAD_CONST               9 ('warnings')
                BUILD_LIST               0

 605            LOAD_CONST              10 ('error_code')
                LOAD_CONST               4 (None)

 597            BUILD_MAP                8
       L14:     RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 596            SWAP                     2
                STORE_FAST              11 (p)
                RERAISE                  0

  --   L16:     PUSH_EXC_INFO

 607            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      107 (to L21)
                NOT_TAKEN
                STORE_FAST              13 (e)

 608   L17:     LOAD_GLOBAL             40 (logger)
                LOAD_ATTR               43 (warning + NULL|self)

 609            LOAD_CONST              17 ('list_durable_callbacks db error type=')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 608            CALL                     1
                POP_TOP

 611            LOAD_GLOBAL             13 (_safe_unavailable + NULL)
                LOAD_CONST              18 ('db_read_failed:')
                LOAD_GLOBAL             45 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               46 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST              19 (('extra_warning',))
                CALL_KW                  1
                STORE_FAST               8 (env)

 612            LOAD_FAST_LOAD_FAST     72 (bid, env)
                LOAD_CONST               3 ('brokerage_id')
                STORE_SUBSCR

 613            LOAD_FAST_LOAD_FAST     88 (filter_status, env)
                LOAD_CONST               5 ('filter_status')
                STORE_SUBSCR

 614            LOAD_FAST_LOAD_FAST    104 (capped, env)
                LOAD_CONST               6 ('limit')
                STORE_SUBSCR

 615            LOAD_SMALL_INT           0
                LOAD_FAST                8 (env)
                LOAD_CONST               7 ('count')
                STORE_SUBSCR

 616            LOAD_FAST                8 (env)
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               4 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 607   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L5 -> L16 [0]
  L6 to L8 -> L16 [0]
  L8 to L10 -> L15 [2]
  L11 to L13 -> L15 [2]
  L13 to L14 -> L16 [0]
  L15 to L16 -> L16 [0]
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C180907A0, file "app/services/callbacks/callback_schedule_store.py", line 596>:
 596           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project + NULL)
               LOAD_FAST_BORROW         1 (r)
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

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/callbacks/callback_schedule_store.py", line 619>:
619           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

620           LOAD_CONST               2 ('str')

619           LOAD_CONST               3 ('lookahead_minutes')

622           LOAD_CONST               4 ('Any')

619           LOAD_CONST               5 ('now')

623           LOAD_CONST               4 ('Any')

619           LOAD_CONST               6 ('return')

624           LOAD_CONST               7 ('Dict[str, Any]')

619           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object durable_reminder_report at 0x0000018C17D43F80, file "app/services/callbacks/callback_schedule_store.py", line 619>:
 619            RESUME                   0

 632            LOAD_GLOBAL              1 (_validate_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       50 (to L1)
                NOT_TAKEN

 634            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 635            LOAD_CONST               3 ('brokerage_id')
                LOAD_CONST               4 (None)

 636            LOAD_CONST               5 ('lookahead_minutes')
                LOAD_GLOBAL              3 (_clamp_lookahead + NULL)
                LOAD_FAST_BORROW         1 (lookahead_minutes)
                CALL                     1

 637            LOAD_CONST               6 ('now')
                LOAD_GLOBAL              5 (_iso + NULL)
                LOAD_GLOBAL              7 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                CALL                     1

 638            LOAD_CONST               7 ('due_count')
                LOAD_SMALL_INT           0

 639            LOAD_CONST               8 ('due')
                BUILD_LIST               0

 640            LOAD_CONST               9 ('overdue_count')
                LOAD_SMALL_INT           0

 641            LOAD_CONST              10 ('overdue')
                BUILD_LIST               0

 642            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 643            LOAD_CONST              12 ('error_code')
                LOAD_CONST              13 ('missing_brokerage_id')

 633            BUILD_MAP               10
                RETURN_VALUE

 645    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                STORE_FAST               3 (bid)

 646            LOAD_GLOBAL              3 (_clamp_lookahead + NULL)
                LOAD_FAST_BORROW         1 (lookahead_minutes)
                CALL                     1
                STORE_FAST               4 (lookahead)

 647            LOAD_GLOBAL              7 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               5 (now_dt)

 648            LOAD_FAST_BORROW         5 (now_dt)
                LOAD_GLOBAL             11 (timedelta + NULL)
                LOAD_FAST_BORROW         4 (lookahead)
                LOAD_CONST              14 (('minutes',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                STORE_FAST               6 (upper)

 649            LOAD_GLOBAL             13 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 650            LOAD_FAST_BORROW         7 (db)
                POP_JUMP_IF_NOT_NONE    55 (to L2)
                NOT_TAKEN

 651            LOAD_GLOBAL             15 (_safe_unavailable + NULL)
                CALL                     0
                STORE_FAST               8 (env)

 652            LOAD_FAST_BORROW_LOAD_FAST_BORROW 56 (bid, env)
                LOAD_CONST               3 ('brokerage_id')
                STORE_SUBSCR

 653            LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (lookahead, env)
                LOAD_CONST               5 ('lookahead_minutes')
                STORE_SUBSCR

 654            LOAD_GLOBAL              5 (_iso + NULL)
                LOAD_FAST_BORROW         5 (now_dt)
                CALL                     1
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST               6 ('now')
                STORE_SUBSCR

 655            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST               7 ('due_count')
                STORE_SUBSCR

 656            BUILD_LIST               0
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST               8 ('due')
                STORE_SUBSCR

 657            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST               9 ('overdue_count')
                STORE_SUBSCR

 658            BUILD_LIST               0
                LOAD_FAST_BORROW         8 (env)
                LOAD_CONST              10 ('overdue')
                STORE_SUBSCR

 659            LOAD_FAST_BORROW         8 (env)
                RETURN_VALUE

 660    L2:     NOP

 662    L3:     LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE)
                CALL                     1

 663            LOAD_ATTR               21 (select + NULL|self)
                LOAD_CONST              15 (',')
                LOAD_ATTR               23 (join + NULL|self)
                LOAD_GLOBAL             24 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 664            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 665            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               1 ('status')
                LOAD_CONST              16 ('pending')
                CALL                     2

 666            LOAD_ATTR               29 (order + NULL|self)
                LOAD_CONST              17 ('scheduled_for')
                CALL                     1

 667            LOAD_ATTR               31 (limit + NULL|self)
                LOAD_GLOBAL             32 (_LIST_HARD_CAP)
                CALL                     1

 668            LOAD_ATTR               35 (execute + NULL|self)
                CALL                     0

 661            STORE_FAST               9 (result)

 670            LOAD_GLOBAL             37 (list + NULL)
                LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST              18 ('data')
                LOAD_CONST               4 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
                STORE_FAST              10 (rows)

 671            BUILD_LIST               0
                STORE_FAST              11 (due)

 672            BUILD_LIST               0
                STORE_FAST              12 (overdue)

 673            LOAD_FAST_BORROW        10 (rows)
                GET_ITER
        L7:     FOR_ITER               102 (to L13)
                STORE_FAST              13 (r)

 674            LOAD_GLOBAL             41 (_project + NULL)
                LOAD_FAST_BORROW        13 (r)
                CALL                     1
                STORE_FAST              14 (projected)

 675            LOAD_FAST_BORROW        14 (projected)
                POP_JUMP_IF_NOT_NONE     3 (to L8)
                NOT_TAKEN

 676            JUMP_BACKWARD           20 (to L7)

 677    L8:     LOAD_GLOBAL             43 (_coerce_scheduled_for + NULL)
                LOAD_FAST_BORROW        14 (projected)
                LOAD_ATTR               45 (get + NULL|self)
                LOAD_CONST              17 ('scheduled_for')
                CALL                     1
                CALL                     1
                STORE_FAST              15 (sched)

 678            LOAD_FAST_BORROW        15 (sched)
                POP_JUMP_IF_NOT_NONE     3 (to L9)
                NOT_TAKEN

 679            JUMP_BACKWARD           52 (to L7)

 680    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 245 (sched, now_dt)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       20 (to L10)
                NOT_TAKEN

 681            LOAD_FAST_BORROW        12 (overdue)
                LOAD_ATTR               47 (append + NULL|self)
                LOAD_FAST_BORROW        14 (projected)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           77 (to L7)

 682   L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 246 (sched, upper)
                COMPARE_OP              58 (bool(<=))
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           85 (to L7)

 683   L12:     LOAD_FAST_BORROW        11 (due)
                LOAD_ATTR               47 (append + NULL|self)
                LOAD_FAST_BORROW        14 (projected)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          104 (to L7)

 673   L13:     END_FOR
                POP_ITER

 685            LOAD_CONST               1 ('status')
                LOAD_CONST              19 ('ok')

 686            LOAD_CONST               3 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 687            LOAD_CONST               5 ('lookahead_minutes')
                LOAD_FAST_BORROW         4 (lookahead)

 688            LOAD_CONST               6 ('now')
                LOAD_GLOBAL              5 (_iso + NULL)
                LOAD_FAST_BORROW         5 (now_dt)
                CALL                     1

 689            LOAD_CONST               7 ('due_count')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW        11 (due)
                CALL                     1

 690            LOAD_CONST               8 ('due')
                LOAD_FAST_BORROW        11 (due)

 691            LOAD_CONST               9 ('overdue_count')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW        12 (overdue)
                CALL                     1

 692            LOAD_CONST              10 ('overdue')
                LOAD_FAST_BORROW        12 (overdue)

 693            LOAD_CONST              11 ('warnings')
                BUILD_LIST               0

 694            LOAD_CONST              12 ('error_code')
                LOAD_CONST               4 (None)

 684            BUILD_MAP               10
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 696            LOAD_GLOBAL             50 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      132 (to L20)
                NOT_TAKEN
                STORE_FAST              16 (e)

 697   L16:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 698            LOAD_CONST              20 ('durable_reminder_report db error type=')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 697            CALL                     1
                POP_TOP

 700            LOAD_GLOBAL             15 (_safe_unavailable + NULL)
                LOAD_CONST              21 ('db_read_failed:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_CONST              22 (('extra_warning',))
                CALL_KW                  1
                STORE_FAST               8 (env)

 701            LOAD_FAST_LOAD_FAST     56 (bid, env)
                LOAD_CONST               3 ('brokerage_id')
                STORE_SUBSCR

 702            LOAD_FAST_LOAD_FAST     72 (lookahead, env)
                LOAD_CONST               5 ('lookahead_minutes')
                STORE_SUBSCR

 703            LOAD_GLOBAL              5 (_iso + NULL)
                LOAD_FAST                5 (now_dt)
                CALL                     1
                LOAD_FAST                8 (env)
                LOAD_CONST               6 ('now')
                STORE_SUBSCR

 704            LOAD_SMALL_INT           0
                LOAD_FAST                8 (env)
                LOAD_CONST               7 ('due_count')
                STORE_SUBSCR

 705            BUILD_LIST               0
                LOAD_FAST                8 (env)
                LOAD_CONST               8 ('due')
                STORE_SUBSCR

 706            LOAD_SMALL_INT           0
                LOAD_FAST                8 (env)
                LOAD_CONST               9 ('overdue_count')
                STORE_SUBSCR

 707            BUILD_LIST               0
                LOAD_FAST                8 (env)
                LOAD_CONST              10 ('overdue')
                STORE_SUBSCR

 708            LOAD_FAST                8 (env)
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               4 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 696   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L15 [0]
  L5 to L11 -> L15 [0]
  L12 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti
```
