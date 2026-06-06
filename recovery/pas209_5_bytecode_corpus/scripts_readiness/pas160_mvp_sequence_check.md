# scripts_readiness/pas160_mvp_sequence_check

- **pyc:** `scripts\__pycache__\pas160_mvp_sequence_check.cpython-314.pyc`
- **expected source path (absent):** `scripts/pas160_mvp_sequence_check.py`
- **co_filename (from bytecode):** `scripts/pas160_mvp_sequence_check.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS160 — Production MVP doctrine + sequence lock gate.

Deterministic, non-mutating evaluator for "is the locked
PAS161→PAS170 MVP sequence on file and self-consistent?".
Walks the repo, confirms the PAS160 doctrine + sequence
documents exist, confirms each phase PAS161 → PAS170 is named
in the sequence doc, confirms the five hard MVP blockers are
each called out by name in at least one of the docs, confirms
the doctrine carries every required freeze / safety clause
(Memory Review frozen, TrustClaw audit-first, no production
data, no migrations in PAS160), and confirms that the prior-
phase readiness checkers it depends on (PAS145, PAS158) are
still present. Emits a verdict (READY / NOT_READY) plus a
machine-readable ``pas160_mvp_sequence_check_report.json``.

This script never:
  * modifies files,
  * calls Supabase,
  * reads .env / secrets,
  * imports external vendors,
  * imports embedding / vector libraries,
  * touches the off-limits
    ``scripts/combined_supabase_migration.sql``.

Usage:
  python scripts/pas160_mvp_sequence_check.py
  python scripts/pas160_mvp_sequence_check.py --json
  python scripts/pas160_mvp_sequence_check.py --summary-only
  python scripts/pas160_mvp_sequence_check.py --strict

Exit codes:
    0  — sequence locked (verdict == READY)
    1  — sequence not locked (verdict == NOT_READY)
    2  — bad CLI arguments
```

## Imports

`Iterable`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_aggregate`, `_any_phrase_present`, `_build_parser`, `_check`, `_now_iso`, `_operator_actions`, `_print_summary`, `_read_text`, `_write_report`, `check_blockers_named`, `check_doctrine_phrases`, `check_existing_memory_review_docs`, `check_no_env_read`, `check_no_new_memory_review_doc_required`, `check_offlimits_present`, `check_pas159_audit_reference`, `check_pas160_docs_exist`, `check_phase_tokens_in_sequence_doc`, `check_prior_readiness_checkers`, `evaluate`, `main`

## Env-key candidates

`BLOCK`, `FAIL`, `INFO`, `NOT_READY`, `PAS160`, `PASS`, `READY`

## String constants (redacted where noted)

- '\nPAS160 — Production MVP doctrine + sequence lock gate.\n\nDeterministic, non-mutating evaluator for "is the locked\nPAS161→PAS170 MVP sequence on file and self-consistent?".\nWalks the repo, confirms the PAS160 doctrine + sequence\ndocuments exist, confirms each phase PAS161 → PAS170 is named\nin the sequence doc, confirms the five hard MVP blockers are\neach called out by name in at least one of the docs, confirms\nthe doctrine carries every required freeze / safety clause\n(Memory Review frozen, TrustClaw audit-first, no production\ndata, no migrations in PAS160), and confirms that the prior-\nphase readiness checkers it depends on (PAS145, PAS158) are\nstill present. Emits a verdict (READY / NOT_READY) plus a\nmachine-readable ``pas160_mvp_sequence_check_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas160_mvp_sequence_check.py\n  python scripts/pas160_mvp_sequence_check.py --json\n  python scripts/pas160_mvp_sequence_check.py --summary-only\n  python scripts/pas160_mvp_sequence_check.py --strict\n\nExit codes:\n    0  — sequence locked (verdict == READY)\n    1  — sequence not locked (verdict == NOT_READY)\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'READY'
- 'NOT_READY'
- 'BLOCK'
- 'INFO'
- 'docs/pas159_production_brokerage_mvp_gap_audit.md'
- 'severity'
- 'detail'
- 'pas160_mvp_sequence_check_report.json'
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
- 'text'
- 'phrases'
- 'Iterable[str]'
- 'bool'
- 'Case-insensitive any-of search.'
- 'repo_root'
- 'List[dict]'
- 'pas160_doc:'
- 'PASS'
- 'FAIL'
- 'Required PAS160 doc present: '
- 'missing'
- 'prior_checker:'
- 'Prior-phase readiness checker present: '
- 'PAS159 was delivered as a synchronous audit response, not\na doc. If the doc form is also on disk, surface it; if not,\nemit an INFO row (does not block the verdict).'
- 'pas159_audit:'
- 'PAS159 audit doc (optional reference): '
- 'audit was delivered inline; doc form not on disk'
- "Confirm the PAS160 docs do NOT require a Memory Review\nphase beyond PAS158. We assert this structurally: the\nsequence-lock doc must NOT name a PAS147–PAS158-style\n'memory_review_*' phase as a follow-on feature deliverable.\n\nDetection rule: search the sequence doc for any reference\nto a 'memory_review' feature phase strictly later than\nPAS158. If found, FAIL.\n"
- 'docs'
- 'pas160_mvp_sequence_lock.md'
- 'no_new_memory_review_phase'
- 'Sequence doc does not require a new Memory Review feature phase beyond PAS158'
- 'forbidden tokens in sequence doc: '
- 'phase_token:'
- 'Sequence doc mentions '
- ' missing from sequence doc'
- 'Each of the five hard MVP blockers must be called out\nby name in EITHER the doctrine doc OR the sequence doc.'
- 'blocker_named:'
- 'Blocker called out by name: '
- 'expected one of: '
- ' | '
- 'Each doctrine clause must appear in at least one PAS160\ndoc. The match is case-insensitive any-of.'
- 'doctrine_phrase:'
- 'Doctrine clause present: '
- 'PAS147–PAS158 docs should still be on disk (the freeze\nlocks them as maintenance baseline). Missing → INFO, not\nBLOCK (the verdict is about the LOCK, not about the\nhistorical docs).'
- 'history_doc:'
- 'Historical Memory Review doc on disk: '
- 'missing — maintenance baseline incomplete'
- 'offlimits:'
- 'Off-limits file present (do not modify): '
- 'missing — restore from git history'
- 'Self-check: this script must NOT read .env, call\nSupabase, or import external vendor / embedding libraries.\nLine-level scan over our own source — banner / docstring\nreferences are allowed.'
- 'dotenv import'
- 'supabase import'
- 'external-vendor import'
- 'embedding / vector import'
- 'load_dotenv()'
- 'load_dotenv() call'
- 'environ read'
- 'self_check:no_env_or_vendor'
- 'PAS160 sequence checker never reads .env, calls Supabase, or imports vendor / embedding libs'
- 'disqualifying code-line patterns: '
- 'checks'
- 'verdict'
- 'blockers'
- 'info'
- 'List[str]'
- '[BLOCK] Required PAS160 doc missing: '
- ' — author or restore ('
- '[BLOCK] Prior-phase readiness checker missing: '
- '[BLOCK] Sequence doc missing phase mention: '
- '[BLOCK] Five-blocker list incomplete: '
- '[BLOCK] Doctrine clause missing: '
- '[BLOCK] Sequence doc reintroduces a Memory Review feature phase ('
- '[BLOCK] Off-limits file issue: '
- 'self_check:'
- '] PAS160 checker self-check failed: '
- '[INFO] '
- ' — '
- 'see report'
- 'phase'
- 'PAS160'
- 'generated_at'
- 'ready'
- 'blocker_count'
- 'info_count'
- 'check_count'
- 'pass_count'
- 'fail_count'
- 'operator_actions'
- 'argparse.ArgumentParser'
- 'pas160_mvp_sequence_check'
- 'PAS160 — Evaluate whether the production-MVP sequence lock (PAS161 → PAS170) is on file and self-consistent. Read-only. Does not touch Supabase, .env, or any tenant data.'
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
- '[PAS160] verdict='
- ' blockers='
- ' info='
- ' checks='
- ' pass='
- ' fail='
- '[PAS160] operator actions:'
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

   1           LOAD_CONST               0 ('\nPAS160 — Production MVP doctrine + sequence lock gate.\n\nDeterministic, non-mutating evaluator for "is the locked\nPAS161→PAS170 MVP sequence on file and self-consistent?".\nWalks the repo, confirms the PAS160 doctrine + sequence\ndocuments exist, confirms each phase PAS161 → PAS170 is named\nin the sequence doc, confirms the five hard MVP blockers are\neach called out by name in at least one of the docs, confirms\nthe doctrine carries every required freeze / safety clause\n(Memory Review frozen, TrustClaw audit-first, no production\ndata, no migrations in PAS160), and confirms that the prior-\nphase readiness checkers it depends on (PAS145, PAS158) are\nstill present. Emits a verdict (READY / NOT_READY) plus a\nmachine-readable ``pas160_mvp_sequence_check_report.json``.\n\nThis script never:\n  * modifies files,\n  * calls Supabase,\n  * reads .env / secrets,\n  * imports external vendors,\n  * imports embedding / vector libraries,\n  * touches the off-limits\n    ``scripts/combined_supabase_migration.sql``.\n\nUsage:\n  python scripts/pas160_mvp_sequence_check.py\n  python scripts/pas160_mvp_sequence_check.py --json\n  python scripts/pas160_mvp_sequence_check.py --summary-only\n  python scripts/pas160_mvp_sequence_check.py --strict\n\nExit codes:\n    0  — sequence locked (verdict == READY)\n    1  — sequence not locked (verdict == NOT_READY)\n    2  — bad CLI arguments\n')
               STORE_NAME               0 (__doc__)

  38           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              1 (__future__)
               IMPORT_FROM              2 (annotations)
               STORE_NAME               2 (annotations)
               POP_TOP

  40           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              3 (argparse)
               STORE_NAME               3 (argparse)

  41           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (json)
               STORE_NAME               4 (json)

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (os)
               STORE_NAME               5 (os)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (sys)
               STORE_NAME               6 (sys)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timezone)
               STORE_NAME               8 (timezone)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Path',))
               IMPORT_NAME              9 (pathlib)
               IMPORT_FROM             10 (Path)
               STORE_NAME              10 (Path)
               POP_TOP

  46           LOAD_SMALL_INT           0
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

  78           LOAD_CONST              61 (('docs/pas160_production_mvp_doctrine_freeze.md', 'docs/pas160_mvp_sequence_lock.md'))
               STORE_NAME              30 (REQUIRED_PAS160_DOCS)

  83           LOAD_CONST              62 (('scripts/pas145_mvp_readiness_check.py', 'scripts/pas158_memory_review_readiness_check.py'))
               STORE_NAME              31 (REQUIRED_PRIOR_READINESS_CHECKERS)

  90           LOAD_CONST              13 ('docs/pas159_production_brokerage_mvp_gap_audit.md')
               STORE_NAME              32 (OPTIONAL_PAS159_AUDIT_DOC)

  94           LOAD_CONST              63 (('PAS161', 'PAS162', 'PAS163', 'PAS164', 'PAS165', 'PAS166', 'PAS167', 'PAS168', 'PAS169', 'PAS170'))
               STORE_NAME              33 (REQUIRED_PHASE_TOKENS)

 110           LOAD_CONST              64 ((('lead-ingestion', ('lead ingestion', 'Lead Ingestion')), ('brain-knowledge-ingestion', ('PAS Brain knowledge ingestion', 'Brain knowledge ingestion', 'Brain Knowledge Ingestion', 'knowledge ingestion')), ('memory-candidate-pipeline', ('memory candidate generation', 'Memory Candidate Generation', 'candidate generation pipeline', 'Memory Candidate Generation Pipeline')), ('google-calendar', ('Google Calendar', 'google calendar')), ('slack-employee-mode', ('Slack Employee Mode', 'Slack employee mode', 'employee-mode'))))
               STORE_NAME              34 (REQUIRED_BLOCKER_TOKENS)

 135           LOAD_CONST              65 ((('freeze', ('Memory Review expansion is frozen', 'Memory Review is frozen', 'Memory Review (PAS147–PAS158) is **frozen', 'is **frozen', 'frozen in maintenance', 'maintenance-only')), ('trustclaw-audit-first', ('audit-first', 'audit, not an integration', 'audit-first per', 'TrustClaw / Composio is audit-first')), ('no-production-data', ('No production data touched', 'no production data touched', 'production data touched')), ('no-migrations-in-pas160', ('No migrations', 'no migrations', 'without a phase-specific runbook'))))
               STORE_NAME              35 (REQUIRED_DOCTRINE_PHRASES)

 161           LOAD_CONST              66 (('docs/pas147_operator_memory_review_console.md', 'docs/pas148_operator_memory_review_ui.md', 'docs/pas149_memory_review_history.md', 'docs/pas150_memory_review_stats.md', 'docs/pas151_memory_review_timeseries.md', 'docs/pas152_memory_review_csv_export.md', 'docs/pas153_memory_review_csv_filters.md', 'docs/pas154_memory_review_actor_catalog.md', 'docs/pas155_memory_review_operator_alerts.md', 'docs/pas156_memory_review_alert_bookmarks.md', 'docs/pas157_memory_review_help_layer.md', 'docs/pas158_memory_review_operations_runbook.md', 'docs/pas158_demo_simulation_checklist.md'))
               STORE_NAME              36 (EXISTING_MEMORY_REVIEW_DOCS)

 180           LOAD_CONST              67 (('scripts/combined_supabase_migration.sql',))
               STORE_NAME              37 (OFFLIMITS_FILES)

 189           LOAD_CONST              14 ('severity')

 194           LOAD_NAME               28 (SEVERITY_BLOCK)

 189           LOAD_CONST              15 ('detail')

 195           LOAD_CONST              16 ('')

 189           BUILD_MAP                2
               LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18025030, file "scripts/pas160_mvp_sequence_check.py", line 189>)
               MAKE_FUNCTION
               LOAD_CONST              18 (<code object _check at 0x0000018C17FA2F10, file "scripts/pas160_mvp_sequence_check.py", line 189>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (_check)

 206           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts/pas160_mvp_sequence_check.py", line 206>)
               MAKE_FUNCTION
               LOAD_CONST              20 (<code object _now_iso at 0x0000018C180388F0, file "scripts/pas160_mvp_sequence_check.py", line 206>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_now_iso)

 210           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas160_mvp_sequence_check.py", line 210>)
               MAKE_FUNCTION
               LOAD_CONST              22 (<code object _read_text at 0x0000018C18052F70, file "scripts/pas160_mvp_sequence_check.py", line 210>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (_read_text)

 217           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18024C30, file "scripts/pas160_mvp_sequence_check.py", line 217>)
               MAKE_FUNCTION
               LOAD_CONST              24 (<code object _any_phrase_present at 0x0000018C17FE13E0, file "scripts/pas160_mvp_sequence_check.py", line 217>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              41 (_any_phrase_present)

 232           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas160_mvp_sequence_check.py", line 232>)
               MAKE_FUNCTION
               LOAD_CONST              26 (<code object check_pas160_docs_exist at 0x0000018C18060DB0, file "scripts/pas160_mvp_sequence_check.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (check_pas160_docs_exist)

 246           LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas160_mvp_sequence_check.py", line 246>)
               MAKE_FUNCTION
               LOAD_CONST              28 (<code object check_prior_readiness_checkers at 0x0000018C18060A50, file "scripts/pas160_mvp_sequence_check.py", line 246>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (check_prior_readiness_checkers)

 260           LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas160_mvp_sequence_check.py", line 260>)
               MAKE_FUNCTION
               LOAD_CONST              30 (<code object check_pas159_audit_reference at 0x0000018C17FA92F0, file "scripts/pas160_mvp_sequence_check.py", line 260>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (check_pas159_audit_reference)

 275           LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas160_mvp_sequence_check.py", line 275>)
               MAKE_FUNCTION
               LOAD_CONST              32 (<code object check_no_new_memory_review_doc_required at 0x0000018C17D77E00, file "scripts/pas160_mvp_sequence_check.py", line 275>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (check_no_new_memory_review_doc_required)

 320           LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas160_mvp_sequence_check.py", line 320>)
               MAKE_FUNCTION
               LOAD_CONST              34 (<code object check_phase_tokens_in_sequence_doc at 0x0000018C179C3A50, file "scripts/pas160_mvp_sequence_check.py", line 320>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (check_phase_tokens_in_sequence_doc)

 336           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas160_mvp_sequence_check.py", line 336>)
               MAKE_FUNCTION
               LOAD_CONST              36 (<code object check_blockers_named at 0x0000018C17F73C50, file "scripts/pas160_mvp_sequence_check.py", line 336>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (check_blockers_named)

 357           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas160_mvp_sequence_check.py", line 357>)
               MAKE_FUNCTION
               LOAD_CONST              38 (<code object check_doctrine_phrases at 0x0000018C17F73470, file "scripts/pas160_mvp_sequence_check.py", line 357>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (check_doctrine_phrases)

 378           LOAD_CONST              39 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas160_mvp_sequence_check.py", line 378>)
               MAKE_FUNCTION
               LOAD_CONST              40 (<code object check_existing_memory_review_docs at 0x0000018C18060C00, file "scripts/pas160_mvp_sequence_check.py", line 378>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (check_existing_memory_review_docs)

 396           LOAD_CONST              41 (<code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas160_mvp_sequence_check.py", line 396>)
               MAKE_FUNCTION
               LOAD_CONST              42 (<code object check_offlimits_present at 0x0000018C18060390, file "scripts/pas160_mvp_sequence_check.py", line 396>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (check_offlimits_present)

 410           LOAD_CONST              43 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas160_mvp_sequence_check.py", line 410>)
               MAKE_FUNCTION
               LOAD_CONST              44 (<code object check_no_env_read at 0x0000018C181B4AE0, file "scripts/pas160_mvp_sequence_check.py", line 410>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (check_no_env_read)

 462           LOAD_CONST              45 (<code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas160_mvp_sequence_check.py", line 462>)
               MAKE_FUNCTION
               LOAD_CONST              46 (<code object _aggregate at 0x0000018C17EC4B00, file "scripts/pas160_mvp_sequence_check.py", line 462>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (_aggregate)

 475           LOAD_CONST              47 (<code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas160_mvp_sequence_check.py", line 475>)
               MAKE_FUNCTION
               LOAD_CONST              48 (<code object _operator_actions at 0x0000018C17D8BF50, file "scripts/pas160_mvp_sequence_check.py", line 475>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              53 (_operator_actions)

 533           LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas160_mvp_sequence_check.py", line 533>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object evaluate at 0x0000018C17F63670, file "scripts/pas160_mvp_sequence_check.py", line 533>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (evaluate)

 567           LOAD_CONST              51 ('pas160_mvp_sequence_check_report.json')
               STORE_NAME              55 (REPORT_FILENAME)

 570           LOAD_CONST              52 (<code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas160_mvp_sequence_check.py", line 570>)
               MAKE_FUNCTION
               LOAD_CONST              53 (<code object _build_parser at 0x0000018C1801CDC0, file "scripts/pas160_mvp_sequence_check.py", line 570>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (_build_parser)

 608           LOAD_CONST              54 (<code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas160_mvp_sequence_check.py", line 608>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object _print_summary at 0x0000018C17D8D460, file "scripts/pas160_mvp_sequence_check.py", line 608>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (_print_summary)

 626           LOAD_CONST              56 (<code object __annotate__ at 0x0000018C18026430, file "scripts/pas160_mvp_sequence_check.py", line 626>)
               MAKE_FUNCTION
               LOAD_CONST              57 (<code object _write_report at 0x0000018C18104210, file "scripts/pas160_mvp_sequence_check.py", line 626>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              58 (_write_report)

 640           LOAD_CONST              68 ((None,))
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C180FC030, file "scripts/pas160_mvp_sequence_check.py", line 640>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object main at 0x0000018C17F84690, file "scripts/pas160_mvp_sequence_check.py", line 640>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              59 (main)

 668           LOAD_NAME               60 (__name__)
               LOAD_CONST              60 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       26 (to L5)
               NOT_TAKEN

 669           LOAD_NAME                6 (sys)
               LOAD_ATTR              122 (exit)
               PUSH_NULL
               LOAD_NAME               59 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               POP_TOP
               LOAD_CONST               2 (None)
               RETURN_VALUE

 668   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  54           LOAD_NAME               19 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  55   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          309 (to L1)

  54   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "scripts/pas160_mvp_sequence_check.py", line 189>:
189           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('check_id')

190           LOAD_CONST               2 ('str')

189           LOAD_CONST               3 ('status')

191           LOAD_CONST               2 ('str')

189           LOAD_CONST               4 ('label')

192           LOAD_CONST               2 ('str')

189           LOAD_CONST               5 ('severity')

194           LOAD_CONST               2 ('str')

189           LOAD_CONST               6 ('detail')

195           LOAD_CONST               2 ('str')

189           LOAD_CONST               7 ('return')

196           LOAD_CONST               8 ('dict')

189           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object _check at 0x0000018C17FA2F10, file "scripts/pas160_mvp_sequence_check.py", line 189>:
189           RESUME                   0

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

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts/pas160_mvp_sequence_check.py", line 206>:
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

Disassembly of <code object _now_iso at 0x0000018C180388F0, file "scripts/pas160_mvp_sequence_check.py", line 206>:
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

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts/pas160_mvp_sequence_check.py", line 210>:
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

Disassembly of <code object _read_text at 0x0000018C18052F70, file "scripts/pas160_mvp_sequence_check.py", line 210>:
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "scripts/pas160_mvp_sequence_check.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('text')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('phrases')
              LOAD_CONST               4 ('Iterable[str]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _any_phrase_present at 0x0000018C17FE13E0, file "scripts/pas160_mvp_sequence_check.py", line 217>:
217           RESUME                   0

219           LOAD_FAST_BORROW         0 (text)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

220           LOAD_CONST               1 (False)
              RETURN_VALUE

221   L1:     LOAD_FAST_BORROW         0 (text)
              LOAD_ATTR                1 (lower + NULL|self)
              CALL                     0
              STORE_FAST               2 (lower)

222           LOAD_FAST_BORROW         1 (phrases)
              GET_ITER
      L2:     FOR_ITER                27 (to L4)
              STORE_FAST               3 (phrase)

223           LOAD_FAST_BORROW         3 (phrase)
              LOAD_ATTR                1 (lower + NULL|self)
              CALL                     0
              LOAD_FAST_BORROW         2 (lower)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           26 (to L2)

224   L3:     POP_TOP
              LOAD_CONST               2 (True)
              RETURN_VALUE

222   L4:     END_FOR
              POP_ITER

225           LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts/pas160_mvp_sequence_check.py", line 232>:
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

Disassembly of <code object check_pas160_docs_exist at 0x0000018C18060DB0, file "scripts/pas160_mvp_sequence_check.py", line 232>:
232           RESUME                   0

233           BUILD_LIST               0
              STORE_FAST               1 (out)

234           LOAD_GLOBAL              0 (REQUIRED_PAS160_DOCS)
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

237           LOAD_CONST               0 ('pas160_doc:')
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

239   L3:     LOAD_CONST               3 ('Required PAS160 doc present: ')
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
      L4:     LOAD_CONST               5 ('missing')

236   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

234   L6:     END_FOR
              POP_ITER

243           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts/pas160_mvp_sequence_check.py", line 246>:
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

Disassembly of <code object check_prior_readiness_checkers at 0x0000018C18060A50, file "scripts/pas160_mvp_sequence_check.py", line 246>:
246           RESUME                   0

247           BUILD_LIST               0
              STORE_FAST               1 (out)

248           LOAD_GLOBAL              0 (REQUIRED_PRIOR_READINESS_CHECKERS)
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

251           LOAD_CONST               0 ('prior_checker:')
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

253   L3:     LOAD_CONST               3 ('Prior-phase readiness checker present: ')
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
      L4:     LOAD_CONST               5 ('missing')

250   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

248   L6:     END_FOR
              POP_ITER

257           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts/pas160_mvp_sequence_check.py", line 260>:
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

Disassembly of <code object check_pas159_audit_reference at 0x0000018C17FA92F0, file "scripts/pas160_mvp_sequence_check.py", line 260>:
260           RESUME                   0

264           LOAD_GLOBAL              0 (OPTIONAL_PAS159_AUDIT_DOC)
              STORE_FAST               1 (p)

265           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         1 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               2 (ok)

266           LOAD_GLOBAL              7 (_check + NULL)

267           LOAD_CONST               1 ('pas159_audit:')
              LOAD_FAST_BORROW         1 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

268           LOAD_FAST_BORROW         2 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               3 ('FAIL')

269   L2:     LOAD_CONST               4 ('PAS159 audit doc (optional reference): ')
              LOAD_FAST_BORROW         1 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

270           LOAD_GLOBAL              8 (SEVERITY_INFO)

271           LOAD_FAST_BORROW         2 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L3)
              NOT_TAKEN
              LOAD_CONST               5 ('')

266           LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              BUILD_LIST               1
              RETURN_VALUE

271   L3:     LOAD_CONST               6 ('audit was delivered inline; doc form not on disk')

266           LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              BUILD_LIST               1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3D20, file "scripts/pas160_mvp_sequence_check.py", line 275>:
275           RESUME                   0
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

Disassembly of <code object check_no_new_memory_review_doc_required at 0x0000018C17D77E00, file "scripts/pas160_mvp_sequence_check.py", line 275>:
 275            RESUME                   0

 285            BUILD_LIST               0
                STORE_FAST               1 (out)

 286            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_FAST_BORROW         0 (repo_root)
                CALL                     1
                LOAD_CONST               1 ('docs')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('pas160_mvp_sequence_lock.md')
                BINARY_OP               11 (/)
                STORE_FAST               2 (seq_doc)

 287            LOAD_GLOBAL              3 (_read_text + NULL)
                LOAD_FAST_BORROW         2 (seq_doc)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               3 ('')
        L1:     STORE_FAST               3 (src)

 288            LOAD_CONST              11 (('memory_review_phase', 'pas159_memory_review', 'pas160_memory_review', 'pas161_memory_review', 'pas162_memory_review', 'pas163_memory_review', 'pas164_memory_review', 'pas165_memory_review', 'pas166_memory_review', 'pas167_memory_review', 'pas168_memory_review', 'pas169_memory_review', 'pas170_memory_review'))
                STORE_FAST               4 (forbidden_substrings)

 306            LOAD_FAST_BORROW         3 (src)
                LOAD_ATTR                5 (lower + NULL|self)
                CALL                     0
                STORE_FAST               5 (lower)

 307            LOAD_FAST_BORROW         4 (forbidden_substrings)
                GET_ITER
                LOAD_FAST_AND_CLEAR      6 (s)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2
        L3:     FOR_ITER                13 (to L6)
                STORE_FAST_LOAD_FAST   102 (s, s)
                LOAD_FAST_BORROW         5 (lower)
                CONTAINS_OP              0 (in)
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L3)
        L5:     LOAD_FAST_BORROW         6 (s)
                LIST_APPEND              2
                JUMP_BACKWARD           15 (to L3)
        L6:     END_FOR
                POP_ITER
        L7:     STORE_FAST               7 (bad)
                STORE_FAST               6 (s)

 308            LOAD_FAST                1 (out)
                LOAD_ATTR                7 (append + NULL|self)
                LOAD_GLOBAL              9 (_check + NULL)

 309            LOAD_CONST               4 ('no_new_memory_review_phase')

 310            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN
                LOAD_CONST               5 ('FAIL')
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               6 ('PASS')

 311    L9:     LOAD_CONST               7 ('Sequence doc does not require a new Memory Review feature phase beyond PAS158')

 313            LOAD_GLOBAL             10 (SEVERITY_BLOCK)

 315            LOAD_FAST_BORROW         7 (bad)
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L10)
                NOT_TAKEN

 314            LOAD_CONST               8 ('forbidden tokens in sequence doc: ')
                LOAD_CONST               9 (', ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST_BORROW         7 (bad)
                CALL                     1
                BINARY_OP                0 (+)
                JUMP_FORWARD             1 (to L11)

 315   L10:     LOAD_CONST               3 ('')

 308   L11:     LOAD_CONST              10 (('severity', 'detail'))
                CALL_KW                  5
                CALL                     1
                POP_TOP

 317            LOAD_FAST_BORROW         1 (out)
                RETURN_VALUE

  --   L12:     SWAP                     2
                POP_TOP

 307            SWAP                     2
                STORE_FAST               6 (s)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L12 [2]
  L5 to L7 -> L12 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA1D40, file "scripts/pas160_mvp_sequence_check.py", line 320>:
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

Disassembly of <code object check_phase_tokens_in_sequence_doc at 0x0000018C179C3A50, file "scripts/pas160_mvp_sequence_check.py", line 320>:
320           RESUME                   0

321           BUILD_LIST               0
              STORE_FAST               1 (out)

322           LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_CONST               0 ('docs')
              BINARY_OP               11 (/)
              LOAD_CONST               1 ('pas160_mvp_sequence_lock.md')
              BINARY_OP               11 (/)
              STORE_FAST               2 (seq_doc)

323           LOAD_GLOBAL              3 (_read_text + NULL)
              LOAD_FAST_BORROW         2 (seq_doc)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               2 ('')
      L1:     STORE_FAST               3 (src)

324           LOAD_GLOBAL              4 (REQUIRED_PHASE_TOKENS)
              GET_ITER
      L2:     FOR_ITER                71 (to L7)
              STORE_FAST               4 (token)

325           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (token, src)
              CONTAINS_OP              0 (in)
              STORE_FAST               5 (ok)

326           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

327           LOAD_CONST               3 ('phase_token:')
              LOAD_FAST_BORROW         4 (token)
              FORMAT_SIMPLE
              BUILD_STRING             2

328           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L4)
      L3:     LOAD_CONST               5 ('FAIL')

329   L4:     LOAD_CONST               6 ('Sequence doc mentions ')
              LOAD_FAST_BORROW         4 (token)
              FORMAT_SIMPLE
              BUILD_STRING             2

330           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

331           LOAD_FAST_BORROW         5 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN
              LOAD_CONST               2 ('')
              JUMP_FORWARD             4 (to L6)
      L5:     LOAD_FAST_BORROW         4 (token)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' missing from sequence doc')
              BUILD_STRING             2

326   L6:     LOAD_CONST               8 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           73 (to L2)

324   L7:     END_FOR
              POP_ITER

333           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "scripts/pas160_mvp_sequence_check.py", line 336>:
336           RESUME                   0
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

Disassembly of <code object check_blockers_named at 0x0000018C17F73C50, file "scripts/pas160_mvp_sequence_check.py", line 336>:
336           RESUME                   0

339           BUILD_LIST               0
              STORE_FAST               1 (out)

340           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (REQUIRED_PAS160_DOCS)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               2 (doctrine)

341           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (REQUIRED_PAS160_DOCS)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L2:     STORE_FAST               3 (sequence)

342           LOAD_FAST_BORROW         2 (doctrine)
              LOAD_CONST               2 ('\n')
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         3 (sequence)
              BINARY_OP                0 (+)
              STORE_FAST               4 (combined)

343           LOAD_GLOBAL              6 (REQUIRED_BLOCKER_TOKENS)
              GET_ITER
      L3:     FOR_ITER                99 (to L8)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   86 (name, phrases)

344           LOAD_GLOBAL              9 (_any_phrase_present + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (combined, phrases)
              CALL                     2
              STORE_FAST               7 (ok)

345           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

346           LOAD_CONST               3 ('blocker_named:')
              LOAD_FAST_BORROW         5 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

347           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('FAIL')

348   L5:     LOAD_CONST               6 ('Blocker called out by name: ')
              LOAD_FAST_BORROW         5 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

349           LOAD_GLOBAL             14 (SEVERITY_BLOCK)

350           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD            23 (to L7)

351   L6:     LOAD_CONST               7 ('expected one of: ')
              LOAD_CONST               8 (' | ')
              LOAD_ATTR               17 (join + NULL|self)
              LOAD_FAST_BORROW         6 (phrases)
              CALL                     1
              BINARY_OP                0 (+)

345   L7:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          101 (to L3)

343   L8:     END_FOR
              POP_ITER

354           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts/pas160_mvp_sequence_check.py", line 357>:
357           RESUME                   0
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

Disassembly of <code object check_doctrine_phrases at 0x0000018C17F73470, file "scripts/pas160_mvp_sequence_check.py", line 357>:
357           RESUME                   0

360           BUILD_LIST               0
              STORE_FAST               1 (out)

361           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (REQUIRED_PAS160_DOCS)
              LOAD_SMALL_INT           0
              BINARY_OP               26 ([])
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L1:     STORE_FAST               2 (doctrine)

362           LOAD_GLOBAL              1 (_read_text + NULL)
              LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_GLOBAL              4 (REQUIRED_PAS160_DOCS)
              LOAD_SMALL_INT           1
              BINARY_OP               26 ([])
              BINARY_OP               11 (/)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 ('')
      L2:     STORE_FAST               3 (sequence)

363           LOAD_FAST_BORROW         2 (doctrine)
              LOAD_CONST               2 ('\n')
              BINARY_OP                0 (+)
              LOAD_FAST_BORROW         3 (sequence)
              BINARY_OP                0 (+)
              STORE_FAST               4 (combined)

364           LOAD_GLOBAL              6 (REQUIRED_DOCTRINE_PHRASES)
              GET_ITER
      L3:     FOR_ITER                99 (to L8)
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   86 (name, phrases)

365           LOAD_GLOBAL              9 (_any_phrase_present + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (combined, phrases)
              CALL                     2
              STORE_FAST               7 (ok)

366           LOAD_FAST                1 (out)
              LOAD_ATTR               11 (append + NULL|self)
              LOAD_GLOBAL             13 (_check + NULL)

367           LOAD_CONST               3 ('doctrine_phrase:')
              LOAD_FAST_BORROW         5 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

368           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('PASS')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('FAIL')

369   L5:     LOAD_CONST               6 ('Doctrine clause present: ')
              LOAD_FAST_BORROW         5 (name)
              FORMAT_SIMPLE
              BUILD_STRING             2

370           LOAD_GLOBAL             14 (SEVERITY_BLOCK)

371           LOAD_FAST_BORROW         7 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              LOAD_CONST               1 ('')
              JUMP_FORWARD            23 (to L7)

372   L6:     LOAD_CONST               7 ('expected one of: ')
              LOAD_CONST               8 (' | ')
              LOAD_ATTR               17 (join + NULL|self)
              LOAD_FAST_BORROW         6 (phrases)
              CALL                     1
              BINARY_OP                0 (+)

366   L7:     LOAD_CONST               9 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          101 (to L3)

364   L8:     END_FOR
              POP_ITER

375           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts/pas160_mvp_sequence_check.py", line 378>:
378           RESUME                   0
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

Disassembly of <code object check_existing_memory_review_docs at 0x0000018C18060C00, file "scripts/pas160_mvp_sequence_check.py", line 378>:
378           RESUME                   0

383           BUILD_LIST               0
              STORE_FAST               1 (out)

384           LOAD_GLOBAL              0 (EXISTING_MEMORY_REVIEW_DOCS)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

385           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

386           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

387           LOAD_CONST               1 ('history_doc:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

388           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               2 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               3 ('FAIL')

389   L3:     LOAD_CONST               4 ('Historical Memory Review doc on disk: ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

390           LOAD_GLOBAL             10 (SEVERITY_INFO)

391           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               5 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               6 ('missing — maintenance baseline incomplete')

386   L5:     LOAD_CONST               7 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

384   L6:     END_FOR
              POP_ITER

393           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "scripts/pas160_mvp_sequence_check.py", line 396>:
396           RESUME                   0
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

Disassembly of <code object check_offlimits_present at 0x0000018C18060390, file "scripts/pas160_mvp_sequence_check.py", line 396>:
396           RESUME                   0

397           BUILD_LIST               0
              STORE_FAST               1 (out)

398           LOAD_GLOBAL              0 (OFFLIMITS_FILES)
              GET_ITER
      L1:     FOR_ITER                96 (to L6)
              STORE_FAST               2 (p)

399           LOAD_GLOBAL              3 (Path + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              LOAD_FAST_BORROW         2 (p)
              BINARY_OP               11 (/)
              LOAD_ATTR                5 (is_file + NULL|self)
              CALL                     0
              STORE_FAST               3 (ok)

400           LOAD_FAST                1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_GLOBAL              9 (_check + NULL)

401           LOAD_CONST               0 ('offlimits:')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

402           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_CONST               1 ('PASS')
              JUMP_FORWARD             1 (to L3)
      L2:     LOAD_CONST               2 ('FAIL')

403   L3:     LOAD_CONST               3 ('Off-limits file present (do not modify): ')
              LOAD_FAST_BORROW         2 (p)
              FORMAT_SIMPLE
              BUILD_STRING             2

404           LOAD_GLOBAL             10 (SEVERITY_BLOCK)

405           LOAD_FAST_BORROW         3 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              LOAD_CONST               4 ('')
              JUMP_FORWARD             1 (to L5)
      L4:     LOAD_CONST               5 ('missing — restore from git history')

400   L5:     LOAD_CONST               6 (('severity', 'detail'))
              CALL_KW                  5
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           98 (to L1)

398   L6:     END_FOR
              POP_ITER

407           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts/pas160_mvp_sequence_check.py", line 410>:
410           RESUME                   0
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

Disassembly of <code object check_no_env_read at 0x0000018C181B4AE0, file "scripts/pas160_mvp_sequence_check.py", line 410>:
410            RESUME                   0

415            BUILD_LIST               0
               STORE_FAST               1 (out)

416            LOAD_GLOBAL              1 (Path + NULL)
               LOAD_GLOBAL              2 (__file__)
               CALL                     1
               LOAD_ATTR                5 (resolve + NULL|self)
               CALL                     0
               STORE_FAST               2 (self_path)

417            LOAD_GLOBAL              7 (_read_text + NULL)
               LOAD_FAST_BORROW         2 (self_path)
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               1 ('')
       L1:     STORE_FAST               3 (src)

419            BUILD_LIST               0
               STORE_FAST               4 (bad)

420            LOAD_FAST_BORROW         3 (src)
               LOAD_ATTR                9 (splitlines + NULL|self)
               CALL                     0
               GET_ITER
       L2:     EXTENDED_ARG             1
               FOR_ITER               311 (to L11)
               STORE_FAST               5 (raw_line)

421            LOAD_FAST_BORROW         5 (raw_line)
               LOAD_ATTR               11 (strip + NULL|self)
               CALL                     0
               STORE_FAST               6 (stripped)

422            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               2 ('#')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

423            JUMP_BACKWARD           45 (to L2)

424    L3:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              17 (('import dotenv', 'from dotenv'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

425            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               3 ('dotenv import')
               CALL                     1
               POP_TOP

426    L4:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              18 (('import supabase', 'from supabase'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

427            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               4 ('supabase import')
               CALL                     1
               POP_TOP

428    L5:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              19 (('import composio', 'from composio', 'import trustclaw', 'from trustclaw'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

432            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               5 ('external-vendor import')
               CALL                     1
               POP_TOP

433    L6:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              20 (('import numpy', 'import faiss', 'import pgvector', 'from pgvector', 'from openai import embeddings', 'from openai.embeddings'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L7)
               NOT_TAKEN

439            LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               6 ('embedding / vector import')
               CALL                     1
               POP_TOP

440    L7:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST               7 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        24 (to L8)
               NOT_TAKEN

441            LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               17 (endswith + NULL|self)
               LOAD_CONST               7 ('load_dotenv()')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L9)
               NOT_TAKEN

442    L8:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               8 ('load_dotenv() call')
               CALL                     1
               POP_TOP

443    L9:     LOAD_FAST_BORROW         6 (stripped)
               LOAD_ATTR               13 (startswith + NULL|self)
               LOAD_CONST              21 (('os.environ[', 'os.getenv(', 'getenv('))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         4 (to L10)
               NOT_TAKEN
               EXTENDED_ARG             1
               JUMP_BACKWARD          294 (to L2)

444   L10:     LOAD_FAST_BORROW         4 (bad)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_CONST               9 ('environ read')
               CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          314 (to L2)

420   L11:     END_FOR
               POP_ITER

446            LOAD_FAST                1 (out)
               LOAD_ATTR               15 (append + NULL|self)
               LOAD_GLOBAL             19 (_check + NULL)

447            LOAD_CONST              10 ('self_check:no_env_or_vendor')

448            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE        3 (to L12)
               NOT_TAKEN
               LOAD_CONST              11 ('FAIL')
               JUMP_FORWARD             1 (to L13)
      L12:     LOAD_CONST              12 ('PASS')

449   L13:     LOAD_CONST              13 ('PAS160 sequence checker never reads .env, calls Supabase, or imports vendor / embedding libs')

451            LOAD_GLOBAL             20 (SEVERITY_BLOCK)

453            LOAD_FAST_BORROW         4 (bad)
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L14)
               NOT_TAKEN

452            LOAD_CONST              14 ('disqualifying code-line patterns: ')
               LOAD_CONST              15 (', ')
               LOAD_ATTR               23 (join + NULL|self)
               LOAD_FAST_BORROW         4 (bad)
               CALL                     1
               BINARY_OP                0 (+)
               JUMP_FORWARD             1 (to L15)

453   L14:     LOAD_CONST               1 ('')

446   L15:     LOAD_CONST              16 (('severity', 'detail'))
               CALL_KW                  5
               CALL                     1
               POP_TOP

455            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA1E30, file "scripts/pas160_mvp_sequence_check.py", line 462>:
462           RESUME                   0
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

Disassembly of <code object _aggregate at 0x0000018C17EC4B00, file "scripts/pas160_mvp_sequence_check.py", line 462>:
 462            RESUME                   0

 464            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 463            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L1:     BUILD_LIST               0
                SWAP                     2

 464    L2:     FOR_ITER                49 (to L7)
                STORE_FAST               1 (c)

 465            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 464    L3:     POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L2)

 465    L4:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              2 (SEVERITY_BLOCK)
                COMPARE_OP              88 (bool(==))

 464    L5:     POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L2)
        L6:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L2)
        L7:     END_FOR
                POP_ITER

 463    L8:     STORE_FAST               2 (blockers)
                STORE_FAST               1 (c)

 468            LOAD_FAST_BORROW         0 (checks)
                GET_ITER

 467            LOAD_FAST_AND_CLEAR      1 (c)
                SWAP                     2
        L9:     BUILD_LIST               0
                SWAP                     2

 468   L10:     FOR_ITER                49 (to L15)
                STORE_FAST               1 (c)

 469            LOAD_FAST_BORROW         1 (c)
                LOAD_CONST               0 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               1 ('FAIL')
                COMPARE_OP              88 (bool(==))

 468   L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           19 (to L10)

 469   L12:     LOAD_FAST_BORROW         1 (c)
                LOAD_ATTR                1 (get + NULL|self)
                LOAD_CONST               2 ('severity')
                CALL                     1
                LOAD_GLOBAL              4 (SEVERITY_INFO)
                COMPARE_OP              88 (bool(==))

 468   L13:     POP_JUMP_IF_TRUE         3 (to L14)
                NOT_TAKEN
                JUMP_BACKWARD           47 (to L10)
       L14:     LOAD_FAST_BORROW         1 (c)
                LIST_APPEND              2
                JUMP_BACKWARD           51 (to L10)
       L15:     END_FOR
                POP_ITER

 467   L16:     STORE_FAST               3 (info)
                STORE_FAST               1 (c)

 471            LOAD_FAST_BORROW         2 (blockers)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L17)
                NOT_TAKEN
                LOAD_GLOBAL              6 (VERDICT_NOT_READY)
                JUMP_FORWARD             5 (to L18)
       L17:     LOAD_GLOBAL              8 (VERDICT_READY)
       L18:     STORE_FAST               4 (verdict)

 472            LOAD_CONST               3 ('verdict')
                LOAD_FAST_BORROW         4 (verdict)
                LOAD_CONST               4 ('blockers')
                LOAD_FAST_BORROW         2 (blockers)
                LOAD_CONST               5 ('info')
                LOAD_FAST_BORROW         3 (info)
                BUILD_MAP                3
                RETURN_VALUE

  --   L19:     SWAP                     2
                POP_TOP

 463            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0

  --   L20:     SWAP                     2
                POP_TOP

 467            SWAP                     2
                STORE_FAST               1 (c)
                RERAISE                  0
ExceptionTable:
  L1 to L3 -> L19 [2]
  L4 to L5 -> L19 [2]
  L6 to L8 -> L19 [2]
  L9 to L11 -> L20 [2]
  L12 to L13 -> L20 [2]
  L14 to L16 -> L20 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "scripts/pas160_mvp_sequence_check.py", line 475>:
475           RESUME                   0
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

Disassembly of <code object _operator_actions at 0x0000018C17D8BF50, file "scripts/pas160_mvp_sequence_check.py", line 475>:
475            RESUME                   0

476            BUILD_LIST               0
               STORE_FAST               1 (out)

477            LOAD_FAST_BORROW         0 (checks)
               GET_ITER
       L1:     EXTENDED_ARG             2
               FOR_ITER               581 (to L16)
               STORE_FAST               2 (c)

478            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               0 ('status')
               BINARY_OP               26 ([])
               LOAD_CONST               1 ('FAIL')
               COMPARE_OP             119 (bool(!=))
               POP_JUMP_IF_FALSE        3 (to L2)
               NOT_TAKEN

479            JUMP_BACKWARD           20 (to L1)

480    L2:     LOAD_FAST_BORROW         2 (c)
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

481            LOAD_FAST_BORROW         2 (c)
               LOAD_CONST               3 ('id')
               BINARY_OP               26 ([])
               STORE_FAST               4 (cid)

482            LOAD_FAST_BORROW         2 (c)
               LOAD_ATTR                1 (get + NULL|self)
               LOAD_CONST               4 ('detail')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               5 ('')
       L4:     STORE_FAST               5 (detail)

483            LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST               6 ('pas160_doc:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L5)
               NOT_TAKEN

484            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

485            LOAD_CONST               7 ('[BLOCK] Required PAS160 doc missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST               8 (' — author or restore (')

486            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

485            BUILD_STRING             5

484            CALL                     1
               POP_TOP
               JUMP_BACKWARD          136 (to L1)

488    L5:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              10 ('prior_checker:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L6)
               NOT_TAKEN

489            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

490            LOAD_CONST              11 ('[BLOCK] Prior-phase readiness checker missing: ')

491            LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

490            BUILD_STRING             5

489            CALL                     1
               POP_TOP
               JUMP_BACKWARD          185 (to L1)

493    L6:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              13 ('phase_token:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       27 (to L7)
               NOT_TAKEN

494            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

495            LOAD_CONST              14 ('[BLOCK] Sequence doc missing phase mention: ')

496            LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

495            BUILD_STRING             5

494            CALL                     1
               POP_TOP
               JUMP_BACKWARD          234 (to L1)

498    L7:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              15 ('blocker_named:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L8)
               NOT_TAKEN

499            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

500            LOAD_CONST              16 ('[BLOCK] Five-blocker list incomplete: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')

501            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

500            BUILD_STRING             5

499            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          284 (to L1)

503    L8:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              17 ('doctrine_phrase:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L9)
               NOT_TAKEN

504            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

505            LOAD_CONST              18 ('[BLOCK] Doctrine clause missing: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')

506            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

505            BUILD_STRING             5

504            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          334 (to L1)

508    L9:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              19 ('no_new_memory_review_phase')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       25 (to L10)
               NOT_TAKEN

509            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

510            LOAD_CONST              20 ('[BLOCK] Sequence doc reintroduces a Memory Review feature phase (')

511            LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

510            BUILD_STRING             3

509            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          381 (to L1)

513   L10:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              21 ('offlimits:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       28 (to L11)
               NOT_TAKEN

514            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

515            LOAD_CONST              22 ('[BLOCK] Off-limits file issue: ')
               LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')
               BUILD_STRING             5

514            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          431 (to L1)

517   L11:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              23 ('self_check:')
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       31 (to L12)
               NOT_TAKEN

518            LOAD_FAST_BORROW         1 (out)
               LOAD_ATTR                7 (append + NULL|self)

519            LOAD_CONST              24 ('[')
               LOAD_FAST_BORROW         3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST              25 ('] PAS160 checker self-check failed: ')

520            LOAD_FAST_BORROW         4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              12 (' (')
               LOAD_FAST_BORROW         5 (detail)
               FORMAT_SIMPLE
               LOAD_CONST               9 (').')

519            BUILD_STRING             7

518            CALL                     1
               POP_TOP
               EXTENDED_ARG             1
               JUMP_BACKWARD          484 (to L1)

522   L12:     LOAD_FAST_BORROW         4 (cid)
               LOAD_ATTR                5 (startswith + NULL|self)
               LOAD_CONST              31 (('pas159_audit:', 'history_doc:'))
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_FALSE       38 (to L14)
               NOT_TAKEN

523            LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)

524            LOAD_CONST              26 ('[INFO] ')
               LOAD_FAST                4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              27 (' — ')
               LOAD_FAST                5 (detail)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L13)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              28 ('see report')
      L13:     FORMAT_SIMPLE
               LOAD_CONST              29 ('.')
               BUILD_STRING             5

523            CALL                     1
               POP_TOP
               EXTENDED_ARG             2
               JUMP_BACKWARD          544 (to L1)

527   L14:     LOAD_FAST                1 (out)
               LOAD_ATTR                7 (append + NULL|self)

528            LOAD_CONST              24 ('[')
               LOAD_FAST                3 (sev)
               FORMAT_SIMPLE
               LOAD_CONST              30 ('] ')
               LOAD_FAST                4 (cid)
               FORMAT_SIMPLE
               LOAD_CONST              27 (' — ')
               LOAD_FAST                5 (detail)
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST              28 ('see report')
      L15:     FORMAT_SIMPLE
               LOAD_CONST              29 ('.')
               BUILD_STRING             7

527            CALL                     1
               POP_TOP
               EXTENDED_ARG             2
               JUMP_BACKWARD          584 (to L1)

477   L16:     END_FOR
               POP_ITER

530            LOAD_FAST_BORROW         1 (out)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "scripts/pas160_mvp_sequence_check.py", line 533>:
533           RESUME                   0
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

Disassembly of <code object evaluate at 0x0000018C17F63670, file "scripts/pas160_mvp_sequence_check.py", line 533>:
533           RESUME                   0

534           BUILD_LIST               0
              STORE_FAST               1 (checks)

535           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              3 (check_pas160_docs_exist + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

536           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              5 (check_prior_readiness_checkers + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

537           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              7 (check_pas159_audit_reference + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

538           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL              9 (check_no_new_memory_review_doc_required + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

539           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             11 (check_phase_tokens_in_sequence_doc + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

540           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             13 (check_blockers_named + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

541           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             15 (check_doctrine_phrases + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

542           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             17 (check_existing_memory_review_docs + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

543           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             19 (check_offlimits_present + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

544           LOAD_FAST_BORROW         1 (checks)
              LOAD_ATTR                1 (extend + NULL|self)
              LOAD_GLOBAL             21 (check_no_env_read + NULL)
              LOAD_FAST_BORROW         0 (repo_root)
              CALL                     1
              CALL                     1
              POP_TOP

546           LOAD_GLOBAL             23 (_aggregate + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1
              STORE_FAST               2 (agg)

548           LOAD_CONST               0 ('phase')
              LOAD_CONST               1 ('PAS160')

549           LOAD_CONST               2 ('generated_at')
              LOAD_GLOBAL             25 (_now_iso + NULL)
              CALL                     0

550           LOAD_CONST               3 ('verdict')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])

551           LOAD_CONST               4 ('ready')
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               3 ('verdict')
              BINARY_OP               26 ([])
              LOAD_GLOBAL             26 (VERDICT_READY)
              COMPARE_OP              72 (==)

552           LOAD_CONST               5 ('blocker_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               6 ('blockers')
              BINARY_OP               26 ([])
              CALL                     1

553           LOAD_CONST               7 ('info_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         2 (agg)
              LOAD_CONST               8 ('info')
              BINARY_OP               26 ([])
              CALL                     1

554           LOAD_CONST               9 ('check_count')
              LOAD_GLOBAL             29 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

555           LOAD_CONST              10 ('pass_count')
              LOAD_GLOBAL             31 (sum + NULL)
              LOAD_CONST              11 (<code object <genexpr> at 0x0000018C18053BD0, file "scripts/pas160_mvp_sequence_check.py", line 555>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

556           LOAD_CONST              12 ('fail_count')
              LOAD_GLOBAL             31 (sum + NULL)
              LOAD_CONST              13 (<code object <genexpr> at 0x0000018C180533F0, file "scripts/pas160_mvp_sequence_check.py", line 556>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1

557           LOAD_CONST              14 ('checks')
              LOAD_FAST_BORROW         1 (checks)

558           LOAD_CONST              15 ('operator_actions')
              LOAD_GLOBAL             33 (_operator_actions + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

547           BUILD_MAP               11
              STORE_FAST               3 (report)

560           LOAD_FAST_BORROW         3 (report)
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18053BD0, file "scripts/pas160_mvp_sequence_check.py", line 555>:
 555           RETURN_GENERATOR
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

Disassembly of <code object <genexpr> at 0x0000018C180533F0, file "scripts/pas160_mvp_sequence_check.py", line 556>:
 556           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C17FA26A0, file "scripts/pas160_mvp_sequence_check.py", line 570>:
570           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1801CDC0, file "scripts/pas160_mvp_sequence_check.py", line 570>:
570           RESUME                   0

571           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

572           LOAD_CONST               0 ('pas160_mvp_sequence_check')

574           LOAD_CONST               1 ('PAS160 — Evaluate whether the production-MVP sequence lock (PAS161 → PAS170) is on file and self-consistent. Read-only. Does not touch Supabase, .env, or any tenant data.')

571           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

580           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

581           LOAD_CONST               3 ('--repo-root')

582           LOAD_GLOBAL              6 (_REPO_ROOT_DEFAULT)

583           LOAD_CONST               4 ('Repo root to evaluate (default: parent of this script).')

580           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

585           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

586           LOAD_CONST               6 ('--output')

587           LOAD_GLOBAL              8 (REPORT_FILENAME)

588           LOAD_CONST               7 ('Where to write the JSON report (default ./')
              LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST               8 (').')
              BUILD_STRING             3

585           LOAD_CONST               5 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

590           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

591           LOAD_CONST               9 ('--json')

592           LOAD_CONST              10 ('store_true')

593           LOAD_CONST              11 ('Emit the report JSON on stdout in addition to the file.')

590           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

595           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

596           LOAD_CONST              13 ('--summary-only')

597           LOAD_CONST              10 ('store_true')

598           LOAD_CONST              14 ('Skip writing the full report file; print verdict only.')

595           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

600           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

601           LOAD_CONST              15 ('--strict')

602           LOAD_CONST              10 ('store_true')

603           LOAD_CONST              16 ('Exit 1 unless verdict == READY (default policy is the same).')

600           LOAD_CONST              12 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

605           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2790, file "scripts/pas160_mvp_sequence_check.py", line 608>:
608           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D8D460, file "scripts/pas160_mvp_sequence_check.py", line 608>:
608           RESUME                   0

609           LOAD_GLOBAL              1 (print + NULL)

610           LOAD_CONST               0 ('[PAS160] verdict=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               1 ('verdict')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               2 (' blockers=')

611           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               3 ('blocker_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               4 (' info=')

612           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               5 ('info_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               6 (' checks=')

613           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               7 ('check_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST               8 (' pass=')

614           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST               9 ('pass_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE
              LOAD_CONST              10 (' fail=')

615           LOAD_FAST_BORROW         0 (report)
              LOAD_CONST              11 ('fail_count')
              BINARY_OP               26 ([])
              FORMAT_SIMPLE

610           BUILD_STRING            12

609           CALL                     1
              POP_TOP

617           LOAD_FAST_BORROW         0 (report)
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

618           LOAD_FAST_BORROW         1 (actions)
              TO_BOOL
              POP_JUMP_IF_FALSE       93 (to L5)
              NOT_TAKEN

619           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              13 ('[PAS160] operator actions:')
              CALL                     1
              POP_TOP

620           LOAD_FAST_BORROW         1 (actions)
              LOAD_CONST              14 (slice(None, 20, None))
              BINARY_OP               26 ([])
              GET_ITER
      L2:     FOR_ITER                17 (to L3)
              STORE_FAST               2 (a)

621           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              15 ('  - ')
              LOAD_FAST_BORROW         2 (a)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L2)

620   L3:     END_FOR
              POP_ITER

622           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          20
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       34 (to L4)
              NOT_TAKEN

623           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              16 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         1 (actions)
              CALL                     1
              LOAD_SMALL_INT          20
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              17 (' more (see report file)')
              BUILD_STRING             3
              CALL                     1
              POP_TOP
              LOAD_CONST              18 (None)
              RETURN_VALUE

622   L4:     LOAD_CONST              18 (None)
              RETURN_VALUE

618   L5:     LOAD_CONST              18 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "scripts/pas160_mvp_sequence_check.py", line 626>:
626           RESUME                   0
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

Disassembly of <code object _write_report at 0x0000018C18104210, file "scripts/pas160_mvp_sequence_check.py", line 626>:
 626           RESUME                   0

 627           NOP

 628   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 629           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 630           LOAD_CONST               3 ('utf-8')

 628           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 632           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 633   L4:     LOAD_GLOBAL             11 (print + NULL)

 634           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 635           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 634           BUILD_STRING             4

 636           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 633           LOAD_CONST               7 (('file',))
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

 632   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C180FC030, file "scripts/pas160_mvp_sequence_check.py", line 640>:
640           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17F84690, file "scripts/pas160_mvp_sequence_check.py", line 640>:
 640            RESUME                   0

 641            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 642            NOP

 643    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 647    L2:     LOAD_GLOBAL             10 (os)
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

 648            LOAD_GLOBAL             10 (os)
                LOAD_ATTR               12 (path)
                LOAD_ATTR               21 (isdir + NULL|self)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L4)
                NOT_TAKEN

 649            LOAD_GLOBAL             23 (print + NULL)

 650            LOAD_CONST               2 ('error: --repo-root not a directory: ')
                LOAD_FAST                4 (repo_root)
                FORMAT_SIMPLE
                BUILD_STRING             2

 651            LOAD_GLOBAL             24 (sys)
                LOAD_ATTR               26 (stderr)

 649            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 653            LOAD_SMALL_INT           2
                RETURN_VALUE

 655    L4:     LOAD_GLOBAL             29 (evaluate + NULL)
                LOAD_FAST                4 (repo_root)
                CALL                     1
                STORE_FAST               5 (report)

 657            LOAD_FAST                2 (args)
                LOAD_ATTR               30 (summary_only)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L5)
                NOT_TAKEN

 658            LOAD_GLOBAL             33 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               34 (output)
                LOAD_FAST                5 (report)
                CALL                     2
                POP_TOP

 660    L5:     LOAD_GLOBAL             37 (_print_summary + NULL)
                LOAD_FAST                5 (report)
                CALL                     1
                POP_TOP

 662            LOAD_FAST                2 (args)
                LOAD_ATTR               38 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L6)
                NOT_TAKEN

 663            LOAD_GLOBAL             23 (print + NULL)
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

 665    L6:     LOAD_FAST                5 (report)
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

 644            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 645    L9:     LOAD_FAST                3 (e)
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

 644   L17:     RERAISE                  0

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
