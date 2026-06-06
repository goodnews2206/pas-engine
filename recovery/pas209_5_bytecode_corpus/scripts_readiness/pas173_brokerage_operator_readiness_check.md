# scripts_readiness/pas173_brokerage_operator_readiness_check

- **pyc:** `scripts\__pycache__\pas173_brokerage_operator_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas173_brokerage_operator_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas173_brokerage_operator_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS173 — Brokerage operator system readiness gate.

Deterministic, non-mutating evaluator for "is PAS173 the
controlled-self-serve layer wired correctly and free of
regressions in the PAS160-PAS172 doctrine?".

Walks the repo and verifies:

  * PAS160-PAS172 readiness scripts still exist.
  * PAS173 surfaces exist:
      - scripts/migrate_v21_brokerage_profiles.sql
      - app/services/brokerage/profile_service.py
      - app/services/brokerage/config_validator.py
      - app/services/brokerage/onboarding_templates.py
      - app/services/operator/operator_actions.py
      - app/routes/operator_brokerages.py
      - scripts/pas173_brokerage_operator_readiness_check.py
      - docs/pas173_brokerage_operator_system.md
      - docs/orvn_brokerage_onboarding_playbook.md
      - tests/mvp/test_pas173_brokerage_operator_system.py
  * Migration v21 carries PROPOSAL ONLY + DO NOT EXECUTE +
    closed onboarding_status enum + closed pilot_stage enum +
    tenant-write denial.
  * Profile service exposes the documented surface
    (ensure / get / list / pause / resume / mark_*) + closed
    enums + allow-listed features/metadata keys.
  * Config validator exposes the documented surface +
    closed allow-lists for warnings/errors + presence-only
    discipline (no env value echoes).
  * Onboarding templates expose the documented surface +
    are deterministic (no AI generation, no DB read).
  * Operator actions expose the closed allow-list +
    audit-block + dispatch table.
  * operator_brokerages route exposes the four GETs +
    one POST (actions) + admin-auth + defensive forbidden-
    token scanner.
  * Worker still OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).
  * FastAPI lifespan in ``app/main.py`` does NOT auto-start
    the worker.
  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
    Memory Review / embedding / vector / Composio /
    TrustClaw / OpenAI / Anthropic imports in any PAS173
    file.
  * Memory Review (PAS147-PAS158) untouched.
  * Event contract registers every PAS173 event type.
  * Docs carry the required clauses.
  * Onboarding playbook carries the required clauses.
  * Supports ``--summary-only`` / ``--json``.
  * Exits 0 ready, 1 blockers, 2 bad args.
  * Never reads ``.env``.
  * Never touches production data.
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_config_validator`, `check_docs_required_clauses`, `check_event_contract`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_no_inbox_scan_tokens`, `check_no_startup_worker`, `check_onboarding_templates`, `check_operator_actions`, `check_operator_brokerages_route`, `check_playbook_required_clauses`, `check_prior_phases_intact`, `check_profile_service`, `check_self_no_env_or_db`, `check_v21_sql`, `check_worker_off_by_default`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS173`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS173 — Brokerage operator system readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS173 the\ncontrolled-self-serve layer wired correctly and free of\nregressions in the PAS160-PAS172 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS172 readiness scripts still exist.\n  * PAS173 surfaces exist:\n      - scripts/migrate_v21_brokerage_profiles.sql\n      - app/services/brokerage/profile_service.py\n      - app/services/brokerage/config_validator.py\n      - app/services/brokerage/onboarding_templates.py\n      - app/services/operator/operator_actions.py\n      - app/routes/operator_brokerages.py\n      - scripts/pas173_brokerage_operator_readiness_check.py\n      - docs/pas173_brokerage_operator_system.md\n      - docs/orvn_brokerage_onboarding_playbook.md\n      - tests/mvp/test_pas173_brokerage_operator_system.py\n  * Migration v21 carries PROPOSAL ONLY + DO NOT EXECUTE +\n    closed onboarding_status enum + closed pilot_stage enum +\n    tenant-write denial.\n  * Profile service exposes the documented surface\n    (ensure / get / list / pause / resume / mark_*) + closed\n    enums + allow-listed features/metadata keys.\n  * Config validator exposes the documented surface +\n    closed allow-lists for warnings/errors + presence-only\n    discipline (no env value echoes).\n  * Onboarding templates expose the documented surface +\n    are deterministic (no AI generation, no DB read).\n  * Operator actions expose the closed allow-list +\n    audit-block + dispatch table.\n  * operator_brokerages route exposes the four GETs +\n    one POST (actions) + admin-auth + defensive forbidden-\n    token scanner.\n  * Worker still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio /\n    TrustClaw / OpenAI / Anthropic imports in any PAS173\n    file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS173 event type.\n  * Docs carry the required clauses.\n  * Onboarding playbook carries the required clauses.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas173_brokerage_operator_readiness_report.json'
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
- 'Required PAS173 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS173 must not delete'
- 'memory_review:'
- 'Memory Review file present: '
- 'Memory Review file deleted — PAS173 must not touch'
- 'app'
- 'services'
- 'ingestion'
- 'worker.py'
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Pending-call worker is OFF by default (strict env literal)'
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
- 'brokerage'
- 'profile_service.py'
- 'profile_service:'
- 'Profile service token: '
- 'missing token '
- 'config_validator.py'
- 'config_validator:'
- 'Config validator token: '
- 'logger.info(f'
- 'config_validator:no_value_echoes'
- 'Config validator does not echo env / brokerage values'
- 'onboarding_templates.py'
- 'onboarding_templates:'
- 'Onboarding templates token: '
- '"generated_at": None'
- 'onboarding_templates:deterministic'
- 'Onboarding templates are deterministic (no timestamp echoed)'
- 'missing deterministic generated_at=None marker'
- 'get_supabase'
- 'get_supabase call'
- 'os.environ'
- 'os.environ read'
- 'onboarding_templates:no_db_env_read'
- 'Onboarding templates never read DB or env'
- 'operator'
- 'operator_actions.py'
- 'operator_actions:'
- 'Operator actions token: '
- 'ALLOWED_OPERATOR_ACTIONS = ('
- 'operator_actions:closed_allow_list'
- 'Operator actions allow-list is a closed literal tuple'
- 'expected literal tuple declaration'
- 'routes'
- 'operator_brokerages.py'
- 'operator_brokerages:'
- 'Operator brokerages route token: '
- 'operator_brokerages:no_pii_exposure'
- 'Operator brokerages route does not reference transcript/raw payload'
- 'operator_brokerages_router'
- 'prefix="/ops/brokerages"'
- 'operator_brokerages:router_mounted'
- 'operator_brokerages_router is mounted at /ops/brokerages'
- 'expected `operator_brokerages_router` import + `include_router(..., prefix="/ops/brokerages")`'
- 'scripts'
- 'migrate_v21_brokerage_profiles.sql'
- 'proposal only'
- 'v21_sql:proposal_only'
- "v21 SQL carries 'PROPOSAL ONLY' guardrail"
- "missing 'PROPOSAL ONLY' label"
- 'do not execute'
- 'v21_sql:do_not_execute'
- "v21 SQL carries 'DO NOT EXECUTE' trailer"
- 'missing trailer'
- 'v21_sql:closed_onboarding_status_enum'
- 'v21 SQL carries the closed onboarding_status enum literals'
- 'missing one or more status literals'
- 'v21_sql:closed_pilot_stage_enum'
- 'v21 SQL carries the closed pilot_stage enum literals'
- 'missing one or more pilot_stage literals'
- 'pas_brokerage_profiles_tenant_no_insert'
- 'with check (false)'
- 'v21_sql:tenant_no_write'
- 'v21 SQL denies tenant write'
- 'missing tenant-write denial'
- 'pas_brokerage_profiles_tenant_select'
- "auth.jwt() ->> 'brokerage_id'"
- 'v21_sql:tenant_select_scoped'
- 'v21 SQL scopes tenant SELECT to own brokerage_id'
- 'missing tenant scoped select'
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'app/services/brokerage/__init__.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'app/services/brokerage/profile_service.py'
- 'no_inbox_scan:'
- 'No inbox-scanning tokens: '
- 'inbox-scan tokens present: '
- 'docs'
- 'pas173_brokerage_operator_system.md'
- 'docs:phrase:'
- 'Doctrine doc carries clause: '
- 'expected one of: '
- ' | '
- 'orvn_brokerage_onboarding_playbook.md'
- 'playbook:phrase:'
- 'Onboarding playbook carries clause: '
- 'dotenv import'
- 'supabase import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'supabase client call'
- 'self_check:no_env_or_db'
- 'PAS173 readiness checker never reads .env / touches DB'
- 'disqualifying patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS173'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas173_brokerage_operator_readiness_check'
- 'PAS173 — Evaluate the brokerage operator system (profile service + config validator + onboarding templates + operator actions + multi-brokerage ops routes). Read-only — never reads .env, never touches Supabase, never runs a migration.'
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
- '[PAS173] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS173] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS173 — Brokerage operator system readiness gate.\n\nDeterministic, non-mutating evaluator for "is PAS173 the\ncontrolled-self-serve layer wired correctly and free of\nregressions in the PAS160-PAS172 doctrine?".\n\nWalks the repo and verifies:\n\n  * PAS160-PAS172 readiness scripts still exist.\n  * PAS173 surfaces exist:\n      - scripts/migrate_v21_brokerage_profiles.sql\n      - app/services/brokerage/profile_service.py\n      - app/services/brokerage/config_validator.py\n      - app/services/brokerage/onboarding_templates.py\n      - app/services/operator/operator_actions.py\n      - app/routes/operator_brokerages.py\n      - scripts/pas173_brokerage_operator_readiness_check.py\n      - docs/pas173_brokerage_operator_system.md\n      - docs/orvn_brokerage_onboarding_playbook.md\n      - tests/mvp/test_pas173_brokerage_operator_system.py\n  * Migration v21 carries PROPOSAL ONLY + DO NOT EXECUTE +\n    closed onboarding_status enum + closed pilot_stage enum +\n    tenant-write denial.\n  * Profile service exposes the documented surface\n    (ensure / get / list / pause / resume / mark_*) + closed\n    enums + allow-listed features/metadata keys.\n  * Config validator exposes the documented surface +\n    closed allow-lists for warnings/errors + presence-only\n    discipline (no env value echoes).\n  * Onboarding templates expose the documented surface +\n    are deterministic (no AI generation, no DB read).\n  * Operator actions expose the closed allow-list +\n    audit-block + dispatch table.\n  * operator_brokerages route exposes the four GETs +\n    one POST (actions) + admin-auth + defensive forbidden-\n    token scanner.\n  * Worker still OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` literal intact).\n  * FastAPI lifespan in ``app/main.py`` does NOT auto-start\n    the worker.\n  * No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n    Memory Review / embedding / vector / Composio /\n    TrustClaw / OpenAI / Anthropic imports in any PAS173\n    file.\n  * Memory Review (PAS147-PAS158) untouched.\n  * Event contract registers every PAS173 event type.\n  * Docs carry the required clauses.\n  * Onboarding playbook carries the required clauses.\n  * Supports ``--summary-only`` / ``--json``.\n  * Exits 0 ready, 1 blockers, 2 bad args.\n  * Never reads ``.env``.\n  * Never touches production data.\n')
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

  83           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  90           LOAD_CONST              74 (('scripts/migrate_v21_brokerage_profiles.sql', 'app/services/brokerage/__init__.py', 'app/services/brokerage/profile_service.py', 'app/services/brokerage/config_validator.py', 'app/services/brokerage/onboarding_templates.py', 'app/services/operator/__init__.py', 'app/services/operator/operator_actions.py', 'app/routes/operator_brokerages.py', 'scripts/pas173_brokerage_operator_readiness_check.py', 'docs/pas173_brokerage_operator_system.md', 'docs/orvn_brokerage_onboarding_playbook.md', 'tests/mvp/test_pas173_brokerage_operator_system.py'))
               STORE_NAME              29 (REQUIRED_FILES)

 105           LOAD_CONST              75 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'scripts/pas164_email_ingestion_readiness_check.py', 'scripts/pas165_email_auth_dedupe_readiness_check.py', 'scripts/pas166_email_dedupe_policy_readiness_check.py', 'scripts/pas167_email_secret_reaper_readiness_check.py', 'scripts/pas168_email_secret_rotation_readiness_check.py', 'scripts/pas169_crypto_roundtrip_check.py', 'scripts/pas169_launch_readiness_check.py', 'scripts/pas_launch_integrity_check.py', 'scripts/pas170_operator_survival_readiness_check.py', 'scripts/pas171_external_pilot_readiness_check.py', 'scripts/pas172_pilot_operations_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 123           LOAD_CONST              76 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 133           LOAD_CONST              77 (('def ensure_profile(', 'def get_profile(', 'def list_profiles(', 'def update_onboarding_status(', 'def update_pilot_stage(', 'def pause_brokerage(', 'def resume_brokerage(', 'def mark_onboarding_completed(', 'ALLOWED_ONBOARDING_STATUSES', 'ALLOWED_PILOT_STAGES', 'ALLOWED_FEATURES_KEYS', 'ALLOWED_METADATA_KEYS', '_TABLE = "pas_brokerage_profiles"', 'brokerage_profile_store_unavailable'))
               STORE_NAME              32 (REQUIRED_PROFILE_SERVICE_TOKENS)

 150           LOAD_CONST              78 (('def validate_brokerage_configuration(', 'def validate_brokerage_launch_ready(', 'def configuration_warning_report(', 'ALLOWED_WARNINGS', 'ALLOWED_ERRORS'))
               STORE_NAME              33 (REQUIRED_CONFIG_VALIDATOR_TOKENS)

 158           LOAD_CONST              79 (('def brokerage_onboarding_checklist(', 'def launch_checklist(', 'def rollback_checklist(', 'def smoke_test_template(', 'def pilot_expansion_checklist('))
               STORE_NAME              34 (REQUIRED_ONBOARDING_TEMPLATES_TOKENS)

 166           LOAD_CONST              80 (('def execute_action(', 'ALLOWED_OPERATOR_ACTIONS', 'ALLOWED_ACTOR_TYPES', 'action_not_allowed', 'invalid_actor_type', 'operator.action.executed'))
               STORE_NAME              35 (REQUIRED_OPERATOR_ACTIONS_TOKENS)

 175           LOAD_CONST              81 (('def require_admin(', '@router.get("")', '@router.get("/{brokerage_id}")', '@router.get("/{brokerage_id}/health")', '@router.get("/{brokerage_id}/launch-readiness")', '@router.get("/{brokerage_id}/onboarding-checklist")', '@router.post("/{brokerage_id}/actions")', '_FORBIDDEN_RESPONSE_TOKENS', 'ops_envelope_forbidden_token'))
               STORE_NAME              36 (REQUIRED_OPERATOR_BROKERAGES_TOKENS)

 188           LOAD_CONST              82 (('operator.action.executed', 'brokerage.onboarding.started', 'brokerage.onboarding.completed', 'brokerage.stage.updated', 'brokerage.paused', 'brokerage.resumed', 'brokerage.launch.readiness_generated'))
               STORE_NAME              37 (REQUIRED_EVENT_TYPES)

 201           LOAD_CONST              83 (('import gmail', 'from gmail', 'import googleapiclient', 'from googleapiclient', 'import google.oauth2', 'from google.oauth2', 'from google.auth', 'import google.auth', 'from google_auth_oauthlib', 'import imaplib', 'from imaplib', 'import poplib', 'from poplib', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import chromadb', 'from chromadb', 'import pinecone', 'from pinecone', 'import langchain', 'from langchain', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings', 'from app.services.memory', 'import app.services.memory', 'from anthropic', 'import anthropic', 'from openai', 'import openai'))
               STORE_NAME              38 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 226           LOAD_CONST              84 (('imaplib', 'poplib', 'fetch_inbox', 'gmail_oauth', 'gmail_token', 'users().messages'))
               STORE_NAME              39 (FORBIDDEN_INBOX_TOKENS)

 236           LOAD_CONST              85 (('transcript', 'raw_payload', 'raw_email', 'raw_body'))
               STORE_NAME              40 (FORBIDDEN_PII_EXPOSURE_TOKENS)

 244           LOAD_CONST              86 (('block_actions', 'view_submission', 'interactivity', 'slash_command_callback', '"type": "button"', '"type": "actions"'))
               STORE_NAME              41 (FORBIDDEN_SLACK_INTERACTIVE_TOKENS)

 258           LOAD_CONST              13 ('severity')

 260           LOAD_NAME               27 (SEVERITY_BLOCK)

 258           LOAD_CONST              14 ('detail')

 260           LOAD_CONST              15 ('')

 258           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 258>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3B40, file "scripts\pas173_brokerage_operator_readiness_check.py", line 258>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              42 (_check)

 271           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 271>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C180388F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 271>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_now_iso)

 275           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas173_brokerage_operator_readiness_check.py", line 275>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053E10, file "scripts\pas173_brokerage_operator_readiness_check.py", line 275>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_read_text)

 282           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 282>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas173_brokerage_operator_readiness_check.py", line 282>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (_strip_python_comments_and_strings)

 321           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas173_brokerage_operator_readiness_check.py", line 321>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C18061470, file "scripts\pas173_brokerage_operator_readiness_check.py", line 321>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_files_present)

 335           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas173_brokerage_operator_readiness_check.py", line 335>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 335>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_prior_phases_intact)

 349           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 349>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas173_brokerage_operator_readiness_check.py", line 349>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_memory_review_intact)

 363           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18114120, file "scripts\pas173_brokerage_operator_readiness_check.py", line 363>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_worker_off_by_default at 0x0000018C1801C9E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 363>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_worker_off_by_default)

 381           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18114210, file "scripts\pas173_brokerage_operator_readiness_check.py", line 381>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_no_startup_worker at 0x0000018C17EA5300, file "scripts\pas173_brokerage_operator_readiness_check.py", line 381>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_no_startup_worker)

 405           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C181143F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 405>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_profile_service at 0x0000018C17F01670, file "scripts\pas173_brokerage_operator_readiness_check.py", line 405>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_profile_service)

 421           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C181144E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 421>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_config_validator at 0x0000018C17EA5880, file "scripts\pas173_brokerage_operator_readiness_check.py", line 421>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_config_validator)

 457           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C181145D0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 457>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_onboarding_templates at 0x0000018C17F79120, file "scripts\pas173_brokerage_operator_readiness_check.py", line 457>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_onboarding_templates)

 496           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C181147B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 496>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_operator_actions at 0x0000018C17CD1490, file "scripts\pas173_brokerage_operator_readiness_check.py", line 496>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_operator_actions)

 521           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18114990, file "scripts\pas173_brokerage_operator_readiness_check.py", line 521>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_operator_brokerages_route at 0x0000018C17EF9A30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 521>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_operator_brokerages_route)

 566           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18114A80, file "scripts\pas173_brokerage_operator_readiness_check.py", line 566>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_v21_sql at 0x0000018C181A30B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 566>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_v21_sql)

 640           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C18114B70, file "scripts\pas173_brokerage_operator_readiness_check.py", line 640>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_event_contract at 0x0000018C17FED630, file "scripts\pas173_brokerage_operator_readiness_check.py", line 640>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_event_contract)

 656           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C18114C60, file "scripts\pas173_brokerage_operator_readiness_check.py", line 656>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_no_forbidden_imports at 0x0000018C17E95410, file "scripts\pas173_brokerage_operator_readiness_check.py", line 656>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (check_no_forbidden_imports)

 692           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C18114D50, file "scripts\pas173_brokerage_operator_readiness_check.py", line 692>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object check_no_inbox_scan_tokens at 0x0000018C17CD1ED0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 692>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (check_no_inbox_scan_tokens)

 723           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C18114F30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 723>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object check_docs_required_clauses at 0x0000018C17D8ACB0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 723>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (check_docs_required_clauses)

 760           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18115020, file "scripts\pas173_brokerage_operator_readiness_check.py", line 760>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_playbook_required_clauses at 0x0000018C17D8B9D0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 760>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              61 (check_playbook_required_clauses)

 791           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18115110, file "scripts\pas173_brokerage_operator_readiness_check.py", line 791>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts\pas173_brokerage_operator_readiness_check.py", line 791>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (check_self_no_env_or_db)

 825           LOAD_CONST              58 (<code object __annotate__ at 0x0000018C18115200, file "scripts\pas173_brokerage_operator_readiness_check.py", line 825>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object _aggregate at 0x0000018C17EC44A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 825>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_aggregate)

 841           LOAD_CONST              60 (<code object __annotate__ at 0x0000018C181152F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 841>)
               MAKE_FUNCTION
               LOAD_CONST              61 (<code object _operator_actions at 0x0000018C180483B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 841>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_operator_actions)

 851           LOAD_CONST              62 (<code object __annotate__ at 0x0000018C181153E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 851>)
               MAKE_FUNCTION
               LOAD_CONST              63 (<code object evaluate at 0x0000018C17E93E60, file "scripts\pas173_brokerage_operator_readiness_check.py", line 851>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              65 (evaluate)

 887           LOAD_CONST              64 ('pas173_brokerage_operator_readiness_report.json')
               STORE_NAME              66 (REPORT_FILENAME)

 890           LOAD_CONST              65 (<code object __annotate__ at 0x0000018C181155C0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 890>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object _build_parser at 0x0000018C1801D1A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 890>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              67 (_build_parser)

 924           LOAD_CONST              67 (<code object __annotate__ at 0x0000018C181156B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 924>)
               MAKE_FUNCTION
               LOAD_CONST              68 (<code object _print_summary at 0x0000018C17D8C5C0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 924>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              68 (_print_summary)

 942           LOAD_CONST              69 (<code object __annotate__ at 0x0000018C18025830, file "scripts\pas173_brokerage_operator_readiness_check.py", line 942>)
               MAKE_FUNCTION
               LOAD_CONST              70 (<code object _write_report at 0x0000018C180FC030, file "scripts\pas173_brokerage_operator_readiness_check.py", line 942>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              69 (_write_report)

 956           LOAD_CONST              87 ((None,))
               LOAD_CONST              71 (<code object __annotate__ at 0x0000018C181157A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 956>)
               MAKE_FUNCTION
               LOAD_CONST              72 (<code object main at 0x0000018C17D893A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 956>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              70 (main)

 984           LOAD_NAME               71 (__name__)
               LOAD_CONST              73 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 985           LOAD_NAME                6 (sys)
               LOAD_ATTR              144 (exit)
               PUSH_NULL
               LOAD_NAME               70 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 984   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  70           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  71   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          361 (to L1)

  70   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 258>:
258           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

259           LOAD_CONST               2 ('str')

258           LOAD_CONST               3 ('status')

259           LOAD_CONST               2 ('str')

258           LOAD_CONST               4 ('label')

259           LOAD_CONST               2 ('str')

258           LOAD_CONST               5 ('severity')

260           LOAD_CONST               2 ('str')

258           LOAD_CONST               6 ('detail')

260           LOAD_CONST               2 ('str')

258           LOAD_CONST               7 ('return')

261           LOAD_CONST               8 ('dict')

258           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3B40, file "scripts\pas173_brokerage_operator_readiness_check.py", line 258>:
258           RESUME                   0

263           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

264           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

265           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

266           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

267           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

262           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 271>:
271           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 271>:
271           RESUME                   0

272           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas173_brokerage_operator_readiness_check.py", line 275>:
275           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053E10, file "scripts\pas173_brokerage_operator_readiness_check.py", line 275>:
 275           RESUME                   0

 276           NOP

 277   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 278           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 279   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 278   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 282>:
282           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17D81580, file "scripts\pas173_brokerage_operator_readiness_check.py", line 282>:
282            RESUME                   0

283            BUILD_LIST               0
               STORE_FAST               1 (out)

284            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

285    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

286            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

287            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

288            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

289            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

290            JUMP_FORWARD           240 (to L13)

291    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

292            JUMP_BACKWARD           59 (to L1)

293    L3:     LOAD_FAST_BORROW         0 (src)
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

294    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

295            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

296            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

297            JUMP_FORWARD           138 (to L13)

298    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

299            JUMP_BACKWARD          161 (to L1)

300    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

301            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

302            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

303    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

304            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

305            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

306            JUMP_BACKWARD           30 (to L7)

307    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

308    L9:     JUMP_FORWARD            11 (to L11)

309   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

310   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

311            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

312   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

313            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

314   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\pas173_brokerage_operator_readiness_check.py", line 321>:
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

Disassembly of <code object check_files_present at 0x0000018C18061470, file "scripts\pas173_brokerage_operator_readiness_check.py", line 321>:
321           RESUME                   0

322           BUILD_LIST               0
              STORE_FAST               1 (out)

323           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
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

328   L3:     LOAD_CONST               3 ('Required PAS173 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

329           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

330           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

325   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

323   L6:     END_FOR
              POP_ITER

332           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas173_brokerage_operator_readiness_check.py", line 335>:
335           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C180606F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 335>:
335           RESUME                   0

336           BUILD_LIST               0
              STORE_FAST               1 (out)

337           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

338           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

339           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

340           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

341           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

342   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

343           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

344           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS173 must not delete')

339   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

337   L6:     END_FOR
              POP_ITER

346           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 349>:
349           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18061110, file "scripts\pas173_brokerage_operator_readiness_check.py", line 349>:
349           RESUME                   0

350           BUILD_LIST               0
              STORE_FAST               1 (out)

351           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

352           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

353           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

354           LOAD_CONST               0 ('memory_review:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

355           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

356   L3:     LOAD_CONST               3 ('Memory Review file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

357           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

358           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('Memory Review file deleted — PAS173 must not touch')

353   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

351   L6:     END_FOR
              POP_ITER

360           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114120, file "scripts\pas173_brokerage_operator_readiness_check.py", line 363>:
363           RESUME                   0
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

Disassembly of <code object check_worker_off_by_default at 0x0000018C1801C9E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 363>:
363           RESUME                   0

364           BUILD_LIST               0
              STORE_FAST               1 (out)

365           LOAD_GLOBAL              1 (Path + NULL)
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

366           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

368           LOAD_CONST               5 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         6 (to L2)
              NOT_TAKEN
              POP_TOP

369           LOAD_CONST               6 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
              LOAD_FAST_BORROW         3 (src)
              CONTAINS_OP              0 (in)

367   L2:     STORE_FAST               4 (literal_ok)

371           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

372           LOAD_CONST               7 ('worker:off_by_default')

373           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               8 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               9 ('FAIL')

374   L4:     LOAD_CONST              10 ('Pending-call worker is OFF by default (strict env literal)')

375           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

376           LOAD_FAST_BORROW         4 (literal_ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L6)
      L5:     LOAD_CONST              11 ('missing strict enable-literal constant')

371   L6:     LOAD_CONST              12 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

378           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114210, file "scripts\pas173_brokerage_operator_readiness_check.py", line 381>:
381           RESUME                   0
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

Disassembly of <code object check_no_startup_worker at 0x0000018C17EA5300, file "scripts\pas173_brokerage_operator_readiness_check.py", line 381>:
381           RESUME                   0

382           BUILD_LIST               0
              STORE_FAST               1 (out)

383           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

384           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

385           LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
              LOAD_FAST_BORROW         3 (src)
              CALL                     1
              STORE_FAST               4 (executable)

386           BUILD_LIST               0
              STORE_FAST               5 (bad)

387           LOAD_CONST               3 ('from app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L2)
              NOT_TAKEN

388           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               4 ('from app.services.ingestion.worker import …')
              CALL                     1
              POP_TOP

389   L2:     LOAD_CONST               5 ('import app.services.ingestion.worker')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L3)
              NOT_TAKEN

390           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               5 ('import app.services.ingestion.worker')
              CALL                     1
              POP_TOP

391   L3:     LOAD_CONST               6 ('run_worker_loop')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L4)
              NOT_TAKEN

392           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               7 ('run_worker_loop reference')
              CALL                     1
              POP_TOP

393   L4:     LOAD_CONST               8 ('process_pending_call(')
              LOAD_FAST_BORROW         4 (executable)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE       18 (to L5)
              NOT_TAKEN

394           LOAD_FAST_BORROW         5 (bad)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_CONST               9 ('process_pending_call call')
              CALL                     1
              POP_TOP

395   L5:     LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

396           LOAD_CONST              10 ('main:no_startup_worker')

397           LOAD_FAST_BORROW         5 (bad)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST              11 ('FAIL')
              JUMP_FORWARD             1 (to L7)
      L6:     LOAD_CONST              12 ('PASS')

398   L7:     LOAD_CONST              13 ('FastAPI lifespan does not auto-start the pending-call worker')

399           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

400           LOAD_FAST_BORROW         5 (bad)
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

395   L9:     LOAD_CONST              16 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

402           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181143F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 405>:
405           RESUME                   0
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

Disassembly of <code object check_profile_service at 0x0000018C17F01670, file "scripts\pas173_brokerage_operator_readiness_check.py", line 405>:
405           RESUME                   0

406           BUILD_LIST               0
              STORE_FAST               1 (out)

407           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('services')
              BINARY_OP               11 (/)
              LOAD_CONST               2 ('brokerage')
              BINARY_OP               11 (/)
              LOAD_CONST               3 ('profile_service.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (p)

408           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

409           LOAD_GLOBAL              4 (REQUIRED_PROFILE_SERVICE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                78 (to L7)
              STORE_FAST               4 (tok)

410           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

411           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

412           LOAD_CONST               5 ('profile_service:')
              LOAD_FAST_BORROW         4 (tok)
              LOAD_CONST               6 (slice(None, 48, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

413           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               7 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               8 ('FAIL')

414   L4:     LOAD_CONST               9 ('Profile service token: ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

415           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

416           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              10 ('missing token ')
              LOAD_FAST_BORROW         4 (tok)
              FORMAT_SIMPLE
              BUILD_STRING             2

411   L6:     LOAD_CONST              11 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           80 (to L2)

409   L7:     END_FOR
              POP_ITER

418           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181144E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 421>:
421           RESUME                   0
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

Disassembly of <code object check_config_validator at 0x0000018C17EA5880, file "scripts\pas173_brokerage_operator_readiness_check.py", line 421>:
421            RESUME                   0

422            BUILD_LIST               0
               STORE_FAST               1 (out)

423            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('brokerage')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('config_validator.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

424            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

425            LOAD_GLOBAL              4 (REQUIRED_CONFIG_VALIDATOR_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

426            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

427            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

428            LOAD_CONST               5 ('config_validator:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

429            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

430    L4:     LOAD_CONST               9 ('Config validator token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

431            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

432            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

427    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

425    L7:     END_FOR
               POP_ITER

436            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

437            BUILD_LIST               0
               STORE_FAST               7 (bad)

440            LOAD_CONST              12 ('logger.info(f')
               LOAD_FAST_BORROW         6 (executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE        2 (to L8)
               NOT_TAKEN

446            NOP

447    L8:     LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

448            LOAD_CONST              13 ('config_validator:no_value_echoes')

449            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('PASS')

450   L10:     LOAD_CONST              14 ('Config validator does not echo env / brokerage values')

451            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

452            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD            16 (to L12)
      L11:     LOAD_CONST              15 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1

447   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

454            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181145D0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 457>:
457           RESUME                   0
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

Disassembly of <code object check_onboarding_templates at 0x0000018C17F79120, file "scripts\pas173_brokerage_operator_readiness_check.py", line 457>:
457            RESUME                   0

458            BUILD_LIST               0
               STORE_FAST               1 (out)

459            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('brokerage')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('onboarding_templates.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

460            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

461            LOAD_GLOBAL              4 (REQUIRED_ONBOARDING_TEMPLATES_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

462            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

463            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

464            LOAD_CONST               5 ('onboarding_templates:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

465            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

466    L4:     LOAD_CONST               9 ('Onboarding templates token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

467            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

468            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

463    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

461    L7:     END_FOR
               POP_ITER

471            LOAD_CONST              12 ('"generated_at": None')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (deterministic)

472            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

473            LOAD_CONST              13 ('onboarding_templates:deterministic')

474            LOAD_FAST_BORROW         6 (deterministic)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               8 ('FAIL')

475    L9:     LOAD_CONST              14 ('Onboarding templates are deterministic (no timestamp echoed)')

476            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

477            LOAD_FAST_BORROW         6 (deterministic)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              15 ('missing deterministic generated_at=None marker')

472   L11:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

480            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               7 (executable)

481            BUILD_LIST               0
               STORE_FAST               8 (bad)

482            LOAD_CONST              16 ('get_supabase')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L12)
               NOT_TAKEN

483            LOAD_FAST_BORROW         8 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_CONST              17 ('get_supabase call')
               CALL                     1
               POP_TOP

484   L12:     LOAD_CONST              18 ('os.environ')
               LOAD_FAST_BORROW         7 (executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L13)
               NOT_TAKEN

485            LOAD_FAST_BORROW         8 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_CONST              19 ('os.environ read')
               CALL                     1
               POP_TOP

486   L13:     LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

487            LOAD_CONST              20 ('onboarding_templates:no_db_env_read')

488            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L15)
      L14:     LOAD_CONST               7 ('PASS')

489   L15:     LOAD_CONST              21 ('Onboarding templates never read DB or env')

490            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

491            LOAD_FAST_BORROW         8 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L16)
               NOT_TAKEN
               LOAD_CONST              22 (', ')
               LOAD_ATTR               15 (join + NULL|self)
               LOAD_FAST_BORROW         8 (bad)
               CALL                     1
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               4 ('')

486   L17:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

493            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181147B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 496>:
496           RESUME                   0
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

Disassembly of <code object check_operator_actions at 0x0000018C17CD1490, file "scripts\pas173_brokerage_operator_readiness_check.py", line 496>:
496            RESUME                   0

497            BUILD_LIST               0
               STORE_FAST               1 (out)

498            LOAD_GLOBAL              1 (Path + NULL)
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

499            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

500            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_ACTIONS_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

501            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

502            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

503            LOAD_CONST               5 ('operator_actions:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               6 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

504            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

505    L4:     LOAD_CONST               9 ('Operator actions token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

506            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

507            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

502    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

500    L7:     END_FOR
               POP_ITER

510            LOAD_CONST              12 ('ALLOWED_OPERATOR_ACTIONS = (')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (declared_ok)

511            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

512            LOAD_CONST              13 ('operator_actions:closed_allow_list')

513            LOAD_FAST_BORROW         6 (declared_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               8 ('FAIL')

514    L9:     LOAD_CONST              14 ('Operator actions allow-list is a closed literal tuple')

515            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

516            LOAD_FAST_BORROW         6 (declared_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              15 ('expected literal tuple declaration')

511   L11:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

518            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114990, file "scripts\pas173_brokerage_operator_readiness_check.py", line 521>:
521           RESUME                   0
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

Disassembly of <code object check_operator_brokerages_route at 0x0000018C17EF9A30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 521>:
521            RESUME                   0

522            BUILD_LIST               0
               STORE_FAST               1 (out)

523            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('operator_brokerages.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

524            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
       L1:     STORE_FAST               3 (src)

525            LOAD_GLOBAL              4 (REQUIRED_OPERATOR_BROKERAGES_TOKENS)
               GET_ITER
       L2:     FOR_ITER                78 (to L7)
               STORE_FAST               4 (tok)

526            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

527            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

528            LOAD_CONST               4 ('operator_brokerages:')
               LOAD_FAST_BORROW         4 (tok)
               LOAD_CONST               5 (slice(None, 48, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

529            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               7 ('FAIL')

530    L4:     LOAD_CONST               8 ('Operator brokerages route token: ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

531            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

532            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               9 ('missing token ')
               LOAD_FAST_BORROW         4 (tok)
               FORMAT_SIMPLE
               BUILD_STRING             2

527    L6:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           80 (to L2)

525    L7:     END_FOR
               POP_ITER

535            LOAD_GLOBAL             13 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

536            BUILD_LIST               0
               STORE_FAST               7 (bad)

537            LOAD_GLOBAL             14 (FORBIDDEN_PII_EXPOSURE_TOKENS)
               GET_ITER
       L8:     FOR_ITER                28 (to L10)
               STORE_FAST               4 (tok)

538            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (tok, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L8)

539    L9:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (tok)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L8)

537   L10:     END_FOR
               POP_ITER

540            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

541            LOAD_CONST              11 ('operator_brokerages:no_pii_exposure')

542            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               7 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               6 ('PASS')

543   L12:     LOAD_CONST              12 ('Operator brokerages route does not reference transcript/raw payload')

544            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

545            LOAD_FAST_BORROW         7 (bad)
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

540   L14:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

548            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST              15 ('main.py')
               BINARY_OP               11 (/)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               3 ('')
      L15:     STORE_FAST               8 (main_src)

550            LOAD_CONST              16 ('operator_brokerages_router')
               LOAD_FAST_BORROW         8 (main_src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        6 (to L16)
               NOT_TAKEN
               POP_TOP

551            LOAD_CONST              17 ('prefix="/ops/brokerages"')
               LOAD_FAST_BORROW         8 (main_src)
               CONTAINS_OP              0 (in)

549   L16:     STORE_FAST               9 (router_ok)

553            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

554            LOAD_CONST              18 ('operator_brokerages:router_mounted')

555            LOAD_FAST_BORROW         9 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               6 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               7 ('FAIL')

556   L18:     LOAD_CONST              19 ('operator_brokerages_router is mounted at /ops/brokerages')

557            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

558            LOAD_FAST_BORROW         9 (router_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               3 ('')
               JUMP_FORWARD             1 (to L20)

559   L19:     LOAD_CONST              20 ('expected `operator_brokerages_router` import + `include_router(..., prefix="/ops/brokerages")`')

553   L20:     LOAD_CONST              10 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

563            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114A80, file "scripts\pas173_brokerage_operator_readiness_check.py", line 566>:
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

Disassembly of <code object check_v21_sql at 0x0000018C181A30B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 566>:
  --            MAKE_CELL               10 (src)

 566            RESUME                   0

 567            BUILD_LIST               0
                STORE_FAST               1 (out)

 568            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('migrate_v21_brokerage_profiles.sql')
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
        L1:     STORE_DEREF             10 (src)

 570            LOAD_DEREF              10 (src)
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

 573            LOAD_CONST               4 ('v21_sql:proposal_only')

 574            LOAD_FAST_BORROW         4 (proposal_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               6 ('FAIL')

 575    L3:     LOAD_CONST               7 ("v21 SQL carries 'PROPOSAL ONLY' guardrail")

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

 581            LOAD_CONST              11 ('v21_sql:do_not_execute')

 582            LOAD_FAST_BORROW         5 (do_not_exec)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 ('FAIL')

 583    L7:     LOAD_CONST              12 ("v21 SQL carries 'DO NOT EXECUTE' trailer")

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
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 588>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 589            LOAD_CONST              34 (("'NOT_STARTED'", "'IN_PROGRESS'", "'CONFIGURED'", "'VERIFIED'", "'LIVE'", "'PAUSED'"))
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
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C18026130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 588>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 589            LOAD_CONST              34 (("'NOT_STARTED'", "'IN_PROGRESS'", "'CONFIGURED'", "'VERIFIED'", "'LIVE'", "'PAUSED'"))
                GET_ITER

 588            CALL                     0
                CALL                     1
       L14:     STORE_FAST               6 (statuses_ok)

 594            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 595            LOAD_CONST              17 ('v21_sql:closed_onboarding_status_enum')

 596            LOAD_FAST_BORROW         6 (statuses_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L16)
       L15:     LOAD_CONST               6 ('FAIL')

 597   L16:     LOAD_CONST              18 ('v21 SQL carries the closed onboarding_status enum literals')

 598            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 599            LOAD_FAST_BORROW         6 (statuses_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              19 ('missing one or more status literals')

 594   L18:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 602            LOAD_GLOBAL             12 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L22)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 602>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 603            LOAD_CONST              35 (("'INTERNAL'", "'TRUSTED_PILOT'", "'EXPANDED_PILOT'", "'PRODUCTION'"))
                GET_ITER

 602            CALL                     0
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
                LOAD_FAST_BORROW        10 (src)
                BUILD_TUPLE              1
                LOAD_CONST              20 (<code object <genexpr> at 0x0000018C18025130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 602>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 603            LOAD_CONST              35 (("'INTERNAL'", "'TRUSTED_PILOT'", "'EXPANDED_PILOT'", "'PRODUCTION'"))
                GET_ITER

 602            CALL                     0
                CALL                     1
       L23:     STORE_FAST               7 (stages_ok)

 608            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 609            LOAD_CONST              21 ('v21_sql:closed_pilot_stage_enum')

 610            LOAD_FAST_BORROW         7 (stages_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L24)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L25)
       L24:     LOAD_CONST               6 ('FAIL')

 611   L25:     LOAD_CONST              22 ('v21 SQL carries the closed pilot_stage enum literals')

 612            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 613            LOAD_FAST_BORROW         7 (stages_ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L26)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L27)
       L26:     LOAD_CONST              23 ('missing one or more pilot_stage literals')

 608   L27:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 616            LOAD_CONST              24 ('pas_brokerage_profiles_tenant_no_insert')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L28)
                NOT_TAKEN
                POP_TOP

 617            LOAD_CONST              25 ('with check (false)')
                LOAD_FAST_BORROW         3 (lower)
                CONTAINS_OP              0 (in)

 615   L28:     STORE_FAST               8 (tenant_no_write)

 619            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 620            LOAD_CONST              26 ('v21_sql:tenant_no_write')

 621            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L29)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L30)
       L29:     LOAD_CONST               6 ('FAIL')

 622   L30:     LOAD_CONST              27 ('v21 SQL denies tenant write')

 623            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 624            LOAD_FAST_BORROW         8 (tenant_no_write)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L31)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L32)
       L31:     LOAD_CONST              28 ('missing tenant-write denial')

 619   L32:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 627            LOAD_CONST              29 ('pas_brokerage_profiles_tenant_select')
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        6 (to L33)
                NOT_TAKEN
                POP_TOP

 628            LOAD_CONST              30 ("auth.jwt() ->> 'brokerage_id'")
                LOAD_DEREF              10 (src)
                CONTAINS_OP              0 (in)

 626   L33:     STORE_FAST               9 (tenant_select_scoped)

 630            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 631            LOAD_CONST              31 ('v21_sql:tenant_select_scoped')

 632            LOAD_FAST_BORROW         9 (tenant_select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L34)
                NOT_TAKEN
                LOAD_CONST               5 ('PASS')
                JUMP_FORWARD             1 (to L35)
       L34:     LOAD_CONST               6 ('FAIL')

 633   L35:     LOAD_CONST              32 ('v21 SQL scopes tenant SELECT to own brokerage_id')

 634            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 635            LOAD_FAST_BORROW         9 (tenant_select_scoped)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L36)
                NOT_TAKEN
                LOAD_CONST               2 ('')
                JUMP_FORWARD             1 (to L37)
       L36:     LOAD_CONST              33 ('missing tenant scoped select')

 630   L37:     LOAD_CONST               9 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 637            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 588>:
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

Disassembly of <code object <genexpr> at 0x0000018C18025130, file "scripts\pas173_brokerage_operator_readiness_check.py", line 602>:
  --           COPY_FREE_VARS           1

 602           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 603   L2:     FOR_ITER                 9 (to L3)
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

Disassembly of <code object __annotate__ at 0x0000018C18114B70, file "scripts\pas173_brokerage_operator_readiness_check.py", line 640>:
640           RESUME                   0
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

Disassembly of <code object check_event_contract at 0x0000018C17FED630, file "scripts\pas173_brokerage_operator_readiness_check.py", line 640>:
640           RESUME                   0

641           BUILD_LIST               0
              STORE_FAST               1 (out)

642           LOAD_GLOBAL              1 (Path + NULL)
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

643           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

644           LOAD_GLOBAL              4 (REQUIRED_EVENT_TYPES)
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

645           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

646           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

647           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

648           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

649   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

650           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

651           LOAD_FAST_BORROW         5 (ok)
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

646   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

644   L7:     END_FOR
              POP_ITER

653           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114C60, file "scripts\pas173_brokerage_operator_readiness_check.py", line 656>:
656           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17E95410, file "scripts\pas173_brokerage_operator_readiness_check.py", line 656>:
656            RESUME                   0

657            BUILD_LIST               0
               STORE_FAST               1 (out)

658            LOAD_CONST              10 (('app/services/brokerage/__init__.py', 'app/services/brokerage/profile_service.py', 'app/services/brokerage/config_validator.py', 'app/services/brokerage/onboarding_templates.py', 'app/services/operator/__init__.py', 'app/services/operator/operator_actions.py', 'app/routes/operator_brokerages.py', 'scripts/pas173_brokerage_operator_readiness_check.py'))
               STORE_FAST               2 (files)

668            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     EXTENDED_ARG             1
               FOR_ITER               297 (to L15)
               STORE_FAST               3 (relpath)

669            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

670            LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN

671            JUMP_BACKWARD           46 (to L1)

672    L2:     LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L3:     STORE_FAST               5 (src)

673            BUILD_LIST               0
               STORE_FAST               6 (bad)

674            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L4:     FOR_ITER               107 (to L10)
               STORE_FAST               7 (line)

675            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

676            LOAD_FAST_BORROW         8 (stripped)
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

677    L5:     JUMP_BACKWARD           52 (to L4)

678    L6:     LOAD_GLOBAL             12 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L7:     FOR_ITER                45 (to L9)
               STORE_FAST               9 (prefix)

679            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L7)

680    L8:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L7)

678    L9:     END_FOR
               POP_ITER
               JUMP_BACKWARD          109 (to L4)

674   L10:     END_FOR
               POP_ITER

681            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

682            LOAD_CONST               3 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

683            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L11)
               NOT_TAKEN
               LOAD_CONST               4 ('FAIL')
               JUMP_FORWARD             1 (to L12)
      L11:     LOAD_CONST               5 ('PASS')

684   L12:     LOAD_CONST               6 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

685            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

687            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       43 (to L13)
               NOT_TAKEN

686            LOAD_CONST               7 ('forbidden import prefixes: ')
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

687   L13:     LOAD_CONST               1 ('')

681   L14:     LOAD_CONST               9 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          300 (to L1)

668   L15:     END_FOR
               POP_ITER

689            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114D50, file "scripts\pas173_brokerage_operator_readiness_check.py", line 692>:
692           RESUME                   0
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

Disassembly of <code object check_no_inbox_scan_tokens at 0x0000018C17CD1ED0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 692>:
692            RESUME                   0

693            BUILD_LIST               0
               STORE_FAST               1 (out)

694            LOAD_CONST               9 (('app/services/brokerage/profile_service.py', 'app/services/brokerage/config_validator.py', 'app/services/brokerage/onboarding_templates.py', 'app/services/operator/operator_actions.py', 'app/routes/operator_brokerages.py', 'scripts/pas173_brokerage_operator_readiness_check.py'))
               STORE_FAST               2 (files)

702            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               200 (to L11)
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

705            JUMP_BACKWARD           45 (to L1)

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

707            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         5 (src)
               CALL                     1
               STORE_FAST               6 (executable)

708            BUILD_LIST               0
               STORE_FAST               7 (bad)

709            LOAD_GLOBAL              8 (FORBIDDEN_INBOX_TOKENS)
               GET_ITER
       L4:     FOR_ITER                28 (to L6)
               STORE_FAST               8 (token)

710            LOAD_FAST_BORROW_LOAD_FAST_BORROW 134 (token, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L4)

711    L5:     LOAD_FAST_BORROW         7 (bad)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_FAST_BORROW         8 (token)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           30 (to L4)

709    L6:     END_FOR
               POP_ITER

712            LOAD_FAST                1 (out)
               LOAD_ATTR               11 (append + NULL|self)
               LOAD_GLOBAL             13 (_check + NULL)

713            LOAD_CONST               2 ('no_inbox_scan:')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

714            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L7)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L8)
       L7:     LOAD_CONST               4 ('PASS')

715    L8:     LOAD_CONST               5 ('No inbox-scanning tokens: ')
               LOAD_FAST_BORROW         3 (relpath)
               FORMAT_SIMPLE
               BUILD_STRING             2

716            LOAD_GLOBAL             14 (SEVERITY_BLOCK)

718            LOAD_FAST_BORROW         7 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L9)
               NOT_TAKEN

717            LOAD_CONST               6 ('inbox-scan tokens present: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               17 (join + NULL|self)
               LOAD_FAST_BORROW         7 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L10)

718    L9:     LOAD_CONST               1 ('')

712   L10:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          202 (to L1)

702   L11:     END_FOR
               POP_ITER

720            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18114F30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 723>:
723           RESUME                   0
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

Disassembly of <code object check_docs_required_clauses at 0x0000018C17D8ACB0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 723>:
  --            MAKE_CELL                8 (lower)

 723            RESUME                   0

 724            BUILD_LIST               0
                STORE_FAST               1 (out)

 725            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas173_brokerage_operator_system.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 726            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 727            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 728            LOAD_CONST              13 ((('onboarding-doctrine', ('onboarding doctrine',)), ('self-serve-doctrine', ('controlled self-serve', 'self-serve doctrine')), ('multi-brokerage', ('multi-brokerage',)), ('no-autonomous', ('no-autonomous', 'no autonomous', 'autonomous decisioning')), ('rollout-stages', ('rollout stages', 'pilot_stage', 'pilot stage')), ('launch-readiness', ('launch readiness',)), ('rollback', ('rollback',)), ('escalation', ('escalation',)), ('pilot-expansion', ('pilot expansion',)), ('no-gmail', ('no gmail',)), ('limitations', ('limitation',)), ('not-built', ('intentionally not built', 'intentionally does not', 'deliberately not'))))
                STORE_FAST               4 (required_phrases)

 747            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 748            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas173_brokerage_operator_readiness_check.py", line 748>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026630, file "scripts\pas173_brokerage_operator_readiness_check.py", line 748>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 749            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 750            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 751            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 752    L9:     LOAD_CONST               9 ('Doctrine doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 753            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 755            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 754            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 755   L10:     LOAD_CONST               2 ('')

 749   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 747   L12:     END_FOR
                POP_ITER

 757            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026630, file "scripts\pas173_brokerage_operator_readiness_check.py", line 748>:
  --           COPY_FREE_VARS           1

 748           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115020, file "scripts\pas173_brokerage_operator_readiness_check.py", line 760>:
760           RESUME                   0
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

Disassembly of <code object check_playbook_required_clauses at 0x0000018C17D8B9D0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 760>:
  --            MAKE_CELL                8 (lower)

 760            RESUME                   0

 761            BUILD_LIST               0
                STORE_FAST               1 (out)

 762            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('orvn_brokerage_onboarding_playbook.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 763            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 764            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 765            LOAD_CONST              13 ((('pre-flight', ('pre-flight',)), ('onboarding-flow', ('onboarding workflow', 'onboarding flow')), ('operator-actions', ('operator action',)), ('health-snapshot', ('health snapshot',)), ('launch-readiness', ('launch readiness',)), ('pilot-expansion', ('pilot expansion',)), ('escalation', ('escalation',)), ('rollback', ('rollback',)), ('no-gmail', ('no gmail',)), ('doctrine', ('doctrine',))))
                STORE_FAST               4 (required_phrases)

 778            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 779            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024B30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 779>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18024B30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 779>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 780            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 781            LOAD_CONST               6 ('playbook:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 782            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 783    L9:     LOAD_CONST               9 ('Onboarding playbook carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 784            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 786            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 785            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 786   L10:     LOAD_CONST               2 ('')

 780   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 778   L12:     END_FOR
                POP_ITER

 788            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18024B30, file "scripts\pas173_brokerage_operator_readiness_check.py", line 779>:
  --           COPY_FREE_VARS           1

 779           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18115110, file "scripts\pas173_brokerage_operator_readiness_check.py", line 791>:
791           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_db at 0x0000018C17D88890, file "scripts\pas173_brokerage_operator_readiness_check.py", line 791>:
791            RESUME                   0

792            BUILD_LIST               0
               STORE_FAST               1 (out)

793            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

794            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

795            LOAD_GLOBAL              9 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               4 (executable)

796            BUILD_LIST               0
               STORE_FAST               5 (bad)

797            LOAD_FAST_BORROW         4 (executable)
               LOAD_ATTR               11 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     FOR_ITER               199 (to L9)
               STORE_FAST               6 (raw_line)

798            LOAD_FAST_BORROW         6 (raw_line)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

799            LOAD_FAST_BORROW         7 (stripped)
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L3)
               NOT_TAKEN

800            JUMP_BACKWARD           29 (to L2)

801    L3:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              15 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

802            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               1 ('dotenv import')
               CALL                     1
               POP_TOP

803    L4:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              16 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

804            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               2 ('supabase import')
               CALL                     1
               POP_TOP

805    L5:     LOAD_CONST               3 ('load_dotenv()')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

806            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               4 ('load_dotenv() call')
               CALL                     1
               POP_TOP

807    L6:     LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               15 (startswith + NULL|self)
               LOAD_CONST              17 (('os.environ[', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

808            LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               5 ('environ read')
               CALL                     1
               POP_TOP

809    L7:     LOAD_CONST               6 ('get_supabase')
               LOAD_FAST_BORROW         7 (stripped)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD          182 (to L2)

810    L8:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_CONST               7 ('supabase client call')
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          201 (to L2)

797    L9:     END_FOR
               POP_ITER

811            LOAD_FAST                1 (out)
               LOAD_ATTR               17 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

812            LOAD_CONST               8 ('self_check:no_env_or_db')

813            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               9 ('FAIL')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              10 ('PASS')

814   L11:     LOAD_CONST              11 ('PAS173 readiness checker never reads .env / touches DB')

815            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

816            LOAD_FAST_BORROW         5 (bad)
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

811   L13:     LOAD_CONST              14 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

818            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18115200, file "scripts\pas173_brokerage_operator_readiness_check.py", line 825>:
825           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC44A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 825>:
 825            RESUME                   0

 827            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 826            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 827    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 828            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 827    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 828    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 827    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 826    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 831            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 830            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 831   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 832            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 831   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 832   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 831   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 830   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 835            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 836   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 837            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 834            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 826            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 830            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C181152F0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 841>:
841           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180483B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 841>:
841           RESUME                   0

842           BUILD_LIST               0
              STORE_FAST               1 (out)

843           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

844           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

845           JUMP_BACKWARD           19 (to L1)

846   L2:     LOAD_FAST_BORROW         2 (c)
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

847           LOAD_FAST                1 (out)
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

843   L5:     END_FOR
              POP_ITER

848           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181153E0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 851>:
851           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17E93E60, file "scripts\pas173_brokerage_operator_readiness_check.py", line 851>:
851           RESUME                   0

852           BUILD_LIST               0
              STORE_FAST               1 (checks)

853           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

854           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

855           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

856           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_worker_off_by_default + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

857           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_no_startup_worker + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

858           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_profile_service + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

859           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_config_validator + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

860           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_onboarding_templates + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

861           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_operator_actions + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

862           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_operator_brokerages_route + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

863           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_v21_sql + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

864           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_event_contract + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

865           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

866           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             29 (check_no_inbox_scan_tokens + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

867           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             31 (check_docs_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

868           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             33 (check_playbook_required_clauses + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

869           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             35 (check_self_no_env_or_db + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

871           LOAD_GLOBAL             37 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

873           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS173')

874           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             39 (_now_iso + NULL)
              CALL                     0

875           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

876           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             40 (VERDICT_READY)
              COMPARE_OP              72 (==)

877           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

878           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

879           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             43 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

880           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 880>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

881           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             45 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053990, file "scripts\pas173_brokerage_operator_readiness_check.py", line 881>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

882           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

883           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             47 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

872           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 880>:
 880           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053990, file "scripts\pas173_brokerage_operator_readiness_check.py", line 881>:
 881           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C181155C0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 890>:
890           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801D1A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 890>:
890           RESUME                   0

891           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

892           LOAD_CONST               0 ('pas173_brokerage_operator_readiness_check')

894           LOAD_CONST               1 ('PAS173 — Evaluate the brokerage operator system (profile service + config validator + onboarding templates + operator actions + multi-brokerage ops routes). Read-only — never reads .env, never touches Supabase, never runs a migration.')

891           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

901           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

902           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

903           LOAD_CONST               4 ('Repo root (default: parent of this script).')

901           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

905           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

906           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

907           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

905           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

909           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

910           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

911           LOAD_CONST              11 ('Emit JSON on stdout in addition to the summary.')

909           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

913           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

914           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

915           LOAD_CONST              14 ('Skip writing the JSON report file.')

913           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

917           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

918           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

919           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

917           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

921           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C181156B0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 924>:
924           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8C5C0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 924>:
924           RESUME                   0

925           LOAD_GLOBAL              1 (print + NULL)

926           LOAD_CONST               0 ('[PAS173] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

927           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

928           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

929           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

930           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

931           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

926           BUILD_STRING            12

925           CALL                     1
              POP_TOP

933           LOAD_FAST_BORROW         0 (report)
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

934           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

935           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS173] operator actions:')
              CALL                     1
              POP_TOP

936           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

937           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

936   L3:     END_FOR
              POP_ITER

938           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

939           LOAD_GLOBAL              1 (print + NULL)
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

938   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

934   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "scripts\pas173_brokerage_operator_readiness_check.py", line 942>:
942           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C180FC030, file "scripts\pas173_brokerage_operator_readiness_check.py", line 942>:
 942           RESUME                   0

 943           NOP

 944   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 945           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 946           LOAD_CONST               3 ('utf-8')

 944           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 948           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 949   L4:     LOAD_GLOBAL             11 (print + NULL)

 950           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 951           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 950           BUILD_STRING             4

 952           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 949           LOAD_CONST               7 (('file',))
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

 948   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C181157A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 956>:
956           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D893A0, file "scripts\pas173_brokerage_operator_readiness_check.py", line 956>:
 956            RESUME                   0

 957            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 958            NOP

 959    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 963    L2:     LOAD_GLOBAL             10 (os)
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

 964            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 965            LOAD_GLOBAL             23 (print + NULL)

 966            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 967            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 965            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 969            LOAD_SMALL_INT           2
                RETURN_VALUE

 971    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 973            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 974            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 976    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 978            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 979            LOAD_GLOBAL             23 (print + NULL)
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

 981    L6:     LOAD_FAST                5 (report)
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

 960            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 961    L9:     LOAD_FAST                3 (e)
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

 960   L17:     RERAISE                  0

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
