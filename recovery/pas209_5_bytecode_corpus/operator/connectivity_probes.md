# operator/connectivity_probes

- **pyc:** `app\services\operator\__pycache__\connectivity_probes.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/connectivity_probes.py`
- **co_filename (from bytecode):** `app\services\operator\connectivity_probes.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS174 — Connectivity probes (DRY-RUN ONLY).

Operator-facing diagnostic helpers. Every probe is structural
validation only — config presence, auth-header shape, hostname
format. **NO real outbound calls.** **NO real Slack post.**
**NO real Cal.com booking.** **NO email send.** **NO secret
echo.**

Doctrine carried by every probe:

* **No real outbound traffic.** Even when a webhook URL or an
  API key is configured, the probe returns a structural
  envelope based on the shape of the configured values. Real
  reachability stays an operator-side `curl`.
* **Deterministic.** Same input → same envelope (modulo the
  iso timestamp, which is informational only).
* **No secret echo.** Probes return ``has_<field>: bool``
  shapes plus structural fingerprints (e.g. URL host, first
  3 chars of a key prefix) — NEVER full values.
* **Closed health-status enum** ``{ok, warning, failed,
  skipped}``.
* **Never raises.** Bad input collapses to a ``failed`` /
  ``skipped`` envelope.
* **No env value persistence.** Probes read settings + env in
  memory but NEVER write the value to logs / events /
  responses.

Public surface:

  * ``probe_twilio_configuration(brokerage=None)``
  * ``probe_slack_webhook(brokerage=None)``
  * ``probe_calcom_configuration(brokerage=None)``
  * ``probe_worker_visibility()``
  * ``probe_encryption_posture()``
  * ``run_all_probes(brokerage=None)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.config`, `app.services.worker.heartbeat_monitor`, `datetime`, `get_settings`, `heartbeat_monitor_report`, `logging`, `os`, `re`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_envelope`, `_has_int`, `_has_str`, `_now_iso`, `_prefix_fingerprint`, `_settings_safe`, `_validate_https_url_shape`, `probe_calcom_configuration`, `probe_encryption_posture`, `probe_slack_webhook`, `probe_twilio_configuration`, `probe_worker_visibility`, `run_all_probes`

## Env-key candidates

`CALCOM_API_KEY`, `CALCOM_EVENT_TYPE_ID`, `PAS_ALERT_SLACK_WEBHOOK_URL`, `PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID`, `PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_`, `PENDING_CALLS_WORKER_ENABLED`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`

## String constants (redacted where noted)

- '\nPAS174 — Connectivity probes (DRY-RUN ONLY).\n\nOperator-facing diagnostic helpers. Every probe is structural\nvalidation only — config presence, auth-header shape, hostname\nformat. **NO real outbound calls.** **NO real Slack post.**\n**NO real Cal.com booking.** **NO email send.** **NO secret\necho.**\n\nDoctrine carried by every probe:\n\n* **No real outbound traffic.** Even when a webhook URL or an\n  API key is configured, the probe returns a structural\n  envelope based on the shape of the configured values. Real\n  reachability stays an operator-side `curl`.\n* **Deterministic.** Same input → same envelope (modulo the\n  iso timestamp, which is informational only).\n* **No secret echo.** Probes return ``has_<field>: bool``\n  shapes plus structural fingerprints (e.g. URL host, first\n  3 chars of a key prefix) — NEVER full values.\n* **Closed health-status enum** ``{ok, warning, failed,\n  skipped}``.\n* **Never raises.** Bad input collapses to a ``failed`` /\n  ``skipped`` envelope.\n* **No env value persistence.** Probes read settings + env in\n  memory but NEVER write the value to logs / events /\n  responses.\n\nPublic surface:\n\n  * ``probe_twilio_configuration(brokerage=None)``\n  * ``probe_slack_webhook(brokerage=None)``\n  * ``probe_calcom_configuration(brokerage=None)``\n  * ``probe_worker_visibility()``\n  * ``probe_encryption_posture()``\n  * ``run_all_probes(brokerage=None)``\n'
- 'pas.operator.connectivity_probes'
- '^https?://([^/?#\\s]+)(/.*)?$'
- 'warnings'
- 'error_code'
- 'return'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'bool'
- 'Optional[str]'
- 'Return a short ``<prefix>...`` fingerprint of a string-\nvalued credential or webhook URL. NEVER returns the full\nvalue. Returns ``None`` for non-string / empty inputs.'
- '***'
- 'Dict[str, Any]'
- 'Return a structural classification of a URL. NEVER\nreturns the raw URL value.'
- 'present'
- 'valid_shape'
- 'host'
- 'scheme'
- 'warning'
- 'url_missing'
- 'url_malformed'
- 'https://'
- 'https'
- 'http'
- 'url_not_https'
- 'probe_type'
- 'status'
- 'summary'
- 'Optional[List[str]]'
- 'generated_at'
- 'connectivity_probes settings load error type='
- 'brokerage'
- 'Verify Twilio configuration shape WITHOUT placing a real\ncall. Checks settings presence + brokerage twilio_phone +\nfingerprints only. NEVER dials.'
- 'twilio_account_sid_present'
- 'TWILIO_ACCOUNT_SID'
- 'twilio_auth_token_present'
- 'TWILIO_AUTH_TOKEN'
- 'twilio_account_sid_fingerprint'
- 'brokerage_twilio_phone_present'
- 'twilio_phone'
- 'twilio_credentials_missing'
- 'brokerage_twilio_phone_missing'
- 'twilio'
- 'Verify Slack webhook configuration shape WITHOUT\nposting. Checks operator webhook URL + per-brokerage\nwebhook URL shapes only. NEVER POSTs.'
- 'PAS_ALERT_SLACK_WEBHOOK_URL'
- 'slack_webhook_url'
- 'alert_slack_webhook_url'
- 'operator_webhook'
- 'brokerage_summary_webhook'
- 'brokerage_alert_webhook'
- 'operator_webhook_fingerprint'
- 'alert_slack_webhook_missing'
- 'operator_webhook:'
- 'brokerage_summary_webhook_missing'
- 'brokerage_alert_webhook_missing'
- 'slack_webhook'
- 'Verify Cal.com configuration shape WITHOUT booking.\nChecks api key + event type id presence + the brokerage\ntimezone field. NEVER books.'
- 'calcom_api_key_present'
- 'CALCOM_API_KEY'
- 'calcom_event_type_present'
- 'CALCOM_EVENT_TYPE_ID'
- 'calcom_api_key_fingerprint'
- 'brokerage_timezone_present'
- 'timezone'
- 'calcom_api_key_missing'
- 'calcom_event_type_missing'
- 'brokerage_timezone_missing'
- 'calcom'
- 'Verify the worker is wired into the heartbeat monitor\nsurface. Does NOT start, restart, or kill any worker.\nReads the heartbeat snapshot only.'
- 'worker_enable_env_set'
- 'PENDING_CALLS_WORKER_ENABLED'
- 'worker_enable_strict'
- 'true'
- 'heartbeat_store_reachable'
- 'heartbeat_row_count'
- 'oldest_heartbeat_age_seconds'
- 'total'
- 'oldest_age_seconds'
- 'heartbeat_store_unavailable'
- 'probe_worker_visibility error type='
- 'heartbeat_probe_error:'
- 'worker_enable_set_non_strict'
- 'worker_visibility'
- 'Verify the email-forwarder secret-at-rest encryption\nposture. Reads env-flag presence only — NEVER decrypts,\nNEVER echoes the kid or the key.'
- 'PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID'
- 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_'
- 'active_kid_set'
- 'kid_envelope_count'
- 'encryption_enabled'
- 'email_forwarder_secret_unencrypted'
- 'email_forwarder_kid_set_without_key'
- 'encryption_posture'
- 'Run every probe and return a combined structural\nenvelope. NEVER raises. NEVER places real outbound traffic.'
- 'failed'
- 'skipped'
- 'probe_count'
- 'ok_count'
- 'warning_count'
- 'failed_count'
- 'skipped_count'
- 'probes'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS174 — Connectivity probes (DRY-RUN ONLY).\n\nOperator-facing diagnostic helpers. Every probe is structural\nvalidation only — config presence, auth-header shape, hostname\nformat. **NO real outbound calls.** **NO real Slack post.**\n**NO real Cal.com booking.** **NO email send.** **NO secret\necho.**\n\nDoctrine carried by every probe:\n\n* **No real outbound traffic.** Even when a webhook URL or an\n  API key is configured, the probe returns a structural\n  envelope based on the shape of the configured values. Real\n  reachability stays an operator-side `curl`.\n* **Deterministic.** Same input → same envelope (modulo the\n  iso timestamp, which is informational only).\n* **No secret echo.** Probes return ``has_<field>: bool``\n  shapes plus structural fingerprints (e.g. URL host, first\n  3 chars of a key prefix) — NEVER full values.\n* **Closed health-status enum** ``{ok, warning, failed,\n  skipped}``.\n* **Never raises.** Bad input collapses to a ``failed`` /\n  ``skipped`` envelope.\n* **No env value persistence.** Probes read settings + env in\n  memory but NEVER write the value to logs / events /\n  responses.\n\nPublic surface:\n\n  * ``probe_twilio_configuration(brokerage=None)``\n  * ``probe_slack_webhook(brokerage=None)``\n  * ``probe_calcom_configuration(brokerage=None)``\n  * ``probe_worker_visibility()``\n  * ``probe_encryption_posture()``\n  * ``run_all_probes(brokerage=None)``\n')
              STORE_NAME               0 (__doc__)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (re)
              STORE_NAME               5 (re)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timezone'))
              IMPORT_NAME              6 (datetime)
              IMPORT_FROM              6 (datetime)
              STORE_NAME               6 (datetime)
              IMPORT_FROM              7 (timezone)
              STORE_NAME               7 (timezone)
              POP_TOP

 45           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              8 (typing)
              IMPORT_FROM              9 (Any)
              STORE_NAME               9 (Any)
              IMPORT_FROM             10 (Dict)
              STORE_NAME              10 (Dict)
              IMPORT_FROM             11 (List)
              STORE_NAME              11 (List)
              IMPORT_FROM             12 (Optional)
              STORE_NAME              12 (Optional)
              POP_TOP

 48           LOAD_NAME                3 (logging)
              LOAD_ATTR               26 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.connectivity_probes')
              CALL                     1
              STORE_NAME              14 (logger)

 55           LOAD_CONST              34 (('ok', 'warning', 'failed', 'skipped'))
              STORE_NAME              15 (ALLOWED_PROBE_STATUSES)

 57           LOAD_CONST              35 (('twilio', 'slack_webhook', 'calcom', 'worker_visibility', 'encryption_posture'))
              STORE_NAME              16 (ALLOWED_PROBE_TYPES)

 67           LOAD_SMALL_INT           3
              STORE_NAME              17 (_FINGERPRINT_PREFIX_LEN)

 74           LOAD_CONST               6 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\connectivity_probes.py", line 74>)
              MAKE_FUNCTION
              LOAD_CONST               7 (<code object _now_iso at 0x0000018C18038CB0, file "app\services\operator\connectivity_probes.py", line 74>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (_now_iso)

 78           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\connectivity_probes.py", line 78>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _has_str at 0x0000018C18038670, file "app\services\operator\connectivity_probes.py", line 78>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_has_str)

 82           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\connectivity_probes.py", line 82>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _has_int at 0x0000018C18053CF0, file "app\services\operator\connectivity_probes.py", line 82>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_has_int)

 89           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\connectivity_probes.py", line 89>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _prefix_fingerprint at 0x0000018C18010B30, file "app\services\operator\connectivity_probes.py", line 89>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_prefix_fingerprint)

101           LOAD_NAME                5 (re)
              LOAD_ATTR               44 (compile)
              PUSH_NULL
              LOAD_CONST              14 ('^https?://([^/?#\\s]+)(/.*)?$')
              LOAD_NAME                5 (re)
              LOAD_ATTR               46 (IGNORECASE)
              CALL                     2
              STORE_NAME              24 (_URL_RE)

104           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\connectivity_probes.py", line 104>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _validate_https_url_shape at 0x0000018C17E93990, file "app\services\operator\connectivity_probes.py", line 104>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_validate_https_url_shape)

134           LOAD_CONST              17 ('warnings')

139           LOAD_CONST               2 (None)

134           LOAD_CONST              18 ('error_code')

140           LOAD_CONST               2 (None)

134           BUILD_MAP                2
              LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\connectivity_probes.py", line 134>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _envelope at 0x0000018C1802C620, file "app\services\operator\connectivity_probes.py", line 134>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              26 (_envelope)

152           LOAD_CONST              21 (<code object _settings_safe at 0x0000018C17FF13B0, file "app\services\operator\connectivity_probes.py", line 152>)
              MAKE_FUNCTION
              STORE_NAME              27 (_settings_safe)

168           LOAD_CONST              36 ((None,))
              LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\connectivity_probes.py", line 168>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object probe_twilio_configuration at 0x0000018C17D52180, file "app\services\operator\connectivity_probes.py", line 168>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              28 (probe_twilio_configuration)

199           LOAD_CONST              36 ((None,))
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\connectivity_probes.py", line 199>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object probe_slack_webhook at 0x0000018C17D81910, file "app\services\operator\connectivity_probes.py", line 199>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              29 (probe_slack_webhook)

235           LOAD_CONST              36 ((None,))
              LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\connectivity_probes.py", line 235>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object probe_calcom_configuration at 0x0000018C17ED9FB0, file "app\services\operator\connectivity_probes.py", line 235>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              30 (probe_calcom_configuration)

268           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\connectivity_probes.py", line 268>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object probe_worker_visibility at 0x0000018C17EF9A30, file "app\services\operator\connectivity_probes.py", line 268>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (probe_worker_visibility)

307           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\connectivity_probes.py", line 307>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object probe_encryption_posture at 0x0000018C17EDA2D0, file "app\services\operator\connectivity_probes.py", line 307>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (probe_encryption_posture)

337           LOAD_CONST              36 ((None,))
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\operator\connectivity_probes.py", line 337>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object run_all_probes at 0x0000018C17D8C5C0, file "app\services\operator\connectivity_probes.py", line 337>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              33 (run_all_probes)

370           BUILD_LIST               0
              LOAD_CONST              37 (('ALLOWED_PROBE_STATUSES', 'ALLOWED_PROBE_TYPES', 'probe_twilio_configuration', 'probe_slack_webhook', 'probe_calcom_configuration', 'probe_worker_visibility', 'probe_encryption_posture', 'run_all_probes'))
              LIST_EXTEND              1
              STORE_NAME              34 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\connectivity_probes.py", line 74>:
 74           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_iso at 0x0000018C18038CB0, file "app\services\operator\connectivity_probes.py", line 74>:
 74           RESUME                   0

 75           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              LOAD_ATTR                9 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "app\services\operator\connectivity_probes.py", line 78>:
 78           RESUME                   0
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

Disassembly of <code object _has_str at 0x0000018C18038670, file "app\services\operator\connectivity_probes.py", line 78>:
 78           RESUME                   0

 79           LOAD_GLOBAL              1 (isinstance + NULL)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\connectivity_probes.py", line 82>:
 82           RESUME                   0
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

Disassembly of <code object _has_int at 0x0000018C18053CF0, file "app\services\operator\connectivity_probes.py", line 82>:
  82           RESUME                   0

  83           NOP

  84   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               LOAD_SMALL_INT           0
               COMPARE_OP             103 (!=)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  85           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

  86   L4:     POP_EXCEPT
               LOAD_CONST               1 (False)
               RETURN_VALUE

  85   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\connectivity_probes.py", line 89>:
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
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _prefix_fingerprint at 0x0000018C18010B30, file "app\services\operator\connectivity_probes.py", line 89>:
 89           RESUME                   0

 93           LOAD_GLOBAL              1 (_has_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 94           LOAD_CONST               1 (None)
              RETURN_VALUE

 95   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                3 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 96           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              6 (_FINGERPRINT_PREFIX_LEN)
              COMPARE_OP              58 (bool(<=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 97           LOAD_CONST               2 ('***')
              RETURN_VALUE

 98   L2:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              LOAD_GLOBAL              6 (_FINGERPRINT_PREFIX_LEN)
              BINARY_SLICE
              FORMAT_SIMPLE
              LOAD_CONST               2 ('***')
              BUILD_STRING             2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\connectivity_probes.py", line 104>:
104           RESUME                   0
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

Disassembly of <code object _validate_https_url_shape at 0x0000018C17E93990, file "app\services\operator\connectivity_probes.py", line 104>:
104           RESUME                   0

107           LOAD_GLOBAL              1 (_has_str + NULL)
              LOAD_FAST_BORROW         0 (value)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        13 (to L1)
              NOT_TAKEN

109           LOAD_CONST               1 ('present')
              LOAD_CONST               2 (False)

110           LOAD_CONST               3 ('valid_shape')
              LOAD_CONST               2 (False)

111           LOAD_CONST               4 ('host')
              LOAD_CONST               5 (None)

112           LOAD_CONST               6 ('scheme')
              LOAD_CONST               5 (None)

113           LOAD_CONST               7 ('warning')
              LOAD_CONST               8 ('url_missing')

108           BUILD_MAP                5
              RETURN_VALUE

115   L1:     LOAD_GLOBAL              2 (_URL_RE)
              LOAD_ATTR                5 (match + NULL|self)
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              CALL                     1
              STORE_FAST               1 (m)

116           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_TRUE        13 (to L2)
              NOT_TAKEN

118           LOAD_CONST               1 ('present')
              LOAD_CONST               9 (True)

119           LOAD_CONST               3 ('valid_shape')
              LOAD_CONST               2 (False)

120           LOAD_CONST               4 ('host')
              LOAD_CONST               5 (None)

121           LOAD_CONST               6 ('scheme')
              LOAD_CONST               5 (None)

122           LOAD_CONST               7 ('warning')
              LOAD_CONST              10 ('url_malformed')

117           BUILD_MAP                5
              RETURN_VALUE

124   L2:     LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR                9 (group + NULL|self)
              LOAD_SMALL_INT           1
              CALL                     1
              LOAD_ATTR               11 (lower + NULL|self)
              CALL                     0
              STORE_FAST               2 (host)

126           LOAD_CONST               1 ('present')
              LOAD_CONST               9 (True)

127           LOAD_CONST               3 ('valid_shape')
              LOAD_CONST               9 (True)

128           LOAD_CONST               4 ('host')
              LOAD_FAST                2 (host)

129           LOAD_CONST               6 ('scheme')
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               11 (lower + NULL|self)
              CALL                     0
              LOAD_ATTR               13 (startswith + NULL|self)
              LOAD_CONST              11 ('https://')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST              12 ('https')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST              13 ('http')

130   L4:     LOAD_CONST               7 ('warning')
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                7 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               11 (lower + NULL|self)
              CALL                     0
              LOAD_ATTR               13 (startswith + NULL|self)
              LOAD_CONST              11 ('https://')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L5)
              NOT_TAKEN
              LOAD_CONST               5 (None)

125           BUILD_MAP                5
              RETURN_VALUE

130   L5:     LOAD_CONST              14 ('url_not_https')

125           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\connectivity_probes.py", line 134>:
134           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('probe_type')

136           LOAD_CONST               2 ('str')

134           LOAD_CONST               3 ('status')

137           LOAD_CONST               2 ('str')

134           LOAD_CONST               4 ('summary')

138           LOAD_CONST               5 ('Dict[str, Any]')

134           LOAD_CONST               6 ('warnings')

139           LOAD_CONST               7 ('Optional[List[str]]')

134           LOAD_CONST               8 ('error_code')

140           LOAD_CONST               9 ('Optional[str]')

134           LOAD_CONST              10 ('return')

141           LOAD_CONST               5 ('Dict[str, Any]')

134           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _envelope at 0x0000018C1802C620, file "app\services\operator\connectivity_probes.py", line 134>:
134           RESUME                   0

143           LOAD_CONST               0 ('probe_type')
              LOAD_FAST                0 (probe_type)

144           LOAD_CONST               1 ('status')
              LOAD_FAST                1 (status)

145           LOAD_CONST               2 ('summary')
              LOAD_FAST                2 (summary)

146           LOAD_CONST               3 ('warnings')
              LOAD_GLOBAL              1 (list + NULL)
              LOAD_FAST                3 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

147           LOAD_CONST               4 ('error_code')
              LOAD_FAST_BORROW         4 (error_code)

148           LOAD_CONST               5 ('generated_at')
              LOAD_GLOBAL              3 (_now_iso + NULL)
              CALL                     0

142           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _settings_safe at 0x0000018C17FF13B0, file "app\services\operator\connectivity_probes.py", line 152>:
 152           RESUME                   0

 153           NOP

 154   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_settings',))
               IMPORT_NAME              0 (app.config)
               IMPORT_FROM              1 (get_settings)
               STORE_FAST               0 (get_settings)
               POP_TOP

 155           LOAD_FAST_BORROW         0 (get_settings)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 156           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 157   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 158           LOAD_CONST               2 ('connectivity_probes settings load error type=')

 159           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 158           BUILD_STRING             2

 157           CALL                     1
               POP_TOP

 161   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 156   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\connectivity_probes.py", line 168>:
168           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object probe_twilio_configuration at 0x0000018C17D52180, file "app\services\operator\connectivity_probes.py", line 168>:
168            RESUME                   0

172            LOAD_GLOBAL              1 (_settings_safe + NULL)
               CALL                     0
               STORE_FAST               1 (s)

174            LOAD_CONST               1 ('twilio_account_sid_present')
               LOAD_GLOBAL              3 (_has_str + NULL)
               LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               2 ('TWILIO_ACCOUNT_SID')
               LOAD_CONST               3 ('')
               CALL                     3
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               4 (None)
       L2:     CALL                     1

175            LOAD_CONST               5 ('twilio_auth_token_present')
               LOAD_GLOBAL              3 (_has_str + NULL)
               LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               6 ('TWILIO_AUTH_TOKEN')
               LOAD_CONST               3 ('')
               CALL                     3
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 (None)
       L4:     CALL                     1

176            LOAD_CONST               7 ('twilio_account_sid_fingerprint')
               LOAD_GLOBAL              7 (_prefix_fingerprint + NULL)

177            LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               2 ('TWILIO_ACCOUNT_SID')
               LOAD_CONST               3 ('')
               CALL                     3
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               4 (None)

176    L6:     CALL                     1

179            LOAD_CONST               8 ('brokerage_twilio_phone_present')
               LOAD_CONST               9 (False)

173            BUILD_MAP                4
               STORE_FAST               2 (summary)

181            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L7)
               NOT_TAKEN

182            LOAD_GLOBAL              3 (_has_str + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_ATTR               13 (get + NULL|self)
               LOAD_CONST              10 ('twilio_phone')
               CALL                     1
               CALL                     1
               LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               8 ('brokerage_twilio_phone_present')
               STORE_SUBSCR

184    L7:     BUILD_LIST               0
               STORE_FAST               3 (warnings)

185            LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               1 ('twilio_account_sid_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_FALSE       16 (to L8)
               NOT_TAKEN
               LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               5 ('twilio_auth_token_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L9)
               NOT_TAKEN

186    L8:     LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              11 ('twilio_credentials_missing')
               CALL                     1
               POP_TOP

187    L9:     LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               8 ('brokerage_twilio_phone_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L10)
               NOT_TAKEN

188            LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              12 ('brokerage_twilio_phone_missing')
               CALL                     1
               POP_TOP

190   L10:     LOAD_FAST_BORROW         3 (warnings)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               LOAD_CONST              13 ('ok')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              14 ('warning')
      L12:     STORE_FAST               4 (status)

191            LOAD_GLOBAL             17 (_envelope + NULL)

192            LOAD_CONST              15 ('twilio')

193            LOAD_FAST_BORROW         4 (status)

194            LOAD_FAST_BORROW         2 (summary)

195            LOAD_FAST_BORROW         3 (warnings)

191            LOAD_CONST              16 (('probe_type', 'status', 'summary', 'warnings'))
               CALL_KW                  4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\connectivity_probes.py", line 199>:
199           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object probe_slack_webhook at 0x0000018C17D81910, file "app\services\operator\connectivity_probes.py", line 199>:
199            RESUME                   0

203            LOAD_GLOBAL              0 (os)
               LOAD_ATTR                2 (environ)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               1 ('PAS_ALERT_SLACK_WEBHOOK_URL')
               LOAD_CONST               2 ('')
               CALL                     2
               STORE_FAST               1 (operator_url)

204            LOAD_GLOBAL              7 (_validate_https_url_shape + NULL)
               LOAD_FAST_BORROW         1 (operator_url)
               CALL                     1
               STORE_FAST               2 (op_shape)

206            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               3 ('slack_webhook_url')
               CALL                     1
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               4 (None)
       L2:     STORE_FAST               3 (brokerage_url)

207            LOAD_GLOBAL              9 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL             10 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L3)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               5 ('alert_slack_webhook_url')
               CALL                     1
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 (None)
       L4:     STORE_FAST               4 (brokerage_alert_url)

208            LOAD_GLOBAL              7 (_validate_https_url_shape + NULL)
               LOAD_FAST_BORROW         3 (brokerage_url)
               CALL                     1
               STORE_FAST               5 (br_shape)

209            LOAD_GLOBAL              7 (_validate_https_url_shape + NULL)
               LOAD_FAST_BORROW         4 (brokerage_alert_url)
               CALL                     1
               STORE_FAST               6 (br_alert)

212            LOAD_CONST               6 ('operator_webhook')
               LOAD_FAST_BORROW         2 (op_shape)

213            LOAD_CONST               7 ('brokerage_summary_webhook')
               LOAD_FAST_BORROW         5 (br_shape)

214            LOAD_CONST               8 ('brokerage_alert_webhook')
               LOAD_FAST_BORROW         6 (br_alert)

215            LOAD_CONST               9 ('operator_webhook_fingerprint')
               LOAD_GLOBAL             13 (_prefix_fingerprint + NULL)
               LOAD_FAST_BORROW         1 (operator_url)
               CALL                     1

211            BUILD_MAP                4
               STORE_FAST               7 (summary)

217            BUILD_LIST               0
               STORE_FAST               8 (warnings)

218            LOAD_FAST_BORROW         2 (op_shape)
               LOAD_CONST              10 ('present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L5)
               NOT_TAKEN

219            LOAD_FAST_BORROW         8 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              11 ('alert_slack_webhook_missing')
               CALL                     1
               POP_TOP
               JUMP_FORWARD            42 (to L6)

220    L5:     LOAD_FAST_BORROW         2 (op_shape)
               LOAD_CONST              12 ('warning')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L6)
               NOT_TAKEN

221            LOAD_FAST_BORROW         8 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              13 ('operator_webhook:')
               LOAD_FAST_BORROW         2 (op_shape)
               LOAD_CONST              12 ('warning')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

222    L6:     LOAD_FAST_BORROW         5 (br_shape)
               LOAD_CONST              10 ('present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L7)
               NOT_TAKEN

223            LOAD_FAST_BORROW         8 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              14 ('brokerage_summary_webhook_missing')
               CALL                     1
               POP_TOP

224    L7:     LOAD_FAST_BORROW         6 (br_alert)
               LOAD_CONST              10 ('present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L8)
               NOT_TAKEN

225            LOAD_FAST_BORROW         8 (warnings)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST              15 ('brokerage_alert_webhook_missing')
               CALL                     1
               POP_TOP

226    L8:     LOAD_FAST_BORROW         8 (warnings)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               LOAD_CONST              16 ('ok')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              12 ('warning')
      L10:     STORE_FAST               9 (status)

227            LOAD_GLOBAL             17 (_envelope + NULL)

228            LOAD_CONST              17 ('slack_webhook')

229            LOAD_FAST_BORROW         9 (status)

230            LOAD_FAST_BORROW         7 (summary)

231            LOAD_FAST_BORROW         8 (warnings)

227            LOAD_CONST              18 (('probe_type', 'status', 'summary', 'warnings'))
               CALL_KW                  4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\connectivity_probes.py", line 235>:
235           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object probe_calcom_configuration at 0x0000018C17ED9FB0, file "app\services\operator\connectivity_probes.py", line 235>:
235            RESUME                   0

239            LOAD_GLOBAL              1 (_settings_safe + NULL)
               CALL                     0
               STORE_FAST               1 (s)

241            LOAD_CONST               1 ('calcom_api_key_present')
               LOAD_GLOBAL              3 (_has_str + NULL)
               LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L1)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               2 ('CALCOM_API_KEY')
               LOAD_CONST               3 ('')
               CALL                     3
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_CONST               4 (None)
       L2:     CALL                     1

242            LOAD_CONST               5 ('calcom_event_type_present')
               LOAD_GLOBAL              7 (_has_int + NULL)
               LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L3)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               6 ('CALCOM_EVENT_TYPE_ID')
               LOAD_SMALL_INT           0
               CALL                     3
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               4 (None)
       L4:     CALL                     1

243            LOAD_CONST               7 ('calcom_api_key_fingerprint')
               LOAD_GLOBAL              9 (_prefix_fingerprint + NULL)

244            LOAD_FAST_BORROW         1 (s)
               TO_BOOL
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN
               LOAD_GLOBAL              5 (getattr + NULL)
               LOAD_FAST_BORROW         1 (s)
               LOAD_CONST               2 ('CALCOM_API_KEY')
               LOAD_CONST               3 ('')
               CALL                     3
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               4 (None)

243    L6:     CALL                     1

246            LOAD_CONST               8 ('brokerage_timezone_present')
               LOAD_CONST               9 (False)

240            BUILD_MAP                4
               STORE_FAST               2 (summary)

248            LOAD_GLOBAL             11 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL             12 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       30 (to L7)
               NOT_TAKEN

249            LOAD_GLOBAL              3 (_has_str + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST              10 ('timezone')
               CALL                     1
               CALL                     1
               LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               8 ('brokerage_timezone_present')
               STORE_SUBSCR

251    L7:     BUILD_LIST               0
               STORE_FAST               3 (warnings)

252            LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               1 ('calcom_api_key_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L8)
               NOT_TAKEN

253            LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST              11 ('calcom_api_key_missing')
               CALL                     1
               POP_TOP

254    L8:     LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               5 ('calcom_event_type_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L9)
               NOT_TAKEN

255            LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST              12 ('calcom_event_type_missing')
               CALL                     1
               POP_TOP

256    L9:     LOAD_FAST_BORROW         2 (summary)
               LOAD_CONST               8 ('brokerage_timezone_present')
               BINARY_OP               26 ([])
               TO_BOOL
               POP_JUMP_IF_TRUE        18 (to L10)
               NOT_TAKEN

257            LOAD_FAST_BORROW         3 (warnings)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST              13 ('brokerage_timezone_missing')
               CALL                     1
               POP_TOP

259   L10:     LOAD_FAST_BORROW         3 (warnings)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               LOAD_CONST              14 ('ok')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              15 ('warning')
      L12:     STORE_FAST               4 (status)

260            LOAD_GLOBAL             19 (_envelope + NULL)

261            LOAD_CONST              16 ('calcom')

262            LOAD_FAST_BORROW         4 (status)

263            LOAD_FAST_BORROW         2 (summary)

264            LOAD_FAST_BORROW         3 (warnings)

260            LOAD_CONST              17 (('probe_type', 'status', 'summary', 'warnings'))
               CALL_KW                  4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\connectivity_probes.py", line 268>:
268           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object probe_worker_visibility at 0x0000018C17EF9A30, file "app\services\operator\connectivity_probes.py", line 268>:
 268            RESUME                   0

 273            LOAD_CONST               1 ('worker_enable_env_set')
                LOAD_GLOBAL              0 (os)
                LOAD_ATTR                2 (environ)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('PENDING_CALLS_WORKER_ENABLED')
                CALL                     1
                LOAD_CONST               3 (None)
                IS_OP                    1 (is not)

 274            LOAD_CONST               4 ('worker_enable_strict')
                LOAD_GLOBAL              0 (os)
                LOAD_ATTR                2 (environ)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               2 ('PENDING_CALLS_WORKER_ENABLED')
                CALL                     1
                LOAD_CONST               5 ('true')
                COMPARE_OP              72 (==)

 275            LOAD_CONST               6 ('heartbeat_store_reachable')
                LOAD_CONST               7 (False)

 276            LOAD_CONST               8 ('heartbeat_row_count')
                LOAD_SMALL_INT           0

 277            LOAD_CONST               9 ('oldest_heartbeat_age_seconds')
                LOAD_CONST               3 (None)

 272            BUILD_MAP                5
                STORE_FAST               0 (summary)

 279            BUILD_LIST               0
                STORE_FAST               1 (warnings)

 280            NOP

 281    L1:     LOAD_SMALL_INT           0
                LOAD_CONST              10 (('heartbeat_monitor_report',))
                IMPORT_NAME              3 (app.services.worker.heartbeat_monitor)
                IMPORT_FROM              4 (heartbeat_monitor_report)
                STORE_FAST               2 (heartbeat_monitor_report)
                POP_TOP

 282            LOAD_FAST_BORROW         2 (heartbeat_monitor_report)
                PUSH_NULL
                LOAD_SMALL_INT          50
                LOAD_CONST              11 (('limit',))
                CALL_KW                  1
                STORE_FAST               3 (report)

 283            LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              13 ('ok')
                COMPARE_OP              72 (==)
                LOAD_FAST_BORROW         0 (summary)
                LOAD_CONST               6 ('heartbeat_store_reachable')
                STORE_SUBSCR

 284            LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              14 ('total')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_SMALL_INT           0
        L4:     CALL                     1
                LOAD_FAST_BORROW         0 (summary)
                LOAD_CONST               8 ('heartbeat_row_count')
                STORE_SUBSCR

 285            LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              15 ('oldest_age_seconds')
                CALL                     1
                LOAD_FAST_BORROW         0 (summary)
                LOAD_CONST               9 ('oldest_heartbeat_age_seconds')
                STORE_SUBSCR

 286            LOAD_FAST_BORROW         3 (report)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              12 ('status')
                CALL                     1
                LOAD_CONST              13 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN

 287            LOAD_FAST_BORROW         1 (warnings)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_CONST              16 ('heartbeat_store_unavailable')
                CALL                     1
                POP_TOP

 294    L5:     LOAD_FAST                0 (summary)
                LOAD_CONST               1 ('worker_enable_env_set')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L6)
                NOT_TAKEN

 295            LOAD_FAST                0 (summary)
                LOAD_CONST               4 ('worker_enable_strict')
                BINARY_OP               26 ([])
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L6)
                NOT_TAKEN

 297            LOAD_FAST                1 (warnings)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_CONST              19 ('worker_enable_set_non_strict')
                CALL                     1
                POP_TOP

 298    L6:     LOAD_FAST                1 (warnings)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                LOAD_CONST              13 ('ok')
                JUMP_FORWARD             1 (to L8)
        L7:     LOAD_CONST              20 ('warning')
        L8:     STORE_FAST               5 (status)

 299            LOAD_GLOBAL             25 (_envelope + NULL)

 300            LOAD_CONST              21 ('worker_visibility')

 301            LOAD_FAST                5 (status)

 302            LOAD_FAST                0 (summary)

 303            LOAD_FAST                1 (warnings)

 299            LOAD_CONST              22 (('probe_type', 'status', 'summary', 'warnings'))
                CALL_KW                  4
                RETURN_VALUE

  --    L9:     PUSH_EXC_INFO

 288            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       93 (to L13)
                NOT_TAKEN
                STORE_FAST               4 (e)

 289   L10:     LOAD_GLOBAL             16 (logger)
                LOAD_ATTR               19 (warning + NULL|self)

 290            LOAD_CONST              17 ('probe_worker_visibility error type=')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 289            CALL                     1
                POP_TOP

 292            LOAD_FAST                1 (warnings)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_CONST              18 ('heartbeat_probe_error:')
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
       L11:     POP_EXCEPT
                LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                JUMP_BACKWARD_NO_INTERRUPT 172 (to L5)

  --   L12:     LOAD_CONST               3 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 288   L13:     RERAISE                  0

  --   L14:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L9 [0]
  L3 to L5 -> L9 [0]
  L9 to L10 -> L14 [1] lasti
  L10 to L11 -> L12 [1] lasti
  L12 to L14 -> L14 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\operator\connectivity_probes.py", line 307>:
307           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object probe_encryption_posture at 0x0000018C17EDA2D0, file "app\services\operator\connectivity_probes.py", line 307>:
 307            RESUME                   0

 311            LOAD_GLOBAL              1 (_has_str + NULL)
                LOAD_GLOBAL              2 (os)
                LOAD_ATTR                4 (environ)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               1 ('PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID')
                CALL                     1
                CALL                     1
                STORE_FAST               0 (active_kid_present)

 315            LOAD_GLOBAL              2 (os)
                LOAD_ATTR                4 (environ)
                LOAD_ATTR                9 (keys + NULL|self)
                CALL                     0
                GET_ITER

 314            LOAD_FAST_AND_CLEAR      1 (k)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 315    L2:     FOR_ITER                30 (to L5)
                STORE_FAST               1 (k)

 316            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR               11 (startswith + NULL|self)
                LOAD_CONST               2 ('PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_')
                CALL                     1
                TO_BOOL

 315    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           28 (to L2)
        L4:     LOAD_FAST_BORROW         1 (k)
                LIST_APPEND              2
                JUMP_BACKWARD           32 (to L2)
        L5:     END_FOR
                POP_ITER

 314    L6:     STORE_FAST               2 (matching_keys)
                STORE_FAST               1 (k)

 319            LOAD_CONST               3 ('active_kid_set')
                LOAD_FAST                0 (active_kid_present)

 320            LOAD_CONST               4 ('kid_envelope_count')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         2 (matching_keys)
                CALL                     1

 321            LOAD_CONST               5 ('encryption_enabled')
                LOAD_FAST                0 (active_kid_present)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       15 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         2 (matching_keys)
                CALL                     1
                LOAD_SMALL_INT           0
                COMPARE_OP             132 (>)

 318    L7:     BUILD_MAP                3
                STORE_FAST               3 (summary)

 323            BUILD_LIST               0
                STORE_FAST               4 (warnings)

 324            LOAD_FAST_BORROW         0 (active_kid_present)
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L8)
                NOT_TAKEN

 325            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST               6 ('email_forwarder_secret_unencrypted')
                CALL                     1
                POP_TOP

 326    L8:     LOAD_FAST_BORROW         0 (active_kid_present)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         2 (matching_keys)
                CALL                     1
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       18 (to L9)
                NOT_TAKEN

 327            LOAD_FAST_BORROW         4 (warnings)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_CONST               7 ('email_forwarder_kid_set_without_key')
                CALL                     1
                POP_TOP

 328    L9:     LOAD_FAST_BORROW         4 (warnings)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                LOAD_CONST               8 ('ok')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               9 ('warning')
       L11:     STORE_FAST               5 (status)

 329            LOAD_GLOBAL             17 (_envelope + NULL)

 330            LOAD_CONST              10 ('encryption_posture')

 331            LOAD_FAST_BORROW         5 (status)

 332            LOAD_FAST_BORROW         3 (summary)

 333            LOAD_FAST_BORROW         4 (warnings)

 329            LOAD_CONST              11 (('probe_type', 'status', 'summary', 'warnings'))
                CALL_KW                  4
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 314            SWAP                     2
                STORE_FAST               1 (k)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L12 [2]
  L4 to L6 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\operator\connectivity_probes.py", line 337>:
337           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object run_all_probes at 0x0000018C17D8C5C0, file "app\services\operator\connectivity_probes.py", line 337>:
337           RESUME                   0

341           LOAD_GLOBAL              1 (probe_twilio_configuration + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_CONST               1 (('brokerage',))
              CALL_KW                  1

342           LOAD_GLOBAL              3 (probe_slack_webhook + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_CONST               1 (('brokerage',))
              CALL_KW                  1

343           LOAD_GLOBAL              5 (probe_calcom_configuration + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_CONST               1 (('brokerage',))
              CALL_KW                  1

344           LOAD_GLOBAL              7 (probe_worker_visibility + NULL)
              CALL                     0

345           LOAD_GLOBAL              9 (probe_encryption_posture + NULL)
              CALL                     0

340           BUILD_LIST               5
              STORE_FAST               1 (probes)

347           LOAD_GLOBAL             11 (sum + NULL)
              LOAD_CONST               2 (<code object <genexpr> at 0x0000018C180531B0, file "app\services\operator\connectivity_probes.py", line 347>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (probes)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               2 (ok)

348           LOAD_GLOBAL             11 (sum + NULL)
              LOAD_CONST               3 (<code object <genexpr> at 0x0000018C180532D0, file "app\services\operator\connectivity_probes.py", line 348>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (probes)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               3 (warn)

349           LOAD_GLOBAL             11 (sum + NULL)
              LOAD_CONST               4 (<code object <genexpr> at 0x0000018C180533F0, file "app\services\operator\connectivity_probes.py", line 349>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (probes)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               4 (fail)

350           LOAD_GLOBAL             11 (sum + NULL)
              LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18053990, file "app\services\operator\connectivity_probes.py", line 350>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (probes)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               5 (skip)

351           LOAD_CONST               6 ('ok')
              STORE_FAST               6 (overall)

352           LOAD_FAST_BORROW         4 (fail)
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L1)
              NOT_TAKEN

353           LOAD_CONST               7 ('failed')
              STORE_FAST               6 (overall)
              JUMP_FORWARD            28 (to L3)

354   L1:     LOAD_FAST_BORROW         3 (warn)
              TO_BOOL
              POP_JUMP_IF_FALSE        4 (to L2)
              NOT_TAKEN

355           LOAD_CONST               8 ('warning')
              STORE_FAST               6 (overall)
              JUMP_FORWARD            17 (to L3)

356   L2:     LOAD_FAST_BORROW         5 (skip)
              TO_BOOL
              POP_JUMP_IF_FALSE       10 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (ok)
              LOAD_SMALL_INT           0
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

357           LOAD_CONST               9 ('skipped')
              STORE_FAST               6 (overall)

359   L3:     LOAD_CONST              10 ('status')
              LOAD_FAST_BORROW         6 (overall)

360           LOAD_CONST              11 ('probe_count')
              LOAD_GLOBAL             13 (len + NULL)
              LOAD_FAST_BORROW         1 (probes)
              CALL                     1

361           LOAD_CONST              12 ('ok_count')
              LOAD_FAST_BORROW         2 (ok)

362           LOAD_CONST              13 ('warning_count')
              LOAD_FAST_BORROW         3 (warn)

363           LOAD_CONST              14 ('failed_count')
              LOAD_FAST_BORROW         4 (fail)

364           LOAD_CONST              15 ('skipped_count')
              LOAD_FAST_BORROW         5 (skip)

365           LOAD_CONST              16 ('probes')
              LOAD_FAST_BORROW         1 (probes)

366           LOAD_CONST              17 ('generated_at')
              LOAD_GLOBAL             15 (_now_iso + NULL)
              CALL                     0

358           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "app\services\operator\connectivity_probes.py", line 347>:
 347           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('ok')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "app\services\operator\connectivity_probes.py", line 348>:
 348           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('warning')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "app\services\operator\connectivity_probes.py", line 349>:
 349           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('failed')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "app\services\operator\connectivity_probes.py", line 350>:
 350           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('skipped')
               COMPARE_OP              88 (bool(==))
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           18 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti
```
