# scripts_readiness/pas177_tenant_audit_verification_readiness_check

- **pyc:** `scripts\__pycache__\pas177_tenant_audit_verification_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas177_tenant_audit_verification_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas177_tenant_audit_verification_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS177 — Durable tenant ACK + Merkle inclusion proofs readiness gate.

Deterministic, non-mutating evaluator for "is PAS177 wired
correctly and free of regressions in the PAS160-PAS176
doctrine?".

Walks the repo and verifies:

  * PAS160-PAS176 readiness scripts still exist.
  * PAS177 surfaces exist:
      - scripts/migrate_v25_tenant_audit_acknowledgements.sql
      - app/services/tenant/tenant_audit_ack_store.py
      - app/services/operator/merkle_inclusion_proofs.py
      - scripts/generate_audit_inclusion_proof.py
      - scripts/scheduled_audit_verification_template.py
      - scripts/pas177_tenant_audit_verification_readiness_check.py
      - docs/pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md
      - tests/mvp/test_pas177_tenant_audit_verification.py
  * v25 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed
    actor_type + acknowledgement_type enums + tenant
    INSERT scoped to own brokerage + append-only policies
    (no UPDATE / no DELETE for tenant AND service_role).
  * tenant_audit_ack_store exposes the documented surface
    (record / list / summary / exists + closed enums +
    metadata allow-list).
  * tenant_audit_ack_store has NO update / delete helpers
    (append-only invariant).
  * merkle_inclusion_proofs exposes the documented surface
    (build_merkle_tree / generate_inclusion_proof /
    verify_inclusion_proof / proof_for_audit_entry).
  * tenant_portal exposes the three new routes
    (GET /tenant/audit/acknowledgements,
    POST /tenant/audit/windows/{merkle_root_id}/acknowledge,
    GET /tenant/audit/{entry_id}/proof) AND the existing
    PAS176 POST /tenant/audit/{entry_id}/acknowledge.
  * generate_audit_inclusion_proof CLI is read-only.
  * scheduled_audit_verification_template CLI prints
    commands but never installs a scheduler.
  * No autonomous remediation surfaces.
  * audit_service.py STILL has no UPDATE / DELETE helpers
    (PAS174/PAS175/PAS176 carry-forward).
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio / TrustClaw
    / OpenAI / Anthropic imports.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS177 event type.
  * Worker still OFF by default; FastAPI lifespan does not
    auto-start the worker.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_ack_store`, `check_audit_service_invariant`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_prior_phases_intact`, `check_proof_script`, `check_proofs_service`, `check_self_no_env_or_db`, `check_template_script`, `check_tenant_routes`, `check_v25_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS177`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS177 — Durable tenant ACK + Merkle inclusion proofs readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS177 wired\ncorrectly and free of regressions in the PAS160-PAS176\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS176 readiness scripts still exist.\n  * PAS177 surfaces exist:\n      - scripts/migrate_v25_tenant_audit_acknowledgements.sql\n      - app/services/tenant/tenant_audit_ack_store.py\n      - app/services/operator/merkle_inclusion_proofs.py\n      - scripts/generate_audit_inclusion_proof.py\n      - scripts/scheduled_audit_verification_template.py\n      - scripts/pas177_tenant_audit_verification_readiness_check.py\n      - docs/pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md\n      - tests/mvp/test_pas177_tenant_audit_verification.py\n  * v25 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    actor_type + acknowledgement_type enums + tenant\n    INSERT scoped to own brokerage + append-only policies\n    (no UPDATE / no DELETE for tenant AND service_role).\n  * tenant_audit_ack_store exposes the documented surface\n    (record / list / summary / exists + closed enums +\n    metadata allow-list).\n  * tenant_audit_ack_store has NO update / delete helpers\n    (append-only invariant).\n  * merkle_inclusion_proofs exposes the documented surface\n    (build_merkle_tree / generate_inclusion_proof /\n    verify_inclusion_proof / proof_for_audit_entry).\n  * tenant_portal exposes the three new routes\n    (GET /tenant/audit/acknowledgements,\n    POST /tenant/audit/windows/{merkle_root_id}/acknowledge,\n    GET /tenant/audit/{entry_id}/proof) AND the existing\n    PAS176 POST /tenant/audit/{entry_id}/acknowledge.\n  * generate_audit_inclusion_proof CLI is read-only.\n  * scheduled_audit_verification_template CLI prints\n    commands but never installs a scheduler.\n  * No autonomous remediation surfaces.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174/PAS175/PAS176 carry-forward).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS177 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'severity'
- 'detail'
- 'pas177_tenant_audit_verification_readiness_report.json'
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
- 'Required PAS177 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS177 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS177 must not touch'
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
- 'tenant'
- 'tenant_audit_ack_store.py'
- 'ack_store:'
- 'Tenant ack store token: '
- 'missing token '
- 'ack_store:append_only_invariant'
- 'Tenant ack store has no UPDATE / DELETE mutation helpers'
- 'operator'
- 'merkle_inclusion_proofs.py'
- 'proofs:'
- 'Merkle inclusion proofs token: '
- 'routes'
- 'tenant_portal.py'
- 'tenant_routes:'
- 'Tenant route token: '
- 'require_brokerage'
- 'x_api_key'
- 'x_admin_key'
- 'tenant_routes:tenant_auth_only'
- 'Tenant routes use X-API-Key (require_brokerage), never admin'
- 'missing require_brokerage / x_api_key tokens'
- 'scripts'
- 'generate_audit_inclusion_proof.py'
- 'proof_script:'
- 'Proof script token: '
- 'proof_script:read_only'
- 'Proof script is read-only (no DB writes via the supabase fluent API)'
- 'disqualifying patterns: '
- 'scheduled_audit_verification_template.py'
- 'template_script:'
- 'Scheduled template script token: '
- 'template_script:no_automation'
- 'Scheduled template script does not install scheduler / call services / read env'
- 'PAS174/PAS175/PAS176 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS177 must preserve.'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'migrate_v25_tenant_audit_acknowledgements.sql'
- 'proposal only'
- 'v25_sql:proposal_only'
- "v25 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v25_sql:do_not_execute'
- "v25 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'CREATE TABLE IF NOT EXISTS pas_tenant_audit_acknowledgements'
- 'v25_sql:table_present'
- 'v25 SQL creates pas_tenant_audit_acknowledgements'
- 'missing CREATE TABLE'
- 'v25_sql:closed_actor_type_enum'
- 'v25 SQL carries the closed actor_type enum'
- 'missing one or more actor_type literals'
- 'v25_sql:closed_ack_type_enum'
- 'v25 SQL carries the closed acknowledgement_type enum'
- 'missing one or more ack_type literals'
- 'pas_tenant_audit_acks_tenant_no_update'
- 'pas_tenant_audit_acks_tenant_no_delete'
- 'pas_tenant_audit_acks_service_role_no_update'
- 'pas_tenant_audit_acks_service_role_no_delete'
- 'v25_sql:append_only_policies'
- 'v25 SQL denies tenant + service_role UPDATE/DELETE (append-only)'
- 'missing one or more no-update/no-delete policies'
- 'pas_tenant_audit_acks_tenant_insert'
- "WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'))"
- 'v25_sql:tenant_insert_scoped'
- 'v25 SQL scopes tenant INSERT to own brokerage_id'
- 'expected pas_tenant_audit_acks_tenant_insert policy with WITH CHECK clause'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/tenant/tenant_audit_ack_store.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md'
- 'docs:phrase:'
- 'Doctrine doc carries clause: '
- 'expected one of: '
- ' | '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'get_supabase'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS177 readiness checker never reads .env / touches DB'
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS177'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas177_tenant_audit_verification_readiness_check'
- 'PAS177 — Evaluate durable tenant ACK + Merkle inclusion proofs + scheduled verification template surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS177] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS177] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS177 — Durable tenant ACK + Merkle inclusion proofs readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS177 wired\ncorrectly and free of regressions in the PAS160-PAS176\ndoctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS176 readiness scripts still exist.\n  * PAS177 surfaces exist:\n      - scripts/migrate_v25_tenant_audit_acknowledgements.sql\n      - app/services/tenant/tenant_audit_ack_store.py\n      - app/services/operator/merkle_inclusion_proofs.py\n      - scripts/generate_audit_inclusion_proof.py\n      - scripts/scheduled_audit_verification_template.py\n      - scripts/pas177_tenant_audit_verification_readiness_check.py\n      - docs/pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md\n      - tests/mvp/test_pas177_tenant_audit_verification.py\n  * v25 SQL carries PROPOSAL ONLY + DO NOT EXECUTE + closed\n    actor_type + acknowledgement_type enums + tenant\n    INSERT scoped to own brokerage + append-only policies\n    (no UPDATE / no DELETE for tenant AND service_role).\n  * tenant_audit_ack_store exposes the documented surface\n    (record / list / summary / exists + closed enums +\n    metadata allow-list).\n  * tenant_audit_ack_store has NO update / delete helpers\n    (append-only invariant).\n  * merkle_inclusion_proofs exposes the documented surface\n    (build_merkle_tree / generate_inclusion_proof /\n    verify_inclusion_proof / proof_for_audit_entry).\n  * tenant_portal exposes the three new routes\n    (GET /tenant/audit/acknowledgements,\n    POST /tenant/audit/windows/{merkle_root_id}/acknowledge,\n    GET /tenant/audit/{entry_id}/proof) AND the existing\n    PAS176 POST /tenant/audit/{entry_id}/acknowledge.\n  * generate_audit_inclusion_proof CLI is read-only.\n  * scheduled_audit_verification_template CLI prints\n    commands but never installs a scheduler.\n  * No autonomous remediation surfaces.\n  * audit_service.py STILL has no UPDATE / DELETE helpers\n    (PAS174/PAS175/PAS176 carry-forward).\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio / TrustClaw\n    / OpenAI / Anthropic imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS177 event type.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  63           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  64           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  67           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  68           NOP

  69   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  67   L4:     END_FOR
               POP_ITER

  74           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  75           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  74           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  79           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  80           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  82           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  89           LOAD_CONST              73 (('scripts/migrate_v25_tenant_audit_acknowledgements.sql', 'app/services/tenant/tenant_audit_ack_store.py', 'app/services/operator/merkle_inclusion_proofs.py', 'scripts/generate_audit_inclusion_proof.py', 'scripts/scheduled_audit_verification_template.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'docs/pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md', 'tests/mvp/test_pas177_tenant_audit_verification.py'))
               STORE_NAME              28 (REQUIRED_FILES)

 100           LOAD_CONST              74 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 122           LOAD_CONST              75 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 132           LOAD_CONST              76 (('def record_tenant_audit_acknowledgement(', 'def list_tenant_audit_acknowledgements(', 'def tenant_acknowledgement_summary(', 'def acknowledgement_exists(', 'ALLOWED_ACTOR_TYPES', 'ALLOWED_ACKNOWLEDGEMENT_TYPES', 'ALLOWED_METADATA_KEYS', '_TABLE = "pas_tenant_audit_acknowledgements"', 'tenant_audit_ack_store_unavailable'))
               STORE_NAME              31 (REQUIRED_ACK_STORE_TOKENS)

 146           LOAD_CONST              77 (('def update_ack_', 'def delete_ack_', 'def update_acknowledgement_', 'def delete_acknowledgement_', 'def mutate_ack_', 'def truncate_ack_'))
               STORE_NAME              32 (FORBIDDEN_ACK_MUTATION_TOKENS)

 155           LOAD_CONST              78 (('def build_merkle_tree(', 'def generate_inclusion_proof(', 'def verify_inclusion_proof(', 'def proof_for_audit_entry('))
               STORE_NAME              33 (REQUIRED_PROOFS_TOKENS)

 162           LOAD_CONST              79 (('@router.post("/audit/{entry_id}/acknowledge")', '@router.get("/audit/acknowledgements")', '@router.post("/audit/windows/{merkle_root_id}/acknowledge")', '@router.get("/audit/{entry_id}/proof")', 'tenant_audit_acknowledgements_route', 'tenant_audit_window_acknowledge_route', 'tenant_audit_proof_route'))
               STORE_NAME              34 (REQUIRED_TENANT_ROUTE_TOKENS)

 174           LOAD_CONST              80 (('def generate(', '--brokerage-id', '--audit-entry-id', '--merkle-root-id', '--json', 'proof_for_audit_entry', 'verify_inclusion_proof'))
               STORE_NAME              35 (REQUIRED_PROOF_SCRIPT_TOKENS)

 184           LOAD_CONST              81 (('def _template_payload(', 'operator_command_sequence', 'constraints', 'recommended_interval'))
               STORE_NAME              36 (REQUIRED_TEMPLATE_SCRIPT_TOKENS)

 193           LOAD_CONST              82 (('subprocess.run', 'subprocess.Popen', 'schedule.every', 'crontab', 'httpx', 'requests.', 'os.environ.get', 'os.environ[', 'load_dotenv'))
               STORE_NAME              37 (FORBIDDEN_TEMPLATE_AUTOMATION_TOKENS)

 206           LOAD_CONST              83 (('audit.merkle.root_persisted', 'tenant.audit.acknowledged', 'tenant.audit.acknowledgement.failed', 'tenant.audit.proof.generated', 'tenant.audit.proof.verification_failed', 'audit.verification.scheduled_template_generated'))
               STORE_NAME              38 (REQUIRED_EVENT_TYPES)

 218           LOAD_CONST              84 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              39 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 243           LOAD_CONST              85 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              40 (FORBIDDEN_INBOX_TOKENS)

 257           LOAD_CONST              12 ('severity')

 259           LOAD_NAME               27 (SEVERITY_BLOCK)

 257           LOAD_CONST              13 ('detail')

 259           LOAD_CONST              14 ('')

 257           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18026630, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 257>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _check at 0x0000018C17FA34B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 257>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 270           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 270>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _now_iso at 0x0000018C18038F30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 270>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 274           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 274>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _read_text at 0x0000018C18053630, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 274>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 281           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 320           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 320>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_files_present at 0x0000018C18061470, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 320>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 333           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 333>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 333>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_prior_phases_intact)

 346           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 346>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 346>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_intact)

 359           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 359>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 359>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_worker_off_by_default)

 376           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 376>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_startup_worker at 0x0000018C17D87850, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 376>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_no_startup_worker)

 399           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C181143F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 399>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_ack_store at 0x0000018C182FF320, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 399>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_ack_store)

 425           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C181144E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 425>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_proofs_service at 0x0000018C17FEE230, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 425>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_proofs_service)

 440           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 440>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_tenant_routes at 0x0000018C17D875A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 440>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_tenant_routes)

 467           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C181146C0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 467>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_proof_script at 0x0000018C182FFEA0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 467>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_proof_script)

 515           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C181147B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 515>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_template_script at 0x0000018C182FED60, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 515>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_template_script)

 543           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C181148A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 543>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_audit_service_invariant at 0x0000018C17D76780, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 543>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_audit_service_invariant)

 570           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 570>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_v25_sql at 0x0000018C17D8BF50, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 570>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_v25_sql)

 650           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 650>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_event_contract at 0x0000018C1801C9E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 650>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_event_contract)

 665           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C18114B70, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 665>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_no_forbidden_imports at 0x0000018C17F74690, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 665>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_forbidden_imports)

 697           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 697>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC2960, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 697>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_inbox_scan_tokens)

 726           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C18114E40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 726>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_doc_required_clauses at 0x0000018C17CD2160, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 726>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_doc_required_clauses)

 764           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C18114F30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 764>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 764>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_self_no_env_or_db)

 797           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 797>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _aggregate at 0x0000018C1800B0A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 797>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_aggregate)

 809           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18115110, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 809>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 809>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_operator_actions)

 819           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18115200, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 819>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object evaluate at 0x0000018C182DA010, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 819>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (evaluate)

 855           LOAD_CONST              63 ('pas177_tenant_audit_verification_readiness_report.json')
               STORE_NAME              65 (REPORT_FILENAME)

 858           LOAD_CONST              64 (<code object __annotate__ at 0x0000018C181153E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 858>)
               MAKE_FUNCTION
               LOAD_CONST              65 (<code object _build_parser at 0x0000018C180FC5D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 858>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_build_parser)

 876           LOAD_CONST              66 (<code object __annotate__ at 0x0000018C181154D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 876>)
               MAKE_FUNCTION
               LOAD_CONST              67 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 876>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_print_summary)

 894           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 894>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _write_report at 0x0000018C180FC7B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 894>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_write_report)

 908           LOAD_CONST              86 ((None,))
               LOAD_CONST              70 (<code object __annotate__ at 0x0000018C181155C0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 908>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object main at 0x0000018C17D88C40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 908>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              69 (main)

 933           LOAD_NAME               70 (__name__)
               LOAD_CONST              72 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 934           LOAD_NAME                6 (sys)
               LOAD_ATTR              142 (exit)
               PUSH_NULL
               LOAD_NAME               69 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 933   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  70           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  71   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          359 (to L1)

  70   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026630, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 257>:
257           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

258           LOAD_CONST               2 ('str')

257           LOAD_CONST               3 ('status')

258           LOAD_CONST               2 ('str')

257           LOAD_CONST               4 ('label')

258           LOAD_CONST               2 ('str')

257           LOAD_CONST               5 ('severity')

259           LOAD_CONST               2 ('str')

257           LOAD_CONST               6 ('detail')

259           LOAD_CONST               2 ('str')

257           LOAD_CONST               7 ('return')

260           LOAD_CONST               8 ('dict')

257           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA34B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 257>:
257           RESUME                   0

262           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

263           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

264           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

265           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

266           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

261           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 270>:
270           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 270>:
270           RESUME                   0

271           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 274>:
274           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053630, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 274>:
 274           RESUME                   0

 275           NOP

 276   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 277           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 278   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 277   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 281>:
281           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 281>:
281            RESUME                   0

282            BUILD_LIST               0
               STORE_FAST               1 (out)

283            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

284    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

285            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

286            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

287            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

288            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

289            JUMP_FORWARD           240 (to L13)

290    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

291            JUMP_BACKWARD           59 (to L1)

292    L3:     LOAD_FAST_BORROW         0 (src)
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

293    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

294            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

295            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

296            JUMP_FORWARD           138 (to L13)

297    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

298            JUMP_BACKWARD          161 (to L1)

299    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

300            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

301            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

302    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

303            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

304            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

305            JUMP_BACKWARD           30 (to L7)

306    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

307    L9:     JUMP_FORWARD            11 (to L11)

308   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

309   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

310            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

311   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

312            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

313   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 320>:
320           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C18061470, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 320>:
320           RESUME                   0

321           BUILD_LIST               0
              STORE_FAST               1 (out)

322           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

323           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

324           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

325           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

326           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

327   L3:     LOAD_CONST               3 ('Required PAS177 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

328           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

324   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

322   L6:     END_FOR
              POP_ITER

330           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 333>:
333           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 333>:
333           RESUME                   0

334           BUILD_LIST               0
              STORE_FAST               1 (out)

335           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

336           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

337           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

338           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

339           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

340   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

341           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS177 must not delete')

337   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

335   L6:     END_FOR
              POP_ITER

343           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 346>:
346           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 346>:
346           RESUME                   0

347           BUILD_LIST               0
              STORE_FAST               1 (out)

348           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

349           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

350           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

351           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

352           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

353   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

354           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS177 must not touch')

350   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

348   L6:     END_FOR
              POP_ITER

356           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 359>:
359           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C179C3C30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 359>:
359           RESUME                   0

360           BUILD_LIST               0
              STORE_FAST               1 (out)

361           LOAD_GLOBAL              1 (Path + NULL)
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

362           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

364           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

365           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

363   L2:     STORE_FAST               4 (literal_ok)

367           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

368           LOAD_CONST               7 ('worker:off_by_default')

369           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

370   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

371           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

367   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

373           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 376>:
376           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D87850, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 376>:
376           RESUME                   0

377           BUILD_LIST               0
              STORE_FAST               1 (out)

378           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

379           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

380           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

381           BUILD_LIST               0
              STORE_FAST               5 (bad)

382           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

383           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

384   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

385           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

386   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

387           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

388   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

389           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

390   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

391           LOAD_CONST              10 ('main:no_startup_worker')

392           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

393   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

394           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE       25 (to L8)
              NOT_TAKEN
              LOAD_CONST              14 ('disqualifying tokens: ')
              LOAD_CONST              15 (', ')
              LOAD_ATTR               11 (join + NULL|self)
              LOAD_FAST_BORROW         5 (bad)
              CALL                     1
              BINARY_OP                0 (+)
              JUMP_FORWARD             1 (to L9)
      L8:     LOAD_CONST               2 ('')

390   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

396           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 399>:
399           RESUME                   0
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

Disassembly of <code object check_ack_store at 0x0000018C182FF320, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 399>:
399            RESUME                   0

400            BUILD_LIST               0
               STORE_FAST               1 (out)

401            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('tenant_audit_ack_store.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

402            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

403            LOAD_GLOBAL              4 (REQUIRED_ACK_STORE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

404            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

405            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

406            LOAD_CONST               5 ('ack_store:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

407            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

408    L4:     LOAD_CONST               9 ('Tenant ack store token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

409            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

405    L6:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

403    L7:     END_FOR
               POP_ITER

412            BUILD_LIST               0
               STORE_FAST               6 (bad)

413            LOAD_GLOBAL             10 (FORBIDDEN_ACK_MUTATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

414            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

415    L9:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

413   L10:     END_FOR
               POP_ITER

416            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

417            LOAD_CONST              12 ('ack_store:append_only_invariant')

418            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               7 ('PASS')

419   L12:     LOAD_CONST              13 ('Tenant ack store has no UPDATE / DELETE mutation helpers')

420            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              14 ('disqualifying tokens: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               4 ('')

416   L14:     LOAD_CONST              11 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

422            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 425>:
425           RESUME                   0
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

Disassembly of <code object check_proofs_service at 0x0000018C17FEE230, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 425>:
425           RESUME                   0

426           BUILD_LIST               0
              STORE_FAST               1 (out)

427           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('operator')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('merkle_inclusion_proofs.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

428           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

429           LOAD_GLOBAL              4 (REQUIRED_PROOFS_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

430           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

431           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

432           LOAD_CONST               5 ('proofs:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

433           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

434   L4:     LOAD_CONST               9 ('Merkle inclusion proofs token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

435           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

431   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

429   L7:     END_FOR
              POP_ITER

437           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 440>:
440           RESUME                   0
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

Disassembly of <code object check_tenant_routes at 0x0000018C17D875A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 440>:
440            RESUME                   0

441            BUILD_LIST               0
               STORE_FAST               1 (out)

442            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant_portal.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

443            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

444            LOAD_GLOBAL              4 (REQUIRED_TENANT_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

445            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

446            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

447            LOAD_CONST               4 ('tenant_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

448            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

449    L4:     LOAD_CONST               8 ('Tenant route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

450            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

446    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

444    L7:     END_FOR
               POP_ITER

454            LOAD_CONST              11 ('require_brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L8)
               NOT_TAKEN
               POP_TOP

455            LOAD_CONST              12 ('x_api_key')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

454            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN
               POP_TOP

456            LOAD_CONST              13 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              1 (not in)

453    L8:     STORE_FAST               6 (auth_ok)

458            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

459            LOAD_CONST              14 ('tenant_routes:tenant_auth_only')

460            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('FAIL')

461   L10:     LOAD_CONST              15 ('Tenant routes use X-API-Key (require_brokerage), never admin')

462            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing require_brokerage / x_api_key tokens')

458   L12:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

464            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181146C0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 467>:
467           RESUME                   0
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

Disassembly of <code object check_proof_script at 0x0000018C182FFEA0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 467>:
467            RESUME                   0

468            BUILD_LIST               0
               STORE_FAST               1 (out)

469            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('generate_audit_inclusion_proof.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

470            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

471            LOAD_GLOBAL              4 (REQUIRED_PROOF_SCRIPT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

472            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

473            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

474            LOAD_CONST               3 ('proof_script:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

475            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

476    L4:     LOAD_CONST               7 ('Proof script token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

477            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

473    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

471    L7:     END_FOR
               POP_ITER

484            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

485            BUILD_LIST               0
               STORE_FAST               7 (bad)

486            LOAD_CONST              14 (('table(_AUDIT_TABLE).insert', 'table(_MERKLE_TABLE).insert', 'table(_TABLE).insert', 'table("pas_', '.insert({', '.insert([', '.update({', '.delete().execute', '.delete().eq'))
               STORE_FAST               8 (write_patterns)

497            LOAD_FAST_BORROW         8 (write_patterns)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               9 (verb)

498            LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (verb, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

499    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         9 (verb)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

497   L10:     END_FOR
               POP_ITER

506            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

507            LOAD_CONST              10 ('proof_script:read_only')

508            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

509   L12:     LOAD_CONST              11 ('Proof script is read-only (no DB writes via the supabase fluent API)')

510            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying patterns: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               13 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               2 ('')

506   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

512            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 515>:
515           RESUME                   0
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

Disassembly of <code object check_template_script at 0x0000018C182FED60, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 515>:
515            RESUME                   0

516            BUILD_LIST               0
               STORE_FAST               1 (out)

517            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('scheduled_audit_verification_template.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

518            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

519            LOAD_GLOBAL              4 (REQUIRED_TEMPLATE_SCRIPT_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

520            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

521            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

522            LOAD_CONST               3 ('template_script:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               4 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

523            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               5 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               6 ('FAIL')

524    L4:     LOAD_CONST               7 ('Scheduled template script token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

525            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               8 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

521    L6:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

519    L7:     END_FOR
               POP_ITER

529            LOAD_GLOBAL             11 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

530            BUILD_LIST               0
               STORE_FAST               7 (bad)

531            LOAD_GLOBAL             12 (FORBIDDEN_TEMPLATE_AUTOMATION_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

532            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

533    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

531   L10:     END_FOR
               POP_ITER

534            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

535            LOAD_CONST              10 ('template_script:no_automation')

536            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               6 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

537   L12:     LOAD_CONST              11 ('Scheduled template script does not install scheduler / call services / read env')

538            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L13)
               NOT_TAKEN
               LOAD_CONST              12 ('disqualifying tokens: ')
               LOAD_CONST              13 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               2 ('')

534   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

540            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181148A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 543>:
543           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C17D76780, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 543>:
543           RESUME                   0

546           BUILD_LIST               0
              STORE_FAST               1 (out)

547           LOAD_GLOBAL              1 (Path + NULL)
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

548           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

549           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

557           BUILD_LIST               0
              STORE_FAST               5 (bad)

558           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

559           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

560   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

558   L4:     END_FOR
              POP_ITER

561           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

562           LOAD_CONST               6 ('audit_service:append_only_carry')

563           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

564   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

565           LOAD_FAST_BORROW         5 (bad)
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

561   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

567           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 570>:
570           RESUME                   0
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

Disassembly of <code object check_v25_sql at 0x0000018C17D8BF50, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 570>:
  --            MAKE_CELL               11 (src)

 570            RESUME                   0

 571            BUILD_LIST               0
                STORE_FAST               1 (out)

 572            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v25_tenant_audit_acknowledgements.sql')
                BINARY_OP               11 (/)
                STORE_FAST               2 (p)

 573            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (p)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_DEREF             11 (src)

 574            LOAD_DEREF              11 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (lower)

 575            LOAD_CONST               3 ('proposal only')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               4 (proposal_ok)

 576            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 577            LOAD_CONST               4 ('v25_sql:proposal_only')

 578            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 579    L3:     LOAD_CONST               7 ("v25 SQL carries 'PROPOSAL ONLY' guardrail")

 580            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               8 ("missing 'PROPOSAL ONLY' label")

 576    L5:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 582            LOAD_CONST              10 ('do not execute')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)
                STORE_FAST               5 (do_not_exec)

 583            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 584            LOAD_CONST              11 ('v25_sql:do_not_execute')

 585            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 586    L7:     LOAD_CONST              12 ("v25 SQL carries 'DO NOT EXECUTE' trailer")

 587            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST              13 ('missing trailer')

 583    L9:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 589            LOAD_CONST              14 ('CREATE TABLE IF NOT EXISTS pas_tenant_audit_acknowledgements')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                STORE_FAST               6 (table_ok)

 590            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 591            LOAD_CONST              15 ('v25_sql:table_present')

 592            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               6 ('FAIL')

 593   L11:     LOAD_CONST              16 ('v25 SQL creates pas_tenant_audit_acknowledgements')

 594            LOAD_FAST_BORROW         6 (table_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST              17 ('missing CREATE TABLE')

 590   L13:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 597            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L17)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 597>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 598            LOAD_CONST              40 (("'TENANT'", "'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 597            CALL                     0
       L14:     FOR_ITER                12 (to L16)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L14)
       L15:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L18)
       L16:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L18)
       L17:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              18 (<code object <genexpr> at 0x0000018C18025530, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 597>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 598            LOAD_CONST              40 (("'TENANT'", "'OPERATOR'", "'ADMIN'", "'SYSTEM'"))
                GET_ITER

 597            CALL                     0
                CALL                     1
       L18:     STORE_FAST               7 (actor_types_ok)

 600            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 601            LOAD_CONST              21 ('v25_sql:closed_actor_type_enum')

 602            LOAD_FAST_BORROW         7 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L19)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L20)
       L19:     LOAD_CONST               6 ('FAIL')

 603   L20:     LOAD_CONST              22 ('v25 SQL carries the closed actor_type enum')

 604            LOAD_FAST_BORROW         7 (actor_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L22)
       L21:     LOAD_CONST              23 ('missing one or more actor_type literals')

 600   L22:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 607            LOAD_GLOBAL             10 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L26)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 607>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 608            LOAD_CONST              41 (("'AUDIT_ENTRY_VIEWED'", "'AUDIT_WINDOW_ACKNOWLEDGED'", "'MERKLE_ROOT_ACKNOWLEDGED'", "'CHAIN_STATUS_VIEWED'"))
                GET_ITER

 607            CALL                     0
       L23:     FOR_ITER                12 (to L25)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L23)
       L24:     POP_ITER
                LOAD_CONST              19 (False)
                JUMP_FORWARD            20 (to L27)
       L25:     END_FOR
                POP_ITER
                LOAD_CONST              20 (True)
                JUMP_FORWARD            16 (to L27)
       L26:     PUSH_NULL
                LOAD_FAST_BORROW        11 (src)
                BUILD_TUPLE              1
                LOAD_CONST              24 (<code object <genexpr> at 0x0000018C18024930, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 607>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 608            LOAD_CONST              41 (("'AUDIT_ENTRY_VIEWED'", "'AUDIT_WINDOW_ACKNOWLEDGED'", "'MERKLE_ROOT_ACKNOWLEDGED'", "'CHAIN_STATUS_VIEWED'"))
                GET_ITER

 607            CALL                     0
                CALL                     1
       L27:     STORE_FAST               8 (ack_types_ok)

 615            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 616            LOAD_CONST              25 ('v25_sql:closed_ack_type_enum')

 617            LOAD_FAST_BORROW         8 (ack_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L28)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L29)
       L28:     LOAD_CONST               6 ('FAIL')

 618   L29:     LOAD_CONST              26 ('v25 SQL carries the closed acknowledgement_type enum')

 619            LOAD_FAST_BORROW         8 (ack_types_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L30)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L31)
       L30:     LOAD_CONST              27 ('missing one or more ack_type literals')

 615   L31:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 623            LOAD_CONST              28 ('pas_tenant_audit_acks_tenant_no_update')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L32)
                NOT_TAKEN
                POP_TOP

 624            LOAD_CONST              29 ('pas_tenant_audit_acks_tenant_no_delete')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 623            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L32)
                NOT_TAKEN
                POP_TOP

 625            LOAD_CONST              30 ('pas_tenant_audit_acks_service_role_no_update')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 623            COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L32)
                NOT_TAKEN
                POP_TOP

 626            LOAD_CONST              31 ('pas_tenant_audit_acks_service_role_no_delete')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 622   L32:     STORE_FAST               9 (append_only_ok)

 628            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 629            LOAD_CONST              32 ('v25_sql:append_only_policies')

 630            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L34)
       L33:     LOAD_CONST               6 ('FAIL')

 631   L34:     LOAD_CONST              33 ('v25 SQL denies tenant + service_role UPDATE/DELETE (append-only)')

 632            LOAD_FAST_BORROW         9 (append_only_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L35)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L36)
       L35:     LOAD_CONST              34 ('missing one or more no-update/no-delete policies')

 628   L36:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 636            LOAD_CONST              35 ('pas_tenant_audit_acks_tenant_insert')
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L37)
                NOT_TAKEN
                POP_TOP

 637            LOAD_CONST              36 ("WITH CHECK (brokerage_id = (auth.jwt() ->> 'brokerage_id'))")
                LOAD_DEREF              11 (src)
                CONTAINS_OP              0 (in)

 635   L37:     STORE_FAST              10 (insert_scoped)

 639            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 640            LOAD_CONST              37 ('v25_sql:tenant_insert_scoped')

 641            LOAD_FAST_BORROW        10 (insert_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L38)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L39)
       L38:     LOAD_CONST               6 ('FAIL')

 642   L39:     LOAD_CONST              38 ('v25 SQL scopes tenant INSERT to own brokerage_id')

 643            LOAD_FAST_BORROW        10 (insert_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L40)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L41)

 644   L40:     LOAD_CONST              39 ('expected pas_tenant_audit_acks_tenant_insert policy with WITH CHECK clause')

 639   L41:     LOAD_CONST               9 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 647            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025530, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 597>:
  --           COPY_FREE_VARS           1

 597           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 598   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object <genexpr> at 0x0000018C18024930, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 607>:
  --           COPY_FREE_VARS           1

 607           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 608   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 650>:
650           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C1801C9E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 650>:
650           RESUME                   0

651           BUILD_LIST               0
              STORE_FAST               1 (out)

652           LOAD_GLOBAL              1 (Path + NULL)
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

653           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

654           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

655           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

656           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

657           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

658           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

659   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

660           LOAD_FAST_BORROW         5 (ok)
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

656   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

654   L7:     END_FOR
              POP_ITER

662           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 665>:
665           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F74690, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 665>:
665            RESUME                   0

666            BUILD_LIST               0
               STORE_FAST               1 (out)

667            LOAD_CONST              10 (('app/services/tenant/tenant_audit_ack_store.py', 'app/services/operator/merkle_inclusion_proofs.py', 'scripts/generate_audit_inclusion_proof.py', 'scripts/scheduled_audit_verification_template.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py'))
               STORE_FAST               2 (files)

674            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

675            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

676            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

677            JUMP_BACKWARD           46 (to L1)

678    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

679            BUILD_LIST               0
               STORE_FAST               6 (bad)

680            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

681            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

682            LOAD_FAST_BORROW         8 (stripped)
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

683    L5:     JUMP_BACKWARD           52 (to L4)

684    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

685            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

686    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

684    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

680   L10:     END_FOR
               POP_ITER

687            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

688            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

689            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

690   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

692            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

691            LOAD_CONST               7 ('forbidden import prefixes: ')
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

692   L13:     LOAD_CONST               1 ('')

687   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

674   L15:     END_FOR
               POP_ITER

694            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 697>:
697           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC2960, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 697>:
697            RESUME                   0

698            BUILD_LIST               0
               STORE_FAST               1 (out)

699            LOAD_CONST               9 (('app/services/tenant/tenant_audit_ack_store.py', 'app/services/operator/merkle_inclusion_proofs.py', 'scripts/generate_audit_inclusion_proof.py', 'scripts/scheduled_audit_verification_template.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py'))
               STORE_FAST               2 (files)

706            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

707            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

708            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

709            JUMP_BACKWARD           45 (to L1)

710    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

711            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

712            BUILD_LIST               0
               STORE_FAST               7 (bad)

713            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

714            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

715    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

713    L6:     END_FOR
               POP_ITER

716            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

717            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

718            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

719    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

721            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

720            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

721    L9:     LOAD_CONST               1 ('')

716   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

706   L11:     END_FOR
               POP_ITER

723            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114E40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 726>:
726           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17CD2160, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 726>:
  --            MAKE_CELL                8 (lower)

 726            RESUME                   0

 727            BUILD_LIST               0
                STORE_FAST               1 (out)

 728            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas177_tenant_audit_acknowledgements_and_inclusion_proofs.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 729            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 730            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 731            LOAD_CONST              13 ((('purpose', ('purpose',)), ('tenant-ack-doctrine', ('tenant acknowledgement doctrine', 'acknowledgement doctrine')), ('append-only', ('append-only',)), ('merkle-inclusion-proof', ('merkle inclusion proof',)), ('no-autonomous', ('no autonomous', 'no-autonomous', 'no automatic remediation')), ('scheduled-template', ('scheduled verification template', 'scheduled-verification template')), ('non-repudiation', ('non-repudiation',)), ('daily-cadence', ('daily verification cadence', 'daily verification', 'daily cadence')), ('rollback', ('rollback',)), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 752            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 753            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 753>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 753>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 754            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 755            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 756            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 757    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 759            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 758            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 759   L10:     LOAD_CONST               2 ('')

 754   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 752   L12:     END_FOR
                POP_ITER

 761            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 753>:
  --           COPY_FREE_VARS           1

 753           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 764>:
764           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D89750, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 764>:
764            RESUME                   0

765            BUILD_LIST               0
               STORE_FAST               1 (out)

766            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

767            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

768            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

769            BUILD_LIST               0
               STORE_FAST               5 (bad)

770            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

771            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

772            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

773            JUMP_BACKWARD           29 (to L2)

774    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

775            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

776    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

777            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

778    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

779            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

780    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

781            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

782    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

783    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

770    L9:     END_FOR
               POP_ITER

784            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

785            LOAD_CONST               8 ('self_check:no_env_or_db')

786            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

787   L11:     LOAD_CONST              11 ('PAS177 readiness checker never reads .env / touches DB')

788            LOAD_FAST_BORROW         5 (bad)
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

784   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

790            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 797>:
797           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C1800B0A0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 797>:
 797            RESUME                   0

 799            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 798            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 799    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 800            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 799    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 800    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 799    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 798    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 803            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 804   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 805            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 802            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 798            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 809>:
809           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048AB0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 809>:
809           RESUME                   0

810           BUILD_LIST               0
              STORE_FAST               1 (out)

811           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

812           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

813           JUMP_BACKWARD           19 (to L1)

814   L2:     LOAD_FAST_BORROW         2 (c)
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

815           LOAD_FAST                1 (out)
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

811   L5:     END_FOR
              POP_ITER

816           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 819>:
819           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C182DA010, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 819>:
819           RESUME                   0

820           BUILD_LIST               0
              STORE_FAST               1 (checks)

821           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

822           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

823           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

824           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

825           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

826           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_ack_store + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

827           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_proofs_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

828           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_tenant_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

829           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_proof_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

830           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_template_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

831           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

832           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_v25_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

833           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

834           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

835           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

836           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

837           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

839           LOAD_GLOBAL             37 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

841           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS177')

842           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             39 (_now_iso + NULL)
              CALL                     0

843           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

844           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             40 (VERDICT_READY)
              COMPARE_OP              72 (==)

845           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

846           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

847           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

848           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180533F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 848>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

849           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053990, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 849>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

850           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

851           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             47 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

840           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 848>:
 848           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 849>:
 849           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 858>:
858           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC5D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 858>:
858           RESUME                   0

859           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

860           LOAD_CONST               0 ('pas177_tenant_audit_verification_readiness_check')

862           LOAD_CONST               1 ('PAS177 — Evaluate durable tenant ACK + Merkle inclusion proofs + scheduled verification template surfaces. Read-only — never reads .env, never touches Supabase, never runs a migration.')

859           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

868           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

869           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

870           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

871           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

872           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

873           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181154D0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 876>:
876           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 876>:
876           RESUME                   0

877           LOAD_GLOBAL              1 (print + NULL)

878           LOAD_CONST               0 ('[PAS177] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

879           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

880           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

881           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

882           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

883           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

878           BUILD_STRING            12

877           CALL                     1
              POP_TOP

885           LOAD_FAST_BORROW         0 (report)
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

886           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

887           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS177] operator actions:')
              CALL                     1
              POP_TOP

888           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

889           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

888   L3:     END_FOR
              POP_ITER

890           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

891           LOAD_GLOBAL              1 (print + NULL)
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

890   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

886   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 894>:
894           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC7B0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 894>:
 894           RESUME                   0

 895           NOP

 896   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 897           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 898           LOAD_CONST               3 ('utf-8')

 896           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 900           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 901   L4:     LOAD_GLOBAL             11 (print + NULL)

 902           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 903           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 902           BUILD_STRING             4

 904           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 901           LOAD_CONST               7 (('file',))
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

 900   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 908>:
908           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88C40, file "scripts\pas177_tenant_audit_verification_readiness_check.py", line 908>:
 908            RESUME                   0

 909            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 910            NOP

 911    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 915    L2:     LOAD_GLOBAL             10 (os)
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

 916            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 917            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 918            LOAD_SMALL_INT           2
                RETURN_VALUE

 920    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 922            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 923            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 925    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 927            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 928            LOAD_GLOBAL             23 (print + NULL)
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

 930    L6:     LOAD_FAST                5 (report)
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

 912            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 913    L9:     LOAD_FAST                3 (e)
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

 912   L17:     RERAISE                  0

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
