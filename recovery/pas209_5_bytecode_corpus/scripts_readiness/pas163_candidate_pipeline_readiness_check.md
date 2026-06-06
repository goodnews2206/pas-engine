# scripts_readiness/pas163_candidate_pipeline_readiness_check

- **pyc:** `scripts\__pycache__\pas163_candidate_pipeline_readiness_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas163_candidate_pipeline_readiness_check.py`
- **co_filename (from bytecode):** `scripts\pas163_candidate_pipeline_readiness_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS163 — Outbound dial + memory candidate pipeline readiness gate.

Deterministic, non-mutating evaluator for "is the outbound dial
adapter wired, the memory candidate pipeline structurally safe,
and Memory Review hooked to a real input source?".

Walks the repo and verifies:
  * outbound/dial.py exists and defines ``place_outbound_call``;
  * the adapter never uses ``http://localhost/outbound/call``;
  * the adapter never returns a fake / hard-coded call_sid token;
  * the worker resolves ``place_outbound_call`` via its resolver,
    marks DIALED on adapter ``status="ok"``, and marks FAILED on
    adapter ``status="failed"``;
  * the worker remains OFF by default
    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` unchanged);
  * the candidate pipeline exposes the three required functions
    and rejects calls without ``brokerage_id``;
  * the pipeline filters DANGEROUS / EPHEMERAL kinds and never
    emits APPROVED status directly;
  * neither the pipeline nor the demo seed touches raw payload /
    raw transcript / vector / embedding / external vendor code;
  * the PAS162 / PAS161 / PAS160 readiness checkers still exist;
  * no Memory Review UI file is deleted or modified by PAS163.

Emits a verdict (READY / NOT_READY) plus a machine-readable
``pas163_candidate_pipeline_readiness_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * imports external vendors,
  * imports embedding / vector libraries.

Usage:
  python scripts/pas163_candidate_pipeline_readiness_check.py
  python scripts/pas163_candidate_pipeline_readiness_check.py --json
  python scripts/pas163_candidate_pipeline_readiness_check.py --summary-only
  python scripts/pas163_candidate_pipeline_readiness_check.py --strict

Exit codes:
    0  — READY  (verdict == READY)
    1  — NOT_READY
    2  — bad CLI arguments
```

## Imports

`List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_strip_python_comments_and_strings`, `_write_report`, `check_candidate_pipeline`, `check_dial_adapter`, `check_docs_required_doctrine`, `check_event_contract_registration`, `check_files_present`, `check_memory_review_intact`, `check_no_forbidden_imports`, `check_prior_phases_intact`, `check_seed_script`, `check_self_no_env_or_vendor`, `check_worker_wiring`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS163`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS163 — Outbound dial + memory candidate pipeline readiness gate.\n\nDeterministic, non-mutating evaluator for "is the outbound dial\nadapter wired, the memory candidate pipeline structurally safe,\nand Memory Review hooked to a real input source?".\n\nWalks the repo and verifies:\n  * outbound/dial.py exists and defines ``place_outbound_call``;\n  * the adapter never uses ``http://localhost/outbound/call``;\n  * the adapter never returns a fake / hard-coded call_sid token;\n  * the worker resolves ``place_outbound_call`` via its resolver,\n    marks DIALED on adapter ``status="ok"``, and marks FAILED on\n    adapter ``status="failed"``;\n  * the worker remains OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` unchanged);\n  * the candidate pipeline exposes the three required functions\n    and rejects calls without ``brokerage_id``;\n  * the pipeline filters DANGEROUS / EPHEMERAL kinds and never\n    emits APPROVED status directly;\n  * neither the pipeline nor the demo seed touches raw payload /\n    raw transcript / vector / embedding / external vendor code;\n  * the PAS162 / PAS161 / PAS160 readiness checkers still exist;\n  * no Memory Review UI file is deleted or modified by PAS163.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas163_candidate_pipeline_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries.\n\nUsage:\n  python scripts/pas163_candidate_pipeline_readiness_check.py\n  python scripts/pas163_candidate_pipeline_readiness_check.py --json\n  python scripts/pas163_candidate_pipeline_readiness_check.py --summary-only\n  python scripts/pas163_candidate_pipeline_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'severity'
- 'detail'
- 'pas163_candidate_pipeline_readiness_report.json'
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
- 'Required PAS163 file present: '
- 'missing'
- 'prior_phase:'
- 'Prior-phase readiness script intact: '
- 'missing — PAS163 must not delete'
- 'memory_review_file:'
- 'Memory Review file present (PAS163 must not delete): '
- 'PAS163 must not delete Memory Review files'
- 'app'
- 'services'
- 'outbound'
- 'dial.py'
- 'dial_fn:'
- 'Dial function present: '
- 'missing def: '
- 'dial:no_forbidden:'
- 'Dial adapter excludes pattern: '
- 'pattern '
- ' present in executable'
- '.startswith("+")'
- ".startswith('+')"
- 'dial:phone_guard'
- 'Dial adapter validates E.164 phone format'
- "missing '+' guard in dial adapter"
- 'ingestion'
- 'worker.py'
- 'worker_fn:'
- 'Worker function present: '
- 'from app.services.outbound.dial import place_outbound_call'
- 'worker:imports_dial_adapter'
- 'Worker resolver imports place_outbound_call'
- "missing 'from app.services.outbound.dial import place_outbound_call'"
- 'adapter_status == "ok"'
- "adapter_status == 'ok'"
- 'worker:dialed_on_ok'
- "Worker marks DIALED on adapter status='ok'"
- 'missing \'adapter_status == "ok"\' branch'
- 'outbound_dial_adapter_missing'
- 'worker:failed_on_adapter_missing'
- 'Worker marks FAILED with outbound_dial_adapter_missing'
- "missing 'outbound_dial_adapter_missing' branch"
- '_ENV_FLAG_ENABLED_LITERAL = "true"'
- "_ENV_FLAG_ENABLED_LITERAL = 'true'"
- 'worker:off_by_default'
- 'Worker remains OFF by default (strict enable literal)'
- 'enable literal constant not found'
- 'memory'
- 'candidate_pipeline.py'
- 'pipeline_fn:'
- 'Pipeline function present: '
- 'classify_memory_candidate'
- 'pipeline:reuses_classifier'
- 'Pipeline reuses classify_memory_candidate'
- 'classifier reference not found'
- 'MemoryKind.DANGEROUS'
- 'MemoryKind.EPHEMERAL'
- 'pipeline:filters_dangerous_ephemeral'
- 'Pipeline source filters DANGEROUS and EPHEMERAL kinds'
- 'expected references to MemoryKind.DANGEROUS and MemoryKind.EPHEMERAL'
- 'MemoryStatus.CANDIDATE'
- 'pipeline:candidate_only'
- 'Pipeline forces MemoryStatus.CANDIDATE on every record'
- 'expected MemoryStatus.CANDIDATE reference'
- 'MemoryStatus.APPROVED'
- 'approve_memory'
- 'pipeline:no_auto_approve'
- 'Pipeline never sets MemoryStatus.APPROVED'
- 'APPROVED status / approve_memory present in executable'
- 'missing_brokerage_id'
- 'pipeline:requires_brokerage_id'
- 'Pipeline rejects calls without brokerage_id'
- 'missing_brokerage_id token not found'
- 'pipeline:no_forbidden:'
- 'Pipeline excludes forbidden field '
- 'forbidden field '
- ' in executable'
- 'scripts'
- 'seed_memory_candidate_demo.py'
- 'seed:cli_flag:'
- 'Seed CLI exposes flag '
- 'missing CLI flag '
- 'generate_memory_candidates_from_replay'
- 'seed:uses_pipeline'
- 'Seed invokes generate_memory_candidates_from_replay'
- 'pipeline reference not found'
- 'app/services/outbound/dial.py'
- 'forbidden_import:'
- 'No forbidden imports: '
- 'forbidden import prefixes: '
- 'events'
- 'contract.py'
- 'events:'
- 'Event contract registers '
- 'missing event type '
- 'docs'
- 'pas163_outbound_dial_and_candidate_pipeline.md'
- 'docs:phrase:'
- 'Doc carries clause: '
- 'expected one of: '
- ' | '
- 'dotenv import'
- 'supabase import'
- 'external-vendor import'
- 'embedding / vector import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'self_check:no_env_or_vendor'
- 'PAS163 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- ' — '
- 'see report'
- 'phase'
- 'PAS163'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas163_candidate_pipeline_readiness_check'
- 'PAS163 — Evaluate the outbound dial adapter, worker wiring, and memory candidate pipeline for structural correctness, no-auto-approval doctrine, and absence of raw-payload leakage. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- '[PAS163] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS163] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS163 — Outbound dial + memory candidate pipeline readiness gate.\n\nDeterministic, non-mutating evaluator for "is the outbound dial\nadapter wired, the memory candidate pipeline structurally safe,\nand Memory Review hooked to a real input source?".\n\nWalks the repo and verifies:\n  * outbound/dial.py exists and defines ``place_outbound_call``;\n  * the adapter never uses ``http://localhost/outbound/call``;\n  * the adapter never returns a fake / hard-coded call_sid token;\n  * the worker resolves ``place_outbound_call`` via its resolver,\n    marks DIALED on adapter ``status="ok"``, and marks FAILED on\n    adapter ``status="failed"``;\n  * the worker remains OFF by default\n    (``_ENV_FLAG_ENABLED_LITERAL = "true"`` unchanged);\n  * the candidate pipeline exposes the three required functions\n    and rejects calls without ``brokerage_id``;\n  * the pipeline filters DANGEROUS / EPHEMERAL kinds and never\n    emits APPROVED status directly;\n  * neither the pipeline nor the demo seed touches raw payload /\n    raw transcript / vector / embedding / external vendor code;\n  * the PAS162 / PAS161 / PAS160 readiness checkers still exist;\n  * no Memory Review UI file is deleted or modified by PAS163.\n\nEmits a verdict (READY / NOT_READY) plus a machine-readable\n``pas163_candidate_pipeline_readiness_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries.\n\nUsage:\n  python scripts/pas163_candidate_pipeline_readiness_check.py\n  python scripts/pas163_candidate_pipeline_readiness_check.py --json\n  python scripts/pas163_candidate_pipeline_readiness_check.py --summary-only\n  python scripts/pas163_candidate_pipeline_readiness_check.py --strict\n\nExit codes:\n    0  — READY  (verdict == READY)\n    1  — NOT_READY\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  48           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  52           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  53           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  55           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  56           LOAD_SMALL_INT           0
               LOAD_CONST               5 (('List', 'Optional'))
               IMPORT_NAME             11 (typing)
               IMPORT_FROM             12 (List)
               STORE_NAME              12 (List)
               IMPORT_FROM             13 (Optional)
               STORE_NAME              13 (Optional)
               POP_TOP

  59           LOAD_NAME                6 (sys)
               LOAD_ATTR               28 (stdout)
               LOAD_NAME                6 (sys)
               LOAD_ATTR               30 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              16 (_stream)

  60           NOP

  61   L2:     LOAD_NAME               16 (_stream)
               LOAD_ATTR               35 (reconfigure + NULL|self)
               LOAD_CONST               6 ('utf-8')
               LOAD_CONST               7 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  59   L4:     END_FOR
               POP_ITER

  66           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               41 (abspath + NULL|self)

  67           LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               43 (join + NULL|self)
               LOAD_NAME                5 (os)
               LOAD_ATTR               38 (path)
               LOAD_ATTR               45 (dirname + NULL|self)
               LOAD_NAME               23 (__file__)
               CALL                     1
               LOAD_CONST               8 ('..')
               CALL                     2

  66           CALL                     1
               STORE_NAME              24 (_REPO_ROOT_DEFAULT)

  71           LOAD_CONST               9 ('READY')
               STORE_NAME              25 (VERDICT_READY)

  72           LOAD_CONST              10 ('NOT_READY')
               STORE_NAME              26 (VERDICT_NOT_READY)

  74           LOAD_CONST              11 ('BLOCK')
               STORE_NAME              27 (SEVERITY_BLOCK)

  75           LOAD_CONST              12 ('INFO')
               STORE_NAME              28 (SEVERITY_INFO)

  82           LOAD_CONST              62 (('app/services/outbound/__init__.py', 'app/services/outbound/dial.py', 'app/services/memory/candidate_pipeline.py', 'app/services/ingestion/worker.py', 'scripts/seed_memory_candidate_demo.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'docs/pas163_outbound_dial_and_candidate_pipeline.md', 'tests/mvp/test_pas163_outbound_dial_candidate_pipeline.py'))
               STORE_NAME              29 (REQUIRED_FILES)

  95           LOAD_CONST              63 (('scripts/pas160_mvp_sequence_check.py', 'scripts/pas161_lead_ingestion_readiness_check.py', 'scripts/pas162_pending_calls_readiness_check.py'))
               STORE_NAME              30 (PRIOR_PHASE_FILES)

 102           LOAD_CONST              64 (('app/services/memory/review.py', 'app/services/memory/review_stats.py', 'app/services/memory/review_export.py', 'app/services/memory/review_actors.py', 'app/services/memory/review_alerts.py', 'app/services/memory/operator_console.py'))
               STORE_NAME              31 (MEMORY_REVIEW_FILES)

 112           LOAD_CONST              65 (('def place_outbound_call(',))
               STORE_NAME              32 (REQUIRED_DIAL_FUNCTIONS)

 116           LOAD_CONST              66 (('def build_memory_candidate_from_call(', 'def generate_memory_candidates_for_call(', 'def generate_memory_candidates_from_replay('))
               STORE_NAME              33 (REQUIRED_PIPELINE_FUNCTIONS)

 122           LOAD_CONST              67 (('def _resolve_outbound_dial_adapter(', 'def process_pending_call('))
               STORE_NAME              34 (REQUIRED_WORKER_FUNCTIONS)

 129           LOAD_CONST              68 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic', 'import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai.embeddings'))
               STORE_NAME              35 (FORBIDDEN_IMPORT_LINE_PREFIXES)

 141           LOAD_CONST              69 (('http://localhost', 'http://127.0.0.1', '/outbound/call', 'FAKE_CALL_SID', 'fake_call_sid', 'dummy_call_sid'))
               STORE_NAME              36 (FORBIDDEN_DIAL_PATTERNS)

 155           LOAD_CONST              13 ('severity')

 157           LOAD_NAME               27 (SEVERITY_BLOCK)

 155           LOAD_CONST              14 ('detail')

 157           LOAD_CONST              15 ('')

 155           BUILD_MAP                2
               LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 155>)
               MAKE_FUNCTION
               LOAD_CONST              17 (<code object _check at 0x0000018C17FA3E10, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 155>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (_check)

 168           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 168>)
               MAKE_FUNCTION
               LOAD_CONST              19 (<code object _now_iso at 0x0000018C180388F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 168>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (_now_iso)

 172           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 172>)
               MAKE_FUNCTION
               LOAD_CONST              21 (<code object _read_text at 0x0000018C18053AB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 172>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_read_text)

 179           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 179>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 179>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_strip_python_comments_and_strings)

 218           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 218>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object check_files_present at 0x0000018C180606F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 218>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (check_files_present)

 232           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 232>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (check_prior_phases_intact)

 246           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 246>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 246>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_memory_review_intact)

 260           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 260>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object check_dial_adapter at 0x0000018C17E8A470, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 260>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_dial_adapter)

 299           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 299>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object check_worker_wiring at 0x0000018C17F7A670, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 299>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_worker_wiring)

 361           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 361>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object check_candidate_pipeline at 0x0000018C17E56800, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 361>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_candidate_pipeline)

 444           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 444>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object check_seed_script at 0x0000018C17ECE6C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 444>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_seed_script)

 468           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 468>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object check_no_forbidden_imports at 0x0000018C17D8A830, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 468>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_no_forbidden_imports)

 498           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 498>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object check_event_contract_registration at 0x0000018C179A7290, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 498>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_event_contract_registration)

 519           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 519>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object check_docs_required_doctrine at 0x0000018C17F72F30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 519>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_docs_required_doctrine)

 551           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 551>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object check_self_no_env_or_vendor at 0x0000018C17F78C60, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 551>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_self_no_env_or_vendor)

 599           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 599>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 599>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_aggregate)

 615           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 615>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object _operator_actions at 0x0000018C180488F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 615>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (_operator_actions)

 625           LOAD_CONST              50 (<code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 625>)
               MAKE_FUNCTION
               LOAD_CONST              51 (<code object evaluate at 0x0000018C17F790E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 625>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (evaluate)

 655           LOAD_CONST              52 ('pas163_candidate_pipeline_readiness_report.json')
               STORE_NAME              55 (REPORT_FILENAME)

 658           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C180FC210, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 658>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object _build_parser at 0x0000018C1801CFB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 658>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_build_parser)

 692           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C180FC120, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 692>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 692>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_print_summary)

 710           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18025130, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 710>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object _write_report at 0x0000018C18104210, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 710>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_write_report)

 724           LOAD_CONST              70 ((None,))
               LOAD_CONST              59 (<code object __annotate__ at 0x0000018C180FC300, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 724>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object main at 0x0000018C17F83070, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 724>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              59 (main)

 752           LOAD_NAME               60 (__name__)
               LOAD_CONST              61 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 753           LOAD_NAME                6 (sys)
               LOAD_ATTR              122 (exit)
               PUSH_NULL
               LOAD_NAME               59 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 752   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  62           LOAD_NAME               18 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  63   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          315 (to L1)

  62   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 155>:
155           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

156           LOAD_CONST               2 ('str')

155           LOAD_CONST               3 ('status')

156           LOAD_CONST               2 ('str')

155           LOAD_CONST               4 ('label')

156           LOAD_CONST               2 ('str')

155           LOAD_CONST               5 ('severity')

157           LOAD_CONST               2 ('str')

155           LOAD_CONST               6 ('detail')

157           LOAD_CONST               2 ('str')

155           LOAD_CONST               7 ('return')

158           LOAD_CONST               8 ('dict')

155           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA3E10, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 155>:
155           RESUME                   0

160           LOAD_CONST               0 ('id')
              LOAD_FAST_BORROW         0 (check_id)

161           LOAD_CONST               1 ('status')
              LOAD_FAST_BORROW         1 (status)

162           LOAD_CONST               2 ('label')
              LOAD_FAST_BORROW         2 (label)

163           LOAD_CONST               3 ('severity')
              LOAD_FAST_BORROW         3 (severity)

164           LOAD_CONST               4 ('detail')
              LOAD_FAST_BORROW         4 (detail)

159           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 168>:
168           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 168>:
168           RESUME                   0

169           LOAD_GLOBAL              0 (datetime)
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

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 172>:
172           RESUME                   0
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

Disassembly of <code object _read_text at 0x0000018C18053AB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 172>:
 172           RESUME                   0

 173           NOP

 174   L1:     LOAD_FAST_BORROW         0 (path)
               LOAD_ATTR                1 (read_text + NULL|self)
               LOAD_CONST               0 ('utf-8')
               LOAD_CONST               1 ('replace')
               LOAD_CONST               2 (('encoding', 'errors'))
               CALL_KW                  2
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 175           LOAD_GLOBAL              2 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 176   L4:     POP_EXCEPT
               LOAD_CONST               3 (None)
               RETURN_VALUE

 175   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 179>:
179           RESUME                   0
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

Disassembly of <code object _strip_python_comments_and_strings at 0x0000018C17E59E70, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 179>:
179            RESUME                   0

180            BUILD_LIST               0
               STORE_FAST               1 (out)

181            LOAD_SMALL_INT           0
               LOAD_GLOBAL              1 (len + NULL)
               LOAD_FAST_BORROW         0 (src)
               CALL                     1
               STORE_FAST_STORE_FAST   50 (n, i)

182    L1:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (i, n)
               COMPARE_OP              18 (bool(<))
               EXTENDED_ARG             1
               POP_JUMP_IF_FALSE      282 (to L13)
               NOT_TAKEN

183            LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               BINARY_OP               26 ([])
               STORE_FAST               4 (ch)

184            LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               1 ('#')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       38 (to L3)
               NOT_TAKEN

185            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_CONST               2 ('\n')
               LOAD_FAST_BORROW         2 (i)
               CALL                     2
               STORE_FAST               5 (j)

186            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L2)
               NOT_TAKEN

187            JUMP_FORWARD           240 (to L13)

188    L2:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

189            JUMP_BACKWARD           59 (to L1)

190    L3:     LOAD_FAST_BORROW         0 (src)
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

191    L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (src, i)
               LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               BINARY_SLICE
               STORE_FAST               6 (quote)

192            LOAD_FAST_BORROW         0 (src)
               LOAD_ATTR                3 (find + NULL|self)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 98 (quote, i)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               CALL                     2
               STORE_FAST               7 (end)

193            LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           0
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        2 (to L5)
               NOT_TAKEN

194            JUMP_FORWARD           138 (to L13)

195    L5:     LOAD_FAST_BORROW         7 (end)
               LOAD_SMALL_INT           3
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

196            JUMP_BACKWARD          161 (to L1)

197    L6:     LOAD_FAST_BORROW         4 (ch)
               LOAD_CONST               7 (('"', "'"))
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_FALSE       92 (to L12)
               NOT_TAKEN

198            LOAD_FAST                4 (ch)
               STORE_FAST               6 (quote)

199            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               5 (j)

200    L7:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (j, n)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE       63 (to L11)
               NOT_TAKEN

201            LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
               BINARY_OP               26 ([])
               LOAD_CONST               5 ('\\')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       12 (to L8)
               NOT_TAKEN

202            LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           2
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)

203            JUMP_BACKWARD           30 (to L7)

204    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (src, j)
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

205    L9:     JUMP_FORWARD            11 (to L11)

206   L10:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               5 (j)
               JUMP_BACKWARD           68 (to L7)

207   L11:     LOAD_FAST_BORROW         5 (j)
               LOAD_SMALL_INT           1
               BINARY_OP                0 (+)
               STORE_FAST               2 (i)

208            EXTENDED_ARG             1
               JUMP_BACKWARD          259 (to L1)

209   L12:     LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_FAST_BORROW         4 (ch)
               CALL                     1
               POP_TOP

210            LOAD_FAST_BORROW         2 (i)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST               2 (i)
               EXTENDED_ARG             1
               JUMP_BACKWARD          288 (to L1)

211   L13:     LOAD_CONST               6 ('')
               LOAD_ATTR                9 (join + NULL|self)
               LOAD_FAST_BORROW         1 (out)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 218>:
218           RESUME                   0
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

Disassembly of <code object check_files_present at 0x0000018C180606F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 218>:
218           RESUME                   0

219           BUILD_LIST               0
              STORE_FAST               1 (out)

220           LOAD_GLOBAL              0 (REQUIRED_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

221           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

222           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

223           LOAD_CONST               0 ('file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

224           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

225   L3:     LOAD_CONST               3 ('Required PAS163 file present: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

226           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

227           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing')

222   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

220   L6:     END_FOR
              POP_ITER

229           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 232>:
232           RESUME                   0
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

Disassembly of <code object check_prior_phases_intact at 0x0000018C18061110, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 232>:
232           RESUME                   0

233           BUILD_LIST               0
              STORE_FAST               1 (out)

234           LOAD_GLOBAL              0 (PRIOR_PHASE_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

235           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

236           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

237           LOAD_CONST               0 ('prior_phase:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

238           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

239   L3:     LOAD_CONST               3 ('Prior-phase readiness script intact: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

240           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

241           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — PAS163 must not delete')

236   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

234   L6:     END_FOR
              POP_ITER

243           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 246>:
246           RESUME                   0
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

Disassembly of <code object check_memory_review_intact at 0x0000018C18060DB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 246>:
246           RESUME                   0

247           BUILD_LIST               0
              STORE_FAST               1 (out)

248           LOAD_GLOBAL              0 (MEMORY_REVIEW_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

249           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

250           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

251           LOAD_CONST               0 ('memory_review_file:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

252           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

253   L3:     LOAD_CONST               3 ('Memory Review file present (PAS163 must not delete): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

254           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

255           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('PAS163 must not delete Memory Review files')

250   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

248   L6:     END_FOR
              POP_ITER

257           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 260>:
260           RESUME                   0
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

Disassembly of <code object check_dial_adapter at 0x0000018C17E8A470, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 260>:
260            RESUME                   0

261            BUILD_LIST               0
               STORE_FAST               1 (out)

262            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('outbound')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('dial.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

263            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

264            LOAD_GLOBAL              4 (REQUIRED_DIAL_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

265            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

266            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

267            LOAD_CONST               5 ('dial_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

268            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

269    L4:     LOAD_CONST               9 ('Dial function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

270            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

271            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

266    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

264    L7:     END_FOR
               POP_ITER

273            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST               6 (executable)

274            LOAD_GLOBAL             16 (FORBIDDEN_DIAL_PATTERNS)
               GET_ITER
       L8:     FOR_ITER                80 (to L13)
               STORE_FAST               7 (forbidden)

275            LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (forbidden, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (present)

276            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

277            LOAD_CONST              12 ('dial:no_forbidden:')
               LOAD_FAST_BORROW         7 (forbidden)
               LOAD_CONST              13 (slice(None, 32, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

278            LOAD_FAST_BORROW         8 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L9)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L10)
       L9:     LOAD_CONST               7 ('PASS')

279   L10:     LOAD_CONST              14 ('Dial adapter excludes pattern: ')
               LOAD_FAST_BORROW         7 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

280            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

282            LOAD_FAST_BORROW         8 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L11)
               NOT_TAKEN

281            LOAD_CONST              15 ('pattern ')
               LOAD_FAST_BORROW         7 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              16 (' present in executable')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L12)

282   L11:     LOAD_CONST               4 ('')

276   L12:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           82 (to L8)

274   L13:     END_FOR
               POP_ITER

287            LOAD_CONST              17 ('.startswith("+")')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L14)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              18 (".startswith('+')")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

286   L14:     STORE_FAST               9 (has_phone_guard)

289            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

290            LOAD_CONST              19 ('dial:phone_guard')

291            LOAD_FAST_BORROW         9 (has_phone_guard)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST               8 ('FAIL')

292   L16:     LOAD_CONST              20 ('Dial adapter validates E.164 phone format')

293            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

294            LOAD_FAST_BORROW         9 (has_phone_guard)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST              21 ("missing '+' guard in dial adapter")

289   L18:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

296            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 299>:
299           RESUME                   0
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

Disassembly of <code object check_worker_wiring at 0x0000018C17F7A670, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 299>:
299            RESUME                   0

300            BUILD_LIST               0
               STORE_FAST               1 (out)

301            LOAD_GLOBAL              1 (Path + NULL)
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

302            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

303            LOAD_GLOBAL              4 (REQUIRED_WORKER_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

304            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

305            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

306            LOAD_CONST               5 ('worker_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

307            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

308    L4:     LOAD_CONST               9 ('Worker function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

309            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

310            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

305    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

303    L7:     END_FOR
               POP_ITER

314            LOAD_CONST              12 ('from app.services.outbound.dial import place_outbound_call')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

313            STORE_FAST               6 (import_ok)

316            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

317            LOAD_CONST              13 ('worker:imports_dial_adapter')

318            LOAD_FAST_BORROW         6 (import_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               8 ('FAIL')

319    L9:     LOAD_CONST              14 ('Worker resolver imports place_outbound_call')

320            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

321            LOAD_FAST_BORROW         6 (import_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)

322   L10:     LOAD_CONST              15 ("missing 'from app.services.outbound.dial import place_outbound_call'")

316   L11:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

327            LOAD_CONST              16 ('adapter_status == "ok"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L12)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              17 ("adapter_status == 'ok'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

326   L12:     STORE_FAST               7 (dialed_ok)

329            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

330            LOAD_CONST              18 ('worker:dialed_on_ok')

331            LOAD_FAST_BORROW         7 (dialed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L13)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L14)
      L13:     LOAD_CONST               8 ('FAIL')

332   L14:     LOAD_CONST              19 ("Worker marks DIALED on adapter status='ok'")

333            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

334            LOAD_FAST_BORROW         7 (dialed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L15)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L16)
      L15:     LOAD_CONST              20 ('missing \'adapter_status == "ok"\' branch')

329   L16:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

337            LOAD_CONST              21 ('outbound_dial_adapter_missing')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (failed_ok)

338            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

339            LOAD_CONST              22 ('worker:failed_on_adapter_missing')

340            LOAD_FAST_BORROW         8 (failed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L17)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L18)
      L17:     LOAD_CONST               8 ('FAIL')

341   L18:     LOAD_CONST              23 ('Worker marks FAILED with outbound_dial_adapter_missing')

342            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

343            LOAD_FAST_BORROW         8 (failed_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L19)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L20)
      L19:     LOAD_CONST              24 ("missing 'outbound_dial_adapter_missing' branch")

338   L20:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

348            LOAD_CONST              25 ('_ENV_FLAG_ENABLED_LITERAL = "true"')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L21)
               NOT_TAKEN
               POP_TOP

349            LOAD_CONST              26 ("_ENV_FLAG_ENABLED_LITERAL = 'true'")
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)

347   L21:     STORE_FAST               9 (flag_ok)

351            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

352            LOAD_CONST              27 ('worker:off_by_default')

353            LOAD_FAST_BORROW         9 (flag_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L22)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L23)
      L22:     LOAD_CONST               8 ('FAIL')

354   L23:     LOAD_CONST              28 ('Worker remains OFF by default (strict enable literal)')

355            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

356            LOAD_FAST_BORROW         9 (flag_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L24)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L25)
      L24:     LOAD_CONST              29 ('enable literal constant not found')

351   L25:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

358            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 361>:
361           RESUME                   0
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

Disassembly of <code object check_candidate_pipeline at 0x0000018C17E56800, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 361>:
361            RESUME                   0

362            BUILD_LIST               0
               STORE_FAST               1 (out)

363            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('app')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('services')
               BINARY_OP               11 (/)
               LOAD_CONST               2 ('memory')
               BINARY_OP               11 (/)
               LOAD_CONST               3 ('candidate_pipeline.py')
               BINARY_OP               11 (/)
               STORE_FAST               2 (p)

364            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               4 ('')
       L1:     STORE_FAST               3 (src)

365            LOAD_GLOBAL              4 (REQUIRED_PIPELINE_FUNCTIONS)
               GET_ITER
       L2:     FOR_ITER                92 (to L7)
               STORE_FAST               4 (needle)

366            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

367            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

368            LOAD_CONST               5 ('pipeline_fn:')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_CONST               6 (slice(None, 40, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               BUILD_STRING             2

369            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               8 ('FAIL')

370    L4:     LOAD_CONST               9 ('Pipeline function present: ')
               LOAD_FAST_BORROW         4 (needle)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               FORMAT_SIMPLE
               BUILD_STRING             2

371            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

372            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST              10 ('missing def: ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

367    L6:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           94 (to L2)

365    L7:     END_FOR
               POP_ITER

375            LOAD_CONST              12 ('classify_memory_candidate')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (classify_ok)

376            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

377            LOAD_CONST              13 ('pipeline:reuses_classifier')

378            LOAD_FAST_BORROW         6 (classify_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               8 ('FAIL')

379    L9:     LOAD_CONST              14 ('Pipeline reuses classify_memory_candidate')

380            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

381            LOAD_FAST_BORROW         6 (classify_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              15 ('classifier reference not found')

376   L11:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

385            LOAD_CONST              16 ('MemoryKind.DANGEROUS')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               7 (danger_ok)

386            LOAD_CONST              17 ('MemoryKind.EPHEMERAL')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               8 (ephemeral_ok)

387            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

388            LOAD_CONST              18 ('pipeline:filters_dangerous_ephemeral')

389            LOAD_FAST_BORROW         7 (danger_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE       11 (to L12)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (ephemeral_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST               8 ('FAIL')

390   L13:     LOAD_CONST              19 ('Pipeline source filters DANGEROUS and EPHEMERAL kinds')

391            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

392            LOAD_FAST_BORROW         7 (danger_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE       11 (to L14)
               NOT_TAKEN
               LOAD_FAST_BORROW         8 (ephemeral_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L14)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L15)

393   L14:     LOAD_CONST              20 ('expected references to MemoryKind.DANGEROUS and MemoryKind.EPHEMERAL')

387   L15:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

398            LOAD_CONST              21 ('MemoryStatus.CANDIDATE')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               9 (candidate_ok)

399            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

400            LOAD_CONST              22 ('pipeline:candidate_only')

401            LOAD_FAST_BORROW         9 (candidate_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L16)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L17)
      L16:     LOAD_CONST               8 ('FAIL')

402   L17:     LOAD_CONST              23 ('Pipeline forces MemoryStatus.CANDIDATE on every record')

403            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

404            LOAD_FAST_BORROW         9 (candidate_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L18)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L19)
      L18:     LOAD_CONST              24 ('expected MemoryStatus.CANDIDATE reference')

399   L19:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

407            LOAD_GLOBAL             15 (_strip_python_comments_and_strings + NULL)
               LOAD_FAST_BORROW         3 (src)
               CALL                     1
               STORE_FAST              10 (executable)

409            LOAD_CONST              25 ('MemoryStatus.APPROVED')
               LOAD_FAST_BORROW        10 (executable)
               CONTAINS_OP              0 (in)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         6 (to L20)
               NOT_TAKEN
               POP_TOP

410            LOAD_CONST              26 ('approve_memory')
               LOAD_FAST_BORROW        10 (executable)
               CONTAINS_OP              0 (in)

408   L20:     STORE_FAST              11 (approve_present)

412            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

413            LOAD_CONST              27 ('pipeline:no_auto_approve')

414            LOAD_FAST_BORROW        11 (approve_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L21)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L22)
      L21:     LOAD_CONST               7 ('PASS')

415   L22:     LOAD_CONST              28 ('Pipeline never sets MemoryStatus.APPROVED')

416            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

418            LOAD_FAST_BORROW        11 (approve_present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L23)
               NOT_TAKEN

417            LOAD_CONST              29 ('APPROVED status / approve_memory present in executable')
               JUMP_FORWARD             1 (to L24)

418   L23:     LOAD_CONST               4 ('')

412   L24:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

422            LOAD_CONST              30 ('missing_brokerage_id')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST              12 (bid_ok)

423            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

424            LOAD_CONST              31 ('pipeline:requires_brokerage_id')

425            LOAD_FAST_BORROW        12 (bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L25)
               NOT_TAKEN
               LOAD_CONST               7 ('PASS')
               JUMP_FORWARD             1 (to L26)
      L25:     LOAD_CONST               8 ('FAIL')

426   L26:     LOAD_CONST              32 ('Pipeline rejects calls without brokerage_id')

427            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

428            LOAD_FAST_BORROW        12 (bid_ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L27)
               NOT_TAKEN
               LOAD_CONST               4 ('')
               JUMP_FORWARD             1 (to L28)
      L27:     LOAD_CONST              33 ('missing_brokerage_id token not found')

423   L28:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

431            LOAD_CONST              38 (('raw_payload', 'raw_transcript', 'full_transcript'))
               GET_ITER
      L29:     FOR_ITER                74 (to L34)
               STORE_FAST              13 (forbidden)

432            LOAD_FAST_BORROW_LOAD_FAST_BORROW 218 (forbidden, executable)
               CONTAINS_OP              0 (in)
               STORE_FAST              14 (present)

433            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)
               LOAD_GLOBAL              9 (_check + NULL)

434            LOAD_CONST              34 ('pipeline:no_forbidden:')
               LOAD_FAST_BORROW        13 (forbidden)
               FORMAT_SIMPLE
               BUILD_STRING             2

435            LOAD_FAST_BORROW        14 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L30)
               NOT_TAKEN
               LOAD_CONST               8 ('FAIL')
               JUMP_FORWARD             1 (to L31)
      L30:     LOAD_CONST               7 ('PASS')

436   L31:     LOAD_CONST              35 ('Pipeline excludes forbidden field ')
               LOAD_FAST_BORROW        13 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               BUILD_STRING             2

437            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

439            LOAD_FAST_BORROW        14 (present)
               TO_BOOL
               POP_JUMP_IF_FALSE        8 (to L32)
               NOT_TAKEN

438            LOAD_CONST              36 ('forbidden field ')
               LOAD_FAST_BORROW        13 (forbidden)
               CONVERT_VALUE            2 (repr)
               FORMAT_SIMPLE
               LOAD_CONST              37 (' in executable')
               BUILD_STRING             3
               JUMP_FORWARD             1 (to L33)

439   L32:     LOAD_CONST               4 ('')

433   L33:     LOAD_CONST              11 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           76 (to L29)

431   L34:     END_FOR
               POP_ITER

441            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 444>:
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

Disassembly of <code object check_seed_script at 0x0000018C17ECE6C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 444>:
444            RESUME                   0

445            BUILD_LIST               0
               STORE_FAST               1 (out)

446            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_CONST               0 ('scripts')
               BINARY_OP               11 (/)
               LOAD_CONST               1 ('seed_memory_candidate_demo.py')
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
               LOAD_CONST               2 ('')
       L1:     STORE_FAST               3 (src)

448            LOAD_CONST              13 (('--brokerage-id', '--demo', '--json'))
               GET_ITER
       L2:     FOR_ITER                71 (to L7)
               STORE_FAST               4 (needle)

449            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (needle, src)
               CONTAINS_OP              0 (in)
               STORE_FAST               5 (ok)

450            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

451            LOAD_CONST               3 ('seed:cli_flag:')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

452            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L4)
       L3:     LOAD_CONST               5 ('FAIL')

453    L4:     LOAD_CONST               6 ('Seed CLI exposes flag ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

454            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

455            LOAD_FAST_BORROW         5 (ok)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L5)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             4 (to L6)
       L5:     LOAD_CONST               7 ('missing CLI flag ')
               LOAD_FAST_BORROW         4 (needle)
               FORMAT_SIMPLE
               BUILD_STRING             2

450    L6:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

448    L7:     END_FOR
               POP_ITER

457            LOAD_CONST               9 ('generate_memory_candidates_from_replay')
               LOAD_FAST_BORROW         3 (src)
               CONTAINS_OP              0 (in)
               STORE_FAST               6 (pipeline_ref)

458            LOAD_FAST                1 (out)
               LOAD_ATTR                5 (append + NULL|self)
               LOAD_GLOBAL              7 (_check + NULL)

459            LOAD_CONST              10 ('seed:uses_pipeline')

460            LOAD_FAST_BORROW         6 (pipeline_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               4 ('PASS')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               5 ('FAIL')

461    L9:     LOAD_CONST              11 ('Seed invokes generate_memory_candidates_from_replay')

462            LOAD_GLOBAL              8 (SEVERITY_BLOCK)

463            LOAD_FAST_BORROW         6 (pipeline_ref)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L10)
               NOT_TAKEN
               LOAD_CONST               2 ('')
               JUMP_FORWARD             1 (to L11)
      L10:     LOAD_CONST              12 ('pipeline reference not found')

458   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

465            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 468>:
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

Disassembly of <code object check_no_forbidden_imports at 0x0000018C17D8A830, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 468>:
468            RESUME                   0

469            BUILD_LIST               0
               STORE_FAST               1 (out)

470            LOAD_CONST               9 (('app/services/outbound/dial.py', 'app/services/outbound/__init__.py', 'app/services/memory/candidate_pipeline.py', 'scripts/seed_memory_candidate_demo.py', 'scripts/pas163_candidate_pipeline_readiness_check.py', 'app/services/ingestion/worker.py'))
               STORE_FAST               2 (files)

478            LOAD_FAST_BORROW         2 (files)
               GET_ITER
       L1:     FOR_ITER               241 (to L12)
               STORE_FAST               3 (relpath)

479            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (repo_root)
               CALL                     1
               LOAD_FAST_BORROW         3 (relpath)
               BINARY_OP               11 (/)
               STORE_FAST               4 (p)

480            LOAD_GLOBAL              3 (_read_text + NULL)
               LOAD_FAST_BORROW         4 (p)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L2:     STORE_FAST               5 (src)

481            BUILD_LIST               0
               STORE_FAST               6 (bad)

482            LOAD_FAST_BORROW         5 (src)
               LOAD_ATTR                5 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L3:     FOR_ITER                74 (to L7)
               STORE_FAST               7 (line)

483            LOAD_FAST_BORROW         7 (line)
               LOAD_ATTR                7 (strip + NULL|self)
               CALL                     0
               STORE_FAST               8 (stripped)

484            LOAD_GLOBAL              8 (FORBIDDEN_IMPORT_LINE_PREFIXES)
               GET_ITER
       L4:     FOR_ITER                45 (to L6)
               STORE_FAST               9 (prefix)

485            LOAD_FAST_BORROW         8 (stripped)
               LOAD_ATTR               11 (startswith + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L5)
               NOT_TAKEN
               JUMP_BACKWARD           28 (to L4)

486    L5:     LOAD_FAST_BORROW         6 (bad)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_FAST_BORROW         9 (prefix)
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           47 (to L4)

484    L6:     END_FOR
               POP_ITER
               JUMP_BACKWARD           76 (to L3)

482    L7:     END_FOR
               POP_ITER

487            LOAD_FAST                1 (out)
               LOAD_ATTR               13 (append + NULL|self)
               LOAD_GLOBAL             15 (_check + NULL)

488            LOAD_CONST               2 ('forbidden_import:')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

489            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L8)
               NOT_TAKEN
               LOAD_CONST               3 ('FAIL')
               JUMP_FORWARD             1 (to L9)
       L8:     LOAD_CONST               4 ('PASS')

490    L9:     LOAD_CONST               5 ('No forbidden imports: ')
               LOAD_FAST_BORROW         4 (p)
               LOAD_ATTR               16 (name)
               FORMAT_SIMPLE
               BUILD_STRING             2

491            LOAD_GLOBAL             18 (SEVERITY_BLOCK)

493            LOAD_FAST_BORROW         6 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

492            LOAD_CONST               6 ('forbidden import prefixes: ')
               LOAD_CONST               7 (', ')
               LOAD_ATTR               21 (join + NULL|self)
               LOAD_FAST_BORROW         6 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L11)

493   L10:     LOAD_CONST               1 ('')

487   L11:     LOAD_CONST               8 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP
               JUMP_BACKWARD          243 (to L1)

478   L12:     END_FOR
               POP_ITER

495            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 498>:
498           RESUME                   0
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

Disassembly of <code object check_event_contract_registration at 0x0000018C179A7290, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 498>:
498           RESUME                   0

499           BUILD_LIST               0
              STORE_FAST               1 (out)

500           LOAD_GLOBAL              1 (Path + NULL)
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

501           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (p)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L1:     STORE_FAST               3 (src)

502           LOAD_CONST              11 (('pending_call.dialed', 'pending_call.failed', 'memory.candidate.generated', 'memory.candidate.generation_failed'))
              GET_ITER
      L2:     FOR_ITER                72 (to L7)
              STORE_FAST               4 (required)

508           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (required, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

509           LOAD_FAST                1 (out)
              LOAD_ATTR                5 (append + NULL|self)
              LOAD_GLOBAL              7 (_check + NULL)

510           LOAD_CONST               5 ('events:')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

511           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               6 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               7 ('FAIL')

512   L4:     LOAD_CONST               8 ('Event contract registers ')
              LOAD_FAST_BORROW         4 (required)
              FORMAT_SIMPLE
              BUILD_STRING             2

513           LOAD_GLOBAL              8 (SEVERITY_BLOCK)

514           LOAD_FAST_BORROW         5 (ok)
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

509   L6:     LOAD_CONST              10 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           74 (to L2)

502   L7:     END_FOR
              POP_ITER

516           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 519>:
519           RESUME                   0
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

Disassembly of <code object check_docs_required_doctrine at 0x0000018C17F72F30, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 519>:
  --            MAKE_CELL                8 (lower)

 519            RESUME                   0

 520            BUILD_LIST               0
                STORE_FAST               1 (out)

 521            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               0 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               1 ('pas163_outbound_dial_and_candidate_pipeline.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (doc)

 522            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               2 ('')
        L1:     STORE_FAST               3 (src)

 523            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_DEREF              8 (lower)

 524            LOAD_CONST              13 ((('outbound-dial', ('outbound dial', 'place_outbound_call')), ('worker-integration', ('worker', 'process_pending_call')), ('candidate-pipeline', ('candidate pipeline', 'memory candidate')), ('no-auto-approval', ('no auto-approval', 'no auto approve', 'never auto-approve', 'candidate only', 'no auto-approval doctrine')), ('no-raw-transcript', ('no raw transcript', 'raw transcript', 'no raw payload')), ('event-safety', ('event payload safety', 'event payload')), ('demo-seed', ('demo seed', 'seed_memory_candidate_demo')), ('limitations', ('limitations', 'intentionally not built')), ('memory-review', ('memory review',))))
                STORE_FAST               4 (required_phrases)

 538            LOAD_FAST_BORROW         4 (required_phrases)
                GET_ITER
        L2:     FOR_ITER               146 (to L12)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (name, phrases)

 539            LOAD_GLOBAL              6 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       31 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         8 (lower)
                BUILD_TUPLE              1
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026530, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 539>)
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
                LOAD_CONST               3 (<code object <genexpr> at 0x0000018C18026530, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 539>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_FAST_BORROW         6 (phrases)
                GET_ITER
                CALL                     0
                CALL                     1
        L7:     STORE_FAST               7 (present)

 540            LOAD_FAST                1 (out)
                LOAD_ATTR                9 (append + NULL|self)
                LOAD_GLOBAL             11 (_check + NULL)

 541            LOAD_CONST               6 ('docs:phrase:')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 542            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               7 ('PASS')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               8 ('FAIL')

 543    L9:     LOAD_CONST               9 ('Doc carries clause: ')
                LOAD_FAST_BORROW         5 (name)
                FORMAT_SIMPLE
                BUILD_STRING             2

 544            LOAD_GLOBAL             12 (SEVERITY_BLOCK)

 546            LOAD_FAST_BORROW         7 (present)
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L10)
                NOT_TAKEN

 545            LOAD_CONST              10 ('expected one of: ')
                LOAD_CONST              11 (' | ')
                LOAD_ATTR               15 (join + NULL|self)
                LOAD_FAST_BORROW         6 (phrases)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 546   L10:     LOAD_CONST               2 ('')

 540   L11:     LOAD_CONST              12 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          148 (to L2)

 538   L12:     END_FOR
                POP_ITER

 548            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18026530, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 539>:
  --           COPY_FREE_VARS           1

 539           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 551>:
551           RESUME                   0
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

Disassembly of <code object check_self_no_env_or_vendor at 0x0000018C17F78C60, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 551>:
551            RESUME                   0

552            BUILD_LIST               0
               STORE_FAST               1 (out)

553            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

554            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               0 ('')
       L1:     STORE_FAST               3 (src)

555            BUILD_LIST               0
               STORE_FAST               4 (bad)

556            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

557            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

558            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               1 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

559            JUMP_BACKWARD           45 (to L2)

560    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              16 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

561            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               2 ('dotenv import')
               CALL                     1
               POP_TOP

562    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

563            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('supabase import')
               CALL                     1
               POP_TOP

564    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw', 'import openai', 'from openai', 'import anthropic', 'from anthropic'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

570            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('external-vendor import')
               CALL                     1
               POP_TOP

571    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

577            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('embedding / vector import')
               CALL                     1
               POP_TOP

578    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

579            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               6 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

580    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               7 ('load_dotenv() call')
               CALL                     1
               POP_TOP

581    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

582   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

556   L11:     END_FOR
               POP_ITER

583            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

584            LOAD_CONST               9 ('self_check:no_env_or_vendor')

585            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              10 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              11 ('PASS')

586   L13:     LOAD_CONST              12 ('PAS163 readiness checker never reads .env, calls Supabase, or imports vendor / embedding libs')

588            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

590            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

589            LOAD_CONST              13 ('disqualifying code-line patterns: ')
               LOAD_CONST              14 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

590   L14:     LOAD_CONST               0 ('')

583   L15:     LOAD_CONST              15 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

592            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 599>:
599           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC57C0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 599>:
 599            RESUME                   0

 601            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 600            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 601    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 602            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 601    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 602    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 601    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 600    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 605            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 604            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 605   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 606            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 605   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 606   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 605   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 604   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 609            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)

 610   L18:     LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)

 611            LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)

 608            BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 600            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 604            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 615>:
615           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C180488F0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 615>:
615           RESUME                   0

616           BUILD_LIST               0
              STORE_FAST               1 (out)

617           LOAD_FAST_BORROW         0 (checks)
              GET_ITER
      L1:     FOR_ITER               109 (to L5)
              STORE_FAST               2 (c)

618           LOAD_FAST_BORROW         2 (c)
              LOAD_CONST               0 ('status')
              BINARY_OP               26 ([])
              LOAD_CONST               1 ('FAIL')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

619           JUMP_BACKWARD           19 (to L1)

620   L2:     LOAD_FAST_BORROW         2 (c)
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

621           LOAD_FAST                1 (out)
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

617   L5:     END_FOR
              POP_ITER

622           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3000, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 625>:
625           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F790E0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 625>:
625           RESUME                   0

626           BUILD_LIST               0
              STORE_FAST               1 (checks)

627           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_files_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

628           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_phases_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

629           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_memory_review_intact + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

630           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_dial_adapter + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

631           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_worker_wiring + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

632           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_candidate_pipeline + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

633           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_seed_script + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

634           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_no_forbidden_imports + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

635           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_event_contract_registration + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

636           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_docs_required_doctrine + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

637           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             23 (check_self_no_env_or_vendor + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

639           LOAD_GLOBAL             25 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

641           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS163')

642           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             27 (_now_iso + NULL)
              CALL                     0

643           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

644           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             28 (VERDICT_READY)
              COMPARE_OP              72 (==)

645           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

646           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

647           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             31 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

648           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             33 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 648>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

649           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             33 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C18052F70, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 649>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

650           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

651           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             35 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

640           BUILD_MAP               11
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053CF0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 648>:
 648           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C18052F70, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 649>:
 649           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C180FC210, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 658>:
658           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CFB0, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 658>:
658           RESUME                   0

659           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

660           LOAD_CONST               0 ('pas163_candidate_pipeline_readiness_check')

662           LOAD_CONST               1 ('PAS163 — Evaluate the outbound dial adapter, worker wiring, and memory candidate pipeline for structural correctness, no-auto-approval doctrine, and absence of raw-payload leakage. Read-only. Does not touch Supabase, .env, or any tenant data.')

659           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

669           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

670           LOAD_CONST               3 ('--repo-root')
              LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

671           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

669           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

673           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

674           LOAD_CONST               6 ('--output')
              LOAD_GLOBAL              8 (REPORT_FILENAME)

675           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

673           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

677           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

678           LOAD_CONST               9 ('--json')
              LOAD_CONST              10 ('store_true')

679           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

677           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

681           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

682           LOAD_CONST              13 ('--summary-only')
              LOAD_CONST              10 ('store_true')

683           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

681           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

685           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

686           LOAD_CONST              15 ('--strict')
              LOAD_CONST              10 ('store_true')

687           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

685           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

689           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180FC120, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 692>:
692           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8CD10, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 692>:
692           RESUME                   0

693           LOAD_GLOBAL              1 (print + NULL)

694           LOAD_CONST               0 ('[PAS163] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

695           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

696           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

697           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

698           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

699           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

694           BUILD_STRING            12

693           CALL                     1
              POP_TOP

701           LOAD_FAST_BORROW         0 (report)
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

702           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

703           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS163] operator actions:')
              CALL                     1
              POP_TOP

704           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 25, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

705           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

704   L3:     END_FOR
              POP_ITER

706           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          25
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

707           LOAD_GLOBAL              1 (print + NULL)
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

706   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

702   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025130, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 710>:
710           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104210, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 710>:
 710           RESUME                   0

 711           NOP

 712   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 713           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 714           LOAD_CONST               3 ('utf-8')

 712           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 716           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 717   L4:     LOAD_GLOBAL             11 (print + NULL)

 718           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 719           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 718           BUILD_STRING             4

 720           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 717           LOAD_CONST               7 (('file',))
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

 716   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC300, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 724>:
724           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F83070, file "scripts\pas163_candidate_pipeline_readiness_check.py", line 724>:
 724            RESUME                   0

 725            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 726            NOP

 727    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 731    L2:     LOAD_GLOBAL             10 (os)
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

 732            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 733            LOAD_GLOBAL             23 (print + NULL)

 734            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 735            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 733            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 737            LOAD_SMALL_INT           2
                RETURN_VALUE

 739    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 741            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 742            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 744    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 746            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 747            LOAD_GLOBAL             23 (print + NULL)
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

 749    L6:     LOAD_FAST                5 (report)
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

 728            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 729    L9:     LOAD_FAST                3 (e)
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

 728   L17:     RERAISE                  0

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
