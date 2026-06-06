# brokerage/profile_service

- **pyc:** `app\services\brokerage\__pycache__\profile_service.cpython-314.pyc`
- **expected source path (absent):** `app\services\brokerage/profile_service.py`
- **co_filename (from bytecode):** `app\services\brokerage\profile_service.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** brokerage

## Module docstring

```
PAS173 — Brokerage profile service (Supabase-backed v1).

Operator-facing surface for the brokerage operational profile
side-car table ``pas_brokerage_profiles`` (proposal at
``scripts/migrate_v21_brokerage_profiles.sql``). The profile
holds ONLY operational lifecycle columns (onboarding_status,
pilot_stage, timezone, market, features/metadata) — secrets,
API keys, and per-brokerage Twilio/Slack values stay on the
existing ``brokerages`` table and are NEVER projected here.

Doctrine carried by every helper:

* **No PII.** No phone / email / name / transcript / raw
  payload anywhere. The ``features`` and ``metadata`` JSONB
  columns are projected against a closed allow-list at write
  time; anything outside the list is dropped.
* **No secrets.** The profile service NEVER reads or echoes
  ``api_key``, ``twilio_*``, ``slack_webhook_url``, or any
  env value.
* **Structural envelopes only.** Every helper returns
  ``{status, profile|profiles|None, warnings, error_code}``;
  NEVER raises.
* **DB unavailable** → ``status="skipped"`` envelope. The
  caller (operator route) collapses to a structural 200.
* **Tenant write denied at the DB layer** (RLS); the service
  layer also rejects non-allow-list status / pilot_stage
  inputs so a mis-routed call cannot smuggle a bogus token.
* **Audit-safe.** Every status-changing helper takes an
  ``actor_id`` kwarg the operator route fills from
  X-Admin-Key context; this lands in the structural metadata
  for forensic correlation but is NEVER stored as a secret.

Public surface:

  * ``ensure_profile(...)``       — idempotent insert.
  * ``get_profile(brokerage_id)``  — structural single read.
  * ``list_profiles(...)``         — multi-brokerage operator view.
  * ``update_onboarding_status(...)`` — closed enum transition.
  * ``update_pilot_stage(...)``    — closed enum transition.
  * ``pause_brokerage(...)``       — convenience wrapper.
  * ``resume_brokerage(...)``      — convenience wrapper.
  * ``mark_onboarding_completed(...)`` — sets timestamp.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `datetime`, `get_supabase`, `logging`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_get_db_safe`, `_is_unique_violation`, `_iso`, `_list_envelope`, `_now_dt`, `_project_features`, `_project_metadata`, `_project_row`, `_safe_envelope`, `_update_status_columns`, `_validate_brokerage_id`, `_validate_onboarding_status`, `_validate_pilot_stage`, `ensure_profile`, `get_profile`, `list_profiles`, `mark_onboarding_completed`, `pause_brokerage`, `resume_brokerage`, `update_onboarding_status`, `update_pilot_stage`

## Env-key candidates

`INTERNAL`, `LIVE`, `NOT_STARTED`, `PAUSED`, `VERIFIED`

## String constants (redacted where noted)

- '\nPAS173 — Brokerage profile service (Supabase-backed v1).\n\nOperator-facing surface for the brokerage operational profile\nside-car table ``pas_brokerage_profiles`` (proposal at\n``scripts/migrate_v21_brokerage_profiles.sql``). The profile\nholds ONLY operational lifecycle columns (onboarding_status,\npilot_stage, timezone, market, features/metadata) — secrets,\nAPI keys, and per-brokerage Twilio/Slack values stay on the\nexisting ``brokerages`` table and are NEVER projected here.\n\nDoctrine carried by every helper:\n\n* **No PII.** No phone / email / name / transcript / raw\n  payload anywhere. The ``features`` and ``metadata`` JSONB\n  columns are projected against a closed allow-list at write\n  time; anything outside the list is dropped.\n* **No secrets.** The profile service NEVER reads or echoes\n  ``api_key``, ``twilio_*``, ``slack_webhook_url``, or any\n  env value.\n* **Structural envelopes only.** Every helper returns\n  ``{status, profile|profiles|None, warnings, error_code}``;\n  NEVER raises.\n* **DB unavailable** → ``status="skipped"`` envelope. The\n  caller (operator route) collapses to a structural 200.\n* **Tenant write denied at the DB layer** (RLS); the service\n  layer also rejects non-allow-list status / pilot_stage\n  inputs so a mis-routed call cannot smuggle a bogus token.\n* **Audit-safe.** Every status-changing helper takes an\n  ``actor_id`` kwarg the operator route fills from\n  X-Admin-Key context; this lands in the structural metadata\n  for forensic correlation but is NEVER stored as a secret.\n\nPublic surface:\n\n  * ``ensure_profile(...)``       — idempotent insert.\n  * ``get_profile(brokerage_id)``  — structural single read.\n  * ``list_profiles(...)``         — multi-brokerage operator view.\n  * ``update_onboarding_status(...)`` — closed enum transition.\n  * ``update_pilot_stage(...)``    — closed enum transition.\n  * ``pause_brokerage(...)``       — convenience wrapper.\n  * ``resume_brokerage(...)``      — convenience wrapper.\n  * ``mark_onboarding_completed(...)`` — sets timestamp.\n'
- 'pas.brokerage.profile_service'
- 'pas_brokerage_profiles'
- 'NOT_STARTED'
- 'VERIFIED'
- 'INTERNAL'
- 'brokerage_name'
- 'market'
- 'onboarding_status'
- 'pilot_stage'
- 'onboarding_owner'
- 'config_version'
- 'features'
- 'metadata'
- 'profile'
- 'warnings'
- 'error_code'
- 'profiles'
- 'count'
- 'limit'
- 'filter_status'
- 'filter_stage'
- 'timezone_name'
- 'now'
- 'actor_id'
- 'target_status'
- 'completed'
- 'extra_metadata'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'profile_service db client unavailable type='
- 'value'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'notes_token'
- 'row'
- 'Optional[Dict[str, Any]]'
- 'missing_brokerage_id'
- 'brokerage_id_too_long'
- 'invalid_onboarding_status'
- 'invalid_pilot_stage'
- 'status'
- 'Optional[List[str]]'
- 'Optional[List[Dict[str, Any]]]'
- 'brokerage_id'
- 'Insert a profile row if missing; return the projected row.\nIdempotent — on conflict, returns the existing row (does\nNOT clobber). NEVER raises.'
- 'failed'
- 'skipped'
- 'brokerage_profile_store_unavailable'
- 'timezone'
- 'created_at'
- 'updated_at'
- 'data'
- 'ensure_profile insert error type='
- 'db_write_failed:'
- 'new_status'
- 'Transition the onboarding status. ``actor_id`` is the\nORVN operator who triggered the transition; bounded and\nstored in metadata.last_stage_actor for forensic trace.\nNEVER raises.'
- 'onboarding'
- 'LIVE'
- 'new_stage'
- 'PAUSED'
- 'last_paused_at'
- 'invalid_resume_target'
- 'last_resumed_at'
- 'onboarding_completed_at'
- 'patch'
- 'validate_status'
- 'validate_kind'
- 'bool'
- 'brokerage_profile_not_found'
- '_update_status_columns read error type='
- 'db_read_failed:'
- 'last_stage_change_at'
- 'last_stage_actor'
- '_update_status_columns update error type='
- 'get_profile read error type='
- 'list_profiles read error type='
- 'exc'
- 'BaseException'
- '23505'
- 'duplicate key value violates unique constraint'
- 'already exists'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS173 — Brokerage profile service (Supabase-backed v1).\n\nOperator-facing surface for the brokerage operational profile\nside-car table ``pas_brokerage_profiles`` (proposal at\n``scripts/migrate_v21_brokerage_profiles.sql``). The profile\nholds ONLY operational lifecycle columns (onboarding_status,\npilot_stage, timezone, market, features/metadata) — secrets,\nAPI keys, and per-brokerage Twilio/Slack values stay on the\nexisting ``brokerages`` table and are NEVER projected here.\n\nDoctrine carried by every helper:\n\n* **No PII.** No phone / email / name / transcript / raw\n  payload anywhere. The ``features`` and ``metadata`` JSONB\n  columns are projected against a closed allow-list at write\n  time; anything outside the list is dropped.\n* **No secrets.** The profile service NEVER reads or echoes\n  ``api_key``, ``twilio_*``, ``slack_webhook_url``, or any\n  env value.\n* **Structural envelopes only.** Every helper returns\n  ``{status, profile|profiles|None, warnings, error_code}``;\n  NEVER raises.\n* **DB unavailable** → ``status="skipped"`` envelope. The\n  caller (operator route) collapses to a structural 200.\n* **Tenant write denied at the DB layer** (RLS); the service\n  layer also rejects non-allow-list status / pilot_stage\n  inputs so a mis-routed call cannot smuggle a bogus token.\n* **Audit-safe.** Every status-changing helper takes an\n  ``actor_id`` kwarg the operator route fills from\n  X-Admin-Key context; this lands in the structural metadata\n  for forensic correlation but is NEVER stored as a secret.\n\nPublic surface:\n\n  * ``ensure_profile(...)``       — idempotent insert.\n  * ``get_profile(brokerage_id)``  — structural single read.\n  * ``list_profiles(...)``         — multi-brokerage operator view.\n  * ``update_onboarding_status(...)`` — closed enum transition.\n  * ``update_pilot_stage(...)``    — closed enum transition.\n  * ``pause_brokerage(...)``       — convenience wrapper.\n  * ``resume_brokerage(...)``      — convenience wrapper.\n  * ``mark_onboarding_completed(...)`` — sets timestamp.\n')
              STORE_NAME               0 (__doc__)

 46           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 48           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 49           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              4 (datetime)
              IMPORT_FROM              4 (datetime)
              STORE_NAME               4 (datetime)
              IMPORT_FROM              5 (timezone)
              STORE_NAME               5 (timezone)
              POP_TOP

 50           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              POP_TOP

 53           LOAD_NAME                3 (logging)
              LOAD_ATTR               22 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.brokerage.profile_service')
              CALL                     1
              STORE_NAME              12 (logger)

 56           LOAD_CONST               6 ('pas_brokerage_profiles')
              STORE_NAME              13 (_TABLE)

 59           LOAD_CONST              77 (('NOT_STARTED', 'IN_PROGRESS', 'CONFIGURED', 'VERIFIED', 'LIVE', 'PAUSED'))
              STORE_NAME              14 (ALLOWED_ONBOARDING_STATUSES)

 68           LOAD_CONST              78 (('INTERNAL', 'TRUSTED_PILOT', 'EXPANDED_PILOT', 'PRODUCTION'))
              STORE_NAME              15 (ALLOWED_PILOT_STAGES)

 78           LOAD_CONST              79 (('transfer_enabled', 'booking_enabled', 'ai_disclosure_enabled', 'heartbeat_enabled', 'durable_dedupe_enabled', 'durable_callbacks_enabled', 'alert_slack_enabled'))
              STORE_NAME              16 (ALLOWED_FEATURES_KEYS)

 89           LOAD_CONST              80 (('config_version_history', 'last_readiness_snapshot_at', 'last_paused_at', 'last_resumed_at', 'last_stage_change_at', 'last_stage_actor', 'notes_token'))
              STORE_NAME              17 (ALLOWED_METADATA_KEYS)

100           LOAD_SMALL_INT         200
              STORE_NAME              18 (_BROKERAGE_ID_MAX_LEN)

101           LOAD_SMALL_INT         200
              STORE_NAME              19 (_BROKERAGE_NAME_MAX_LEN)

102           LOAD_SMALL_INT         200
              STORE_NAME              20 (_OWNER_MAX_LEN)

103           LOAD_SMALL_INT         100
              STORE_NAME              21 (_CONFIG_VERSION_MAX_LEN)

104           LOAD_SMALL_INT         100
              STORE_NAME              22 (_TIMEZONE_MAX_LEN)

105           LOAD_SMALL_INT         100
              STORE_NAME              23 (_MARKET_MAX_LEN)

106           LOAD_SMALL_INT         200
              STORE_NAME              24 (_NOTES_TOKEN_MAX_LEN)

107           LOAD_CONST              10 (500)
              STORE_NAME              25 (_LIST_HARD_CAP)

108           LOAD_SMALL_INT          50
              STORE_NAME              26 (_DEFAULT_LIMIT)

111           LOAD_CONST              81 (('brokerage_id', 'brokerage_name', 'timezone', 'market', 'onboarding_status', 'pilot_stage', 'onboarding_completed_at', 'onboarding_owner', 'config_version', 'features', 'metadata', 'created_at', 'updated_at'))
              STORE_NAME              27 (_STRUCTURAL_COLUMNS)

132           LOAD_CONST              82 ((None,))
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2010, file "app\services\brokerage\profile_service.py", line 132>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _now_dt at 0x0000018C179C3A50, file "app\services\brokerage\profile_service.py", line 132>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              28 (_now_dt)

140           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\brokerage\profile_service.py", line 140>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _iso at 0x0000018C18025030, file "app\services\brokerage\profile_service.py", line 140>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_iso)

144           LOAD_CONST              23 (<code object _get_db_safe at 0x0000018C17FF0F30, file "app\services\brokerage\profile_service.py", line 144>)
              MAKE_FUNCTION
              STORE_NAME              30 (_get_db_safe)

156           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\brokerage\profile_service.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _bound_str at 0x0000018C17972550, file "app\services\brokerage\profile_service.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_bound_str)

167           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\brokerage\profile_service.py", line 167>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object _project_features at 0x0000018C17FA92F0, file "app\services\brokerage\profile_service.py", line 167>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (_project_features)

177           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\brokerage\profile_service.py", line 177>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _project_metadata at 0x0000018C17EDF800, file "app\services\brokerage\profile_service.py", line 177>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_project_metadata)

200           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\brokerage\profile_service.py", line 200>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _project_row at 0x0000018C179A7290, file "app\services\brokerage\profile_service.py", line 200>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_project_row)

212           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\brokerage\profile_service.py", line 212>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object _validate_brokerage_id at 0x0000018C18010B30, file "app\services\brokerage\profile_service.py", line 212>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              35 (_validate_brokerage_id)

220           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\brokerage\profile_service.py", line 220>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object _validate_onboarding_status at 0x0000018C17FA2E20, file "app\services\brokerage\profile_service.py", line 220>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              36 (_validate_onboarding_status)

226           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\brokerage\profile_service.py", line 226>)
              MAKE_FUNCTION
              LOAD_CONST              37 (<code object _validate_pilot_stage at 0x0000018C17FA3000, file "app\services\brokerage\profile_service.py", line 226>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_validate_pilot_stage)

232           LOAD_CONST              38 ('profile')

235           LOAD_CONST               2 (None)

232           LOAD_CONST              39 ('warnings')

236           LOAD_CONST               2 (None)

232           LOAD_CONST              40 ('error_code')

237           LOAD_CONST               2 (None)

232           BUILD_MAP                3
              LOAD_CONST              41 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\brokerage\profile_service.py", line 232>)
              MAKE_FUNCTION
              LOAD_CONST              42 (<code object _safe_envelope at 0x0000018C18090140, file "app\services\brokerage\profile_service.py", line 232>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (_safe_envelope)

247           LOAD_CONST              43 ('profiles')

250           LOAD_CONST               2 (None)

247           LOAD_CONST              44 ('count')

251           LOAD_SMALL_INT           0

247           LOAD_CONST              45 ('limit')

252           LOAD_NAME               26 (_DEFAULT_LIMIT)

247           LOAD_CONST              46 ('filter_status')

253           LOAD_CONST               2 (None)

247           LOAD_CONST              47 ('filter_stage')

254           LOAD_CONST               2 (None)

247           LOAD_CONST              39 ('warnings')

255           LOAD_CONST               2 (None)

247           LOAD_CONST              40 ('error_code')

256           LOAD_CONST               2 (None)

247           BUILD_MAP                7
              LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18090250, file "app\services\brokerage\profile_service.py", line 247>)
              MAKE_FUNCTION
              LOAD_CONST              49 (<code object _list_envelope at 0x0000018C17FE13E0, file "app\services\brokerage\profile_service.py", line 247>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              39 (_list_envelope)

274           LOAD_CONST              11 ('brokerage_name')

277           LOAD_CONST               2 (None)

274           LOAD_CONST              50 ('timezone_name')

278           LOAD_CONST               2 (None)

274           LOAD_CONST              12 ('market')

279           LOAD_CONST               2 (None)

274           LOAD_CONST              15 ('onboarding_owner')

280           LOAD_CONST               2 (None)

274           LOAD_CONST              16 ('config_version')

281           LOAD_CONST               2 (None)

274           LOAD_CONST              17 ('features')

282           LOAD_CONST               2 (None)

274           LOAD_CONST              18 ('metadata')

283           LOAD_CONST               2 (None)

274           LOAD_CONST              13 ('onboarding_status')

284           LOAD_CONST               7 ('NOT_STARTED')

274           LOAD_CONST              14 ('pilot_stage')

285           LOAD_CONST               9 ('INTERNAL')

274           LOAD_CONST              51 ('now')

286           LOAD_CONST               2 (None)

274           BUILD_MAP               10
              LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18053090, file "app\services\brokerage\profile_service.py", line 274>)
              MAKE_FUNCTION
              LOAD_CONST              53 (<code object ensure_profile at 0x0000018C17ED2600, file "app\services\brokerage\profile_service.py", line 274>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              40 (ensure_profile)

351           LOAD_CONST              54 ('actor_id')

355           LOAD_CONST               2 (None)

351           LOAD_CONST              51 ('now')

356           LOAD_CONST               2 (None)

351           BUILD_MAP                2
              LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\brokerage\profile_service.py", line 351>)
              MAKE_FUNCTION
              LOAD_CONST              56 (<code object update_onboarding_status at 0x0000018C18024F30, file "app\services\brokerage\profile_service.py", line 351>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              41 (update_onboarding_status)

373           LOAD_CONST              54 ('actor_id')

377           LOAD_CONST               2 (None)

373           LOAD_CONST              51 ('now')

378           LOAD_CONST               2 (None)

373           BUILD_MAP                2
              LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18025530, file "app\services\brokerage\profile_service.py", line 373>)
              MAKE_FUNCTION
              LOAD_CONST              58 (<code object update_pilot_stage at 0x0000018C18025830, file "app\services\brokerage\profile_service.py", line 373>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              42 (update_pilot_stage)

390           LOAD_CONST              54 ('actor_id')

393           LOAD_CONST               2 (None)

390           LOAD_CONST              51 ('now')

394           LOAD_CONST               2 (None)

390           BUILD_MAP                2
              LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18025930, file "app\services\brokerage\profile_service.py", line 390>)
              MAKE_FUNCTION
              LOAD_CONST              60 (<code object pause_brokerage at 0x0000018C17C49B80, file "app\services\brokerage\profile_service.py", line 390>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              43 (pause_brokerage)

408           LOAD_CONST              54 ('actor_id')

411           LOAD_CONST               2 (None)

408           LOAD_CONST              61 ('target_status')

412           LOAD_CONST               8 ('VERIFIED')

408           LOAD_CONST              51 ('now')

413           LOAD_CONST               2 (None)

408           BUILD_MAP                3
              LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18025A30, file "app\services\brokerage\profile_service.py", line 408>)
              MAKE_FUNCTION
              LOAD_CONST              63 (<code object resume_brokerage at 0x0000018C17F95E60, file "app\services\brokerage\profile_service.py", line 408>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              44 (resume_brokerage)

433           LOAD_CONST              54 ('actor_id')

436           LOAD_CONST               2 (None)

433           LOAD_CONST              51 ('now')

437           LOAD_CONST               2 (None)

433           BUILD_MAP                2
              LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18025B30, file "app\services\brokerage\profile_service.py", line 433>)
              MAKE_FUNCTION
              LOAD_CONST              65 (<code object mark_onboarding_completed at 0x0000018C1802C750, file "app\services\brokerage\profile_service.py", line 433>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              45 (mark_onboarding_completed)

454           LOAD_CONST              54 ('actor_id')

460           LOAD_CONST               2 (None)

454           LOAD_CONST              66 ('completed')

461           LOAD_CONST              67 (False)

454           LOAD_CONST              68 ('extra_metadata')

462           LOAD_CONST               2 (None)

454           LOAD_CONST              51 ('now')

463           LOAD_CONST               2 (None)

454           BUILD_MAP                4
              LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18090580, file "app\services\brokerage\profile_service.py", line 454>)
              MAKE_FUNCTION
              LOAD_CONST              70 (<code object _update_status_columns at 0x0000018C17F79A60, file "app\services\brokerage\profile_service.py", line 454>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              46 (_update_status_columns)

555           LOAD_CONST              71 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\brokerage\profile_service.py", line 555>)
              MAKE_FUNCTION
              LOAD_CONST              72 (<code object get_profile at 0x0000018C17F7A4E0, file "app\services\brokerage\profile_service.py", line 555>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              47 (get_profile)

593           LOAD_CONST              46 ('filter_status')

595           LOAD_CONST               2 (None)

593           LOAD_CONST              47 ('filter_stage')

596           LOAD_CONST               2 (None)

593           LOAD_CONST              45 ('limit')

597           LOAD_NAME               26 (_DEFAULT_LIMIT)

593           BUILD_MAP                3
              LOAD_CONST              73 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\brokerage\profile_service.py", line 593>)
              MAKE_FUNCTION
              LOAD_CONST              74 (<code object list_profiles at 0x0000018C17F7ACC0, file "app\services\brokerage\profile_service.py", line 593>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              48 (list_profiles)

668           LOAD_CONST              75 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\brokerage\profile_service.py", line 668>)
              MAKE_FUNCTION
              LOAD_CONST              76 (<code object _is_unique_violation at 0x0000018C17F96140, file "app\services\brokerage\profile_service.py", line 668>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              49 (_is_unique_violation)

682           BUILD_LIST               0
              LOAD_CONST              83 (('ALLOWED_ONBOARDING_STATUSES', 'ALLOWED_PILOT_STAGES', 'ALLOWED_FEATURES_KEYS', 'ALLOWED_METADATA_KEYS', 'ensure_profile', 'get_profile', 'list_profiles', 'update_onboarding_status', 'update_pilot_stage', 'pause_brokerage', 'resume_brokerage', 'mark_onboarding_completed'))
              LIST_EXTEND              1
              STORE_NAME              50 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "app\services\brokerage\profile_service.py", line 132>:
132           RESUME                   0
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

Disassembly of <code object _now_dt at 0x0000018C179C3A50, file "app\services\brokerage\profile_service.py", line 132>:
132           RESUME                   0

133           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

134           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

135           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

136   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

137   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\brokerage\profile_service.py", line 140>:
140           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18025030, file "app\services\brokerage\profile_service.py", line 140>:
140           RESUME                   0

141           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF0F30, file "app\services\brokerage\profile_service.py", line 144>:
 144           RESUME                   0

 145           NOP

 146   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 147           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 148           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 149   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 150           LOAD_CONST               2 ('profile_service db client unavailable type=')

 151           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 150           BUILD_STRING             2

 149           CALL                     1
               POP_TOP

 153   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 148   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\brokerage\profile_service.py", line 156>:
156           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _bound_str at 0x0000018C17972550, file "app\services\brokerage\profile_service.py", line 156>:
156           RESUME                   0

157           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

158           LOAD_CONST               0 (None)
              RETURN_VALUE

159   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

160           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

161           LOAD_CONST               0 (None)
              RETURN_VALUE

162   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

163           LOAD_CONST               0 (None)
              RETURN_VALUE

164   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\brokerage\profile_service.py", line 167>:
167           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_features at 0x0000018C17FA92F0, file "app\services\brokerage\profile_service.py", line 167>:
167           RESUME                   0

168           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

169           BUILD_MAP                0
              RETURN_VALUE

170   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

171           LOAD_GLOBAL              4 (ALLOWED_FEATURES_KEYS)
              GET_ITER
      L2:     FOR_ITER                51 (to L5)
              STORE_FAST               2 (k)

172           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, value)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)
      L3:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (value, k)
              BINARY_OP               26 ([])
              LOAD_GLOBAL              6 (bool)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           41 (to L2)

173   L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (value, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           53 (to L2)

171   L5:     END_FOR
              POP_ITER

174           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\brokerage\profile_service.py", line 177>:
177           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _project_metadata at 0x0000018C17EDF800, file "app\services\brokerage\profile_service.py", line 177>:
177            RESUME                   0

178            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (value)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

179            BUILD_MAP                0
               RETURN_VALUE

180    L1:     BUILD_MAP                0
               STORE_FAST               1 (out)

181            LOAD_GLOBAL              4 (ALLOWED_METADATA_KEYS)
               GET_ITER
       L2:     FOR_ITER               240 (to L17)
               STORE_FAST               2 (k)

182            LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, value)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

183            JUMP_BACKWARD           11 (to L2)

184    L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (value, k)
               BINARY_OP               26 ([])
               STORE_FAST               3 (v)

185            LOAD_FAST_BORROW         3 (v)
               POP_JUMP_IF_NONE        34 (to L4)
               NOT_TAKEN
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL              6 (int)
               LOAD_GLOBAL              8 (float)
               LOAD_GLOBAL             10 (bool)
               BUILD_TUPLE              3
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE        7 (to L5)
               NOT_TAKEN

186    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
               LOAD_FAST_BORROW         2 (k)
               STORE_SUBSCR
               JUMP_BACKWARD           62 (to L2)

187    L5:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL             12 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       42 (to L8)
               NOT_TAKEN

188            LOAD_FAST_BORROW         2 (k)
               LOAD_CONST               1 ('notes_token')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       29 (to L7)
               NOT_TAKEN

189            LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               LOAD_GLOBAL             16 (_NOTES_TOKEN_MAX_LEN)
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L6)
               NOT_TAKEN

190            LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
               LOAD_FAST_BORROW         2 (k)
               STORE_SUBSCR
               JUMP_BACKWARD          117 (to L2)

189    L6:     JUMP_BACKWARD          119 (to L2)

192    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (v, out)
               LOAD_FAST_BORROW         2 (k)
               STORE_SUBSCR
               JUMP_BACKWARD          125 (to L2)

193    L8:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         3 (v)
               LOAD_GLOBAL             18 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD          149 (to L2)

195    L9:     LOAD_GLOBAL             20 (all)
               COPY                     1
               LOAD_COMMON_CONSTANT     3 (<built-in function all>)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       28 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18052F70, file "app\services\brokerage\profile_service.py", line 195>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         3 (v)
               GET_ITER
               CALL                     0
      L10:     FOR_ITER                12 (to L12)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L10)
      L11:     POP_ITER
               LOAD_CONST               3 (False)
               JUMP_FORWARD            17 (to L14)
      L12:     END_FOR
               POP_ITER
               LOAD_CONST               4 (True)
               JUMP_FORWARD            13 (to L14)
      L13:     PUSH_NULL
               LOAD_CONST               2 (<code object <genexpr> at 0x0000018C18052F70, file "app\services\brokerage\profile_service.py", line 195>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         3 (v)
               GET_ITER
               CALL                     0
               CALL                     1
      L14:     TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               JUMP_BACKWARD          209 (to L2)
      L15:     LOAD_GLOBAL             15 (len + NULL)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               LOAD_SMALL_INT          50
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_TRUE         3 (to L16)
               NOT_TAKEN
               JUMP_BACKWARD          227 (to L2)

196   L16:     LOAD_GLOBAL             19 (list + NULL)
               LOAD_FAST_BORROW         3 (v)
               CALL                     1
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
               STORE_SUBSCR
               JUMP_BACKWARD          242 (to L2)

181   L17:     END_FOR
               POP_ITER

197            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "app\services\brokerage\profile_service.py", line 195>:
 195           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                21 (to L3)
               STORE_FAST               1 (x)
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (x)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\brokerage\profile_service.py", line 200>:
200           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C179A7290, file "app\services\brokerage\profile_service.py", line 200>:
200           RESUME                   0

201           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (row)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

202           LOAD_CONST               0 (None)
              RETURN_VALUE

203   L1:     BUILD_MAP                0
              STORE_FAST               1 (out)

204           LOAD_GLOBAL              4 (_STRUCTURAL_COLUMNS)
              GET_ITER
      L2:     FOR_ITER                21 (to L4)
              STORE_FAST               2 (col)

205           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (col, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

206   L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, col)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, col)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L2)

204   L4:     END_FOR
              POP_ITER

207           LOAD_GLOBAL              7 (_project_features + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('features')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L5:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               1 ('features')
              STORE_SUBSCR

208           LOAD_GLOBAL             11 (_project_metadata + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('metadata')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L6:     CALL                     1
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               2 ('metadata')
              STORE_SUBSCR

209           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\brokerage\profile_service.py", line 212>:
212           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_brokerage_id at 0x0000018C18010B30, file "app\services\brokerage\profile_service.py", line 212>:
212           RESUME                   0

213           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

214   L1:     LOAD_CONST               0 ('missing_brokerage_id')
              RETURN_VALUE

215   L2:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

216           LOAD_CONST               1 ('brokerage_id_too_long')
              RETURN_VALUE

217   L3:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\brokerage\profile_service.py", line 220>:
220           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_onboarding_status at 0x0000018C17FA2E20, file "app\services\brokerage\profile_service.py", line 220>:
220           RESUME                   0

221           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_ONBOARDING_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

222           LOAD_CONST               0 ('invalid_onboarding_status')
              RETURN_VALUE

223   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\brokerage\profile_service.py", line 226>:
226           RESUME                   0
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _validate_pilot_stage at 0x0000018C17FA3000, file "app\services\brokerage\profile_service.py", line 226>:
226           RESUME                   0

227           LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              0 (ALLOWED_PILOT_STAGES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

228           LOAD_CONST               0 ('invalid_pilot_stage')
              RETURN_VALUE

229   L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\brokerage\profile_service.py", line 232>:
232           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

234           LOAD_CONST               2 ('str')

232           LOAD_CONST               3 ('profile')

235           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

232           LOAD_CONST               5 ('warnings')

236           LOAD_CONST               6 ('Optional[List[str]]')

232           LOAD_CONST               7 ('error_code')

237           LOAD_CONST               8 ('Optional[str]')

232           LOAD_CONST               9 ('return')

238           LOAD_CONST              10 ('Dict[str, Any]')

232           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C18090140, file "app\services\brokerage\profile_service.py", line 232>:
232           RESUME                   0

240           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

241           LOAD_CONST               1 ('profile')
              LOAD_FAST                1 (profile)

242           LOAD_CONST               2 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

243           LOAD_CONST               3 ('error_code')
              LOAD_FAST_BORROW         3 (error_code)

239           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090250, file "app\services\brokerage\profile_service.py", line 247>:
247           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

249           LOAD_CONST               2 ('str')

247           LOAD_CONST               3 ('profiles')

250           LOAD_CONST               4 ('Optional[List[Dict[str, Any]]]')

247           LOAD_CONST               5 ('count')

251           LOAD_CONST               6 ('int')

247           LOAD_CONST               7 ('limit')

252           LOAD_CONST               6 ('int')

247           LOAD_CONST               8 ('filter_status')

253           LOAD_CONST               9 ('Optional[str]')

247           LOAD_CONST              10 ('filter_stage')

254           LOAD_CONST               9 ('Optional[str]')

247           LOAD_CONST              11 ('warnings')

255           LOAD_CONST              12 ('Optional[List[str]]')

247           LOAD_CONST              13 ('error_code')

256           LOAD_CONST               9 ('Optional[str]')

247           LOAD_CONST              14 ('return')

257           LOAD_CONST              15 ('Dict[str, Any]')

247           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _list_envelope at 0x0000018C17FE13E0, file "app\services\brokerage\profile_service.py", line 247>:
247           RESUME                   0

259           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

260           LOAD_CONST               1 ('profiles')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                1 (profiles)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

261           LOAD_CONST               2 ('count')
              LOAD_FAST                2 (count)

262           LOAD_CONST               3 ('limit')
              LOAD_FAST                3 (limit)

263           LOAD_CONST               4 ('filter_status')
              LOAD_FAST                4 (filter_status)

264           LOAD_CONST               5 ('filter_stage')
              LOAD_FAST                5 (filter_stage)

265           LOAD_CONST               6 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                6 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1

266           LOAD_CONST               7 ('error_code')
              LOAD_FAST_BORROW         7 (error_code)

258           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053090, file "app\services\brokerage\profile_service.py", line 274>:
274           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

276           LOAD_CONST               2 ('str')

274           LOAD_CONST               3 ('brokerage_name')

277           LOAD_CONST               4 ('Optional[str]')

274           LOAD_CONST               5 ('timezone_name')

278           LOAD_CONST               4 ('Optional[str]')

274           LOAD_CONST               6 ('market')

279           LOAD_CONST               4 ('Optional[str]')

274           LOAD_CONST               7 ('onboarding_owner')

280           LOAD_CONST               4 ('Optional[str]')

274           LOAD_CONST               8 ('config_version')

281           LOAD_CONST               4 ('Optional[str]')

274           LOAD_CONST               9 ('features')

282           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

274           LOAD_CONST              11 ('metadata')

283           LOAD_CONST              10 ('Optional[Dict[str, Any]]')

274           LOAD_CONST              12 ('onboarding_status')

284           LOAD_CONST               2 ('str')

274           LOAD_CONST              13 ('pilot_stage')

285           LOAD_CONST               2 ('str')

274           LOAD_CONST              14 ('now')

286           LOAD_CONST              15 ('Any')

274           LOAD_CONST              16 ('return')

287           LOAD_CONST              17 ('Dict[str, Any]')

274           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object ensure_profile at 0x0000018C17ED2600, file "app\services\brokerage\profile_service.py", line 274>:
 274            RESUME                   0

 292            LOAD_GLOBAL              1 (_validate_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        31 (to L1)
                NOT_TAKEN
                POP_TOP

 293            LOAD_GLOBAL              3 (_validate_onboarding_status + NULL)
                LOAD_FAST_BORROW         8 (onboarding_status)
                CALL                     1

 292            COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        12 (to L1)
                NOT_TAKEN
                POP_TOP

 294            LOAD_GLOBAL              5 (_validate_pilot_stage + NULL)
                LOAD_FAST_BORROW         9 (pilot_stage)
                CALL                     1

 291    L1:     STORE_FAST              11 (err)

 296            LOAD_FAST_BORROW        11 (err)
                POP_JUMP_IF_NONE        14 (to L2)
                NOT_TAKEN

 297            LOAD_GLOBAL              7 (_safe_envelope + NULL)
                LOAD_CONST               2 ('failed')
                LOAD_FAST_BORROW        11 (err)
                LOAD_CONST               3 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 299    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                STORE_FAST              12 (bid)

 300            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (brokerage_name)
                LOAD_GLOBAL             12 (_BROKERAGE_NAME_MAX_LEN)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               12 (bid)
        L3:     STORE_FAST              13 (name)

 301            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         2 (timezone_name)
                LOAD_GLOBAL             14 (_TIMEZONE_MAX_LEN)
                CALL                     2
                STORE_FAST              14 (tz)

 302            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (market)
                LOAD_GLOBAL             16 (_MARKET_MAX_LEN)
                CALL                     2
                STORE_FAST              15 (mkt)

 303            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         4 (onboarding_owner)
                LOAD_GLOBAL             18 (_OWNER_MAX_LEN)
                CALL                     2
                STORE_FAST              16 (owner)

 304            LOAD_GLOBAL             11 (_bound_str + NULL)
                LOAD_FAST_BORROW         5 (config_version)
                LOAD_GLOBAL             20 (_CONFIG_VERSION_MAX_LEN)
                CALL                     2
                STORE_FAST              17 (cv)

 305            LOAD_GLOBAL             23 (_project_features + NULL)
                LOAD_FAST_BORROW         6 (features)
                CALL                     1
                STORE_FAST              18 (feats)

 306            LOAD_GLOBAL             25 (_project_metadata + NULL)
                LOAD_FAST_BORROW         7 (metadata)
                CALL                     1
                STORE_FAST              19 (meta)

 308            LOAD_GLOBAL             27 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              20 (db)

 309            LOAD_FAST_BORROW        20 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L4)
                NOT_TAKEN

 310            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 311            LOAD_CONST               4 ('skipped')

 312            LOAD_CONST               5 ('brokerage_profile_store_unavailable')
                BUILD_LIST               1

 313            LOAD_CONST               5 ('brokerage_profile_store_unavailable')

 310            LOAD_CONST               6 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 316    L4:     LOAD_GLOBAL             29 (_now_dt + NULL)
                LOAD_FAST_BORROW        10 (now)
                CALL                     1
                STORE_FAST              21 (now_dt)

 317            LOAD_GLOBAL             31 (_iso + NULL)
                LOAD_FAST_BORROW        21 (now_dt)
                CALL                     1
                STORE_FAST              22 (iso_now)

 319            LOAD_CONST               7 ('brokerage_id')
                LOAD_FAST_BORROW        12 (bid)

 320            LOAD_CONST               8 ('brokerage_name')
                LOAD_FAST_BORROW        13 (name)

 321            LOAD_CONST               9 ('timezone')
                LOAD_FAST_BORROW        14 (tz)

 322            LOAD_CONST              10 ('market')
                LOAD_FAST_BORROW        15 (mkt)

 323            LOAD_CONST              11 ('onboarding_status')
                LOAD_FAST_BORROW         8 (onboarding_status)

 324            LOAD_CONST              12 ('pilot_stage')
                LOAD_FAST_BORROW         9 (pilot_stage)

 325            LOAD_CONST              13 ('onboarding_owner')
                LOAD_FAST_BORROW        16 (owner)

 326            LOAD_CONST              14 ('config_version')
                LOAD_FAST_BORROW        17 (cv)

 327            LOAD_CONST              15 ('features')
                LOAD_FAST_BORROW        18 (feats)

 328            LOAD_CONST              16 ('metadata')
                LOAD_FAST_BORROW        19 (meta)

 329            LOAD_CONST              17 ('created_at')
                LOAD_FAST_BORROW        22 (iso_now)

 330            LOAD_CONST              18 ('updated_at')
                LOAD_FAST_BORROW        22 (iso_now)

 318            BUILD_MAP               12
                STORE_FAST              23 (row)

 332            NOP

 333    L5:     LOAD_FAST_BORROW        20 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_GLOBAL             34 (_TABLE)
                CALL                     1
                LOAD_ATTR               37 (insert + NULL|self)
                LOAD_FAST_BORROW        23 (row)
                CALL                     1
                LOAD_ATTR               39 (execute + NULL|self)
                CALL                     0
                STORE_FAST              24 (result)

 334            LOAD_GLOBAL             41 (list + NULL)
                LOAD_GLOBAL             43 (getattr + NULL)
                LOAD_FAST_BORROW        24 (result)
                LOAD_CONST              19 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
                STORE_FAST              25 (rows)

 335            LOAD_FAST_BORROW        25 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L9)
        L7:     NOT_TAKEN
        L8:     LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST_BORROW        25 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD            10 (to L10)
        L9:     LOAD_GLOBAL             45 (_project_row + NULL)
                LOAD_FAST_BORROW        23 (row)
                CALL                     1
       L10:     STORE_FAST              26 (proj)

 336            LOAD_GLOBAL              7 (_safe_envelope + NULL)
                LOAD_CONST              20 ('ok')
                LOAD_FAST_BORROW        26 (proj)
                LOAD_CONST              21 (('status', 'profile'))
                CALL_KW                  2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 337            LOAD_GLOBAL             46 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      124 (to L20)
                NOT_TAKEN
                STORE_FAST              27 (e)

 338   L13:     LOAD_GLOBAL             49 (_is_unique_violation + NULL)
                LOAD_FAST               27 (e)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L16)
                NOT_TAKEN

 340            LOAD_GLOBAL             51 (get_profile + NULL)
                LOAD_FAST               12 (bid)
                CALL                     1
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              27 (e)
                DELETE_FAST             27 (e)
                RETURN_VALUE

 341   L16:     LOAD_GLOBAL             52 (logger)
                LOAD_ATTR               55 (warning + NULL|self)

 342            LOAD_CONST              22 ('ensure_profile insert error type=')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               27 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 341            CALL                     1
                POP_TOP

 344            LOAD_GLOBAL              7 (_safe_envelope + NULL)

 345            LOAD_CONST               4 ('skipped')

 346            LOAD_CONST              23 ('db_write_failed:')
                LOAD_GLOBAL             57 (type + NULL)
                LOAD_FAST               27 (e)
                CALL                     1
                LOAD_ATTR               58 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 347            LOAD_CONST               5 ('brokerage_profile_store_unavailable')

 344            LOAD_CONST               6 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              27 (e)
                DELETE_FAST             27 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST               1 (None)
                STORE_FAST              27 (e)
                DELETE_FAST             27 (e)
                RERAISE                  1

 337   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L7 -> L12 [0]
  L8 to L11 -> L12 [0]
  L12 to L13 -> L21 [1] lasti
  L13 to L14 -> L19 [1] lasti
  L14 to L15 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\brokerage\profile_service.py", line 351>:
351           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

353           LOAD_CONST               2 ('str')

351           LOAD_CONST               3 ('new_status')

354           LOAD_CONST               2 ('str')

351           LOAD_CONST               4 ('actor_id')

355           LOAD_CONST               5 ('Optional[str]')

351           LOAD_CONST               6 ('now')

356           LOAD_CONST               7 ('Any')

351           LOAD_CONST               8 ('return')

357           LOAD_CONST               9 ('Dict[str, Any]')

351           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object update_onboarding_status at 0x0000018C18024F30, file "app\services\brokerage\profile_service.py", line 351>:
351           RESUME                   0

362           LOAD_GLOBAL              1 (_update_status_columns + NULL)

363           LOAD_FAST_BORROW         0 (brokerage_id)

364           LOAD_CONST               1 ('onboarding_status')
              LOAD_FAST_BORROW         1 (new_status)
              BUILD_MAP                1

365           LOAD_FAST_BORROW         1 (new_status)

366           LOAD_CONST               2 ('onboarding')

367           LOAD_FAST_BORROW         2 (actor_id)

368           LOAD_FAST_BORROW         1 (new_status)
              LOAD_CONST               3 ('LIVE')
              COMPARE_OP              72 (==)

369           LOAD_FAST_BORROW         3 (now)

362           LOAD_CONST               4 (('brokerage_id', 'patch', 'validate_status', 'validate_kind', 'actor_id', 'completed', 'now'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\brokerage\profile_service.py", line 373>:
373           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

375           LOAD_CONST               2 ('str')

373           LOAD_CONST               3 ('new_stage')

376           LOAD_CONST               2 ('str')

373           LOAD_CONST               4 ('actor_id')

377           LOAD_CONST               5 ('Optional[str]')

373           LOAD_CONST               6 ('now')

378           LOAD_CONST               7 ('Any')

373           LOAD_CONST               8 ('return')

379           LOAD_CONST               9 ('Dict[str, Any]')

373           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object update_pilot_stage at 0x0000018C18025830, file "app\services\brokerage\profile_service.py", line 373>:
373           RESUME                   0

380           LOAD_GLOBAL              1 (_update_status_columns + NULL)

381           LOAD_FAST_BORROW         0 (brokerage_id)

382           LOAD_CONST               0 ('pilot_stage')
              LOAD_FAST_BORROW         1 (new_stage)
              BUILD_MAP                1

383           LOAD_FAST_BORROW         1 (new_stage)

384           LOAD_CONST               0 ('pilot_stage')

385           LOAD_FAST_BORROW         2 (actor_id)

386           LOAD_FAST_BORROW         3 (now)

380           LOAD_CONST               1 (('brokerage_id', 'patch', 'validate_status', 'validate_kind', 'actor_id', 'now'))
              CALL_KW                  6
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025930, file "app\services\brokerage\profile_service.py", line 390>:
390           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

392           LOAD_CONST               2 ('str')

390           LOAD_CONST               3 ('actor_id')

393           LOAD_CONST               4 ('Optional[str]')

390           LOAD_CONST               5 ('now')

394           LOAD_CONST               6 ('Any')

390           LOAD_CONST               7 ('return')

395           LOAD_CONST               8 ('Dict[str, Any]')

390           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object pause_brokerage at 0x0000018C17C49B80, file "app\services\brokerage\profile_service.py", line 390>:
390           RESUME                   0

396           LOAD_GLOBAL              1 (_iso + NULL)
              LOAD_GLOBAL              3 (_now_dt + NULL)
              LOAD_FAST_BORROW         2 (now)
              CALL                     1
              CALL                     1
              STORE_FAST               3 (iso_now)

397           LOAD_GLOBAL              5 (_update_status_columns + NULL)

398           LOAD_FAST_BORROW         0 (brokerage_id)

399           LOAD_CONST               0 ('onboarding_status')
              LOAD_CONST               1 ('PAUSED')
              BUILD_MAP                1

400           LOAD_CONST               1 ('PAUSED')

401           LOAD_CONST               2 ('onboarding')

402           LOAD_FAST_BORROW         1 (actor_id)

403           LOAD_CONST               3 ('last_paused_at')
              LOAD_FAST_BORROW         3 (iso_now)
              BUILD_MAP                1

404           LOAD_FAST_BORROW         2 (now)

397           LOAD_CONST               4 (('brokerage_id', 'patch', 'validate_status', 'validate_kind', 'actor_id', 'extra_metadata', 'now'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025A30, file "app\services\brokerage\profile_service.py", line 408>:
408           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

410           LOAD_CONST               2 ('str')

408           LOAD_CONST               3 ('actor_id')

411           LOAD_CONST               4 ('Optional[str]')

408           LOAD_CONST               5 ('target_status')

412           LOAD_CONST               2 ('str')

408           LOAD_CONST               6 ('now')

413           LOAD_CONST               7 ('Any')

408           LOAD_CONST               8 ('return')

414           LOAD_CONST               9 ('Dict[str, Any]')

408           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object resume_brokerage at 0x0000018C17F95E60, file "app\services\brokerage\profile_service.py", line 408>:
408           RESUME                   0

415           LOAD_GLOBAL              1 (_validate_onboarding_status + NULL)
              LOAD_FAST_BORROW         2 (target_status)
              CALL                     1
              STORE_FAST               4 (err)

416           LOAD_FAST_BORROW         4 (err)
              POP_JUMP_IF_NOT_NONE     8 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (target_status)
              LOAD_CONST               1 ('PAUSED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE       14 (to L2)
              NOT_TAKEN

417   L1:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

418           LOAD_CONST               2 ('failed')

419           LOAD_CONST               3 ('invalid_resume_target')

417           LOAD_CONST               4 (('status', 'error_code'))
              CALL_KW                  2
              RETURN_VALUE

421   L2:     LOAD_GLOBAL              5 (_iso + NULL)
              LOAD_GLOBAL              7 (_now_dt + NULL)
              LOAD_FAST_BORROW         3 (now)
              CALL                     1
              CALL                     1
              STORE_FAST               5 (iso_now)

422           LOAD_GLOBAL              9 (_update_status_columns + NULL)

423           LOAD_FAST_BORROW         0 (brokerage_id)

424           LOAD_CONST               5 ('onboarding_status')
              LOAD_FAST_BORROW         2 (target_status)
              BUILD_MAP                1

425           LOAD_FAST_BORROW         2 (target_status)

426           LOAD_CONST               6 ('onboarding')

427           LOAD_FAST_BORROW         1 (actor_id)

428           LOAD_CONST               7 ('last_resumed_at')
              LOAD_FAST_BORROW         5 (iso_now)
              BUILD_MAP                1

429           LOAD_FAST_BORROW         3 (now)

422           LOAD_CONST               8 (('brokerage_id', 'patch', 'validate_status', 'validate_kind', 'actor_id', 'extra_metadata', 'now'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025B30, file "app\services\brokerage\profile_service.py", line 433>:
433           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

435           LOAD_CONST               2 ('str')

433           LOAD_CONST               3 ('actor_id')

436           LOAD_CONST               4 ('Optional[str]')

433           LOAD_CONST               5 ('now')

437           LOAD_CONST               6 ('Any')

433           LOAD_CONST               7 ('return')

438           LOAD_CONST               8 ('Dict[str, Any]')

433           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object mark_onboarding_completed at 0x0000018C1802C750, file "app\services\brokerage\profile_service.py", line 433>:
433           RESUME                   0

439           LOAD_GLOBAL              1 (_iso + NULL)
              LOAD_GLOBAL              3 (_now_dt + NULL)
              LOAD_FAST_BORROW         2 (now)
              CALL                     1
              CALL                     1
              STORE_FAST               3 (iso_now)

440           LOAD_GLOBAL              5 (_update_status_columns + NULL)

441           LOAD_FAST_BORROW         0 (brokerage_id)

443           LOAD_CONST               0 ('onboarding_status')
              LOAD_CONST               1 ('LIVE')

444           LOAD_CONST               2 ('onboarding_completed_at')
              LOAD_FAST_BORROW         3 (iso_now)

442           BUILD_MAP                2

446           LOAD_CONST               1 ('LIVE')

447           LOAD_CONST               3 ('onboarding')

448           LOAD_FAST_BORROW         1 (actor_id)

449           LOAD_CONST               4 (True)

450           LOAD_FAST_BORROW         2 (now)

440           LOAD_CONST               5 (('brokerage_id', 'patch', 'validate_status', 'validate_kind', 'actor_id', 'completed', 'now'))
              CALL_KW                  7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18090580, file "app\services\brokerage\profile_service.py", line 454>:
454           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

456           LOAD_CONST               2 ('str')

454           LOAD_CONST               3 ('patch')

457           LOAD_CONST               4 ('Dict[str, Any]')

454           LOAD_CONST               5 ('validate_status')

458           LOAD_CONST               2 ('str')

454           LOAD_CONST               6 ('validate_kind')

459           LOAD_CONST               2 ('str')

454           LOAD_CONST               7 ('actor_id')

460           LOAD_CONST               8 ('Optional[str]')

454           LOAD_CONST               9 ('completed')

461           LOAD_CONST              10 ('bool')

454           LOAD_CONST              11 ('extra_metadata')

462           LOAD_CONST              12 ('Optional[Dict[str, Any]]')

454           LOAD_CONST              13 ('now')

463           LOAD_CONST              14 ('Any')

454           LOAD_CONST              15 ('return')

464           LOAD_CONST               4 ('Dict[str, Any]')

454           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object _update_status_columns at 0x0000018C17F79A60, file "app\services\brokerage\profile_service.py", line 454>:
 454            RESUME                   0

 465            LOAD_GLOBAL              1 (_validate_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               8 (err)

 466            LOAD_FAST_BORROW         8 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 467            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_FAST_BORROW         8 (err)
                LOAD_CONST               2 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 468    L1:     LOAD_FAST_BORROW         3 (validate_kind)
                LOAD_CONST               3 ('onboarding')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       13 (to L2)
                NOT_TAKEN

 469            LOAD_GLOBAL              5 (_validate_onboarding_status + NULL)
                LOAD_FAST_BORROW         2 (validate_status)
                CALL                     1
                STORE_FAST               8 (err)
                JUMP_FORWARD            11 (to L3)

 471    L2:     LOAD_GLOBAL              7 (_validate_pilot_stage + NULL)
                LOAD_FAST_BORROW         2 (validate_status)
                CALL                     1
                STORE_FAST               8 (err)

 472    L3:     LOAD_FAST_BORROW         8 (err)
                POP_JUMP_IF_NONE        14 (to L4)
                NOT_TAKEN

 473            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_FAST_BORROW         8 (err)
                LOAD_CONST               2 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 475    L4:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                STORE_FAST               9 (bid)

 476            LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST              10 (db)

 477            LOAD_FAST_BORROW        10 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L5)
                NOT_TAKEN

 478            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 479            LOAD_CONST               4 ('skipped')

 480            LOAD_CONST               5 ('brokerage_profile_store_unavailable')
                BUILD_LIST               1

 481            LOAD_CONST               5 ('brokerage_profile_store_unavailable')

 478            LOAD_CONST               6 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 485    L5:     LOAD_GLOBAL             13 (_now_dt + NULL)
                LOAD_FAST_BORROW         7 (now)
                CALL                     1
                STORE_FAST              11 (now_dt)

 486            LOAD_GLOBAL             15 (_iso + NULL)
                LOAD_FAST_BORROW        11 (now_dt)
                CALL                     1
                STORE_FAST              12 (iso_now)

 487            NOP

 489    L6:     LOAD_FAST_BORROW        10 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE)
                CALL                     1

 490            LOAD_ATTR               21 (select + NULL|self)
                LOAD_CONST               7 (',')
                LOAD_ATTR               23 (join + NULL|self)
                LOAD_GLOBAL             24 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 491            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               8 ('brokerage_id')
                LOAD_FAST_BORROW         9 (bid)
                CALL                     2

 492            LOAD_ATTR               29 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 493            LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0

 488            STORE_FAST              13 (cur)

 495            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW        13 (cur)
                LOAD_CONST               9 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     CALL                     1
                STORE_FAST              14 (cur_rows)

 496            LOAD_FAST_BORROW        14 (cur_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L11)
        L8:     NOT_TAKEN

 497    L9:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 498            LOAD_CONST               1 ('failed')

 499            LOAD_CONST              10 ('brokerage_profile_not_found')

 497            LOAD_CONST               2 (('status', 'error_code'))
                CALL_KW                  2
       L10:     RETURN_VALUE

 501   L11:     LOAD_FAST_BORROW        14 (cur_rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              15 (cur_row)

 512   L12:     LOAD_GLOBAL             47 (_project_metadata + NULL)
                LOAD_FAST               15 (cur_row)
                LOAD_ATTR               49 (get + NULL|self)
                LOAD_CONST              13 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L13:     CALL                     1
                STORE_FAST              17 (existing_md)

 513            LOAD_GLOBAL             51 (dict + NULL)
                LOAD_FAST               17 (existing_md)
                CALL                     1
                STORE_FAST              18 (merged_md)

 514            LOAD_FAST               12 (iso_now)
                LOAD_FAST               18 (merged_md)
                LOAD_CONST              14 ('last_stage_change_at')
                STORE_SUBSCR

 515            LOAD_FAST                4 (actor_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L14)
                NOT_TAKEN

 516            LOAD_GLOBAL             53 (_bound_str + NULL)
                LOAD_FAST                4 (actor_id)
                LOAD_GLOBAL             54 (_OWNER_MAX_LEN)
                CALL                     2
                STORE_FAST              19 (bounded_actor)

 517            LOAD_FAST               19 (bounded_actor)
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L14)
                NOT_TAKEN

 518            LOAD_FAST               19 (bounded_actor)
                LOAD_FAST               18 (merged_md)
                LOAD_CONST              15 ('last_stage_actor')
                STORE_SUBSCR

 519   L14:     LOAD_FAST                6 (extra_metadata)
                TO_BOOL
                POP_JUMP_IF_FALSE       45 (to L18)
                NOT_TAKEN

 520            LOAD_FAST                6 (extra_metadata)
                LOAD_ATTR               57 (items + NULL|self)
                CALL                     0
                GET_ITER
       L15:     FOR_ITER                24 (to L17)
                UNPACK_SEQUENCE          2
                STORE_FAST              20 (k)
                STORE_FAST              21 (v)

 521            LOAD_FAST               20 (k)
                LOAD_GLOBAL             58 (ALLOWED_METADATA_KEYS)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L15)

 522   L16:     LOAD_FAST               21 (v)
                LOAD_FAST               18 (merged_md)
                LOAD_FAST               20 (k)
                STORE_SUBSCR
                JUMP_BACKWARD           26 (to L15)

 520   L17:     END_FOR
                POP_ITER

 523   L18:     LOAD_GLOBAL             47 (_project_metadata + NULL)
                LOAD_FAST               18 (merged_md)
                CALL                     1
                STORE_FAST              18 (merged_md)

 524            LOAD_GLOBAL             51 (dict + NULL)
                LOAD_FAST                1 (patch)
                CALL                     1
                STORE_FAST               1 (patch)

 525            LOAD_FAST               18 (merged_md)
                LOAD_FAST                1 (patch)
                LOAD_CONST              13 ('metadata')
                STORE_SUBSCR

 526            LOAD_FAST_LOAD_FAST    193 (iso_now, patch)
                LOAD_CONST              16 ('updated_at')
                STORE_SUBSCR

 527            LOAD_FAST                5 (completed)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L19)
                NOT_TAKEN
                LOAD_CONST              17 ('onboarding_completed_at')
                LOAD_FAST                1 (patch)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        5 (to L19)
                NOT_TAKEN

 528            LOAD_FAST_LOAD_FAST    193 (iso_now, patch)
                LOAD_CONST              17 ('onboarding_completed_at')
                STORE_SUBSCR

 530   L19:     NOP

 532   L20:     LOAD_FAST               10 (db)
                LOAD_ATTR               17 (table + NULL|self)
                LOAD_GLOBAL             18 (_TABLE)
                CALL                     1

 533            LOAD_ATTR               61 (update + NULL|self)
                LOAD_FAST                1 (patch)
                CALL                     1

 534            LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               8 ('brokerage_id')
                LOAD_FAST                9 (bid)
                CALL                     2

 535            LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0

 531            STORE_FAST              22 (result)

 537            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST               22 (result)
                LOAD_CONST               9 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
       L21:     NOT_TAKEN
       L22:     POP_TOP
                BUILD_LIST               0
       L23:     CALL                     1
                STORE_FAST              23 (rows)

 538            LOAD_FAST               23 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L26)
       L24:     NOT_TAKEN
       L25:     LOAD_GLOBAL             63 (_project_row + NULL)
                LOAD_FAST               23 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST               0 (None)
       L27:     STORE_FAST              24 (proj)

 539            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              18 ('ok')
                LOAD_FAST               24 (proj)
                LOAD_CONST              19 (('status', 'profile'))
                CALL_KW                  2
       L28:     RETURN_VALUE

  --   L29:     PUSH_EXC_INFO

 502            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L34)
                NOT_TAKEN
                STORE_FAST              16 (e)

 503   L30:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 504            LOAD_CONST              11 ('_update_status_columns read error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 503            CALL                     1
                POP_TOP

 506            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 507            LOAD_CONST               4 ('skipped')

 508            LOAD_CONST              12 ('db_read_failed:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 509            LOAD_CONST               5 ('brokerage_profile_store_unavailable')

 506            LOAD_CONST               6 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L31:     SWAP                     2
       L32:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L33:     LOAD_CONST               0 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 502   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L36:     PUSH_EXC_INFO

 540            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L41)
                NOT_TAKEN
                STORE_FAST              16 (e)

 541   L37:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 542            LOAD_CONST              20 ('_update_status_columns update error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 541            CALL                     1
                POP_TOP

 544            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 545            LOAD_CONST               4 ('skipped')

 546            LOAD_CONST              21 ('db_write_failed:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST               16 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 547            LOAD_CONST               5 ('brokerage_profile_store_unavailable')

 544            LOAD_CONST               6 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L38:     SWAP                     2
       L39:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RETURN_VALUE

  --   L40:     LOAD_CONST               0 (None)
                STORE_FAST              16 (e)
                DELETE_FAST             16 (e)
                RERAISE                  1

 540   L41:     RERAISE                  0

  --   L42:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L8 -> L29 [0]
  L9 to L10 -> L29 [0]
  L11 to L12 -> L29 [0]
  L20 to L21 -> L36 [0]
  L22 to L24 -> L36 [0]
  L25 to L28 -> L36 [0]
  L29 to L30 -> L35 [1] lasti
  L30 to L31 -> L33 [1] lasti
  L31 to L32 -> L35 [1] lasti
  L33 to L35 -> L35 [1] lasti
  L36 to L37 -> L42 [1] lasti
  L37 to L38 -> L40 [1] lasti
  L38 to L39 -> L42 [1] lasti
  L40 to L42 -> L42 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\brokerage\profile_service.py", line 555>:
555           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object get_profile at 0x0000018C17F7A4E0, file "app\services\brokerage\profile_service.py", line 555>:
 555            RESUME                   0

 556            LOAD_GLOBAL              1 (_validate_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               1 (err)

 557            LOAD_FAST_BORROW         1 (err)
                POP_JUMP_IF_NONE        14 (to L1)
                NOT_TAKEN

 558            LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST               1 ('failed')
                LOAD_FAST_BORROW         1 (err)
                LOAD_CONST               2 (('status', 'error_code'))
                CALL_KW                  2
                RETURN_VALUE

 559    L1:     LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               2 (bid)

 560            LOAD_GLOBAL              7 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 561            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    16 (to L2)
                NOT_TAKEN

 562            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 563            LOAD_CONST               3 ('skipped')

 564            LOAD_CONST               4 ('brokerage_profile_store_unavailable')
                BUILD_LIST               1

 565            LOAD_CONST               4 ('brokerage_profile_store_unavailable')

 562            LOAD_CONST               5 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 567    L2:     NOP

 569    L3:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE)
                CALL                     1

 570            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST               6 (',')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_GLOBAL             16 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 571            LOAD_ATTR               19 (eq + NULL|self)
                LOAD_CONST               7 ('brokerage_id')
                LOAD_FAST_BORROW         2 (bid)
                CALL                     2

 572            LOAD_ATTR               21 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 573            LOAD_ATTR               23 (execute + NULL|self)
                CALL                     0

 568            STORE_FAST               4 (result)

 575            LOAD_GLOBAL             25 (list + NULL)
                LOAD_GLOBAL             27 (getattr + NULL)
                LOAD_FAST_BORROW         4 (result)
                LOAD_CONST               8 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
        L4:     NOT_TAKEN
        L5:     POP_TOP
                BUILD_LIST               0
        L6:     CALL                     1
                STORE_FAST               5 (rows)

 576            LOAD_FAST_BORROW         5 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        14 (to L10)
        L7:     NOT_TAKEN

 577    L8:     LOAD_GLOBAL              3 (_safe_envelope + NULL)

 578            LOAD_CONST               1 ('failed')

 579            LOAD_CONST               9 ('brokerage_profile_not_found')

 577            LOAD_CONST               2 (('status', 'error_code'))
                CALL_KW                  2
        L9:     RETURN_VALUE

 581   L10:     LOAD_GLOBAL              3 (_safe_envelope + NULL)
                LOAD_CONST              10 ('ok')
                LOAD_GLOBAL             29 (_project_row + NULL)
                LOAD_FAST_BORROW         5 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_CONST              11 (('status', 'profile'))
                CALL_KW                  2
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 582            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       91 (to L17)
                NOT_TAKEN
                STORE_FAST               6 (e)

 583   L13:     LOAD_GLOBAL             32 (logger)
                LOAD_ATTR               35 (warning + NULL|self)

 584            LOAD_CONST              12 ('get_profile read error type=')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 583            CALL                     1
                POP_TOP

 586            LOAD_GLOBAL              3 (_safe_envelope + NULL)

 587            LOAD_CONST               3 ('skipped')

 588            LOAD_CONST              13 ('db_read_failed:')
                LOAD_GLOBAL             37 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               38 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 589            LOAD_CONST               4 ('brokerage_profile_store_unavailable')

 586            LOAD_CONST               5 (('status', 'warnings', 'error_code'))
                CALL_KW                  3
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               0 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 582   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L12 [0]
  L5 to L7 -> L12 [0]
  L8 to L9 -> L12 [0]
  L10 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\brokerage\profile_service.py", line 593>:
593           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('filter_status')

595           LOAD_CONST               2 ('Optional[str]')

593           LOAD_CONST               3 ('filter_stage')

596           LOAD_CONST               2 ('Optional[str]')

593           LOAD_CONST               4 ('limit')

597           LOAD_CONST               5 ('Any')

593           LOAD_CONST               6 ('return')

598           LOAD_CONST               7 ('Dict[str, Any]')

593           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object list_profiles at 0x0000018C17F7ACC0, file "app\services\brokerage\profile_service.py", line 593>:
 593            RESUME                   0

 599            LOAD_FAST_BORROW         0 (filter_status)
                POP_JUMP_IF_NONE        26 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (filter_status)
                LOAD_GLOBAL              0 (ALLOWED_ONBOARDING_STATUSES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       15 (to L1)
                NOT_TAKEN

 600            LOAD_GLOBAL              3 (_list_envelope + NULL)

 601            LOAD_CONST               1 ('failed')
                LOAD_FAST_BORROW         0 (filter_status)

 602            LOAD_CONST               2 ('invalid_onboarding_status')

 600            LOAD_CONST               3 (('status', 'filter_status', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 604    L1:     LOAD_FAST_BORROW         1 (filter_stage)
                POP_JUMP_IF_NONE        26 (to L2)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (filter_stage)
                LOAD_GLOBAL              4 (ALLOWED_PILOT_STAGES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       15 (to L2)
                NOT_TAKEN

 605            LOAD_GLOBAL              3 (_list_envelope + NULL)

 606            LOAD_CONST               1 ('failed')
                LOAD_FAST_BORROW         1 (filter_stage)

 607            LOAD_CONST               4 ('invalid_pilot_stage')

 605            LOAD_CONST               5 (('status', 'filter_stage', 'error_code'))
                CALL_KW                  3
                RETURN_VALUE

 609    L2:     NOP

 610    L3:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                STORE_FAST               3 (capped)

 613    L4:     LOAD_FAST_BORROW         3 (capped)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN

 614            LOAD_SMALL_INT           1
                STORE_FAST               3 (capped)

 615    L5:     LOAD_FAST_BORROW         3 (capped)
                LOAD_GLOBAL             14 (_LIST_HARD_CAP)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        7 (to L6)
                NOT_TAKEN

 616            LOAD_GLOBAL             14 (_LIST_HARD_CAP)
                STORE_FAST               3 (capped)

 618    L6:     LOAD_GLOBAL             17 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               4 (db)

 619            LOAD_FAST_BORROW         4 (db)
                POP_JUMP_IF_NOT_NONE    19 (to L7)
                NOT_TAKEN

 620            LOAD_GLOBAL              3 (_list_envelope + NULL)

 621            LOAD_CONST               6 ('skipped')

 622            LOAD_FAST_BORROW         0 (filter_status)

 623            LOAD_FAST_BORROW         1 (filter_stage)

 624            LOAD_FAST_BORROW         3 (capped)

 625            LOAD_CONST               7 ('brokerage_profile_store_unavailable')
                BUILD_LIST               1

 626            LOAD_CONST               7 ('brokerage_profile_store_unavailable')

 620            LOAD_CONST               8 (('status', 'filter_status', 'filter_stage', 'limit', 'warnings', 'error_code'))
                CALL_KW                  6
                RETURN_VALUE

 628    L7:     NOP

 630    L8:     LOAD_FAST_BORROW         4 (db)
                LOAD_ATTR               19 (table + NULL|self)
                LOAD_GLOBAL             20 (_TABLE)
                CALL                     1

 631            LOAD_ATTR               23 (select + NULL|self)
                LOAD_CONST               9 (',')
                LOAD_ATTR               25 (join + NULL|self)
                LOAD_GLOBAL             26 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 632            LOAD_ATTR               29 (order + NULL|self)
                LOAD_CONST              10 ('updated_at')
                LOAD_CONST              11 (True)
                LOAD_CONST              12 (('desc',))
                CALL_KW                  2

 633            LOAD_ATTR               31 (limit + NULL|self)
                LOAD_FAST_BORROW         3 (capped)
                CALL                     1

 629            STORE_FAST               5 (query)

 635            LOAD_FAST_BORROW         0 (filter_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

 636   L10:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               33 (eq + NULL|self)
                LOAD_CONST              13 ('onboarding_status')
                LOAD_FAST_BORROW         0 (filter_status)
                CALL                     2
                STORE_FAST               5 (query)

 637   L11:     LOAD_FAST_BORROW         1 (filter_stage)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L14)
       L12:     NOT_TAKEN

 638   L13:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               33 (eq + NULL|self)
                LOAD_CONST              14 ('pilot_stage')
                LOAD_FAST_BORROW         1 (filter_stage)
                CALL                     2
                STORE_FAST               5 (query)

 639   L14:     LOAD_FAST_BORROW         5 (query)
                LOAD_ATTR               35 (execute + NULL|self)
                CALL                     0
                STORE_FAST               6 (result)

 640            LOAD_GLOBAL             37 (list + NULL)
                LOAD_GLOBAL             39 (getattr + NULL)
                LOAD_FAST_BORROW         6 (result)
                LOAD_CONST              15 ('data')
                LOAD_CONST               0 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L17)
       L15:     NOT_TAKEN
       L16:     POP_TOP
                BUILD_LIST               0
       L17:     CALL                     1
                STORE_FAST               7 (rows)

 641            LOAD_CONST              16 (<code object <genexpr> at 0x0000018C18090690, file "app\services\brokerage\profile_service.py", line 641>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         7 (rows)
                GET_ITER
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR      8 (p)
                SWAP                     2
       L18:     BUILD_LIST               0
                SWAP                     2
       L19:     FOR_ITER                10 (to L22)
                STORE_FAST_LOAD_FAST   136 (p, p)
       L20:     POP_JUMP_IF_NOT_NONE     3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD            8 (to L19)
       L21:     LOAD_FAST_BORROW         8 (p)
                LIST_APPEND              2
                JUMP_BACKWARD           12 (to L19)
       L22:     END_FOR
                POP_ITER
       L23:     STORE_FAST               9 (projected)
                STORE_FAST               8 (p)

 642            LOAD_GLOBAL              3 (_list_envelope + NULL)

 643            LOAD_CONST              17 ('ok')

 644            LOAD_FAST_BORROW         9 (projected)

 645            LOAD_GLOBAL             41 (len + NULL)
                LOAD_FAST_BORROW         9 (projected)
                CALL                     1

 646            LOAD_FAST_BORROW         3 (capped)

 647            LOAD_FAST_BORROW         0 (filter_status)

 648            LOAD_FAST_BORROW         1 (filter_stage)

 642            LOAD_CONST              18 (('status', 'profiles', 'count', 'limit', 'filter_status', 'filter_stage'))
                CALL_KW                  6
       L24:     RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 611            LOAD_GLOBAL              8 (TypeError)
                LOAD_GLOBAL             10 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L27)
                NOT_TAKEN
                POP_TOP

 612            LOAD_GLOBAL             12 (_DEFAULT_LIMIT)
                STORE_FAST               3 (capped)
       L26:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 327 (to L4)

 611   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     SWAP                     2
                POP_TOP

 641            SWAP                     2
                STORE_FAST               8 (p)
                RERAISE                  0

  --   L30:     PUSH_EXC_INFO

 650            LOAD_GLOBAL             42 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       94 (to L35)
                NOT_TAKEN
                STORE_FAST              10 (e)

 651   L31:     LOAD_GLOBAL             44 (logger)
                LOAD_ATTR               47 (warning + NULL|self)

 652            LOAD_CONST              19 ('list_profiles read error type=')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 651            CALL                     1
                POP_TOP

 654            LOAD_GLOBAL              3 (_list_envelope + NULL)

 655            LOAD_CONST               6 ('skipped')

 656            LOAD_FAST                3 (capped)

 657            LOAD_FAST                0 (filter_status)

 658            LOAD_FAST                1 (filter_stage)

 659            LOAD_CONST              20 ('db_read_failed:')
                LOAD_GLOBAL             49 (type + NULL)
                LOAD_FAST               10 (e)
                CALL                     1
                LOAD_ATTR               50 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 660            LOAD_CONST               7 ('brokerage_profile_store_unavailable')

 654            LOAD_CONST              21 (('status', 'limit', 'filter_status', 'filter_stage', 'warnings', 'error_code'))
                CALL_KW                  6
       L32:     SWAP                     2
       L33:     POP_EXCEPT
                LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RETURN_VALUE

  --   L34:     LOAD_CONST               0 (None)
                STORE_FAST              10 (e)
                DELETE_FAST             10 (e)
                RERAISE                  1

 650   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L25 [0]
  L8 to L9 -> L30 [0]
  L10 to L12 -> L30 [0]
  L13 to L15 -> L30 [0]
  L16 to L18 -> L30 [0]
  L18 to L20 -> L29 [2]
  L21 to L23 -> L29 [2]
  L23 to L24 -> L30 [0]
  L25 to L26 -> L28 [1] lasti
  L27 to L28 -> L28 [1] lasti
  L29 to L30 -> L30 [0]
  L30 to L31 -> L36 [1] lasti
  L31 to L32 -> L34 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L34 to L36 -> L36 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18090690, file "app\services\brokerage\profile_service.py", line 641>:
 641           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                16 (to L3)
               STORE_FAST               1 (r)
               LOAD_GLOBAL              1 (_project_row + NULL)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\brokerage\profile_service.py", line 668>:
668           RESUME                   0
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

Disassembly of <code object _is_unique_violation at 0x0000018C17F96140, file "app\services\brokerage\profile_service.py", line 668>:
 668           RESUME                   0

 669           NOP

 670   L1:     LOAD_GLOBAL              1 (repr + NULL)
               LOAD_FAST_BORROW         0 (exc)
               CALL                     1
               STORE_FAST               1 (s)

 673   L2:     LOAD_CONST               1 ('23505')
               LOAD_FAST                1 (s)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 674           LOAD_CONST               2 (True)
               RETURN_VALUE

 675   L3:     LOAD_FAST                1 (s)
               LOAD_ATTR                5 (lower + NULL|self)
               CALL                     0
               STORE_FAST               2 (lowered)

 677           LOAD_CONST               3 ('duplicate key value violates unique constraint')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L4)
               NOT_TAKEN
               POP_TOP

 678           LOAD_CONST               4 ('already exists')
               LOAD_FAST                2 (lowered)
               CONTAINS_OP              0 (in)

 676   L4:     RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 671           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L7)
               NOT_TAKEN
               POP_TOP

 672   L6:     POP_EXCEPT
               LOAD_CONST               0 (False)
               RETURN_VALUE

 671   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti
```
