# scripts_readiness/pas182_adaptive_memory_bridge_readiness_check

- **pyc:** `scripts\__pycache__\pas182_adaptive_memory_bridge_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas182_adaptive_memory_bridge_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas182_adaptive_memory_bridge_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS182 — Adaptive memory bridge readiness gate.

Deterministic, non-mutating evaluator for "is PAS182 wired
correctly and free of regressions in the PAS160-PAS181 +
PAS-SECURITY-01/02/03/04 doctrine?".

Walks the repo and verifies:

  * Prior phases (PAS160-PAS181 + PAS-SECURITY-01/02/03/04)
    readiness scripts still exist.
  * PAS182 surfaces exist:
      - app/services/learning/adaptive_memory_bridge.py
      - app/services/learning/adaptive_memory_projection.py
      - app/routes/operator_adaptive_memory.py
      - app/routes/tenant_adaptive_memory.py
      - scripts/pas182_adaptive_memory_bridge_readiness_check.py
      - docs/pas182_adaptive_memory_bridge.md
      - tests/mvp/test_pas182_adaptive_memory_bridge.py
  * adaptive_memory_bridge exposes documented surface, closed
    reason-code enum, low-risk + high-confidence thresholds,
    CANDIDATE-only invariants.
  * adaptive_memory_projection exposes closed operator and
    tenant allow-lists; tenant projection strictly narrower.
  * operator_adaptive_memory has the 2 documented routes
    under require_admin with the PAS-SECURITY-04 rate-limit
    pattern.
  * tenant_adaptive_memory has the 1 documented GET route
    under require_brokerage; no POST surface.
  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /
    DEPLOYED / APPROVED) in PAS182 source.
  * No auto-approval / live-mutation tokens.
  * No live-mutation imports (state_machine / memory review /
    approval / booking / outbound / worker / slack).
  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /
    POP3 / inbox-scanning / Composio / TrustClaw imports.
  * Memory Review (PAS147-PAS158) untouched.
  * audit_service.py STILL has no UPDATE / DELETE helpers.
  * PAS179 / PAS180 / PAS181 services intact.
  * PAS163 candidate pipeline intact + reachable.
  * Event contract registers every PAS182 event type.
  * main.py mounts both new routers.
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

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_audit_service_invariant`, `check_bridge_service`, `check_doc_required_clauses`, `check_event_contract`, `check_files_present`, `check_main_router_mounts`, `check_memory_review_intact`, `check_no_auto_approval_tokens`, `check_no_forbidden_imports`, `check_no_forbidden_status_tokens`, `check_no_inbox_scan_tokens`, `check_no_live_mutation_imports`, `check_no_startup_worker`, `check_operator_routes`, `check_prior_phases_intact`, `check_projection_service`, `check_self_no_env_or_db`, `check_tenant_routes`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `NOT_READY`, `PAS182`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS182 — Adaptive memory bridge readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS182 wired\ncorrectly and free of regressions in the PAS160-PAS181 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * Prior phases (PAS160-PAS181 + PAS-SECURITY-01/02/03/04)\n    readiness scripts still exist.\n  * PAS182 surfaces exist:\n      - app/services/learning/adaptive_memory_bridge.py\n      - app/services/learning/adaptive_memory_projection.py\n      - app/routes/operator_adaptive_memory.py\n      - app/routes/tenant_adaptive_memory.py\n      - scripts/pas182_adaptive_memory_bridge_readiness_check.py\n      - docs/pas182_adaptive_memory_bridge.md\n      - tests/mvp/test_pas182_adaptive_memory_bridge.py\n  * adaptive_memory_bridge exposes documented surface, closed\n    reason-code enum, low-risk + high-confidence thresholds,\n    CANDIDATE-only invariants.\n  * adaptive_memory_projection exposes closed operator and\n    tenant allow-lists; tenant projection strictly narrower.\n  * operator_adaptive_memory has the 2 documented routes\n    under require_admin with the PAS-SECURITY-04 rate-limit\n    pattern.\n  * tenant_adaptive_memory has the 1 documented GET route\n    under require_brokerage; no POST surface.\n  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /\n    DEPLOYED / APPROVED) in PAS182 source.\n  * No auto-approval / live-mutation tokens.\n  * No live-mutation imports (state_machine / memory review /\n    approval / booking / outbound / worker / slack).\n  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /\n    POP3 / inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers.\n  * PAS179 / PAS180 / PAS181 services intact.\n  * PAS163 candidate pipeline intact + reachable.\n  * Event contract registers every PAS182 event type.\n  * main.py mounts both new routers.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'severity'
- 'detail'
- 'pas182_adaptive_memory_bridge_readiness_report.json'
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
- 'Required PAS182 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS182 must not delete'
- 'pas179_181_service:'
- 'PAS179/PAS180/PAS181 service intact: '
- 'service deleted — PAS182 must not touch'
- 'pas163_pipeline:'
- 'PAS163 memory candidate pipeline intact: '
- 'PAS163 file missing — bridge cannot create CANDIDATEs'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS182 must not touch'
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
- 'learning'
- 'adaptive_memory_bridge.py'
- 'bridge:'
- 'Adaptive-memory bridge token: '
- 'missing token '
- 'adaptive_memory_projection.py'
- 'projection:'
- 'Adaptive-memory projection token: '
- 'routes'
- 'operator_adaptive_memory.py'
- 'operator_routes:'
- 'Operator adaptive-memory route token: '
- 'require_admin'
- 'x_admin_key'
- 'operator_routes:require_admin'
- 'Operator adaptive-memory routes use require_admin (X-Admin-Key)'
- 'missing require_admin / X-Admin-Key tokens'
- 'tenant_adaptive_memory.py'
- 'tenant_routes:'
- 'Tenant adaptive-memory route token: '
- 'require_brokerage'
- 'x_api_key'
- 'tenant_routes:tenant_auth_only'
- 'Tenant adaptive-memory routes use X-API-Key (require_brokerage), never admin'
- 'missing require_brokerage / x_api_key tokens'
- '@router.post'
- 'tenant_routes:no_mutation_surface'
- 'Tenant adaptive-memory routes have NO @router.post surface'
- 'tenant route file declares a POST route'
- 'app/services/learning/adaptive_memory_bridge.py'
- 'no_forbidden_status:'
- 'No forbidden status tokens: '
- 'no_auto_approval:'
- 'No auto-approval / live-mutation tokens: '
- 'no_live_mutation_import:'
- 'No live-mutation imports: '
- 'forbidden imports: '
- 'PAS174-PAS181 invariant: audit_service has no\nUPDATE / DELETE helpers. PAS182 must preserve.'
- 'operator'
- 'audit_service.py'
- 'audit_service:append_only_carry'
- 'Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'main:mount:'
- 'app/main.py mounts '
- 'missing mount token '
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas182_adaptive_memory_bridge.md'
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
- 'PAS182 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS182'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 🔒 '<REDACTED:high-entropy blob, len=45>'
- 'PAS182 — Evaluate the adaptive-memory bridge (manual-test → memory CANDIDATE) services + routes + doctrine. Read-only — never reads .env, never touches Supabase, never runs a migration.'
- '--repo-root'
- '--output'
- '--json'
- 'store_true'
- '--summary-only'
- '--strict'
- 'report'
- 'None'
- '[PAS182] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS182] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS182 — Adaptive memory bridge readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS182 wired\ncorrectly and free of regressions in the PAS160-PAS181 +\nPAS-SECURITY-01/02/03/04 doctrine?".\n\nWalks the repo and verifies:\n\n  * Prior phases (PAS160-PAS181 + PAS-SECURITY-01/02/03/04)\n    readiness scripts still exist.\n  * PAS182 surfaces exist:\n      - app/services/learning/adaptive_memory_bridge.py\n      - app/services/learning/adaptive_memory_projection.py\n      - app/routes/operator_adaptive_memory.py\n      - app/routes/tenant_adaptive_memory.py\n      - scripts/pas182_adaptive_memory_bridge_readiness_check.py\n      - docs/pas182_adaptive_memory_bridge.md\n      - tests/mvp/test_pas182_adaptive_memory_bridge.py\n  * adaptive_memory_bridge exposes documented surface, closed\n    reason-code enum, low-risk + high-confidence thresholds,\n    CANDIDATE-only invariants.\n  * adaptive_memory_projection exposes closed operator and\n    tenant allow-lists; tenant projection strictly narrower.\n  * operator_adaptive_memory has the 2 documented routes\n    under require_admin with the PAS-SECURITY-04 rate-limit\n    pattern.\n  * tenant_adaptive_memory has the 1 documented GET route\n    under require_brokerage; no POST surface.\n  * No forbidden statuses (LIVE / APPLIED / AUTO_APPLIED /\n    DEPLOYED / APPROVED) in PAS182 source.\n  * No auto-approval / live-mutation tokens.\n  * No live-mutation imports (state_machine / memory review /\n    approval / booking / outbound / worker / slack).\n  * No LLM / embeddings / vector / Gmail / OAuth / IMAP /\n    POP3 / inbox-scanning / Composio / TrustClaw imports.\n  * Memory Review (PAS147-PAS158) untouched.\n  * audit_service.py STILL has no UPDATE / DELETE helpers.\n  * PAS179 / PAS180 / PAS181 services intact.\n  * PAS163 candidate pipeline intact + reachable.\n  * Event contract registers every PAS182 event type.\n  * main.py mounts both new routers.\n  * Worker still OFF by default; FastAPI lifespan does not\n    auto-start the worker.\n  * Supports --summary-only / --json.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads .env.\n  * Never touches production data.\n')
               STORE_NAME               0 (__doc__)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  55           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  58           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  59           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  62           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  63           NOP

  64   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  62   L4:     END_FOR
               POP_ITER

  69           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  70           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  69           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  74           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  75           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  77           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  84           LOAD_CONST              77 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py', 'docs/pas182_adaptive_memory_bridge.md', 'tests/mvp/test_pas182_adaptive_memory_bridge.py'))
               STORE_NAME              28 (REQUIRED_FILES)

  94           LOAD_CONST              78 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'scripts/pas174_operator_audit_readiness_check.py', 'scripts/pas175_audit_integrity_readiness_check.py', 'scripts/pas176_audit_chain_readiness_check.py', 'scripts/pas177_tenant_audit_verification_readiness_check.py', 'scripts/pas178_audit_window_chain_readiness_check.py', 'scripts/pas179_controlled_learning_readiness_check.py', 'scripts/pas180_learning_review_readiness_check.py', 'scripts/pas181_manual_test_harness_readiness_check.py', 'scripts/pas_security_01_hardening_readiness_check.py', 'scripts/pas_security_02_rate_limit_scanner_readiness_check.py', 'scripts/pas_security_03_admin_webhook_ci_readiness_check.py', 'scripts/pas_security_04_operator_reveal_https_readiness_check.py'))
               STORE_NAME              29 (PRIOR_PHASE_FILES)

 125           LOAD_CONST              79 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              30 (MEMORY_REVIEW_FILES)

 134           LOAD_CONST              80 (('app/services/learning/learning_policy.py', 'app/services/learning/scenario_contracts.py', 'app/services/learning/outcome_feedback.py', 'app/services/learning/recommendation_engine.py', 'app/services/learning/guardrails.py', 'app/services/learning/recommendation_review.py', 'app/services/learning/recommendation_projection.py', 'app/services/learning/manual_test_harness.py', 'app/services/learning/manual_test_evidence.py', 'app/services/learning/manual_test_scoring.py', 'app/routes/operator_learning.py', 'app/routes/tenant_learning.py', 'app/routes/operator_learning_tests.py', 'app/routes/tenant_learning_tests.py'))
               STORE_NAME              31 (PAS179_181_FILES)

 151           LOAD_CONST              81 (('app/services/memory/candidate_pipeline.py', 'app/services/memory/contracts.py', 'app/services/memory/store.py'))
               STORE_NAME              32 (PAS163_FILES)

 158           LOAD_CONST              82 (('def evaluate_bridge_eligibility(', 'def bridge_to_memory_candidate(', 'def adaptive_memory_bridge_report(', 'ALLOWED_BRIDGE_REASON_CODES', 'ALLOWED_BRIDGE_KEYS', 'ALLOWED_ACTOR_TYPES', 'LOW_RISK_THRESHOLD', 'HIGH_CONFIDENCE_THRESHOLD', 'APPROVED_FOR_MANUAL_TEST', 'SIMULATION_ONLY', 'OBSERVATIONAL_ONLY', 'missing_storage_helper', 'candidate_pipeline', 'generate_memory_candidates_from_replay', 'MemoryStatus', 'bridge_rejected_by_operator'))
               STORE_NAME              33 (REQUIRED_BRIDGE_TOKENS)

 177           LOAD_CONST              83 (('def project_operator_bridge_view(', 'def project_tenant_bridge_view(', 'def project_operator_bridge_list(', 'def project_tenant_bridge_list(', 'OPERATOR_BRIDGE_KEYS', 'TENANT_BRIDGE_KEYS', 'PROJECTION_FORBIDDEN_KEYS'))
               STORE_NAME              34 (REQUIRED_PROJECTION_TOKENS)

 187           LOAD_CONST              84 (('@router.post("/manual-tests/{test_run_id}/bridge-memory-candidate")', '@router.get("/adaptive-memory/bridge-report")', 'def require_admin(', 'bridge_memory_candidate_route', 'bridge_report_route', 'check_rate_limit', 'surface="admin"'))
               STORE_NAME              35 (REQUIRED_OPERATOR_ROUTE_TOKENS)

 197           LOAD_CONST              85 (('@router.get("/adaptive-memory/bridge-status")', 'def require_brokerage(', 'bridge_status_route'))
               STORE_NAME              36 (REQUIRED_TENANT_ROUTE_TOKENS)

 205           LOAD_CONST              86 (('"LIVE"', "'LIVE'", '"APPLIED"', "'APPLIED'", '"AUTO_APPLIED"', "'AUTO_APPLIED'", '"DEPLOYED"', "'DEPLOYED'", '"APPROVED"', "'APPROVED'"))
               STORE_NAME              37 (FORBIDDEN_STATUS_TOKENS)

 221           LOAD_CONST              87 (('auto_approve', 'auto_apply', 'apply_live', 'mutate_live', 'auto_applied'))
               STORE_NAME              38 (FORBIDDEN_AUTO_APPROVAL_TOKENS)

 232           LOAD_CONST              88 (('from app.engine.state_machine', 'import app.engine.state_machine', 'from app.services.memory.review', 'import app.services.memory.review', 'from app.services.memory.approval', 'import app.services.memory.approval', 'from app.services.booking', 'import app.services.booking', 'from app.services.outbound', 'import app.services.outbound', 'from app.services.worker', 'import app.services.worker', 'from app.services.ingestion.worker', 'import app.services.ingestion.worker', 'from app.services.slack', 'import app.services.slack'))
               STORE_NAME              39 (FORBIDDEN_LIVE_MUTATION_IMPORTS)

 252           LOAD_CONST              89 (('learning.manual_test.completed', 'learning.adaptive_memory.bridge_confirmed', 'learning.adaptive_memory.candidate_created', 'learning.adaptive_memory.bridge_rejected', 'tenant.learning.adaptive_memory.viewed'))
               STORE_NAME              40 (REQUIRED_EVENT_TYPES)

 263           LOAD_CONST              90 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              41 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 287           LOAD_CONST              91 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              42 (FORBIDDEN_INBOX_TOKENS)

 301           LOAD_CONST              12 ('severity')

 303           LOAD_NAME               27 (SEVERITY_BLOCK)

 301           LOAD_CONST              13 ('detail')

 303           LOAD_CONST              14 ('')

 301           BUILD_MAP                2
               LOAD_CONST              15 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 301>)
               MAKE_FUNCTION
               LOAD_CONST              16 (<code object _check at 0x0000018C17FA3B40, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 301>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (_check)

 314           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 314>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _now_iso at 0x0000018C18038F30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 314>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_now_iso)

 318           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 318>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _read_text at 0x0000018C180531B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 318>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_read_text)

 325           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 325>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 325>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (_strip_python_comments_and_strings)

 364           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 364>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object check_files_present at 0x0000018C180612C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 364>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_files_present)

 377           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 377>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_prior_phases_intact at 0x0000018C17F73650, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 377>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_prior_phases_intact)

 406           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 406>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_memory_review_intact at 0x0000018C18060A50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 406>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_memory_review_intact)

 419           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 419>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_worker_off_by_default at 0x0000018C180FC5D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 419>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_worker_off_by_default)

 436           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 436>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_startup_worker at 0x0000018C17D86020, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 436>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_startup_worker)

 459           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 459>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_bridge_service at 0x0000018C17FED630, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 459>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_bridge_service)

 474           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 474>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_projection_service at 0x0000018C17FEDA30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 474>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_projection_service)

 489           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 489>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_operator_routes at 0x0000018C17D515A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 489>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_operator_routes)

 511           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 511>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_tenant_routes at 0x0000018C17F72FD0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 511>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_tenant_routes)

 545           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 545>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_no_forbidden_status_tokens at 0x0000018C17D51840, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 545>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_no_forbidden_status_tokens)

 573           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 573>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_no_auto_approval_tokens at 0x0000018C182FFEA0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 573>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_no_auto_approval_tokens)

 601           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 601>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object check_no_live_mutation_imports at 0x0000018C17F73990, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 601>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_live_mutation_imports)

 632           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 632>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object check_audit_service_invariant at 0x0000018C182DACA0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 632>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_audit_service_invariant)

 659           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 659>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object check_event_contract at 0x0000018C1801CFB0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 659>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_event_contract)

 674           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 674>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object check_main_router_mounts at 0x0000018C180FCB70, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 674>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_main_router_mounts)

 693           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 693>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object check_no_forbidden_imports at 0x0000018C17F73310, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 693>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_no_forbidden_imports)

 725           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 725>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object check_no_inbox_scan_tokens at 0x0000018C17CC2460, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 725>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (check_no_inbox_scan_tokens)

 753           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 753>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object check_doc_required_clauses at 0x0000018C17E93370, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 753>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (check_doc_required_clauses)

 802           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 802>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object check_self_no_env_or_db at 0x0000018C17D87D80, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 802>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (check_self_no_env_or_db)

 835           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 835>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _aggregate at 0x0000018C17FA92F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 835>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              66 (_aggregate)

 847           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 847>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _operator_actions at 0x0000018C18048730, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 847>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_operator_actions)

 857           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 857>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object evaluate at 0x0000018C17D8BD50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 857>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (evaluate)

 895           LOAD_CONST              67 ('pas182_adaptive_memory_bridge_readiness_report.json')
               STORE_NAME              69 (REPORT_FILENAME)

 898           LOAD_CONST              68 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 898>)
               MAKE_FUNCTION
               LOAD_CONST              69 (<code object _build_parser at 0x0000018C180FC210, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 898>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              70 (_build_parser)

 916           LOAD_CONST              70 (<code object __annotate__ at 0x0000018C18114030, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 916>)
               MAKE_FUNCTION
               LOAD_CONST              71 (<code object _print_summary at 0x0000018C17D8D460, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 916>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              71 (_print_summary)

 934           LOAD_CONST              72 (<code object __annotate__ at 0x0000018C18026530, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 934>)
               MAKE_FUNCTION
               LOAD_CONST              73 (<code object _write_report at 0x0000018C180FC3F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 934>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              72 (_write_report)

 948           LOAD_CONST              92 ((None,))
               LOAD_CONST              74 (<code object __annotate__ at 0x0000018C181156B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 948>)
               MAKE_FUNCTION
               LOAD_CONST              75 (<code object main at 0x0000018C17D88890, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 948>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              73 (main)

 973           LOAD_NAME               74 (__name__)
               LOAD_CONST              76 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 974           LOAD_NAME                6 (sys)
               LOAD_ATTR              150 (exit)
               PUSH_NULL
               LOAD_NAME               73 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 973   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  65           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  66   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          375 (to L1)

  65   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 301>:
301           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

302           LOAD_CONST               2 ('str')

301           LOAD_CONST               3 ('status')

302           LOAD_CONST               2 ('str')

301           LOAD_CONST               4 ('label')

302           LOAD_CONST               2 ('str')

301           LOAD_CONST               5 ('severity')

303           LOAD_CONST               2 ('str')

301           LOAD_CONST               6 ('detail')

303           LOAD_CONST               2 ('str')

301           LOAD_CONST               7 ('return')

304           LOAD_CONST               8 ('dict')

301           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 301>:
301           RESUME                   0

306           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

307           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

308           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

309           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

310           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

305           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 314>:
314           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18038F30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 314>:
314           RESUME                   0

315           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 318>:
318           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C180531B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 318>:
 318           RESUME                   0

 319           NOP

 320   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 321           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 322   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 321   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 325>:
325           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 325>:
325            RESUME                   0

326            BUILD_LIST               0
               STORE_FAST               1 (out)

327            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

328    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

329            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

330            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

331            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

332            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

333            JUMP_FORWARD           240 (to L13)

334    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

335            JUMP_BACKWARD           59 (to L1)

336    L3:     LOAD_FAST_BORROW         0 (src)
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

337    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

338            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

339            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

340            JUMP_FORWARD           138 (to L13)

341    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

342            JUMP_BACKWARD          161 (to L1)

343    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

344            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

345            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

346    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

347            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

348            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

349            JUMP_BACKWARD           30 (to L7)

350    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

351    L9:     JUMP_FORWARD            11 (to L11)

352   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

353   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

354            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

355   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

356            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

357   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 364>:
364           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180612C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 364>:
364           RESUME                   0

365           BUILD_LIST               0
              STORE_FAST               1 (out)

366           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

367           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

368           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

369           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

370           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

371   L3:     LOAD_CONST               3 ('Required PAS182 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

372           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

368   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

366   L6:     END_FOR
              POP_ITER

374           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 377>:
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C17F73650, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 377>:
377            RESUME                   0

378            BUILD_LIST               0
               STORE_FAST               1 (out)

379            LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
               GET_ITER
       L1:     FOR_ITER                91 (to L6)
               STORE_FAST               2 (p)

380            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

381            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

382            LOAD_CONST               0 ('prior_phase:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

383            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L3)
       L2:     LOAD_CONST               2 ('FAIL')

384    L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

385            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L5)
       L4:     LOAD_CONST               5 ('missing — PAS182 must not delete')

381    L5:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           93 (to L1)

379    L6:     END_FOR
               POP_ITER

387            LOAD_GLOBAL             10 (PAS179_181_FILES)
               GET_ITER
       L7:     FOR_ITER                91 (to L12)
               STORE_FAST               2 (p)

388            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

389            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

390            LOAD_CONST               7 ('pas179_181_service:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

391            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               2 ('FAIL')

392    L9:     LOAD_CONST               8 ('PAS179/PAS180/PAS181 service intact: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

393            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST               9 ('service deleted — PAS182 must not touch')

389   L11:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           93 (to L7)

387   L12:     END_FOR
               POP_ITER

395            LOAD_GLOBAL             12 (PAS163_FILES)
               GET_ITER
      L13:     FOR_ITER                91 (to L18)
               STORE_FAST               2 (p)

396            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               LOAD_ATTR                5 (is_file + NULL|self)
               CALL                     0
               STORE_FAST               3 (ok)

397            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

398            LOAD_CONST              10 ('pas163_pipeline:')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

399            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               1 ('PASS')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               2 ('FAIL')

400   L15:     LOAD_CONST              11 ('PAS163 memory candidate pipeline intact: ')
               LOAD_FAST_BORROW         2 (p)
               FORMAT_SIMPLE
               BUILD_STRING             2

401            LOAD_FAST_BORROW         3 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST              12 ('PAS163 file missing — bridge cannot create CANDIDATEs')

397   L17:     LOAD_CONST               6 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           93 (to L13)

395   L18:     END_FOR
               POP_ITER

403            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 406>:
406           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060A50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 406>:
406           RESUME                   0

407           BUILD_LIST               0
              STORE_FAST               1 (out)

408           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                91 (to L6)
              STORE_FAST               2 (p)

409           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

410           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

411           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

412           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

413   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

414           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS182 must not touch')

410   L5:     LOAD_CONST               6 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           93 (to L1)

408   L6:     END_FOR
              POP_ITER

416           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 419>:
419           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C180FC5D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 419>:
419           RESUME                   0

420           BUILD_LIST               0
              STORE_FAST               1 (out)

421           LOAD_GLOBAL              1 (Path + NULL)
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

422           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

424           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

425           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

423   L2:     STORE_FAST               4 (literal_ok)

427           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

428           LOAD_CONST               7 ('worker:off_by_default')

429           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

430   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default')

431           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

427   L6:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

433           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 436>:
436           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17D86020, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 436>:
436           RESUME                   0

437           BUILD_LIST               0
              STORE_FAST               1 (out)

438           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

439           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

440           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

441           BUILD_LIST               0
              STORE_FAST               5 (bad)

442           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

443           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

444   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

445           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

446   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

447           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

448   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

449           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

450   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

451           LOAD_CONST              10 ('main:no_startup_worker')

452           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

453   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

454           LOAD_FAST_BORROW         5 (bad)
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

450   L9:     LOAD_CONST              16 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

456           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 459>:
459           RESUME                   0
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

Disassembly of <code object check_bridge_service at 0x0000018C17FED630, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 459>:
459           RESUME                   0

460           BUILD_LIST               0
              STORE_FAST               1 (out)

461           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('adaptive_memory_bridge.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

462           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

463           LOAD_GLOBAL              4 (REQUIRED_BRIDGE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

464           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

465           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

466           LOAD_CONST               5 ('bridge:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

467           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

468   L4:     LOAD_CONST               9 ('Adaptive-memory bridge token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

469           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

465   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

463   L7:     END_FOR
              POP_ITER

471           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 474>:
474           RESUME                   0
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

Disassembly of <code object check_projection_service at 0x0000018C17FEDA30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 474>:
474           RESUME                   0

475           BUILD_LIST               0
              STORE_FAST               1 (out)

476           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('learning')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('adaptive_memory_projection.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

477           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

478           LOAD_GLOBAL              4 (REQUIRED_PROJECTION_TOKENS)
              GET_ITER
      L2:     FOR_ITER                73 (to L7)
              STORE_FAST               4 (tok)

479           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

480           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

481           LOAD_CONST               5 ('projection:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

482           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

483   L4:     LOAD_CONST               9 ('Adaptive-memory projection token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

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

480   L6:     LOAD_CONST              11 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           75 (to L2)

478   L7:     END_FOR
              POP_ITER

486           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 489>:
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

Disassembly of <code object check_operator_routes at 0x0000018C17D515A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 489>:
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
               LOAD_CONST               2 ('operator_adaptive_memory.py')
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

493            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

494            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

495            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

496            LOAD_CONST               4 ('operator_routes:')
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

498    L4:     LOAD_CONST               8 ('Operator adaptive-memory route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

499            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

495    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

493    L7:     END_FOR
               POP_ITER

501            LOAD_CONST              11 ('require_admin')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              12 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
       L8:     STORE_FAST               6 (auth_ok)

502            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

503            LOAD_CONST              13 ('operator_routes:require_admin')

504            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('FAIL')

505   L10:     LOAD_CONST              14 ('Operator adaptive-memory routes use require_admin (X-Admin-Key)')

506            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              15 ('missing require_admin / X-Admin-Key tokens')

502   L12:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

508            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 511>:
511           RESUME                   0
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

Disassembly of <code object check_tenant_routes at 0x0000018C17F72FD0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 511>:
511            RESUME                   0

512            BUILD_LIST               0
               STORE_FAST               1 (out)

513            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('tenant_adaptive_memory.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

514            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

515            LOAD_GLOBAL              4 (REQUIRED_TENANT_ROUTE_TOKENS)
               GET_ITER
       L2:     FOR_ITER                73 (to L7)
               STORE_FAST               4 (tok)

516            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

517            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

518            LOAD_CONST               4 ('tenant_routes:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

519            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

520    L4:     LOAD_CONST               8 ('Tenant adaptive-memory route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

521            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

517    L6:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           75 (to L2)

515    L7:     END_FOR
               POP_ITER

524            LOAD_CONST              11 ('require_brokerage')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       33 (to L8)
               NOT_TAKEN
               POP_TOP

525            LOAD_CONST              12 ('x_api_key')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

524            COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       20 (to L8)
               NOT_TAKEN
               POP_TOP

526            LOAD_CONST              13 ('x_admin_key')
               LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              1 (not in)

523    L8:     STORE_FAST               6 (auth_ok)

528            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

529            LOAD_CONST              14 ('tenant_routes:tenant_auth_only')

530            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('FAIL')

531   L10:     LOAD_CONST              15 ('Tenant adaptive-memory routes use X-API-Key (require_brokerage), never admin')

532            LOAD_FAST_BORROW         6 (auth_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST              16 ('missing require_brokerage / x_api_key tokens')

528   L12:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

534            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

535            LOAD_CONST              17 ('@router.post')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              1 (not in)
               STORE_FAST               8 (no_post)

536            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

537            LOAD_CONST              18 ('tenant_routes:no_mutation_surface')

538            LOAD_FAST_BORROW         8 (no_post)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               7 ('FAIL')

539   L14:     LOAD_CONST              19 ('Tenant adaptive-memory routes have NO @router.post surface')

540            LOAD_FAST_BORROW         8 (no_post)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST              20 ('tenant route file declares a POST route')

536   L16:     LOAD_CONST              10 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

542            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 545>:
545           RESUME                   0
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

Disassembly of <code object check_no_forbidden_status_tokens at 0x0000018C17D51840, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 545>:
545            RESUME                   0

546            BUILD_LIST               0
               STORE_FAST               1 (out)

547            LOAD_CONST               9 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py'))
               STORE_FAST               2 (files)

553            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               213 (to L11)
               STORE_FAST               3 (relpath)

554            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

555            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

556            JUMP_BACKWARD           45 (to L1)

557    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

558            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

559            BUILD_LIST               0
               STORE_FAST               7 (bad)

560            LOAD_GLOBAL              8 (FORBIDDEN_STATUS_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (tok)

561            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

562    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

560    L6:     END_FOR
               POP_ITER

563            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

564            LOAD_CONST               2 ('no_forbidden_status:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

565            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

566    L8:     LOAD_CONST               5 ('No forbidden status tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

568            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L9)
               NOT_TAKEN

567            LOAD_CONST               6 ('disqualifying tokens: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_GLOBAL             17 (sorted + NULL)
               LOAD_GLOBAL             19 (set + NULL)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

568    L9:     LOAD_CONST               1 ('')

563   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          215 (to L1)

553   L11:     END_FOR
               POP_ITER

570            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 573>:
573           RESUME                   0
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

Disassembly of <code object check_no_auto_approval_tokens at 0x0000018C182FFEA0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 573>:
573            RESUME                   0

574            BUILD_LIST               0
               STORE_FAST               1 (out)

575            LOAD_CONST               9 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py'))
               STORE_FAST               2 (files)

581            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               242 (to L11)
               STORE_FAST               3 (relpath)

582            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

583            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

584            JUMP_BACKWARD           45 (to L1)

585    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

586            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

587            BUILD_LIST               0
               STORE_FAST               7 (bad)

588            LOAD_GLOBAL              8 (FORBIDDEN_AUTO_APPROVAL_TOKENS)
               GET_ITER
       L4:     FOR_ITER                57 (to L6)
               STORE_FAST               8 (tok)

589            LOAD_FAST_BORROW         8 (tok)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         6 (executable)
               LOAD_ATTR               11 (lower + NULL|self)
               CALL                     0
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           40 (to L4)

590    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         8 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           59 (to L4)

588    L6:     END_FOR
               POP_ITER

591            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

592            LOAD_CONST               2 ('no_auto_approval:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

593            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

594    L8:     LOAD_CONST               5 ('No auto-approval / live-mutation tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

596            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L9)
               NOT_TAKEN

595            LOAD_CONST               6 ('disqualifying tokens: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_GLOBAL             19 (sorted + NULL)
               LOAD_GLOBAL             21 (set + NULL)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               CALL                     1
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

596    L9:     LOAD_CONST               1 ('')

591   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          244 (to L1)

581   L11:     END_FOR
               POP_ITER

598            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 601>:
601           RESUME                   0
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

Disassembly of <code object check_no_live_mutation_imports at 0x0000018C17F73990, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 601>:
601            RESUME                   0

602            BUILD_LIST               0
               STORE_FAST               1 (out)

603            LOAD_CONST              10 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py'))
               STORE_FAST               2 (files)

609            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

610            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

611            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

612            JUMP_BACKWARD           46 (to L1)

613    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

614            BUILD_LIST               0
               STORE_FAST               6 (bad)

615            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

616            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

617            LOAD_FAST_BORROW         8 (stripped)
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

618    L5:     JUMP_BACKWARD           52 (to L4)

619    L6:     LOAD_GLOBAL             12 (FORBIDDEN_LIVE_MUTATION_IMPORTS)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

620            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

621    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

619    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

615   L10:     END_FOR
               POP_ITER

622            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

623            LOAD_CONST               3 ('no_live_mutation_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

624            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

625   L12:     LOAD_CONST               6 ('No live-mutation imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

627            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

626            LOAD_CONST               7 ('forbidden imports: ')
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

627   L13:     LOAD_CONST               1 ('')

622   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

609   L15:     END_FOR
               POP_ITER

629            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 632>:
632           RESUME                   0
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

Disassembly of <code object check_audit_service_invariant at 0x0000018C182DACA0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 632>:
632           RESUME                   0

635           BUILD_LIST               0
              STORE_FAST               1 (out)

636           LOAD_GLOBAL              1 (Path + NULL)
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

637           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('')
      L1:     STORE_FAST               3 (src)

638           LOAD_CONST              13 (('def update_audit_', 'def delete_audit_', 'def update_operator_audit_', 'def delete_operator_audit_', 'def mutate_audit_', 'def truncate_audit_'))
              STORE_FAST               4 (forbidden)

646           BUILD_LIST               0
              STORE_FAST               5 (bad)

647           LOAD_FAST_BORROW         4 (forbidden)
              GET_ITER
      L2:     FOR_ITER                28 (to L4)
              STORE_FAST               6 (tok)

648           LOAD_FAST_BORROW_LOAD_FAST_BORROW 99 (tok, src)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L2)

649   L3:     LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_FAST_BORROW         6 (tok)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           30 (to L2)

647   L4:     END_FOR
              POP_ITER

650           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

651           LOAD_CONST               6 ('audit_service:append_only_carry')

652           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               7 ('FAIL')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST               8 ('PASS')

653   L6:     LOAD_CONST               9 ('Audit service still has no UPDATE / DELETE mutation helpers (carry-forward invariant)')

654           LOAD_FAST_BORROW         5 (bad)
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

650   L8:     LOAD_CONST              12 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

656           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 659>:
659           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C1801CFB0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 659>:
659           RESUME                   0

660           BUILD_LIST               0
              STORE_FAST               1 (out)

661           LOAD_GLOBAL              1 (Path + NULL)
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

662           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

663           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                67 (to L7)
              STORE_FAST               4 (required)

664           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

665           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

666           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

667           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

668   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

669           LOAD_FAST_BORROW         5 (ok)
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

665   L6:     LOAD_CONST              10 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           69 (to L2)

663   L7:     END_FOR
              POP_ITER

671           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 674>:
674           RESUME                   0
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

Disassembly of <code object check_main_router_mounts at 0x0000018C180FCB70, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 674>:
674           RESUME                   0

675           BUILD_LIST               0
              STORE_FAST               1 (out)

676           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

677           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

678           LOAD_CONST              10 (('operator_adaptive_memory_router', 'tenant_adaptive_memory_router'))
              STORE_FAST               4 (required)

682           LOAD_FAST_BORROW         4 (required)
              GET_ITER
      L2:     FOR_ITER                74 (to L7)
              STORE_FAST               5 (tok)

683           LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               6 (ok)

684           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

685           LOAD_CONST               3 ('main:mount:')
              LOAD_FAST_BORROW         5 (tok)
              LOAD_CONST               4 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

686           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               6 ('FAIL')

687   L4:     LOAD_CONST               7 ('app/main.py mounts ')
              LOAD_FAST_BORROW         5 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

688           LOAD_FAST_BORROW         6 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             5 (to L6)
      L5:     LOAD_CONST               8 ('missing mount token ')
              LOAD_FAST_BORROW         5 (tok)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              BUILD_STRING             2

684   L6:     LOAD_CONST               9 (('detail',))
              CALL_KW                  4
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L2)

682   L7:     END_FOR
              POP_ITER

690           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 693>:
693           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17F73310, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 693>:
693            RESUME                   0

694            BUILD_LIST               0
               STORE_FAST               1 (out)

695            LOAD_CONST              10 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py', 'scripts/pas182_adaptive_memory_bridge_readiness_check.py'))
               STORE_FAST               2 (files)

702            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               292 (to L15)
               STORE_FAST               3 (relpath)

703            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

704            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

705            JUMP_BACKWARD           46 (to L1)

706    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

707            BUILD_LIST               0
               STORE_FAST               6 (bad)

708            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

709            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

710            LOAD_FAST_BORROW         8 (stripped)
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

711    L5:     JUMP_BACKWARD           52 (to L4)

712    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

713            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

714    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

712    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

708   L10:     END_FOR
               POP_ITER

715            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

716            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

717            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

718   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

720            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

719            LOAD_CONST               7 ('forbidden import prefixes: ')
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

720   L13:     LOAD_CONST               1 ('')

715   L14:     LOAD_CONST               9 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          295 (to L1)

702   L15:     END_FOR
               POP_ITER

722            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 725>:
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CC2460, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 725>:
725            RESUME                   0

726            BUILD_LIST               0
               STORE_FAST               1 (out)

727            LOAD_CONST               9 (('app/services/learning/adaptive_memory_bridge.py', 'app/services/learning/adaptive_memory_projection.py', 'app/routes/operator_adaptive_memory.py', 'app/routes/tenant_adaptive_memory.py'))
               STORE_FAST               2 (files)

733            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               195 (to L11)
               STORE_FAST               3 (relpath)

734            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

735            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

736            JUMP_BACKWARD           45 (to L1)

737    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

738            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

739            BUILD_LIST               0
               STORE_FAST               7 (bad)

740            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

741            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

742    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

740    L6:     END_FOR
               POP_ITER

743            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

744            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

745            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

746    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

748            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

747            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

748    L9:     LOAD_CONST               1 ('')

743   L10:     LOAD_CONST               8 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          197 (to L1)

733   L11:     END_FOR
               POP_ITER

750            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 753>:
753           RESUME                   0
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

Disassembly of <code object check_doc_required_clauses at 0x0000018C17E93370, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 753>:
  --            MAKE_CELL                8 (lower)

 753            RESUME                   0

 754            BUILD_LIST               0
                STORE_FAST               1 (out)

 755            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas182_adaptive_memory_bridge.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 756            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 757            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 758            LOAD_CONST              13 ((('hard-constraints', ('hard constraints',)), ('no-auto-approval', ('no auto-approval',)), ('no-live-behavior-mutation', ('no-live-behavior-mutation', 'no live behavior mutation')), ('candidate-only', ('candidate only', 'candidate-only')), ('simulation-only', ('simulation_only', 'simulation-only', 'simulation only')), ('observational-only', ('observational_only', 'observational-only', 'observational only')), ('eligibility', ('eligibility',)), ('low-risk-threshold', ('low_risk_threshold', 'low-risk threshold', 'low_risk threshold')), ('high-confidence-threshold', ('high_confidence_threshold', 'high-confidence threshold', 'high_confidence threshold')), ('missing-storage-helper', ('missing_storage_helper', 'missing storage helper')), ('never-raises', ('never raises',)), ('forbidden-payload-keys', ('forbidden payload', 'forbidden payload keys')), ('no-llm', ('no llm',)), ('no-embeddings', ('no embeddings',)), ('no-gmail', ('no gmail',)), ('no-composio', ('no composio',)), ('worker-off', ('worker remains off', 'worker stays off')), ('pas163-handoff', ('pas163',)), ('pas181-source', ('pas181',))))
                STORE_FAST               4 (required_phrases)

 790            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               141 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 791            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 791>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 791>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 792            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 793            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 794            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 795    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 797            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 796            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 797   L10:     LOAD_CONST               2 ('')

 792   L11:     LOAD_CONST              12 (('detail',))
                CALL_KW                  4
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          143 (to L2)

 790   L12:     END_FOR
                POP_ITER

 799            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024E30, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 791>:
  --           COPY_FREE_VARS           1

 791           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 802>:
802           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D87D80, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 802>:
802            RESUME                   0

803            BUILD_LIST               0
               STORE_FAST               1 (out)

804            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

805            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

806            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

807            BUILD_LIST               0
               STORE_FAST               5 (bad)

808            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

809            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

810            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

811            JUMP_BACKWARD           29 (to L2)

812    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

813            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

814    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

815            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

816    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

817            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

818    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

819            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

820    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

821    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

808    L9:     END_FOR
               POP_ITER

822            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

823            LOAD_CONST               8 ('self_check:no_env_or_db')

824            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

825   L11:     LOAD_CONST              11 ('PAS182 readiness checker never reads .env / touches DB')

826            LOAD_FAST_BORROW         5 (bad)
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

822   L13:     LOAD_CONST              14 (('detail',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

828            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 835>:
835           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17FA92F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 835>:
 835            RESUME                   0

 837            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 836            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 837    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 838            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 837    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 838    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 837    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 836    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 841            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L9)
                NOT_TAKEN
                LOAD_GLOBAL              4 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L10)
        L9:     LOAD_GLOBAL              6 (VERDICT_READY)

 842   L10:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 843            LOAD_CONST               5 ('info')
                BUILD_LIST               0

 840            BUILD_MAP                3
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 836            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L11 [2]
  L4 to L5 -> L11 [2]
  L6 to L8 -> L11 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 847>:
847           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 847>:
847           RESUME                   0

848           BUILD_LIST               0
              STORE_FAST               1 (out)

849           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

850           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

851           JUMP_BACKWARD           19 (to L1)

852   L2:     LOAD_FAST_BORROW         2 (c)
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

853           LOAD_FAST                1 (out)
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

849   L5:     END_FOR
              POP_ITER

854           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 857>:
857           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17D8BD50, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 857>:
857           RESUME                   0

858           BUILD_LIST               0
              STORE_FAST               1 (checks)

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_bridge_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_projection_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_operator_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_tenant_routes + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_forbidden_status_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_no_auto_approval_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

870           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_no_live_mutation_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

871           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_audit_service_invariant + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

872           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

873           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_main_router_mounts + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

874           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

875           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

876           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             37 (check_doc_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

877           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             39 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

879           LOAD_GLOBAL             41 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

881           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS182')

882           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             43 (_now_iso + NULL)
              CALL                     0

883           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

884           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             44 (VERDICT_READY)
              COMPARE_OP              72 (==)

885           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

886           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

887           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             47 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

888           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C180532D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 888>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

889           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             49 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053510, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 889>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

890           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

891           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             51 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

880           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180532D0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 888>:
 888           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053510, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 889>:
 889           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 898>:
898           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C180FC210, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 898>:
898           RESUME                   0

899           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

900           LOAD_CONST               0 ('pas182_adaptive_memory_bridge_readiness_check')

902           LOAD_CONST               1 ('PAS182 — Evaluate the adaptive-memory bridge (manual-test → memory CANDIDATE) services + routes + doctrine. Read-only — never reads .env, never touches Supabase, never runs a migration.')

899           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

908           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

909           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               5 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              LOAD_CONST               4 (('default',))
              CALL_KW                  2
              POP_TOP

910           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               6 ('--json')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

911           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST               9 ('--summary-only')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

912           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)
              LOAD_CONST              10 ('--strict')
              LOAD_CONST               7 ('store_true')
              LOAD_CONST               8 (('action',))
              CALL_KW                  2
              POP_TOP

913           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114030, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 916>:
916           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 916>:
916           RESUME                   0

917           LOAD_GLOBAL              1 (print + NULL)

918           LOAD_CONST               0 ('[PAS182] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

919           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

920           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

921           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

922           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

923           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

918           BUILD_STRING            12

917           CALL                     1
              POP_TOP

925           LOAD_FAST_BORROW         0 (report)
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

926           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

927           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS182] operator actions:')
              CALL                     1
              POP_TOP

928           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

929           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

928   L3:     END_FOR
              POP_ITER

930           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

931           LOAD_GLOBAL              1 (print + NULL)
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

930   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

926   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 934>:
934           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC3F0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 934>:
 934           RESUME                   0

 935           NOP

 936   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 937           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 938           LOAD_CONST               3 ('utf-8')

 936           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 940           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 941   L4:     LOAD_GLOBAL             11 (print + NULL)

 942           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 943           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 942           BUILD_STRING             4

 944           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 941           LOAD_CONST               7 (('file',))
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

 940   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 948>:
948           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D88890, file "scripts\pas182_adaptive_memory_bridge_readiness_check.py", line 948>:
 948            RESUME                   0

 949            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 950            NOP

 951    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 955    L2:     LOAD_GLOBAL             10 (os)
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

 956            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 957            LOAD_GLOBAL             23 (print + NULL)
                LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 958            LOAD_SMALL_INT           2
                RETURN_VALUE

 960    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 962            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 963            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 965    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 967            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 968            LOAD_GLOBAL             23 (print + NULL)
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

 970    L6:     LOAD_FAST                5 (report)
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

 952            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 953    L9:     LOAD_FAST                3 (e)
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

 952   L17:     RERAISE                  0

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
