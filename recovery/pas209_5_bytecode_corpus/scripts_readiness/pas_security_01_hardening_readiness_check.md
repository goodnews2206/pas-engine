# scripts_readiness/pas_security_01_hardening_readiness_check

- **pyc:** `scripts\__pycache__\pas_security_01_hardening_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas_security_01_hardening_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas_security_01_hardening_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS-SECURITY-01 — Defensive hardening readiness gate.

Deterministic, non-mutating evaluator for "is PAS's defensive
security posture intact?".

Walks the repo and verifies:

  * PAS160-PAS181 readiness scripts still exist.
  * PAS-SECURITY-01 surfaces exist:
      - app/services/security/__init__.py
      - app/services/security/cors_policy.py
      - app/services/security/redirect_validation.py
      - app/services/security/error_safety.py
      - scripts/pas_security_01_hardening_readiness_check.py
      - docs/pas_security_01_defensive_hardening_audit.md
      - tests/mvp/test_pas_security_01_hardening.py
  * app/main.py CORS posture: wildcard is gated on
    ENVIRONMENT == "development"; otherwise origins come from
    settings.BASE_URL.
  * No RedirectResponse usage in app/routes/ (or, if present,
    validate_redirect_target is called nearby).
  * No supabase storage usage (or, if present, doc is updated
    — this gate documents the unused posture).
  * No public-response stack-trace pattern: routes do not
    `return ... str(e)` or `return ... traceback.format_exc()`.
  * Twilio webhook signature verifier present in
    app/routes/twilio_webhook.py.
  * Email-ingestion signature posture present in
    app/routes/email_ingestion.py.
  * Slack webhook signature posture present in
    app/routes/slack_command.py.
  * Every @router.post in app/routes/ either:
      * carries a require_brokerage / require_admin Depends,
      * is a Twilio webhook (signature-verified), or
      * is explicitly whitelisted as a dev/unauthenticated
        surface (no such surface in PAS181).
  * No route accepts brokerage_id from URL/body as source of
    truth (no `brokerage_id: str` declared as a path or query
    parameter in tenant-facing routes).
  * Dependency posture: requirements.txt pins versions for
    fastapi / supabase / cryptography / httpx / pydantic-
    settings / twilio / anthropic / openai.
  * Rate-limit posture: app/utils/rate_limiter.py present;
    Twilio / outbound / simulate routes use rate_limit.
  * Session/token rotation: rotate_brokerage_api_key surface
    present (PAS175); rotate_email_forwarder_secret script
    present (PAS168).
  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /
    embeddings / vector / LLM imports in the security service
    files.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service.py STILL has no UPDATE / DELETE helpers
    (PAS174-PAS181 carry-forward).
  * Event contract registers every PAS-SECURITY-01 event type.
  * Worker still OFF by default.
  * Supports --summary-only / --json.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads .env.
  * Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_iter_route_files`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_cors_posture`, `check_dependency_pinning`, `check_doc_required_clauses`, `check_error_safety_module`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_brokerage_id_body_trust`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_public_raw_exception`, `check_prior_phases_intact`, `check_rate_limit_posture`, `check_redirect_posture`, `check_self_no_env_or_db`, `check_server_side_permissions`, `check_session_token_posture`, `check_storage_posture`, `check_webhook_signatures`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`ADMIN_API_KEY`, `BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS-SECURITY-01 — Defensive hardening readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS\'s defensive\nsecurity posture intact?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 readiness scripts still exist.\n  * PAS-SECURITY-01 surfaces exist:\n      - app/services/security/__init__.py\n      - app/services/security/cors_policy.py\n      - app/services/security/redirect_validation.py\n      - app/services/security/error_safety.py\n      - scripts/pas_security_01_hardening_readiness_check.py\n      - docs/pas_security_01_defensive_hardening_audit.md\n      - tests/mvp/test_pas_security_01_hardening.py\n  * app/main.py CORS posture: wildcard is gated on\n    ENVIRONMENT == "development"; otherwise origins come from\n    settings.BASE_URL.\n  * No RedirectResponse usage in app/routes/ (or, if present,\n    validate_redirect_target is called nearby).\n  * No supabase storage usage (or, if present, doc is updated\n    — this gate documents the unused posture).\n  * No public-response stack-trace pattern: routes do not\n    `return ... str(e)` or `return ... traceback.format_exc()`.\n  * Twilio webhook signature verifier present in\n    app/routes/twilio_webhook.py.\n  * Email-ingestion signature posture present in\n    app/routes/email_ingestion.py.\n  * Slack webhook signature posture present in\n    app/routes/slack_command.py.\n  * Every @router.post in app/routes/ either:\n      * carries a require_brokerage / require_admin Depends,\n      * is a Twilio webhook (signature-verified), or\n      * is explicitly whitelisted as a dev/unauthenticated\n        surface (no such surface in PAS181).\n  * No route accepts brokerage_id from URL/body as source of\n    truth (no `brokerage_id: str` declared as a path or query\n    parameter in tenant-facing routes).\n  * Dependency posture: requirements.txt pins versions for\n    fastapi / supabase / cryptography / httpx / pydantic-\n    settings / twilio / anthropic / openai.\n  * Rate-limit posture: app/utils/rate_limiter.py present;\n    Twilio / outbound / simulate routes use rate_limit.\n  * Session/token rotation: rotate_brokerage_api_key surface\n    present (PAS175); rotate_email_forwarder_secret script\n    present (PAS168).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports in the security service\n    files.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS181 carry-forward).\n  * Event contract registers every PAS-SECURITY-01 event type.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas_security_01_hardening_readiness_report.json'
- 'check_id'
- 'str'
- 'status'
- 'label'
- 'return'
- 'dict'
- 'seconds'
- 'path'
- 'Path'
- 'Optional[str]'
- 'replace'
- 'src'
- '"""'
- "'''"
- 'repo_root'
- 'List[Path]'
- 'app'
- 'routes'
- '.py'
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS-SECURITY-01 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS-SECURITY-01 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS-SECURITY-01 must not touch'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'main.py'
- 'CORSMiddleware'
- 'add_middleware('
- 'cors:middleware_present'
- 'CORS middleware is installed'
- 'missing CORSMiddleware add_middleware call'
- 'ENVIRONMENT == "development"'
- "ENVIRONMENT == 'development'"
- 'cors:wildcard_guarded'
- "Wildcard '*' CORS is gated on ENVIRONMENT == 'development'"
- "expected literal ENVIRONMENT == 'development' guard"
- 'settings.BASE_URL'
- 'settings.CORS_ORIGINS'
- 'cors:origins_from_settings'
- 'Non-dev origins resolved from settings (env/config-bound)'
- 'expected settings.BASE_URL or settings.CORS_ORIGINS'
- 'security'
- 'cors_policy.py'
- 'cors_policy:'
- 'cors_policy module exports '
- 'missing token '
- 'RedirectResponse'
- 'validate_redirect_target'
- 'redirect:no_unguarded_redirect_response'
- 'Any route using RedirectResponse imports validate_redirect_target'
- 'unguarded routes: '
- 'redirect:no_redirect_response_usage'
- 'No RedirectResponse usage in any app/routes/* file'
- 'redirect_validation.py'
- 'redirect_validation:'
- 'redirect_validation module exports '
- 'storage:no_app_dir'
- 'No app/ directory — storage scan trivially clean'
- '*.py'
- 'docs'
- 'pas_security_01_defensive_hardening_audit.md'
- 'storage / rls posture'
- 'storage posture'
- 'storage:usage_documented'
- 'Supabase storage usage is documented in PAS-SECURITY-01 doctrine'
- 'files using storage: '
- 'storage:unused'
- 'No supabase storage usage detected — unused posture'
- 'Route source MUST NOT return ``str(e)`` / ``traceback.format_exc()``\ndirectly to the client. Internal logging via\n``logger.exception(...)`` / ``logger.warning(f"... {type(e).__name__}")``\nis allowed.'
- 'system.py'
- 'return JSONResponse({'
- 'errors:no_public_raw_exception'
- 'No route returns str(e) / traceback.format_exc() in a public response'
- 'offenders: '
- 'error_safety.py'
- 'error_safety:'
- 'error_safety module exports '
- 'twilio_webhook.py'
- 'RequestValidator'
- 'X-Twilio-Signature'
- 'Invalid Twilio signature'
- 'webhook:twilio_signature_verified'
- 'Twilio webhook verifies HMAC signature and rejects 403 on failure'
- 'missing RequestValidator / signature check'
- 'email_ingestion.py'
- 'forwarder_signature'
- 'verify_hmac'
- 'forwarder_secret'
- 'webhook:email_ingestion_signature_posture'
- 'Email ingestion route has a signature/secret verification posture'
- 'missing signature posture markers'
- 'slack_command.py'
- 'X-Slack-Signature'
- 'X-Slack-Request-Timestamp'
- 'slack_signing_secret'
- 'verify_slack_signature'
- 'slack_signature'
- 'webhook:slack_signature_posture'
- 'Slack command route has a signing-secret verification posture'
- 'missing Slack signature markers'
- 'Every @router.post in app/routes/ either:\n   * declares Depends(require_brokerage) / Depends(require_admin),\n   * authenticates inline (Header X-API-Key/X-Admin-Key +\n     body validation against get_brokerage_by_api_key /\n     ADMIN_API_KEY),\n   * verifies signature in the handler body (Twilio HMAC,\n     Slack signing secret), or\n   * is an explicitly documented bootstrap / demo surface\n     (onboarding.py / demo.py / simulate.py) — these are\n     intentional public flows.\n\nBootstrap/demo files are whitelisted by name. Signature-\nverifying files are detected by signature/secret tokens in\nthe file source as a whole.'
- 'Header('
- 'get_brokerage_by_api_key'
- 'ADMIN_API_KEY'
- '@router.post('
- 'Depends(require_brokerage'
- 'Depends(require_admin'
- 'require_brokerage('
- 'require_admin('
- 'auth:server_side_post_routes_gated'
- 'Every @router.post in app/routes/* is auth-gated (Depends or inline Header + validation or signature verifier)'
- ' | '
- 'Tenant routes MUST NOT declare brokerage_id as a Path or\nQuery parameter (would imply trusting the URL/body).'
- 'brokerage_id: str'
- 'brokerage_id:str'
- 'brokerage_id = Query('
- 'brokerage_id = Path('
- 'Body('
- 'Query('
- 'Path('
- 'auth:no_brokerage_id_body_trust'
- 'Tenant routes do not declare brokerage_id as a URL/body parameter'
- 'requirements.txt'
- 'deps:pinned_versions_present'
- 'requirements.txt pins fastapi / supabase / cryptography / httpx / pydantic-settings / twilio / anthropic / openai'
- 'missing pins: '
- 'deps:scanner_unavailable_documented'
- 'Vulnerability scanner posture documented (out-of-band)'
- 'utils'
- 'rate_limiter.py'
- 'def rate_limit('
- 'def client_ip('
- 'HTTPException('
- '429'
- 'rate_limit:module_present'
- 'app/utils/rate_limiter.py exports rate_limit + client_ip'
- 'missing module helpers or 429 raise'
- 'rate_limit('
- 'rate_limit:applied:'
- ' calls rate_limit(...)'
- 'missing rate_limit call'
- 'rate-limit posture'
- 'documented gap'
- 'rate_limit:gap_documented'
- 'Doctrine doc documents the rate-limit gap (email-ingestion / admin / slack)'
- "missing 'rate-limit posture' + 'documented gap' phrasing"
- 'operator'
- 'operator_actions.py'
- 'rotate_brokerage_api_key'
- 'session:api_key_rotation_present'
- 'Operator-driven rotate_brokerage_api_key action is implemented (PAS175)'
- 'rotate_brokerage_api_key not found in operator services'
- 'scripts'
- 'rotate_email_forwarder_secret.py'
- 'session:email_forwarder_rotation_script'
- 'Email forwarder secret rotation script is present (PAS168)'
- 'missing scripts/rotate_email_forwarder_secret.py'
- 'PAS174-PAS181 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS-SECURITY-01 must preserve.'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'disqualifying tokens: '
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/security/__init__.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'app/services/security/cors_policy.py'
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs:phrase:'
- 'Doctrine doc carries clause: '
- 'expected one of: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS-SECURITY-01 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS-SECURITY-01'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas_security_01_hardening_readiness_check'
- 'PAS-SECURITY-01 — Evaluate defensive hardening posture (CORS, redirects, storage, debug leakage, webhook signatures, server-side permissions, dependency pinning, rate limits, raw error exposure, session/token expiry). Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS-SECURITY-01] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS-SECURITY-01] operator actions:'
- '  - '
- '  ... and '
- ' more (see report file)'
- 'payload'
- '  [warn] failed to write report at '
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --repo-root not a directory: '

## Disassembly

```
   0           RESUME                   0

   1           LOAD_CONST               0 ('\nPAS-SECURITY-01 — Defensive hardening readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS\'s defensive\nsecurity posture intact?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS181 readiness scripts still exist.\n  * PAS-SECURITY-01 surfaces exist:\n      - app/services/security/__init__.py\n      - app/services/security/cors_policy.py\n      - app/services/security/redirect_validation.py\n      - app/services/security/error_safety.py\n      - scripts/pas_security_01_hardening_readiness_check.py\n      - docs/pas_security_01_defensive_hardening_audit.md\n      - tests/mvp/test_pas_security_01_hardening.py\n  * app/main.py CORS posture: wildcard is gated on\n    ENVIRONMENT == "development"; otherwise origins come from\n    settings.BASE_URL.\n  * No RedirectResponse usage in app/routes/ (or, if present,\n    validate_redirect_target is called nearby).\n  * No supabase storage usage (or, if present, doc is updated\n    — this gate documents the unused posture).\n  * No public-response stack-trace pattern: routes do not\n    `return ... str(e)` or `return ... traceback.format_exc()`.\n  * Twilio webhook signature verifier present in\n    app/routes/twilio_webhook.py.\n  * Email-ingestion signature posture present in\n    app/routes/email_ingestion.py.\n  * Slack webhook signature posture present in\n    app/routes/slack_command.py.\n  * Every @router.post in app/routes/ either:\n      * carries a require_brokerage / require_admin Depends,\n      * is a Twilio webhook (signature-verified), or\n      * is explicitly whitelisted as a dev/unauthenticated\n        surface (no such surface in PAS181).\n  * No route accepts brokerage_id from URL/body as source of\n    truth (no `brokerage_id: str` declared as a path or query\n    parameter in tenant-facing routes).\n  * Dependency posture: requirements.txt pins versions for\n    fastapi / supabase / cryptography / httpx / pydantic-\n    settings / twilio / anthropic / openai.\n  * Rate-limit posture: app/utils/rate_limiter.py present;\n    Twilio / outbound / simulate routes use rate_limit.\n  * Session/token rotation: rotate_brokerage_api_key surface\n    present (PAS175); rotate_email_forwarder_secret script\n    present (PAS168).\n  * No Gmail / OAuth / IMAP / POP3 / Composio / TrustClaw /\n    embeddings / vector / LLM imports in the security service\n    files.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174-PAS181 carry-forward).\n  * Event contract registers every PAS-SECURITY-01 event type.\n  * Worker still OFF by default.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  63           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  65           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  66           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  67           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  68           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  69           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  70           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  71           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  74           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  75           NOP

  76   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  74   L4:     END_FOR
               POP_ITER

  81           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  82           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  81           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  86           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  87           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  89           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  90           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  97           LOAD_CONST              84 (('app/services/security/__init__.py', 'app/services/security/cors_policy.py', 'app/services/security/redirect_validation.py', 'app/services/security/error_safety.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'docs/pas_security_01_defensive_hardening_audit.md', 'tests/mvp/test_pas_security_01_hardening.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 107           LOAD_CONST              85 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 134           LOAD_CONST              86 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 144           LOAD_CONST              87 (('def classify_cors_posture(', 'def is_wildcard_origin(', 'def is_local_origin(', 'def audit_cors_config(', 'ALLOWED_ENVIRONMENT_TIERS', 'LOCAL_ORIGIN_FORBIDDEN_TOKENS', 'VERDICT_OK', 'VERDICT_WARN', 'VERDICT_FAIL'))
               STORE_NAME              32 (REQUIRED_CORS_POLICY_TOKENS)

 156           LOAD_CONST              88 (('def validate_redirect_target(', 'def normalise_redirect_host(', 'ALLOWED_REDIRECT_SCHEMES', 'FORBIDDEN_REDIRECT_TOKENS'))
               STORE_NAME              33 (REQUIRED_REDIRECT_TOKENS)

 163           LOAD_CONST              89 (('def to_public_error(', 'def scan_response_for_leaks(', 'def redact_response(', 'FORBIDDEN_RESPONSE_FIELDS', 'STACK_TRACE_MARKERS'))
               STORE_NAME              34 (REQUIRED_ERROR_SAFETY_TOKENS)

 172           LOAD_CONST              90 (('security.cors.audit_completed', 'security.redirect.blocked', 'security.webhook.unauthorized', 'security.rate_limit.gap_detected', 'security.error_safety.audit_completed'))
               STORE_NAME              35 (REQUIRED_EVENT_TYPES)

 182           LOAD_CONST              91 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              36 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 206           LOAD_CONST              92 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              37 (FORBIDDEN_INBOX_TOKENS)

 220           LOAD_CONST              93 (('return {"detail": str(e)', "return {'detail': str(e)", 'return {"error": str(e)', "return {'error': str(e)", 'return JSONResponse({', 'traceback.format_exc()'))
               STORE_NAME              38 (FORBIDDEN_RAW_EXCEPTION_PATTERNS)

 230           LOAD_CONST              94 (('fastapi==', 'uvicorn', 'pydantic-settings==', 'twilio==', 'httpx==', 'anthropic==', 'openai==', 'supabase==', 'cryptography'))
               STORE_NAME              39 (PINNED_DEPENDENCIES)

 247           LOAD_CONST              13 ('severity')

 249           LOAD_NAME               27 (SEVERITY_BLOCK)

 247           LOAD_CONST              14 ('detail')

 249           LOAD_CONST              15 ('')

 247           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\pas_security_01_hardening_readiness_check.py", line 247>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA34B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 247>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (_check)

 260           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas_security_01_hardening_readiness_check.py", line 260>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038A30, file "scripts\pas_security_01_hardening_readiness_check.py", line 260>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_now_iso)

 264           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas_security_01_hardening_readiness_check.py", line 264>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053510, file "scripts\pas_security_01_hardening_readiness_check.py", line 264>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_read_text)

 271           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas_security_01_hardening_readiness_check.py", line 271>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas_security_01_hardening_readiness_check.py", line 271>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_strip_python_comments_and_strings)

 306           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas_security_01_hardening_readiness_check.py", line 306>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _iter_route_files at 0x0000018C17FEDA30, file "scripts\pas_security_01_hardening_readiness_check.py", line 306>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_iter_route_files)

 321           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 321>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_files_present at 0x0000018C18061110, file "scripts\pas_security_01_hardening_readiness_check.py", line 321>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 334           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas_security_01_hardening_readiness_check.py", line 334>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas_security_01_hardening_readiness_check.py", line 334>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 347           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas_security_01_hardening_readiness_check.py", line 347>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_memory_review_intact at 0x0000018C180608A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 347>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 360           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas_security_01_hardening_readiness_check.py", line 360>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts\pas_security_01_hardening_readiness_check.py", line 360>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_worker_off_by_default)

 377           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas_security_01_hardening_readiness_check.py", line 377>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_cors_posture at 0x0000018C181A1CE0, file "scripts\pas_security_01_hardening_readiness_check.py", line 377>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_cors_posture)

 424           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas_security_01_hardening_readiness_check.py", line 424>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_redirect_posture at 0x0000018C182DF830, file "scripts\pas_security_01_hardening_readiness_check.py", line 424>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_redirect_posture)

 468           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas_security_01_hardening_readiness_check.py", line 468>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_storage_posture at 0x0000018C182DFCC0, file "scripts\pas_security_01_hardening_readiness_check.py", line 468>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_storage_posture)

 522           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18114300, file "scripts\pas_security_01_hardening_readiness_check.py", line 522>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_public_raw_exception at 0x0000018C17F77EF0, file "scripts\pas_security_01_hardening_readiness_check.py", line 522>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_no_public_raw_exception)

 556           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C181144E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 556>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_error_safety_module at 0x0000018C17FEE030, file "scripts\pas_security_01_hardening_readiness_check.py", line 556>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_error_safety_module)

 571           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas_security_01_hardening_readiness_check.py", line 571>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_webhook_signatures at 0x0000018C17ED9FB0, file "scripts\pas_security_01_hardening_readiness_check.py", line 571>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_webhook_signatures)

 620           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C181146C0, file "scripts\pas_security_01_hardening_readiness_check.py", line 620>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_server_side_permissions at 0x0000018C17EA7750, file "scripts\pas_security_01_hardening_readiness_check.py", line 620>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_server_side_permissions)

 703           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C181147B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 703>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_brokerage_id_body_trust at 0x0000018C17D7C560, file "scripts\pas_security_01_hardening_readiness_check.py", line 703>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_no_brokerage_id_body_trust)

 752           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C181148A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 752>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_dependency_pinning at 0x0000018C17F631E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 752>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_dependency_pinning)

 780           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas_security_01_hardening_readiness_check.py", line 780>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_rate_limit_posture at 0x0000018C17EF9A30, file "scripts\pas_security_01_hardening_readiness_check.py", line 780>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_rate_limit_posture)

 834           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas_security_01_hardening_readiness_check.py", line 834>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_session_token_posture at 0x0000018C17F76200, file "scripts\pas_security_01_hardening_readiness_check.py", line 834>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_session_token_posture)

 868           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18114B70, file "scripts\pas_security_01_hardening_readiness_check.py", line 868>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_audit_service_invariant at 0x0000018C17D76780, file "scripts\pas_security_01_hardening_readiness_check.py", line 868>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_audit_service_invariant)

 895           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas_security_01_hardening_readiness_check.py", line 895>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object check_event_contract at 0x0000018C1801C9E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 895>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_event_contract)

 910           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C18114D50, file "scripts\pas_security_01_hardening_readiness_check.py", line 910>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object check_no_forbidden_imports at 0x0000018C17EA5700, file "scripts\pas_security_01_hardening_readiness_check.py", line 910>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_no_forbidden_imports)

 942           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C18114E40, file "scripts\pas_security_01_hardening_readiness_check.py", line 942>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts\pas_security_01_hardening_readiness_check.py", line 942>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_no_inbox_scan_tokens)

 969           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas_security_01_hardening_readiness_check.py", line 969>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object check_doc_required_clauses at 0x0000018C17CD1ED0, file "scripts\pas_security_01_hardening_readiness_check.py", line 969>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_doc_required_clauses)

1016           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C18114030, file "scripts\pas_security_01_hardening_readiness_check.py", line 1016>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1016>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_self_no_env_or_db)

1049           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C181156B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1049>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1049>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_aggregate)

1065           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C181152F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1065>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _operator_actions at 0x0000018C18048FF0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1065>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_operator_actions)

1075           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18115C50, file "scripts\pas_security_01_hardening_readiness_check.py", line 1075>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object evaluate at 0x0000018C177C5700, file "scripts\pas_security_01_hardening_readiness_check.py", line 1075>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (evaluate)

1115           LOAD_CONST              74 ('pas_security_01_hardening_readiness_report.json')
               STORE_NAME              69 (REPORT_FILENAME)

1118           LOAD_CONST              75 (<code object __annotate__ at 0x0000018C18115D40, file "scripts\pas_security_01_hardening_readiness_check.py", line 1118>)
               MAKE_FUNCTION
               LOAD_CONST              76 (<code object _build_parser at 0x0000018C18128210, file "scripts\pas_security_01_hardening_readiness_check.py", line 1118>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_build_parser)

1139           LOAD_CONST              77 (<code object __annotate__ at 0x0000018C181157A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1139>)
               MAKE_FUNCTION
               LOAD_CONST              78 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas_security_01_hardening_readiness_check.py", line 1139>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_print_summary)

1157           LOAD_CONST              79 (<code object __annotate__ at 0x0000018C18026130, file "scripts\pas_security_01_hardening_readiness_check.py", line 1157>)
               MAKE_FUNCTION
               LOAD_CONST              80 (<code object _write_report at 0x0000018C181283F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1157>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_write_report)

1171           LOAD_CONST              95 ((None,))
               LOAD_CONST              81 (<code object __annotate__ at 0x0000018C18115890, file "scripts\pas_security_01_hardening_readiness_check.py", line 1171>)
               MAKE_FUNCTION
               LOAD_CONST              82 (<code object main at 0x0000018C17D88890, file "scripts\pas_security_01_hardening_readiness_check.py", line 1171>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              73 (main)

1196           LOAD_NAME               74 (__name__)
               LOAD_CONST              83 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

1197           LOAD_NAME                6 (sys)
               LOAD_ATTR              150 (exit)
               PUSH_NULL
               LOAD_NAME               73 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

1196   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  77           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  78   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          387 (to L1)

  77   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\pas_security_01_hardening_readiness_check.py", line 247>:
247           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

248           LOAD_CONST               2 ('str')

247           LOAD_CONST               3 ('status')

248           LOAD_CONST               2 ('str')

247           LOAD_CONST               4 ('label')

248           LOAD_CONST               2 ('str')

247           LOAD_CONST               5 ('severity')

249           LOAD_CONST               2 ('str')

247           LOAD_CONST               6 ('detail')

249           LOAD_CONST               2 ('str')

247           LOAD_CONST               7 ('return')

250           LOAD_CONST               8 ('dict')

247           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 247>:
247           RESUME                   0

252           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

253           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

254           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

255           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

256           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

251           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas_security_01_hardening_readiness_check.py", line 260>:
260           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038A30, file "scripts\pas_security_01_hardening_readiness_check.py", line 260>:
260           RESUME                   0

261           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas_security_01_hardening_readiness_check.py", line 264>:
264           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_text at 0x0000018C18053510, file "scripts\pas_security_01_hardening_readiness_check.py", line 264>:
 264           RESUME                   0

 265           NOP

 266   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 267           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 268   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 267   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas_security_01_hardening_readiness_check.py", line 271>:
271           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('src')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D6DFC0, file "scripts\pas_security_01_hardening_readiness_check.py", line 271>:
271            RESUME                   0

272            BUILD_LIST               0
               STORE_FAST               1 (out)

273            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

274    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

275            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

276            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

277            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

278            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

279            JUMP_FORWARD           240 (to L13)

280    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

281            JUMP_BACKWARD           59 (to L1)

282    L3:     LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               3 ('"""')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        25 (to L4)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               4 ("'''")
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       55 (to L6)
               NOT_TAKEN

283    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

284            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

285            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

286            JUMP_FORWARD           138 (to L13)

287    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

288            JUMP_BACKWARD          161 (to L1)

289    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

290            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

291            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

292    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

293            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

294            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

295            JUMP_BACKWARD           30 (to L7)

296    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_FAST_BORROW         6 (quote)
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_TRUE        14 (to L9)
               NOT_TAKEN
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               2 ('\n')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        2 (to L10)
               NOT_TAKEN

297    L9:     JUMP_FORWARD            11 (to L11)

298   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

299   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

300            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

301   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

302            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

303   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas_security_01_hardening_readiness_check.py", line 306>:
306           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Path]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iter_route_files at 0x0000018C17FEDA30, file "scripts\pas_security_01_hardening_readiness_check.py", line 306>:
306           RESUME                   0

307           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('routes')
              BINARY_OP               11 (/)
              STORE_FAST               1 (routes_dir)

308           LOAD_FAST_BORROW         1 (routes_dir)
              LOAD_ATTR                3 (is_dir + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

309           BUILD_LIST               0
              RETURN_VALUE

310   L1:     BUILD_LIST               0
              STORE_FAST               2 (out)

311           LOAD_GLOBAL              5 (sorted + NULL)
              LOAD_FAST_BORROW         1 (routes_dir)
              LOAD_ATTR                7 (iterdir + NULL|self)
              CALL                     0
              CALL                     1
              GET_ITER
      L2:     FOR_ITER                63 (to L5)
              STORE_FAST               3 (p)

312           LOAD_FAST_BORROW         3 (p)
              LOAD_ATTR                9 (is_file + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L2)
      L3:     LOAD_FAST_BORROW         3 (p)
              LOAD_ATTR               10 (suffix)
              LOAD_CONST               2 ('.py')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           46 (to L2)

313   L4:     LOAD_FAST_BORROW         2 (out)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_FAST_BORROW         3 (p)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           65 (to L2)

311   L5:     END_FOR
              POP_ITER

314           LOAD_FAST_BORROW         2 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 321>:
321           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_files_present at 0x0000018C18061110, file "scripts\pas_security_01_hardening_readiness_check.py", line 321>:
321           RESUME                   0

322           BUILD_LIST               0
              STORE_FAST               1 (out)

323           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

324           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

325           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

326           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

327           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

328   L3:     LOAD_CONST               3 ('Required PAS-SECURITY-01 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

329           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

325   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

323   L6:     END_FOR
              POP_ITER

331           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas_security_01_hardening_readiness_check.py", line 334>:
334           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_prior_phases_intact at 0x0000018C18060A50, file "scripts\pas_security_01_hardening_readiness_check.py", line 334>:
334           RESUME                   0

335           BUILD_LIST               0
              STORE_FAST               1 (out)

336           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

337           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

338           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

339           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

340           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

341   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

342           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS-SECURITY-01 must not delete')

338   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

336   L6:     END_FOR
              POP_ITER

344           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas_security_01_hardening_readiness_check.py", line 347>:
347           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_memory_review_intact at 0x0000018C180608A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 347>:
347           RESUME                   0

348           BUILD_LIST               0
              STORE_FAST               1 (out)

349           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

350           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

351           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

352           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

353           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

354   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

355           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS-SECURITY-01 must not touch')

351   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

349   L6:     END_FOR
              POP_ITER

357           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas_security_01_hardening_readiness_check.py", line 360>:
360           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3A50, file "scripts\pas_security_01_hardening_readiness_check.py", line 360>:
360           RESUME                   0

361           BUILD_LIST               0
              STORE_FAST               1 (out)

362           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('ingestion')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('worker.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

363           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

365           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

366           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

364   L2:     STORE_FAST               4 (literal_ok)

368           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

369           LOAD_CONST               7 ('worker:off_by_default')

370           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

371   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

372           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

368   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

374           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas_security_01_hardening_readiness_check.py", line 377>:
377           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_cors_posture at 0x0000018C181A1CE0, file "scripts\pas_security_01_hardening_readiness_check.py", line 377>:
377            RESUME                   0

378            BUILD_LIST               0
               STORE_FAST               1 (out)

379            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('main.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

380            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

382            LOAD_CONST               3 ('CORSMiddleware')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('add_middleware(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
       L2:     STORE_FAST               4 (middleware_ok)

383            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

384            LOAD_CONST               5 ('cors:middleware_present')

385            LOAD_FAST_BORROW         4 (middleware_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

386    L4:     LOAD_CONST               8 ('CORS middleware is installed')

387            LOAD_FAST_BORROW         4 (middleware_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST               9 ('missing CORSMiddleware add_middleware call')

383    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

391            LOAD_CONST              11 ('ENVIRONMENT == "development"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L7)
               NOT_TAKEN
               POP_TOP

392            LOAD_CONST              12 ("ENVIRONMENT == 'development'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

390    L7:     STORE_FAST               5 (wildcard_guarded)

394            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

395            LOAD_CONST              13 ('cors:wildcard_guarded')

396            LOAD_FAST_BORROW         5 (wildcard_guarded)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               7 ('FAIL')

397    L9:     LOAD_CONST              14 ("Wildcard '*' CORS is gated on ENVIRONMENT == 'development'")

398            LOAD_FAST_BORROW         5 (wildcard_guarded)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              15 ("expected literal ENVIRONMENT == 'development' guard")

394   L11:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

402            LOAD_CONST              16 ('settings.BASE_URL')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              17 ('settings.CORS_ORIGINS')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

401   L12:     STORE_FAST               6 (origins_from_settings)

404            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

405            LOAD_CONST              18 ('cors:origins_from_settings')

406            LOAD_FAST_BORROW         6 (origins_from_settings)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               7 ('FAIL')

407   L14:     LOAD_CONST              19 ('Non-dev origins resolved from settings (env/config-bound)')

408            LOAD_FAST_BORROW         6 (origins_from_settings)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST              20 ('expected settings.BASE_URL or settings.CORS_ORIGINS')

404   L16:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

411            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST              21 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST              22 ('security')
               BINARY_OP               11 (/)
               LOAD_CONST              23 ('cors_policy.py')
               BINARY_OP               11 (/)
               STORE_FAST               7 (pol)

412            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         7 (pol)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L17)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
      L17:     STORE_FAST               8 (pol_src)

413            LOAD_GLOBAL              8 (REQUIRED_CORS_POLICY_TOKENS)
               GET_ITER
      L18:     FOR_ITER                73 (to L23)
               STORE_FAST               9 (tok)

414            LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (tok, pol_src)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (ok)

415            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

416            LOAD_CONST              24 ('cors_policy:')
               LOAD_FAST_BORROW         9 (tok)
               LOAD_CONST              25 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

417            LOAD_FAST_BORROW        10 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST               7 ('FAIL')

418   L20:     LOAD_CONST              26 ('cors_policy module exports ')
               LOAD_FAST_BORROW         9 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

419            LOAD_FAST_BORROW        10 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L22)
      L21:     LOAD_CONST              27 ('missing token ')
               LOAD_FAST_BORROW         9 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

415   L22:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L18)

413   L23:     END_FOR
               POP_ITER

421            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas_security_01_hardening_readiness_check.py", line 424>:
424           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_redirect_posture at 0x0000018C182DF830, file "scripts\pas_security_01_hardening_readiness_check.py", line 424>:
424            RESUME                   0

425            BUILD_LIST               0
               STORE_FAST               1 (out)

427            BUILD_LIST               0
               STORE_FAST               2 (bad)

428            LOAD_GLOBAL              1 (_iter_route_files + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               GET_ITER
       L1:     FOR_ITER               110 (to L4)
               STORE_FAST               3 (p)

429            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L2:     STORE_FAST               4 (src)

430            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

431            LOAD_CONST               1 ('RedirectResponse')
               LOAD_FAST_BORROW         5 (executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               JUMP_BACKWARD           44 (to L1)

432    L3:     LOAD_FAST_BORROW         2 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (str + NULL)
               LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               11 (relative_to + NULL|self)
               LOAD_GLOBAL             13 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               CALL                     1
               LOAD_ATTR               15 (replace + NULL|self)
               LOAD_CONST               2 ('\\')
               LOAD_CONST               3 ('/')
               CALL                     2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          112 (to L1)

428    L4:     END_FOR
               POP_ITER

433            LOAD_FAST_BORROW         2 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE      150 (to L13)
               NOT_TAKEN

436            BUILD_LIST               0
               STORE_FAST               6 (offenders)

437            LOAD_FAST_BORROW         2 (bad)
               GET_ITER
       L5:     FOR_ITER                68 (to L8)
               STORE_FAST               7 (relpath)

438            LOAD_GLOBAL             13 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         7 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               3 (p)

439            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L6:     STORE_FAST               4 (src)

440            LOAD_CONST               4 ('validate_redirect_target')
               LOAD_FAST_BORROW         4 (src)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD           51 (to L5)

441    L7:     LOAD_FAST_BORROW         6 (offenders)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         7 (relpath)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           70 (to L5)

437    L8:     END_FOR
               POP_ITER

442            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

443            LOAD_CONST               5 ('redirect:no_unguarded_redirect_response')

444            LOAD_FAST_BORROW         6 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('PASS')

445   L10:     LOAD_CONST               8 ('Any route using RedirectResponse imports validate_redirect_target')

446            LOAD_FAST_BORROW         6 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L11)
               NOT_TAKEN
               LOAD_CONST               9 ('unguarded routes: ')
               LOAD_CONST              10 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_FAST_BORROW         6 (offenders)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               0 ('')

442   L12:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_FORWARD            28 (to L14)

449   L13:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

450            LOAD_CONST              12 ('redirect:no_redirect_response_usage')

451            LOAD_CONST               7 ('PASS')

452            LOAD_CONST              13 ('No RedirectResponse usage in any app/routes/* file')

449            CALL                     3
               CALL                     1
               POP_TOP

455   L14:     LOAD_GLOBAL             13 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST              14 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST              15 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST              16 ('security')
               BINARY_OP               11 (/)
               LOAD_CONST              17 ('redirect_validation.py')
               BINARY_OP               11 (/)
               STORE_FAST               8 (rv)

456            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         8 (rv)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
      L15:     STORE_FAST               9 (rv_src)

457            LOAD_GLOBAL             20 (REQUIRED_REDIRECT_TOKENS)
               GET_ITER
      L16:     FOR_ITER                73 (to L21)
               STORE_FAST              10 (tok)

458            LOAD_FAST_BORROW_LOAD_FAST_BORROW 169 (tok, rv_src)
               CONTAINS_OP              0 (in)
               STORE_FAST              11 (ok)

459            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

460            LOAD_CONST              18 ('redirect_validation:')
               LOAD_FAST_BORROW        10 (tok)
               LOAD_CONST              19 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

461            LOAD_FAST_BORROW        11 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               6 ('FAIL')

462   L18:     LOAD_CONST              20 ('redirect_validation module exports ')
               LOAD_FAST_BORROW        10 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

463            LOAD_FAST_BORROW        11 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               0 ('')
               JUMP_FORWARD             4 (to L20)
      L19:     LOAD_CONST              21 ('missing token ')
               LOAD_FAST_BORROW        10 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

459   L20:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L16)

457   L21:     END_FOR
               POP_ITER

465            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas_security_01_hardening_readiness_check.py", line 468>:
468           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_storage_posture at 0x0000018C182DFCC0, file "scripts\pas_security_01_hardening_readiness_check.py", line 468>:
 468            RESUME                   0

 469            BUILD_LIST               0
                STORE_FAST               1 (out)

 473            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                STORE_FAST               2 (app_dir)

 474            LOAD_FAST_BORROW         2 (app_dir)
                LOAD_ATTR                3 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        31 (to L1)
                NOT_TAKEN

 475            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 476            LOAD_CONST               1 ('storage:no_app_dir')

 477            LOAD_CONST               2 ('PASS')

 478            LOAD_CONST               3 ('No app/ directory — storage scan trivially clean')

 475            CALL                     3
                CALL                     1
                POP_TOP

 480            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 481    L1:     BUILD_LIST               0
                STORE_FAST               3 (hits)

 482            LOAD_FAST_BORROW         2 (app_dir)
                LOAD_ATTR                9 (rglob + NULL|self)
                LOAD_CONST               4 ('*.py')
                CALL                     1
                GET_ITER
        L2:     FOR_ITER               118 (to L8)
                STORE_FAST               4 (p)

 483            NOP

 484    L3:     LOAD_FAST_BORROW         4 (p)
                LOAD_ATTR               11 (read_text + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 ('replace')
                LOAD_CONST               7 (('encoding', 'errors'))
                CALL_KW                  2
                STORE_FAST               5 (src)

 487    L4:     LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST                5 (src)
                CALL                     1
                STORE_FAST               6 (executable)

 488            LOAD_CONST              24 (('supabase.storage', 'storage.from_(', '.create_bucket('))
                GET_ITER
        L5:     FOR_ITER                78 (to L7)
                STORE_FAST               7 (marker)

 489            LOAD_FAST_LOAD_FAST    118 (marker, executable)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 490    L6:     LOAD_FAST                3 (hits)
                LOAD_ATTR                5 (append + NULL|self)

 491            LOAD_GLOBAL             17 (str + NULL)
                LOAD_FAST                4 (p)
                LOAD_ATTR               19 (relative_to + NULL|self)
                LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST                0 (repo_root)
                CALL                     1
                CALL                     1
                CALL                     1
                LOAD_ATTR               21 (replace + NULL|self)
                LOAD_CONST               8 ('\\')
                LOAD_CONST               9 ('/')
                CALL                     2

 490            CALL                     1
                POP_TOP

 493            POP_TOP
                JUMP_BACKWARD          116 (to L2)

 488    L7:     END_FOR
                POP_ITER
                JUMP_BACKWARD          120 (to L2)

 482    L8:     END_FOR
                POP_ITER

 494            LOAD_FAST_BORROW         3 (hits)
                TO_BOOL
                POP_JUMP_IF_FALSE      171 (to L15)
                NOT_TAKEN

 495            LOAD_GLOBAL             23 (_read_text + NULL)

 496            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST              10 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST              11 ('pas_security_01_defensive_hardening_audit.md')
                BINARY_OP               11 (/)

 495            CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP

 497            LOAD_CONST              12 ('')

 495    L9:     STORE_FAST               8 (doc)

 498            LOAD_FAST_BORROW         8 (doc)
                LOAD_ATTR               25 (lower + NULL|self)
                CALL                     0
                STORE_FAST               9 (doc_lower)

 500            LOAD_CONST              13 ('storage / rls posture')
                LOAD_FAST_BORROW         9 (doc_lower)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L10)
                NOT_TAKEN
                POP_TOP

 501            LOAD_CONST              14 ('storage posture')
                LOAD_FAST_BORROW         9 (doc_lower)
                CONTAINS_OP              0 (in)

 499   L10:     STORE_FAST              10 (documented)

 503            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 504            LOAD_CONST              15 ('storage:usage_documented')

 505            LOAD_FAST_BORROW        10 (documented)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               2 ('PASS')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              16 ('FAIL')

 506   L12:     LOAD_CONST              17 ('Supabase storage usage is documented in PAS-SECURITY-01 doctrine')

 509            LOAD_FAST_BORROW        10 (documented)
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L13)
                NOT_TAKEN

 508            LOAD_CONST              18 ('files using storage: ')
                LOAD_CONST              19 (', ')
                LOAD_ATTR               27 (join + NULL|self)
                LOAD_GLOBAL             29 (sorted + NULL)
                LOAD_GLOBAL             31 (set + NULL)
                LOAD_FAST_BORROW         3 (hits)
                CALL                     1
                CALL                     1
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L14)

 509   L13:     LOAD_CONST              12 ('')

 503   L14:     LOAD_CONST              20 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 519            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 513   L15:     LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 514            LOAD_CONST              21 ('storage:unused')

 515            LOAD_CONST               2 ('PASS')

 516            LOAD_CONST              22 ('No supabase storage usage detected — unused posture')

 517            LOAD_GLOBAL             32 (SEVERITY_INFO)

 513            LOAD_CONST              23 (('severity',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 519            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 485            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L18)
                NOT_TAKEN
                POP_TOP

 486   L17:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          351 (to L2)

 485   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L16 [1]
  L16 to L17 -> L19 [2] lasti
  L18 to L19 -> L19 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114300, file "scripts\pas_security_01_hardening_readiness_check.py", line 522>:
522           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_public_raw_exception at 0x0000018C17F77EF0, file "scripts\pas_security_01_hardening_readiness_check.py", line 522>:
522            RESUME                   0

527            BUILD_LIST               0
               STORE_FAST               1 (out)

528            BUILD_LIST               0
               STORE_FAST               2 (bad)

529            LOAD_GLOBAL              1 (_iter_route_files + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               GET_ITER
       L1:     FOR_ITER               147 (to L8)
               STORE_FAST               3 (p)

532            LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR                2 (name)
               LOAD_CONST               1 ('system.py')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

533            JUMP_BACKWARD           22 (to L1)

534    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L3:     STORE_FAST               4 (src)

535            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         4 (src)
               CALL                     1
               STORE_FAST               5 (executable)

536            LOAD_GLOBAL              8 (FORBIDDEN_RAW_EXCEPTION_PATTERNS)
               GET_ITER
       L4:     FOR_ITER                83 (to L7)
               STORE_FAST               6 (pat)

540            LOAD_FAST_BORROW         6 (pat)
               LOAD_CONST               3 ('return JSONResponse({')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN

541            JUMP_BACKWARD           12 (to L4)

542    L5:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 101 (pat, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           20 (to L4)

543    L6:     LOAD_FAST_BORROW         2 (bad)
               LOAD_ATTR               11 (append + NULL|self)

544            LOAD_FAST_BORROW         3 (p)
               LOAD_ATTR               13 (relative_to + NULL|self)
               LOAD_GLOBAL             15 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST               4 (':')
               LOAD_FAST_BORROW         6 (pat)
               FORMAT_SIMPLE
               BUILD_STRING             3
               LOAD_ATTR               17 (replace + NULL|self)
               LOAD_CONST               5 ('\\')
               LOAD_CONST               6 ('/')
               CALL                     2

543            CALL                     1
               POP_TOP

546            POP_TOP
               JUMP_BACKWARD          145 (to L1)

536    L7:     END_FOR
               POP_ITER
               JUMP_BACKWARD          149 (to L1)

529    L8:     END_FOR
               POP_ITER

547            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

548            LOAD_CONST               7 ('errors:no_public_raw_exception')

549            LOAD_FAST_BORROW         2 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               9 ('PASS')

550   L10:     LOAD_CONST              10 ('No route returns str(e) / traceback.format_exc() in a public response')

551            LOAD_FAST_BORROW         2 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L11)
               NOT_TAKEN
               LOAD_CONST              11 ('offenders: ')
               LOAD_CONST              12 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         2 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               2 ('')

547   L12:     LOAD_CONST              13 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

553            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 556>:
556           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_error_safety_module at 0x0000018C17FEE030, file "scripts\pas_security_01_hardening_readiness_check.py", line 556>:
556           RESUME                   0

557           BUILD_LIST               0
              STORE_FAST               1 (out)

558           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('security')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('error_safety.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

559           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

560           LOAD_GLOBAL              4 (REQUIRED_ERROR_SAFETY_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

561           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

562           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

563           LOAD_CONST               5 ('error_safety:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

564           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

565   L4:     LOAD_CONST               9 ('error_safety module exports ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

566           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

562   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

560   L7:     END_FOR
              POP_ITER

568           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas_security_01_hardening_readiness_check.py", line 571>:
571           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_webhook_signatures at 0x0000018C17ED9FB0, file "scripts\pas_security_01_hardening_readiness_check.py", line 571>:
571            RESUME                   0

572            BUILD_LIST               0
               STORE_FAST               1 (out)

574            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('twilio_webhook.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

575            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

577            LOAD_CONST               4 ('RequestValidator')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L2)
               NOT_TAKEN
               POP_TOP

578            LOAD_CONST               5 ('X-Twilio-Signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

577            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L2)
               NOT_TAKEN
               POP_TOP

579            LOAD_CONST               6 ('Invalid Twilio signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

576    L2:     STORE_FAST               4 (tw_ok)

581            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

582            LOAD_CONST               7 ('webhook:twilio_signature_verified')

583            LOAD_FAST_BORROW         4 (tw_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               8 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               9 ('FAIL')

584    L4:     LOAD_CONST              10 ('Twilio webhook verifies HMAC signature and rejects 403 on failure')

585            LOAD_FAST_BORROW         4 (tw_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST              11 ('missing RequestValidator / signature check')

581    L6:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

588            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST              13 ('email_ingestion.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

589            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L7:     STORE_FAST               3 (src)

591            LOAD_CONST              14 ('forwarder_signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L8)
               NOT_TAKEN
               POP_TOP

592            LOAD_CONST              15 ('verify_hmac')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

591            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L8)
               NOT_TAKEN
               POP_TOP

593            LOAD_CONST              16 ('forwarder_secret')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

590    L8:     STORE_FAST               5 (em_ok)

595            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

596            LOAD_CONST              17 ('webhook:email_ingestion_signature_posture')

597            LOAD_FAST_BORROW         5 (em_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               9 ('FAIL')

598   L10:     LOAD_CONST              18 ('Email ingestion route has a signature/secret verification posture')

599            LOAD_FAST_BORROW         5 (em_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              19 ('missing signature posture markers')

595   L12:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

602            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST              20 ('slack_command.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

603            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
      L13:     STORE_FAST               3 (src)

605            LOAD_CONST              21 ('X-Slack-Signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        73 (to L14)
               NOT_TAKEN
               POP_TOP

606            LOAD_CONST              22 ('X-Slack-Request-Timestamp')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

605            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        60 (to L14)
               NOT_TAKEN
               POP_TOP

607            LOAD_CONST              23 ('slack_signing_secret')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)

605            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        33 (to L14)
               NOT_TAKEN
               POP_TOP

608            LOAD_CONST              24 ('verify_slack_signature')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

605            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L14)
               NOT_TAKEN
               POP_TOP

609            LOAD_CONST              25 ('slack_signature')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)

604   L14:     STORE_FAST               6 (sl_ok)

611            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

612            LOAD_CONST              26 ('webhook:slack_signature_posture')

613            LOAD_FAST_BORROW         6 (sl_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               8 ('PASS')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               9 ('FAIL')

614   L16:     LOAD_CONST              27 ('Slack command route has a signing-secret verification posture')

615            LOAD_FAST_BORROW         6 (sl_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST              28 ('missing Slack signature markers')

611   L18:     LOAD_CONST              12 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

617            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts\pas_security_01_hardening_readiness_check.py", line 620>:
620           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_server_side_permissions at 0x0000018C17EA7750, file "scripts\pas_security_01_hardening_readiness_check.py", line 620>:
620            RESUME                   0

635            BUILD_LIST               0
               STORE_FAST               1 (out)

637            BUILD_SET                0
               LOAD_CONST              23 (frozenset({'demo.py', 'simulate.py', 'onboarding.py'}))
               SET_UPDATE               1
               STORE_FAST               2 (documented_public_files)

647            BUILD_SET                0
               LOAD_CONST              24 (frozenset({'slack_command.py', 'websocket_handler.py', 'twilio_webhook.py'}))
               SET_UPDATE               1
               STORE_FAST               3 (allowed_signature_files)

652            BUILD_LIST               0
               STORE_FAST               4 (offenders)

653            LOAD_GLOBAL              1 (_iter_route_files + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               316 (to L11)
               STORE_FAST               5 (p)

654            LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR                2 (name)
               LOAD_FAST_BORROW         3 (allowed_signature_files)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        18 (to L2)
               NOT_TAKEN
               LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR                2 (name)
               LOAD_FAST_BORROW         2 (documented_public_files)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

655    L2:     JUMP_BACKWARD           40 (to L1)

656    L3:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         5 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L4:     STORE_FAST               6 (src)

657            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         6 (src)
               CALL                     1
               STORE_FAST               7 (executable)

663            LOAD_CONST               2 ('Header(')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L5)
               NOT_TAKEN
               POP_TOP

665            LOAD_CONST               3 ('get_brokerage_by_api_key')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L5)
               NOT_TAKEN
               POP_TOP

666            LOAD_CONST               4 ('ADMIN_API_KEY')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              0 (in)

662    L5:     STORE_FAST               8 (file_has_inline_auth)

669            LOAD_FAST_BORROW         8 (file_has_inline_auth)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

670            JUMP_BACKWARD          113 (to L1)

672    L6:     LOAD_SMALL_INT           0
               STORE_FAST               9 (i)

673    L7:     NOP

674            LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR                9 (find + NULL|self)
               LOAD_CONST               5 ('@router.post(')
               LOAD_FAST_BORROW         9 (i)
               CALL                     2
               STORE_FAST               9 (i)

675            LOAD_FAST_BORROW         9 (i)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN

676            JUMP_BACKWARD          143 (to L1)

679    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 121 (executable, i)
               LOAD_FAST_BORROW         9 (i)
               LOAD_CONST               6 (800)
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST              10 (window)

681            LOAD_CONST               7 ('Depends(require_brokerage')
               LOAD_FAST_BORROW        10 (window)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        45 (to L9)
               NOT_TAKEN
               POP_TOP

682            LOAD_CONST               8 ('Depends(require_admin')
               LOAD_FAST_BORROW        10 (window)
               CONTAINS_OP              0 (in)

681            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        32 (to L9)
               NOT_TAKEN
               POP_TOP

683            LOAD_CONST               9 ('require_brokerage(')
               LOAD_FAST_BORROW        10 (window)
               CONTAINS_OP              0 (in)

681            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        19 (to L9)
               NOT_TAKEN
               POP_TOP

684            LOAD_CONST              10 ('require_admin(')
               LOAD_FAST_BORROW        10 (window)
               CONTAINS_OP              0 (in)

681            COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L9)
               NOT_TAKEN
               POP_TOP

685            LOAD_CONST               2 ('Header(')
               LOAD_FAST_BORROW        10 (window)
               CONTAINS_OP              0 (in)

680    L9:     STORE_FAST              11 (has_auth)

687            LOAD_FAST_BORROW        11 (has_auth)
               TO_BOOL
               POP_JUMP_IF_TRUE        90 (to L10)
               NOT_TAKEN

689            LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR                9 (find + NULL|self)
               LOAD_CONST              11 (')')
               LOAD_FAST_BORROW         9 (i)
               CALL                     2
               STORE_FAST              12 (eo)

690            LOAD_FAST_BORROW         4 (offenders)
               LOAD_ATTR               11 (append + NULL|self)

691            LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR               13 (relative_to + NULL|self)
               LOAD_GLOBAL             15 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               FORMAT_SIMPLE
               LOAD_CONST              12 (':')
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 121 (executable, i)
               LOAD_FAST_BORROW        12 (eo)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               BINARY_SLICE
               FORMAT_SIMPLE
               BUILD_STRING             3
               LOAD_ATTR               17 (replace + NULL|self)
               LOAD_CONST              13 ('\\')
               LOAD_CONST              14 ('/')
               CALL                     2

690            CALL                     1
               POP_TOP

693   L10:     LOAD_FAST_BORROW         9 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               9 (i)
               JUMP_BACKWARD          204 (to L7)

653   L11:     END_FOR
               POP_ITER

694            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

695            LOAD_CONST              15 ('auth:server_side_post_routes_gated')

696            LOAD_FAST_BORROW         4 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              16 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              17 ('PASS')

697   L13:     LOAD_CONST              18 ('Every @router.post in app/routes/* is auth-gated (Depends or inline Header + validation or signature verifier)')

698            LOAD_FAST_BORROW         4 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L14)
               NOT_TAKEN
               LOAD_CONST              19 ('unguarded routes: ')
               LOAD_CONST              20 (' | ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         4 (offenders)
               LOAD_CONST              21 (slice(None, 10, None))
               BINARY_OP               26 ([])
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               1 ('')

694   L15:     LOAD_CONST              22 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

700            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 703>:
703           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_brokerage_id_body_trust at 0x0000018C17D7C560, file "scripts\pas_security_01_hardening_readiness_check.py", line 703>:
703            RESUME                   0

706            BUILD_LIST               0
               STORE_FAST               1 (out)

707            BUILD_LIST               0
               STORE_FAST               2 (offenders)

708            LOAD_CONST              20 (('tenant_portal.py', 'tenant_learning.py', 'tenant_learning_tests.py', 'portal.py'))
               STORE_FAST               3 (tenant_route_files)

714            LOAD_FAST_BORROW         3 (tenant_route_files)
               GET_ITER
       L1:     FOR_ITER               215 (to L9)
               STORE_FAST               4 (name)

715            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('routes')
               BINARY_OP               11 (/)
               LOAD_FAST_BORROW         4 (name)
               BINARY_OP               11 (/)
               STORE_FAST               5 (p)

716            LOAD_FAST_BORROW         5 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

717            JUMP_BACKWARD           59 (to L1)

718    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         5 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L3:     STORE_FAST               6 (src)

719            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         6 (src)
               CALL                     1
               STORE_FAST               7 (executable)

723            LOAD_FAST_BORROW         7 (executable)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               104 (to L8)
               STORE_FAST               8 (line)

724            LOAD_FAST_BORROW         8 (line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               9 (stripped)

725            LOAD_FAST_BORROW         9 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN

726            JUMP_BACKWARD           29 (to L4)

728    L5:     LOAD_CONST               4 ('brokerage_id: str')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        24 (to L6)
               NOT_TAKEN

729            LOAD_CONST               5 ('brokerage_id:str')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        17 (to L6)
               NOT_TAKEN

730            LOAD_CONST               6 ('brokerage_id = Query(')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        10 (to L6)
               NOT_TAKEN

731            LOAD_CONST               7 ('brokerage_id = Path(')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           59 (to L4)

738    L6:     LOAD_CONST               8 ('Body(')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        17 (to L7)
               NOT_TAKEN

739            LOAD_CONST               9 ('Query(')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE        10 (to L7)
               NOT_TAKEN

740            LOAD_CONST              10 ('Path(')
               LOAD_FAST_BORROW         9 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               JUMP_BACKWARD           82 (to L4)

742    L7:     LOAD_FAST_BORROW         2 (offenders)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         4 (name)
               FORMAT_SIMPLE
               LOAD_CONST              11 (': ')
               LOAD_FAST_BORROW         9 (stripped)
               FORMAT_SIMPLE
               BUILD_STRING             3
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          106 (to L4)

723    L8:     END_FOR
               POP_ITER
               JUMP_BACKWARD          217 (to L1)

714    L9:     END_FOR
               POP_ITER

743            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

744            LOAD_CONST              12 ('auth:no_brokerage_id_body_trust')

745            LOAD_FAST_BORROW         2 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST              13 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              14 ('PASS')

746   L11:     LOAD_CONST              15 ('Tenant routes do not declare brokerage_id as a URL/body parameter')

747            LOAD_FAST_BORROW         2 (offenders)
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L12)
               NOT_TAKEN
               LOAD_CONST              16 ('offenders: ')
               LOAD_CONST              17 (' | ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         2 (offenders)
               LOAD_CONST              18 (slice(None, 10, None))
               BINARY_OP               26 ([])
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               3 ('')

743   L13:     LOAD_CONST              19 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

749            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 752>:
752           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_dependency_pinning at 0x0000018C17F631E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 752>:
752           RESUME                   0

753           BUILD_LIST               0
              STORE_FAST               1 (out)

754           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('requirements.txt')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

755           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               3 (src)

756           BUILD_LIST               0
              STORE_FAST               4 (bad)

757           LOAD_GLOBAL              4 (PINNED_DEPENDENCIES)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               5 (pkg)

758           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (pkg, src)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

759   L3:     LOAD_FAST_BORROW         4 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         5 (pkg)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

757   L4:     END_FOR
              POP_ITER

760           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

761           LOAD_CONST               2 ('deps:pinned_versions_present')

762           LOAD_FAST_BORROW         4 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               3 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               4 ('PASS')

763   L6:     LOAD_CONST               5 ('requirements.txt pins fastapi / supabase / cryptography / httpx / pydantic-settings / twilio / anthropic / openai')

764           LOAD_FAST_BORROW         4 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST               6 ('missing pins: ')
              LOAD_CONST               7 (', ')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         4 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               1 ('')

760   L8:     LOAD_CONST               8 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

771           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

772           LOAD_CONST               9 ('deps:scanner_unavailable_documented')

773           LOAD_CONST               4 ('PASS')

774           LOAD_CONST              10 ('Vulnerability scanner posture documented (out-of-band)')

775           LOAD_GLOBAL             12 (SEVERITY_INFO)

771           LOAD_CONST              11 (('severity',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

777           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas_security_01_hardening_readiness_check.py", line 780>:
780           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_rate_limit_posture at 0x0000018C17EF9A30, file "scripts\pas_security_01_hardening_readiness_check.py", line 780>:
780            RESUME                   0

781            BUILD_LIST               0
               STORE_FAST               1 (out)

783            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('utils')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('rate_limiter.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

784            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

786            LOAD_CONST               4 ('def rate_limit(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       32 (to L2)
               NOT_TAKEN
               POP_TOP

787            LOAD_CONST               5 ('def client_ip(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

786            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       19 (to L2)
               NOT_TAKEN
               POP_TOP

788            LOAD_CONST               6 ('HTTPException(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

786            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L2)
               NOT_TAKEN
               POP_TOP

789            LOAD_CONST               7 ('429')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

785    L2:     STORE_FAST               4 (rate_module_ok)

791            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

792            LOAD_CONST               8 ('rate_limit:module_present')

793            LOAD_FAST_BORROW         4 (rate_module_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               9 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST              10 ('FAIL')

794    L4:     LOAD_CONST              11 ('app/utils/rate_limiter.py exports rate_limit + client_ip')

795            LOAD_FAST_BORROW         4 (rate_module_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_CONST              12 ('missing module helpers or 429 raise')

791    L6:     LOAD_CONST              13 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

800            LOAD_CONST              26 ((('app/routes/twilio_webhook.py', 'twilio'), ('app/routes/outbound.py', 'outbound'), ('app/routes/simulate.py', 'simulate')))
               GET_ITER
       L7:     FOR_ITER               105 (to L13)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   86 (relpath, key)

805            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         5 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

806            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L8:     STORE_FAST               3 (src)

807            LOAD_CONST              14 ('rate_limit(')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (ok)

808            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

809            LOAD_CONST              15 ('rate_limit:applied:')
               LOAD_FAST_BORROW         6 (key)
               FORMAT_SIMPLE
               BUILD_STRING             2

810            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               9 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST              10 ('FAIL')

811   L10:     LOAD_FAST_BORROW         5 (relpath)
               FORMAT_SIMPLE
               LOAD_CONST              16 (' calls rate_limit(...)')
               BUILD_STRING             2

812            LOAD_FAST_BORROW         7 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              17 ('missing rate_limit call')

808   L12:     LOAD_CONST              13 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          107 (to L7)

800   L13:     END_FOR
               POP_ITER

816            LOAD_GLOBAL              3 (_read_text + NULL)

817            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST              18 ('docs')
               BINARY_OP               11 (/)
               LOAD_CONST              19 ('pas_security_01_defensive_hardening_audit.md')
               BINARY_OP               11 (/)

816            CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L14)
               NOT_TAKEN
               POP_TOP

818            LOAD_CONST               3 ('')

816   L14:     STORE_FAST               8 (doc)

819            LOAD_FAST_BORROW         8 (doc)
               LOAD_ATTR                9 (lower + NULL|self)
               CALL                     0
               STORE_FAST               9 (doc_lower)

821            LOAD_CONST              20 ('rate-limit posture')
               LOAD_FAST_BORROW         9 (doc_lower)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L15)
               NOT_TAKEN
               POP_TOP

822            LOAD_CONST              21 ('documented gap')
               LOAD_FAST_BORROW         9 (doc_lower)
               CONTAINS_OP              0 (in)

820   L15:     STORE_FAST              10 (gap_documented)

824            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

825            LOAD_CONST              22 ('rate_limit:gap_documented')

826            LOAD_FAST_BORROW        10 (gap_documented)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               9 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST              10 ('FAIL')

827   L17:     LOAD_CONST              23 ('Doctrine doc documents the rate-limit gap (email-ingestion / admin / slack)')

828            LOAD_FAST_BORROW        10 (gap_documented)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST              24 ("missing 'rate-limit posture' + 'documented gap' phrasing")

829   L19:     LOAD_GLOBAL             10 (SEVERITY_INFO)

824            LOAD_CONST              25 (('detail', 'severity'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

831            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas_security_01_hardening_readiness_check.py", line 834>:
834           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_session_token_posture at 0x0000018C17F76200, file "scripts\pas_security_01_hardening_readiness_check.py", line 834>:
 834            RESUME                   0

 835            BUILD_LIST               0
                STORE_FAST               1 (out)

 837            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('operator')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('operator_actions.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 838            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_FAST               3 (src)

 839            LOAD_FAST_BORROW         3 (src)
                TO_BOOL
                POP_JUMP_IF_TRUE       114 (to L7)
                NOT_TAKEN

 841            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('operator')
                BINARY_OP               11 (/)
                STORE_FAST               4 (p_alt)

 842            LOAD_CONST               5 (False)
                STORE_FAST               5 (rotate_present)

 843            LOAD_FAST_BORROW         4 (p_alt)
                LOAD_ATTR                5 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       57 (to L6)
                NOT_TAKEN

 844            LOAD_FAST_BORROW         4 (p_alt)
                LOAD_ATTR                7 (glob + NULL|self)
                LOAD_CONST               6 ('*.py')
                CALL                     1
                GET_ITER
        L2:     FOR_ITER                35 (to L5)
                STORE_FAST               6 (f)

 845            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         6 (f)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L3:     STORE_FAST               7 (t)

 846            LOAD_CONST               7 ('rotate_brokerage_api_key')
                LOAD_FAST_BORROW         7 (t)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           33 (to L2)

 847    L4:     LOAD_CONST               8 (True)
                STORE_FAST               5 (rotate_present)

 848            POP_TOP
                JUMP_FORWARD             8 (to L8)

 844    L5:     END_FOR
                POP_ITER

  --    L6:     JUMP_FORWARD             5 (to L8)

 850    L7:     LOAD_CONST               7 ('rotate_brokerage_api_key')
                LOAD_FAST_BORROW         3 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (rotate_present)

 851    L8:     LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 852            LOAD_CONST               9 ('session:api_key_rotation_present')

 853            LOAD_FAST_BORROW         5 (rotate_present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_CONST              10 ('PASS')
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              11 ('FAIL')

 854   L10:     LOAD_CONST              12 ('Operator-driven rotate_brokerage_api_key action is implemented (PAS175)')

 855            LOAD_FAST_BORROW         5 (rotate_present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_CONST              13 ('rotate_brokerage_api_key not found in operator services')

 851   L12:     LOAD_CONST              14 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 858            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST              15 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST              16 ('rotate_email_forwarder_secret.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 859            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 860            LOAD_CONST              17 ('session:email_forwarder_rotation_script')

 861            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR               13 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST              10 ('PASS')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST              11 ('FAIL')

 862   L14:     LOAD_CONST              18 ('Email forwarder secret rotation script is present (PAS168)')

 863            LOAD_FAST_BORROW         2 (p)
                LOAD_ATTR               13 (is_file + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               4 ('')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST              19 ('missing scripts/rotate_email_forwarder_secret.py')

 859   L16:     LOAD_CONST              14 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 865            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts\pas_security_01_hardening_readiness_check.py", line 868>:
868           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_audit_service_invariant at 0x0000018C17D76780, file "scripts\pas_security_01_hardening_readiness_check.py", line 868>:
868           RESUME                   0

871           BUILD_LIST               0
              STORE_FAST               1 (out)

872           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               1 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               4 ('audit_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

873           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

874           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

882           BUILD_LIST               0
              STORE_FAST               5 (bad)

883           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

884           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

885   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

883   L4:     END_FOR
              POP_ITER

886           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

887           LOAD_CONST               6 ('audit_service:append_only_carry')

888           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

889   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

890           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L7)
              NOT_TAKEN
              LOAD_CONST              10 ('disqualifying tokens: ')
              LOAD_CONST              11 (', ')
              LOAD_ATTR                9 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L8)
      L7:     LOAD_CONST               5 ('')

886   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

892           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas_security_01_hardening_readiness_check.py", line 895>:
895           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_event_contract at 0x0000018C1801C9E0, file "scripts\pas_security_01_hardening_readiness_check.py", line 895>:
895           RESUME                   0

896           BUILD_LIST               0
              STORE_FAST               1 (out)

897           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('events')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('contract.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

898           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

899           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

900           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

901           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

902           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

903           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

904   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

905           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             5 (to L6)
      L5:     LOAD_CONST               9 ('missing event type ')
              LOAD_FAST_BORROW         4 (required)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

901   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

899   L7:     END_FOR
              POP_ITER

907           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts\pas_security_01_hardening_readiness_check.py", line 910>:
910           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17EA5700, file "scripts\pas_security_01_hardening_readiness_check.py", line 910>:
910            RESUME                   0

911            BUILD_LIST               0
               STORE_FAST               1 (out)

912            LOAD_CONST              10 (('app/services/security/__init__.py', 'app/services/security/cors_policy.py', 'app/services/security/redirect_validation.py', 'app/services/security/error_safety.py', 'scripts/pas_security_01_hardening_readiness_check.py'))
               STORE_FAST               2 (files)

919            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

920            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

921            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

922            JUMP_BACKWARD           46 (to L1)

923    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

924            BUILD_LIST               0
               STORE_FAST               6 (bad)

925            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

926            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

927            LOAD_FAST_BORROW         8 (stripped)
               TO_BOOL
               POP_JUMP_IF_FALSE       24 (to L5)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_CONST               2 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN

928    L5:     JUMP_BACKWARD           52 (to L4)

929    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

930            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

931    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

929    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

925   L10:     END_FOR
               POP_ITER

932            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

933            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

934            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

935   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

937            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

936            LOAD_CONST               7 ('forbidden import prefixes: ')
               LOAD_CONST               8 (', ')
               LOAD_ATTR               19 (join + NULL|self)
               LOAD_GLOBAL             21 (sorted + NULL)
               LOAD_GLOBAL             23 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

937   L13:     LOAD_CONST               1 ('')

932   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

919   L15:     END_FOR
               POP_ITER

939            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts\pas_security_01_hardening_readiness_check.py", line 942>:
942           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC1CE0, file "scripts\pas_security_01_hardening_readiness_check.py", line 942>:
942            RESUME                   0

943            BUILD_LIST               0
               STORE_FAST               1 (out)

944            LOAD_CONST               9 (('app/services/security/cors_policy.py', 'app/services/security/redirect_validation.py', 'app/services/security/error_safety.py'))
               STORE_FAST               2 (files)

949            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

950            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

951            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

952            JUMP_BACKWARD           45 (to L1)

953    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

954            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

955            BUILD_LIST               0
               STORE_FAST               7 (bad)

956            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

957            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

958    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

956    L6:     END_FOR
               POP_ITER

959            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

960            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

961            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

962    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

964            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

963            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

964    L9:     LOAD_CONST               1 ('')

959   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

949   L11:     END_FOR
               POP_ITER

966            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas_security_01_hardening_readiness_check.py", line 969>:
969           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('repo_root')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD1ED0, file "scripts\pas_security_01_hardening_readiness_check.py", line 969>:
  --            MAKE_CELL                8 (lower)

 969            RESUME                   0

 970            BUILD_LIST               0
                STORE_FAST               1 (out)

 971            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas_security_01_defensive_hardening_audit.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 972            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 973            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 974            LOAD_CONST              13 ((('purpose', ('purpose',)), ('cors-posture', ('cors posture',)), ('redirect-posture', ('redirect posture',)), ('storage-posture', ('storage / rls posture', 'storage posture')), ('debug-leakage', ('debug / log leakage posture', 'debug / log leakage', 'log leakage posture')), ('webhook-signature', ('webhook signature posture', 'webhook signature')), ('server-side', ('server-side permission posture', 'server-side permission')), ('dependency-audit', ('dependency audit posture', 'dependency audit')), ('rate-limit', ('rate-limit posture', 'rate-limit')), ('raw-error', ('raw error exposure posture', 'raw error exposure')), ('session-token', ('session / token expiry posture', 'session/token expiry', 'session / token expiry')), ('no-gmail', ('no gmail', 'no autonomous remediation')), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not', 'deliberately does not build')), ('limitations', ('limitation',))))
                STORE_FAST               4 (required_phrases)

1004            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

1005            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas_security_01_hardening_readiness_check.py", line 1005>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
        L3:     FOR_ITER                12 (to L5)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L4:     POP_ITER
                LOAD_CONST               4 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST               5 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025C30, file "scripts\pas_security_01_hardening_readiness_check.py", line 1005>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

1006            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

1007            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

1008            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

1009    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

1011            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

1010            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

1011   L10:     LOAD_CONST               2 ('')

1006   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

1004   L12:     END_FOR
                POP_ITER

1013            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025C30, file "scripts\pas_security_01_hardening_readiness_check.py", line 1005>:
  --           COPY_FREE_VARS           1

1005           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_DEREF               2 (lower)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts\pas_security_01_hardening_readiness_check.py", line 1016>:
1016           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('repo_root')
               LOAD_CONST               2 ('str')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('List[dict]')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D893A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1016>:
1016            RESUME                   0

1017            BUILD_LIST               0
                STORE_FAST               1 (out)

1018            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_GLOBAL              2 (__file__)
                CALL                     1
                LOAD_ATTR                5 (resolve + NULL|self)
                CALL                     0
                STORE_FAST               2 (self_path)

1019            LOAD_GLOBAL              7 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (self_path)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               0 ('')
        L1:     STORE_FAST               3 (src)

1020            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               4 (executable)

1021            BUILD_LIST               0
                STORE_FAST               5 (bad)

1022            LOAD_FAST_BORROW         4 (executable)
                LOAD_ATTR               11 (splitlines + NULL|self)
                CALL                     0
                GET_ITER
        L2:     FOR_ITER               199 (to L9)
                STORE_FAST               6 (raw_line)

1023            LOAD_FAST_BORROW         6 (raw_line)
                LOAD_ATTR               13 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (stripped)

1024            LOAD_FAST_BORROW         7 (stripped)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

1025            JUMP_BACKWARD           29 (to L2)

1026    L3:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              15 (('import dotenv', 'from dotenv'))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L4)
                NOT_TAKEN

1027            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               1 ('dotenv import')
                CALL                     1
                POP_TOP

1028    L4:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              16 (('import supabase', 'from supabase'))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L5)
                NOT_TAKEN

1029            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               2 ('supabase import')
                CALL                     1
                POP_TOP

1030    L5:     LOAD_CONST               3 ('load_dotenv()')
                LOAD_FAST_BORROW         7 (stripped)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       18 (to L6)
                NOT_TAKEN

1031            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               4 ('load_dotenv() call')
                CALL                     1
                POP_TOP

1032    L6:     LOAD_FAST_BORROW         7 (stripped)
                LOAD_ATTR               15 (startswith + NULL|self)
                LOAD_CONST              17 (('os.environ[', 'getenv('))
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       18 (to L7)
                NOT_TAKEN

1033            LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               5 ('environ read')
                CALL                     1
                POP_TOP

1034    L7:     LOAD_CONST               6 ('get_supabase')
                LOAD_FAST_BORROW         7 (stripped)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD          182 (to L2)

1035    L8:     LOAD_FAST_BORROW         5 (bad)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_CONST               7 ('supabase client call')
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          201 (to L2)

1022    L9:     END_FOR
                POP_ITER

1036            LOAD_FAST                1 (out)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_GLOBAL             19 (_check + NULL)

1037            LOAD_CONST               8 ('self_check:no_env_or_db')

1038            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               9 ('FAIL')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              10 ('PASS')

1039   L11:     LOAD_CONST              11 ('PAS-SECURITY-01 readiness checker never reads .env / touches DB')

1040            LOAD_FAST_BORROW         5 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN
                LOAD_CONST              12 ('disqualifying patterns: ')
                LOAD_CONST              13 (', ')
                LOAD_ATTR               21 (join + NULL|self)
                LOAD_FAST_BORROW         5 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               0 ('')

1036   L13:     LOAD_CONST              14 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

1042            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1049>:
1049           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('checks')
               LOAD_CONST               2 ('List[dict]')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('dict')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1049>:
1049            RESUME                   0

1051            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

1050            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

1051    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

1052            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

1051    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

1052    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

1051    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

1050    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

1055            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

1054            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

1055   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

1056            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

1055   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

1056   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

1055   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

1054   L16:     STORE_FAST               3 (info_failures)
                STORE_FAST               1 (c)

1059            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

1060   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

1061            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info_failures)

1058            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

1050            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

1054            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1065>:
1065           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('checks')
               LOAD_CONST               2 ('List[dict]')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('List[str]')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object _operator_actions at 0x0000018C18048FF0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1065>:
1065           RESUME                   0

1066           BUILD_LIST               0
               STORE_FAST               1 (out)

1067           LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     FOR_ITER               109 (to L5)
               STORE_FAST               2 (c)

1068           LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

1069           JUMP_BACKWARD           19 (to L1)

1070   L2:     LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               2 ('severity')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         7 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_GLOBAL              2 (SEVERITY_BLOCK)
       L3:     STORE_FAST               3 (sev)

1071           LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_CONST               3 ('[')
               LOAD_FAST                3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST               4 ('] ')
               LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               5 ('id')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' — ')
               LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               7 ('detail')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               8 ('see report')
       L4:     FORMAT_SIMPLE
               LOAD_CONST               9 ('.')
               BUILD_STRING             7
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          111 (to L1)

1067   L5:     END_FOR
               POP_ITER

1072           LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115C50, file "scripts\pas_security_01_hardening_readiness_check.py", line 1075>:
1075           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('repo_root')
               LOAD_CONST               2 ('str')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('dict')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object evaluate at 0x0000018C177C5700, file "scripts\pas_security_01_hardening_readiness_check.py", line 1075>:
1075           RESUME                   0

1076           BUILD_LIST               0
               STORE_FAST               1 (checks)

1077           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              3 (check_files_present + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1078           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1079           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1080           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1081           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             11 (check_cors_posture + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1082           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             13 (check_redirect_posture + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1083           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             15 (check_storage_posture + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1084           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             17 (check_no_public_raw_exception + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1085           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             19 (check_error_safety_module + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1086           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             21 (check_webhook_signatures + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1087           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             23 (check_server_side_permissions + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1088           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             25 (check_no_brokerage_id_body_trust + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1089           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             27 (check_dependency_pinning + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1090           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             29 (check_rate_limit_posture + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1091           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             31 (check_session_token_posture + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1092           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             33 (check_audit_service_invariant + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1093           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             35 (check_event_contract + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1094           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             37 (check_no_forbidden_imports + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1095           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             39 (check_no_inbox_scan_tokens + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1096           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             41 (check_doc_required_clauses + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1097           LOAD_FAST_BORROW         1 (checks)
               LOAD_ATTR                1 (extend + NULL|self)
               LOAD_GLOBAL             43 (check_self_no_env_or_db + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               CALL                     1
               POP_TOP

1099           LOAD_GLOBAL             45 (_aggregate + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1
               STORE_FAST               2 (agg)

1101           LOAD_CONST               0 ('phase')
               LOAD_CONST               1 ('PAS-SECURITY-01')

1102           LOAD_CONST               2 ('generated_at')
               LOAD_GLOBAL             47 (_now_iso + NULL)
               CALL                     0

1103           LOAD_CONST               3 ('verdict')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])

1104           LOAD_CONST               4 ('ready')
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               3 ('verdict')
               BINARY_OP               26 ([])
               LOAD_GLOBAL             48 (VERDICT_READY)
               COMPARE_OP              72 (==)

1105           LOAD_CONST               5 ('blocker_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               6 ('blockers')
               BINARY_OP               26 ([])
               CALL                     1

1106           LOAD_CONST               7 ('info_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         2 (agg)
               LOAD_CONST               8 ('info')
               BINARY_OP               26 ([])
               CALL                     1

1107           LOAD_CONST               9 ('check_count')
               LOAD_GLOBAL             51 (len + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1108           LOAD_CONST              10 ('pass_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053090, file "scripts\pas_security_01_hardening_readiness_check.py", line 1108>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1109           LOAD_CONST              12 ('fail_count')
               LOAD_GLOBAL             53 (sum + NULL)
               LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053630, file "scripts\pas_security_01_hardening_readiness_check.py", line 1109>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (checks)
               GET_ITER
               CALL                     0
               CALL                     1

1110           LOAD_CONST              14 ('checks')
               LOAD_FAST_BORROW         1 (checks)

1111           LOAD_CONST              15 ('operator_actions')
               LOAD_GLOBAL             55 (_operator_actions + NULL)
               LOAD_FAST_BORROW         1 (checks)
               CALL                     1

1100           BUILD_MAP               11
               RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053090, file "scripts\pas_security_01_hardening_readiness_check.py", line 1108>:
1108           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('PASS')
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

Disassembly of <code object <genexpr> at 0x0000018C18053630, file "scripts\pas_security_01_hardening_readiness_check.py", line 1109>:
1109           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                22 (to L5)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
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

Disassembly of <code object __annotate__ at 0x0000018C18115D40, file "scripts\pas_security_01_hardening_readiness_check.py", line 1118>:
1118           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('return')
               LOAD_CONST               2 ('argparse.ArgumentParser')
               BUILD_MAP                1
               RETURN_VALUE

Disassembly of <code object _build_parser at 0x0000018C18128210, file "scripts\pas_security_01_hardening_readiness_check.py", line 1118>:
1118           RESUME                   0

1119           LOAD_GLOBAL              0 (argparse)
               LOAD_ATTR                2 (ArgumentParser)
               PUSH_NULL

1120           LOAD_CONST               0 ('pas_security_01_hardening_readiness_check')

1122           LOAD_CONST               1 ('PAS-SECURITY-01 — Evaluate defensive hardening posture (CORS, redirects, storage, debug leakage, webhook signatures, server-side permissions, dependency pinning, rate limits, raw error exposure, session/token expiry). Read-only — never reads .env, never touches Supabase, never runs a migration.')

1119           LOAD_CONST               2 (('prog', 'description'))
               CALL_KW                  2
               STORE_FAST               0 (p)

1131           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               3 ('--repo-root')
               LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1132           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               5 ('--output')
               LOAD_GLOBAL              8 (REPORT_FILENAME)
               LOAD_CONST               4 (('default',))
               CALL_KW                  2
               POP_TOP

1133           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               6 ('--json')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1134           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST               9 ('--summary-only')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1135           LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                5 (add_argument + NULL|self)
               LOAD_CONST              10 ('--strict')
               LOAD_CONST               7 ('store_true')
               LOAD_CONST               8 (('action',))
               CALL_KW                  2
               POP_TOP

1136           LOAD_FAST_BORROW         0 (p)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181157A0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1139>:
1139           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('report')
               LOAD_CONST               2 ('dict')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('None')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas_security_01_hardening_readiness_check.py", line 1139>:
1139           RESUME                   0

1140           LOAD_GLOBAL              1 (print + NULL)

1141           LOAD_CONST               0 ('[PAS-SECURITY-01] verdict=')
               LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               1 ('verdict')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               2 (' blockers=')

1142           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               3 ('blocker_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               4 (' info=')

1143           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               5 ('info_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               6 (' checks=')

1144           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               7 ('check_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 (' pass=')

1145           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST               9 ('pass_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST              10 (' fail=')

1146           LOAD_FAST_BORROW         0 (report)
               LOAD_CONST              11 ('fail_count')
               BINARY_OP               26 ([])
               FORMAT_SIMPLE

1141           BUILD_STRING            12

1140           CALL                     1
               POP_TOP

1148           LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              12 ('operator_actions')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L1:     STORE_FAST               1 (actions)

1149           LOAD_FAST_BORROW         1 (actions)
               TO_BOOL
               POP_JUMP_IF_FALSE       93 (to L5)
               NOT_TAKEN

1150           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('[PAS-SECURITY-01] operator actions:')
               CALL                     1
               POP_TOP

1151           LOAD_FAST_BORROW         1 (actions)
               LOAD_CONST              14 (slice(None, 25, None))
               BINARY_OP               26 ([])
               GET_ITER
       L2:     FOR_ITER                17 (to L3)
               STORE_FAST               2 (a)

1152           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              15 ('  - ')
               LOAD_FAST_BORROW         2 (a)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L2)

1151   L3:     END_FOR
               POP_ITER

1153           LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE       34 (to L4)
               NOT_TAKEN

1154           LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              16 ('  ... and ')
               LOAD_GLOBAL              5 (len + NULL)
               LOAD_FAST_BORROW         1 (actions)
               CALL                     1
               LOAD_SMALL_INT          25
               BINARY_OP               10 (-)
               FORMAT_SIMPLE
               LOAD_CONST              17 (' more (see report file)')
               BUILD_STRING             3
               CALL                     1
               POP_TOP
               LOAD_CONST              18 (None)
               RETURN_VALUE

1153   L4:     LOAD_CONST              18 (None)
               RETURN_VALUE

1149   L5:     LOAD_CONST              18 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\pas_security_01_hardening_readiness_check.py", line 1157>:
1157           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('path')
               LOAD_CONST               2 ('str')
               LOAD_CONST               3 ('payload')
               LOAD_CONST               4 ('dict')
               LOAD_CONST               5 ('return')
               LOAD_CONST               6 ('None')
               BUILD_MAP                3
               RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C181283F0, file "scripts\pas_security_01_hardening_readiness_check.py", line 1157>:
1157           RESUME                   0

1158           NOP

1159   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

1160           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

1161           LOAD_CONST               3 ('utf-8')

1159           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

1163           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

1164   L4:     LOAD_GLOBAL             11 (print + NULL)

1165           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

1166           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

1165           BUILD_STRING             4

1167           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

1164           LOAD_CONST               7 (('file',))
               CALL_KW                  2
               POP_TOP
       L5:     POP_EXCEPT
               LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               8 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

1163   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18115890, file "scripts\pas_security_01_hardening_readiness_check.py", line 1171>:
1171           RESUME                   0
               LOAD_FAST_BORROW         0 (format)
               LOAD_SMALL_INT           2
               COMPARE_OP             132 (>)
               POP_JUMP_IF_FALSE        3 (to L1)
               NOT_TAKEN
               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
               RAISE_VARARGS            1
       L1:     LOAD_CONST               1 ('argv')
               LOAD_CONST               2 ('Optional[List[str]]')
               LOAD_CONST               3 ('return')
               LOAD_CONST               4 ('int')
               BUILD_MAP                2
               RETURN_VALUE

Disassembly of <code object main at 0x0000018C17D88890, file "scripts\pas_security_01_hardening_readiness_check.py", line 1171>:
1171            RESUME                   0

1172            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

1173            NOP

1174    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

1178    L2:     LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               15 (abspath + NULL|self)
                LOAD_FAST                2 (args)
                LOAD_ATTR               16 (repo_root)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         7 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_GLOBAL             18 (_REPO_ROOT_DEFAULT)
        L3:     CALL                     1
                STORE_FAST               4 (repo_root)

1179            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

1180            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

1181            LOAD_SMALL_INT           2
                RETURN_VALUE

1183    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

1185            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

1186            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

1188    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

1190            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

1191            LOAD_GLOBAL             23 (print + NULL)
                LOAD_GLOBAL             38 (json)
                LOAD_ATTR               40 (dumps)
                PUSH_NULL
                LOAD_FAST                5 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

1193    L6:     LOAD_FAST                5 (report)
                LOAD_CONST               6 ('verdict')
                BINARY_OP               26 ([])
                LOAD_GLOBAL             42 (VERDICT_READY)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT           0
                RETURN_VALUE
        L7:     LOAD_SMALL_INT           1
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

1175            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

1176    L9:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               7 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L14)
       L10:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L13)
       L11:     NOT_TAKEN
       L12:     POP_TOP
                LOAD_SMALL_INT           0
       L13:     CALL                     1
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

1175   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L8 to L9 -> L18 [1] lasti
  L9 to L11 -> L16 [1] lasti
  L12 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
