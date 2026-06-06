# brokerage/config_validator

- **pyc:** `app\services\brokerage\__pycache__\config_validator.cpython-314.pyc`
- **expected source path (absent):** `app\services\brokerage/config_validator.py`
- **co_filename (from bytecode):** `app\services\brokerage\config_validator.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** brokerage

## Module docstring

```
PAS173 — Brokerage configuration validator.

Deterministic, presence-only validator. Answers the operator's
question "is this brokerage configured well enough to advance
its onboarding stage / open external traffic?" by combining:

* Per-brokerage row presence checks (twilio_phone,
  slack_webhook_url, calcom config) — values are NEVER
  echoed.
* Process-wide env posture checks (worker default-OFF,
  encryption flags, durable-dedupe flags, alert webhook) —
  values are NEVER echoed.
* Per-brokerage operational posture checks (timezone
  configured, dedupe wired, callbacks wired).

The validator returns warnings ("you can still operate") and
errors ("you cannot advance to LIVE"). The launch-ready helper
collapses both into a single boolean for the operator route.

Doctrine carried by every helper:

* **No secrets, no env values.** Every check is "is this set?"
  (boolean), NEVER "what is the value?". The envelope returns
  the field NAME plus a boolean — never the actual string.
* **No raw payloads, no PII.** The brokerage row may carry
  ``twilio_phone`` etc.; we read presence only.
* **Deterministic.** Same input → same output. No timestamps
  in the warning identifier, no random tie-breaks.
* **Never raises.** A misshapen brokerage row produces a
  structural error envelope; the operator route stays up.
* **Bounded.** Warning + error lists are bounded by the
  closed allow-list below.

Public surface:

  * ``validate_brokerage_configuration(brokerage)``
  * ``validate_brokerage_launch_ready(brokerage, profile=None)``
  * ``configuration_warning_report(brokerage, profile=None)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.config`, `get_settings`, `logging`, `os`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_check_brokerage_row`, `_check_critical_errors`, `_check_process_env`, `_check_profile_posture`, `_has_int`, `_has_str`, `_safe_envelope`, `configuration_warning_report`, `validate_brokerage_configuration`, `validate_brokerage_launch_ready`

## Env-key candidates

`ADMIN_API_KEY`, `CALCOM_API_KEY`, `CALCOM_EVENT_TYPE_ID`, `ENVIRONMENT`, `PAS_ALERT_SLACK_WEBHOOK_URL`, `PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED`, `PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID`, `PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED`, `PENDING_CALLS_WORKER_ENABLED`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`

## String constants (redacted where noted)

- '\nPAS173 — Brokerage configuration validator.\n\nDeterministic, presence-only validator. Answers the operator\'s\nquestion "is this brokerage configured well enough to advance\nits onboarding stage / open external traffic?" by combining:\n\n* Per-brokerage row presence checks (twilio_phone,\n  slack_webhook_url, calcom config) — values are NEVER\n  echoed.\n* Process-wide env posture checks (worker default-OFF,\n  encryption flags, durable-dedupe flags, alert webhook) —\n  values are NEVER echoed.\n* Per-brokerage operational posture checks (timezone\n  configured, dedupe wired, callbacks wired).\n\nThe validator returns warnings ("you can still operate") and\nerrors ("you cannot advance to LIVE"). The launch-ready helper\ncollapses both into a single boolean for the operator route.\n\nDoctrine carried by every helper:\n\n* **No secrets, no env values.** Every check is "is this set?"\n  (boolean), NEVER "what is the value?". The envelope returns\n  the field NAME plus a boolean — never the actual string.\n* **No raw payloads, no PII.** The brokerage row may carry\n  ``twilio_phone`` etc.; we read presence only.\n* **Deterministic.** Same input → same output. No timestamps\n  in the warning identifier, no random tie-breaks.\n* **Never raises.** A misshapen brokerage row produces a\n  structural error envelope; the operator route stays up.\n* **Bounded.** Warning + error lists are bounded by the\n  closed allow-list below.\n\nPublic surface:\n\n  * ``validate_brokerage_configuration(brokerage)``\n  * ``validate_brokerage_launch_ready(brokerage, profile=None)``\n  * ``configuration_warning_report(brokerage, profile=None)``\n'
- 'pas.brokerage.config_validator'
- 'warnings'
- 'errors'
- 'warning_count'
- 'error_count'
- 'launch_ready'
- 'error_code'
- 'profile'
- 'required_pilot_stage'
- 'value'
- 'Any'
- 'return'
- 'bool'
- 'Boolean presence test for a string field. NEVER echoes\nthe value. Returns True iff value is a non-empty string.'
- 'Presence test for an int field that is meaningful when\nnon-zero (e.g. CALCOM_EVENT_TYPE_ID). NEVER echoes.'
- 'status'
- 'str'
- 'Optional[List[str]]'
- 'Optional[int]'
- 'Optional[bool]'
- 'Optional[str]'
- 'Dict[str, Any]'
- 'brokerage'
- 'List[str]'
- 'Per-brokerage row presence checks. NEVER echoes values.'
- 'twilio_phone'
- 'twilio_phone_missing'
- 'slack_webhook_url'
- 'slack_webhook_missing'
- 'Process-wide env posture checks. Presence-only — NEVER\nechoes the value.'
- 'TWILIO_ACCOUNT_SID'
- 'TWILIO_AUTH_TOKEN'
- 'twilio_credentials_missing'
- 'CALCOM_API_KEY'
- 'calcom_api_key_missing'
- 'CALCOM_EVENT_TYPE_ID'
- 'calcom_event_type_missing'
- 'ADMIN_API_KEY'
- 'admin_key_missing'
- 'config_validator settings load error type='
- 'PAS_ALERT_SLACK_WEBHOOK_URL'
- 'alert_slack_webhook_missing'
- 'PENDING_CALLS_WORKER_ENABLED'
- 'true'
- 'worker_enable_set_non_strict'
- 'PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED'
- 'durable_pending_call_dedupe_disabled'
- 'PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED'
- 'durable_callback_schedule_disabled'
- 'PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID'
- 'email_forwarder_secret_unencrypted'
- 'Optional[Dict[str, Any]]'
- 'Per-brokerage operational posture checks against the\nPAS173 profile row.'
- 'brokerage_timezone_missing'
- 'callback_reminder_lookahead_unconfigured'
- 'timezone'
- 'features'
- 'durable_dedupe_enabled'
- 'durable_callbacks_enabled'
- 'heartbeat_enabled'
- 'brokerage_id_missing'
- 'active'
- 'brokerage_inactive'
- 'admin_key_missing_critical'
- 'ENVIRONMENT'
- 'development'
- 'production'
- 'production_environment_with_worker_enable_unset'
- "Validate a brokerage's configuration. Returns a\nstructural envelope with closed-allow-list warnings +\nerrors. NEVER raises. NEVER echoes a secret / env value."
- 'failed'
- 'brokerage_input_not_dict'
- 'Deterministic "can this brokerage advance to LIVE?"\ncheck. Returns the configuration envelope plus a\n``launch_ready`` boolean.\n\nLaunch-ready rules:\n  * zero errors,\n  * onboarding_status in {CONFIGURED, VERIFIED} (or LIVE),\n  * pilot_stage in {TRUSTED_PILOT, EXPANDED_PILOT, PRODUCTION}\n    when ``required_pilot_stage`` is supplied.\n\nNEVER raises.\n'
- 'onboarding_status'
- 'pilot_stage'
- 'Operator-facing summary. Returns the\n``validate_brokerage_configuration`` envelope with the\nextra count surfaces operators want on a dashboard.'
- 'brokerage.configuration_warning_report'
- 'surface'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS173 — Brokerage configuration validator.\n\nDeterministic, presence-only validator. Answers the operator\'s\nquestion "is this brokerage configured well enough to advance\nits onboarding stage / open external traffic?" by combining:\n\n* Per-brokerage row presence checks (twilio_phone,\n  slack_webhook_url, calcom config) — values are NEVER\n  echoed.\n* Process-wide env posture checks (worker default-OFF,\n  encryption flags, durable-dedupe flags, alert webhook) —\n  values are NEVER echoed.\n* Per-brokerage operational posture checks (timezone\n  configured, dedupe wired, callbacks wired).\n\nThe validator returns warnings ("you can still operate") and\nerrors ("you cannot advance to LIVE"). The launch-ready helper\ncollapses both into a single boolean for the operator route.\n\nDoctrine carried by every helper:\n\n* **No secrets, no env values.** Every check is "is this set?"\n  (boolean), NEVER "what is the value?". The envelope returns\n  the field NAME plus a boolean — never the actual string.\n* **No raw payloads, no PII.** The brokerage row may carry\n  ``twilio_phone`` etc.; we read presence only.\n* **Deterministic.** Same input → same output. No timestamps\n  in the warning identifier, no random tie-breaks.\n* **Never raises.** A misshapen brokerage row produces a\n  structural error envelope; the operator route stays up.\n* **Bounded.** Warning + error lists are bounded by the\n  closed allow-list below.\n\nPublic surface:\n\n  * ``validate_brokerage_configuration(brokerage)``\n  * ``validate_brokerage_launch_ready(brokerage, profile=None)``\n  * ``configuration_warning_report(brokerage, profile=None)``\n')
              STORE_NAME               0 (__doc__)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 44           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 45           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 46           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (List)
              STORE_NAME               8 (List)
              IMPORT_FROM              9 (Optional)
              STORE_NAME               9 (Optional)
              POP_TOP

 49           LOAD_NAME                3 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.brokerage.config_validator')
              CALL                     1
              STORE_NAME              11 (logger)

 60           LOAD_CONST              33 (('twilio_credentials_missing', 'twilio_phone_missing', 'slack_webhook_missing', 'alert_slack_webhook_missing', 'calcom_api_key_missing', 'calcom_event_type_missing', 'brokerage_timezone_missing', 'worker_enable_set_non_strict', 'durable_pending_call_dedupe_disabled', 'durable_callback_schedule_disabled', 'email_forwarder_secret_unencrypted', 'callback_reminder_lookahead_unconfigured', 'admin_key_missing'))
              STORE_NAME              12 (ALLOWED_WARNINGS)

 77           LOAD_CONST              34 (('brokerage_id_missing', 'brokerage_inactive', 'admin_key_missing_critical', 'production_environment_with_worker_enable_unset'))
              STORE_NAME              13 (ALLOWED_ERRORS)

 89           LOAD_CONST               5 (<code object __annotate__ at 0x0000018C17FA1E30, file "app\services\brokerage\config_validator.py", line 89>)
              MAKE_FUNCTION
              LOAD_CONST               6 (<code object _has_str at 0x0000018C18038170, file "app\services\brokerage\config_validator.py", line 89>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (_has_str)

 95           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\brokerage\config_validator.py", line 95>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _has_int at 0x0000018C18052F70, file "app\services\brokerage\config_validator.py", line 95>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_has_int)

104           LOAD_CONST               9 ('warnings')

107           LOAD_CONST               2 (None)

104           LOAD_CONST              10 ('errors')

108           LOAD_CONST               2 (None)

104           LOAD_CONST              11 ('warning_count')

109           LOAD_CONST               2 (None)

104           LOAD_CONST              12 ('error_count')

110           LOAD_CONST               2 (None)

104           LOAD_CONST              13 ('launch_ready')

111           LOAD_CONST               2 (None)

104           LOAD_CONST              14 ('error_code')

112           LOAD_CONST               2 (None)

104           BUILD_MAP                6
              LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\brokerage\config_validator.py", line 104>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _safe_envelope at 0x0000018C17FA92F0, file "app\services\brokerage\config_validator.py", line 104>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              16 (_safe_envelope)

127           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2010, file "app\services\brokerage\config_validator.py", line 127>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _check_brokerage_row at 0x0000018C1794E810, file "app\services\brokerage\config_validator.py", line 127>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (_check_brokerage_row)

139           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\brokerage\config_validator.py", line 139>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _check_process_env at 0x0000018C17ED0510, file "app\services\brokerage\config_validator.py", line 139>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_check_process_env)

185           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\brokerage\config_validator.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _check_profile_posture at 0x0000018C17EDAA30, file "app\services\brokerage\config_validator.py", line 185>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_check_profile_posture)

209           LOAD_CONST              35 ((None,))
              LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\brokerage\config_validator.py", line 209>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _check_critical_errors at 0x0000018C17D78310, file "app\services\brokerage\config_validator.py", line 209>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              20 (_check_critical_errors)

245           LOAD_CONST              25 ('profile')

248           LOAD_CONST               2 (None)

245           BUILD_MAP                1
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\brokerage\config_validator.py", line 245>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object validate_brokerage_configuration at 0x0000018C17ED0B40, file "app\services\brokerage\config_validator.py", line 245>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              21 (validate_brokerage_configuration)

278           LOAD_CONST              25 ('profile')

281           LOAD_CONST               2 (None)

278           LOAD_CONST              28 ('required_pilot_stage')

282           LOAD_CONST               2 (None)

278           BUILD_MAP                2
              LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18024D30, file "app\services\brokerage\config_validator.py", line 278>)
              MAKE_FUNCTION
              LOAD_CONST              30 (<code object validate_brokerage_launch_ready at 0x0000018C17FED630, file "app\services\brokerage\config_validator.py", line 278>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              22 (validate_brokerage_launch_ready)

315           LOAD_CONST              25 ('profile')

318           LOAD_CONST               2 (None)

315           BUILD_MAP                1
              LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\brokerage\config_validator.py", line 315>)
              MAKE_FUNCTION
              LOAD_CONST              32 (<code object configuration_warning_report at 0x0000018C18024F30, file "app\services\brokerage\config_validator.py", line 315>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              23 (configuration_warning_report)

328           BUILD_LIST               0
              LOAD_CONST              36 (('ALLOWED_WARNINGS', 'ALLOWED_ERRORS', 'validate_brokerage_configuration', 'validate_brokerage_launch_ready', 'configuration_warning_report'))
              LIST_EXTEND              1
              STORE_NAME              24 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "app\services\brokerage\config_validator.py", line 89>:
 89           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _has_str at 0x0000018C18038170, file "app\services\brokerage\config_validator.py", line 89>:
 89           RESUME                   0

 92           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_FALSE       26 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              5 (bool + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              CALL                     1
      L1:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\brokerage\config_validator.py", line 95>:
 95           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _has_int at 0x0000018C18052F70, file "app\services\brokerage\config_validator.py", line 95>:
  95           RESUME                   0

  98           NOP

  99   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP             103 (!=)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 100           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 101   L4:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

 100   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FBFEE0, file "app\services\brokerage\config_validator.py", line 104>:
104           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('status')

106           LOAD_CONST               2 ('str')

104           LOAD_CONST               3 ('warnings')

107           LOAD_CONST               4 ('Optional[List[str]]')

104           LOAD_CONST               5 ('errors')

108           LOAD_CONST               4 ('Optional[List[str]]')

104           LOAD_CONST               6 ('warning_count')

109           LOAD_CONST               7 ('Optional[int]')

104           LOAD_CONST               8 ('error_count')

110           LOAD_CONST               7 ('Optional[int]')

104           LOAD_CONST               9 ('launch_ready')

111           LOAD_CONST              10 ('Optional[bool]')

104           LOAD_CONST              11 ('error_code')

112           LOAD_CONST              12 ('Optional[str]')

104           LOAD_CONST              13 ('return')

113           LOAD_CONST              14 ('Dict[str, Any]')

104           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object _safe_envelope at 0x0000018C17FA92F0, file "app\services\brokerage\config_validator.py", line 104>:
104           RESUME                   0

114           LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                1 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1
              STORE_FAST               7 (w)

115           LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                2 (errors)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     CALL                     1
              STORE_FAST               8 (e)

117           LOAD_CONST               0 ('status')
              LOAD_FAST                0 (status)

118           LOAD_CONST               1 ('warnings')
              LOAD_FAST                7 (w)

119           LOAD_CONST               2 ('errors')
              LOAD_FAST                8 (e)

120           LOAD_CONST               3 ('warning_count')
              LOAD_FAST_BORROW         3 (warning_count)
              POP_JUMP_IF_NONE         3 (to L3)
              NOT_TAKEN
              LOAD_FAST                3 (warning_count)
              JUMP_FORWARD            10 (to L4)
      L3:     LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         7 (w)
              CALL                     1

121   L4:     LOAD_CONST               4 ('error_count')
              LOAD_FAST_BORROW         4 (error_count)
              POP_JUMP_IF_NONE         3 (to L5)
              NOT_TAKEN
              LOAD_FAST                4 (error_count)
              JUMP_FORWARD            10 (to L6)
      L5:     LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         8 (e)
              CALL                     1

122   L6:     LOAD_CONST               5 ('launch_ready')
              LOAD_FAST_BORROW         5 (launch_ready)

123           LOAD_CONST               6 ('error_code')
              LOAD_FAST_BORROW         6 (error_code)

116           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "app\services\brokerage\config_validator.py", line 127>:
127           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _check_brokerage_row at 0x0000018C1794E810, file "app\services\brokerage\config_validator.py", line 127>:
127           RESUME                   0

129           BUILD_LIST               0
              STORE_FAST               1 (out)

130           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

131           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

132   L1:     LOAD_GLOBAL              5 (_has_str + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               1 ('twilio_phone')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L2)
              NOT_TAKEN

133           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_CONST               2 ('twilio_phone_missing')
              CALL                     1
              POP_TOP

134   L2:     LOAD_GLOBAL              5 (_has_str + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                7 (get + NULL|self)
              LOAD_CONST               3 ('slack_webhook_url')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L3)
              NOT_TAKEN

135           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                9 (append + NULL|self)
              LOAD_CONST               4 ('slack_webhook_missing')
              CALL                     1
              POP_TOP

136   L3:     LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\brokerage\config_validator.py", line 139>:
139           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('List[str]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _check_process_env at 0x0000018C17ED0510, file "app\services\brokerage\config_validator.py", line 139>:
 139            RESUME                   0

 142            BUILD_LIST               0
                STORE_FAST               0 (out)

 144            NOP

 145    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('get_settings',))
                IMPORT_NAME              0 (app.config)
                IMPORT_FROM              1 (get_settings)
                STORE_FAST               1 (get_settings)
                POP_TOP

 146            LOAD_FAST_BORROW         1 (get_settings)
                PUSH_NULL
                CALL                     0
                STORE_FAST               2 (s)

 147            LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         2 (s)
                LOAD_CONST               2 ('TWILIO_ACCOUNT_SID')
                LOAD_CONST               3 ('')
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       29 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         2 (s)
                LOAD_CONST               4 ('TWILIO_AUTH_TOKEN')
                LOAD_CONST               3 ('')
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L3)
                NOT_TAKEN

 148    L2:     LOAD_FAST_BORROW         0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               5 ('twilio_credentials_missing')
                CALL                     1
                POP_TOP

 149    L3:     LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         2 (s)
                LOAD_CONST               6 ('CALCOM_API_KEY')
                LOAD_CONST               3 ('')
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L4)
                NOT_TAKEN

 150            LOAD_FAST_BORROW         0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               7 ('calcom_api_key_missing')
                CALL                     1
                POP_TOP

 151    L4:     LOAD_GLOBAL             11 (_has_int + NULL)
                LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         2 (s)
                LOAD_CONST               8 ('CALCOM_EVENT_TYPE_ID')
                LOAD_SMALL_INT           0
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L5)
                NOT_TAKEN

 152            LOAD_FAST_BORROW         0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               9 ('calcom_event_type_missing')
                CALL                     1
                POP_TOP

 153    L5:     LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL              7 (getattr + NULL)
                LOAD_FAST_BORROW         2 (s)
                LOAD_CONST              10 ('ADMIN_API_KEY')
                LOAD_CONST               3 ('')
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L6)
                NOT_TAKEN

 154            LOAD_FAST_BORROW         0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              11 ('admin_key_missing')
                CALL                     1
                POP_TOP

 161    L6:     LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL             22 (os)
                LOAD_ATTR               24 (environ)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              14 ('PAS_ALERT_SLACK_WEBHOOK_URL')
                CALL                     1
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L7)
                NOT_TAKEN

 162            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              15 ('alert_slack_webhook_missing')
                CALL                     1
                POP_TOP

 166    L7:     LOAD_GLOBAL             22 (os)
                LOAD_ATTR               24 (environ)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              16 ('PENDING_CALLS_WORKER_ENABLED')
                CALL                     1
                STORE_FAST               4 (worker_env)

 167            LOAD_FAST                4 (worker_env)
                POP_JUMP_IF_NONE        25 (to L8)
                NOT_TAKEN
                LOAD_FAST                4 (worker_env)
                LOAD_CONST              17 ('true')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       18 (to L8)
                NOT_TAKEN

 168            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              18 ('worker_enable_set_non_strict')
                CALL                     1
                POP_TOP

 172    L8:     LOAD_GLOBAL             22 (os)
                LOAD_ATTR               24 (environ)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              19 ('PAS_PENDING_CALL_DEDUPE_DURABLE_ENABLED')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
        L9:     LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               31 (lower + NULL|self)
                CALL                     0
                LOAD_CONST              25 (('false', '0', 'no', 'off', 'disabled'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L10)
                NOT_TAKEN

 173            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              20 ('durable_pending_call_dedupe_disabled')
                CALL                     1
                POP_TOP

 174   L10:     LOAD_GLOBAL             22 (os)
                LOAD_ATTR               24 (environ)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              21 ('PAS_CALLBACK_SCHEDULE_DURABLE_ENABLED')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
       L11:     LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               31 (lower + NULL|self)
                CALL                     0
                LOAD_CONST              25 (('false', '0', 'no', 'off', 'disabled'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L12)
                NOT_TAKEN

 175            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              22 ('durable_callback_schedule_disabled')
                CALL                     1
                POP_TOP

 179   L12:     LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL             22 (os)
                LOAD_ATTR               24 (environ)
                LOAD_ATTR               27 (get + NULL|self)
                LOAD_CONST              23 ('PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID')
                CALL                     1
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L13)
                NOT_TAKEN

 180            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              24 ('email_forwarder_secret_unencrypted')
                CALL                     1
                POP_TOP

 182   L13:     LOAD_FAST                0 (out)
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 155            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       72 (to L18)
                NOT_TAKEN
                STORE_FAST               3 (e)

 156   L15:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 157            LOAD_CONST              12 ('config_validator settings load error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 156            CALL                     1
                POP_TOP

 159            LOAD_FAST                0 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              11 ('admin_key_missing')
                CALL                     1
                POP_TOP
       L16:     POP_EXCEPT
                LOAD_CONST              13 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 446 (to L6)

  --   L17:     LOAD_CONST              13 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 155   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L6 -> L14 [0]
  L14 to L15 -> L19 [1] lasti
  L15 to L16 -> L17 [1] lasti
  L17 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\brokerage\config_validator.py", line 185>:
185           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('profile')
              LOAD_CONST               2 ('Optional[Dict[str, Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _check_profile_posture at 0x0000018C17EDAA30, file "app\services\brokerage\config_validator.py", line 185>:
185           RESUME                   0

188           BUILD_LIST               0
              STORE_FAST               1 (out)

189           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (profile)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        37 (to L1)
              NOT_TAKEN

194           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               1 ('brokerage_timezone_missing')
              CALL                     1
              POP_TOP

195           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               2 ('callback_reminder_lookahead_unconfigured')
              CALL                     1
              POP_TOP

196           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

197   L1:     LOAD_GLOBAL              7 (_has_str + NULL)
              LOAD_FAST_BORROW         0 (profile)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               3 ('timezone')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L2)
              NOT_TAKEN

198           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               1 ('brokerage_timezone_missing')
              CALL                     1
              POP_TOP

199   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (profile)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('features')
              CALL                     1
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (profile)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('features')
              CALL                     1
              JUMP_FORWARD             1 (to L4)
      L3:     BUILD_MAP                0
      L4:     STORE_FAST               2 (feats)

200           LOAD_GLOBAL             11 (bool + NULL)
              LOAD_FAST_BORROW         2 (feats)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               5 ('durable_dedupe_enabled')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L5)
              NOT_TAKEN

201           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               6 ('durable_pending_call_dedupe_disabled')
              CALL                     1
              POP_TOP

202   L5:     LOAD_GLOBAL             11 (bool + NULL)
              LOAD_FAST_BORROW         2 (feats)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               7 ('durable_callbacks_enabled')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L6)
              NOT_TAKEN

203           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               8 ('durable_callback_schedule_disabled')
              CALL                     1
              POP_TOP

204   L6:     LOAD_GLOBAL             11 (bool + NULL)
              LOAD_FAST_BORROW         2 (feats)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               9 ('heartbeat_enabled')
              CALL                     1
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        18 (to L7)
              NOT_TAKEN

205           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_CONST               2 ('callback_reminder_lookahead_unconfigured')
              CALL                     1
              POP_TOP

206   L7:     LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\brokerage\config_validator.py", line 209>:
209           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

210           LOAD_CONST               2 ('Any')

209           LOAD_CONST               3 ('profile')

211           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

209           LOAD_CONST               5 ('return')

212           LOAD_CONST               6 ('List[str]')

209           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _check_critical_errors at 0x0000018C17D78310, file "app\services\brokerage\config_validator.py", line 209>:
 209            RESUME                   0

 213            BUILD_LIST               0
                STORE_FAST               2 (out)

 215            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L1)
                NOT_TAKEN
                POP_TOP

 216            LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               0 ('id')
                CALL                     1
                CALL                     1

 214    L1:     STORE_FAST               3 (bid_present)

 218            LOAD_FAST_BORROW         3 (bid_present)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L2)
                NOT_TAKEN

 219            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               1 ('brokerage_id_missing')
                CALL                     1
                POP_TOP

 220    L2:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               2 ('active')
                CALL                     1
                LOAD_CONST               3 (False)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       18 (to L3)
                NOT_TAKEN

 221            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               4 ('brokerage_inactive')
                CALL                     1
                POP_TOP

 223    L3:     NOP

 224    L4:     LOAD_SMALL_INT           0
                LOAD_CONST               5 (('get_settings',))
                IMPORT_NAME              5 (app.config)
                IMPORT_FROM              6 (get_settings)
                STORE_FAST               4 (get_settings)
                POP_TOP

 225            LOAD_FAST_BORROW         4 (get_settings)
                PUSH_NULL
                CALL                     0
                STORE_FAST               5 (s)

 226            LOAD_GLOBAL              5 (_has_str + NULL)
                LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         5 (s)
                LOAD_CONST               6 ('ADMIN_API_KEY')
                LOAD_CONST               7 ('')
                CALL                     3
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L5)
                NOT_TAKEN

 227            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               8 ('admin_key_missing_critical')
                CALL                     1
                POP_TOP

 228    L5:     LOAD_GLOBAL             15 (getattr + NULL)
                LOAD_FAST_BORROW         5 (s)
                LOAD_CONST               9 ('ENVIRONMENT')
                LOAD_CONST              10 ('development')
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              10 ('development')
        L8:     LOAD_ATTR               17 (lower + NULL|self)
                CALL                     0
                STORE_FAST               6 (env_kind)

 236    L9:     LOAD_FAST_BORROW         6 (env_kind)
                LOAD_CONST              11 ('production')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       51 (to L10)
                NOT_TAKEN
                LOAD_GLOBAL             20 (os)
                LOAD_ATTR               22 (environ)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST              12 ('PENDING_CALLS_WORKER_ENABLED')
                CALL                     1
                POP_JUMP_IF_NOT_NONE    18 (to L10)
                NOT_TAKEN

 237            LOAD_FAST_BORROW         2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST              13 ('production_environment_with_worker_enable_unset')
                CALL                     1
                POP_TOP

 238   L10:     LOAD_FAST_BORROW         2 (out)
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 229            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       23 (to L13)
                NOT_TAKEN
                POP_TOP

 230            LOAD_FAST                2 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_CONST               8 ('admin_key_missing_critical')
                CALL                     1
                POP_TOP

 231            LOAD_CONST              10 ('development')
                STORE_FAST               6 (env_kind)
       L12:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 91 (to L9)

 229   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L6 -> L11 [0]
  L7 to L9 -> L11 [0]
  L11 to L12 -> L14 [1] lasti
  L13 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\brokerage\config_validator.py", line 245>:
245           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

246           LOAD_CONST               2 ('Any')

245           LOAD_CONST               3 ('profile')

248           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

245           LOAD_CONST               5 ('return')

249           LOAD_CONST               6 ('Dict[str, Any]')

245           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object validate_brokerage_configuration at 0x0000018C17ED0B40, file "app\services\brokerage\config_validator.py", line 245>:
 245            RESUME                   0

 253            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        17 (to L1)
                NOT_TAKEN

 254            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 255            LOAD_CONST               1 ('failed')

 256            LOAD_CONST               2 ('brokerage_id_missing')
                BUILD_LIST               1

 257            BUILD_LIST               0

 258            LOAD_CONST               3 ('brokerage_input_not_dict')

 254            LOAD_CONST               4 (('status', 'errors', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 260    L1:     BUILD_LIST               0
                STORE_FAST               2 (warnings)

 261            LOAD_FAST_BORROW         2 (warnings)
                LOAD_ATTR                7 (extend + NULL|self)
                LOAD_GLOBAL              9 (_check_brokerage_row + NULL)
                LOAD_FAST_BORROW         0 (brokerage)
                CALL                     1
                CALL                     1
                POP_TOP

 262            LOAD_FAST_BORROW         2 (warnings)
                LOAD_ATTR                7 (extend + NULL|self)
                LOAD_GLOBAL             11 (_check_process_env + NULL)
                CALL                     0
                CALL                     1
                POP_TOP

 263            LOAD_FAST_BORROW         2 (warnings)
                LOAD_ATTR                7 (extend + NULL|self)
                LOAD_GLOBAL             13 (_check_profile_posture + NULL)
                LOAD_FAST_BORROW         1 (profile)
                CALL                     1
                CALL                     1
                POP_TOP

 266            LOAD_GLOBAL              2 (dict)
                LOAD_ATTR               15 (fromkeys + NULL|self)
                LOAD_FAST_BORROW         2 (warnings)
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      3 (w)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                17 (to L6)
                STORE_FAST_LOAD_FAST    51 (w, w)
                LOAD_GLOBAL             16 (ALLOWED_WARNINGS)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           15 (to L3)
        L5:     LOAD_FAST_BORROW         3 (w)
                LIST_APPEND              2
                JUMP_BACKWARD           19 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               2 (warnings)
                STORE_FAST               3 (w)

 268            LOAD_GLOBAL             19 (_check_critical_errors + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage, profile)
                LOAD_CONST               5 (('profile',))
                CALL_KW                  2
                STORE_FAST               4 (errors)

 269            LOAD_GLOBAL              2 (dict)
                LOAD_ATTR               15 (fromkeys + NULL|self)
                LOAD_FAST_BORROW         4 (errors)
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      5 (e)
                SWAP                     2
        L8:     BUILD_LIST               0
                SWAP                     2
        L9:     FOR_ITER                17 (to L12)
                STORE_FAST_LOAD_FAST    85 (e, e)
                LOAD_GLOBAL             20 (ALLOWED_ERRORS)
                CONTAINS_OP              0 (in)
       L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           15 (to L9)
       L11:     LOAD_FAST_BORROW         5 (e)
                LIST_APPEND              2
                JUMP_BACKWARD           19 (to L9)
       L12:     END_FOR
                POP_ITER
       L13:     STORE_FAST               4 (errors)
                STORE_FAST               5 (e)

 271            LOAD_GLOBAL              5 (_safe_envelope + NULL)

 272            LOAD_CONST               6 ('ok')

 273            LOAD_FAST_BORROW         2 (warnings)

 274            LOAD_FAST_BORROW         4 (errors)

 271            LOAD_CONST               7 (('status', 'warnings', 'errors'))
                CALL_KW                  3
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 266            SWAP                     2
                STORE_FAST               3 (w)
                RERAISE                  0

  --   L15:     SWAP                     2
                POP_TOP

 269            SWAP                     2
                STORE_FAST               5 (e)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L14 [2]
  L5 to L7 -> L14 [2]
  L8 to L10 -> L15 [2]
  L11 to L13 -> L15 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024D30, file "app\services\brokerage\config_validator.py", line 278>:
278           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

279           LOAD_CONST               2 ('Any')

278           LOAD_CONST               3 ('profile')

281           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

278           LOAD_CONST               5 ('required_pilot_stage')

282           LOAD_CONST               6 ('Optional[str]')

278           LOAD_CONST               7 ('return')

283           LOAD_CONST               8 ('Dict[str, Any]')

278           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object validate_brokerage_launch_ready at 0x0000018C17FED630, file "app\services\brokerage\config_validator.py", line 278>:
 278           RESUME                   0

 296           LOAD_GLOBAL              1 (validate_brokerage_configuration + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage, profile)
               LOAD_CONST               1 (('profile',))
               CALL_KW                  2
               STORE_FAST               3 (env)

 297           LOAD_FAST_BORROW         3 (env)
               LOAD_CONST               2 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               3 ('ok')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        8 (to L1)
               NOT_TAKEN

 298           LOAD_CONST               4 (False)
               LOAD_FAST_BORROW         3 (env)
               LOAD_CONST               5 ('launch_ready')
               STORE_SUBSCR

 299           LOAD_FAST_BORROW         3 (env)
               RETURN_VALUE

 300   L1:     LOAD_FAST_BORROW         3 (env)
               LOAD_CONST               6 ('error_count')
               BINARY_OP               26 ([])
               LOAD_SMALL_INT           0
               COMPARE_OP              72 (==)
               STORE_FAST               4 (launch_ready)

 302           LOAD_GLOBAL              3 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (profile)
               LOAD_GLOBAL              4 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       60 (to L4)
               NOT_TAKEN

 303           LOAD_FAST_BORROW         1 (profile)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               7 ('onboarding_status')
               CALL                     1
               STORE_FAST               5 (ob)

 304           LOAD_FAST_BORROW         5 (ob)
               LOAD_CONST               9 (('CONFIGURED', 'VERIFIED', 'LIVE'))
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

 305           LOAD_CONST               4 (False)
               STORE_FAST               4 (launch_ready)

 306   L2:     LOAD_FAST_BORROW         2 (required_pilot_stage)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L3)
               NOT_TAKEN

 307           LOAD_FAST_BORROW         1 (profile)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               8 ('pilot_stage')
               CALL                     1
               LOAD_FAST_BORROW         2 (required_pilot_stage)
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 308           LOAD_CONST               4 (False)
               STORE_FAST               4 (launch_ready)

  --   L3:     JUMP_FORWARD             2 (to L5)

 310   L4:     LOAD_CONST               4 (False)
               STORE_FAST               4 (launch_ready)

 311   L5:     LOAD_GLOBAL              9 (bool + NULL)
               LOAD_FAST_BORROW         4 (launch_ready)
               CALL                     1
               LOAD_FAST_BORROW         3 (env)
               LOAD_CONST               5 ('launch_ready')
               STORE_SUBSCR

 312           LOAD_FAST_BORROW         3 (env)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\brokerage\config_validator.py", line 315>:
315           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

316           LOAD_CONST               2 ('Any')

315           LOAD_CONST               3 ('profile')

318           LOAD_CONST               4 ('Optional[Dict[str, Any]]')

315           LOAD_CONST               5 ('return')

319           LOAD_CONST               6 ('Dict[str, Any]')

315           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object configuration_warning_report at 0x0000018C18024F30, file "app\services\brokerage\config_validator.py", line 315>:
315           RESUME                   0

323           LOAD_GLOBAL              1 (validate_brokerage_configuration + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (brokerage, profile)
              LOAD_CONST               1 (('profile',))
              CALL_KW                  2
              STORE_FAST               2 (env)

324           LOAD_CONST               2 ('brokerage.configuration_warning_report')
              LOAD_FAST_BORROW         2 (env)
              LOAD_CONST               3 ('surface')
              STORE_SUBSCR

325           LOAD_FAST_BORROW         2 (env)
              RETURN_VALUE
```
