# scripts_readiness/restore_drill

- **pyc:** `scripts\__pycache__\restore_drill.cpython-314.pyc`
- **expected source path (absent):** `scripts/restore_drill.py`
- **co_filename (from bytecode):** `scripts\restore_drill.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143G — Restore drill runner.

Decrypts a `.pasbak` recovery archive into a temporary workspace and
runs through the full PAS recovery checklist WITHOUT touching a live
database. The output is a `restore_drill_report.json` an operator can
attach to their quarterly drill ticket.

What this tool DOES (offline, simulated):
  - decrypt the archive (HMAC verified before any plaintext use)
  - extract into a tmp directory
  - re-verify the embedded backup_manifest + dump checksum
  - check pg_restore --list compatibility (skipped if pg_restore absent)
  - simulate `pg_restore` invocation (prints redacted command line only)
  - simulate event-export restoration (line-count + sha-256 of JSONL)
  - call scripts/integrity_check.py (offline)
  - call scripts/run_monitoring_check.py (consumes the drill report)
  - measure unpack / verify / restore-sim / total durations

What this tool does NOT do:
  - touch a live Postgres
  - touch live pas_events / calls / leads
  - upload anything

Usage:
  PAS_BAK_PASS=<phrase> python scripts/restore_drill.py \
      --archive recovery/recovery_20260509.pasbak \
      --passphrase-env PAS_BAK_PASS

Exit codes:
    0  — drill succeeded (all checks pass; or --strict not passed)
    1  — drill failed (always with --strict; otherwise on hard fail)
    2  — bad CLI arguments
    3  — passphrase missing or empty
    4  — archive missing / unreadable
    5  — passphrase wrong (MAC verification failed)
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `argparse`, `datetime`, `gzip`, `hashlib`, `importlib.util`, `io`, `json`, `os`, `pathlib`, `shutil`, `subprocess`, `sys`, `tarfile`, `tempfile`, `time`, `typing`, `util`

## Classes

_none_

## Functions / methods

`__annotate__`, `_now_iso`, `_print_human`, `_read_passphrase`, `_sha256_of_file`, `_step_events_replay`, `_step_integrity_check`, `_step_monitoring_check`, `_step_pg_restore_list`, `_step_re_verify`, `_step_simulate_restore`, `_step_unpack`, `_time_step`, `decrypt_archive_to_bytes`, `extract_tarball_to`, `main`, `run_drill`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS143G — Restore drill runner.\n\nDecrypts a `.pasbak` recovery archive into a temporary workspace and\nruns through the full PAS recovery checklist WITHOUT touching a live\ndatabase. The output is a `restore_drill_report.json` an operator can\nattach to their quarterly drill ticket.\n\nWhat this tool DOES (offline, simulated):\n  - decrypt the archive (HMAC verified before any plaintext use)\n  - extract into a tmp directory\n  - re-verify the embedded backup_manifest + dump checksum\n  - check pg_restore --list compatibility (skipped if pg_restore absent)\n  - simulate `pg_restore` invocation (prints redacted command line only)\n  - simulate event-export restoration (line-count + sha-256 of JSONL)\n  - call scripts/integrity_check.py (offline)\n  - call scripts/run_monitoring_check.py (consumes the drill report)\n  - measure unpack / verify / restore-sim / total durations\n\nWhat this tool does NOT do:\n  - touch a live Postgres\n  - touch live pas_events / calls / leads\n  - upload anything\n\nUsage:\n  PAS_BAK_PASS=<phrase> python scripts/restore_drill.py \\\n      --archive recovery/recovery_20260509.pasbak \\\n      --passphrase-env PAS_BAK_PASS\n\nExit codes:\n    0  — drill succeeded (all checks pass; or --strict not passed)\n    1  — drill failed (always with --strict; otherwise on hard fail)\n    2  — bad CLI arguments\n    3  — passphrase missing or empty\n    4  — archive missing / unreadable\n    5  — passphrase wrong (MAC verification failed)\n'
- 'utf-8'
- 'package_backup.py'
- 'package_backup_lib_for_drill'
- 'workspace'
- 'keep_temp'
- 'operator_notes'
- 'archive_path'
- 'Path'
- 'passphrase'
- 'str'
- 'return'
- 'bytes'
- '\nVerify MAC + decrypt the archive payload. Returns the plaintext\ntarball bytes. Raises:\n  FileNotFoundError — archive missing\n  ValueError        — malformed header / wrong magic\n  PermissionError   — MAC mismatch (wrong passphrase or tampered file)\n'
- 'encrypted'
- 'archive is unencrypted; refuse to drill'
- 'salt'
- 'archive MAC verification failed'
- 'ciphertext'
- 'nonce'
- 'plaintext'
- 'dest'
- 'List[str]'
- '\nExtract the gzipped tarball into `dest`. Returns the list of\nextracted relative paths. Refuses absolute paths and `..` traversal.\n'
- 'unsafe tar member name: '
- 'path'
- 'env_var'
- 'Optional[str]'
- ' files extracted'
- "\nRe-run the PAS143D-style sanity checks against the extracted\nbackup. Skips pg_restore if the binary isn't on PATH.\n"
- 'backup_manifest.json'
- 'backup_manifest.json unreadable: '
- 'dump_file'
- "dump file '"
- "' missing"
- 'sha256'
- 'dump sha256 mismatch ('
- '… vs '
- 'dump sha256 OK ('
- 'Optional: pg_restore --list against the dump.'
- 'pg_restore'
- '--list'
- 'non-zero exit'
- 'tuple'
- '\nSimulate `pg_restore` invocation. Prints the SAFE form of the\ncommand line — never the real DB URL — and records that the\nsimulation ran. NEVER actually executes pg_restore against a DB.\n'
- 'manifest unreadable: '
- '--clean'
- '--if-exists'
- '--no-owner'
- '--no-privileges'
- '<DB_URL>'
- 'simulated: '
- '\nValidate any sibling events JSONL in the archive (count + sha256).\nOptional — passes silently if no events were exported.\n'
- 'pas_events.jsonl'
- ' unreadable: '
- ' JSONL file(s); '
- ' valid row(s)'
- 'Invoke the offline integrity check; report PASS/FAIL.'
- 'scripts'
- 'integrity_check.py'
- '--strict'
- 'Invoke the monitoring check; non-zero in --strict means alerts.'
- 'run_monitoring_check.py'
- 'archive'
- 'Optional[Path]'
- 'bool'
- 'Dict[str, Any]'
- '\nPure entry-point. Returns the report dict the CLI persists.\nNever raises — catches every failure mode and records it in the\n`failures` list so the caller can act on `restore_success`.\n'
- 'skipped'
- 'pas143g_drill_'
- 'archive missing: '
- 'MAC verification failed (wrong passphrase or tampered archive)'
- 'archive malformed: '
- 'decrypt error: '
- 'decrypt_s'
- 'unpack_s'
- 'unpack failed: '
- 'verify_s'
- 're-verify failed: '
- 'pg_restore_list_s'
- 'pg_restore --list: '
- 'restore_sim_s'
- 'restore-sim: '
- 'events_replay_s'
- 'events-replay: '
- 'integrity_check_s'
- 'pass'
- 'fail'
- 'integrity: '
- 'monitoring_check_s'
- 'monitoring: '
- 'total_s'
- 'tool'
- 'pas143g.restore_drill'
- 'started_at'
- 'completed_at'
- 'archive_sha256'
- 'restore_success'
- 'failures'
- 'warnings'
- 'durations'
- 'recovered_files'
- 'recovered_file_count'
- 'simulated_commands'
- 'integrity_status'
- 'monitoring_status'
- 'kept_temp'
- 'report'
- 'None'
- 'PAS143G — RESTORE DRILL'
- '  archive:         '
- '  archive sha256:  '
- '  restore success: '
- '  durations (s):'
- '    '
- '<22'
- '.4f'
- '  integrity_status:  '
- '  monitoring_status: '
- '  FAILURES:'
- '    - '
- '  warnings:'
- '  simulated:'
- '    $ '
- '========================================================================'
- '------------------------------------------------------------------------'
- 'argv'
- 'Optional[list]'
- 'int'
- 'restore_drill'
- 'PAS143G — offline disaster-recovery rehearsal.'
- '--archive'
- 'Path to the .pasbak file to drill.'
- '--passphrase-env'
- 'Name of the env var holding the passphrase.'
- 'store_true'
- 'Exit non-zero on any failure.'
- '--keep-temp'
- "Don't delete the workspace; useful for forensics."
- '--json'
- 'Emit the report as JSON to stdout.'
- '--note'
- 'Free-text operator note recorded in the report.'
- '[FAIL] archive not found: '
- "[FAIL] passphrase env var '"
- "' missing or empty"
- 'restore_drill_report.json'
- '  [warn] could not write '
- '  report: '
- 'MAC verification failed'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS143G — Restore drill runner.\n\nDecrypts a `.pasbak` recovery archive into a temporary workspace and\nruns through the full PAS recovery checklist WITHOUT touching a live\ndatabase. The output is a `restore_drill_report.json` an operator can\nattach to their quarterly drill ticket.\n\nWhat this tool DOES (offline, simulated):\n  - decrypt the archive (HMAC verified before any plaintext use)\n  - extract into a tmp directory\n  - re-verify the embedded backup_manifest + dump checksum\n  - check pg_restore --list compatibility (skipped if pg_restore absent)\n  - simulate `pg_restore` invocation (prints redacted command line only)\n  - simulate event-export restoration (line-count + sha-256 of JSONL)\n  - call scripts/integrity_check.py (offline)\n  - call scripts/run_monitoring_check.py (consumes the drill report)\n  - measure unpack / verify / restore-sim / total durations\n\nWhat this tool does NOT do:\n  - touch a live Postgres\n  - touch live pas_events / calls / leads\n  - upload anything\n\nUsage:\n  PAS_BAK_PASS=<phrase> python scripts/restore_drill.py \\\n      --archive recovery/recovery_20260509.pasbak \\\n      --passphrase-env PAS_BAK_PASS\n\nExit codes:\n    0  — drill succeeded (all checks pass; or --strict not passed)\n    1  — drill failed (always with --strict; otherwise on hard fail)\n    2  — bad CLI arguments\n    3  — passphrase missing or empty\n    4  — archive missing / unreadable\n    5  — passphrase wrong (MAC verification failed)\n')
                STORE_NAME               0 (__doc__)

  39            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  41            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  42            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (datetime)
                STORE_NAME               5 (_dt)

  43            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (hashlib)
                STORE_NAME               6 (hashlib)

  44            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              7 (importlib.util)
                IMPORT_FROM              8 (util)
                STORE_NAME               9 (_ilu)
                POP_TOP

  45            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             10 (json)
                STORE_NAME              10 (json)

  46            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             11 (os)
                STORE_NAME              11 (os)

  47            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             12 (shutil)
                STORE_NAME              12 (shutil)

  48            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             13 (subprocess)
                STORE_NAME              13 (subprocess)

  49            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             14 (sys)
                STORE_NAME              14 (sys)

  50            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             15 (tarfile)
                STORE_NAME              15 (tarfile)

  51            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             16 (tempfile)
                STORE_NAME              16 (tempfile)

  52            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME             17 (time)
                STORE_NAME              17 (time)

  53            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Path',))
                IMPORT_NAME             18 (pathlib)
                IMPORT_FROM             19 (Path)
                STORE_NAME              19 (Path)
                POP_TOP

  54            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
                IMPORT_NAME             20 (typing)
                IMPORT_FROM             21 (Any)
                STORE_NAME              21 (Any)
                IMPORT_FROM             22 (Dict)
                STORE_NAME              22 (Dict)
                IMPORT_FROM             23 (List)
                STORE_NAME              23 (List)
                IMPORT_FROM             24 (Optional)
                STORE_NAME              24 (Optional)
                POP_TOP

  57            LOAD_NAME               14 (sys)
                LOAD_ATTR               50 (stdout)
                LOAD_NAME               14 (sys)
                LOAD_ATTR               52 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              27 (_stream)

  58            NOP

  59    L2:     LOAD_NAME               27 (_stream)
                LOAD_ATTR               57 (reconfigure + NULL|self)
                LOAD_CONST               5 ('utf-8')
                LOAD_CONST               6 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  57    L4:     END_FOR
                POP_ITER

  64            LOAD_NAME               11 (os)
                LOAD_ATTR               60 (path)
                LOAD_ATTR               63 (abspath + NULL|self)
                LOAD_NAME               11 (os)
                LOAD_ATTR               60 (path)
                LOAD_ATTR               65 (join + NULL|self)
                LOAD_NAME               11 (os)
                LOAD_ATTR               60 (path)
                LOAD_ATTR               67 (dirname + NULL|self)
                LOAD_NAME               34 (__file__)
                CALL                     1
                LOAD_CONST               7 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              35 (_REPO_ROOT)

  65            LOAD_NAME               35 (_REPO_ROOT)
                LOAD_NAME               14 (sys)
                LOAD_ATTR               60 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  66            LOAD_NAME               14 (sys)
                LOAD_ATTR               60 (path)
                LOAD_ATTR               73 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               35 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  70    L5:     LOAD_NAME               19 (Path)
                PUSH_NULL
                LOAD_NAME               34 (__file__)
                CALL                     1
                LOAD_ATTR               75 (resolve + NULL|self)
                CALL                     0
                LOAD_ATTR               76 (parent)
                LOAD_CONST               8 ('package_backup.py')
                BINARY_OP               11 (/)
                STORE_NAME              39 (_pb_path)

  71            LOAD_NAME                9 (_ilu)
                LOAD_ATTR               80 (spec_from_file_location)
                PUSH_NULL
                LOAD_CONST               9 ('package_backup_lib_for_drill')
                LOAD_NAME               39 (_pb_path)
                CALL                     2
                STORE_NAME              41 (_spec)

  72            LOAD_NAME                9 (_ilu)
                LOAD_ATTR               84 (module_from_spec)
                PUSH_NULL
                LOAD_NAME               41 (_spec)
                CALL                     1
                STORE_NAME              43 (_pb)

  73            LOAD_NAME               43 (_pb)
                LOAD_NAME               14 (sys)
                LOAD_ATTR               88 (modules)
                LOAD_NAME               41 (_spec)
                LOAD_ATTR               90 (name)
                STORE_SUBSCR

  74            LOAD_NAME               41 (_spec)
                LOAD_ATTR               92 (loader)
                LOAD_ATTR               95 (exec_module + NULL|self)
                LOAD_NAME               43 (_pb)
                CALL                     1
                POP_TOP

  81            LOAD_CONST              10 (<code object __annotate__ at 0x0000018C18025830, file "scripts\restore_drill.py", line 81>)
                MAKE_FUNCTION
                LOAD_CONST              11 (<code object decrypt_archive_to_bytes at 0x0000018C17F001D0, file "scripts\restore_drill.py", line 81>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              48 (decrypt_archive_to_bytes)

 109            LOAD_CONST              12 (<code object __annotate__ at 0x0000018C18026030, file "scripts\restore_drill.py", line 109>)
                MAKE_FUNCTION
                LOAD_CONST              13 (<code object extract_tarball_to at 0x0000018C17D81580, file "scripts\restore_drill.py", line 109>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              49 (extract_tarball_to)

 131            LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\restore_drill.py", line 131>)
                MAKE_FUNCTION
                LOAD_CONST              15 (<code object _now_iso at 0x0000018C17972550, file "scripts\restore_drill.py", line 131>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              50 (_now_iso)

 135            LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2970, file "scripts\restore_drill.py", line 135>)
                MAKE_FUNCTION
                LOAD_CONST              17 (<code object _sha256_of_file at 0x0000018C17FEDC30, file "scripts\restore_drill.py", line 135>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              51 (_sha256_of_file)

 146            LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\restore_drill.py", line 146>)
                MAKE_FUNCTION
                LOAD_CONST              19 (<code object _read_passphrase at 0x0000018C18038A30, file "scripts\restore_drill.py", line 146>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              52 (_read_passphrase)

 157            LOAD_CONST              20 (<code object _time_step at 0x0000018C179A7290, file "scripts\restore_drill.py", line 157>)
                MAKE_FUNCTION
                STORE_NAME              53 (_time_step)

 166            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3B40, file "scripts\restore_drill.py", line 166>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _step_unpack at 0x0000018C17FBFEE0, file "scripts\restore_drill.py", line 166>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              54 (_step_unpack)

 171            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA2F10, file "scripts\restore_drill.py", line 171>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _step_re_verify at 0x0000018C17EE1CC0, file "scripts\restore_drill.py", line 171>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              55 (_step_re_verify)

 194            LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA33C0, file "scripts\restore_drill.py", line 194>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object _step_pg_restore_list at 0x0000018C18646C00, file "scripts\restore_drill.py", line 194>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              56 (_step_pg_restore_list)

 217            LOAD_CONST              27 (<code object __annotate__ at 0x0000018C17FA34B0, file "scripts\restore_drill.py", line 217>)
                MAKE_FUNCTION
                LOAD_CONST              28 (<code object _step_simulate_restore at 0x0000018C17F00A10, file "scripts\restore_drill.py", line 217>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              57 (_step_simulate_restore)

 241            LOAD_CONST              29 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\restore_drill.py", line 241>)
                MAKE_FUNCTION
                LOAD_CONST              30 (<code object _step_events_replay at 0x0000018C17CC2E60, file "scripts\restore_drill.py", line 241>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              58 (_step_events_replay)

 261            LOAD_CONST              31 (<code object __annotate__ at 0x0000018C17FA3C30, file "scripts\restore_drill.py", line 261>)
                MAKE_FUNCTION
                LOAD_CONST              32 (<code object _step_integrity_check at 0x0000018C17ED9100, file "scripts\restore_drill.py", line 261>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              59 (_step_integrity_check)

 280            LOAD_CONST              33 (<code object __annotate__ at 0x0000018C17FA35A0, file "scripts\restore_drill.py", line 280>)
                MAKE_FUNCTION
                LOAD_CONST              34 (<code object _step_monitoring_check at 0x0000018C17ED8BC0, file "scripts\restore_drill.py", line 280>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              60 (_step_monitoring_check)

 303            LOAD_CONST              35 ('workspace')

 307            LOAD_CONST               2 (None)

 303            LOAD_CONST              36 ('keep_temp')

 308            LOAD_CONST              37 (False)

 303            LOAD_CONST              38 ('operator_notes')

 309            LOAD_CONST              39 ('')

 303            BUILD_MAP                3
                LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\restore_drill.py", line 303>)
                MAKE_FUNCTION
                LOAD_CONST              41 (<code object run_drill at 0x0000018C17F78C70, file "scripts\restore_drill.py", line 303>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
                STORE_NAME              61 (run_drill)

 446            LOAD_CONST              42 (<code object __annotate__ at 0x0000018C17FA2100, file "scripts\restore_drill.py", line 446>)
                MAKE_FUNCTION
                LOAD_CONST              43 (<code object _print_human at 0x0000018C17F796E0, file "scripts\restore_drill.py", line 446>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              62 (_print_human)

 482            LOAD_CONST              47 ((None,))
                LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA2B50, file "scripts\restore_drill.py", line 482>)
                MAKE_FUNCTION
                LOAD_CONST              45 (<code object main at 0x0000018C17F723C0, file "scripts\restore_drill.py", line 482>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              63 (main)

 541            LOAD_NAME               64 (__name__)
                LOAD_CONST              46 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       14 (to L6)
                NOT_TAKEN

 542            LOAD_NAME               65 (SystemExit)
                PUSH_NULL
                LOAD_NAME               63 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                RAISE_VARARGS            1

 541    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  60            LOAD_NAME               29 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  61    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          413 (to L1)

  60    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025830, file "scripts\restore_drill.py", line 81>:
 81           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('archive_path')

 82           LOAD_CONST               2 ('Path')

 81           LOAD_CONST               3 ('passphrase')

 83           LOAD_CONST               4 ('str')

 81           LOAD_CONST               5 ('return')

 84           LOAD_CONST               6 ('bytes')

 81           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object decrypt_archive_to_bytes at 0x0000018C17F001D0, file "scripts\restore_drill.py", line 81>:
 81           RESUME                   0

 92           LOAD_GLOBAL              0 (_pb)
              LOAD_ATTR                3 (read_archive_full + NULL|self)
              LOAD_FAST_BORROW         0 (archive_path)
              CALL                     1
              STORE_FAST               2 (info)

 93           LOAD_FAST_BORROW         2 (info)
              LOAD_CONST               1 ('encrypted')
              BINARY_OP               26 ([])
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L1)
              NOT_TAKEN

 95           LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               2 ('archive is unencrypted; refuse to drill')
              CALL                     1
              RAISE_VARARGS            1

 97   L1:     LOAD_GLOBAL              0 (_pb)
              LOAD_ATTR                7 (derive_keys + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (passphrase, info)
              LOAD_CONST               3 ('salt')
              BINARY_OP               26 ([])
              CALL                     2
              UNPACK_SEQUENCE          2
              STORE_FAST_STORE_FAST   52 (enc_key, mac_key)

100           LOAD_GLOBAL              0 (_pb)
              LOAD_ATTR                9 (verify_archive_mac_from_disk + NULL|self)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 4 (archive_path, mac_key)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L2)
              NOT_TAKEN

103           LOAD_GLOBAL             11 (PermissionError + NULL)
              LOAD_CONST               4 ('archive MAC verification failed')
              CALL                     1
              RAISE_VARARGS            1

105   L2:     LOAD_GLOBAL              0 (_pb)
              LOAD_ATTR               13 (decrypt + NULL|self)
              LOAD_FAST_BORROW         2 (info)
              LOAD_CONST               5 ('ciphertext')
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (enc_key, info)
              LOAD_CONST               6 ('nonce')
              BINARY_OP               26 ([])
              CALL                     3
              STORE_FAST               5 (plaintext)

106           LOAD_FAST_BORROW         5 (plaintext)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\restore_drill.py", line 109>:
109           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plaintext')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               3 ('dest')
              LOAD_CONST               4 ('Path')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('List[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object extract_tarball_to at 0x0000018C17D81580, file "scripts\restore_drill.py", line 109>:
 109            RESUME                   0

 114            LOAD_FAST_BORROW         1 (dest)
                LOAD_ATTR                1 (mkdir + NULL|self)
                LOAD_CONST               1 (True)
                LOAD_CONST               1 (True)
                LOAD_CONST               2 (('parents', 'exist_ok'))
                CALL_KW                  2
                POP_TOP

 115            BUILD_LIST               0
                STORE_FAST               2 (extracted)

 116            LOAD_SMALL_INT           0
                LOAD_CONST               3 (None)
                IMPORT_NAME              1 (gzip)
                STORE_FAST               3 (_gzip)

 117            LOAD_SMALL_INT           0
                LOAD_CONST               3 (None)
                IMPORT_NAME              2 (io)
                STORE_FAST               4 (_io)

 118            LOAD_FAST_BORROW         4 (_io)
                LOAD_ATTR                7 (BytesIO + NULL|self)
                LOAD_FAST_BORROW         0 (plaintext)
                CALL                     1
                STORE_FAST               5 (bio)

 119            LOAD_FAST_BORROW         3 (_gzip)
                LOAD_ATTR                9 (GzipFile + NULL|self)
                LOAD_FAST_BORROW         5 (bio)
                LOAD_CONST               4 ('rb')
                LOAD_CONST               5 (('fileobj', 'mode'))
                CALL_KW                  2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     STORE_FAST               6 (gz)

 120            LOAD_GLOBAL             10 (tarfile)
                LOAD_ATTR               12 (open)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (gz)
                LOAD_CONST               6 ('r')
                LOAD_CONST               5 (('fileobj', 'mode'))
                CALL_KW                  2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_FAST               7 (tar)

 121            LOAD_FAST_BORROW         7 (tar)
                LOAD_ATTR               15 (getmembers + NULL|self)
                CALL                     0
                GET_ITER
        L3:     FOR_ITER               129 (to L6)
                STORE_FAST               8 (member)

 123            LOAD_FAST_BORROW         8 (member)
                LOAD_ATTR               16 (name)
                LOAD_ATTR               19 (replace + NULL|self)
                LOAD_CONST               7 ('\\')
                LOAD_CONST               8 ('/')
                CALL                     2
                STORE_FAST               9 (name)

 124            LOAD_FAST_BORROW         9 (name)
                LOAD_ATTR               21 (startswith + NULL|self)
                LOAD_CONST               8 ('/')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        27 (to L4)
                NOT_TAKEN
                LOAD_CONST               9 ('..')
                LOAD_GLOBAL             23 (Path + NULL)
                LOAD_FAST_BORROW         9 (name)
                CALL                     1
                LOAD_ATTR               24 (parts)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       16 (to L5)
                NOT_TAKEN

 125    L4:     LOAD_GLOBAL             27 (ValueError + NULL)
                LOAD_CONST              10 ('unsafe tar member name: ')
                LOAD_FAST_BORROW         9 (name)
                CONVERT_VALUE            2 (repr)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                RAISE_VARARGS            1

 126    L5:     LOAD_FAST_BORROW         7 (tar)
                LOAD_ATTR               29 (extract + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 129 (member, dest)
                CALL                     2
                POP_TOP

 127            LOAD_FAST_BORROW         2 (extracted)
                LOAD_ATTR               31 (append + NULL|self)
                LOAD_FAST_BORROW         9 (name)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          131 (to L3)

 121    L6:     END_FOR
                POP_ITER

 120    L7:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP

 119    L8:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP

 128            LOAD_FAST_BORROW         2 (extracted)
                RETURN_VALUE

 120    L9:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L10)
                NOT_TAKEN
                RERAISE                  2
       L10:     POP_TOP
       L11:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 26 (to L8)

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 119   L13:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L14)
                NOT_TAKEN
                RERAISE                  2
       L14:     POP_TOP
       L15:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP

 128            LOAD_FAST                2 (extracted)
                RETURN_VALUE

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L13 [2] lasti
  L2 to L7 -> L9 [4] lasti
  L7 to L8 -> L13 [2] lasti
  L9 to L11 -> L12 [6] lasti
  L11 to L13 -> L13 [2] lasti
  L13 to L15 -> L16 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\restore_drill.py", line 131>:
131           RESUME                   0
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

Disassembly of <code object _now_iso at 0x0000018C17972550, file "scripts\restore_drill.py", line 131>:
131           RESUME                   0

132           LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                2 (datetime)
              LOAD_ATTR                5 (now + NULL|self)
              LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                6 (timezone)
              LOAD_ATTR                8 (utc)
              CALL                     1
              LOAD_ATTR               11 (isoformat + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "scripts\restore_drill.py", line 135>:
135           RESUME                   0
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
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sha256_of_file at 0x0000018C17FEDC30, file "scripts\restore_drill.py", line 135>:
  --            MAKE_CELL                3 (fh)

 135            RESUME                   0

 136            NOP

 137    L1:     LOAD_GLOBAL              0 (hashlib)
                LOAD_ATTR                2 (sha256)
                PUSH_NULL
                CALL                     0
                STORE_FAST               1 (h)

 138            LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST_BORROW         0 (path)
                LOAD_CONST               0 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_DEREF              3 (fh)

 139            LOAD_GLOBAL              7 (iter + NULL)
                LOAD_FAST_BORROW         3 (fh)
                BUILD_TUPLE              1
                LOAD_CONST               1 (<code object <lambda> at 0x0000018C18024C30, file "scripts\restore_drill.py", line 139>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)
                LOAD_CONST               2 (b'')
                CALL                     2
                GET_ITER
        L3:     FOR_ITER                20 (to L4)
                STORE_FAST               2 (chunk)

 140            LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR                9 (update + NULL|self)
                LOAD_FAST_BORROW         2 (chunk)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           22 (to L3)

 139    L4:     END_FOR
                POP_ITER

 138    L5:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP

 141    L6:     LOAD_FAST_BORROW         1 (h)
                LOAD_ATTR               11 (hexdigest + NULL|self)
                CALL                     0
        L7:     RETURN_VALUE

 138    L8:     PUSH_EXC_INFO
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
                JUMP_BACKWARD_NO_INTERRUPT 32 (to L6)

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 142            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L14)
                NOT_TAKEN
                POP_TOP

 143   L13:     POP_EXCEPT
                LOAD_CONST               4 ('')
                RETURN_VALUE

 142   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L2 to L5 -> L8 [2] lasti
  L5 to L7 -> L12 [0]
  L8 to L10 -> L11 [4] lasti
  L10 to L12 -> L12 [0]
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti

Disassembly of <code object <lambda> at 0x0000018C18024C30, file "scripts\restore_drill.py", line 139>:
  --           COPY_FREE_VARS           1

 139           RESUME                   0
               LOAD_DEREF               0 (fh)
               LOAD_ATTR                1 (read + NULL|self)
               LOAD_CONST               1 (1048576)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\restore_drill.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env_var')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _read_passphrase at 0x0000018C18038A30, file "scripts\restore_drill.py", line 146>:
146           RESUME                   0

147           LOAD_FAST_BORROW         0 (env_var)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

148           LOAD_CONST               0 (None)
              RETURN_VALUE

149   L1:     LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         0 (env_var)
              CALL                     1
              STORE_FAST               1 (v)

150           LOAD_FAST_BORROW         1 (v)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              RETURN_VALUE
      L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object _time_step at 0x0000018C179A7290, file "scripts\restore_drill.py", line 157>:
 157           RESUME                   0

 158           LOAD_GLOBAL              0 (time)
               LOAD_ATTR                2 (perf_counter)
               PUSH_NULL
               CALL                     0
               STORE_FAST               3 (start)

 159           NOP

 160   L1:     LOAD_FAST_BORROW         0 (fn)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (args)
               BUILD_MAP                0
               LOAD_FAST_BORROW         2 (kwargs)
               DICT_MERGE               1
               CALL_FUNCTION_EX
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   69 (ok, detail)

 163   L2:     LOAD_FAST_LOAD_FAST     69 (ok, detail)
               LOAD_GLOBAL              0 (time)
               LOAD_ATTR                2 (perf_counter)
               PUSH_NULL
               CALL                     0
               LOAD_FAST                3 (start)
               BINARY_OP               10 (-)
               BUILD_TUPLE              3
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 161           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       66 (to L8)
               NOT_TAKEN
               STORE_FAST               6 (e)

 162   L4:     LOAD_CONST               0 (False)
               LOAD_GLOBAL              7 (type + NULL)
               LOAD_FAST                6 (e)
               CALL                     1
               LOAD_ATTR                8 (__name__)
               FORMAT_SIMPLE
               LOAD_CONST               1 (': ')
               LOAD_FAST                6 (e)
               FORMAT_SIMPLE
               BUILD_STRING             3
               LOAD_GLOBAL              0 (time)
               LOAD_ATTR                2 (perf_counter)
               PUSH_NULL
               CALL                     0
               LOAD_FAST                3 (start)
               BINARY_OP               10 (-)
               BUILD_TUPLE              3
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               2 (None)
               STORE_FAST               6 (e)
               DELETE_FAST              6 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               2 (None)
               STORE_FAST               6 (e)
               DELETE_FAST              6 (e)
               RERAISE                  1

 161   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "scripts\restore_drill.py", line 166>:
166           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plaintext')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               3 ('workspace')
              LOAD_CONST               4 ('Path')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _step_unpack at 0x0000018C17FBFEE0, file "scripts\restore_drill.py", line 166>:
166           RESUME                   0

167           LOAD_GLOBAL              1 (extract_tarball_to + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (plaintext, workspace)
              CALL                     2
              STORE_FAST               2 (extracted)

168           LOAD_CONST               0 (True)
              LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         2 (extracted)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               1 (' files extracted')
              BUILD_STRING             2
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "scripts\restore_drill.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _step_re_verify at 0x0000018C17EE1CC0, file "scripts\restore_drill.py", line 171>:
 171            RESUME                   0

 176            LOAD_FAST_BORROW         0 (workspace)
                LOAD_CONST               1 ('backup_manifest.json')
                BINARY_OP               11 (/)
                STORE_FAST               1 (backup_manifest_path)

 177            LOAD_FAST_BORROW         1 (backup_manifest_path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 178            LOAD_CONST              18 ((False, 'backup_manifest.json missing in extracted archive'))
                RETURN_VALUE

 179    L1:     NOP

 180    L2:     LOAD_GLOBAL              2 (json)
                LOAD_ATTR                4 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (backup_manifest_path)
                LOAD_ATTR                7 (read_text + NULL|self)
                LOAD_CONST               3 ('utf-8')
                LOAD_CONST               4 (('encoding',))
                CALL_KW                  1
                CALL                     1
                STORE_FAST               2 (manifest)

 183    L3:     LOAD_FAST                2 (manifest)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               7 ('dump_file')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L4:     STORE_FAST               4 (dump_name)

 184            LOAD_FAST                4 (dump_name)
                TO_BOOL
                POP_JUMP_IF_FALSE        9 (to L5)
                NOT_TAKEN
                LOAD_FAST_LOAD_FAST      4 (workspace, dump_name)
                BINARY_OP               11 (/)
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               6 (None)
        L6:     STORE_FAST               5 (dump_path)

 185            LOAD_FAST                5 (dump_path)
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L7)
                NOT_TAKEN
                LOAD_FAST                5 (dump_path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L8)
                NOT_TAKEN

 186    L7:     LOAD_CONST               2 (False)
                LOAD_CONST               9 ("dump file '")
                LOAD_FAST                4 (dump_name)
                FORMAT_SIMPLE
                LOAD_CONST              10 ("' missing")
                BUILD_STRING             3
                BUILD_TUPLE              2
                RETURN_VALUE

 187    L8:     LOAD_GLOBAL             13 (_sha256_of_file + NULL)
                LOAD_FAST                5 (dump_path)
                CALL                     1
                STORE_FAST               6 (actual_sha)

 188            LOAD_FAST                2 (manifest)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST              11 ('sha256')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L9:     STORE_FAST               7 (expected)

 189            LOAD_FAST                7 (expected)
                TO_BOOL
                POP_JUMP_IF_FALSE       32 (to L10)
                NOT_TAKEN
                LOAD_FAST_LOAD_FAST    103 (actual_sha, expected)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       26 (to L10)
                NOT_TAKEN

 190            LOAD_CONST               2 (False)
                LOAD_CONST              12 ('dump sha256 mismatch (')
                LOAD_FAST                6 (actual_sha)
                LOAD_CONST              13 (slice(None, 12, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              14 ('… vs ')
                LOAD_FAST                7 (expected)
                LOAD_CONST              13 (slice(None, 12, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              15 ('…)')
                BUILD_STRING             5
                BUILD_TUPLE              2
                RETURN_VALUE

 191   L10:     LOAD_CONST              16 (True)
                LOAD_CONST              17 ('dump sha256 OK (')
                LOAD_FAST                6 (actual_sha)
                LOAD_CONST              13 (slice(None, 12, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              15 ('…)')
                BUILD_STRING             3
                BUILD_TUPLE              2
                RETURN_VALUE

  --   L11:     PUSH_EXC_INFO

 181            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       18 (to L16)
                NOT_TAKEN
                STORE_FAST               3 (e)

 182   L12:     LOAD_CONST               2 (False)
                LOAD_CONST               5 ('backup_manifest.json unreadable: ')
                LOAD_FAST                3 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_TUPLE              2
       L13:     SWAP                     2
       L14:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L15:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 181   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L11 [0]
  L11 to L12 -> L17 [1] lasti
  L12 to L13 -> L15 [1] lasti
  L13 to L14 -> L17 [1] lasti
  L15 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "scripts\restore_drill.py", line 194>:
194           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _step_pg_restore_list at 0x0000018C18646C00, file "scripts\restore_drill.py", line 194>:
 194            RESUME                   0

 196            LOAD_GLOBAL              0 (shutil)
                LOAD_ATTR                2 (which)
                PUSH_NULL
                LOAD_CONST               1 ('pg_restore')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 197            LOAD_CONST              15 ((True, 'pg_restore not on PATH; skipped'))
                RETURN_VALUE

 199    L1:     LOAD_FAST_BORROW         0 (workspace)
                LOAD_CONST               3 ('backup_manifest.json')
                BINARY_OP               11 (/)
                STORE_FAST               1 (backup_manifest_path)

 200            NOP

 201    L2:     LOAD_GLOBAL              4 (json)
                LOAD_ATTR                6 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (backup_manifest_path)
                LOAD_ATTR                9 (read_text + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 (('encoding',))
                CALL_KW                  1
                CALL                     1
                STORE_FAST               2 (manifest)

 204    L3:     LOAD_FAST_LOAD_FAST      2 (workspace, manifest)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('dump_file')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L4:     BINARY_OP               11 (/)
                STORE_FAST               3 (dump_path)

 205            NOP

 206    L5:     LOAD_GLOBAL             14 (subprocess)
                LOAD_ATTR               16 (run)
                PUSH_NULL

 207            LOAD_CONST               1 ('pg_restore')
                LOAD_CONST               9 ('--list')
                LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST                3 (dump_path)
                CALL                     1
                BUILD_LIST               3

 208            LOAD_CONST               2 (True)
                LOAD_CONST               2 (True)
                LOAD_CONST               6 (False)
                LOAD_SMALL_INT          60

 206            LOAD_CONST              10 (('capture_output', 'text', 'check', 'timeout'))
                CALL_KW                  5
                STORE_FAST               4 (out)

 212    L6:     LOAD_FAST                4 (out)
                LOAD_ATTR               24 (returncode)
                LOAD_SMALL_INT           0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       56 (to L9)
                NOT_TAKEN

 213            LOAD_CONST               6 (False)
                LOAD_FAST                4 (out)
                LOAD_ATTR               26 (stderr)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L7:     LOAD_CONST              13 (slice(None, 200, None))
                BINARY_OP               26 ([])
                LOAD_ATTR               29 (strip + NULL|self)
                CALL                     0
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              14 ('non-zero exit')
        L8:     BUILD_TUPLE              2
                RETURN_VALUE

 214    L9:     LOAD_CONST              17 ((True, 'TOC readable'))
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 202            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L12)
                NOT_TAKEN
                POP_TOP

 203            LOAD_CONST              16 ((False, 'could not re-read manifest for dump path'))
                SWAP                     2
       L11:     POP_EXCEPT
                RETURN_VALUE

 202   L12:     RERAISE                  0

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L14:     PUSH_EXC_INFO

 210            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L19)
                NOT_TAKEN
                STORE_FAST               5 (e)

 211   L15:     LOAD_CONST               6 (False)
                LOAD_GLOBAL             21 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               22 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST              11 (': ')
                LOAD_FAST                5 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_TUPLE              2
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST              12 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 210   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L10 [0]
  L5 to L6 -> L14 [0]
  L10 to L11 -> L13 [1] lasti
  L12 to L13 -> L13 [1] lasti
  L14 to L15 -> L20 [1] lasti
  L15 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "scripts\restore_drill.py", line 217>:
217           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('tuple')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _step_simulate_restore at 0x0000018C17F00A10, file "scripts\restore_drill.py", line 217>:
 217            RESUME                   0

 223            LOAD_FAST_BORROW         0 (workspace)
                LOAD_CONST               1 ('backup_manifest.json')
                BINARY_OP               11 (/)
                STORE_FAST               1 (backup_manifest_path)

 224            NOP

 225    L1:     LOAD_GLOBAL              0 (json)
                LOAD_ATTR                2 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW         1 (backup_manifest_path)
                LOAD_ATTR                5 (read_text + NULL|self)
                LOAD_CONST               2 ('utf-8')
                LOAD_CONST               3 (('encoding',))
                CALL_KW                  1
                CALL                     1
                STORE_FAST               2 (manifest)

 228    L2:     LOAD_FAST                2 (manifest)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               7 ('dump_file')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               8 ('')
        L3:     STORE_FAST               4 (dump_name)

 230            LOAD_CONST               9 ('pg_restore')

 231            LOAD_CONST              10 ('--clean')

 232            LOAD_CONST              11 ('--if-exists')

 233            LOAD_CONST              12 ('--no-owner')

 234            LOAD_CONST              13 ('--no-privileges')

 235            LOAD_CONST              14 ('<DB_URL>')

 236            LOAD_GLOBAL             11 (str + NULL)
                LOAD_FAST_LOAD_FAST      4 (workspace, dump_name)
                BINARY_OP               11 (/)
                CALL                     1

 229            BUILD_LIST               7
                STORE_FAST               5 (safe_cmd)

 238            LOAD_CONST              15 (True)
                LOAD_CONST              16 ('simulated: ')
                LOAD_CONST              17 (' ')
                LOAD_ATTR               13 (join + NULL|self)
                LOAD_FAST                5 (safe_cmd)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_TUPLE              2
                RETURN_VALUE

  --    L4:     PUSH_EXC_INFO

 226            LOAD_GLOBAL              6 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       18 (to L9)
                NOT_TAKEN
                STORE_FAST               3 (e)

 227    L5:     LOAD_CONST               4 (False)
                LOAD_CONST               5 ('manifest unreadable: ')
                LOAD_FAST                3 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_TUPLE              2
        L6:     SWAP                     2
        L7:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --    L8:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 226    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L4 [0]
  L4 to L5 -> L10 [1] lasti
  L5 to L6 -> L8 [1] lasti
  L6 to L7 -> L10 [1] lasti
  L8 to L10 -> L10 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\restore_drill.py", line 241>:
241           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _step_events_replay at 0x0000018C17CC2E60, file "scripts\restore_drill.py", line 241>:
 241            RESUME                   0

 246            LOAD_GLOBAL              1 (list + NULL)
                LOAD_FAST_BORROW         0 (workspace)
                LOAD_ATTR                3 (rglob + NULL|self)
                LOAD_CONST               1 ('pas_events.jsonl')
                CALL                     1
                CALL                     1
                STORE_FAST               1 (found)

 247            LOAD_FAST_BORROW         1 (found)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 248            LOAD_CONST              11 ((True, 'no pas_events.jsonl in archive (optional component)'))
                RETURN_VALUE

 249    L1:     LOAD_SMALL_INT           0
                STORE_FAST               2 (total_lines)

 250            LOAD_FAST_BORROW         1 (found)
                GET_ITER
        L2:     FOR_ITER                77 (to L11)
                STORE_FAST               3 (p)

 251            NOP

 252    L3:     LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST_BORROW         3 (p)
                LOAD_CONST               3 ('r')
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 (('encoding',))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L4:     STORE_FAST               4 (fh)

 253            LOAD_FAST_BORROW         4 (fh)
                GET_ITER
        L5:     FOR_ITER                36 (to L8)
                STORE_FAST               5 (line)

 254            LOAD_FAST_BORROW         5 (line)
                LOAD_ATTR                7 (strip + NULL|self)
                CALL                     0
                TO_BOOL
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           27 (to L5)

 255    L7:     LOAD_FAST_BORROW         2 (total_lines)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (total_lines)
                JUMP_BACKWARD           38 (to L5)

 253    L8:     END_FOR
                POP_ITER

 252    L9:     LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                LOAD_CONST               6 (None)
                CALL                     3
                POP_TOP
       L10:     JUMP_BACKWARD           79 (to L2)

 250   L11:     END_FOR
                POP_ITER

 258            LOAD_CONST               2 (True)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         1 (found)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST               9 (' JSONL file(s); ')
                LOAD_FAST_BORROW         2 (total_lines)
                FORMAT_SIMPLE
                LOAD_CONST              10 (' valid row(s)')
                BUILD_STRING             4
                BUILD_TUPLE              2
                RETURN_VALUE

 252   L12:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L13)
                NOT_TAKEN
                RERAISE                  2
       L13:     POP_TOP
       L14:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
       L15:     JUMP_BACKWARD          117 (to L2)

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L17:     PUSH_EXC_INFO

 256            LOAD_GLOBAL              8 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       32 (to L22)
                NOT_TAKEN
                STORE_FAST               6 (e)

 257   L18:     LOAD_CONST               7 (False)
                LOAD_FAST                3 (p)
                LOAD_ATTR               10 (name)
                FORMAT_SIMPLE
                LOAD_CONST               8 (' unreadable: ')
                LOAD_FAST                6 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_TUPLE              2
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                SWAP                     2
                POP_TOP
                RETURN_VALUE

  --   L21:     LOAD_CONST               6 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 256   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L17 [1]
  L4 to L6 -> L12 [3] lasti
  L7 to L9 -> L12 [3] lasti
  L9 to L10 -> L17 [1]
  L12 to L14 -> L16 [5] lasti
  L14 to L15 -> L17 [1]
  L16 to L17 -> L17 [1]
  L17 to L18 -> L23 [2] lasti
  L18 to L19 -> L21 [2] lasti
  L19 to L20 -> L23 [2] lasti
  L21 to L23 -> L23 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "scripts\restore_drill.py", line 261>:
261           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _step_integrity_check at 0x0000018C17ED9100, file "scripts\restore_drill.py", line 261>:
 261            RESUME                   0

 263            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_GLOBAL              2 (__file__)
                CALL                     1
                LOAD_ATTR                5 (resolve + NULL|self)
                CALL                     0
                LOAD_ATTR                6 (parents)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                STORE_FAST               1 (repo_root)

 264            LOAD_FAST_BORROW         1 (repo_root)
                LOAD_CONST               1 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('integrity_check.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (script)

 265            LOAD_FAST_BORROW         2 (script)
                LOAD_ATTR                9 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 266            LOAD_CONST               9 ((False, 'integrity_check.py missing from repo'))
                RETURN_VALUE

 267    L1:     NOP

 268    L2:     LOAD_GLOBAL             10 (subprocess)
                LOAD_ATTR               12 (run)
                PUSH_NULL

 269            LOAD_GLOBAL             14 (sys)
                LOAD_ATTR               16 (executable)
                LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         2 (script)
                CALL                     1
                LOAD_CONST               4 ('--strict')
                BUILD_LIST               3

 270            LOAD_CONST               5 (True)
                LOAD_CONST               5 (True)
                LOAD_CONST               3 (False)
                LOAD_SMALL_INT         120

 271            LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         0 (workspace)
                CALL                     1

 268            LOAD_CONST               6 (('capture_output', 'text', 'check', 'timeout', 'cwd'))
                CALL_KW                  6
                STORE_FAST               3 (proc)

 275    L3:     LOAD_FAST                3 (proc)
                LOAD_ATTR               26 (returncode)
                LOAD_SMALL_INT           0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 276            LOAD_CONST              10 ((False, 'integrity_check exited non-zero'))
                RETURN_VALUE

 277    L4:     LOAD_CONST              11 ((True, 'integrity_check passed'))
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 273            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN
                STORE_FAST               4 (e)

 274    L6:     LOAD_CONST               3 (False)
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': ')
                LOAD_FAST                4 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_TUPLE              2
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 273   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "scripts\restore_drill.py", line 280>:
280           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('workspace')
              LOAD_CONST               2 ('Path')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _step_monitoring_check at 0x0000018C17ED8BC0, file "scripts\restore_drill.py", line 280>:
 280            RESUME                   0

 282            LOAD_GLOBAL              1 (Path + NULL)
                LOAD_GLOBAL              2 (__file__)
                CALL                     1
                LOAD_ATTR                5 (resolve + NULL|self)
                CALL                     0
                LOAD_ATTR                6 (parents)
                LOAD_SMALL_INT           1
                BINARY_OP               26 ([])
                STORE_FAST               1 (repo_root)

 283            LOAD_FAST_BORROW         1 (repo_root)
                LOAD_CONST               1 ('scripts')
                BINARY_OP               11 (/)
                LOAD_CONST               2 ('run_monitoring_check.py')
                BINARY_OP               11 (/)
                STORE_FAST               2 (script)

 284            LOAD_FAST_BORROW         2 (script)
                LOAD_ATTR                9 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 285            LOAD_CONST               9 ((False, 'run_monitoring_check.py missing from repo'))
                RETURN_VALUE

 286    L1:     NOP

 287    L2:     LOAD_GLOBAL             10 (subprocess)
                LOAD_ATTR               12 (run)
                PUSH_NULL

 288            LOAD_GLOBAL             14 (sys)
                LOAD_ATTR               16 (executable)
                LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         2 (script)
                CALL                     1
                LOAD_CONST               4 ('--strict')
                BUILD_LIST               3

 289            LOAD_CONST               5 (True)
                LOAD_CONST               5 (True)
                LOAD_CONST               3 (False)
                LOAD_SMALL_INT         120

 290            LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         0 (workspace)
                CALL                     1

 287            LOAD_CONST               6 (('capture_output', 'text', 'check', 'timeout', 'cwd'))
                CALL_KW                  6
                STORE_FAST               3 (proc)

 294    L3:     LOAD_FAST                3 (proc)
                LOAD_ATTR               26 (returncode)
                LOAD_SMALL_INT           0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 295            LOAD_CONST              10 ((False, 'monitoring_check flagged HIGH/CRITICAL alerts'))
                RETURN_VALUE

 296    L4:     LOAD_CONST              11 ((True, 'monitoring_check passed'))
                RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 292            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       39 (to L10)
                NOT_TAKEN
                STORE_FAST               4 (e)

 293    L6:     LOAD_CONST               3 (False)
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                4 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                LOAD_CONST               7 (': ')
                LOAD_FAST                4 (e)
                FORMAT_SIMPLE
                BUILD_STRING             3
                BUILD_TUPLE              2
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               8 (None)
                STORE_FAST               4 (e)
                DELETE_FAST              4 (e)
                RERAISE                  1

 292   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\restore_drill.py", line 303>:
303           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('archive')

304           LOAD_CONST               2 ('Path')

303           LOAD_CONST               3 ('passphrase')

305           LOAD_CONST               4 ('str')

303           LOAD_CONST               5 ('workspace')

307           LOAD_CONST               6 ('Optional[Path]')

303           LOAD_CONST               7 ('keep_temp')

308           LOAD_CONST               8 ('bool')

303           LOAD_CONST               9 ('operator_notes')

309           LOAD_CONST               4 ('str')

303           LOAD_CONST              10 ('return')

310           LOAD_CONST              11 ('Dict[str, Any]')

303           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object run_drill at 0x0000018C17F78C70, file "scripts\restore_drill.py", line 303>:
  --            MAKE_CELL                2 (workspace)

 303            RESUME                   0

 316            LOAD_GLOBAL              1 (_now_iso + NULL)
                CALL                     0
                STORE_FAST               5 (started_at)

 317            LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                STORE_FAST               6 (started_perf)

 318            LOAD_GLOBAL              7 (_sha256_of_file + NULL)
                LOAD_FAST_BORROW         0 (archive)
                CALL                     1
                STORE_FAST               7 (archive_sha)

 319            BUILD_LIST               0
                STORE_FAST               8 (failures)

 320            BUILD_LIST               0
                STORE_FAST               9 (warnings)

 321            BUILD_MAP                0
                STORE_FAST              10 (durations)

 322            BUILD_LIST               0
                STORE_FAST              11 (simulated_commands)

 323            BUILD_LIST               0
                STORE_FAST              12 (recovered_files)

 325            LOAD_CONST               1 ('skipped')
                STORE_FAST              13 (integrity_status)

 326            LOAD_CONST               1 ('skipped')
                STORE_FAST              14 (monitoring_status)

 327            LOAD_DEREF               2 (workspace)
                LOAD_CONST               2 (None)
                IS_OP                    0 (is)
                STORE_FAST              15 (ws_managed)

 328            LOAD_DEREF               2 (workspace)
                POP_JUMP_IF_NOT_NONE    34 (to L1)
                NOT_TAKEN

 329            LOAD_GLOBAL              9 (Path + NULL)
                LOAD_GLOBAL             10 (tempfile)
                LOAD_ATTR               12 (mkdtemp)
                PUSH_NULL
                LOAD_CONST               3 ('pas143g_drill_')
                LOAD_CONST               4 (('prefix',))
                CALL_KW                  1
                CALL                     1
                STORE_DEREF              2 (workspace)
                JUMP_FORWARD            19 (to L2)

 331    L1:     LOAD_DEREF               2 (workspace)
                LOAD_ATTR               15 (mkdir + NULL|self)
                LOAD_CONST               5 (True)
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('parents', 'exist_ok'))
                CALL_KW                  2
                POP_TOP

 333    L2:     LOAD_CONST               2 (None)
                STORE_FAST              16 (plaintext)

 334            NOP

 336    L3:     LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                STORE_FAST              17 (t0)

 337    L4:     NOP

 338    L5:     LOAD_GLOBAL             17 (decrypt_archive_to_bytes + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (archive, passphrase)
                CALL                     2
                STORE_FAST              16 (plaintext)

 347    L6:     LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                LOAD_FAST_BORROW        17 (t0)
                BINARY_OP               10 (-)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              11 ('decrypt_s')
                STORE_SUBSCR

 350            LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        93 (to L8)
                NOT_TAKEN

 351            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             34 (_step_unpack)
                LOAD_FAST_BORROW        16 (plaintext)
                LOAD_DEREF               2 (workspace)
                CALL                     3
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 352            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              12 ('unpack_s')
                STORE_SUBSCR

 353            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        22 (to L7)
                NOT_TAKEN

 354            LOAD_FAST_BORROW         8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              13 ('unpack failed: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            42 (to L9)

 356    L7:     LOAD_GLOBAL             37 (sorted + NULL)
                LOAD_FAST_BORROW         2 (workspace)
                BUILD_TUPLE              1
                LOAD_CONST              14 (<code object <genexpr> at 0x0000018C17FF10B0, file "scripts\restore_drill.py", line 356>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE   8 (closure)

 358            LOAD_DEREF               2 (workspace)
                LOAD_ATTR               39 (rglob + NULL|self)
                LOAD_CONST              15 ('*')
                CALL                     1
                GET_ITER

 356            CALL                     0
                CALL                     1
                STORE_FAST              12 (recovered_files)
                JUMP_FORWARD             5 (to L9)

 362    L8:     LOAD_CONST              16 (0.0)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              12 ('unpack_s')
                STORE_SUBSCR

 365    L9:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        62 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         8 (failures)
                TO_BOOL
                POP_JUMP_IF_TRUE        54 (to L12)
       L10:     NOT_TAKEN

 366   L11:     LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             40 (_step_re_verify)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 367            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              17 ('verify_s')
                STORE_SUBSCR

 368            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L12)
                NOT_TAKEN

 369            LOAD_FAST_BORROW         8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              18 ('re-verify failed: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 372   L12:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        54 (to L13)
                NOT_TAKEN

 373            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             42 (_step_pg_restore_list)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 374            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              19 ('pg_restore_list_s')
                STORE_SUBSCR

 375            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L13)
                NOT_TAKEN

 376            LOAD_FAST_BORROW         9 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              20 ('pg_restore --list: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 379   L13:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        88 (to L15)
                NOT_TAKEN

 380            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             44 (_step_simulate_restore)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 381            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              21 ('restore_sim_s')
                STORE_SUBSCR

 382            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L14)
                NOT_TAKEN

 383            LOAD_FAST_BORROW        11 (simulated_commands)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_FAST_BORROW        20 (detail)
                LOAD_ATTR               47 (replace + NULL|self)
                LOAD_CONST              22 ('simulated: ')
                LOAD_CONST              23 ('')
                CALL                     2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            20 (to L15)

 385   L14:     LOAD_FAST_BORROW         9 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              24 ('restore-sim: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 388   L15:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        54 (to L16)
                NOT_TAKEN

 389            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             48 (_step_events_replay)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 390            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              25 ('events_replay_s')
                STORE_SUBSCR

 391            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L16)
                NOT_TAKEN

 392            LOAD_FAST_BORROW         9 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              26 ('events-replay: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 395   L16:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        66 (to L21)
                NOT_TAKEN

 396            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             50 (_step_integrity_check)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 397            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              27 ('integrity_check_s')
                STORE_SUBSCR

 398            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
                NOT_TAKEN
                LOAD_CONST              28 ('pass')
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_CONST              29 ('fail')
       L18:     STORE_FAST              13 (integrity_status)

 399            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L21)
       L19:     NOT_TAKEN

 400   L20:     LOAD_FAST_BORROW         9 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              30 ('integrity: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 403   L21:     LOAD_FAST_BORROW        16 (plaintext)
                POP_JUMP_IF_NONE        66 (to L26)
                NOT_TAKEN

 404            LOAD_GLOBAL             33 (_time_step + NULL)
                LOAD_GLOBAL             52 (_step_monitoring_check)
                LOAD_DEREF               2 (workspace)
                CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST              19 (ok)
                STORE_FAST              20 (detail)
                STORE_FAST              21 (dur)

 405            LOAD_FAST_BORROW        21 (dur)
                LOAD_FAST_BORROW        10 (durations)
                LOAD_CONST              31 ('monitoring_check_s')
                STORE_SUBSCR

 406            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L22)
                NOT_TAKEN
                LOAD_CONST              28 ('pass')
                JUMP_FORWARD             1 (to L23)
       L22:     LOAD_CONST              29 ('fail')
       L23:     STORE_FAST              14 (monitoring_status)

 407            LOAD_FAST_BORROW        19 (ok)
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L26)
       L24:     NOT_TAKEN

 408   L25:     LOAD_FAST_BORROW         9 (warnings)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              32 ('monitoring: ')
                LOAD_FAST_BORROW        20 (detail)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 410   L26:     LOAD_FAST_BORROW        15 (ws_managed)
                TO_BOOL
                POP_JUMP_IF_FALSE       34 (to L28)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (keep_temp)
                TO_BOOL
                POP_JUMP_IF_TRUE        26 (to L28)
                NOT_TAKEN

 411            NOP

 412   L27:     LOAD_GLOBAL             54 (shutil)
                LOAD_ATTR               56 (rmtree)
                PUSH_NULL
                LOAD_DEREF               2 (workspace)
                LOAD_CONST               5 (True)
                LOAD_CONST              33 (('ignore_errors',))
                CALL_KW                  2
                POP_TOP

 416   L28:     LOAD_GLOBAL              1 (_now_iso + NULL)
                CALL                     0
                STORE_FAST              22 (completed_at)

 417            LOAD_GLOBAL              2 (time)
                LOAD_ATTR                4 (perf_counter)
                PUSH_NULL
                CALL                     0
                LOAD_FAST                6 (started_perf)
                BINARY_OP               10 (-)
                LOAD_FAST               10 (durations)
                LOAD_CONST              34 ('total_s')
                STORE_SUBSCR

 419            LOAD_FAST                8 (failures)
                TO_BOOL
                UNARY_NOT
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        5 (to L29)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST               16 (plaintext)
                LOAD_CONST               2 (None)
                IS_OP                    1 (is not)
       L29:     STORE_FAST              23 (restore_success)

 421            BUILD_MAP                0

 422            LOAD_CONST              35 ('tool')
                LOAD_CONST              36 ('pas143g.restore_drill')

 421            MAP_ADD                  1

 423            LOAD_CONST              37 ('started_at')
                LOAD_FAST                5 (started_at)

 421            MAP_ADD                  1

 424            LOAD_CONST              38 ('completed_at')
                LOAD_FAST               22 (completed_at)

 421            MAP_ADD                  1

 425            LOAD_CONST              39 ('archive')
                LOAD_GLOBAL             59 (str + NULL)
                LOAD_FAST                0 (archive)
                CALL                     1

 421            MAP_ADD                  1

 426            LOAD_CONST              40 ('archive_sha256')
                LOAD_FAST                7 (archive_sha)

 421            MAP_ADD                  1

 427            LOAD_CONST              41 ('restore_success')
                LOAD_FAST               23 (restore_success)

 421            MAP_ADD                  1

 428            LOAD_CONST              42 ('failures')
                LOAD_FAST                8 (failures)

 421            MAP_ADD                  1

 429            LOAD_CONST              43 ('warnings')
                LOAD_FAST                9 (warnings)

 421            MAP_ADD                  1

 430            LOAD_CONST              44 ('durations')
                LOAD_FAST               10 (durations)
                LOAD_ATTR               61 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR     24 (k)
                LOAD_FAST_AND_CLEAR     25 (v)
                SWAP                     3
       L30:     BUILD_MAP                0
                SWAP                     2
       L31:     FOR_ITER                19 (to L32)
                UNPACK_SEQUENCE          2
                STORE_FAST              24 (k)
                STORE_FAST              25 (v)
                LOAD_FAST               24 (k)
                LOAD_GLOBAL             63 (round + NULL)
                LOAD_FAST               25 (v)
                LOAD_SMALL_INT           4
                CALL                     2
                MAP_ADD                  2
                JUMP_BACKWARD           21 (to L31)
       L32:     END_FOR
                POP_ITER
       L33:     SWAP                     3
                STORE_FAST              25 (v)
                STORE_FAST              24 (k)

 421            MAP_ADD                  1

 431            LOAD_CONST              45 ('recovered_files')
                LOAD_FAST               12 (recovered_files)
                LOAD_CONST              46 (slice(None, 200, None))
                BINARY_OP               26 ([])

 421            MAP_ADD                  1

 432            LOAD_CONST              47 ('recovered_file_count')
                LOAD_GLOBAL             65 (len + NULL)
                LOAD_FAST               12 (recovered_files)
                CALL                     1

 421            MAP_ADD                  1

 433            LOAD_CONST              48 ('simulated_commands')
                LOAD_FAST               11 (simulated_commands)

 421            MAP_ADD                  1

 434            LOAD_CONST              49 ('integrity_status')
                LOAD_FAST               13 (integrity_status)

 421            MAP_ADD                  1

 435            LOAD_CONST              50 ('monitoring_status')
                LOAD_FAST               14 (monitoring_status)

 421            MAP_ADD                  1

 436            LOAD_CONST              51 ('operator_notes')
                LOAD_FAST                4 (operator_notes)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L34)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              23 ('')

 421   L34:     MAP_ADD                  1

 437            LOAD_CONST              52 ('kept_temp')
                LOAD_GLOBAL             67 (bool + NULL)
                LOAD_FAST                3 (keep_temp)
                CALL                     1

 421            MAP_ADD                  1

 438            LOAD_CONST              53 ('workspace')
                LOAD_FAST                3 (keep_temp)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L35)
                NOT_TAKEN
                LOAD_GLOBAL             59 (str + NULL)
                LOAD_DEREF               2 (workspace)
                CALL                     1

 421            MAP_ADD                  1
                RETURN_VALUE

 438   L35:     LOAD_CONST               2 (None)

 421            MAP_ADD                  1
                RETURN_VALUE

  --   L36:     PUSH_EXC_INFO

 339            LOAD_GLOBAL             18 (FileNotFoundError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       32 (to L40)
                NOT_TAKEN
                STORE_FAST              18 (e)

 340   L37:     LOAD_FAST                8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST               7 ('archive missing: ')
                LOAD_FAST               18 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
       L38:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 841 (to L6)

  --   L39:     LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 341   L40:     LOAD_GLOBAL             22 (PermissionError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       22 (to L44)
       L41:     NOT_TAKEN
       L42:     POP_TOP

 342            LOAD_FAST                8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST               8 ('MAC verification failed (wrong passphrase or tampered archive)')
                CALL                     1
                POP_TOP
       L43:     POP_EXCEPT
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 875 (to L6)

 343   L44:     LOAD_GLOBAL             24 (ValueError)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       32 (to L50)
       L45:     NOT_TAKEN
       L46:     STORE_FAST              18 (e)

 344   L47:     LOAD_FAST                8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST               9 ('archive malformed: ')
                LOAD_FAST               18 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
       L48:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 911 (to L6)

  --   L49:     LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 345   L50:     LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       51 (to L56)
       L51:     NOT_TAKEN
       L52:     STORE_FAST              18 (e)

 346   L53:     LOAD_FAST                8 (failures)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_CONST              10 ('decrypt error: ')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               18 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP
       L54:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                EXTENDED_ARG             3
                JUMP_BACKWARD_NO_INTERRUPT 970 (to L6)

  --   L55:     LOAD_CONST               2 (None)
                STORE_FAST              18 (e)
                DELETE_FAST             18 (e)
                RERAISE                  1

 345   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 413            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L60)
                NOT_TAKEN
                POP_TOP

 414   L59:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 411 (to L28)

 413   L60:     RERAISE                  0

  --   L61:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L62:     PUSH_EXC_INFO

 410            LOAD_FAST               15 (ws_managed)
                TO_BOOL
                POP_JUMP_IF_FALSE       53 (to L71)
                NOT_TAKEN
                LOAD_FAST                3 (keep_temp)
                TO_BOOL
                POP_JUMP_IF_TRUE        44 (to L70)
       L63:     NOT_TAKEN

 411            NOP

 412   L64:     LOAD_GLOBAL             54 (shutil)
                LOAD_ATTR               56 (rmtree)
                PUSH_NULL
                LOAD_DEREF               2 (workspace)
                LOAD_CONST               5 (True)
                LOAD_CONST              33 (('ignore_errors',))
                CALL_KW                  2
                POP_TOP
       L65:     RERAISE                  0

  --   L66:     PUSH_EXC_INFO

 413            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L68)
                NOT_TAKEN
                POP_TOP

 414   L67:     POP_EXCEPT
                RERAISE                  0

 413   L68:     RERAISE                  0

  --   L69:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 410   L70:     RERAISE                  0
       L71:     RERAISE                  0

  --   L72:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L73:     SWAP                     2
                POP_TOP

 430            SWAP                     3
                STORE_FAST              25 (v)
                STORE_FAST              24 (k)
                RERAISE                  0
ExceptionTable:
  L3 to L4 -> L62 [0]
  L5 to L6 -> L36 [0]
  L6 to L10 -> L62 [0]
  L11 to L19 -> L62 [0]
  L20 to L24 -> L62 [0]
  L25 to L26 -> L62 [0]
  L27 to L28 -> L58 [0]
  L30 to L33 -> L73 [5]
  L36 to L37 -> L57 [1] lasti
  L37 to L38 -> L39 [1] lasti
  L38 to L39 -> L62 [0]
  L39 to L41 -> L57 [1] lasti
  L42 to L43 -> L57 [1] lasti
  L43 to L44 -> L62 [0]
  L44 to L45 -> L57 [1] lasti
  L46 to L47 -> L57 [1] lasti
  L47 to L48 -> L49 [1] lasti
  L48 to L49 -> L62 [0]
  L49 to L51 -> L57 [1] lasti
  L52 to L53 -> L57 [1] lasti
  L53 to L54 -> L55 [1] lasti
  L54 to L55 -> L62 [0]
  L55 to L57 -> L57 [1] lasti
  L57 to L58 -> L62 [0]
  L58 to L59 -> L61 [1] lasti
  L60 to L61 -> L61 [1] lasti
  L62 to L63 -> L72 [1] lasti
  L64 to L65 -> L66 [2]
  L65 to L66 -> L72 [1] lasti
  L66 to L67 -> L69 [3] lasti
  L67 to L68 -> L72 [1] lasti
  L68 to L69 -> L69 [3] lasti
  L69 to L72 -> L72 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C17FF10B0, file "scripts\restore_drill.py", line 356>:
  --           COPY_FREE_VARS           1

 356           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 358   L2:     FOR_ITER                71 (to L5)
               STORE_FAST               1 (p)

 359           LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                1 (is_file + NULL|self)
               CALL                     0
               TO_BOOL

 357   L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_GLOBAL              3 (str + NULL)
               LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                5 (relative_to + NULL|self)
               LOAD_DEREF               2 (workspace)
               CALL                     1
               CALL                     1
               LOAD_ATTR                7 (replace + NULL|self)
               LOAD_CONST               0 ('\\')
               LOAD_CONST               1 ('/')
               CALL                     2
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           73 (to L2)

 358   L5:     END_FOR
               POP_ITER
               LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "scripts\restore_drill.py", line 446>:
446           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('None')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _print_human at 0x0000018C17F796E0, file "scripts\restore_drill.py", line 446>:
446            RESUME                   0

447            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              30 ('========================================================================')
               CALL                     1
               POP_TOP

448            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               1 ('PAS143G — RESTORE DRILL')
               CALL                     1
               POP_TOP

449            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              31 ('------------------------------------------------------------------------')
               CALL                     1
               POP_TOP

450            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               2 ('  archive:         ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               3 ('archive')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

451            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               4 ('  archive sha256:  ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST               5 ('archive_sha256')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN
               POP_TOP
               LOAD_CONST               6 ('')
       L1:     LOAD_CONST               7 (slice(None, 24, None))
               BINARY_OP               26 ([])
               FORMAT_SIMPLE
               LOAD_CONST               8 ('…')
               BUILD_STRING             3
               CALL                     1
               POP_TOP

452            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST               9 ('  restore success: ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              10 ('restore_success')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

453            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              11 ('durations')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L2)
               NOT_TAKEN
               POP_TOP
               BUILD_MAP                0
       L2:     STORE_FAST               1 (durs)

454            LOAD_FAST_BORROW         1 (durs)
               TO_BOOL
               POP_JUMP_IF_FALSE       54 (to L6)
               NOT_TAKEN

455            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              12 ('  durations (s):')
               CALL                     1
               POP_TOP

456            LOAD_CONST              32 (('decrypt_s', 'unpack_s', 'verify_s', 'pg_restore_list_s', 'restore_sim_s', 'events_replay_s', 'integrity_check_s', 'monitoring_check_s', 'total_s'))
               GET_ITER
       L3:     FOR_ITER                36 (to L5)
               STORE_FAST               2 (k)

460            LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (k, durs)
               CONTAINS_OP              0 (in)
               POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L3)

461    L4:     LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              13 ('    ')
               LOAD_FAST_BORROW         2 (k)
               LOAD_CONST              14 ('<22')
               FORMAT_WITH_SPEC
               LOAD_CONST              15 (' ')
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (durs, k)
               BINARY_OP               26 ([])
               LOAD_CONST              16 ('.4f')
               FORMAT_WITH_SPEC
               BUILD_STRING             4
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           38 (to L3)

456    L5:     END_FOR
               POP_ITER

462    L6:     LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              17 ('  integrity_status:  ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              18 ('integrity_status')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

463            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              19 ('  monitoring_status: ')
               LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              20 ('monitoring_status')
               CALL                     1
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

464            LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              21 ('failures')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L7)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L7:     STORE_FAST               3 (fails)

465            LOAD_FAST_BORROW         3 (fails)
               TO_BOOL
               POP_JUMP_IF_FALSE       35 (to L10)
               NOT_TAKEN

466            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              22 ('  FAILURES:')
               CALL                     1
               POP_TOP

467            LOAD_FAST_BORROW         3 (fails)
               GET_ITER
       L8:     FOR_ITER                17 (to L9)
               STORE_FAST               4 (f)

468            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              23 ('    - ')
               LOAD_FAST_BORROW         4 (f)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L8)

467    L9:     END_FOR
               POP_ITER

469   L10:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              24 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L11)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L11:     STORE_FAST               5 (warns)

470            LOAD_FAST_BORROW         5 (warns)
               TO_BOOL
               POP_JUMP_IF_FALSE       35 (to L14)
               NOT_TAKEN

471            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              25 ('  warnings:')
               CALL                     1
               POP_TOP

472            LOAD_FAST_BORROW         5 (warns)
               GET_ITER
      L12:     FOR_ITER                17 (to L13)
               STORE_FAST               6 (w)

473            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              23 ('    - ')
               LOAD_FAST_BORROW         6 (w)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L12)

472   L13:     END_FOR
               POP_ITER

474   L14:     LOAD_FAST_BORROW         0 (report)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_CONST              26 ('simulated_commands')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L15)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
      L15:     STORE_FAST               7 (sims)

475            LOAD_FAST_BORROW         7 (sims)
               TO_BOOL
               POP_JUMP_IF_FALSE       35 (to L18)
               NOT_TAKEN

476            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              27 ('  simulated:')
               CALL                     1
               POP_TOP

477            LOAD_FAST_BORROW         7 (sims)
               GET_ITER
      L16:     FOR_ITER                17 (to L17)
               STORE_FAST               8 (s)

478            LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              28 ('    $ ')
               LOAD_FAST_BORROW         8 (s)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP
               JUMP_BACKWARD           19 (to L16)

477   L17:     END_FOR
               POP_ITER

479   L18:     LOAD_GLOBAL              1 (print + NULL)
               LOAD_CONST              30 ('========================================================================')
               CALL                     1
               POP_TOP
               LOAD_CONST              29 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "scripts\restore_drill.py", line 482>:
482           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('argv')
              LOAD_CONST               2 ('Optional[list]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object main at 0x0000018C17F723C0, file "scripts\restore_drill.py", line 482>:
 482            RESUME                   0

 483            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 484            LOAD_CONST               0 ('restore_drill')

 485            LOAD_CONST               1 ('PAS143G — offline disaster-recovery rehearsal.')

 483            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 487            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('--archive')
                LOAD_CONST               4 (True)

 488            LOAD_CONST               5 ('Path to the .pasbak file to drill.')

 487            LOAD_CONST               6 (('required', 'help'))
                CALL_KW                  3
                POP_TOP

 489            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               7 ('--passphrase-env')
                LOAD_CONST               4 (True)

 490            LOAD_CONST               8 ('Name of the env var holding the passphrase.')

 489            LOAD_CONST               6 (('required', 'help'))
                CALL_KW                  3
                POP_TOP

 491            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               9 ('--strict')
                LOAD_CONST              10 ('store_true')

 492            LOAD_CONST              11 ('Exit non-zero on any failure.')

 491            LOAD_CONST              12 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 493            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              13 ('--keep-temp')
                LOAD_CONST              10 ('store_true')

 494            LOAD_CONST              14 ("Don't delete the workspace; useful for forensics.")

 493            LOAD_CONST              12 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 495            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              15 ('--json')
                LOAD_CONST              10 ('store_true')

 496            LOAD_CONST              16 ('Emit the report as JSON to stdout.')

 495            LOAD_CONST              12 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 497            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              17 ('--note')
                LOAD_CONST              18 ('')

 498            LOAD_CONST              19 ('Free-text operator note recorded in the report.')

 497            LOAD_CONST              20 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 499            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 501            LOAD_GLOBAL              9 (Path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (archive)
                CALL                     1
                STORE_FAST               3 (archive)

 502            LOAD_FAST_BORROW         3 (archive)
                LOAD_ATTR               13 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        33 (to L1)
                NOT_TAKEN

 503            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              21 ('[FAIL] archive not found: ')
                LOAD_FAST_BORROW         3 (archive)
                FORMAT_SIMPLE
                BUILD_STRING             2
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              22 (('file',))
                CALL_KW                  2
                POP_TOP

 504            LOAD_SMALL_INT           4
                RETURN_VALUE

 506    L1:     LOAD_GLOBAL             21 (_read_passphrase + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               22 (passphrase_env)
                CALL                     1
                STORE_FAST               4 (passphrase)

 507            LOAD_FAST_BORROW         4 (passphrase)
                TO_BOOL
                POP_JUMP_IF_TRUE        44 (to L2)
                NOT_TAKEN

 508            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              23 ("[FAIL] passphrase env var '")
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               22 (passphrase_env)
                FORMAT_SIMPLE
                LOAD_CONST              24 ("' missing or empty")
                BUILD_STRING             3

 509            LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)

 508            LOAD_CONST              22 (('file',))
                CALL_KW                  2
                POP_TOP

 510            LOAD_SMALL_INT           3
                RETURN_VALUE

 512    L2:     LOAD_GLOBAL             25 (run_drill + NULL)

 513            LOAD_FAST_BORROW         3 (archive)

 514            LOAD_FAST_BORROW         4 (passphrase)

 515            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               26 (keep_temp)

 516            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (note)

 512            LOAD_CONST              25 (('keep_temp', 'operator_notes'))
                CALL_KW                  4
                STORE_FAST               5 (report)

 520            LOAD_GLOBAL              8 (Path)
                LOAD_ATTR               30 (cwd)
                PUSH_NULL
                CALL                     0
                LOAD_CONST              26 ('restore_drill_report.json')
                BINARY_OP               11 (/)
                STORE_FAST               6 (out_path)

 521            NOP

 522    L3:     LOAD_FAST_BORROW         6 (out_path)
                LOAD_ATTR               33 (write_text + NULL|self)
                LOAD_GLOBAL             34 (json)
                LOAD_ATTR               36 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              27 (('indent',))
                CALL_KW                  2
                LOAD_CONST              28 ('utf-8')
                LOAD_CONST              29 (('encoding',))
                CALL_KW                  2
                POP_TOP

 526    L4:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               34 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L5)
                NOT_TAKEN

 527            LOAD_GLOBAL             15 (print + NULL)
                LOAD_GLOBAL             34 (json)
                LOAD_ATTR               36 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW         5 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST              27 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP
                JUMP_FORWARD            25 (to L6)

 529    L5:     LOAD_GLOBAL             43 (_print_human + NULL)
                LOAD_FAST_BORROW         5 (report)
                CALL                     1
                POP_TOP

 530            LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              33 ('  report: ')
                LOAD_FAST_BORROW         6 (out_path)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 534    L6:     LOAD_GLOBAL             44 (any)
                COPY                     1
                LOAD_COMMON_CONSTANT     4 (<built-in function any>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       53 (to L11)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              34 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\restore_drill.py", line 534>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         5 (report)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              35 ('failures')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L7:     GET_ITER
                CALL                     0
        L8:     FOR_ITER                12 (to L10)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L8)
        L9:     POP_ITER
                LOAD_CONST               4 (True)
                JUMP_FORWARD            42 (to L13)
       L10:     END_FOR
                POP_ITER
                LOAD_CONST              36 (False)
                JUMP_FORWARD            38 (to L13)
       L11:     PUSH_NULL
                LOAD_CONST              34 (<code object <genexpr> at 0x0000018C18024E30, file "scripts\restore_drill.py", line 534>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         5 (report)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              35 ('failures')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L12:     GET_ITER
                CALL                     0
                CALL                     1
       L13:     TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L14)
                NOT_TAKEN

 535            LOAD_SMALL_INT           5
                RETURN_VALUE

 536   L14:     LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               48 (strict)
                TO_BOOL
                POP_JUMP_IF_FALSE       26 (to L15)
                NOT_TAKEN
                LOAD_FAST_BORROW         5 (report)
                LOAD_ATTR               47 (get + NULL|self)
                LOAD_CONST              37 ('restore_success')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN

 537            LOAD_SMALL_INT           1
                RETURN_VALUE

 538   L15:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 523            LOAD_GLOBAL             38 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 524   L17:     LOAD_GLOBAL             15 (print + NULL)
                LOAD_CONST              30 ('  [warn] could not write ')
                LOAD_FAST                6 (out_path)
                LOAD_ATTR               40 (name)
                FORMAT_SIMPLE
                LOAD_CONST              31 (': ')
                LOAD_FAST                7 (e)
                FORMAT_SIMPLE
                BUILD_STRING             4
                LOAD_GLOBAL             16 (sys)
                LOAD_ATTR               18 (stderr)
                LOAD_CONST              22 (('file',))
                CALL_KW                  2
                POP_TOP
       L18:     POP_EXCEPT
                LOAD_CONST              32 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 292 (to L4)

  --   L19:     LOAD_CONST              32 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 523   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L3 to L4 -> L16 [0]
  L16 to L17 -> L21 [1] lasti
  L17 to L18 -> L19 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024E30, file "scripts\restore_drill.py", line 534>:
 534           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                10 (to L3)
               STORE_FAST               1 (f)
               LOAD_CONST               0 ('MAC verification failed')
               LOAD_FAST_BORROW         1 (f)
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           12 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti
```
