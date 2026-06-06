# scripts_readiness/pas174_operator_audit_readiness_check

- **pyc:** `scripts\__pycache__\pas174_operator_audit_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas174_operator_audit_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas174_operator_audit_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS174 — Operator audit layer + tenant visibility readiness gate.

Deterministic, non-mutating evaluator for "is PAS174 wired
correctly and free of regressions in the PAS160-PAS173
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS173 readiness scripts still exist.
  * PAS174 surfaces exist:
      - scripts/migrate_v22_operator_actions_log.sql
      - app/services/operator/audit_service.py
      - app/services/operator/connectivity_probes.py
      - app/services/tenant/__init__.py
      - app/services/tenant/tenant_visibility_service.py
      - app/routes/tenant_portal.py
      - scripts/pas174_operator_audit_readiness_check.py
      - docs/pas174_operator_audit_layer.md
      - docs/orvn_governance_and_operator_accountability.md
      - tests/mvp/test_pas174_operator_audit_layer.py
  * Migration v22 carries PROPOSAL ONLY + DO NOT EXECUTE +
    closed actor_type + status enums + tenant-write denial +
    service_role no-update + no-delete (append-only invariant).
  * Audit service exposes the documented surface
    (log_operator_action / operator_action_history /
    brokerage_action_history / recent_failed_operator_actions)
    + closed enums + closed metadata allow-list.
  * Audit service has NO update / delete helpers.
  * Connectivity probes expose the five documented probes +
    closed status enum.
  * Tenant visibility service exposes the four documented
    helpers + closed forbidden-field allow-list.
  * Tenant routes carry admin-free auth (no X-Admin-Key
    requirement) + brokerage-scoped responses + defensive
    forbidden-field scanner.
  * Operator actions module dispatches every action through
    the audit service.
  * Worker still OFF by default.
  * FastAPI lifespan in app/main.py does NOT auto-start the
    worker.
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    / OpenAI / Anthropic imports in any PAS174 file.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS174 event type.
  * Docs carry the required clauses.
  * Governance handbook carries the required clauses.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service`, `check_connectivity_probes`, `check_docs_required_clauses`, `check_event_contract`, `check_files_present`, `check_governance_handbook`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_operator_actions_audit_wiring`, `check_prior_phases_intact`, `check_self_no_env_or_db`, `check_tenant_route`, `check_tenant_visibility_service`, `check_v22_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS174`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS174 — Operator audit layer + tenant visibility readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS174 wired\ncorrectly and free of regressions in the PAS160-PAS173\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS173 readiness scripts still exist.\n  * PAS174 surfaces exist:\n      - scripts/migrate_v22_operator_actions_log.sql\n      - app/services/operator/audit_service.py\n      - app/services/operator/connectivity_probes.py\n      - app/services/tenant/__init__.py\n      - app/services/tenant/tenant_visibility_service.py\n      - app/routes/tenant_portal.py\n      - scripts/pas174_operator_audit_readiness_check.py\n      - docs/pas174_operator_audit_layer.md\n      - docs/orvn_governance_and_operator_accountability.md\n      - tests/mvp/test_pas174_operator_audit_layer.py\n  * Migration v22 carries PROPOSAL ONLY + DO NOT EXECUTE +\n    closed actor_type + status enums + tenant-write denial +\n    service_role no-update + no-delete (append-only invariant).\n  * Audit service exposes the documented surface\n    (log_operator_action / operator_action_history /\n    brokerage_action_history / recent_failed_operator_actions)\n    + closed enums + closed metadata allow-list.\n  * Audit service has NO update / delete helpers.\n  * Connectivity probes expose the five documented probes +\n    closed status enum.\n  * Tenant visibility service exposes the four documented\n    helpers + closed forbidden-field allow-list.\n  * Tenant routes carry admin-free auth (no X-Admin-Key\n    requirement) + brokerage-scoped responses + defensive\n    forbidden-field scanner.\n  * Operator actions module dispatches every action through\n    the audit service.\n  * Worker still OFF by default.\n  * FastAPI lifespan in app/main.py does NOT auto-start the\n    worker.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports in any PAS174 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS174 event type.\n  * Docs carry the required clauses.\n  * Governance handbook carries the required clauses.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas174_operator_audit_readiness_report.json'
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
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS174 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS174 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS174 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default'
- 'missing strict enable-literal constant'
- 'main.py'
- 'from app.services.ingestion.worker'
- 'from app.services.ingestion.worker import …'
- 'import app.services.ingestion.worker'
- 'run_worker_loop'
- 'run_worker_loop reference'
- 'process_pending_call('
- 'process_pending_call call'
- 'main:no_startup_worker'
- 'FastAPI lifespan does not auto-start the pending-call worker'
- 'disqualifying tokens: '
- 'operator'
- 'audit_service.py'
- 'audit_service:'
- 'Audit service token: '
- 'missing token '
- 'audit_service:append_only_invariant'
- 'Audit service has no UPDATE / DELETE mutation helpers'
- 'connectivity_probes.py'
- 'connectivity_probes:'
- 'Connectivity probe token: '
- 'connectivity_probes:no_real_outbound'
- 'Connectivity probes never place real outbound calls'
- 'tenant'
- 'tenant_visibility_service.py'
- 'tenant_visibility:'
- 'Tenant visibility service token: '
- 'routes'
- 'tenant_portal.py'
- 'tenant_route:'
- 'Tenant route token: '
- 'tenant_route:no_pii_exposure'
- 'Tenant route does not reference transcript/raw payload'
- 'require_brokerage'
- 'x_api_key'
- 'x_admin_key'
- 'tenant_route:tenant_auth_only'
- 'Tenant route uses X-API-Key (require_brokerage), never admin'
- 'expected require_brokerage + x_api_key, no admin auth'
- 'tenant_portal_router'
- 'prefix="/tenant"'
- 'tenant_route:router_mounted'
- 'tenant_portal_router is mounted at /tenant in app/main.py'
- 'expected `tenant_portal_router` import + `include_router(..., prefix="/tenant")`'
- 'operator_actions.py'
- 'operator_actions_audit:'
- 'Operator actions audit wiring token: '
- 'scripts'
- 'migrate_v22_operator_actions_log.sql'
- 'proposal only'
- 'v22_sql:proposal_only'
- "v22 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v22_sql:do_not_execute'
- "v22 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'v22_sql:closed_actor_type_enum'
- 'v22 SQL carries the closed actor_type enum literals'
- 'missing one or more actor_type literals'
- 'v22_sql:closed_status_enum'
- 'v22 SQL carries the closed status enum literals'
- 'missing one or more status literals'
- 'pas_operator_actions_log_tenant_no_insert'
- 'v22_sql:tenant_no_write'
- 'v22 SQL denies tenant write'
- 'missing tenant-write denial'
- 'pas_operator_actions_log_service_role_no_update'
- 'pas_operator_actions_log_service_role_no_delete'
- 'v22_sql:service_role_append_only'
- 'v22 SQL denies service_role UPDATE + DELETE (append-only)'
- 'missing service_role no-update / no-delete policy'
- "auth.jwt() ->> 'brokerage_id'"
- 'v22_sql:tenant_select_scoped'
- 'v22 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant scoped select'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/operator/audit_service.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas174_operator_audit_layer.md'
- 'docs:phrase:'
- 'Doctrine doc carries clause: '
- 'expected one of: '
- ' | '
- 'orvn_governance_and_operator_accountability.md'
- 'governance:phrase:'
- 'Governance handbook carries clause: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS174 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS174'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas174_operator_audit_readiness_check'
- 'PAS174 — Evaluate the operator audit layer + tenant visibility surface. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- 'Repo root (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit JSON on stdout in addition to the summary.'
- '--summary-only'
- 'Skip writing the JSON report file.'
- '--strict'
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS174] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS174] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS174 — Operator audit layer + tenant visibility readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS174 wired\ncorrectly and free of regressions in the PAS160-PAS173\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS173 readiness scripts still exist.\n  * PAS174 surfaces exist:\n      - scripts/migrate_v22_operator_actions_log.sql\n      - app/services/operator/audit_service.py\n      - app/services/operator/connectivity_probes.py\n      - app/services/tenant/__init__.py\n      - app/services/tenant/tenant_visibility_service.py\n      - app/routes/tenant_portal.py\n      - scripts/pas174_operator_audit_readiness_check.py\n      - docs/pas174_operator_audit_layer.md\n      - docs/orvn_governance_and_operator_accountability.md\n      - tests/mvp/test_pas174_operator_audit_layer.py\n  * Migration v22 carries PROPOSAL ONLY + DO NOT EXECUTE +\n    closed actor_type + status enums + tenant-write denial +\n    service_role no-update + no-delete (append-only invariant).\n  * Audit service exposes the documented surface\n    (log_operator_action / operator_action_history /\n    brokerage_action_history / recent_failed_operator_actions)\n    + closed enums + closed metadata allow-list.\n  * Audit service has NO update / delete helpers.\n  * Connectivity probes expose the five documented probes +\n    closed status enum.\n  * Tenant visibility service exposes the four documented\n    helpers + closed forbidden-field allow-list.\n  * Tenant routes carry admin-free auth (no X-Admin-Key\n    requirement) + brokerage-scoped responses + defensive\n    forbidden-field scanner.\n  * Operator actions module dispatches every action through\n    the audit service.\n  * Worker still OFF by default.\n  * FastAPI lifespan in app/main.py does NOT auto-start the\n    worker.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports in any PAS174 file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS174 event type.\n  * Docs carry the required clauses.\n  * Governance handbook carries the required clauses.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  62           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  63           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  66           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  67           NOP

  68   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  66   L4:     END_FOR
               POP_ITER

  73           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  74           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  73           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  78           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  79           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  81           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  82           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  89           LOAD_CONST              74 (('scripts/migrate_v22_operator_actions_log.sql', 'app/services/operator/audit_service.py', 'app/services/operator/connectivity_probes.py', 'app/services/tenant/__init__.py', 'app/services/tenant/tenant_visibility_service.py', 'app/routes/tenant_portal.py', 'scripts/pas174_operator_audit_readiness_check.py', 'docs/pas174_operator_audit_layer.md', 'docs/orvn_governance_and_operator_accountability.md', 'tests/mvp/test_pas174_operator_audit_layer.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 102           LOAD_CONST              75 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 121           LOAD_CONST              76 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 131           LOAD_CONST              77 (('def log_operator_action(', 'def operator_action_history(', 'def brokerage_action_history(', 'def recent_failed_operator_actions(', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_AUDIT_STATUSES', 'ALLOWED_METADATA_KEYS', '_TABLE = "pas_operator_actions_log"', 'audit_store_unavailable'))
               STORE_NAME              32 (REQUIRED_AUDIT_SERVICE_TOKENS)

 144           LOAD_CONST              78 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_', '.update(', '.delete('))
               STORE_NAME              33 (FORBIDDEN_AUDIT_MUTATION_TOKENS)

 155           LOAD_CONST              79 (('def probe_twilio_configuration(', 'def probe_slack_webhook(', 'def probe_calcom_configuration(', 'def probe_worker_visibility(', 'def probe_encryption_posture(', 'def run_all_probes(', 'ALLOWED_PROBE_STATUSES', 'ALLOWED_PROBE_TYPES'))
               STORE_NAME              34 (REQUIRED_CONNECTIVITY_PROBE_TOKENS)

 169           LOAD_CONST              80 (('twilio_client', 'TwilioRestClient', 'httpx.post', 'httpx.AsyncClient', 'requests.post', 'requests.get', 'requests.put', 'calcom_client.book', 'smtplib', 'send_email'))
               STORE_NAME              35 (FORBIDDEN_PROBE_OUTBOUND_TOKENS)

 182           LOAD_CONST              81 (('def tenant_status(', 'def tenant_launch_readiness(', 'def tenant_integration_posture(', 'def tenant_callback_summary(', '_FORBIDDEN_TENANT_FIELDS'))
               STORE_NAME              36 (REQUIRED_TENANT_VISIBILITY_TOKENS)

 190           LOAD_CONST              82 (('def require_brokerage(', '@router.get("/status")', '@router.get("/launch-readiness")', '@router.get("/integrations")', '@router.get("/callback-summary")', '_FORBIDDEN_TENANT_FIELDS', '_scan_for_forbidden', 'tenant_envelope_forbidden_field'))
               STORE_NAME              37 (REQUIRED_TENANT_ROUTE_TOKENS)

 201           LOAD_CONST              83 (('_emit_audit_entry', '_audit_actor_type', '_audit_status_from_dispatch', 'log_operator_action'))
               STORE_NAME              38 (REQUIRED_OPERATOR_ACTIONS_AUDIT_TOKENS)

 209           LOAD_CONST              84 (('operator.action.executed', 'operator.audit.logged', 'operator.audit.failed', 'tenant.visibility.requested', 'connectivity.probe.executed', 'connectivity.probe.failed'))
               STORE_NAME              39 (REQUIRED_EVENT_TYPES)

 221           LOAD_CONST              85 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              40 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 246           LOAD_CONST              86 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              41 (FORBIDDEN_INBOX_TOKENS)

 255           LOAD_CONST              87 (('transcript', 'raw_payload', 'raw_email', 'raw_body'))
               STORE_NAME              42 (FORBIDDEN_TENANT_EXPOSURE_TOKENS)

 267           LOAD_CONST              13 ('severity')

 269           LOAD_NAME               27 (SEVERITY_BLOCK)

 267           LOAD_CONST              14 ('detail')

 269           LOAD_CONST              15 ('')

 267           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025E30, file "scripts\pas174_operator_audit_readiness_check.py", line 267>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA2970, file "scripts\pas174_operator_audit_readiness_check.py", line 267>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_check)

 280           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas174_operator_audit_readiness_check.py", line 280>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18038B70, file "scripts\pas174_operator_audit_readiness_check.py", line 280>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_now_iso)

 284           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas174_operator_audit_readiness_check.py", line 284>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053510, file "scripts\pas174_operator_audit_readiness_check.py", line 284>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_read_text)

 291           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas174_operator_audit_readiness_check.py", line 291>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas174_operator_audit_readiness_check.py", line 291>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_strip_python_comments_and_strings)

 330           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas174_operator_audit_readiness_check.py", line 330>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18060A50, file "scripts\pas174_operator_audit_readiness_check.py", line 330>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_files_present)

 344           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas174_operator_audit_readiness_check.py", line 344>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C180608A0, file "scripts\pas174_operator_audit_readiness_check.py", line 344>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_prior_phases_intact)

 358           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas174_operator_audit_readiness_check.py", line 358>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas174_operator_audit_readiness_check.py", line 358>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_memory_review_intact)

 372           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas174_operator_audit_readiness_check.py", line 372>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas174_operator_audit_readiness_check.py", line 372>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_worker_off_by_default)

 390           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas174_operator_audit_readiness_check.py", line 390>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA4AC0, file "scripts\pas174_operator_audit_readiness_check.py", line 390>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_startup_worker)

 414           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas174_operator_audit_readiness_check.py", line 414>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_audit_service at 0x0000018C17EE1CC0, file "scripts\pas174_operator_audit_readiness_check.py", line 414>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_audit_service)

 444           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas174_operator_audit_readiness_check.py", line 444>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_connectivity_probes at 0x0000018C17EE25F0, file "scripts\pas174_operator_audit_readiness_check.py", line 444>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_connectivity_probes)

 473           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas174_operator_audit_readiness_check.py", line 473>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_tenant_visibility_service at 0x0000018C17F01250, file "scripts\pas174_operator_audit_readiness_check.py", line 473>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_tenant_visibility_service)

 489           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas174_operator_audit_readiness_check.py", line 489>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_tenant_route at 0x0000018C17788D70, file "scripts\pas174_operator_audit_readiness_check.py", line 489>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_tenant_route)

 550           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas174_operator_audit_readiness_check.py", line 550>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_operator_actions_audit_wiring at 0x0000018C17F01040, file "scripts\pas174_operator_audit_readiness_check.py", line 550>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_operator_actions_audit_wiring)

 566           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas174_operator_audit_readiness_check.py", line 566>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_v22_sql at 0x0000018C17D7CA50, file "scripts\pas174_operator_audit_readiness_check.py", line 566>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_v22_sql)

 645           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas174_operator_audit_readiness_check.py", line 645>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas174_operator_audit_readiness_check.py", line 645>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_event_contract)

 661           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas174_operator_audit_readiness_check.py", line 661>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas174_operator_audit_readiness_check.py", line 661>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_forbidden_imports)

 695           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas174_operator_audit_readiness_check.py", line 695>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD2160, file "scripts\pas174_operator_audit_readiness_check.py", line 695>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_no_inbox_scan_tokens)

 725           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas174_operator_audit_readiness_check.py", line 725>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_docs_required_clauses at 0x0000018C17D8B490, file "scripts\pas174_operator_audit_readiness_check.py", line 725>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_docs_required_clauses)

 763           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas174_operator_audit_readiness_check.py", line 763>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_governance_handbook at 0x0000018C17D8A770, file "scripts\pas174_operator_audit_readiness_check.py", line 763>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_governance_handbook)

 796           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas174_operator_audit_readiness_check.py", line 796>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts\pas174_operator_audit_readiness_check.py", line 796>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_self_no_env_or_db)

 830           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas174_operator_audit_readiness_check.py", line 830>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _aggregate at 0x0000018C17EC46C0, file "scripts\pas174_operator_audit_readiness_check.py", line 830>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_aggregate)

 846           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas174_operator_audit_readiness_check.py", line 846>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas174_operator_audit_readiness_check.py", line 846>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (_operator_actions)

 856           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas174_operator_audit_readiness_check.py", line 856>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object evaluate at 0x0000018C182DA4E0, file "scripts\pas174_operator_audit_readiness_check.py", line 856>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (evaluate)

 892           LOAD_CONST              64 ('pas174_operator_audit_readiness_report.json')
               STORE_NAME              67 (REPORT_FILENAME)

 895           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas174_operator_audit_readiness_check.py", line 895>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas174_operator_audit_readiness_check.py", line 895>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_build_parser)

 928           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas174_operator_audit_readiness_check.py", line 928>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas174_operator_audit_readiness_check.py", line 928>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_print_summary)

 946           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18025730, file "scripts\pas174_operator_audit_readiness_check.py", line 946>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _write_report at 0x0000018C180FC210, file "scripts\pas174_operator_audit_readiness_check.py", line 946>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_write_report)

 960           LOAD_CONST              88 ((None,))
               LOAD_CONST              71 (<code object __annotate__ at 0x0000018C18114030, file "scripts\pas174_operator_audit_readiness_check.py", line 960>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object main at 0x0000018C17D87D80, file "scripts\pas174_operator_audit_readiness_check.py", line 960>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              71 (main)

 988           LOAD_NAME               72 (__name__)
               LOAD_CONST              73 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 989           LOAD_NAME                6 (sys)
               LOAD_ATTR              146 (exit)
               PUSH_NULL
               LOAD_NAME               71 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 988   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  69           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  70   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          363 (to L1)

  69   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "scripts\pas174_operator_audit_readiness_check.py", line 267>:
267           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               3 ('status')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               4 ('label')

268           LOAD_CONST               2 ('str')

267           LOAD_CONST               5 ('severity')

269           LOAD_CONST               2 ('str')

267           LOAD_CONST               6 ('detail')

269           LOAD_CONST               2 ('str')

267           LOAD_CONST               7 ('return')

270           LOAD_CONST               8 ('dict')

267           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2970, file "scripts\pas174_operator_audit_readiness_check.py", line 267>:
267           RESUME                   0

272           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

273           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

274           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

275           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

276           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

271           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas174_operator_audit_readiness_check.py", line 280>:
280           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038B70, file "scripts\pas174_operator_audit_readiness_check.py", line 280>:
280           RESUME                   0

281           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas174_operator_audit_readiness_check.py", line 284>:
284           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053510, file "scripts\pas174_operator_audit_readiness_check.py", line 284>:
 284           RESUME                   0

 285           NOP

 286   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 287           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 288   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 287   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas174_operator_audit_readiness_check.py", line 291>:
291           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas174_operator_audit_readiness_check.py", line 291>:
291            RESUME                   0

292            BUILD_LIST               0
               STORE_FAST               1 (out)

293            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

294    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

295            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

296            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

297            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

298            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

299            JUMP_FORWARD           240 (to L13)

300    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

301            JUMP_BACKWARD           59 (to L1)

302    L3:     LOAD_FAST_BORROW         0 (src)
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

303    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

304            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

305            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

306            JUMP_FORWARD           138 (to L13)

307    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

308            JUMP_BACKWARD          161 (to L1)

309    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

310            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

311            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

312    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

313            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

314            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

315            JUMP_BACKWARD           30 (to L7)

316    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

317    L9:     JUMP_FORWARD            11 (to L11)

318   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

319   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

320            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

321   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

322            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

323   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas174_operator_audit_readiness_check.py", line 330>:
330           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18060A50, file "scripts\pas174_operator_audit_readiness_check.py", line 330>:
330           RESUME                   0

331           BUILD_LIST               0
              STORE_FAST               1 (out)

332           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

333           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

334           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

335           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

336           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

337   L3:     LOAD_CONST               3 ('Required PAS174 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

338           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

339           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

334   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

332   L6:     END_FOR
              POP_ITER

341           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas174_operator_audit_readiness_check.py", line 344>:
344           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180608A0, file "scripts\pas174_operator_audit_readiness_check.py", line 344>:
344           RESUME                   0

345           BUILD_LIST               0
              STORE_FAST               1 (out)

346           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

347           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

348           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

349           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

350           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

351   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

352           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

353           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS174 must not delete')

348   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

346   L6:     END_FOR
              POP_ITER

355           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas174_operator_audit_readiness_check.py", line 358>:
358           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060C00, file "scripts\pas174_operator_audit_readiness_check.py", line 358>:
358           RESUME                   0

359           BUILD_LIST               0
              STORE_FAST               1 (out)

360           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

361           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

362           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

363           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

364           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

365   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

366           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

367           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS174 must not touch')

362   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

360   L6:     END_FOR
              POP_ITER

369           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\pas174_operator_audit_readiness_check.py", line 372>:
372           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179A7290, file "scripts\pas174_operator_audit_readiness_check.py", line 372>:
372           RESUME                   0

373           BUILD_LIST               0
              STORE_FAST               1 (out)

374           LOAD_GLOBAL              1 (Path + NULL)
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

375           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

377           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

378           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

376   L2:     STORE_FAST               4 (literal_ok)

380           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

381           LOAD_CONST               7 ('worker:off_by_default')

382           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

383   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

384           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

385           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

380   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

387           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas174_operator_audit_readiness_check.py", line 390>:
390           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA4AC0, file "scripts\pas174_operator_audit_readiness_check.py", line 390>:
390           RESUME                   0

391           BUILD_LIST               0
              STORE_FAST               1 (out)

392           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

393           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

394           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

395           BUILD_LIST               0
              STORE_FAST               5 (bad)

396           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

397           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

398   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

399           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

400   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

401           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

402   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

403           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

404   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

405           LOAD_CONST              10 ('main:no_startup_worker')

406           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

407   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

408           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

409           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L8)
              NOT_TAKEN
              LOAD_CONST              14 ('disqualifying tokens: ')
              LOAD_CONST              15 (', ')
              LOAD_ATTR               13 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               2 ('')

404   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

411           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas174_operator_audit_readiness_check.py", line 414>:
414           RESUME                   0
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

Disassembly of <code object check_audit_service at 0x0000018C17EE1CC0, file "scripts\pas174_operator_audit_readiness_check.py", line 414>:
414            RESUME                   0

415            BUILD_LIST               0
               STORE_FAST               1 (out)

416            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('audit_service.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

417            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

418            LOAD_GLOBAL              4 (REQUIRED_AUDIT_SERVICE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

419            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

420            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

421            LOAD_CONST               5 ('audit_service:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

422            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

423    L4:     LOAD_CONST               9 ('Audit service token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

424            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

425            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

420    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

418    L7:     END_FOR
               POP_ITER

429            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

430            BUILD_LIST               0
               STORE_FAST               7 (bad)

431            LOAD_GLOBAL             14 (FORBIDDEN_AUDIT_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

432            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

433    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

431   L10:     END_FOR
               POP_ITER

434            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

435            LOAD_CONST              12 ('audit_service:append_only_invariant')

436            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

437   L12:     LOAD_CONST              13 ('Audit service has no UPDATE / DELETE mutation helpers')

438            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

439            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

434   L14:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

441            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas174_operator_audit_readiness_check.py", line 444>:
444           RESUME                   0
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

Disassembly of <code object check_connectivity_probes at 0x0000018C17EE25F0, file "scripts\pas174_operator_audit_readiness_check.py", line 444>:
444            RESUME                   0

445            BUILD_LIST               0
               STORE_FAST               1 (out)

446            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('connectivity_probes.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

447            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

448            LOAD_GLOBAL              4 (REQUIRED_CONNECTIVITY_PROBE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

449            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

450            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

451            LOAD_CONST               5 ('connectivity_probes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

452            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

453    L4:     LOAD_CONST               9 ('Connectivity probe token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

454            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

455            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

450    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

448    L7:     END_FOR
               POP_ITER

458            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

459            BUILD_LIST               0
               STORE_FAST               7 (bad)

460            LOAD_GLOBAL             14 (FORBIDDEN_PROBE_OUTBOUND_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

461            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

462    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

460   L10:     END_FOR
               POP_ITER

463            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

464            LOAD_CONST              12 ('connectivity_probes:no_real_outbound')

465            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

466   L12:     LOAD_CONST              13 ('Connectivity probes never place real outbound calls')

467            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

468            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

463   L14:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

470            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas174_operator_audit_readiness_check.py", line 473>:
473           RESUME                   0
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

Disassembly of <code object check_tenant_visibility_service at 0x0000018C17F01250, file "scripts\pas174_operator_audit_readiness_check.py", line 473>:
473           RESUME                   0

474           BUILD_LIST               0
              STORE_FAST               1 (out)

475           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('tenant')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('tenant_visibility_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

476           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

477           LOAD_GLOBAL              4 (REQUIRED_TENANT_VISIBILITY_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

478           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

479           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

480           LOAD_CONST               5 ('tenant_visibility:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

481           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

482   L4:     LOAD_CONST               9 ('Tenant visibility service token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

483           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

484           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

479   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

477   L7:     END_FOR
              POP_ITER

486           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts\pas174_operator_audit_readiness_check.py", line 489>:
489           RESUME                   0
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

Disassembly of <code object check_tenant_route at 0x0000018C17788D70, file "scripts\pas174_operator_audit_readiness_check.py", line 489>:
489            RESUME                   0

490            BUILD_LIST               0
               STORE_FAST               1 (out)

491            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant_portal.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

492            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

493            LOAD_GLOBAL              4 (REQUIRED_TENANT_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

494            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

495            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

496            LOAD_CONST               4 ('tenant_route:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

497            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

498    L4:     LOAD_CONST               8 ('Tenant route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

499            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

500            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

495    L6:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

493    L7:     END_FOR
               POP_ITER

503            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

504            BUILD_LIST               0
               STORE_FAST               7 (bad)

505            LOAD_GLOBAL             14 (FORBIDDEN_TENANT_EXPOSURE_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

506            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

507    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

505   L10:     END_FOR
               POP_ITER

508            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

509            LOAD_CONST              11 ('tenant_route:no_pii_exposure')

510            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('PASS')

511   L12:     LOAD_CONST              12 ('Tenant route does not reference transcript/raw payload')

512            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

513            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              13 ('disqualifying tokens: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               3 ('')

508   L14:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

518            LOAD_CONST              15 ('require_brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L15)
               NOT_TAKEN
               POP_TOP

519            LOAD_CONST              16 ('x_api_key')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

518            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L15)
               NOT_TAKEN
               POP_TOP

520            LOAD_CONST              17 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               19 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              1 (not in)

517   L15:     STORE_FAST               8 (auth_ok)

522            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

523            LOAD_CONST              18 ('tenant_route:tenant_auth_only')

524            LOAD_FAST_BORROW         8 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               7 ('FAIL')

525   L17:     LOAD_CONST              19 ('Tenant route uses X-API-Key (require_brokerage), never admin')

526            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

527            LOAD_FAST_BORROW         8 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L19)

528   L18:     LOAD_CONST              20 ('expected require_brokerage + x_api_key, no admin auth')

522   L19:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

532            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST              21 ('main.py')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L20)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
      L20:     STORE_FAST               9 (main_src)

534            LOAD_CONST              22 ('tenant_portal_router')
               LOAD_FAST_BORROW         9 (main_src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L21)
               NOT_TAKEN
               POP_TOP

535            LOAD_CONST              23 ('prefix="/tenant"')
               LOAD_FAST_BORROW         9 (main_src)
               CONTAINS_OP              0 (in)

533   L21:     STORE_FAST              10 (router_ok)

537            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

538            LOAD_CONST              24 ('tenant_route:router_mounted')

539            LOAD_FAST_BORROW        10 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST               7 ('FAIL')

540   L23:     LOAD_CONST              25 ('tenant_portal_router is mounted at /tenant in app/main.py')

541            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

542            LOAD_FAST_BORROW        10 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L25)

543   L24:     LOAD_CONST              26 ('expected `tenant_portal_router` import + `include_router(..., prefix="/tenant")`')

537   L25:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

547            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas174_operator_audit_readiness_check.py", line 550>:
550           RESUME                   0
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

Disassembly of <code object check_operator_actions_audit_wiring at 0x0000018C17F01040, file "scripts\pas174_operator_audit_readiness_check.py", line 550>:
550           RESUME                   0

551           BUILD_LIST               0
              STORE_FAST               1 (out)

552           LOAD_GLOBAL              1 (Path + NULL)
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

553           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

554           LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ACTIONS_AUDIT_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

555           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

556           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

557           LOAD_CONST               5 ('operator_actions_audit:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

558           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

559   L4:     LOAD_CONST               9 ('Operator actions audit wiring token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

560           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

561           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

556   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

554   L7:     END_FOR
              POP_ITER

563           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas174_operator_audit_readiness_check.py", line 566>:
566           RESUME                   0
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

Disassembly of <code object check_v22_sql at 0x0000018C17D7CA50, file "scripts\pas174_operator_audit_readiness_check.py", line 566>:
  --            MAKE_CELL               11 (src)

 566            RESUME                   0

 567            BUILD_LIST               0
                STORE_FAST               1 (out)

 568            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v22_operator_actions_log.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 569            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             11 (src)

 570            LOAD_DEREF              11 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 571            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 572            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 573            LOAD_CONST               4 ('v22_sql:proposal_only')

 574            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 575    L3:     LOAD_CONST               7 ("v22 SQL carries 'PROPOSAL ONLY' guardrail")

 576            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 577            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 572    L5:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 579            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 580            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 581            LOAD_CONST              11 ('v22_sql:do_not_execute')

 582            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 583    L7:     LOAD_CONST              12 ("v22 SQL carries 'DO NOT EXECUTE' trailer")

 584            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 585            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 580    L9:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 588            LOAD_GLOBAL             12 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L13)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas174_operator_audit_readiness_check.py", line 588>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 589            LOAD_CONST              37 (("'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 588            CALL                     0
       L10:     FOR_ITER                12 (to L12)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L10)
       L11:     POP_ITER
                LOAD_CONST              15 (False)
                JUMP_FORWARD            20 (to L14)
       L12:     END_FOR
                POP_ITER
                LOAD_CONST              16 (True)
                JUMP_FORWARD            16 (to L14)
       L13:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas174_operator_audit_readiness_check.py", line 588>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 589            LOAD_CONST              37 (("'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 588            CALL                     0
                CALL                     1
       L14:     STORE_FAST               6 (actor_types_ok)

 591            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 592            LOAD_CONST              17 ('v22_sql:closed_actor_type_enum')

 593            LOAD_FAST_BORROW         6 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST               6 ('FAIL')

 594   L16:     LOAD_CONST              18 ('v22 SQL carries the closed actor_type enum literals')

 595            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 596            LOAD_FAST_BORROW         6 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              19 ('missing one or more actor_type literals')

 591   L18:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 599            LOAD_GLOBAL             12 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18026030, file "scripts\pas174_operator_audit_readiness_check.py", line 599>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 600            LOAD_CONST              38 (("'SUCCESS'", "'FAILED'", "'SKIPPED'"))
                GET_ITER

 599            CALL                     0
       L19:     FOR_ITER                12 (to L21)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L19)
       L20:     POP_ITER
                LOAD_CONST              15 (False)
                JUMP_FORWARD            20 (to L23)
       L21:     END_FOR
                POP_ITER
                LOAD_CONST              16 (True)
                JUMP_FORWARD            16 (to L23)
       L22:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18026030, file "scripts\pas174_operator_audit_readiness_check.py", line 599>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 600            LOAD_CONST              38 (("'SUCCESS'", "'FAILED'", "'SKIPPED'"))
                GET_ITER

 599            CALL                     0
                CALL                     1
       L23:     STORE_FAST               7 (statuses_ok)

 602            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 603            LOAD_CONST              21 ('v22_sql:closed_status_enum')

 604            LOAD_FAST_BORROW         7 (statuses_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               6 ('FAIL')

 605   L25:     LOAD_CONST              22 ('v22 SQL carries the closed status enum literals')

 606            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 607            LOAD_FAST_BORROW         7 (statuses_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST              23 ('missing one or more status literals')

 602   L27:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 609            LOAD_CONST              24 ('pas_operator_actions_log_tenant_no_insert')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               8 (tenant_no_write)

 610            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 611            LOAD_CONST              25 ('v22_sql:tenant_no_write')

 612            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 613   L29:     LOAD_CONST              26 ('v22 SQL denies tenant write')

 614            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 615            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing tenant-write denial')

 610   L31:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 621            LOAD_CONST              28 ('pas_operator_actions_log_service_role_no_update')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L32)
                NOT_TAKEN
                POP_TOP

 622            LOAD_CONST              29 ('pas_operator_actions_log_service_role_no_delete')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 620   L32:     STORE_FAST               9 (service_role_append_only)

 624            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 625            LOAD_CONST              30 ('v22_sql:service_role_append_only')

 626            LOAD_FAST_BORROW         9 (service_role_append_only)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 627   L34:     LOAD_CONST              31 ('v22 SQL denies service_role UPDATE + DELETE (append-only)')

 628            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 629            LOAD_FAST_BORROW         9 (service_role_append_only)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)

 630   L35:     LOAD_CONST              32 ('missing service_role no-update / no-delete policy')

 624   L36:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 634            LOAD_CONST              33 ("auth.jwt() ->> 'brokerage_id'")
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST              10 (tenant_scoped)

 635            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 636            LOAD_CONST              34 ('v22_sql:tenant_select_scoped')

 637            LOAD_FAST_BORROW        10 (tenant_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L37)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L38)
       L37:     LOAD_CONST               6 ('FAIL')

 638   L38:     LOAD_CONST              35 ('v22 SQL scopes tenant SELECT to own brokerage_id')

 639            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 640            LOAD_FAST_BORROW        10 (tenant_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L39)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L40)
       L39:     LOAD_CONST              36 ('missing tenant scoped select')

 635   L40:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 642            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025530, file "scripts\pas174_operator_audit_readiness_check.py", line 588>:
  --           COPY_FREE_VARS           1

 588           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 589   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
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

Disassembly of <code object <genexpr> at 0x0000018C18026030, file "scripts\pas174_operator_audit_readiness_check.py", line 599>:
  --           COPY_FREE_VARS           1

 599           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 600   L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (s, s)
               LOAD_DEREF               2 (src)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas174_operator_audit_readiness_check.py", line 645>:
645           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FEDC30, file "scripts\pas174_operator_audit_readiness_check.py", line 645>:
645           RESUME                   0

646           BUILD_LIST               0
              STORE_FAST               1 (out)

647           LOAD_GLOBAL              1 (Path + NULL)
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

648           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

649           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

650           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

651           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

652           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

653           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

654   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

655           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

656           LOAD_FAST_BORROW         5 (ok)
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

651   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

649   L7:     END_FOR
              POP_ITER

658           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas174_operator_audit_readiness_check.py", line 661>:
661           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F84C80, file "scripts\pas174_operator_audit_readiness_check.py", line 661>:
661            RESUME                   0

662            BUILD_LIST               0
               STORE_FAST               1 (out)

663            LOAD_CONST              10 (('app/services/operator/audit_service.py', 'app/services/operator/connectivity_probes.py', 'app/services/tenant/__init__.py', 'app/services/tenant/tenant_visibility_service.py', 'app/routes/tenant_portal.py', 'scripts/pas174_operator_audit_readiness_check.py'))
               STORE_FAST               2 (files)

671            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

672            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

673            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

674            JUMP_BACKWARD           46 (to L1)

675    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

676            BUILD_LIST               0
               STORE_FAST               6 (bad)

677            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

678            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

679            LOAD_FAST_BORROW         8 (stripped)
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

680    L5:     JUMP_BACKWARD           52 (to L4)

681    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

682            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

683    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

681    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

677   L10:     END_FOR
               POP_ITER

684            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

685            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

686            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

687   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

688            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

690            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

689            LOAD_CONST               7 ('forbidden import prefixes: ')
               LOAD_CONST               8 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_GLOBAL             23 (sorted + NULL)
               LOAD_GLOBAL             25 (set + NULL)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)

690   L13:     LOAD_CONST               1 ('')

684   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

671   L15:     END_FOR
               POP_ITER

692            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas174_operator_audit_readiness_check.py", line 695>:
695           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD2160, file "scripts\pas174_operator_audit_readiness_check.py", line 695>:
695            RESUME                   0

696            BUILD_LIST               0
               STORE_FAST               1 (out)

697            LOAD_CONST               9 (('app/services/operator/audit_service.py', 'app/services/operator/connectivity_probes.py', 'app/services/tenant/tenant_visibility_service.py', 'app/routes/tenant_portal.py', 'scripts/pas174_operator_audit_readiness_check.py'))
               STORE_FAST               2 (files)

704            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
               STORE_FAST               3 (relpath)

705            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

706            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

707            JUMP_BACKWARD           45 (to L1)

708    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

709            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

710            BUILD_LIST               0
               STORE_FAST               7 (bad)

711            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

712            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

713    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

711    L6:     END_FOR
               POP_ITER

714            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

715            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

716            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

717    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

718            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

720            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

719            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

720    L9:     LOAD_CONST               1 ('')

714   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

704   L11:     END_FOR
               POP_ITER

722            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas174_operator_audit_readiness_check.py", line 725>:
725           RESUME                   0
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

Disassembly of <code object check_docs_required_clauses at 0x0000018C17D8B490, file "scripts\pas174_operator_audit_readiness_check.py", line 725>:
  --            MAKE_CELL                8 (lower)

 725            RESUME                   0

 726            BUILD_LIST               0
                STORE_FAST               1 (out)

 727            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas174_operator_audit_layer.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 728            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 729            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 730            LOAD_CONST              13 ((('immutable-audit', ('immutable audit', 'append-only')), ('tenant-visibility', ('tenant visibility',)), ('no-autonomous', ('no autonomous', 'no-autonomous', 'no autonomous-remediation')), ('connectivity-probe', ('connectivity probe',)), ('append-only-governance', ('append-only', 'append only')), ('rollback', ('rollback',)), ('escalation', ('escalation',)), ('operator-accountability', ('operator accountability', 'accountability model')), ('pilot-governance', ('pilot governance', 'pilot expansion')), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 750            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 751            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas174_operator_audit_readiness_check.py", line 751>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas174_operator_audit_readiness_check.py", line 751>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 752            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 753            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 754            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 755    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 756            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 758            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 757            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 758   L10:     LOAD_CONST               2 ('')

 752   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 750   L12:     END_FOR
                POP_ITER

 760            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "scripts\pas174_operator_audit_readiness_check.py", line 751>:
  --           COPY_FREE_VARS           1

 751           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas174_operator_audit_readiness_check.py", line 763>:
763           RESUME                   0
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

Disassembly of <code object check_governance_handbook at 0x0000018C17D8A770, file "scripts\pas174_operator_audit_readiness_check.py", line 763>:
  --            MAKE_CELL                8 (lower)

 763            RESUME                   0

 764            BUILD_LIST               0
                STORE_FAST               1 (out)

 765            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('orvn_governance_and_operator_accountability.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 766            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 767            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 768            LOAD_CONST              13 ((('daily-quick-look', ('daily quick-look', 'daily quick look')), ('audit-discipline', ('audit-trail discipline', 'audit trail discipline')), ('tenant-portal', ('tenant portal', '/tenant/')), ('probes', ('connectivity probe', 'dry-run only', 'dry run only')), ('accountability', ('accountability model', 'operator accountability')), ('escalation', ('escalation',)), ('rollback', ('rollback',)), ('doctrine', ('doctrine',)), ('no-gmail', ('no gmail',)), ('post-pilot', ('post-pilot',))))
                STORE_FAST               4 (required_phrases)

 783            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 784            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas174_operator_audit_readiness_check.py", line 784>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18025F30, file "scripts\pas174_operator_audit_readiness_check.py", line 784>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 785            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 786            LOAD_CONST               6 ('governance:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 787            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 788    L9:     LOAD_CONST               9 ('Governance handbook carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 789            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 791            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 790            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 791   L10:     LOAD_CONST               2 ('')

 785   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 783   L12:     END_FOR
                POP_ITER

 793            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025F30, file "scripts\pas174_operator_audit_readiness_check.py", line 784>:
  --           COPY_FREE_VARS           1

 784           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas174_operator_audit_readiness_check.py", line 796>:
796           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88C40, file "scripts\pas174_operator_audit_readiness_check.py", line 796>:
796            RESUME                   0

797            BUILD_LIST               0
               STORE_FAST               1 (out)

798            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

799            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

800            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

801            BUILD_LIST               0
               STORE_FAST               5 (bad)

802            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

803            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

804            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

805            JUMP_BACKWARD           29 (to L2)

806    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

807            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

808    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

809            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

810    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

811            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

812    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

813            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

814    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

815    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

802    L9:     END_FOR
               POP_ITER

816            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

817            LOAD_CONST               8 ('self_check:no_env_or_db')

818            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

819   L11:     LOAD_CONST              11 ('PAS174 readiness checker never reads .env / touches DB')

820            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

821            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L12)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               0 ('')

816   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

823            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas174_operator_audit_readiness_check.py", line 830>:
830           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC46C0, file "scripts\pas174_operator_audit_readiness_check.py", line 830>:
 830            RESUME                   0

 832            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 831            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 832    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 833            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 832    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 833    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 832    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 831    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 836            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 835            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 836   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 837            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 836   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 837   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 836   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 835   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 840            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 841   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 842            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 839            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 831            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 835            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas174_operator_audit_readiness_check.py", line 846>:
846           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas174_operator_audit_readiness_check.py", line 846>:
846           RESUME                   0

847           BUILD_LIST               0
              STORE_FAST               1 (out)

848           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

849           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

850           JUMP_BACKWARD           19 (to L1)

851   L2:     LOAD_FAST_BORROW         2 (c)
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

852           LOAD_FAST                1 (out)
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

848   L5:     END_FOR
              POP_ITER

853           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas174_operator_audit_readiness_check.py", line 856>:
856           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C182DA4E0, file "scripts\pas174_operator_audit_readiness_check.py", line 856>:
856           RESUME                   0

857           BUILD_LIST               0
              STORE_FAST               1 (checks)

858           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_audit_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_connectivity_probes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_tenant_visibility_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_tenant_route + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_operator_actions_audit_wiring + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_v22_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

870           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

871           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

872           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_docs_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

873           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_governance_handbook + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

874           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

876           LOAD_GLOBAL             37 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

878           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS174')

879           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             39 (_now_iso + NULL)
              CALL                     0

880           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

881           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             40 (VERDICT_READY)
              COMPARE_OP              72 (==)

882           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

883           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

884           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

885           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pas174_operator_audit_readiness_check.py", line 885>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

886           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas174_operator_audit_readiness_check.py", line 886>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

887           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

888           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             47 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

877           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts\pas174_operator_audit_readiness_check.py", line 885>:
 885           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053AB0, file "scripts\pas174_operator_audit_readiness_check.py", line 886>:
 886           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas174_operator_audit_readiness_check.py", line 895>:
895           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CBD0, file "scripts\pas174_operator_audit_readiness_check.py", line 895>:
895           RESUME                   0

896           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

897           LOAD_CONST               0 ('pas174_operator_audit_readiness_check')

899           LOAD_CONST               1 ('PAS174 — Evaluate the operator audit layer + tenant visibility surface. Read-only — never reads .env, never touches Supabase, never runs a migration.')

896           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

905           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

906           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

907           LOAD_CONST               4 ('Repo root (default: parent of this script).')

905           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

909           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

910           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

911           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

909           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

913           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

914           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

915           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

913           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

917           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

918           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

919           LOAD_CONST              14 ('Skip writing the JSON report file.')

917           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

921           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

922           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

923           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

921           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

925           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas174_operator_audit_readiness_check.py", line 928>:
928           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas174_operator_audit_readiness_check.py", line 928>:
928           RESUME                   0

929           LOAD_GLOBAL              1 (print + NULL)

930           LOAD_CONST               0 ('[PAS174] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

931           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

932           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

933           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

934           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

935           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

930           BUILD_STRING            12

929           CALL                     1
              POP_TOP

937           LOAD_FAST_BORROW         0 (report)
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

938           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

939           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS174] operator actions:')
              CALL                     1
              POP_TOP

940           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

941           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

940   L3:     END_FOR
              POP_ITER

942           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

943           LOAD_GLOBAL              1 (print + NULL)
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

942   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

938   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "scripts\pas174_operator_audit_readiness_check.py", line 946>:
946           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC210, file "scripts\pas174_operator_audit_readiness_check.py", line 946>:
 946           RESUME                   0

 947           NOP

 948   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 949           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 950           LOAD_CONST               3 ('utf-8')

 948           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 952           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 953   L4:     LOAD_GLOBAL             11 (print + NULL)

 954           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 955           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 954           BUILD_STRING             4

 956           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 953           LOAD_CONST               7 (('file',))
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

 952   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts\pas174_operator_audit_readiness_check.py", line 960>:
960           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D87D80, file "scripts\pas174_operator_audit_readiness_check.py", line 960>:
 960            RESUME                   0

 961            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 962            NOP

 963    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 967    L2:     LOAD_GLOBAL             10 (os)
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

 968            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 969            LOAD_GLOBAL             23 (print + NULL)

 970            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 971            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 969            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 973            LOAD_SMALL_INT           2
                RETURN_VALUE

 975    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 977            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 978            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 980    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 982            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 983            LOAD_GLOBAL             23 (print + NULL)
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

 985    L6:     LOAD_FAST                5 (report)
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

 964            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 965    L9:     LOAD_FAST                3 (e)
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

 964   L17:     RERAISE                  0

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
