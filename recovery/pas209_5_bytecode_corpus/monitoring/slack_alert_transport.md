# monitoring/slack_alert_transport

- **pyc:** `app\services\monitoring\__pycache__\slack_alert_transport.cpython-314.pyc`
- **expected source path (absent):** `app\services\monitoring/slack_alert_transport.py`
- **co_filename (from bytecode):** `app\services\monitoring\slack_alert_transport.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** monitoring

## Module docstring

```
PAS170 — Slack alert transport (optional, structural).

Wires the PAS143F2 monitoring dispatcher to a Slack webhook
URL so the existing Alert pipeline finally has a delivery
destination. Closes PAS-AUDIT-01 §C / Production-Critical
Blocker #4 — "alerts are built but never delivered".

Hard doctrine:

* **Structural payloads only.** Slack messages contain only
  the allow-listed alert fields (id, category, severity,
  title, description). Title + description go through the
  PAS143F2 PII redactor before they hit the wire. Metadata
  is NOT sent — it may carry tokens we haven't audited for
  every alert type.
* **Webhook URL resolution is bounded.** PAS170 reads the
  Slack webhook from (in order): the supplied
  ``webhook_url`` kwarg, the brokerage row's
  ``alert_slack_webhook_url`` field (falling back to
  ``slack_webhook_url`` — the call-summary channel —
  intentionally NOT used by default to keep alert noise
  off the sales channel), or the env var
  ``PAS_ALERT_SLACK_WEBHOOK_URL`` (for cross-tenant
  operator alerts).
* **Failure to send NEVER raises.** A failed Slack POST
  surfaces as a structural envelope; the calling code path
  must not crash because Slack is down.
* **Disabled by default.** No alert leaves the process
  unless ``send_alert_to_slack(...)`` is explicitly invoked
  by an operator or by the PAS170 readiness scaffolding.
  There is no startup hook that wires the dispatcher to
  Slack automatically.
* **No secrets in the payload.** Signature, dedupe key,
  encrypted secret, plaintext secret, raw transcript, raw
  email body, phone, email, name — none of these are
  surfaced.
```

## Imports

`Alert`, `Any`, `Dict`, `List`, `Optional`, `__future__`, `alert_to_safe_dict`, `annotations`, `app.services.monitoring.contracts`, `app.services.monitoring.dispatcher`, `datetime`, `httpx`, `logging`, `os`, `threading`, `time`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_alert_id_allowed`, `_build_slack_payload`, `_mark_sent`, `_rate_limited`, `_resolve_webhook_url`, `_scan_body_for_forbidden`, `detect_provider_failure_storm`, `emit_pilot_fallback_notice`, `emit_worker_liveness_heartbeat`, `reset_pilot_alert_rate_limit_for_tests`, `send_alert_to_slack`, `send_alerts_to_slack`, `send_pilot_alert_to_slack`

## Env-key candidates

`CRITICAL`, `HIGH`, `INFO`, `INGESTION`, `LOW`, `MEDIUM`, `PAS_ALERT_SLACK_WEBHOOK_URL`, `RUNTIME`

## String constants (redacted where noted)

- '\nPAS170 — Slack alert transport (optional, structural).\n\nWires the PAS143F2 monitoring dispatcher to a Slack webhook\nURL so the existing Alert pipeline finally has a delivery\ndestination. Closes PAS-AUDIT-01 §C / Production-Critical\nBlocker #4 — "alerts are built but never delivered".\n\nHard doctrine:\n\n* **Structural payloads only.** Slack messages contain only\n  the allow-listed alert fields (id, category, severity,\n  title, description). Title + description go through the\n  PAS143F2 PII redactor before they hit the wire. Metadata\n  is NOT sent — it may carry tokens we haven\'t audited for\n  every alert type.\n* **Webhook URL resolution is bounded.** PAS170 reads the\n  Slack webhook from (in order): the supplied\n  ``webhook_url`` kwarg, the brokerage row\'s\n  ``alert_slack_webhook_url`` field (falling back to\n  ``slack_webhook_url`` — the call-summary channel —\n  intentionally NOT used by default to keep alert noise\n  off the sales channel), or the env var\n  ``PAS_ALERT_SLACK_WEBHOOK_URL`` (for cross-tenant\n  operator alerts).\n* **Failure to send NEVER raises.** A failed Slack POST\n  surfaces as a structural envelope; the calling code path\n  must not crash because Slack is down.\n* **Disabled by default.** No alert leaves the process\n  unless ``send_alert_to_slack(...)`` is explicitly invoked\n  by an operator or by the PAS170 readiness scaffolding.\n  There is no startup hook that wires the dispatcher to\n  Slack automatically.\n* **No secrets in the payload.** Signature, dedupe key,\n  encrypted secret, plaintext secret, raw transcript, raw\n  email body, phone, email, name — none of these are\n  surfaced.\n'
- 'pas.monitoring.slack_alert_transport'
- 'PAS_ALERT_SLACK_WEBHOOK_URL'
- 'brokerage_id'
- 'brokerage'
- 'webhook_url'
- 'include_metadata'
- 'window_seconds'
- 'threshold'
- 'now'
- 'Dict[str, float]'
- '_PILOT_ALERT_LAST_SENT'
- 'dedupe_window'
- 'worker_id'
- 'last_seen_iso'
- 'threshold_secs'
- 'Optional[str]'
- 'Any'
- 'return'
- 'Resolve the destination webhook in bounded precedence.\n\n1. Explicit ``webhook_url`` kwarg.\n2. ``brokerage["alert_slack_webhook_url"]`` (a separate\n   channel from the call-summary webhook so alerts don\'t\n   pollute the sales channel).\n3. ``PAS_ALERT_SLACK_WEBHOOK_URL`` env var (cross-tenant\n   operator channel).\n4. None → caller emits ``alert.slack.failed`` with\n   ``slack_webhook_not_configured``.\n\nNote: PAS170 deliberately does NOT fall back to the\nbrokerage\'s ``slack_webhook_url`` (the call-summary\nchannel). Mixing alert noise into the sales channel is\noperationally wrong; operators must opt in via the\nseparate ``alert_slack_webhook_url`` field.\n'
- 'alert_slack_webhook_url'
- 'safe_alert'
- 'Dict[str, Any]'
- 'bool'
- 'Build the structural Slack Block Kit payload from a\nredacted alert dict. NEVER echoes a forbidden key.'
- 'severity'
- 'INFO'
- 'category'
- 'RUNTIME'
- 'title'
- 'PAS alert'
- 'description'
- 'CRITICAL'
- 'HIGH'
- 'MEDIUM'
- 'LOW'
- 'type'
- 'header'
- 'text'
- 'plain_text'
- ' PAS alert: '
- ' / '
- 'section'
- 'mrkdwn'
- 'metadata'
- 'PAS alert: '
- 'blocks'
- '• *'
- '*: `'
- 'alert'
- 'Send a single PAS143F2 Alert (or dict) to Slack.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":     "sent" | "skipped" | "failed",\n      "warnings":   [<structural tokens>],\n      "error_code": None | "<structural token>",\n    }\n\nBehaviour:\n\n* Alert is normalised + PII-redacted via the existing\n  ``alert_to_safe_dict`` dispatcher helper.\n* Empty alert (bad input) → ``status="skipped"``,\n  warning ``alert_input_invalid``.\n* No webhook resolvable → ``status="skipped"``,\n  warning ``slack_webhook_not_configured``.\n* HTTP error → ``status="failed"``, structural\n  ``error_code`` (e.g. ``http_500``,\n  ``transport_exception:<Type>``). The error message is\n  NEVER raw exception text.\n* Successful POST → ``status="sent"``.\n\nNEVER raises.\n'
- 'status'
- 'skipped'
- 'warnings'
- 'alert_input_invalid'
- 'error_code'
- 'slack_webhook_not_configured'
- 'failed'
- 'httpx_unavailable'
- 'send_alert_to_slack transport error type='
- 'transport_exception:'
- 'sent'
- 'http_'
- 'alerts'
- 'List[Any]'
- 'List[Dict[str, Any]]'
- 'Convenience: send each alert sequentially. NEVER\nraises. Returns one envelope per input alert.\n\nFailure on any single alert does NOT stop the loop —\nsubsequent alerts are attempted independently. The\noperator scripts treat the per-alert envelopes as\nstructural counters.'
- 'send_alerts_to_slack per-item error type='
- 'loop_exception:'
- 'events'
- 'int'
- 'Detect a "provider failure storm" from an in-memory list\nof recent event dicts.\n\nEach event is expected to have at least ``event_type``,\n``payload`` (optional dict with ``provider`` key), and\n``ts`` (ISO-8601 UTC string). Events outside the window\nare ignored.\n\nReturns a structural envelope::\n\n    {\n      "detected": bool,\n      "count":    int,\n      "by_provider": {provider: count, ...},\n      "window_seconds": int,\n      "threshold":      int,\n      "warnings": [],\n      "error_code": None,\n    }\n\nNEVER raises. NEVER echoes raw event payload contents\nbeyond the structural ``provider`` token.\n\nThe caller decides whether to construct an Alert + hand it\nto ``send_alert_to_slack``. PAS170 ships the detector +\nthe transport; wiring them together is the operator\nscript\'s job (see ``scripts/pas170_demo_brokerage_smoke_\nplan.py``).\n'
- 'event_type'
- 'provider.failed'
- 'created_at'
- '+00:00'
- 'payload'
- 'provider'
- 'unknown'
- 'detected'
- 'count'
- 'by_provider'
- 'alert_id'
- 'str'
- 'window'
- 'Return True if ``alert_id`` was successfully sent within\nthe rate-limit window. NEVER raises.'
- 'None'
- 'body'
- 'List[str]'
- 'Walk the outbound body recursively; return any forbidden\ntokens found (in dict keys or string values). NEVER raises.'
- 'obj'
- 'Test-only helper to flush the rate-limit ledger.'
- 'PAS171 outbound-only pilot Slack transport.\n\nWraps :func:`send_alert_to_slack` with:\n\n* **Closed alert-id allow-list.** Refuses alerts whose\n  ``id`` does not start with one of\n  ``_PILOT_ALERT_ID_ALLOWED_PREFIXES``.\n* **Per-process rate-limit dedupe.** The same ``alert.id``\n  is not re-sent within ``dedupe_window`` of a successful\n  prior send. Defaults to 60 seconds.\n* **Extra forbidden-token body scan.** Belt-and-braces\n  check on the final outbound JSON before transport.\n* **Closed-shape envelope** with the structural status:\n  ``"sent" | "refused" | "rate_limited" | "skipped" |\n  "failed"``.\n\nNEVER raises. NEVER echoes the webhook URL.\n'
- 'refused'
- 'pilot_alert_id_not_in_allow_list'
- 'rate_limited'
- 'pilot_alert_rate_limited'
- 'pilot_body_forbidden_token:'
- 'pilot_body_forbidden_token'
- 'Build a ``worker.liveness.missing`` alert and send it via\nthe pilot transport. Operator-callable; not auto-fired.\n\nThe caller decides what "last seen" means — typically a\npoll against the durable ``pas_pending_calls`` table\'s\n``locked_at`` MAX, or a dedicated heartbeat table the\noperator wires up. PAS171 does NOT introduce a heartbeat\ntable — that is PAS172 work.\n\nReturns the same closed-shape envelope as\n:func:`send_pilot_alert_to_slack`. NEVER raises.\n'
- 'worker_liveness_within_threshold'
- 'worker.liveness.missing:'
- 'Worker liveness missing'
- "Pending-call worker '"
- "' has not heartbeated within "
- 's. Operator should inspect the worker process.'
- 'app.services.monitoring.slack_alert_transport'
- 'age_seconds'
- 'subsystem'
- 'Notify the pilot channel that PAS has fallen back from a\ndurable PAS171 store to its PAS170 process-local fallback.\nOperator-callable; not auto-fired. NEVER raises.\n\nAllowed ``subsystem`` values:\n\n* ``"dedupe"`` → ``external_pilot.dedupe_fallback`` alert.\n* ``"callback"`` → ``external_pilot.callback_schedule_fallback`` alert.\n\nAny other value returns ``status="refused"``.\n'
- 'dedupe'
- 'external_pilot.dedupe_fallback'
- 'Pending-call dedupe fell back to process-local'
- 'PAS171 durable pending-call dedupe is unavailable. PAS is operating on the PAS170 process-local registry. Operator should restore the durable store before expanding pilot exposure.'
- 'callback'
- 'external_pilot.callback_schedule_fallback'
- 'Callback schedule fell back to process-local'
- 'PAS171 durable callback schedule is unavailable. PAS is operating on the PAS170 process-local registry. Operator should restore the durable store before expanding pilot exposure.'
- 'pilot_fallback_subsystem_unknown'
- 'global'
- 'INGESTION'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS170 — Slack alert transport (optional, structural).\n\nWires the PAS143F2 monitoring dispatcher to a Slack webhook\nURL so the existing Alert pipeline finally has a delivery\ndestination. Closes PAS-AUDIT-01 §C / Production-Critical\nBlocker #4 — "alerts are built but never delivered".\n\nHard doctrine:\n\n* **Structural payloads only.** Slack messages contain only\n  the allow-listed alert fields (id, category, severity,\n  title, description). Title + description go through the\n  PAS143F2 PII redactor before they hit the wire. Metadata\n  is NOT sent — it may carry tokens we haven\'t audited for\n  every alert type.\n* **Webhook URL resolution is bounded.** PAS170 reads the\n  Slack webhook from (in order): the supplied\n  ``webhook_url`` kwarg, the brokerage row\'s\n  ``alert_slack_webhook_url`` field (falling back to\n  ``slack_webhook_url`` — the call-summary channel —\n  intentionally NOT used by default to keep alert noise\n  off the sales channel), or the env var\n  ``PAS_ALERT_SLACK_WEBHOOK_URL`` (for cross-tenant\n  operator alerts).\n* **Failure to send NEVER raises.** A failed Slack POST\n  surfaces as a structural envelope; the calling code path\n  must not crash because Slack is down.\n* **Disabled by default.** No alert leaves the process\n  unless ``send_alert_to_slack(...)`` is explicitly invoked\n  by an operator or by the PAS170 readiness scaffolding.\n  There is no startup hook that wires the dispatcher to\n  Slack automatically.\n* **No secrets in the payload.** Signature, dedupe key,\n  encrypted secret, plaintext secret, raw transcript, raw\n  email body, phone, email, name — none of these are\n  surfaced.\n')
               STORE_NAME               1 (__doc__)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
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

  46           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('alert_to_safe_dict',))
               IMPORT_NAME             11 (app.services.monitoring.dispatcher)
               IMPORT_FROM             12 (alert_to_safe_dict)
               STORE_NAME              12 (alert_to_safe_dict)
               POP_TOP

  47           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Alert',))
               IMPORT_NAME             13 (app.services.monitoring.contracts)
               IMPORT_FROM             14 (Alert)
               STORE_NAME              14 (Alert)
               POP_TOP

  50           LOAD_NAME                4 (logging)
               LOAD_ATTR               30 (getLogger)
               PUSH_NULL
               LOAD_CONST               6 ('pas.monitoring.slack_alert_transport')
               CALL                     1
               STORE_NAME              16 (logger)

  57           LOAD_CONST               7 ('PAS_ALERT_SLACK_WEBHOOK_URL')
               STORE_NAME              17 (_ENV_OPERATOR_WEBHOOK)

  63           LOAD_CONST              48 (('id', 'category', 'severity', 'title', 'description', 'source', 'created_at'))
               STORE_NAME              18 (_ALERT_PAYLOAD_ALLOWED)

  78           LOAD_CONST              49 (('brokerage_id', 'source', 'status', 'count', 'age_seconds', 'warning_count', 'error_code', 'provider', 'severity', 'dry_run', 'duplicate', 'recovered_count'))
               STORE_NAME              19 (_METADATA_ALLOWED)

  98           LOAD_CONST               9 ('brokerage')

 101           LOAD_CONST               2 (None)

  98           BUILD_MAP                1
               LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\monitoring\slack_alert_transport.py", line 98>)
               MAKE_FUNCTION
               LOAD_CONST              11 (<code object _resolve_webhook_url at 0x0000018C17CD4970, file "app\services\monitoring\slack_alert_transport.py", line 98>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              20 (_resolve_webhook_url)

 136           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18024E30, file "app\services\monitoring\slack_alert_transport.py", line 136>)
               MAKE_FUNCTION
               LOAD_CONST              13 (<code object _build_slack_payload at 0x0000018C17EF9A30, file "app\services\monitoring\slack_alert_transport.py", line 136>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              21 (_build_slack_payload)

 201           LOAD_CONST              14 ('webhook_url')

 204           LOAD_CONST               2 (None)

 201           LOAD_CONST               9 ('brokerage')

 205           LOAD_CONST               2 (None)

 201           LOAD_CONST              15 ('include_metadata')

 206           LOAD_CONST              16 (False)

 201           BUILD_MAP                3
               LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\monitoring\slack_alert_transport.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object send_alert_to_slack at 0x0000018C17ED2550, file "app\services\monitoring\slack_alert_transport.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              22 (send_alert_to_slack)

 300           LOAD_CONST              14 ('webhook_url')

 303           LOAD_CONST               2 (None)

 300           LOAD_CONST               9 ('brokerage')

 304           LOAD_CONST               2 (None)

 300           LOAD_CONST              15 ('include_metadata')

 305           LOAD_CONST              16 (False)

 300           BUILD_MAP                3
               LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18025D30, file "app\services\monitoring\slack_alert_transport.py", line 300>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object send_alerts_to_slack at 0x0000018C17E94610, file "app\services\monitoring\slack_alert_transport.py", line 300>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              23 (send_alerts_to_slack)

 345           LOAD_CONST              50 (300)
               STORE_NAME              24 (_DEFAULT_STORM_WINDOW_SECONDS)

 346           LOAD_SMALL_INT           3
               STORE_NAME              25 (_DEFAULT_STORM_THRESHOLD)

 349           LOAD_CONST              21 ('window_seconds')

 352           LOAD_NAME               24 (_DEFAULT_STORM_WINDOW_SECONDS)

 349           LOAD_CONST              22 ('threshold')

 353           LOAD_NAME               25 (_DEFAULT_STORM_THRESHOLD)

 349           LOAD_CONST              23 ('now')

 354           LOAD_CONST               2 (None)

 349           BUILD_MAP                3
               LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\monitoring\slack_alert_transport.py", line 349>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object detect_provider_failure_storm at 0x0000018C177C5700, file "app\services\monitoring\slack_alert_transport.py", line 349>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              26 (detect_provider_failure_storm)

 484           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             27 (threading)
               STORE_NAME              27 (threading)

 485           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             28 (time)
               STORE_NAME              29 (_time)

 492           LOAD_CONST              51 (('worker.liveness.missing:', 'provider.failure_storm.detected:', 'pending_call.stale_detected:', 'email.forwarder.secret.decrypt_failed:', 'alert.slack.failed:', 'external_pilot.heartbeat:', 'external_pilot.dedupe_fallback:', 'external_pilot.callback_schedule_fallback:', 'audit.chain.broken:'))
               STORE_NAME              30 (_PILOT_ALERT_ID_ALLOWED_PREFIXES)

 510           LOAD_SMALL_INT          60
               STORE_NAME              31 (_PILOT_ALERT_DEDUPE_SECONDS)

 517           BUILD_MAP                0
               STORE_NAME              32 (_PILOT_ALERT_LAST_SENT)
               LOAD_CONST              26 ('Dict[str, float]')
               LOAD_NAME               33 (__annotations__)
               LOAD_CONST              27 ('_PILOT_ALERT_LAST_SENT')
               STORE_SUBSCR

 518           LOAD_NAME               27 (threading)
               LOAD_ATTR               68 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              35 (_PILOT_ALERT_LOCK)

 526           LOAD_CONST              52 (('raw_payload', 'raw_email', 'raw_body', 'transcript', 'summary_text', 'secret', 'dedupe_key', 'x_api_key', 'x-api-key', 'service_role'))
               STORE_NAME              36 (_PILOT_FORBIDDEN_BODY_TOKENS)

 535           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\monitoring\slack_alert_transport.py", line 535>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _alert_id_allowed at 0x0000018C179C3A50, file "app\services\monitoring\slack_alert_transport.py", line 535>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_alert_id_allowed)

 544           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18025C30, file "app\services\monitoring\slack_alert_transport.py", line 544>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _rate_limited at 0x0000018C17FED830, file "app\services\monitoring\slack_alert_transport.py", line 544>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_rate_limited)

 558           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\slack_alert_transport.py", line 558>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _mark_sent at 0x0000018C17FA92F0, file "app\services\monitoring\slack_alert_transport.py", line 558>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_mark_sent)

 566           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\monitoring\slack_alert_transport.py", line 566>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _scan_body_for_forbidden at 0x0000018C180C4470, file "app\services\monitoring\slack_alert_transport.py", line 566>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_scan_body_for_forbidden)

 594           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\monitoring\slack_alert_transport.py", line 594>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object reset_pilot_alert_rate_limit_for_tests at 0x0000018C18010B30, file "app\services\monitoring\slack_alert_transport.py", line 594>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (reset_pilot_alert_rate_limit_for_tests)

 600           LOAD_CONST              14 ('webhook_url')

 603           LOAD_CONST               2 (None)

 600           LOAD_CONST               9 ('brokerage')

 604           LOAD_CONST               2 (None)

 600           LOAD_CONST              15 ('include_metadata')

 605           LOAD_CONST              16 (False)

 600           LOAD_CONST              38 ('dedupe_window')

 606           LOAD_NAME               31 (_PILOT_ALERT_DEDUPE_SECONDS)

 600           BUILD_MAP                4
               LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18024930, file "app\services\monitoring\slack_alert_transport.py", line 600>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object send_pilot_alert_to_slack at 0x0000018C17D8BF50, file "app\services\monitoring\slack_alert_transport.py", line 600>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (send_pilot_alert_to_slack)

 684           LOAD_CONST              41 ('worker_id')

 686           LOAD_CONST               2 (None)

 684           LOAD_CONST              42 ('last_seen_iso')

 687           LOAD_CONST               2 (None)

 684           LOAD_CONST              43 ('threshold_secs')

 688           LOAD_CONST              50 (300)

 684           LOAD_CONST              14 ('webhook_url')

 689           LOAD_CONST               2 (None)

 684           LOAD_CONST               9 ('brokerage')

 690           LOAD_CONST               2 (None)

 684           LOAD_CONST              23 ('now')

 691           LOAD_CONST               2 (None)

 684           BUILD_MAP                6
               LOAD_CONST              44 (<code object __annotate__ at 0x0000018C180C4140, file "app\services\monitoring\slack_alert_transport.py", line 684>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object emit_worker_liveness_heartbeat at 0x0000018C17D7FD70, file "app\services\monitoring\slack_alert_transport.py", line 684>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (emit_worker_liveness_heartbeat)

 764           LOAD_CONST               8 ('brokerage_id')

 767           LOAD_CONST               2 (None)

 764           LOAD_CONST              14 ('webhook_url')

 768           LOAD_CONST               2 (None)

 764           LOAD_CONST               9 ('brokerage')

 769           LOAD_CONST               2 (None)

 764           BUILD_MAP                3
               LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18025530, file "app\services\monitoring\slack_alert_transport.py", line 764>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object emit_pilot_fallback_notice at 0x0000018C17CC2460, file "app\services\monitoring\slack_alert_transport.py", line 764>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              44 (emit_pilot_fallback_notice)

 824           BUILD_LIST               0
               LOAD_CONST              53 (('send_alert_to_slack', 'send_alerts_to_slack', 'detect_provider_failure_storm', 'send_pilot_alert_to_slack', 'emit_worker_liveness_heartbeat', 'emit_pilot_fallback_notice', 'reset_pilot_alert_rate_limit_for_tests'))
               LIST_EXTEND              1
               STORE_NAME              45 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\monitoring\slack_alert_transport.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('webhook_url')

100           LOAD_CONST               2 ('Optional[str]')

 98           LOAD_CONST               3 ('brokerage')

101           LOAD_CONST               4 ('Any')

 98           LOAD_CONST               5 ('return')

102           LOAD_CONST               2 ('Optional[str]')

 98           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _resolve_webhook_url at 0x0000018C17CD4970, file "app\services\monitoring\slack_alert_transport.py", line 98>:
 98           RESUME                   0

120           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (webhook_url)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (webhook_url)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L1)
              NOT_TAKEN

121           LOAD_FAST_BORROW         0 (webhook_url)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

122   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage)
              LOAD_GLOBAL              6 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

123           LOAD_FAST_BORROW         1 (brokerage)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('alert_slack_webhook_url')
              CALL                     1
              STORE_FAST               2 (v)

124           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (v)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (v)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

125           LOAD_FAST_BORROW         2 (v)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

126   L2:     LOAD_GLOBAL             10 (os)
              LOAD_ATTR               12 (environ)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_GLOBAL             14 (_ENV_OPERATOR_WEBHOOK)
              CALL                     1
              STORE_FAST               3 (env)

127           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (env)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         3 (env)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L3)
              NOT_TAKEN

128           LOAD_FAST_BORROW         3 (env)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

129   L3:     LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "app\services\monitoring\slack_alert_transport.py", line 136>:
136           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('safe_alert')

137           LOAD_CONST               2 ('Dict[str, Any]')

136           LOAD_CONST               3 ('include_metadata')

139           LOAD_CONST               4 ('bool')

136           LOAD_CONST               5 ('return')

140           LOAD_CONST               2 ('Dict[str, Any]')

136           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _build_slack_payload at 0x0000018C17EF9A30, file "app\services\monitoring\slack_alert_transport.py", line 136>:
  --            MAKE_CELL               11 (filtered)

 136            RESUME                   0

 143            LOAD_FAST_BORROW         0 (safe_alert)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               1 ('severity')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('INFO')
        L1:     STORE_FAST               2 (sev)

 144            LOAD_FAST_BORROW         0 (safe_alert)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               3 ('category')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('RUNTIME')
        L2:     STORE_FAST               3 (cat)

 145            LOAD_FAST_BORROW         0 (safe_alert)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               5 ('title')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 ('PAS alert')
        L3:     STORE_FAST               4 (title)

 146            LOAD_FAST_BORROW         0 (safe_alert)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               7 ('description')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L4:     STORE_FAST               5 (desc)

 150            LOAD_CONST               9 ('CRITICAL')
                LOAD_CONST              10 ('🚨')

 151            LOAD_CONST              11 ('HIGH')
                LOAD_CONST              12 ('⚠️')

 152            LOAD_CONST              13 ('MEDIUM')
                LOAD_CONST              14 ('🟠')

 153            LOAD_CONST              15 ('LOW')
                LOAD_CONST              16 ('🟡')

 154            LOAD_CONST               2 ('INFO')
                LOAD_CONST              17 ('ℹ️')

 149            BUILD_MAP                5

 155            LOAD_ATTR                1 (get + NULL|self)
                LOAD_FAST_BORROW         2 (sev)
                LOAD_CONST              17 ('ℹ️')
                CALL                     2

 149            STORE_FAST               6 (sev_emoji)

 159            LOAD_CONST              18 ('type')
                LOAD_CONST              19 ('header')

 160            LOAD_CONST              20 ('text')

 161            LOAD_CONST              18 ('type')
                LOAD_CONST              21 ('plain_text')

 162            LOAD_CONST              20 ('text')
                LOAD_FAST_BORROW         6 (sev_emoji)
                FORMAT_SIMPLE
                LOAD_CONST              22 (' PAS alert: ')
                LOAD_FAST_BORROW         2 (sev)
                FORMAT_SIMPLE
                LOAD_CONST              23 (' / ')
                LOAD_FAST_BORROW         3 (cat)
                FORMAT_SIMPLE
                BUILD_STRING             5

 160            BUILD_MAP                2

 158            BUILD_MAP                2

 166            LOAD_CONST              18 ('type')
                LOAD_CONST              24 ('section')

 167            LOAD_CONST              20 ('text')
                LOAD_CONST              18 ('type')
                LOAD_CONST              25 ('mrkdwn')
                LOAD_CONST              20 ('text')
                LOAD_CONST              26 ('*')
                LOAD_FAST_BORROW         4 (title)
                FORMAT_SIMPLE
                LOAD_CONST              26 ('*')
                BUILD_STRING             3
                BUILD_MAP                2

 165            BUILD_MAP                2

 157            BUILD_LIST               2
                STORE_FAST               7 (blocks)

 170            LOAD_FAST_BORROW         5 (desc)
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L5)
                NOT_TAKEN

 171            LOAD_FAST_BORROW         7 (blocks)
                LOAD_ATTR                3 (append + NULL|self)

 172            LOAD_CONST              18 ('type')
                LOAD_CONST              24 ('section')

 173            LOAD_CONST              20 ('text')
                LOAD_CONST              18 ('type')
                LOAD_CONST              25 ('mrkdwn')
                LOAD_CONST              20 ('text')
                LOAD_FAST_BORROW         5 (desc)
                LOAD_CONST              27 (slice(None, 2900, None))
                BINARY_OP               26 ([])
                BUILD_MAP                2

 171            BUILD_MAP                2
                CALL                     1
                POP_TOP

 176    L5:     LOAD_FAST_BORROW         1 (include_metadata)
                TO_BOOL
                POP_JUMP_IF_FALSE      156 (to L13)
                NOT_TAKEN

 177            LOAD_FAST_BORROW         0 (safe_alert)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST              28 ('metadata')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
        L6:     STORE_FAST               8 (md)

 178            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         8 (md)
                LOAD_GLOBAL              6 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      107 (to L13)
                NOT_TAKEN

 180            LOAD_GLOBAL              8 (_METADATA_ALLOWED)
                GET_ITER

 179            LOAD_FAST_AND_CLEAR      9 (k)
                SWAP                     2
        L7:     BUILD_MAP                0
                SWAP                     2

 180    L8:     FOR_ITER                20 (to L11)
                STORE_FAST_LOAD_FAST   153 (k, k)
                LOAD_FAST_BORROW         8 (md)
                CONTAINS_OP              0 (in)
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)
       L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (k, md)
                LOAD_FAST_BORROW         9 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           22 (to L8)
       L11:     END_FOR
                POP_ITER

 179   L12:     SWAP                     2
                STORE_FAST               9 (k)
                STORE_DEREF             11 (filtered)

 182            LOAD_DEREF              11 (filtered)
                TO_BOOL
                POP_JUMP_IF_FALSE       62 (to L13)
                NOT_TAKEN

 183            LOAD_CONST              29 ('\n')
                LOAD_ATTR               11 (join + NULL|self)
                LOAD_FAST_BORROW        11 (filtered)
                BUILD_TUPLE              1
                LOAD_CONST              30 (<code object <genexpr> at 0x0000018C180531B0, file "app\services\monitoring\slack_alert_transport.py", line 183>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 184            LOAD_GLOBAL             13 (sorted + NULL)
                LOAD_DEREF              11 (filtered)
                CALL                     1
                GET_ITER

 183            CALL                     0
                CALL                     1
                STORE_FAST              10 (lines)

 186            LOAD_FAST_BORROW         7 (blocks)
                LOAD_ATTR                3 (append + NULL|self)

 187            LOAD_CONST              18 ('type')
                LOAD_CONST              24 ('section')

 188            LOAD_CONST              20 ('text')
                LOAD_CONST              18 ('type')
                LOAD_CONST              25 ('mrkdwn')
                LOAD_CONST              20 ('text')
                LOAD_FAST_BORROW        10 (lines)
                BUILD_MAP                2

 186            BUILD_MAP                2
                CALL                     1
                POP_TOP

 192   L13:     LOAD_CONST              20 ('text')
                LOAD_CONST              31 ('PAS alert: ')
                LOAD_FAST_BORROW         2 (sev)
                FORMAT_SIMPLE
                LOAD_CONST              23 (' / ')
                LOAD_FAST_BORROW         3 (cat)
                FORMAT_SIMPLE
                BUILD_STRING             4

 193            LOAD_CONST              32 ('blocks')
                LOAD_FAST_BORROW         7 (blocks)

 191            BUILD_MAP                2
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 179            SWAP                     2
                STORE_FAST               9 (k)
                RERAISE                  0
ExceptionTable:
  L7 to L9 -> L14 [2]
  L10 to L12 -> L14 [2]

Disassembly of <code object <genexpr> at 0x0000018C180531B0, file "app\services\monitoring\slack_alert_transport.py", line 183>:
  --           COPY_FREE_VARS           1

 183           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 184   L2:     FOR_ITER                21 (to L3)
               STORE_FAST               1 (k)
               LOAD_CONST               0 ('• *')
               LOAD_FAST_BORROW         1 (k)
               FORMAT_SIMPLE
               LOAD_CONST               1 ('*: `')
               LOAD_DEREF               2 (filtered)
               LOAD_FAST_BORROW         1 (k)
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 ('`')
               BUILD_STRING             5
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           23 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\monitoring\slack_alert_transport.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert')

202           LOAD_CONST               2 ('Any')

201           LOAD_CONST               3 ('webhook_url')

204           LOAD_CONST               4 ('Optional[str]')

201           LOAD_CONST               5 ('brokerage')

205           LOAD_CONST               2 ('Any')

201           LOAD_CONST               6 ('include_metadata')

206           LOAD_CONST               7 ('bool')

201           LOAD_CONST               8 ('return')

207           LOAD_CONST               9 ('Dict[str, Any]')

201           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object send_alert_to_slack at 0x0000018C17ED2550, file "app\services\monitoring\slack_alert_transport.py", line 201>:
 201            RESUME                   0

 234            BUILD_LIST               0
                STORE_FAST               4 (warnings)

 236            LOAD_GLOBAL              1 (alert_to_safe_dict + NULL)
                LOAD_FAST_BORROW         0 (alert)
                CALL                     1
                STORE_FAST               5 (safe)

 237            LOAD_FAST_BORROW         5 (safe)
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L1)
                NOT_TAKEN

 239            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 240            LOAD_CONST               3 ('warnings')
                LOAD_CONST               4 ('alert_input_invalid')
                BUILD_LIST               1

 241            LOAD_CONST               5 ('error_code')
                LOAD_CONST               4 ('alert_input_invalid')

 238            BUILD_MAP                3
                RETURN_VALUE

 246    L1:     LOAD_GLOBAL              2 (_ALERT_PAYLOAD_ALLOWED)
                GET_ITER

 245            LOAD_FAST_AND_CLEAR      6 (k)
                SWAP                     2
        L2:     BUILD_MAP                0
                SWAP                     2

 246    L3:     FOR_ITER                20 (to L6)
                STORE_FAST_LOAD_FAST   102 (k, k)
                LOAD_FAST_BORROW         5 (safe)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (k, safe)
                LOAD_FAST_BORROW         6 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           22 (to L3)
        L6:     END_FOR
                POP_ITER

 245    L7:     STORE_FAST               7 (projected)
                STORE_FAST               6 (k)

 248            LOAD_FAST_BORROW         3 (include_metadata)
                TO_BOOL
                POP_JUMP_IF_FALSE       92 (to L14)
                NOT_TAKEN
                LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (safe)
                LOAD_ATTR                7 (get + NULL|self)
                LOAD_CONST               6 ('metadata')
                CALL                     1
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN

 251            LOAD_GLOBAL             10 (_METADATA_ALLOWED)
                GET_ITER

 249            LOAD_FAST_AND_CLEAR      6 (k)
                SWAP                     2
        L8:     BUILD_MAP                0
                SWAP                     2

 251    L9:     FOR_ITER                34 (to L12)
                STORE_FAST               6 (k)

 252            LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (k, safe)
                LOAD_CONST               6 ('metadata')
                BINARY_OP               26 ([])
                CONTAINS_OP              0 (in)

 250   L10:     POP_JUMP_IF_TRUE         3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L9)
       L11:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (k, safe)
                LOAD_CONST               6 ('metadata')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         6 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           36 (to L9)

 251   L12:     END_FOR
                POP_ITER

 249   L13:     SWAP                     2
                STORE_FAST               6 (k)
                LOAD_FAST_BORROW         7 (projected)
                LOAD_CONST               6 ('metadata')
                STORE_SUBSCR

 254   L14:     LOAD_GLOBAL             13 (_build_slack_payload + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 115 (projected, include_metadata)
                LOAD_CONST               7 (('include_metadata',))
                CALL_KW                  2
                STORE_FAST               8 (body)

 256            LOAD_GLOBAL             15 (_resolve_webhook_url + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (webhook_url, brokerage)
                LOAD_CONST               8 (('webhook_url', 'brokerage'))
                CALL_KW                  2
                STORE_FAST               9 (url)

 257            LOAD_FAST_BORROW         9 (url)
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L15)
                NOT_TAKEN

 259            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 260            LOAD_CONST               3 ('warnings')
                LOAD_CONST               9 ('slack_webhook_not_configured')
                BUILD_LIST               1

 261            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('slack_webhook_not_configured')

 258            BUILD_MAP                3
                RETURN_VALUE

 267   L15:     NOP

 268   L16:     LOAD_SMALL_INT           0
                LOAD_CONST              10 (None)
                IMPORT_NAME              8 (httpx)
                STORE_FAST              10 (httpx)

 276   L17:     NOP

 277   L18:     LOAD_FAST               10 (httpx)
                LOAD_ATTR               21 (post + NULL|self)
                LOAD_FAST_LOAD_FAST    152 (url, body)
                LOAD_CONST              13 (5.0)
                LOAD_CONST              14 (('json', 'timeout'))
                CALL_KW                  3
                STORE_FAST              11 (resp)

 287   L19:     LOAD_SMALL_INT         200
                LOAD_FAST               11 (resp)
                LOAD_ATTR               30 (status_code)
                SWAP                     2
                COPY                     2
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE        8 (to L20)
                NOT_TAKEN
                LOAD_CONST              17 (300)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       12 (to L22)
                NOT_TAKEN
                JUMP_FORWARD             2 (to L21)
       L20:     POP_TOP
                JUMP_FORWARD             8 (to L22)

 289   L21:     LOAD_CONST               1 ('status')
                LOAD_CONST              18 ('sent')

 290            LOAD_CONST               3 ('warnings')
                LOAD_FAST                4 (warnings)

 291            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 (None)

 288            BUILD_MAP                3
                RETURN_VALUE

 294   L22:     LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('failed')

 295            LOAD_CONST               3 ('warnings')
                LOAD_CONST              19 ('http_')
                LOAD_FAST               11 (resp)
                LOAD_ATTR               30 (status_code)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 296            LOAD_CONST               5 ('error_code')
                LOAD_CONST              19 ('http_')
                LOAD_FAST               11 (resp)
                LOAD_ATTR               30 (status_code)
                FORMAT_SIMPLE
                BUILD_STRING             2

 293            BUILD_MAP                3
                RETURN_VALUE

  --   L23:     SWAP                     2
                POP_TOP

 245            SWAP                     2
                STORE_FAST               6 (k)
                RERAISE                  0

  --   L24:     SWAP                     2
                POP_TOP

 249            SWAP                     2
                STORE_FAST               6 (k)
                RERAISE                  0

  --   L25:     PUSH_EXC_INFO

 269            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       13 (to L27)
                NOT_TAKEN
                POP_TOP

 271            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('failed')

 272            LOAD_CONST               3 ('warnings')
                LOAD_CONST              12 ('httpx_unavailable')
                BUILD_LIST               1

 273            LOAD_CONST               5 ('error_code')
                LOAD_CONST              12 ('httpx_unavailable')

 270            BUILD_MAP                3
                SWAP                     2
       L26:     POP_EXCEPT
                RETURN_VALUE

 269   L27:     RERAISE                  0

  --   L28:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L29:     PUSH_EXC_INFO

 278            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      107 (to L34)
                NOT_TAKEN
                STORE_FAST              12 (e)

 279   L30:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 280            LOAD_CONST              15 ('send_alert_to_slack transport error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 279            CALL                     1
                POP_TOP

 283            LOAD_CONST               1 ('status')
                LOAD_CONST              11 ('failed')

 284            LOAD_CONST               3 ('warnings')
                LOAD_CONST              16 ('transport_exception:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 285            LOAD_CONST               5 ('error_code')
                LOAD_CONST              16 ('transport_exception:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 282            BUILD_MAP                3
       L31:     SWAP                     2
       L32:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L33:     LOAD_CONST              10 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 278   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L4 -> L23 [2]
  L5 to L7 -> L23 [2]
  L8 to L10 -> L24 [2]
  L11 to L13 -> L24 [2]
  L16 to L17 -> L25 [0]
  L18 to L19 -> L29 [0]
  L25 to L26 -> L28 [1] lasti
  L27 to L28 -> L28 [1] lasti
  L29 to L30 -> L35 [1] lasti
  L30 to L31 -> L33 [1] lasti
  L31 to L32 -> L35 [1] lasti
  L33 to L35 -> L35 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app\services\monitoring\slack_alert_transport.py", line 300>:
300           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alerts')

301           LOAD_CONST               2 ('List[Any]')

300           LOAD_CONST               3 ('webhook_url')

303           LOAD_CONST               4 ('Optional[str]')

300           LOAD_CONST               5 ('brokerage')

304           LOAD_CONST               6 ('Any')

300           LOAD_CONST               7 ('include_metadata')

305           LOAD_CONST               8 ('bool')

300           LOAD_CONST               9 ('return')

306           LOAD_CONST              10 ('List[Dict[str, Any]]')

300           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object send_alerts_to_slack at 0x0000018C17E94610, file "app\services\monitoring\slack_alert_transport.py", line 300>:
 300            RESUME                   0

 314            LOAD_FAST_BORROW         0 (alerts)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 315            BUILD_LIST               0
                RETURN_VALUE

 316    L1:     BUILD_LIST               0
                STORE_FAST               4 (out)

 317            LOAD_FAST_BORROW         0 (alerts)
                GET_ITER
        L2:     FOR_ITER                34 (to L5)
                STORE_FAST               5 (a)

 318            NOP

 319    L3:     LOAD_FAST_BORROW         4 (out)
                LOAD_ATTR                1 (append + NULL|self)
                LOAD_GLOBAL              3 (send_alert_to_slack + NULL)

 320            LOAD_FAST_BORROW         5 (a)

 321            LOAD_FAST_BORROW         1 (webhook_url)

 322            LOAD_FAST_BORROW         2 (brokerage)

 323            LOAD_FAST_BORROW         3 (include_metadata)

 319            LOAD_CONST               1 (('webhook_url', 'brokerage', 'include_metadata'))
                CALL_KW                  4
                CALL                     1
                POP_TOP
        L4:     JUMP_BACKWARD           36 (to L2)

 317    L5:     END_FOR
                POP_ITER

 335            LOAD_FAST_BORROW         4 (out)
                RETURN_VALUE

  --    L6:     PUSH_EXC_INFO

 325            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      123 (to L10)
                NOT_TAKEN
                STORE_FAST               6 (e)

 326    L7:     LOAD_GLOBAL              6 (logger)
                LOAD_ATTR                9 (warning + NULL|self)

 327            LOAD_CONST               2 ('send_alerts_to_slack per-item error type=')

 328            LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE

 327            BUILD_STRING             2

 326            CALL                     1
                POP_TOP

 330            LOAD_FAST                4 (out)
                LOAD_ATTR                1 (append + NULL|self)

 331            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('failed')

 332            LOAD_CONST               5 ('warnings')
                LOAD_CONST               6 ('loop_exception:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 333            LOAD_CONST               7 ('error_code')
                LOAD_CONST               6 ('loop_exception:')
                LOAD_GLOBAL             11 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               12 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 330            BUILD_MAP                3
                CALL                     1
                POP_TOP
        L8:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                JUMP_BACKWARD          168 (to L2)

  --    L9:     LOAD_CONST               8 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 325   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L6 [1]
  L6 to L7 -> L11 [2] lasti
  L7 to L8 -> L9 [2] lasti
  L9 to L11 -> L11 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\monitoring\slack_alert_transport.py", line 349>:
349           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')

350           LOAD_CONST               2 ('List[Dict[str, Any]]')

349           LOAD_CONST               3 ('window_seconds')

352           LOAD_CONST               4 ('int')

349           LOAD_CONST               5 ('threshold')

353           LOAD_CONST               4 ('int')

349           LOAD_CONST               6 ('now')

354           LOAD_CONST               7 ('Any')

349           LOAD_CONST               8 ('return')

355           LOAD_CONST               9 ('Dict[str, Any]')

349           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object detect_provider_failure_storm at 0x0000018C177C5700, file "app\services\monitoring\slack_alert_transport.py", line 349>:
 349            RESUME                   0

 385            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('datetime', 'timedelta', 'timezone'))
                IMPORT_NAME              0 (datetime)
                IMPORT_FROM              0 (datetime)
                STORE_FAST               4 (datetime)
                IMPORT_FROM              1 (timedelta)
                STORE_FAST               5 (timedelta)
                IMPORT_FROM              2 (timezone)
                STORE_FAST               6 (timezone)
                POP_TOP

 386            NOP

 387    L1:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         1 (window_seconds)
                CALL                     1
                STORE_FAST               7 (win)

 390    L2:     LOAD_FAST_BORROW         7 (win)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 391            LOAD_SMALL_INT           1
                STORE_FAST               7 (win)

 392    L3:     LOAD_FAST_BORROW         7 (win)
                LOAD_CONST              21 (86400)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 393            LOAD_CONST              21 (86400)
                STORE_FAST               7 (win)

 394    L4:     NOP

 395    L5:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         2 (threshold)
                CALL                     1
                STORE_FAST               8 (thresh)

 398    L6:     LOAD_FAST_BORROW         8 (thresh)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN

 399            LOAD_SMALL_INT           1
                STORE_FAST               8 (thresh)

 401    L7:     LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (now, datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       50 (to L10)
                NOT_TAKEN

 402            LOAD_FAST_BORROW         3 (now)
                LOAD_ATTR               18 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_FAST                3 (now)
                JUMP_FORWARD            27 (to L9)
        L8:     LOAD_FAST_BORROW         3 (now)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_FAST_BORROW         6 (timezone)
                LOAD_ATTR               22 (utc)
                LOAD_CONST               2 (('tzinfo',))
                CALL_KW                  1
        L9:     STORE_FAST               9 (now_dt)
                JUMP_FORWARD            27 (to L11)

 404   L10:     LOAD_FAST_BORROW         4 (datetime)
                LOAD_ATTR               25 (now + NULL|self)
                LOAD_FAST_BORROW         6 (timezone)
                LOAD_ATTR               22 (utc)
                CALL                     1
                STORE_FAST               9 (now_dt)

 405   L11:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (now_dt, timedelta)
                PUSH_NULL
                LOAD_FAST_BORROW         7 (win)
                LOAD_CONST               3 (('seconds',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                STORE_FAST              10 (cutoff)

 407            LOAD_SMALL_INT           0
                STORE_FAST              11 (count)

 408            BUILD_MAP                0
                STORE_FAST              12 (by_provider)

 409            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (events)
                LOAD_GLOBAL             26 (list)
                CALL                     2
                TO_BOOL
                EXTENDED_ARG             1
                POP_JUMP_IF_FALSE      393 (to L27)
                NOT_TAKEN

 410            LOAD_FAST_BORROW         0 (events)
                GET_ITER
       L12:     EXTENDED_ARG             1
                FOR_ITER               385 (to L26)
                STORE_FAST              13 (ev)

 411            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW        13 (ev)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN

 412            JUMP_BACKWARD           28 (to L12)

 413   L13:     LOAD_FAST_BORROW        13 (ev)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               4 ('event_type')
                CALL                     1
                STORE_FAST              14 (et)

 414            LOAD_FAST_BORROW        14 (et)
                LOAD_CONST               5 ('provider.failed')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 415            JUMP_BACKWARD           54 (to L12)

 416   L14:     LOAD_FAST_BORROW        13 (ev)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               6 ('ts')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        18 (to L15)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        13 (ev)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               7 ('created_at')
                CALL                     1
       L15:     STORE_FAST              15 (ts)

 417            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST_BORROW        15 (ts)
                LOAD_GLOBAL             32 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN

 418            JUMP_BACKWARD          120 (to L12)

 419   L16:     NOP

 420   L17:     LOAD_FAST_BORROW         4 (datetime)
                LOAD_ATTR               35 (fromisoformat + NULL|self)
                LOAD_FAST_BORROW        15 (ts)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               8 ('Z')
                LOAD_CONST               9 ('+00:00')
                CALL                     2
                CALL                     1
                STORE_FAST              16 (dt)

 421            LOAD_FAST_BORROW        16 (dt)
                LOAD_ATTR               18 (tzinfo)
                POP_JUMP_IF_NOT_NONE    29 (to L18)
                NOT_TAKEN

 422            LOAD_FAST_BORROW        16 (dt)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_FAST_BORROW         6 (timezone)
                LOAD_ATTR               22 (utc)
                LOAD_CONST               2 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST              16 (dt)

 425   L18:     LOAD_FAST               16 (dt)
                LOAD_FAST               10 (cutoff)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN

 426            JUMP_BACKWARD          205 (to L12)

 427   L19:     LOAD_FAST               11 (count)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST              11 (count)

 428            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               13 (ev)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              11 ('payload')
                CALL                     1
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L20)
                NOT_TAKEN
                LOAD_FAST               13 (ev)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              11 ('payload')
                CALL                     1
                JUMP_FORWARD             1 (to L21)
       L20:     BUILD_MAP                0
       L21:     STORE_FAST              17 (payload)

 429            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               17 (payload)
                LOAD_GLOBAL             28 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L22)
                NOT_TAKEN
                LOAD_FAST               17 (payload)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              12 ('provider')
                CALL                     1
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST              10 (None)
       L23:     STORE_FAST              18 (provider)

 430            LOAD_GLOBAL             17 (isinstance + NULL)
                LOAD_FAST               18 (provider)
                LOAD_GLOBAL             32 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L24)
                NOT_TAKEN
                LOAD_FAST               18 (provider)
                LOAD_ATTR               39 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
                NOT_TAKEN

 431   L24:     LOAD_CONST              13 ('unknown')
                STORE_FAST              18 (provider)

 432   L25:     LOAD_FAST               12 (by_provider)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_FAST               18 (provider)
                LOAD_SMALL_INT           0
                CALL                     2
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_FAST               12 (by_provider)
                LOAD_FAST               18 (provider)
                STORE_SUBSCR
                EXTENDED_ARG             1
                JUMP_BACKWARD          388 (to L12)

 410   L26:     END_FOR
                POP_ITER

 435   L27:     LOAD_CONST              14 ('detected')
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 184 (count, thresh)
                COMPARE_OP             172 (>=)

 436            LOAD_CONST              15 ('count')
                LOAD_FAST_BORROW        11 (count)

 437            LOAD_CONST              16 ('by_provider')
                LOAD_FAST_BORROW        12 (by_provider)

 438            LOAD_CONST              17 ('window_seconds')
                LOAD_FAST_BORROW         7 (win)

 439            LOAD_CONST              18 ('threshold')
                LOAD_FAST_BORROW         8 (thresh)

 440            LOAD_CONST              19 ('warnings')
                BUILD_LIST               0

 441            LOAD_CONST              20 ('error_code')
                LOAD_CONST              10 (None)

 434            BUILD_MAP                7
                RETURN_VALUE

  --   L28:     PUSH_EXC_INFO

 388            LOAD_GLOBAL              8 (TypeError)
                LOAD_GLOBAL             10 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L30)
                NOT_TAKEN
                POP_TOP

 389            LOAD_GLOBAL             12 (_DEFAULT_STORM_WINDOW_SECONDS)
                STORE_FAST               7 (win)
       L29:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 610 (to L2)

 388   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L32:     PUSH_EXC_INFO

 396            LOAD_GLOBAL              8 (TypeError)
                LOAD_GLOBAL             10 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       11 (to L34)
                NOT_TAKEN
                POP_TOP

 397            LOAD_GLOBAL             14 (_DEFAULT_STORM_THRESHOLD)
                STORE_FAST               8 (thresh)
       L33:     POP_EXCEPT
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 610 (to L6)

 396   L34:     RERAISE                  0

  --   L35:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L36:     PUSH_EXC_INFO

 423            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L38)
                NOT_TAKEN
                POP_TOP

 424   L37:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          483 (to L12)

 423   L38:     RERAISE                  0

  --   L39:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L28 [0]
  L5 to L6 -> L32 [0]
  L17 to L18 -> L36 [1]
  L28 to L29 -> L31 [1] lasti
  L30 to L31 -> L31 [1] lasti
  L32 to L33 -> L35 [1] lasti
  L34 to L35 -> L35 [1] lasti
  L36 to L37 -> L39 [2] lasti
  L38 to L39 -> L39 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\monitoring\slack_alert_transport.py", line 535>:
535           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert_id')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _alert_id_allowed at 0x0000018C179C3A50, file "app\services\monitoring\slack_alert_transport.py", line 535>:
  --           MAKE_CELL                1 (stripped)

 535           RESUME                   0

 536           LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (alert_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (alert_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

 537   L1:     LOAD_CONST               0 (False)
               RETURN_VALUE

 538   L2:     LOAD_FAST_BORROW         0 (alert_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               STORE_DEREF              1 (stripped)

 539           LOAD_GLOBAL              6 (any)
               COPY                     1
               LOAD_COMMON_CONSTANT     4 (<built-in function any>)
               IS_OP                    0 (is)
               POP_JUMP_IF_FALSE       35 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_FAST_BORROW         1 (stripped)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18053630, file "app\services\monitoring\slack_alert_transport.py", line 539>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)

 540           LOAD_GLOBAL              8 (_PILOT_ALERT_ID_ALLOWED_PREFIXES)
               GET_ITER

 539           CALL                     0
       L3:     FOR_ITER                12 (to L5)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)
       L4:     POP_ITER
               LOAD_CONST               2 (True)
               RETURN_VALUE
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (False)
               RETURN_VALUE
       L6:     PUSH_NULL
               LOAD_FAST_BORROW         1 (stripped)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18053630, file "app\services\monitoring\slack_alert_transport.py", line 539>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)

 540           LOAD_GLOBAL              8 (_PILOT_ALERT_ID_ALLOWED_PREFIXES)
               GET_ITER

 539           CALL                     0
               CALL                     1
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053630, file "app\services\monitoring\slack_alert_transport.py", line 539>:
  --           COPY_FREE_VARS           1

 539           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 540   L2:     FOR_ITER                22 (to L3)
               STORE_FAST               1 (p)
               LOAD_DEREF               2 (stripped)
               LOAD_ATTR                1 (startswith + NULL|self)
               LOAD_FAST_BORROW         1 (p)
               CALL                     1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           24 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025C30, file "app\services\monitoring\slack_alert_transport.py", line 544>:
544           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('window')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _rate_limited at 0x0000018C17FED830, file "app\services\monitoring\slack_alert_transport.py", line 544>:
 544            RESUME                   0

 547            NOP

 548    L1:     LOAD_GLOBAL              0 (_PILOT_ALERT_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 549            LOAD_GLOBAL              2 (_PILOT_ALERT_LAST_SENT)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         0 (alert_id)
                CALL                     1
                STORE_FAST               2 (last)

 550            LOAD_FAST_BORROW         2 (last)
                POP_JUMP_IF_NOT_NONE    12 (to L5)
                NOT_TAKEN

 551            NOP

 548    L3:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
        L4:     LOAD_CONST               2 (False)
                RETURN_VALUE

 552    L5:     LOAD_GLOBAL              6 (_time)
                LOAD_ATTR                8 (monotonic)
                PUSH_NULL
                CALL                     0
                STORE_FAST               3 (now)

 553            LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (now, last)
                BINARY_OP               10 (-)
                LOAD_GLOBAL             11 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             13 (int + NULL)
                LOAD_FAST_BORROW         1 (window)
                CALL                     1
                CALL                     2
                COMPARE_OP               2 (<)

 548    L6:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
        L7:     RETURN_VALUE
        L8:     PUSH_EXC_INFO
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
       L11:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L13:     PUSH_EXC_INFO

 554            LOAD_GLOBAL             14 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L15)
                NOT_TAKEN
                POP_TOP

 555   L14:     POP_EXCEPT
                LOAD_CONST               2 (False)
                RETURN_VALUE

 554   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [0]
  L2 to L3 -> L8 [2] lasti
  L3 to L4 -> L13 [0]
  L5 to L6 -> L8 [2] lasti
  L6 to L7 -> L13 [0]
  L8 to L10 -> L12 [4] lasti
  L10 to L11 -> L13 [0]
  L12 to L13 -> L13 [0]
  L13 to L14 -> L16 [1] lasti
  L15 to L16 -> L16 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\monitoring\slack_alert_transport.py", line 558>:
558           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _mark_sent at 0x0000018C17FA92F0, file "app\services\monitoring\slack_alert_transport.py", line 558>:
 558            RESUME                   0

 559            NOP

 560    L1:     LOAD_GLOBAL              0 (_PILOT_ALERT_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 561            LOAD_GLOBAL              2 (_time)
                LOAD_ATTR                4 (monotonic)
                PUSH_NULL
                CALL                     0
                LOAD_GLOBAL              6 (_PILOT_ALERT_LAST_SENT)
                LOAD_FAST_BORROW         0 (alert_id)
                STORE_SUBSCR

 560    L3:     LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
        L4:     LOAD_CONST               0 (None)
                RETURN_VALUE
        L5:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L6)
                NOT_TAKEN
                RERAISE                  2
        L6:     POP_TOP
        L7:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
        L8:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 562            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L12)
                NOT_TAKEN
                POP_TOP

 563   L11:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 562   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L2 to L3 -> L5 [2] lasti
  L3 to L4 -> L10 [0]
  L5 to L7 -> L9 [4] lasti
  L7 to L8 -> L10 [0]
  L9 to L10 -> L10 [0]
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\monitoring\slack_alert_transport.py", line 566>:
566           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('body')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_body_for_forbidden at 0x0000018C180C4470, file "app\services\monitoring\slack_alert_transport.py", line 566>:
  --           MAKE_CELL                1 (found)
               MAKE_CELL                2 (walk)

 566           RESUME                   0

 569           BUILD_LIST               0
               STORE_DEREF              1 (found)

 570           LOAD_CONST               1 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\monitoring\slack_alert_transport.py", line 570>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (found)
               LOAD_FAST_BORROW         2 (walk)
               BUILD_TUPLE              2
               LOAD_CONST               2 (<code object walk at 0x0000018C17D819C0, file "app\services\monitoring\slack_alert_transport.py", line 570>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              2 (walk)

 590           LOAD_DEREF               2 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (body)
               CALL                     1
               POP_TOP

 591           LOAD_DEREF               1 (found)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\monitoring\slack_alert_transport.py", line 570>:
570           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('obj')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object walk at 0x0000018C17D819C0, file "app\services\monitoring\slack_alert_transport.py", line 570>:
  --            COPY_FREE_VARS           2

 570            RESUME                   0

 571            NOP

 572    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      121 (to L14)
        L2:     NOT_TAKEN

 573    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                98 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 574            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       64 (to L11)
                NOT_TAKEN

 575            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 576            LOAD_GLOBAL             10 (_PILOT_FORBIDDEN_BODY_TOKENS)
                GET_ITER
        L5:     FOR_ITER                37 (to L10)
                STORE_FAST               4 (tok)

 577            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L7:     LOAD_FAST_BORROW         4 (tok)
                LOAD_DEREF               6 (found)
                CONTAINS_OP              1 (not in)
        L8:     POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           20 (to L5)

 578    L9:     LOAD_DEREF               6 (found)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         4 (tok)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           39 (to L5)

 576   L10:     END_FOR
                POP_ITER

 579   L11:     LOAD_DEREF               7 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          100 (to L4)

 573   L12:     END_FOR
                POP_ITER
       L13:     LOAD_CONST               0 (None)
                RETURN_VALUE

 580   L14:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             14 (list)
                LOAD_GLOBAL             16 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L18)
                NOT_TAKEN

 581            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L15:     FOR_ITER                11 (to L16)
                STORE_FAST               2 (v)

 582            LOAD_DEREF               7 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           13 (to L15)

 581   L16:     END_FOR
                POP_ITER
       L17:     LOAD_CONST               0 (None)
                RETURN_VALUE

 583   L18:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       66 (to L26)
                NOT_TAKEN

 584            LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (ol)

 585            LOAD_GLOBAL             10 (_PILOT_FORBIDDEN_BODY_TOKENS)
                GET_ITER
       L19:     FOR_ITER                37 (to L24)
                STORE_FAST               4 (tok)

 586            LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (tok, ol)
                CONTAINS_OP              0 (in)
       L20:     POP_JUMP_IF_TRUE         3 (to L21)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L19)
       L21:     LOAD_FAST_BORROW         4 (tok)
                LOAD_DEREF               6 (found)
                CONTAINS_OP              1 (not in)
       L22:     POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                JUMP_BACKWARD           20 (to L19)

 587   L23:     LOAD_DEREF               6 (found)
                LOAD_ATTR               13 (append + NULL|self)
                LOAD_FAST_BORROW         4 (tok)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           39 (to L19)

 585   L24:     END_FOR
                POP_ITER
       L25:     LOAD_CONST               0 (None)
                RETURN_VALUE

 583   L26:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L27:     PUSH_EXC_INFO

 588            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L29)
                NOT_TAKEN
                POP_TOP

 589   L28:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 588   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L27 [0]
  L3 to L6 -> L27 [0]
  L7 to L8 -> L27 [0]
  L9 to L13 -> L27 [0]
  L14 to L17 -> L27 [0]
  L18 to L20 -> L27 [0]
  L21 to L22 -> L27 [0]
  L23 to L25 -> L27 [0]
  L27 to L28 -> L30 [1] lasti
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\monitoring\slack_alert_transport.py", line 594>:
594           RESUME                   0
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

Disassembly of <code object reset_pilot_alert_rate_limit_for_tests at 0x0000018C18010B30, file "app\services\monitoring\slack_alert_transport.py", line 594>:
 594           RESUME                   0

 596           LOAD_GLOBAL              0 (_PILOT_ALERT_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 597           LOAD_GLOBAL              2 (_PILOT_ALERT_LAST_SENT)
               LOAD_ATTR                5 (clear + NULL|self)
               CALL                     0
               POP_TOP

 596   L2:     LOAD_CONST               1 (None)
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

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\monitoring\slack_alert_transport.py", line 600>:
600           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('alert')

601           LOAD_CONST               2 ('Any')

600           LOAD_CONST               3 ('webhook_url')

603           LOAD_CONST               4 ('Optional[str]')

600           LOAD_CONST               5 ('brokerage')

604           LOAD_CONST               2 ('Any')

600           LOAD_CONST               6 ('include_metadata')

605           LOAD_CONST               7 ('bool')

600           LOAD_CONST               8 ('dedupe_window')

606           LOAD_CONST               9 ('int')

600           LOAD_CONST              10 ('return')

607           LOAD_CONST              11 ('Dict[str, Any]')

600           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object send_pilot_alert_to_slack at 0x0000018C17D8BF50, file "app\services\monitoring\slack_alert_transport.py", line 600>:
 600            RESUME                   0

 627            LOAD_GLOBAL              1 (alert_to_safe_dict + NULL)
                LOAD_FAST_BORROW         0 (alert)
                CALL                     1
                STORE_FAST               5 (safe)

 628            LOAD_FAST_BORROW         5 (safe)
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L1)
                NOT_TAKEN

 630            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('skipped')

 631            LOAD_CONST               3 ('warnings')
                LOAD_CONST               4 ('alert_input_invalid')
                BUILD_LIST               1

 632            LOAD_CONST               5 ('error_code')
                LOAD_CONST               4 ('alert_input_invalid')

 629            BUILD_MAP                3
                RETURN_VALUE

 634    L1:     LOAD_FAST_BORROW         5 (safe)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               6 ('id')
                CALL                     1
                STORE_FAST               6 (alert_id)

 635            LOAD_GLOBAL              5 (_alert_id_allowed + NULL)
                LOAD_FAST_BORROW         6 (alert_id)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        10 (to L2)
                NOT_TAKEN

 637            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('refused')

 638            LOAD_CONST               3 ('warnings')
                LOAD_CONST               8 ('pilot_alert_id_not_in_allow_list')
                BUILD_LIST               1

 639            LOAD_CONST               5 ('error_code')
                LOAD_CONST               8 ('pilot_alert_id_not_in_allow_list')

 636            BUILD_MAP                3
                RETURN_VALUE

 642    L2:     LOAD_GLOBAL              7 (_rate_limited + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (alert_id, dedupe_window)
                LOAD_CONST               9 (('window',))
                CALL_KW                  2
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L3)
                NOT_TAKEN

 644            LOAD_CONST               1 ('status')
                LOAD_CONST              10 ('rate_limited')

 645            LOAD_CONST               3 ('warnings')
                LOAD_CONST              11 ('pilot_alert_rate_limited')
                BUILD_LIST               1

 646            LOAD_CONST               5 ('error_code')
                LOAD_CONST              11 ('pilot_alert_rate_limited')

 643            BUILD_MAP                3
                RETURN_VALUE

 652    L3:     LOAD_GLOBAL              8 (_ALERT_PAYLOAD_ALLOWED)
                GET_ITER

 651            LOAD_FAST_AND_CLEAR      7 (k)
                SWAP                     2
        L4:     BUILD_MAP                0
                SWAP                     2

 652    L5:     FOR_ITER                20 (to L8)
                STORE_FAST_LOAD_FAST   119 (k, k)
                LOAD_FAST_BORROW         5 (safe)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (k, safe)
                LOAD_FAST_BORROW         7 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           22 (to L5)
        L8:     END_FOR
                POP_ITER

 651    L9:     STORE_FAST               8 (projected)
                STORE_FAST               7 (k)

 654            LOAD_FAST_BORROW         3 (include_metadata)
                TO_BOOL
                POP_JUMP_IF_FALSE       92 (to L16)
                NOT_TAKEN
                LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (safe)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              12 ('metadata')
                CALL                     1
                LOAD_GLOBAL             12 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L16)
                NOT_TAKEN

 657            LOAD_GLOBAL             14 (_METADATA_ALLOWED)
                GET_ITER

 655            LOAD_FAST_AND_CLEAR      7 (k)
                SWAP                     2
       L10:     BUILD_MAP                0
                SWAP                     2

 657   L11:     FOR_ITER                34 (to L14)
                STORE_FAST               7 (k)

 658            LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (k, safe)
                LOAD_CONST              12 ('metadata')
                BINARY_OP               26 ([])
                CONTAINS_OP              0 (in)

 656   L12:     POP_JUMP_IF_TRUE         3 (to L13)
                NOT_TAKEN
                JUMP_BACKWARD           18 (to L11)
       L13:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (k, safe)
                LOAD_CONST              12 ('metadata')
                BINARY_OP               26 ([])
                LOAD_FAST_BORROW         7 (k)
                BINARY_OP               26 ([])
                MAP_ADD                  2
                JUMP_BACKWARD           36 (to L11)

 657   L14:     END_FOR
                POP_ITER

 655   L15:     SWAP                     2
                STORE_FAST               7 (k)
                LOAD_FAST_BORROW         8 (projected)
                LOAD_CONST              12 ('metadata')
                STORE_SUBSCR

 660   L16:     LOAD_GLOBAL             17 (_build_slack_payload + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 131 (projected, include_metadata)
                LOAD_CONST              13 (('include_metadata',))
                CALL_KW                  2
                STORE_FAST               9 (body)

 661            LOAD_GLOBAL             19 (_scan_body_for_forbidden + NULL)
                LOAD_FAST_BORROW         9 (body)
                CALL                     1
                STORE_FAST              10 (leaked)

 662            LOAD_FAST_BORROW        10 (leaked)
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L17)
                NOT_TAKEN

 668            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('refused')

 669            LOAD_CONST               3 ('warnings')
                LOAD_CONST              14 ('pilot_body_forbidden_token:')
                LOAD_FAST_BORROW        10 (leaked)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 670            LOAD_CONST               5 ('error_code')
                LOAD_CONST              15 ('pilot_body_forbidden_token')

 667            BUILD_MAP                3
                RETURN_VALUE

 673   L17:     LOAD_GLOBAL             21 (send_alert_to_slack + NULL)

 674            LOAD_FAST_BORROW         0 (alert)

 675            LOAD_FAST_BORROW         1 (webhook_url)

 676            LOAD_FAST_BORROW         2 (brokerage)

 677            LOAD_FAST_BORROW         3 (include_metadata)

 673            LOAD_CONST              16 (('webhook_url', 'brokerage', 'include_metadata'))
                CALL_KW                  4
                STORE_FAST              11 (env)

 679            LOAD_FAST_BORROW        11 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST              17 ('sent')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L18)
                NOT_TAKEN

 680            LOAD_GLOBAL             23 (_mark_sent + NULL)
                LOAD_FAST_BORROW         6 (alert_id)
                CALL                     1
                POP_TOP

 681   L18:     LOAD_FAST_BORROW        11 (env)
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 651            SWAP                     2
                STORE_FAST               7 (k)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 655            SWAP                     2
                STORE_FAST               7 (k)
                RERAISE                  0
ExceptionTable:
  L4 to L6 -> L19 [2]
  L7 to L9 -> L19 [2]
  L10 to L12 -> L20 [2]
  L13 to L15 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180C4140, file "app\services\monitoring\slack_alert_transport.py", line 684>:
684           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('worker_id')

686           LOAD_CONST               2 ('Optional[str]')

684           LOAD_CONST               3 ('last_seen_iso')

687           LOAD_CONST               2 ('Optional[str]')

684           LOAD_CONST               4 ('threshold_secs')

688           LOAD_CONST               5 ('int')

684           LOAD_CONST               6 ('webhook_url')

689           LOAD_CONST               2 ('Optional[str]')

684           LOAD_CONST               7 ('brokerage')

690           LOAD_CONST               8 ('Any')

684           LOAD_CONST               9 ('now')

691           LOAD_CONST               8 ('Any')

684           LOAD_CONST              10 ('return')

692           LOAD_CONST              11 ('Dict[str, Any]')

684           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object emit_worker_liveness_heartbeat at 0x0000018C17D7FD70, file "app\services\monitoring\slack_alert_transport.py", line 684>:
 684            RESUME                   0

 705            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('datetime', 'timezone', 'timedelta'))
                IMPORT_NAME              0 (datetime)
                IMPORT_FROM              0 (datetime)
                STORE_FAST               6 (_dt)
                IMPORT_FROM              1 (timezone)
                STORE_FAST               7 (_tz)
                IMPORT_FROM              2 (timedelta)
                STORE_FAST               8 (_td)
                POP_TOP

 706            NOP

 707    L1:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         2 (threshold_secs)
                CALL                     1
                STORE_FAST               9 (thresh)

 710    L2:     LOAD_FAST_BORROW         9 (thresh)
                LOAD_SMALL_INT          60
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN

 711            LOAD_SMALL_INT          60
                STORE_FAST               9 (thresh)

 712    L3:     LOAD_FAST_BORROW         9 (thresh)
                LOAD_CONST              27 (86400)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 713            LOAD_CONST              27 (86400)
                STORE_FAST               9 (thresh)

 715    L4:     LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (worker_id)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (worker_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (worker_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               2 ('unknown')
        L6:     STORE_FAST              10 (wid)

 716            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (now, _dt)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       50 (to L9)
                NOT_TAKEN

 717            LOAD_FAST_BORROW         5 (now)
                LOAD_ATTR               18 (tzinfo)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_FAST                5 (now)
                JUMP_FORWARD            27 (to L8)
        L7:     LOAD_FAST_BORROW         5 (now)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_FAST_BORROW         7 (_tz)
                LOAD_ATTR               22 (utc)
                LOAD_CONST               3 (('tzinfo',))
                CALL_KW                  1
        L8:     STORE_FAST              11 (now_dt)
                JUMP_FORWARD            27 (to L10)

 719    L9:     LOAD_FAST_BORROW         6 (_dt)
                LOAD_ATTR               25 (now + NULL|self)
                LOAD_FAST_BORROW         7 (_tz)
                LOAD_ATTR               22 (utc)
                CALL                     1
                STORE_FAST              11 (now_dt)

 721   L10:     LOAD_CONST               4 (None)
                STORE_FAST              12 (last_dt)

 722            LOAD_CONST               4 (None)
                STORE_FAST              13 (age_seconds)

 723            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (last_seen_iso)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      130 (to L13)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (last_seen_iso)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE      108 (to L13)
                NOT_TAKEN

 724            NOP

 725   L11:     LOAD_FAST_BORROW         6 (_dt)
                LOAD_ATTR               27 (fromisoformat + NULL|self)

 726            LOAD_FAST_BORROW         1 (last_seen_iso)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               5 ('Z')
                LOAD_CONST               6 ('+00:00')
                CALL                     2

 725            CALL                     1
                STORE_FAST              12 (last_dt)

 728            LOAD_FAST_BORROW        12 (last_dt)
                LOAD_ATTR               18 (tzinfo)
                POP_JUMP_IF_NOT_NONE    29 (to L12)
                NOT_TAKEN

 729            LOAD_FAST_BORROW        12 (last_dt)
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_FAST_BORROW         7 (_tz)
                LOAD_ATTR               22 (utc)
                LOAD_CONST               3 (('tzinfo',))
                CALL_KW                  1
                STORE_FAST              12 (last_dt)

 730   L12:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (now_dt, last_dt)
                BINARY_OP               10 (-)
                LOAD_ATTR               29 (total_seconds + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST              13 (age_seconds)

 735   L13:     LOAD_FAST_BORROW        13 (age_seconds)
                POP_JUMP_IF_NONE        16 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 217 (age_seconds, thresh)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       10 (to L14)
                NOT_TAKEN

 738            LOAD_CONST               7 ('status')
                LOAD_CONST               8 ('skipped')

 739            LOAD_CONST               9 ('warnings')
                LOAD_CONST              10 ('worker_liveness_within_threshold')
                BUILD_LIST               1

 740            LOAD_CONST              11 ('error_code')
                LOAD_CONST              10 ('worker_liveness_within_threshold')

 737            BUILD_MAP                3
                RETURN_VALUE

 743   L14:     LOAD_GLOBAL             33 (Alert + NULL)

 744            LOAD_CONST              12 ('worker.liveness.missing:')
                LOAD_FAST_BORROW        10 (wid)
                FORMAT_SIMPLE
                LOAD_CONST              13 (':')
                LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW        11 (now_dt)
                LOAD_ATTR               35 (timestamp + NULL|self)
                CALL                     0
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             4

 745            LOAD_CONST              14 ('RUNTIME')

 746            LOAD_CONST              15 ('HIGH')

 747            LOAD_CONST              16 ('Worker liveness missing')

 749            LOAD_CONST              17 ("Pending-call worker '")
                LOAD_FAST_BORROW        10 (wid)
                FORMAT_SIMPLE
                LOAD_CONST              18 ("' has not heartbeated within ")

 750            LOAD_FAST_BORROW         9 (thresh)
                FORMAT_SIMPLE
                LOAD_CONST              19 ('s. Operator should inspect the worker process.')

 749            BUILD_STRING             5

 752            LOAD_CONST              20 ('app.services.monitoring.slack_alert_transport')

 753            LOAD_GLOBAL             13 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (brokerage)
                LOAD_GLOBAL             36 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (brokerage)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST              21 ('id')
                CALL                     1
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST               4 (None)

 754   L16:     LOAD_FAST_BORROW        13 (age_seconds)
                POP_JUMP_IF_NONE         5 (to L17)
                NOT_TAKEN
                LOAD_CONST              22 ('age_seconds')
                LOAD_FAST_BORROW        13 (age_seconds)
                BUILD_MAP                1
                JUMP_FORWARD             1 (to L18)
       L17:     BUILD_MAP                0

 743   L18:     LOAD_CONST              23 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
                CALL_KW                  8
                STORE_FAST              14 (alert)

 756            LOAD_GLOBAL             41 (send_pilot_alert_to_slack + NULL)

 757            LOAD_FAST_BORROW        14 (alert)

 758            LOAD_FAST_BORROW         3 (webhook_url)

 759            LOAD_FAST_BORROW         4 (brokerage)

 760            LOAD_CONST              24 (True)

 756            LOAD_CONST              25 (('webhook_url', 'brokerage', 'include_metadata'))
                CALL_KW                  4
                RETURN_VALUE

  --   L19:     PUSH_EXC_INFO

 708            LOAD_GLOBAL              8 (TypeError)
                LOAD_GLOBAL             10 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        7 (to L21)
                NOT_TAKEN
                POP_TOP

 709            LOAD_CONST              26 (300)
                STORE_FAST               9 (thresh)
       L20:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 486 (to L2)

 708   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L23:     PUSH_EXC_INFO

 731            LOAD_GLOBAL             30 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        8 (to L25)
                NOT_TAKEN
                POP_TOP

 732            LOAD_CONST               4 (None)
                STORE_FAST              12 (last_dt)

 733            LOAD_CONST               4 (None)
                STORE_FAST              13 (age_seconds)
       L24:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 179 (to L13)

 731   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L19 [0]
  L11 to L13 -> L23 [0]
  L19 to L20 -> L22 [1] lasti
  L21 to L22 -> L22 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\monitoring\slack_alert_transport.py", line 764>:
764           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('subsystem')

766           LOAD_CONST               2 ('str')

764           LOAD_CONST               3 ('brokerage_id')

767           LOAD_CONST               4 ('Optional[str]')

764           LOAD_CONST               5 ('webhook_url')

768           LOAD_CONST               4 ('Optional[str]')

764           LOAD_CONST               6 ('brokerage')

769           LOAD_CONST               7 ('Any')

764           LOAD_CONST               8 ('return')

770           LOAD_CONST               9 ('Dict[str, Any]')

764           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object emit_pilot_fallback_notice at 0x0000018C17CC2460, file "app\services\monitoring\slack_alert_transport.py", line 764>:
764           RESUME                   0

782           LOAD_FAST_BORROW         0 (subsystem)
              LOAD_CONST               1 ('dedupe')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        8 (to L1)
              NOT_TAKEN

783           LOAD_CONST               2 ('external_pilot.dedupe_fallback')
              STORE_FAST               4 (prefix)

784           LOAD_CONST               3 ('Pending-call dedupe fell back to process-local')
              STORE_FAST               5 (title)

786           LOAD_CONST               4 ('PAS171 durable pending-call dedupe is unavailable. PAS is operating on the PAS170 process-local registry. Operator should restore the durable store before expanding pilot exposure.')

785           STORE_FAST               6 (desc)
              JUMP_FORWARD            23 (to L3)

791   L1:     LOAD_FAST_BORROW         0 (subsystem)
              LOAD_CONST               5 ('callback')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        8 (to L2)
              NOT_TAKEN

792           LOAD_CONST               6 ('external_pilot.callback_schedule_fallback')
              STORE_FAST               4 (prefix)

793           LOAD_CONST               7 ('Callback schedule fell back to process-local')
              STORE_FAST               5 (title)

795           LOAD_CONST               8 ('PAS171 durable callback schedule is unavailable. PAS is operating on the PAS170 process-local registry. Operator should restore the durable store before expanding pilot exposure.')

794           STORE_FAST               6 (desc)
              JUMP_FORWARD             9 (to L3)

802   L2:     LOAD_CONST               9 ('status')
              LOAD_CONST              10 ('refused')

803           LOAD_CONST              11 ('warnings')
              LOAD_CONST              12 ('pilot_fallback_subsystem_unknown')
              BUILD_LIST               1

804           LOAD_CONST              13 ('error_code')
              LOAD_CONST              12 ('pilot_fallback_subsystem_unknown')

801           BUILD_MAP                3
              RETURN_VALUE

807   L3:     LOAD_SMALL_INT           0
              LOAD_CONST              14 (('datetime', 'timezone'))
              IMPORT_NAME              0 (datetime)
              IMPORT_FROM              0 (datetime)
              STORE_FAST               7 (_dt)
              IMPORT_FROM              1 (timezone)
              STORE_FAST               8 (_tz)
              POP_TOP

808           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_FAST                1 (brokerage_id)
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST              15 ('global')
      L5:     STORE_FAST               9 (bid)

809           LOAD_GLOBAL             11 (Alert + NULL)

810           LOAD_FAST_BORROW         4 (prefix)
              FORMAT_SIMPLE
              LOAD_CONST              16 (':')
              LOAD_FAST_BORROW         9 (bid)
              FORMAT_SIMPLE
              LOAD_CONST              16 (':')
              LOAD_GLOBAL             13 (int + NULL)
              LOAD_FAST_BORROW         7 (_dt)
              LOAD_ATTR               15 (now + NULL|self)
              LOAD_FAST_BORROW         8 (_tz)
              LOAD_ATTR               16 (utc)
              CALL                     1
              LOAD_ATTR               19 (timestamp + NULL|self)
              CALL                     0
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             5

811           LOAD_CONST              17 ('INGESTION')

812           LOAD_CONST              18 ('MEDIUM')

813           LOAD_FAST                5 (title)

814           LOAD_FAST                6 (desc)

815           LOAD_CONST              19 ('app.services.monitoring.slack_alert_transport')

816           LOAD_GLOBAL              5 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (brokerage_id)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_FAST                1 (brokerage_id)
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              20 (None)

817   L7:     BUILD_MAP                0

809           LOAD_CONST              21 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
              CALL_KW                  8
              STORE_FAST              10 (alert)

819           LOAD_GLOBAL             21 (send_pilot_alert_to_slack + NULL)

820           LOAD_FAST_BORROW_LOAD_FAST_BORROW 162 (alert, webhook_url)
              LOAD_FAST_BORROW         3 (brokerage)

819           LOAD_CONST              22 (('webhook_url', 'brokerage'))
              CALL_KW                  3
              RETURN_VALUE
```
