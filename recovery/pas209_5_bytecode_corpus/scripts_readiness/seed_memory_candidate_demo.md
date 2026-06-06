# scripts_readiness/seed_memory_candidate_demo

- **pyc:** `scripts\__pycache__\seed_memory_candidate_demo.cpython-314.pyc`
- **expected source path (absent):** `scripts/seed_memory_candidate_demo.py`
- **co_filename (from bytecode):** `scripts\seed_memory_candidate_demo.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS163 — Memory candidate demo seed.

Builds a deterministic replay-shaped event bundle and runs it
through ``app/services/memory/candidate_pipeline.py`` so an
operator can see at least one CANDIDATE row appear in the
Memory Review console without dialing a real call or touching
production data.

Doctrine:

* **No production data touched.** The seed builds a synthetic
  reconstruction bundle in memory; it does not read or write
  any tenant call/event row.
* **No raw transcript printed.** The structural report prints
  pending_call_id / call_id (synthetic) / source / counts only.
  Phone / email / name / transcript NEVER appear in stdout.
* **Brokerage_id required** unless ``--demo`` is supplied. The
  demo brokerage_id is a fixed, obviously-fake string
  (``brk-demo-pas163``) so a candidate created with it can be
  distinguished from real tenant data and pruned trivially.
* **Fails safely on storage absence.** If
  ``app.services.memory.store.insert_memory`` is unreachable
  (no Supabase wiring, no service key), the pipeline returns
  ``status="skipped"`` with ``missing_storage_helper``. The
  seed surfaces that as a structural report — no traceback.

Usage:
    python scripts/seed_memory_candidate_demo.py --brokerage-id brk-1
    python scripts/seed_memory_candidate_demo.py --demo
    python scripts/seed_memory_candidate_demo.py --demo --json

Exit codes:
    0  — pipeline ran (status ``ok`` or ``skipped``)
    1  — pipeline returned status ``failed``
    2  — bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.services.memory.candidate_pipeline`, `argparse`, `generate_memory_candidates_from_replay`, `json`, `os`, `sys`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_demo_reconstruction`, `_build_parser`, `_print_summary`, `_run_pipeline`, `main`

## Env-key candidates

`SYSTEM`

## String constants (redacted where noted)

- '\nPAS163 — Memory candidate demo seed.\n\nBuilds a deterministic replay-shaped event bundle and runs it\nthrough ``app/services/memory/candidate_pipeline.py`` so an\noperator can see at least one CANDIDATE row appear in the\nMemory Review console without dialing a real call or touching\nproduction data.\n\nDoctrine:\n\n* **No production data touched.** The seed builds a synthetic\n  reconstruction bundle in memory; it does not read or write\n  any tenant call/event row.\n* **No raw transcript printed.** The structural report prints\n  pending_call_id / call_id (synthetic) / source / counts only.\n  Phone / email / name / transcript NEVER appear in stdout.\n* **Brokerage_id required** unless ``--demo`` is supplied. The\n  demo brokerage_id is a fixed, obviously-fake string\n  (``brk-demo-pas163``) so a candidate created with it can be\n  distinguished from real tenant data and pruned trivially.\n* **Fails safely on storage absence.** If\n  ``app.services.memory.store.insert_memory`` is unreachable\n  (no Supabase wiring, no service key), the pipeline returns\n  ``status="skipped"`` with ``missing_storage_helper``. The\n  seed surfaces that as a structural report — no traceback.\n\nUsage:\n    python scripts/seed_memory_candidate_demo.py --brokerage-id brk-1\n    python scripts/seed_memory_candidate_demo.py --demo\n    python scripts/seed_memory_candidate_demo.py --demo --json\n\nExit codes:\n    0  — pipeline ran (status ``ok`` or ``skipped``)\n    1  — pipeline returned status ``failed``\n    2  — bad CLI arguments\n'
- 'utf-8'
- 'brk-demo-pas163'
- 'brokerage_id'
- 'str'
- 'return'
- 'Dict[str, Any]'
- 'Return a small replay-reconstruction-shaped dict that the\ncandidate pipeline can classify into a CANDIDATE record.\nNEVER carries raw transcript, phone, email, or name.'
- 'call_id'
- 'demo-call-pas163'
- 'final_outcome'
- 'booked'
- 'events_count'
- 'is_replayable'
- 'missing_lifecycle_steps'
- 'followup_scheduled'
- 'extracted_fields'
- 'intent'
- 'value'
- 'buying'
- 'confidence'
- 'budget'
- '$400k-$600k'
- 'timeline'
- '3 months'
- 'workflow_stages_seen'
- 'argparse.ArgumentParser'
- 'seed_memory_candidate_demo'
- 'PAS163 — Seed a synthetic CANDIDATE memory record so Memory Review has at least one real input. No production data touched. No raw transcript printed.'
- '--brokerage-id'
- 'Brokerage scope for the candidate. Required UNLESS --demo is supplied (which uses the obviously-fake id '
- '--demo'
- 'store_true'
- 'Use the built-in demo brokerage_id. Skips the --brokerage-id requirement. Safe for local seed runs.'
- '--json'
- 'Emit the full pipeline report as JSON on stdout.'
- '--actor-id'
- 'Optional operator actor_id stamped on the lineage.'
- 'report'
- 'None'
- 'status'
- 'candidates_created'
- 'failed'
- 'warnings'
- 'results'
- '[PAS163-seed] status='
- ' brokerage='
- ' candidates_created='
- ' failed='
- ' warning_count='
- '  - warning: '
- '  ... and '
- ' more'
- 'memory_id'
- 'kind'
- '  - candidate memory_id='
- ' status='
- ' kind='
- 'actor_id'
- 'Optional[str]'
- 'candidate_pipeline_unimportable:'
- 'SYSTEM'
- 'pipeline_call_exception:'
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --brokerage-id is required unless --demo is supplied'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS163 — Memory candidate demo seed.\n\nBuilds a deterministic replay-shaped event bundle and runs it\nthrough ``app/services/memory/candidate_pipeline.py`` so an\noperator can see at least one CANDIDATE row appear in the\nMemory Review console without dialing a real call or touching\nproduction data.\n\nDoctrine:\n\n* **No production data touched.** The seed builds a synthetic\n  reconstruction bundle in memory; it does not read or write\n  any tenant call/event row.\n* **No raw transcript printed.** The structural report prints\n  pending_call_id / call_id (synthetic) / source / counts only.\n  Phone / email / name / transcript NEVER appear in stdout.\n* **Brokerage_id required** unless ``--demo`` is supplied. The\n  demo brokerage_id is a fixed, obviously-fake string\n  (``brk-demo-pas163``) so a candidate created with it can be\n  distinguished from real tenant data and pruned trivially.\n* **Fails safely on storage absence.** If\n  ``app.services.memory.store.insert_memory`` is unreachable\n  (no Supabase wiring, no service key), the pipeline returns\n  ``status="skipped"`` with ``missing_storage_helper``. The\n  seed surfaces that as a structural report — no traceback.\n\nUsage:\n    python scripts/seed_memory_candidate_demo.py --brokerage-id brk-1\n    python scripts/seed_memory_candidate_demo.py --demo\n    python scripts/seed_memory_candidate_demo.py --demo --json\n\nExit codes:\n    0  — pipeline ran (status ``ok`` or ``skipped``)\n    1  — pipeline returned status ``failed``\n    2  — bad CLI arguments\n')
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
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  43            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  44            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  45            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
                IMPORT_NAME              7 (typing)
                IMPORT_FROM              8 (Any)
                STORE_NAME               8 (Any)
                IMPORT_FROM              9 (Dict)
                STORE_NAME               9 (Dict)
                IMPORT_FROM             10 (List)
                STORE_NAME              10 (List)
                IMPORT_FROM             11 (Optional)
                STORE_NAME              11 (Optional)
                POP_TOP

  48            LOAD_NAME                6 (sys)
                LOAD_ATTR               24 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               26 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              14 (_stream)

  49            NOP

  50    L2:     LOAD_NAME               14 (_stream)
                LOAD_ATTR               31 (reconfigure + NULL|self)
                LOAD_CONST               4 ('utf-8')
                LOAD_CONST               5 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  48    L4:     END_FOR
                POP_ITER

  55            LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               37 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               39 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               41 (dirname + NULL|self)
                LOAD_NAME               21 (__file__)
                CALL                     1
                LOAD_CONST               6 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              22 (_REPO_ROOT)

  56            LOAD_NAME               22 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  57            LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (path)
                LOAD_ATTR               47 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               22 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  60    L5:     LOAD_CONST               7 ('brk-demo-pas163')
                STORE_NAME              24 (_DEMO_BROKERAGE_ID)

  63            LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\seed_memory_candidate_demo.py", line 63>)
                MAKE_FUNCTION
                LOAD_CONST               9 (<code object _build_demo_reconstruction at 0x0000018C180533F0, file "scripts\seed_memory_candidate_demo.py", line 63>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              25 (_build_demo_reconstruction)

  88            LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA3780, file "scripts\seed_memory_candidate_demo.py", line 88>)
                MAKE_FUNCTION
                LOAD_CONST              11 (<code object _build_parser at 0x0000018C1794ED80, file "scripts\seed_memory_candidate_demo.py", line 88>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              26 (_build_parser)

 123            LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3E10, file "scripts\seed_memory_candidate_demo.py", line 123>)
                MAKE_FUNCTION
                LOAD_CONST              13 (<code object _print_summary at 0x0000018C17D78680, file "scripts\seed_memory_candidate_demo.py", line 123>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              27 (_print_summary)

 147            LOAD_CONST              14 (<code object __annotate__ at 0x0000018C18024B30, file "scripts\seed_memory_candidate_demo.py", line 147>)
                MAKE_FUNCTION
                LOAD_CONST              15 (<code object _run_pipeline at 0x0000018C17F005F0, file "scripts\seed_memory_candidate_demo.py", line 147>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              28 (_run_pipeline)

 184            LOAD_CONST              19 ((None,))
                LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\seed_memory_candidate_demo.py", line 184>)
                MAKE_FUNCTION
                LOAD_CONST              17 (<code object main at 0x0000018C17D87300, file "scripts\seed_memory_candidate_demo.py", line 184>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              29 (main)

 218            LOAD_NAME               30 (__name__)
                LOAD_CONST              18 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 219            LOAD_NAME                6 (sys)
                LOAD_ATTR               62 (exit)
                PUSH_NULL
                LOAD_NAME               29 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 218    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  51            LOAD_NAME               16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

  52    L8:     POP_EXCEPT
                JUMP_BACKWARD          227 (to L1)

  51    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\seed_memory_candidate_demo.py", line 63>:
 63           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _build_demo_reconstruction at 0x0000018C180533F0, file "scripts\seed_memory_candidate_demo.py", line 63>:
 63           RESUME                   0

 68           LOAD_CONST               1 ('call_id')
              LOAD_CONST               2 ('demo-call-pas163')

 69           LOAD_CONST               3 ('brokerage_id')
              LOAD_FAST_BORROW         0 (brokerage_id)

 70           LOAD_CONST               4 ('final_outcome')
              LOAD_CONST               5 ('booked')

 71           LOAD_CONST               6 ('events_count')
              LOAD_SMALL_INT          14

 72           LOAD_CONST               7 ('is_replayable')
              LOAD_CONST               8 (True)

 73           LOAD_CONST               9 ('missing_lifecycle_steps')
              LOAD_CONST              10 ('followup_scheduled')
              BUILD_LIST               1

 74           LOAD_CONST              11 ('extracted_fields')

 75           LOAD_CONST              12 ('intent')
              LOAD_CONST              13 ('value')
              LOAD_CONST              14 ('buying')
              LOAD_CONST              15 ('confidence')
              LOAD_CONST              16 (0.9)
              BUILD_MAP                2

 76           LOAD_CONST              17 ('budget')
              LOAD_CONST              13 ('value')
              LOAD_CONST              18 ('$400k-$600k')
              LOAD_CONST              15 ('confidence')
              LOAD_CONST              19 (0.85)
              BUILD_MAP                2

 77           LOAD_CONST              20 ('timeline')
              LOAD_CONST              13 ('value')
              LOAD_CONST              21 ('3 months')
              LOAD_CONST              15 ('confidence')
              LOAD_CONST              22 (0.8)
              BUILD_MAP                2

 74           BUILD_MAP                3

 80           LOAD_CONST              23 ('workflow_stages_seen')
              BUILD_LIST               0
              LOAD_CONST              24 (('lead_received', 'pas_calling', 'intent_captured', 'budget_captured', 'timeline_captured', 'booking_attempted', 'booking_confirmed', 'completed'))
              LIST_EXTEND              1

 67           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "scripts\seed_memory_candidate_demo.py", line 88>:
 88           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C1794ED80, file "scripts\seed_memory_candidate_demo.py", line 88>:
 88           RESUME                   0

 89           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

 90           LOAD_CONST               0 ('seed_memory_candidate_demo')

 92           LOAD_CONST               1 ('PAS163 — Seed a synthetic CANDIDATE memory record so Memory Review has at least one real input. No production data touched. No raw transcript printed.')

 89           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

 97           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

 98           LOAD_CONST               3 ('--brokerage-id')
              LOAD_GLOBAL              6 (str)
              LOAD_CONST               4 (None)

100           LOAD_CONST               5 ('Brokerage scope for the candidate. Required UNLESS --demo is supplied (which uses the obviously-fake id ')

102           LOAD_GLOBAL              8 (_DEMO_BROKERAGE_ID)
              CONVERT_VALUE            2 (repr)
              FORMAT_SIMPLE
              LOAD_CONST               6 (').')

100           BUILD_STRING             3

 97           LOAD_CONST               7 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

105           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

106           LOAD_CONST               8 ('--demo')
              LOAD_CONST               9 ('store_true')

108           LOAD_CONST              10 ('Use the built-in demo brokerage_id. Skips the --brokerage-id requirement. Safe for local seed runs.')

105           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

112           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

113           LOAD_CONST              12 ('--json')
              LOAD_CONST               9 ('store_true')

114           LOAD_CONST              13 ('Emit the full pipeline report as JSON on stdout.')

112           LOAD_CONST              11 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

116           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

117           LOAD_CONST              14 ('--actor-id')
              LOAD_GLOBAL              6 (str)
              LOAD_CONST               4 (None)

118           LOAD_CONST              15 ('Optional operator actor_id stamped on the lineage.')

116           LOAD_CONST               7 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

120           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3E10, file "scripts\seed_memory_candidate_demo.py", line 123>:
123           RESUME                   0
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

Disassembly of <code object _print_summary at 0x0000018C17D78680, file "scripts\seed_memory_candidate_demo.py", line 123>:
123           RESUME                   0

124           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              STORE_FAST               1 (status)

125           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               1 ('brokerage_id')
              CALL                     1
              STORE_FAST               2 (bid)

126           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               2 ('candidates_created')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               3 (created)

127           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               3 ('failed')
              LOAD_SMALL_INT           0
              CALL                     2
              STORE_FAST               4 (failed)

128           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               4 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     STORE_FAST               5 (warnings)

129           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               5 ('results')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     STORE_FAST               6 (results)

130           LOAD_GLOBAL              3 (print + NULL)

131           LOAD_CONST               6 ('[PAS163-seed] status=')
              LOAD_FAST_BORROW         1 (status)
              FORMAT_SIMPLE
              LOAD_CONST               7 (' brokerage=')
              LOAD_FAST_BORROW         2 (bid)
              FORMAT_SIMPLE
              LOAD_CONST               8 (' candidates_created=')

132           LOAD_FAST_BORROW         3 (created)
              FORMAT_SIMPLE
              LOAD_CONST               9 (' failed=')
              LOAD_FAST_BORROW         4 (failed)
              FORMAT_SIMPLE
              LOAD_CONST              10 (' warning_count=')

133           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              FORMAT_SIMPLE

131           BUILD_STRING            10

130           CALL                     1
              POP_TOP

135           LOAD_FAST_BORROW         5 (warnings)
              LOAD_CONST              11 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L3:     FOR_ITER                17 (to L4)
              STORE_FAST               7 (w)

137           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              12 ('  - warning: ')
              LOAD_FAST_BORROW         7 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           19 (to L3)

135   L4:     END_FOR
              POP_ITER

138           LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              LOAD_SMALL_INT          10
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       32 (to L5)
              NOT_TAKEN

139           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              13 ('  ... and ')
              LOAD_GLOBAL              5 (len + NULL)
              LOAD_FAST_BORROW         5 (warnings)
              CALL                     1
              LOAD_SMALL_INT          10
              BINARY_OP               10 (-)
              FORMAT_SIMPLE
              LOAD_CONST              14 (' more')
              BUILD_STRING             3
              CALL                     1
              POP_TOP

140   L5:     LOAD_FAST_BORROW         6 (results)
              LOAD_CONST              11 (slice(None, 10, None))
              BINARY_OP               26 ([])
              GET_ITER
      L6:     FOR_ITER                74 (to L7)
              STORE_FAST               8 (r)

141           LOAD_FAST_BORROW         8 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              15 ('memory_id')
              CALL                     1
              STORE_FAST               9 (mid)

142           LOAD_FAST_BORROW         8 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST               0 ('status')
              CALL                     1
              STORE_FAST              10 (st)

143           LOAD_FAST_BORROW         8 (r)
              LOAD_ATTR                1 (get + NULL|self)
              LOAD_CONST              16 ('kind')
              CALL                     1
              STORE_FAST              11 (kind)

144           LOAD_GLOBAL              3 (print + NULL)
              LOAD_CONST              17 ('  - candidate memory_id=')
              LOAD_FAST_BORROW         9 (mid)
              FORMAT_SIMPLE
              LOAD_CONST              18 (' status=')
              LOAD_FAST_BORROW        10 (st)
              FORMAT_SIMPLE
              LOAD_CONST              19 (' kind=')
              LOAD_FAST_BORROW        11 (kind)
              FORMAT_SIMPLE
              BUILD_STRING             6
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           76 (to L6)

140   L7:     END_FOR
              POP_ITER
              LOAD_CONST              20 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "scripts\seed_memory_candidate_demo.py", line 147>:
147           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

148           LOAD_CONST               2 ('str')

147           LOAD_CONST               3 ('actor_id')

148           LOAD_CONST               4 ('Optional[str]')

147           LOAD_CONST               5 ('return')

149           LOAD_CONST               6 ('Dict[str, Any]')

147           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _run_pipeline at 0x0000018C17F005F0, file "scripts\seed_memory_candidate_demo.py", line 147>:
 147            RESUME                   0

 150            NOP

 151    L1:     LOAD_SMALL_INT           0
                LOAD_CONST               1 (('generate_memory_candidates_from_replay',))
                IMPORT_NAME              0 (app.services.memory.candidate_pipeline)
                IMPORT_FROM              1 (generate_memory_candidates_from_replay)
                STORE_FAST               2 (generate_memory_candidates_from_replay)
                POP_TOP

 163    L2:     LOAD_GLOBAL             11 (_build_demo_reconstruction + NULL)
                LOAD_FAST                0 (brokerage_id)
                CALL                     1
                STORE_FAST               4 (bundle)

 164            NOP

 165    L3:     LOAD_FAST                2 (generate_memory_candidates_from_replay)
                PUSH_NULL

 166            LOAD_FAST                4 (bundle)

 167            LOAD_FAST                0 (brokerage_id)

 168            LOAD_CONST              10 ('SYSTEM')

 169            LOAD_FAST                1 (actor_id)

 165            LOAD_CONST              11 (('brokerage_id', 'actor_type', 'actor_id'))
                CALL_KW                  4
        L4:     RETURN_VALUE

  --    L5:     PUSH_EXC_INFO

 154            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       48 (to L10)
                NOT_TAKEN
                STORE_FAST               3 (e)

 156    L6:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 157            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 158            LOAD_CONST               5 ('candidates_created')
                LOAD_SMALL_INT           0

 159            LOAD_CONST               3 ('failed')
                LOAD_SMALL_INT           1

 160            LOAD_CONST               6 ('warnings')
                LOAD_CONST               7 ('candidate_pipeline_unimportable:')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 161            LOAD_CONST               8 ('results')
                BUILD_LIST               0

 155            BUILD_MAP                6
        L7:     SWAP                     2
        L8:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --    L9:     LOAD_CONST               9 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 154   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L12:     PUSH_EXC_INFO

 171            LOAD_GLOBAL              4 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       48 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 175   L13:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 176            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                0 (brokerage_id)

 177            LOAD_CONST               5 ('candidates_created')
                LOAD_SMALL_INT           0

 178            LOAD_CONST               3 ('failed')
                LOAD_SMALL_INT           1

 179            LOAD_CONST               6 ('warnings')
                LOAD_CONST              12 ('pipeline_call_exception:')
                LOAD_GLOBAL              7 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR                8 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 180            LOAD_CONST               8 ('results')
                BUILD_LIST               0

 174            BUILD_MAP                6
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               9 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 171   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L3 to L4 -> L12 [0]
  L5 to L6 -> L11 [1] lasti
  L6 to L7 -> L9 [1] lasti
  L7 to L8 -> L11 [1] lasti
  L9 to L11 -> L11 [1] lasti
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\seed_memory_candidate_demo.py", line 184>:
184           RESUME                   0
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

Disassembly of <code object main at 0x0000018C17D87300, file "scripts\seed_memory_candidate_demo.py", line 184>:
 184            RESUME                   0

 185            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 186            NOP

 187    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 191    L2:     LOAD_CONST               1 (None)
                STORE_FAST               4 (brokerage_id)

 192            LOAD_FAST                2 (args)
                LOAD_ATTR               10 (demo)
                TO_BOOL
                POP_JUMP_IF_FALSE        8 (to L3)
                NOT_TAKEN

 193            LOAD_GLOBAL             12 (_DEMO_BROKERAGE_ID)
                STORE_FAST               4 (brokerage_id)
                JUMP_FORWARD            76 (to L4)

 194    L3:     LOAD_FAST                2 (args)
                LOAD_ATTR               14 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       59 (to L4)
                NOT_TAKEN
                LOAD_FAST                2 (args)
                LOAD_ATTR               14 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L4)
                NOT_TAKEN

 195            LOAD_FAST                2 (args)
                LOAD_ATTR               14 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                STORE_FAST               4 (brokerage_id)

 197    L4:     LOAD_FAST                4 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L5)
                NOT_TAKEN

 198            LOAD_GLOBAL             19 (print + NULL)

 199            LOAD_CONST               2 ('error: --brokerage-id is required unless --demo is supplied')

 200            LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)

 198            LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 202            LOAD_SMALL_INT           2
                RETURN_VALUE

 204    L5:     LOAD_GLOBAL             25 (isinstance + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (actor_id)
                LOAD_GLOBAL             28 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       59 (to L6)
                NOT_TAKEN
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (actor_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       27 (to L6)
                NOT_TAKEN
                LOAD_FAST                2 (args)
                LOAD_ATTR               26 (actor_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               1 (None)
        L7:     STORE_FAST               5 (actor_id)

 206            LOAD_GLOBAL             31 (_run_pipeline + NULL)
                LOAD_FAST_LOAD_FAST     69 (brokerage_id, actor_id)
                CALL                     2
                STORE_FAST               6 (report)

 207            LOAD_GLOBAL             33 (_print_summary + NULL)
                LOAD_FAST                6 (report)
                CALL                     1
                POP_TOP

 209            LOAD_FAST                2 (args)
                LOAD_ATTR               34 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L8)
                NOT_TAKEN

 210            LOAD_GLOBAL             19 (print + NULL)
                LOAD_GLOBAL             34 (json)
                LOAD_ATTR               36 (dumps)
                PUSH_NULL
                LOAD_FAST                6 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 212    L8:     LOAD_FAST                6 (report)
                LOAD_ATTR               39 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                STORE_FAST               7 (status)

 213            LOAD_FAST                7 (status)
                LOAD_CONST               7 ('failed')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 214            LOAD_SMALL_INT           1
                RETURN_VALUE

 215    L9:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 188            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L19)
                NOT_TAKEN
                STORE_FAST               3 (e)

 189   L11:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               8 ((0, None))
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L12)
                NOT_TAKEN
                LOAD_SMALL_INT           2
                JUMP_FORWARD            30 (to L16)
       L12:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_SMALL_INT           0
       L15:     CALL                     1
       L16:     SWAP                     2
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L18:     LOAD_CONST               1 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 188   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L10 to L11 -> L20 [1] lasti
  L11 to L13 -> L18 [1] lasti
  L14 to L16 -> L18 [1] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti
```
