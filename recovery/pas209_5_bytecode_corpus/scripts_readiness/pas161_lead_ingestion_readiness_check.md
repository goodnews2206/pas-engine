# scripts_readiness/pas161_lead_ingestion_readiness_check

- **pyc:** `scripts\__pycache__\pas161_lead_ingestion_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas161_lead_ingestion_readiness_check.py`
- **co_filename (from bytecode):** `scripts/pas161_lead_ingestion_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS161 — Lead ingestion readiness gate.

Deterministic, non-mutating evaluator for "is the lead-
ingestion subsystem wired correctly, structurally safe, and
free of payload-trust regressions?". Walks the repo, confirms
the ingestion module files exist, the four webhook routes are
declared, the FastAPI router is wired into ``app/main.py``,
the four provider normalizers exist, the contracts module
carries the closed-shape doctrine, no forbidden raw-payload
field names appear in the executable surfaces, no Memory
Review file is touched, no vendor / embedding / Supabase /
.env reads are introduced by this phase's own code, and the
companion docs + tests exist.

Emits a verdict (READY / NOT_READY) plus a machine-readable
``pas161_lead_ingestion_readiness_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * imports external vendors,
  * imports embedding / vector libraries,
  * touches the off-limits
    ``scripts/combined_supabase_migration.sql``.

Usage:
  python scripts/pas161_lead_ingestion_readiness_check.py
  python scripts/pas161_lead_ingestion_readiness_check.py --json
  python scripts/pas161_lead_ingestion_readiness_check.py --summary-only
  python scripts/pas161_lead_ingestion_readiness_check.py --strict

Exit codes:
    0  — READY  (verdict == READY)
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_docs_required_doctrine`, `check_files_present`, `check_forbidden_raw_fields`, `check_main_wiring`, `check_memory_review_files_present`, `check_no_forbidden_imports`, `check_normalized_contract_excludes_forbidden`, `check_normalizers_defined`, `check_offlimits_present`, `check_route_response_shape_excludes_raw`, `check_routes_declared`, `check_routes_do_not_trust_body_brokerage_id`, `check_self_no_env_or_vendor`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS161`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS161 — Lead ingestion readiness gate.\n\nDeterministic, non-mutating evaluator for "is the lead-\ningestion subsystem wired correctly, structurally safe, and\nfree of payload-trust regressions?". Walks the repo, confirms\nthe ingestion module files exist, the four webhook routes are\ndeclared, the FastAPI router is wired into ``app/main.py``,\nthe four provider normalizers exist, the contracts module\ncarries the closed-shape doctrine, no forbidden raw-payload\nfield names appear in the executable surfaces, no Memory\nReview file is touched, no vendor / embedding / Supabase /\n.env reads are introduced by this phase\'s own code, and the\ncompanion docs + tests exist.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas161_lead_ingestion_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas161_lead_ingestion_readiness_check.py\n  python scripts/pas161_lead_ingestion_readiness_check.py --json\n  python scripts/pas161_lead_ingestion_readiness_check.py --summary-only\n  python scripts/pas161_lead_ingestion_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas161_lead_ingestion_readiness_report.json'
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
- 'Mirror of the per-phase test helper. Strips ``#`` line\ncomments, ``"""``/``\'\'\'`` triple-quoted blocks, and\nsingle/double-quoted strings, so substring bans on\nforbidden tokens inspect executable code only.'
- '"""'
- "'''"
- 'repo_root'
- 'List[dict]'
- 'file:'
- 'PASS'
- 'FAIL'
- 'Required PAS161 file present: '
- 'missing'
- 'offlimits:'
- 'Off-limits file present (do not modify): '
- 'missing — restore from git history'
- 'PAS161 must NOT modify Memory Review files. We verify\nthey all still EXIST; missing → BLOCK (a PAS161 regression\nthat deleted one would be caught here).'
- 'memory_review_file:'
- 'Memory Review file present (PAS161 must not delete): '
- 'PAS161 must not delete Memory Review files'
- 'app'
- 'routes'
- 'lead_ingestion.py'
- 'routes:source_missing'
- 'lead_ingestion.py is missing'
- 'cannot verify routes'
- 'route:'
- 'Webhook route declared: '
- 'none of accepted declarations present: '
- ' | '
- 'main.py'
- 'main:source_missing'
- 'app/main.py is missing'
- 'cannot verify router wiring'
- 'main:'
- 'app/main.py wires the lead ingestion router'
- 'missing literal: '
- 'services'
- 'ingestion'
- 'normalizers.py'
- 'normalizers:source_missing'
- 'normalizers.py is missing'
- 'normalizer:'
- 'Normalizer defined: '
- 'missing def: '
- 'The four webhook routes must NOT read ``brokerage_id``\nfrom the body. Source-text scan of executable code (after\nstripping comments + strings) — banner comments mention\nthe rule but the executable must not.'
- 'routes:no_body_brokerage_id_trust'
- 'Webhook routes do not read brokerage_id from the body'
- 'forbidden patterns in executable: '
- 'No forbidden raw-payload field tokens in executable code\nof any ingestion file.'
- 'forbidden_field:'
- 'No forbidden raw-payload fields in executable: '
- 'forbidden field tokens in executable: '
- 'No Memory Review imports, no vendor / embedding /\nComposio / TrustClaw imports in any ingestion file.'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- '``NormalizedLead`` must not name forbidden keys among its\nfield list. Detection: the dataclass field block in\n``contracts.py`` must not contain ``raw_payload`` /\n``full_payload`` / ``transcript`` / etc. as identifiers.'
- 'contracts.py'
- 'class NormalizedLead'
- 'contract:class_missing'
- 'NormalizedLead class not found'
- '\ndef '
- 'contract:no_forbidden_fields'
- 'NormalizedLead has no forbidden raw-payload fields'
- 'forbidden field identifiers in class body: '
- "The ingest pipeline's return dict must include the\nclosed allow-list keys and must NOT include forbidden raw\nkeys. Source-text scan of the ``_ingest`` function body."
- 'def _ingest('
- 'route_response:no_ingest_fn'
- '_ingest helper not found in lead_ingestion.py'
- 'route_response:forbidden:'
- 'Route response must not include '
- 'found '
- ' in _ingest body executable'
- 'route_response:missing_key:'
- 'Route response must include key '
- 'route_response:shape_ok'
- 'Route response shape includes closed allow-list and excludes raw payload keys'
- 'docs:missing'
- 'PAS161 doc missing: '
- 'docs:phrase:'
- 'Doc carries clause: '
- 'expected one of: '
- 'Self-check: this readiness script must NOT import dotenv\n/ Supabase / Composio / TrustClaw / OpenAI / Anthropic /\nembedding libs, and must NOT read .env or os.environ.'
- 'dotenv import'
- 'supabase import'
- 'external-vendor import'
- 'embedding / vector import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'self_check:no_env_or_vendor'
- 'PAS161 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS161'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas161_lead_ingestion_readiness_check'
- 'PAS161 — Evaluate the lead-ingestion subsystem for structural correctness and doctrine compliance. Read-only. Does not touch Supabase, .env, or any tenant data.'
- '--repo-root'
- 'Repo root to evaluate (default: parent of this script).'
- '--output'
- 'Where to write the JSON report (default ./'
- '--json'
- 'store_true'
- 'Emit the report JSON on stdout in addition to the file.'
- '--summary-only'
- 'Skip writing the full report file; print verdict only.'
- '--strict'
- 'Exit 1 unless verdict == READY (default policy is the same).'
- 'report'
- 'None'
- '[PAS161] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS161] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS161 — Lead ingestion readiness gate.\n\nDeterministic, non-mutating evaluator for "is the lead-\ningestion subsystem wired correctly, structurally safe, and\nfree of payload-trust regressions?". Walks the repo, confirms\nthe ingestion module files exist, the four webhook routes are\ndeclared, the FastAPI router is wired into ``app/main.py``,\nthe four provider normalizers exist, the contracts module\ncarries the closed-shape doctrine, no forbidden raw-payload\nfield names appear in the executable surfaces, no Memory\nReview file is touched, no vendor / embedding / Supabase /\n.env reads are introduced by this phase\'s own code, and the\ncompanion docs + tests exist.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas161_lead_ingestion_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas161_lead_ingestion_readiness_check.py\n  python scripts/pas161_lead_ingestion_readiness_check.py --json\n  python scripts/pas161_lead_ingestion_readiness_check.py --summary-only\n  python scripts/pas161_lead_ingestion_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  45           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  47           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  48           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('Iterable', 'List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (Iterable)
               STORE_NAME              12 (Iterable)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               POP_TOP

  51           LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               32 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              17 (_stream)

  52           NOP

  53   L2:     LOAD_NAME               17 (_stream)
               LOAD_ATTR               37 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  51   L4:     END_FOR
               POP_ITER

  58           LOAD_NAME                5 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               43 (abspath + NULL|self)

  59           LOAD_NAME                5 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               45 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               40 (path)
               LOAD_ATTR               47 (dirname + NULL|self)
               LOAD_NAME               24 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  58           CALL                     1
               STORE_NAME              25 (_REPO_ROOT_DEFAULT)

  67           LOAD_CONST               9 ('READY')
               STORE_NAME              26 (VERDICT_READY)

  68           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              27 (VERDICT_NOT_READY)

  70           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              28 (SEVERITY_BLOCK)

  71           LOAD_CONST              12 ('INFO')
               STORE_NAME              29 (SEVERITY_INFO)

  78           LOAD_CONST              66 (('app/services/ingestion/__init__.py', 'app/services/ingestion/contracts.py', 'app/services/ingestion/normalizers.py', 'app/services/ingestion/security.py', 'app/services/ingestion/pending_calls.py', 'app/routes/lead_ingestion.py'))
               STORE_NAME              30 (REQUIRED_INGESTION_FILES)

  87           LOAD_CONST              67 (('docs/pas161_lead_ingestion.md',))
               STORE_NAME              31 (REQUIRED_DOCS)

  91           LOAD_CONST              68 (('tests/mvp/test_pas161_lead_ingestion.py',))
               STORE_NAME              32 (REQUIRED_TESTS)

  95           LOAD_CONST              69 (('scripts/proposal_v14_pending_calls.sql',))
               STORE_NAME              33 (REQUIRED_PROPOSAL)

  99           LOAD_CONST              70 (('scripts/combined_supabase_migration.sql',))
               STORE_NAME              34 (OFFLIMITS_FILES)

 107           LOAD_CONST              71 ((('generic', ('@router.post("/generic")',)), ('zapier', ('@router.post("/zapier")',)), ('followupboss', ('@router.post("/followupboss")',)), ('gohighlevel', ('@router.post("/gohighlevel")',))))
               STORE_NAME              35 (REQUIRED_ROUTE_DECLS)

 117           LOAD_CONST              72 (('def normalize_generic_webhook(', 'def normalize_zapier_payload(', 'def normalize_followupboss_payload(', 'def normalize_gohighlevel_payload('))
               STORE_NAME              36 (REQUIRED_NORMALIZERS)

 126           LOAD_CONST              73 (('from app.routes.lead_ingestion import router as lead_ingestion_router', 'app.include_router(lead_ingestion_router, prefix="/webhooks"'))
               STORE_NAME              37 (REQUIRED_MAIN_WIRING)

 135           LOAD_CONST              74 (('raw_payload', 'full_payload', 'transcript', 'raw_transcript', 'full_transcript', 'raw_prompt', 'injected_prompt', 'memory_content', 'messages', 'utterances', 'input_text', 'output_text', 'lineage', 'metadata_blob'))
               STORE_NAME              38 (FORBIDDEN_RAW_FIELDS_IN_EXECUTABLE)

 157           LOAD_CONST              75 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              39 (MEMORY_REVIEW_FILES)

 171           LOAD_CONST              76 (('from app.services.memory', 'import app.services.memory', 'import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               STORE_NAME              40 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 193           LOAD_CONST              13 ('severity')

 195           LOAD_NAME               28 (SEVERITY_BLOCK)

 193           LOAD_CONST              14 ('detail')

 195           LOAD_CONST              15 ('')

 193           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025E30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 193>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3E10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 193>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (_check)

 206           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas161_lead_ingestion_readiness_check.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C18039070, file "scripts/pas161_lead_ingestion_readiness_check.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (_now_iso)

 210           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 210>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053870, file "scripts/pas161_lead_ingestion_readiness_check.py", line 210>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_read_text)

 217           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17ED93D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_strip_python_comments_and_strings)

 261           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas161_lead_ingestion_readiness_check.py", line 261>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C1801C7F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 261>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_files_present)

 276           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 276>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_offlimits_present at 0x0000018C180606F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 276>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_offlimits_present)

 290           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas161_lead_ingestion_readiness_check.py", line 290>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_files_present at 0x0000018C18061110, file "scripts/pas161_lead_ingestion_readiness_check.py", line 290>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_memory_review_files_present)

 307           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas161_lead_ingestion_readiness_check.py", line 307>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_routes_declared at 0x0000018C17E59E70, file "scripts/pas161_lead_ingestion_readiness_check.py", line 307>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_routes_declared)

 334           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 334>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_main_wiring at 0x0000018C17E580E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 334>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_main_wiring)

 359           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 359>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_normalizers_defined at 0x0000018C17D8C830, file "scripts/pas161_lead_ingestion_readiness_check.py", line 359>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_normalizers_defined)

 384           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 384>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_routes_do_not_trust_body_brokerage_id at 0x0000018C17D76780, file "scripts/pas161_lead_ingestion_readiness_check.py", line 384>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_routes_do_not_trust_body_brokerage_id)

 417           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 417>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_forbidden_raw_fields at 0x0000018C17F739B0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 417>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (check_forbidden_raw_fields)

 443           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 443>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_no_forbidden_imports at 0x0000018C17D8AB10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 443>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (check_no_forbidden_imports)

 467           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas161_lead_ingestion_readiness_check.py", line 467>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_normalized_contract_excludes_forbidden at 0x0000018C17D7CC40, file "scripts/pas161_lead_ingestion_readiness_check.py", line 467>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (check_normalized_contract_excludes_forbidden)

 514           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas161_lead_ingestion_readiness_check.py", line 514>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_route_response_shape_excludes_raw at 0x0000018C17ED9FB0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 514>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (check_route_response_shape_excludes_raw)

 573           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas161_lead_ingestion_readiness_check.py", line 573>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object check_docs_required_doctrine at 0x0000018C17D7D230, file "scripts/pas161_lead_ingestion_readiness_check.py", line 573>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (check_docs_required_doctrine)

 628           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas161_lead_ingestion_readiness_check.py", line 628>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object check_self_no_env_or_vendor at 0x0000018C17EDA330, file "scripts/pas161_lead_ingestion_readiness_check.py", line 628>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (check_self_no_env_or_vendor)

 679           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C180FC210, file "scripts/pas161_lead_ingestion_readiness_check.py", line 679>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object _aggregate at 0x0000018C17EC57C0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 679>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_aggregate)

 695           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C180FC120, file "scripts/pas161_lead_ingestion_readiness_check.py", line 695>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _operator_actions at 0x0000018C18048730, file "scripts/pas161_lead_ingestion_readiness_check.py", line 695>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_operator_actions)

 707           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C180FC300, file "scripts/pas161_lead_ingestion_readiness_check.py", line 707>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object evaluate at 0x0000018C17788D70, file "scripts/pas161_lead_ingestion_readiness_check.py", line 707>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (evaluate)

 739           LOAD_CONST              56 ('pas161_lead_ingestion_readiness_report.json')
               STORE_NAME              61 (REPORT_FILENAME)

 742           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C180FC3F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 742>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _build_parser at 0x0000018C1801CBD0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 742>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              62 (_build_parser)

 777           LOAD_CONST              59 (<code object __annotate__ at 0x0000018C180FC4E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 777>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _print_summary at 0x0000018C17D8CD10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 777>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              63 (_print_summary)

 795           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18025130, file "scripts/pas161_lead_ingestion_readiness_check.py", line 795>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _write_report at 0x0000018C179C3C30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 795>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              64 (_write_report)

 809           LOAD_CONST              77 ((None,))
               LOAD_CONST              63 (<code object __annotate__ at 0x0000018C180FC5D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 809>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object main at 0x0000018C17F83070, file "scripts/pas161_lead_ingestion_readiness_check.py", line 809>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              65 (main)

 837           LOAD_NAME               66 (__name__)
               LOAD_CONST              65 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 838           LOAD_NAME                6 (sys)
               LOAD_ATTR              134 (exit)
               PUSH_NULL
               LOAD_NAME               65 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 837   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  54           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  55   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          333 (to L1)

  54   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 193>:
193           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

194           LOAD_CONST               2 ('str')

193           LOAD_CONST               3 ('status')

194           LOAD_CONST               2 ('str')

193           LOAD_CONST               4 ('label')

194           LOAD_CONST               2 ('str')

193           LOAD_CONST               5 ('severity')

195           LOAD_CONST               2 ('str')

193           LOAD_CONST               6 ('detail')

195           LOAD_CONST               2 ('str')

193           LOAD_CONST               7 ('return')

196           LOAD_CONST               8 ('dict')

193           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3E10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 193>:
193           RESUME                   0

198           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

199           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

200           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

201           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

202           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

197           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts/pas161_lead_ingestion_readiness_check.py", line 206>:
206           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C18039070, file "scripts/pas161_lead_ingestion_readiness_check.py", line 206>:
206           RESUME                   0

207           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 210>:
210           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053870, file "scripts/pas161_lead_ingestion_readiness_check.py", line 210>:
 210           RESUME                   0

 211           NOP

 212   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 213           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 214   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 213   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 217>:
217           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17ED93D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 217>:
217            RESUME                   0

222            BUILD_LIST               0
               STORE_FAST               1 (out)

223            LOAD_SMALL_INT           0
               STORE_FAST               2 (i)

224            LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST               3 (n)

225    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

226            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

227            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

228            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

229            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

230            JUMP_FORWARD           240 (to L13)

231    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

232            JUMP_BACKWARD           59 (to L1)

233    L3:     LOAD_FAST_BORROW         0 (src)
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

234    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

235            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

236            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

237            JUMP_FORWARD           138 (to L13)

238    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

239            JUMP_BACKWARD          161 (to L1)

240    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

241            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

242            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

243    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

244            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

245            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

246            JUMP_BACKWARD           30 (to L7)

247    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

248    L9:     JUMP_FORWARD            11 (to L11)

249   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

250   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

251            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

252   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

253            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

254   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts/pas161_lead_ingestion_readiness_check.py", line 261>:
261           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C1801C7F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 261>:
261           RESUME                   0

262           BUILD_LIST               0
              STORE_FAST               1 (out)

263           LOAD_GLOBAL              0 (REQUIRED_INGESTION_FILES)
              LOAD_GLOBAL              2 (REQUIRED_DOCS)
              BINARY_OP                0 (+)
              LOAD_GLOBAL              4 (REQUIRED_TESTS)
              BINARY_OP                0 (+)

264           LOAD_GLOBAL              6 (REQUIRED_PROPOSAL)

263           BINARY_OP                0 (+)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

265           LOAD_GLOBAL              9 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR               11 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

266           LOAD_FAST                1 (out)
              LOAD_ATTR               13 (append + NULL|self)
              LOAD_GLOBAL             15 (_check + NULL)

267           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

268           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

269   L3:     LOAD_CONST               3 ('Required PAS161 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

270           LOAD_GLOBAL             16 (SEVERITY_BLOCK)

271           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

266   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

263   L6:     END_FOR
              POP_ITER

273           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 276>:
276           RESUME                   0
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

Disassembly of <code object check_offlimits_present at 0x0000018C180606F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 276>:
276           RESUME                   0

277           BUILD_LIST               0
              STORE_FAST               1 (out)

278           LOAD_GLOBAL              0 (OFFLIMITS_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

279           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

280           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

281           LOAD_CONST               0 ('offlimits:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

282           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

283   L3:     LOAD_CONST               3 ('Off-limits file present (do not modify): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

284           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

285           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — restore from git history')

280   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

278   L6:     END_FOR
              POP_ITER

287           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts/pas161_lead_ingestion_readiness_check.py", line 290>:
290           RESUME                   0
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

Disassembly of <code object check_memory_review_files_present at 0x0000018C18061110, file "scripts/pas161_lead_ingestion_readiness_check.py", line 290>:
290           RESUME                   0

294           BUILD_LIST               0
              STORE_FAST               1 (out)

295           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

296           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

297           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

298           LOAD_CONST               1 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

299           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               3 ('FAIL')

300   L3:     LOAD_CONST               4 ('Memory Review file present (PAS161 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

301           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

302           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               5 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               6 ('PAS161 must not delete Memory Review files')

297   L5:     LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

295   L6:     END_FOR
              POP_ITER

304           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts/pas161_lead_ingestion_readiness_check.py", line 307>:
307           RESUME                   0
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

Disassembly of <code object check_routes_declared at 0x0000018C17E59E70, file "scripts/pas161_lead_ingestion_readiness_check.py", line 307>:
  --            MAKE_CELL                6 (src)

 307            RESUME                   0

 308            BUILD_LIST               0
                STORE_FAST               1 (out)

 309            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('lead_ingestion.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (routes_path)

 310            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (routes_path)
                CALL                     1
                STORE_DEREF              6 (src)

 311            LOAD_DEREF               6 (src)
                POP_JUMP_IF_NOT_NONE    38 (to L1)
                NOT_TAKEN

 312            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 313            LOAD_CONST               3 ('routes:source_missing')

 314            LOAD_CONST               4 ('FAIL')

 315            LOAD_CONST               5 ('lead_ingestion.py is missing')

 316            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 317            LOAD_CONST               6 ('cannot verify routes')

 312            LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 319            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 320    L1:     LOAD_GLOBAL             10 (REQUIRED_ROUTE_DECLS)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   52 (logical, decls)

 321            LOAD_GLOBAL             12 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         6 (src)
                BUILD_TUPLE              1
                LOAD_CONST               8 (<code object <genexpr> at 0x0000018C18025A30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 321>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         4 (decls)
                GET_ITER
                CALL                     0
        L3:     FOR_ITER                12 (to L5)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L4:     POP_ITER
                LOAD_CONST               9 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST              10 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW         6 (src)
                BUILD_TUPLE              1
                LOAD_CONST               8 (<code object <genexpr> at 0x0000018C18025A30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 321>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         4 (decls)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               5 (ok)

 322            LOAD_FAST                1 (out)
                LOAD_ATTR                5 (append + NULL|self)
                LOAD_GLOBAL              7 (_check + NULL)

 323            LOAD_CONST              11 ('route:')
                LOAD_FAST_BORROW         3 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 324            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST              12 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               4 ('FAIL')

 325    L9:     LOAD_CONST              13 ('Webhook route declared: ')
                LOAD_FAST_BORROW         3 (logical)
                FORMAT_SIMPLE
                BUILD_STRING             2

 326            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

 327            LOAD_FAST_BORROW         5 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST              14 ('')
                JUMP_FORWARD            23 (to L11)

 328   L10:     LOAD_CONST              15 ('none of accepted declarations present: ')
                LOAD_CONST              16 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         4 (decls)
                CALL                     1
                BINARY_OP                0 (+)

 322   L11:     LOAD_CONST               7 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 320   L12:     END_FOR
                POP_ITER

 331            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025A30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 321>:
  --           COPY_FREE_VARS           1

 321           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (d, d)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 334>:
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

Disassembly of <code object check_main_wiring at 0x0000018C17E580E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 334>:
334           RESUME                   0

335           BUILD_LIST               0
              STORE_FAST               1 (out)

336           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('app')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('main.py')
              BINARY_OP               11 (/)
              STORE_FAST               2 (main_path)

337           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (main_path)
              CALL                     1
              STORE_FAST               3 (src)

338           LOAD_FAST_BORROW         3 (src)
              POP_JUMP_IF_NOT_NONE    38 (to L1)
              NOT_TAKEN

339           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

340           LOAD_CONST               2 ('main:source_missing')

341           LOAD_CONST               3 ('FAIL')

342           LOAD_CONST               4 ('app/main.py is missing')

343           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

344           LOAD_CONST               5 ('cannot verify router wiring')

339           LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP

346           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

347   L1:     LOAD_GLOBAL             10 (REQUIRED_MAIN_WIRING)
              GET_ITER
      L2:     FOR_ITER                75 (to L7)
              STORE_FAST               4 (needle)

348           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

349           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

350           LOAD_CONST               7 ('main:')
              LOAD_FAST_BORROW         4 (needle)
              LOAD_CONST               8 (slice(None, 60, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

351           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               9 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               3 ('FAIL')

352   L4:     LOAD_CONST              10 ('app/main.py wires the lead ingestion router')

353           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

354           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST              11 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              12 ('missing literal: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

349   L6:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           77 (to L2)

347   L7:     END_FOR
              POP_ITER

356           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 359>:
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

Disassembly of <code object check_normalizers_defined at 0x0000018C17D8C830, file "scripts/pas161_lead_ingestion_readiness_check.py", line 359>:
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

362           LOAD_CONST               3 ('normalizers.py')

361           BINARY_OP               11 (/)
              STORE_FAST               2 (norm_path)

363           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (norm_path)
              CALL                     1
              STORE_FAST               3 (src)

364           LOAD_FAST_BORROW         3 (src)
              POP_JUMP_IF_NOT_NONE    37 (to L1)
              NOT_TAKEN

365           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

366           LOAD_CONST               4 ('normalizers:source_missing')

367           LOAD_CONST               5 ('FAIL')

368           LOAD_CONST               6 ('normalizers.py is missing')

369           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

365           LOAD_CONST               7 (('severity',))
              CALL_KW                  4
              CALL                     1
              POP_TOP

371           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

372   L1:     LOAD_GLOBAL             10 (REQUIRED_NORMALIZERS)
              GET_ITER
      L2:     FOR_ITER                92 (to L7)
              STORE_FAST               4 (needle)

373           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

374           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

375           LOAD_CONST               8 ('normalizer:')
              LOAD_FAST_BORROW         4 (needle)
              LOAD_CONST               9 (slice(None, 40, None))
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              BUILD_STRING             2

376           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST              10 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

377   L4:     LOAD_CONST              11 ('Normalizer defined: ')
              LOAD_FAST_BORROW         4 (needle)
              LOAD_ATTR               13 (strip + NULL|self)
              CALL                     0
              FORMAT_SIMPLE
              BUILD_STRING             2

378           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

379           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST              12 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_CONST              13 ('missing def: ')
              LOAD_FAST_BORROW         4 (needle)
              FORMAT_SIMPLE
              BUILD_STRING             2

374   L6:     LOAD_CONST              14 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           94 (to L2)

372   L7:     END_FOR
              POP_ITER

381           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 384>:
384           RESUME                   0
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

Disassembly of <code object check_routes_do_not_trust_body_brokerage_id at 0x0000018C17D76780, file "scripts/pas161_lead_ingestion_readiness_check.py", line 384>:
 384            RESUME                   0

 389            BUILD_LIST               0
                STORE_FAST               1 (out)

 390            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('routes')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('lead_ingestion.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (routes_path)

 391            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (routes_path)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               4 ('')
        L1:     STORE_FAST               3 (src)

 392            LOAD_GLOBAL              5 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               4 (executable)

 394            LOAD_CONST              12 (("body['brokerage_id']", 'body["brokerage_id"]', 'body.get(brokerage_id', 'payload.brokerage_id', 'LeadPayload('))
                STORE_FAST               5 (forbidden)

 405            LOAD_FAST_BORROW         5 (forbidden)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (t)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST   102 (t, t)
                LOAD_FAST_BORROW         4 (executable)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         6 (t)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               7 (bad)
                STORE_FAST               6 (t)

 406            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 407            LOAD_CONST               5 ('routes:no_body_brokerage_id_trust')

 408            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               6 ('FAIL')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               7 ('PASS')

 409    L9:     LOAD_CONST               8 ('Webhook routes do not read brokerage_id from the body')

 410            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 412            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN

 411            LOAD_CONST               9 ('forbidden patterns in executable: ')
                LOAD_CONST              10 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 412   L10:     LOAD_CONST               4 ('')

 406   L11:     LOAD_CONST              11 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 414            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 405            SWAP                     2
                STORE_FAST               6 (t)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 417>:
417           RESUME                   0
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

Disassembly of <code object check_forbidden_raw_fields at 0x0000018C17F739B0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 417>:
 417            RESUME                   0

 420            BUILD_LIST               0
                STORE_FAST               1 (out)

 423            LOAD_GLOBAL              0 (REQUIRED_INGESTION_FILES)
                GET_ITER

 421            LOAD_FAST_AND_CLEAR      2 (p)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 423    L2:     FOR_ITER                21 (to L3)
                STORE_FAST               2 (p)

 422            LOAD_GLOBAL              3 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_FAST_BORROW         2 (p)
                BINARY_OP               11 (/)
                LIST_APPEND              2
                JUMP_BACKWARD           23 (to L2)

 423    L3:     END_FOR
                POP_ITER

 421    L4:     STORE_FAST               3 (paths)
                STORE_FAST               2 (p)

 425            LOAD_FAST_BORROW         3 (paths)
                GET_ITER
        L5:     FOR_ITER               167 (to L17)
                STORE_FAST               4 (path)

 426            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         4 (path)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 ('')
        L6:     STORE_FAST               5 (src)

 427            LOAD_GLOBAL              7 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         5 (src)
                CALL                     1
                STORE_FAST               6 (executable)

 429            LOAD_GLOBAL              8 (FORBIDDEN_RAW_FIELDS_IN_EXECUTABLE)
                GET_ITER

 428            LOAD_FAST_AND_CLEAR      7 (f)
                SWAP                     2
        L7:     BUILD_LIST               0
                SWAP                     2

 429    L8:     FOR_ITER                13 (to L11)
                STORE_FAST               7 (f)

 430            LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (f, executable)
                CONTAINS_OP              0 (in)

 429    L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)
       L10:     LOAD_FAST_BORROW         7 (f)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L8)
       L11:     END_FOR
                POP_ITER

 428   L12:     STORE_FAST               8 (bad)
                STORE_FAST               7 (f)

 432            LOAD_FAST                1 (out)
                LOAD_ATTR               11 (append + NULL|self)
                LOAD_GLOBAL             13 (_check + NULL)

 433            LOAD_CONST               2 ('forbidden_field:')
                LOAD_FAST_BORROW         4 (path)
                LOAD_ATTR               14 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 434            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
                NOT_TAKEN
                LOAD_CONST               3 ('FAIL')
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_CONST               4 ('PASS')

 435   L14:     LOAD_CONST               5 ('No forbidden raw-payload fields in executable: ')
                LOAD_FAST_BORROW         4 (path)
                LOAD_ATTR               14 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 436            LOAD_GLOBAL             16 (SEVERITY_BLOCK)

 438            LOAD_FAST_BORROW         8 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L15)
                NOT_TAKEN

 437            LOAD_CONST               6 ('forbidden field tokens in executable: ')
                LOAD_CONST               7 (', ')
                LOAD_ATTR               19 (join + NULL|self)
                LOAD_FAST_BORROW         8 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L16)

 438   L15:     LOAD_CONST               1 ('')

 432   L16:     LOAD_CONST               8 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          169 (to L5)

 425   L17:     END_FOR
                POP_ITER

 440            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L18:     SWAP                     2
                POP_TOP

 421            SWAP                     2
                STORE_FAST               2 (p)
                RERAISE                  0

  --   L19:     SWAP                     2
                POP_TOP

 428            SWAP                     2
                STORE_FAST               7 (f)
                RERAISE                  0
ExceptionTable:
  L1 to L4 -> L18 [2]
  L7 to L9 -> L19 [3]
  L10 to L12 -> L19 [3]

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 443>:
443           RESUME                   0
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8AB10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 443>:
443            RESUME                   0

446            BUILD_LIST               0
               STORE_FAST               1 (out)

447            LOAD_GLOBAL              0 (REQUIRED_INGESTION_FILES)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               2 (p)

448            LOAD_GLOBAL              3 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         2 (p)
               BINARY_OP               11 (/)
               STORE_FAST               3 (path)

449            LOAD_GLOBAL              5 (_read_text + NULL)
               LOAD_FAST_BORROW         3 (path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               4 (src)

450            BUILD_LIST               0
               STORE_FAST               5 (bad)

451            LOAD_FAST_BORROW         4 (src)
               LOAD_ATTR                7 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               6 (line)

452            LOAD_FAST_BORROW         6 (line)
               LOAD_ATTR                9 (strip + NULL|self)
               CALL                     0
               STORE_FAST               7 (stripped)

453            LOAD_GLOBAL             10 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               8 (prefix)

454            LOAD_FAST_BORROW         7 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_FAST_BORROW         8 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

455    L5:     LOAD_FAST_BORROW         5 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_FAST_BORROW         8 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

453    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

451    L7:     END_FOR
               POP_ITER

456            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             17 (_check + NULL)

457            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         3 (path)
               LOAD_ATTR               18 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

458            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

459    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         3 (path)
               LOAD_ATTR               18 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

460            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

462            LOAD_FAST_BORROW         5 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

461            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         5 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

462   L10:     LOAD_CONST               1 ('')

456   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

447   L12:     END_FOR
               POP_ITER

464            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts/pas161_lead_ingestion_readiness_check.py", line 467>:
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

Disassembly of <code object check_normalized_contract_excludes_forbidden at 0x0000018C17D7CC40, file "scripts/pas161_lead_ingestion_readiness_check.py", line 467>:
 467            RESUME                   0

 472            BUILD_LIST               0
                STORE_FAST               1 (out)

 473            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('app')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('services')
                BINARY_OP               11 (/)
                LOAD_CONST               3 ('ingestion')
                BINARY_OP               11 (/)
                LOAD_CONST               4 ('contracts.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (contracts)

 474            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (contracts)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('')
        L1:     STORE_FAST               3 (src)

 477            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (find + NULL|self)
                LOAD_CONST               6 ('class NormalizedLead')
                CALL                     1
                STORE_FAST               4 (start)

 478            LOAD_FAST_BORROW         4 (start)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       37 (to L2)
                NOT_TAKEN

 479            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 480            LOAD_CONST               7 ('contract:class_missing')

 481            LOAD_CONST               8 ('FAIL')

 482            LOAD_CONST               9 ('NormalizedLead class not found')

 483            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 479            LOAD_CONST              10 (('severity',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 485            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 486    L2:     LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (find + NULL|self)
                LOAD_CONST              11 ('\ndef ')
                LOAD_FAST_BORROW         4 (start)
                CALL                     2
                STORE_FAST               5 (end)

 487            LOAD_FAST_BORROW         5 (end)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       12 (to L3)
                NOT_TAKEN

 488            LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         3 (src)
                CALL                     1
                STORE_FAST               5 (end)

 489    L3:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (src, start)
                LOAD_FAST_BORROW         5 (end)
                BINARY_SLICE
                STORE_FAST               6 (body)

 490            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
                LOAD_FAST_BORROW         6 (body)
                CALL                     1
                STORE_FAST               7 (executable)

 491            LOAD_CONST              18 (('raw_payload', 'full_payload', 'transcript:', 'raw_transcript', 'evidence:', 'lineage:', 'memory_content', 'raw_prompt', 'injected_prompt'))
                STORE_FAST               8 (forbidden_field_decls)

 502            LOAD_FAST_BORROW         8 (forbidden_field_decls)
                GET_ITER
                LOAD_FAST_AND_CLEAR      9 (f)
                SWAP                     2
        L4:     BUILD_LIST               0
                SWAP                     2
        L5:     FOR_ITER                13 (to L8)
                STORE_FAST_LOAD_FAST   153 (f, f)
                LOAD_FAST_BORROW         7 (executable)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L7:     LOAD_FAST_BORROW         9 (f)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L5)
        L8:     END_FOR
                POP_ITER
        L9:     STORE_FAST              10 (bad)
                STORE_FAST               9 (f)

 503            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 504            LOAD_CONST              12 ('contract:no_forbidden_fields')

 505            LOAD_FAST_BORROW        10 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L10)
                NOT_TAKEN
                LOAD_CONST               8 ('FAIL')
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST              13 ('PASS')

 506   L11:     LOAD_CONST              14 ('NormalizedLead has no forbidden raw-payload fields')

 507            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 509            LOAD_FAST_BORROW        10 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L12)
                NOT_TAKEN

 508            LOAD_CONST              15 ('forbidden field identifiers in class body: ')
                LOAD_CONST              16 (', ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW        10 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L13)

 509   L12:     LOAD_CONST               5 ('')

 503   L13:     LOAD_CONST              17 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 511            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L14:     SWAP                     2
                POP_TOP

 502            SWAP                     2
                STORE_FAST               9 (f)
                RERAISE                  0
ExceptionTable:
  L4 to L6 -> L14 [2]
  L7 to L9 -> L14 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts/pas161_lead_ingestion_readiness_check.py", line 514>:
514           RESUME                   0
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

Disassembly of <code object check_route_response_shape_excludes_raw at 0x0000018C17ED9FB0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 514>:
514            RESUME                   0

518            BUILD_LIST               0
               STORE_FAST               1 (out)

519            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               1 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('routes')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('lead_ingestion.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (routes)

520            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (routes)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

522            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (find + NULL|self)
               LOAD_CONST               5 ('def _ingest(')
               CALL                     1
               STORE_FAST               4 (idx)

523            LOAD_FAST_BORROW         4 (idx)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       37 (to L2)
               NOT_TAKEN

524            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

525            LOAD_CONST               6 ('route_response:no_ingest_fn')

526            LOAD_CONST               7 ('FAIL')

527            LOAD_CONST               8 ('_ingest helper not found in lead_ingestion.py')

528            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

524            LOAD_CONST               9 (('severity',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

530            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

532    L2:     LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                5 (find + NULL|self)
               LOAD_CONST              10 ('\ndef ')
               LOAD_FAST_BORROW         4 (idx)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               5 (next_def)

533            LOAD_FAST_LOAD_FAST     52 (src, idx)
               LOAD_FAST_BORROW         5 (next_def)
               LOAD_SMALL_INT           0
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_FAST                5 (next_def)
               JUMP_FORWARD            10 (to L4)
       L3:     LOAD_GLOBAL             13 (len + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
       L4:     BINARY_SLICE
               STORE_FAST               6 (fn_body)

534            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         6 (fn_body)
               CALL                     1
               STORE_FAST               7 (executable)

540            LOAD_CONST              21 (('raw_payload', 'full_payload', 'transcript', 'memory_content', 'raw_prompt', 'evidence'))
               GET_ITER
       L5:     FOR_ITER                58 (to L7)
               STORE_FAST               8 (forbidden)

542            LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (forbidden, executable)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L5)

543    L6:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

544            LOAD_CONST              11 ('route_response:forbidden:')
               LOAD_FAST_BORROW         8 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

545            LOAD_CONST               7 ('FAIL')

546            LOAD_CONST              12 ('Route response must not include ')
               LOAD_FAST_BORROW         8 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

547            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

548            LOAD_CONST              13 ('found ')
               LOAD_FAST_BORROW         8 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              14 (' in _ingest body executable')
               BUILD_STRING             3

543            LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           60 (to L5)

540    L7:     END_FOR
               POP_ITER

551            LOAD_CONST              22 (('status', 'source', 'brokerage_id', 'lead_id', 'call_queued', 'warnings'))
               GET_ITER
       L8:     FOR_ITER                58 (to L10)
               STORE_FAST               9 (required)

553            LOAD_FAST_BORROW_LOAD_FAST_BORROW 150 (required, fn_body)
               CONTAINS_OP              0 (in)
               STORE_FAST              10 (present)

554            LOAD_FAST_BORROW        10 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           17 (to L8)

555    L9:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

556            LOAD_CONST              16 ('route_response:missing_key:')
               LOAD_FAST_BORROW         9 (required)
               FORMAT_SIMPLE
               BUILD_STRING             2

557            LOAD_CONST               7 ('FAIL')

558            LOAD_CONST              17 ('Route response must include key ')
               LOAD_FAST_BORROW         9 (required)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

559            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

555            LOAD_CONST               9 (('severity',))
               CALL_KW                  4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           60 (to L8)

551   L10:     END_FOR
               POP_ITER

563            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

564            LOAD_CONST              18 ('route_response:shape_ok')

565            LOAD_CONST              19 ('PASS')

566            LOAD_CONST              20 ('Route response shape includes closed allow-list and excludes raw payload keys')

568            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

563            LOAD_CONST               9 (('severity',))
               CALL_KW                  4
               CALL                     1
               POP_TOP

570            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts/pas161_lead_ingestion_readiness_check.py", line 573>:
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17D7D230, file "scripts/pas161_lead_ingestion_readiness_check.py", line 573>:
  --            MAKE_CELL                8 (lower)

 573            RESUME                   0

 574            BUILD_LIST               0
                STORE_FAST               1 (out)

 575            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_GLOBAL              2 (REQUIRED_DOCS)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 576            LOAD_GLOBAL              5 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                STORE_FAST               3 (src)

 577            LOAD_FAST_BORROW         3 (src)
                POP_JUMP_IF_NOT_NONE    51 (to L1)
                NOT_TAKEN

 578            LOAD_FAST_BORROW         1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 579            LOAD_CONST               1 ('docs:missing')

 580            LOAD_CONST               2 ('FAIL')

 581            LOAD_CONST               3 ('PAS161 doc missing: ')
                LOAD_GLOBAL              2 (REQUIRED_DOCS)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             2

 582            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 578            LOAD_CONST               4 (('severity',))
                CALL_KW                  4
                CALL                     1
                POP_TOP

 584            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

 585    L1:     LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR               13 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 586            LOAD_CONST              15 ((('auth-model', ('x-api-key', 'require_brokerage')), ('tenant-isolation', ('brokerage_id from', 'never trust brokerage_id', 'brokerage_id is not accepted', 'brokerage_id is never')), ('no-raw-payload', ('no raw payload logging', 'raw payload', 'no raw_payload')), ('phone-required', ('phone required', 'phone is required', 'missing_phone')), ('pending-call-durability', ('process-local', 'pending_calls_store_is_process_local', 'durability')), ('unblocks-pas163', ('unblocks pas163', 'pas163', 'candidate generation'))))
                STORE_FAST               4 (required_phrases)

 615            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 616            LOAD_GLOBAL             14 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18026530, file "scripts/pas161_lead_ingestion_readiness_check.py", line 616>)
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
                LOAD_CONST               6 (True)
                JUMP_FORWARD            20 (to L7)
        L5:     END_FOR
                POP_ITER
                LOAD_CONST               7 (False)
                JUMP_FORWARD            16 (to L7)
        L6:     PUSH_NULL
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               5 (<code object <genexpr> at 0x0000018C18026530, file "scripts/pas161_lead_ingestion_readiness_check.py", line 616>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 617            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 618            LOAD_CONST               8 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 619            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               9 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               2 ('FAIL')

 620    L9:     LOAD_CONST              10 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 621            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 623            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 622            LOAD_CONST              11 ('expected one of: ')
                LOAD_CONST              12 (' | ')
                LOAD_ATTR               17 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 623   L10:     LOAD_CONST              13 ('')

 617   L11:     LOAD_CONST              14 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 615   L12:     END_FOR
                POP_ITER

 625            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026530, file "scripts/pas161_lead_ingestion_readiness_check.py", line 616>:
  --           COPY_FREE_VARS           1

 616           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts/pas161_lead_ingestion_readiness_check.py", line 628>:
628           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17EDA330, file "scripts/pas161_lead_ingestion_readiness_check.py", line 628>:
628            RESUME                   0

632            BUILD_LIST               0
               STORE_FAST               1 (out)

633            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

634            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L1:     STORE_FAST               3 (src)

635            BUILD_LIST               0
               STORE_FAST               4 (bad)

636            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

637            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

638            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               2 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

639            JUMP_BACKWARD           45 (to L2)

640    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

641            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('dotenv import')
               CALL                     1
               POP_TOP

642    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

643            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('supabase import')
               CALL                     1
               POP_TOP

644    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

650            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('external-vendor import')
               CALL                     1
               POP_TOP

651    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

657            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               6 ('embedding / vector import')
               CALL                     1
               POP_TOP

658    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               7 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

659            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               7 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

660    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('load_dotenv() call')
               CALL                     1
               POP_TOP

661    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              21 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

662   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               9 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

636   L11:     END_FOR
               POP_ITER

663            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

664            LOAD_CONST              10 ('self_check:no_env_or_vendor')

665            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              11 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              12 ('PASS')

666   L13:     LOAD_CONST              13 ('PAS161 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs')

668            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

670            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

669            LOAD_CONST              14 ('disqualifying code-line patterns: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

670   L14:     LOAD_CONST               1 ('')

663   L15:     LOAD_CONST              16 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

672            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC210, file "scripts/pas161_lead_ingestion_readiness_check.py", line 679>:
679           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC57C0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 679>:
 679            RESUME                   0

 681            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 680            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 681    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 682            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 681    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 682    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 681    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 680    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 685            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 684            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 685   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 686            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 685   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 686   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 685   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 684   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 689            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 690   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 691            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 688            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 680            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 684            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C180FC120, file "scripts/pas161_lead_ingestion_readiness_check.py", line 695>:
695           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C18048730, file "scripts/pas161_lead_ingestion_readiness_check.py", line 695>:
695           RESUME                   0

696           BUILD_LIST               0
              STORE_FAST               1 (out)

697           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

698           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

699           JUMP_BACKWARD           19 (to L1)

700   L2:     LOAD_FAST_BORROW         2 (c)
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

701           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)

702           LOAD_CONST               3 ('[')
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

701           CALL                     1
              POP_TOP
              JUMP_BACKWARD          111 (to L1)

697   L5:     END_FOR
              POP_ITER

704           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC300, file "scripts/pas161_lead_ingestion_readiness_check.py", line 707>:
707           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17788D70, file "scripts/pas161_lead_ingestion_readiness_check.py", line 707>:
707           RESUME                   0

708           BUILD_LIST               0
              STORE_FAST               1 (checks)

709           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

710           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_offlimits_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

711           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

712           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_routes_declared + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

713           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_main_wiring + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

714           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_normalizers_defined + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

715           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_routes_do_not_trust_body_brokerage_id + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

716           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_forbidden_raw_fields + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

717           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

718           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_normalized_contract_excludes_forbidden + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

719           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_route_response_shape_excludes_raw + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

720           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             25 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

721           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             27 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

723           LOAD_GLOBAL             29 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

725           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS161')

726           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             31 (_now_iso + NULL)
              CALL                     0

727           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

728           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             32 (VERDICT_READY)
              COMPARE_OP              72 (==)

729           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             35 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

730           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             35 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

731           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             35 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

732           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             37 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053AB0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 732>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

733           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             37 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 733>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

734           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

735           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             39 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

724           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053AB0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 732>:
 732           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 733>:
 733           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC3F0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 742>:
742           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CBD0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 742>:
742           RESUME                   0

743           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

744           LOAD_CONST               0 ('pas161_lead_ingestion_readiness_check')

746           LOAD_CONST               1 ('PAS161 — Evaluate the lead-ingestion subsystem for structural correctness and doctrine compliance. Read-only. Does not touch Supabase, .env, or any tenant data.')

743           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

752           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

753           LOAD_CONST               3 ('--repo-root')

754           LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

755           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

752           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

757           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

758           LOAD_CONST               6 ('--output')

759           LOAD_GLOBAL              8 (REPORT_FILENAME)

760           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

757           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

762           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

763           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

764           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

762           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

766           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

767           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

768           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

766           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

770           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

771           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

772           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

770           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

774           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC4E0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 777>:
777           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "scripts/pas161_lead_ingestion_readiness_check.py", line 777>:
777           RESUME                   0

778           LOAD_GLOBAL              1 (print + NULL)

779           LOAD_CONST               0 ('[PAS161] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

780           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

781           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

782           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

783           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

784           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

779           BUILD_STRING            12

778           CALL                     1
              POP_TOP

786           LOAD_FAST_BORROW         0 (report)
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

787           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

788           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS161] operator actions:')
              CALL                     1
              POP_TOP

789           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

790           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

789   L3:     END_FOR
              POP_ITER

791           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

792           LOAD_GLOBAL              1 (print + NULL)
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

791   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

787   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts/pas161_lead_ingestion_readiness_check.py", line 795>:
795           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C179C3C30, file "scripts/pas161_lead_ingestion_readiness_check.py", line 795>:
 795           RESUME                   0

 796           NOP

 797   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 798           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 799           LOAD_CONST               3 ('utf-8')

 797           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 801           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 802   L4:     LOAD_GLOBAL             11 (print + NULL)

 803           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 804           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 803           BUILD_STRING             4

 805           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 802           LOAD_CONST               7 (('file',))
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

 801   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC5D0, file "scripts/pas161_lead_ingestion_readiness_check.py", line 809>:
809           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F83070, file "scripts/pas161_lead_ingestion_readiness_check.py", line 809>:
 809            RESUME                   0

 810            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 811            NOP

 812    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 816    L2:     LOAD_GLOBAL             10 (os)
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

 817            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 818            LOAD_GLOBAL             23 (print + NULL)

 819            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 820            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 818            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 822            LOAD_SMALL_INT           2
                RETURN_VALUE

 824    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 826            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 827            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 829    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 831            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 832            LOAD_GLOBAL             23 (print + NULL)
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

 834    L6:     LOAD_FAST                5 (report)
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

 813            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 814    L9:     LOAD_FAST                3 (e)
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

 813   L17:     RERAISE                  0

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
