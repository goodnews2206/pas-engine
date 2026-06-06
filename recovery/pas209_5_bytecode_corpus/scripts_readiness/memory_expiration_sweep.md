# scripts_readiness/memory_expiration_sweep

- **pyc:** `scripts\__pycache__\memory_expiration_sweep.cpython-314.pyc`
- **expected source path (absent):** `scripts/memory_expiration_sweep.py`
- **co_filename (from bytecode):** `scripts\memory_expiration_sweep.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS144D — Memory expiration sweep CLI.

Tenant-scoped utility that previews or performs the EXPIRED transition
for every ``pas_memory_records`` row whose ``expires_at`` has lapsed.
Wraps :mod:`app.services.memory.sweeper` and writes a structured
report to ``memory_expiration_sweep_report.json``.

Hard contract:

  * ``--brokerage-id`` is **required**. The CLI has no unscoped mode,
    and there is no flag to flip the helper into one.
  * ``--dry-run`` calls ``sweeper.find_expired_memory`` only. It does
    NOT call ``expire_due_memory`` and the records table is untouched.
  * Normal mode calls ``sweeper.expire_due_memory`` with
    ``actor_type="SYSTEM"`` and writes the resulting report verbatim.
  * The report file never includes raw evidence, metadata, lineage,
    summary, title, or evidence values from the underlying rows. Only
    structural fields (``memory_id``, ``kind``, ``status``,
    ``from_status``, ``to_status``, ``expires_at``, ``review_id``,
    ``warnings``, ``errors``) are persisted.
  * No LLM calls, no embeddings, no migrations, no production-data
    mutation outside the audited PAS144C transition.

Usage:
  python scripts/memory_expiration_sweep.py --brokerage-id brk-1
  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --dry-run
  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --limit 100
  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --json

Exit codes:
  0   success (sweep completed; ``failed == 0``)
  1   sweep completed with at least one ``failed`` row, or a
      structural warning was raised
  2   bad CLI arguments
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Path`, `__future__`, `annotations`, `app.services.memory`, `argparse`, `datetime`, `json`, `os`, `pathlib`, `sweeper`, `sys`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_parser`, `_dry_run`, `_live_sweep`, `_print_summary`, `_safe_result`, `_safe_row`, `_write_report`, `main`

## Env-key candidates

`SWEEP`, `SYSTEM`

## String constants (redacted where noted)

- '\nPAS144D — Memory expiration sweep CLI.\n\nTenant-scoped utility that previews or performs the EXPIRED transition\nfor every ``pas_memory_records`` row whose ``expires_at`` has lapsed.\nWraps :mod:`app.services.memory.sweeper` and writes a structured\nreport to ``memory_expiration_sweep_report.json``.\n\nHard contract:\n\n  * ``--brokerage-id`` is **required**. The CLI has no unscoped mode,\n    and there is no flag to flip the helper into one.\n  * ``--dry-run`` calls ``sweeper.find_expired_memory`` only. It does\n    NOT call ``expire_due_memory`` and the records table is untouched.\n  * Normal mode calls ``sweeper.expire_due_memory`` with\n    ``actor_type="SYSTEM"`` and writes the resulting report verbatim.\n  * The report file never includes raw evidence, metadata, lineage,\n    summary, title, or evidence values from the underlying rows. Only\n    structural fields (``memory_id``, ``kind``, ``status``,\n    ``from_status``, ``to_status``, ``expires_at``, ``review_id``,\n    ``warnings``, ``errors``) are persisted.\n  * No LLM calls, no embeddings, no migrations, no production-data\n    mutation outside the audited PAS144C transition.\n\nUsage:\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --dry-run\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --limit 100\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --json\n\nExit codes:\n  0   success (sweep completed; ``failed == 0``)\n  1   sweep completed with at least one ``failed`` row, or a\n      structural warning was raised\n  2   bad CLI arguments\n'
- 'utf-8'
- 'memory_expiration_sweep_report.json'
- 'row'
- 'Dict[str, Any]'
- 'return'
- 'Return a row dict containing only structural / non-sensitive\nfields. Never carries title/summary/evidence/lineage/metadata.'
- 'entry'
- 'Strip a per-row sweep result down to fields that are safe to\npersist on disk. Mirrors ``_safe_row`` for the transition phase.'
- 'argparse.ArgumentParser'
- 'memory_expiration_sweep'
- 'PAS144D — preview or perform the EXPIRED transition for memory rows whose TTL has lapsed. Tenant-scoped only.'
- '--brokerage-id'
- 'Required tenant identifier. There is no unscoped mode.'
- '--limit'
- "Maximum number of rows to consider in a single sweep. Clamped to the sweeper's hard ceiling."
- '--dry-run'
- 'store_true'
- 'List rows that WOULD expire without invoking the audited transition. The records table is not touched.'
- '--actor-id'
- 'Optional SYSTEM actor identifier for the audit trail.'
- '--reason'
- 'Optional reason string for the audit trail. PII is redacted and the value is truncated by PAS144C.'
- '--json'
- 'Emit the report JSON on stdout in addition to the file.'
- '--report-path'
- 'Where to write the structured report. Defaults to ./'
- 'report'
- 'dry_run'
- 'bool'
- 'None'
- 'Human-readable summary. Never includes raw evidence/metadata.'
- 'DRY-RUN'
- 'SWEEP'
- '] brokerage='
- 'brokerage_id'
- ' checked='
- 'checked'
- ' expired='
- 'expired'
- ' failed='
- 'failed'
- 'warnings'
- '  [warn] '
- 'path'
- 'str'
- 'payload'
- '  [warn] failed to write report at '
- 'args'
- 'argparse.Namespace'
- 'Find-only path. NEVER invokes ``expire_due_memory``.'
- 'mode'
- 'dry-run'
- 'generated_at'
- 'candidates'
- 'Audited path. Routes every row through review.expire_memory_by_id.'
- 'SYSTEM'
- 'live'
- 'results'
- 'argv'
- 'Optional[List[str]]'
- 'int'
- 'error: --brokerage-id must be a non-empty string'

## Disassembly

```
   0            RESUME                   0

   1            LOAD_CONST               0 ('\nPAS144D — Memory expiration sweep CLI.\n\nTenant-scoped utility that previews or performs the EXPIRED transition\nfor every ``pas_memory_records`` row whose ``expires_at`` has lapsed.\nWraps :mod:`app.services.memory.sweeper` and writes a structured\nreport to ``memory_expiration_sweep_report.json``.\n\nHard contract:\n\n  * ``--brokerage-id`` is **required**. The CLI has no unscoped mode,\n    and there is no flag to flip the helper into one.\n  * ``--dry-run`` calls ``sweeper.find_expired_memory`` only. It does\n    NOT call ``expire_due_memory`` and the records table is untouched.\n  * Normal mode calls ``sweeper.expire_due_memory`` with\n    ``actor_type="SYSTEM"`` and writes the resulting report verbatim.\n  * The report file never includes raw evidence, metadata, lineage,\n    summary, title, or evidence values from the underlying rows. Only\n    structural fields (``memory_id``, ``kind``, ``status``,\n    ``from_status``, ``to_status``, ``expires_at``, ``review_id``,\n    ``warnings``, ``errors``) are persisted.\n  * No LLM calls, no embeddings, no migrations, no production-data\n    mutation outside the audited PAS144C transition.\n\nUsage:\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --dry-run\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --limit 100\n  python scripts/memory_expiration_sweep.py --brokerage-id brk-1 --json\n\nExit codes:\n  0   success (sweep completed; ``failed == 0``)\n  1   sweep completed with at least one ``failed`` row, or a\n      structural warning was raised\n  2   bad CLI arguments\n')
                STORE_NAME               0 (__doc__)

  38            LOAD_SMALL_INT           0
                LOAD_CONST               1 (('annotations',))
                IMPORT_NAME              1 (__future__)
                IMPORT_FROM              2 (annotations)
                STORE_NAME               2 (annotations)
                POP_TOP

  40            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              3 (argparse)
                STORE_NAME               3 (argparse)

  41            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              4 (json)
                STORE_NAME               4 (json)

  42            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              5 (os)
                STORE_NAME               5 (os)

  43            LOAD_SMALL_INT           0
                LOAD_CONST               2 (None)
                IMPORT_NAME              6 (sys)
                STORE_NAME               6 (sys)

  44            LOAD_SMALL_INT           0
                LOAD_CONST               3 (('datetime', 'timezone'))
                IMPORT_NAME              7 (datetime)
                IMPORT_FROM              7 (datetime)
                STORE_NAME               7 (datetime)
                IMPORT_FROM              8 (timezone)
                STORE_NAME               8 (timezone)
                POP_TOP

  45            LOAD_SMALL_INT           0
                LOAD_CONST               4 (('Path',))
                IMPORT_NAME              9 (pathlib)
                IMPORT_FROM             10 (Path)
                STORE_NAME              10 (Path)
                POP_TOP

  46            LOAD_SMALL_INT           0
                LOAD_CONST               5 (('Any', 'Dict', 'List', 'Optional'))
                IMPORT_NAME             11 (typing)
                IMPORT_FROM             12 (Any)
                STORE_NAME              12 (Any)
                IMPORT_FROM             13 (Dict)
                STORE_NAME              13 (Dict)
                IMPORT_FROM             14 (List)
                STORE_NAME              14 (List)
                IMPORT_FROM             15 (Optional)
                STORE_NAME              15 (Optional)
                POP_TOP

  50            LOAD_NAME                6 (sys)
                LOAD_ATTR               32 (stdout)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               34 (stderr)
                BUILD_TUPLE              2
                GET_ITER
        L1:     FOR_ITER                22 (to L4)
                STORE_NAME              18 (_stream)

  51            NOP

  52    L2:     LOAD_NAME               18 (_stream)
                LOAD_ATTR               39 (reconfigure + NULL|self)
                LOAD_CONST               6 ('utf-8')
                LOAD_CONST               7 (('encoding',))
                CALL_KW                  1
                POP_TOP
        L3:     JUMP_BACKWARD           24 (to L1)

  50    L4:     END_FOR
                POP_ITER

  57            LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               45 (abspath + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               47 (join + NULL|self)
                LOAD_NAME                5 (os)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               49 (dirname + NULL|self)
                LOAD_NAME               25 (__file__)
                CALL                     1
                LOAD_CONST               8 ('..')
                CALL                     2
                CALL                     1
                STORE_NAME              26 (_REPO_ROOT)

  58            LOAD_NAME               26 (_REPO_ROOT)
                LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       29 (to L5)
                NOT_TAKEN

  59            LOAD_NAME                6 (sys)
                LOAD_ATTR               42 (path)
                LOAD_ATTR               55 (insert + NULL|self)
                LOAD_SMALL_INT           0
                LOAD_NAME               26 (_REPO_ROOT)
                CALL                     2
                POP_TOP

  62    L5:     LOAD_SMALL_INT           0
                LOAD_CONST               9 (('sweeper',))
                IMPORT_NAME             28 (app.services.memory)
                IMPORT_FROM             29 (sweeper)
                STORE_NAME              29 (sweeper)
                POP_TOP

  65            LOAD_CONST              10 ('memory_expiration_sweep_report.json')
                STORE_NAME              30 (REPORT_FILENAME)

  75            LOAD_NAME               31 (frozenset)
                PUSH_NULL
                BUILD_SET                0
                LOAD_CONST              28 (frozenset({'source', 'outcome_weight', 'confidence', 'kind', 'expires_at', 'ttl_days', 'memory_id', 'created_at', 'status'}))
                SET_UPDATE               1
                CALL                     1
                STORE_NAME              32 (_SAFE_ROW_FIELDS)

  87            LOAD_NAME               31 (frozenset)
                PUSH_NULL
                BUILD_SET                0
                LOAD_CONST              29 (frozenset({'from_status', 'review_id', 'kind', 'warnings', 'memory_id', 'to_status', 'errors', 'status'}))
                SET_UPDATE               1
                CALL                     1
                STORE_NAME              33 (_SAFE_RESULT_FIELDS)

  99            LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\memory_expiration_sweep.py", line 99>)
                MAKE_FUNCTION
                LOAD_CONST              12 (<code object _safe_row at 0x0000018C18039070, file "scripts\memory_expiration_sweep.py", line 99>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              34 (_safe_row)

 105            LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_expiration_sweep.py", line 105>)
                MAKE_FUNCTION
                LOAD_CONST              14 (<code object _safe_result at 0x0000018C18038670, file "scripts\memory_expiration_sweep.py", line 105>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              35 (_safe_result)

 115            LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\memory_expiration_sweep.py", line 115>)
                MAKE_FUNCTION
                LOAD_CONST              16 (<code object _build_parser at 0x0000018C17ECF940, file "scripts\memory_expiration_sweep.py", line 115>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              36 (_build_parser)

 174            LOAD_CONST              17 (<code object __annotate__ at 0x0000018C18026030, file "scripts\memory_expiration_sweep.py", line 174>)
                MAKE_FUNCTION
                LOAD_CONST              18 (<code object _print_summary at 0x0000018C17E58E00, file "scripts\memory_expiration_sweep.py", line 174>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              37 (_print_summary)

 188            LOAD_CONST              19 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\memory_expiration_sweep.py", line 188>)
                MAKE_FUNCTION
                LOAD_CONST              20 (<code object _write_report at 0x0000018C179C3C30, file "scripts\memory_expiration_sweep.py", line 188>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              38 (_write_report)

 204            LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_expiration_sweep.py", line 204>)
                MAKE_FUNCTION
                LOAD_CONST              22 (<code object _dry_run at 0x0000018C17EC5380, file "scripts\memory_expiration_sweep.py", line 204>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              39 (_dry_run)

 222            LOAD_CONST              23 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\memory_expiration_sweep.py", line 222>)
                MAKE_FUNCTION
                LOAD_CONST              24 (<code object _live_sweep at 0x0000018C17F84690, file "scripts\memory_expiration_sweep.py", line 222>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                STORE_NAME              40 (_live_sweep)

 243            LOAD_CONST              30 ((None,))
                LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\memory_expiration_sweep.py", line 243>)
                MAKE_FUNCTION
                LOAD_CONST              26 (<code object main at 0x0000018C181B49E0, file "scripts\memory_expiration_sweep.py", line 243>)
                MAKE_FUNCTION
                SET_FUNCTION_ATTRIBUTE  16 (annotate)
                SET_FUNCTION_ATTRIBUTE   1 (defaults)
                STORE_NAME              41 (main)

 278            LOAD_NAME               42 (__name__)
                LOAD_CONST              27 ('__main__')
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       26 (to L6)
                NOT_TAKEN

 279            LOAD_NAME                6 (sys)
                LOAD_ATTR               86 (exit)
                PUSH_NULL
                LOAD_NAME               41 (main)
                PUSH_NULL
                CALL                     0
                CALL                     1
                POP_TOP
                LOAD_CONST               2 (None)
                RETURN_VALUE

 278    L6:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

  53            LOAD_NAME               20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L9)
                NOT_TAKEN
                POP_TOP

  54    L8:     POP_EXCEPT
                EXTENDED_ARG             1
                JUMP_BACKWARD          272 (to L1)

  53    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L7 [1]
  L7 to L8 -> L10 [2] lasti
  L9 to L10 -> L10 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\memory_expiration_sweep.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_row at 0x0000018C18039070, file "scripts\memory_expiration_sweep.py", line 99>:
  99           RESUME                   0

 102           LOAD_GLOBAL              0 (_SAFE_ROW_FIELDS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                28 (to L5)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (row)
               CONTAINS_OP              0 (in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L2)
       L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, row)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 102           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [2]
  L4 to L6 -> L7 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "scripts\memory_expiration_sweep.py", line 105>:
105           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('entry')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_result at 0x0000018C18038670, file "scripts\memory_expiration_sweep.py", line 105>:
 105           RESUME                   0

 108           LOAD_GLOBAL              0 (_SAFE_RESULT_FIELDS)
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (k)
               SWAP                     2
       L1:     BUILD_MAP                0
               SWAP                     2
       L2:     FOR_ITER                28 (to L5)
               STORE_FAST_LOAD_FAST    17 (k, k)
               LOAD_FAST_BORROW         0 (entry)
               CONTAINS_OP              0 (in)
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           11 (to L2)
       L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 16 (k, entry)
               LOAD_ATTR                3 (get + NULL|self)
               LOAD_FAST_BORROW         1 (k)
               CALL                     1
               MAP_ADD                  2
               JUMP_BACKWARD           30 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     SWAP                     2
               STORE_FAST               1 (k)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 108           SWAP                     2
               STORE_FAST               1 (k)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [2]
  L4 to L6 -> L7 [2]

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\memory_expiration_sweep.py", line 115>:
115           RESUME                   0
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

Disassembly of <code object _build_parser at 0x0000018C17ECF940, file "scripts\memory_expiration_sweep.py", line 115>:
115           RESUME                   0

116           LOAD_GLOBAL              0 (argparse)
              LOAD_ATTR                2 (ArgumentParser)
              PUSH_NULL

117           LOAD_CONST               0 ('memory_expiration_sweep')

119           LOAD_CONST               1 ('PAS144D — preview or perform the EXPIRED transition for memory rows whose TTL has lapsed. Tenant-scoped only.')

116           LOAD_CONST               2 (('prog', 'description'))
              CALL_KW                  2
              STORE_FAST               0 (p)

123           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

124           LOAD_CONST               3 ('--brokerage-id')

125           LOAD_CONST               4 (True)

126           LOAD_CONST               5 ('Required tenant identifier. There is no unscoped mode.')

123           LOAD_CONST               6 (('required', 'help'))
              CALL_KW                  3
              POP_TOP

128           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

129           LOAD_CONST               7 ('--limit')

130           LOAD_GLOBAL              6 (int)

131           LOAD_SMALL_INT          50

133           LOAD_CONST               8 ("Maximum number of rows to consider in a single sweep. Clamped to the sweeper's hard ceiling.")

128           LOAD_CONST               9 (('type', 'default', 'help'))
              CALL_KW                  4
              POP_TOP

137           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

138           LOAD_CONST              10 ('--dry-run')

139           LOAD_CONST              11 ('store_true')

141           LOAD_CONST              12 ('List rows that WOULD expire without invoking the audited transition. The records table is not touched.')

137           LOAD_CONST              13 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

145           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

146           LOAD_CONST              14 ('--actor-id')

147           LOAD_CONST              15 (None)

148           LOAD_CONST              16 ('Optional SYSTEM actor identifier for the audit trail.')

145           LOAD_CONST              17 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

150           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

151           LOAD_CONST              18 ('--reason')

152           LOAD_CONST              15 (None)

154           LOAD_CONST              19 ('Optional reason string for the audit trail. PII is redacted and the value is truncated by PAS144C.')

150           LOAD_CONST              17 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

158           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

159           LOAD_CONST              20 ('--json')

160           LOAD_CONST              11 ('store_true')

161           LOAD_CONST              21 ('Emit the report JSON on stdout in addition to the file.')

158           LOAD_CONST              13 (('action', 'help'))
              CALL_KW                  3
              POP_TOP

163           LOAD_FAST_BORROW         0 (p)
              LOAD_ATTR                5 (add_argument + NULL|self)

164           LOAD_CONST              22 ('--report-path')

165           LOAD_GLOBAL              8 (REPORT_FILENAME)

167           LOAD_CONST              23 ('Where to write the structured report. Defaults to ./')

168           LOAD_GLOBAL              8 (REPORT_FILENAME)
              FORMAT_SIMPLE
              LOAD_CONST              24 ('.')

167           BUILD_STRING             3

163           LOAD_CONST              17 (('default', 'help'))
              CALL_KW                  3
              POP_TOP

171           LOAD_FAST_BORROW         0 (p)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\memory_expiration_sweep.py", line 174>:
174           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('dry_run')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _print_summary at 0x0000018C17E58E00, file "scripts\memory_expiration_sweep.py", line 174>:
174           RESUME                   0

176           LOAD_FAST_BORROW         1 (dry_run)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               1 ('DRY-RUN')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               2 ('SWEEP')
      L2:     STORE_FAST               2 (mode)

177           LOAD_GLOBAL              1 (print + NULL)

178           LOAD_CONST               3 ('[')
              LOAD_FAST_BORROW         2 (mode)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('] brokerage=')
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               5 ('brokerage_id')
              LOAD_CONST               6 ('')
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               7 (' checked=')

179           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST               8 ('checked')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST               9 (' expired=')

180           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              10 ('expired')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE
              LOAD_CONST              11 (' failed=')

181           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              12 ('failed')
              LOAD_SMALL_INT           0
              CALL                     2
              FORMAT_SIMPLE

178           BUILD_STRING            10

177           CALL                     1
              POP_TOP

183           LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                3 (get + NULL|self)
              LOAD_CONST              13 ('warnings')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L3:     STORE_FAST               3 (warnings)

184           LOAD_FAST_BORROW         3 (warnings)
              GET_ITER
      L4:     FOR_ITER                33 (to L5)
              STORE_FAST               4 (w)

185           LOAD_GLOBAL              1 (print + NULL)
              LOAD_CONST              14 ('  [warn] ')
              LOAD_FAST_BORROW         4 (w)
              FORMAT_SIMPLE
              BUILD_STRING             2
              LOAD_GLOBAL              4 (sys)
              LOAD_ATTR                6 (stderr)
              LOAD_CONST              15 (('file',))
              CALL_KW                  2
              POP_TOP
              JUMP_BACKWARD           35 (to L4)

184   L5:     END_FOR
              POP_ITER
              LOAD_CONST              16 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\memory_expiration_sweep.py", line 188>:
188           RESUME                   0
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
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _write_report at 0x0000018C179C3C30, file "scripts\memory_expiration_sweep.py", line 188>:
 188           RESUME                   0

 189           NOP

 190   L1:     LOAD_GLOBAL              1 (Path + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               LOAD_ATTR                3 (write_text + NULL|self)

 191           LOAD_GLOBAL              4 (json)
               LOAD_ATTR                6 (dumps)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (payload)
               LOAD_SMALL_INT           2
               LOAD_CONST               1 (True)
               LOAD_CONST               2 (('indent', 'sort_keys'))
               CALL_KW                  3

 192           LOAD_CONST               3 ('utf-8')

 190           LOAD_CONST               4 (('encoding',))
               CALL_KW                  2
               POP_TOP
       L2:     LOAD_CONST               8 (None)
               RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 194           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       64 (to L7)
               NOT_TAKEN
               STORE_FAST               2 (e)

 197   L4:     LOAD_GLOBAL             11 (print + NULL)

 198           LOAD_CONST               5 ('  [warn] failed to write report at ')
               LOAD_FAST                0 (path)
               FORMAT_SIMPLE
               LOAD_CONST               6 (': ')

 199           LOAD_GLOBAL             13 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               14 (__name__)
               FORMAT_SIMPLE

 198           BUILD_STRING             4

 200           LOAD_GLOBAL             16 (sys)
               LOAD_ATTR               18 (stderr)

 197           LOAD_CONST               7 (('file',))
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

 194   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\memory_expiration_sweep.py", line 204>:
204           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('args')
              LOAD_CONST               2 ('argparse.Namespace')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _dry_run at 0x0000018C17EC5380, file "scripts\memory_expiration_sweep.py", line 204>:
 204           RESUME                   0

 206           LOAD_GLOBAL              0 (sweeper)
               LOAD_ATTR                2 (find_expired_memory)
               PUSH_NULL

 207           LOAD_FAST_BORROW         0 (args)
               LOAD_ATTR                4 (brokerage_id)

 208           LOAD_FAST_BORROW         0 (args)
               LOAD_ATTR                6 (limit)

 206           LOAD_CONST               1 (('limit',))
               CALL_KW                  2
               STORE_FAST               1 (rows)

 211           LOAD_CONST               2 ('mode')
               LOAD_CONST               3 ('dry-run')

 212           LOAD_CONST               4 ('brokerage_id')
               LOAD_FAST_BORROW         0 (args)
               LOAD_ATTR                4 (brokerage_id)

 213           LOAD_CONST               5 ('generated_at')
               LOAD_GLOBAL              8 (datetime)
               LOAD_ATTR               10 (now)
               PUSH_NULL
               LOAD_GLOBAL             12 (timezone)
               LOAD_ATTR               14 (utc)
               CALL                     1
               LOAD_ATTR               17 (isoformat + NULL|self)
               CALL                     0

 214           LOAD_CONST               6 ('checked')
               LOAD_GLOBAL             19 (len + NULL)
               LOAD_FAST_BORROW         1 (rows)
               CALL                     1

 215           LOAD_CONST               7 ('expired')
               LOAD_SMALL_INT           0

 216           LOAD_CONST               8 ('failed')
               LOAD_SMALL_INT           0

 217           LOAD_CONST               9 ('candidates')
               LOAD_FAST_BORROW         1 (rows)
               GET_ITER
               LOAD_FAST_AND_CLEAR      2 (r)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                14 (to L3)
               STORE_FAST               2 (r)
               LOAD_GLOBAL             21 (_safe_row + NULL)
               LOAD_FAST_BORROW         2 (r)
               CALL                     1
               LIST_APPEND              2
               JUMP_BACKWARD           16 (to L2)
       L3:     END_FOR
               POP_ITER
       L4:     SWAP                     2
               STORE_FAST               2 (r)

 218           LOAD_CONST              10 ('warnings')
               BUILD_LIST               0

 210           BUILD_MAP                8
               RETURN_VALUE

  --   L5:     SWAP                     2
               POP_TOP

 217           SWAP                     2
               STORE_FAST               2 (r)
               RERAISE                  0
ExceptionTable:
  L1 to L4 -> L5 [15]

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\memory_expiration_sweep.py", line 222>:
222           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('args')
              LOAD_CONST               2 ('argparse.Namespace')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _live_sweep at 0x0000018C17F84690, file "scripts\memory_expiration_sweep.py", line 222>:
 222            RESUME                   0

 224            LOAD_GLOBAL              0 (sweeper)
                LOAD_ATTR                2 (expire_due_memory)
                PUSH_NULL

 225            LOAD_FAST_BORROW         0 (args)
                LOAD_ATTR                4 (brokerage_id)

 226            LOAD_CONST               1 ('SYSTEM')

 227            LOAD_FAST_BORROW         0 (args)
                LOAD_ATTR                6 (actor_id)

 228            LOAD_FAST_BORROW         0 (args)
                LOAD_ATTR                8 (reason)

 229            LOAD_FAST_BORROW         0 (args)
                LOAD_ATTR               10 (limit)

 224            LOAD_CONST               2 (('actor_type', 'actor_id', 'reason', 'limit'))
                CALL_KW                  5
                STORE_FAST               1 (raw)

 232            LOAD_CONST               3 ('mode')
                LOAD_CONST               4 ('live')

 233            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L1)
                NOT_TAKEN
                POP_TOP
                LOAD_FAST_BORROW         0 (args)
                LOAD_ATTR                4 (brokerage_id)

 234    L1:     LOAD_CONST               6 ('generated_at')
                LOAD_GLOBAL             14 (datetime)
                LOAD_ATTR               16 (now)
                PUSH_NULL
                LOAD_GLOBAL             18 (timezone)
                LOAD_ATTR               20 (utc)
                CALL                     1
                LOAD_ATTR               23 (isoformat + NULL|self)
                CALL                     0

 235            LOAD_CONST               7 ('checked')
                LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               7 ('checked')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L2:     CALL                     1

 236            LOAD_CONST               8 ('expired')
                LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               8 ('expired')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L3:     CALL                     1

 237            LOAD_CONST               9 ('failed')
                LOAD_GLOBAL             25 (int + NULL)
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST               9 ('failed')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L4:     CALL                     1

 238            LOAD_CONST              10 ('results')
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              10 ('results')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L5:     GET_ITER
                LOAD_FAST_AND_CLEAR      2 (e)
                SWAP                     2
        L6:     BUILD_LIST               0
                SWAP                     2
        L7:     FOR_ITER                14 (to L8)
                STORE_FAST               2 (e)
                LOAD_GLOBAL             27 (_safe_result + NULL)
                LOAD_FAST_BORROW         2 (e)
                CALL                     1
                LIST_APPEND              2
                JUMP_BACKWARD           16 (to L7)
        L8:     END_FOR
                POP_ITER
        L9:     SWAP                     2
                STORE_FAST               2 (e)

 239            LOAD_CONST              11 ('warnings')
                LOAD_GLOBAL             29 (list + NULL)
                LOAD_FAST_BORROW         1 (raw)
                LOAD_ATTR               13 (get + NULL|self)
                LOAD_CONST              11 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1

 231            BUILD_MAP                8
                RETURN_VALUE

  --   L11:     SWAP                     2
                POP_TOP

 238            SWAP                     2
                STORE_FAST               2 (e)
                RERAISE                  0
ExceptionTable:
  L6 to L9 -> L11 [15]

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\memory_expiration_sweep.py", line 243>:
243           RESUME                   0
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

Disassembly of <code object main at 0x0000018C181B49E0, file "scripts\memory_expiration_sweep.py", line 243>:
 243            RESUME                   0

 244            LOAD_GLOBAL              1 (_build_parser + NULL)
                CALL                     0
                STORE_FAST               1 (parser)

 245            NOP

 246    L1:     LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                3 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 251    L2:     LOAD_GLOBAL             11 (isinstance + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)
                LOAD_GLOBAL             14 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L3)
                NOT_TAKEN
                LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        30 (to L4)
                NOT_TAKEN

 252    L3:     LOAD_GLOBAL             19 (print + NULL)
                LOAD_CONST               2 ('error: --brokerage-id must be a non-empty string')
                LOAD_GLOBAL             20 (sys)
                LOAD_ATTR               22 (stderr)
                LOAD_CONST               3 (('file',))
                CALL_KW                  2
                POP_TOP

 253            LOAD_SMALL_INT           2
                RETURN_VALUE

 255    L4:     LOAD_FAST                2 (args)
                LOAD_ATTR               12 (brokerage_id)
                LOAD_ATTR               17 (strip + NULL|self)
                CALL                     0
                LOAD_FAST                2 (args)
                STORE_ATTR               6 (brokerage_id)

 257            LOAD_FAST                2 (args)
                LOAD_ATTR               24 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE       13 (to L5)
                NOT_TAKEN

 258            LOAD_GLOBAL             27 (_dry_run + NULL)
                LOAD_FAST                2 (args)
                CALL                     1
                STORE_FAST               4 (report)
                JUMP_FORWARD            11 (to L6)

 260    L5:     LOAD_GLOBAL             29 (_live_sweep + NULL)
                LOAD_FAST                2 (args)
                CALL                     1
                STORE_FAST               4 (report)

 262    L6:     LOAD_GLOBAL             31 (_write_report + NULL)
                LOAD_FAST                2 (args)
                LOAD_ATTR               32 (report_path)
                LOAD_FAST                4 (report)
                CALL                     2
                POP_TOP

 263            LOAD_GLOBAL             35 (_print_summary + NULL)
                LOAD_FAST_LOAD_FAST     66 (report, args)
                LOAD_ATTR               24 (dry_run)
                LOAD_CONST               4 (('dry_run',))
                CALL_KW                  2
                POP_TOP

 265            LOAD_FAST                2 (args)
                LOAD_ATTR               36 (json)
                TO_BOOL
                POP_JUMP_IF_FALSE       35 (to L7)
                NOT_TAKEN

 268            LOAD_GLOBAL             19 (print + NULL)
                LOAD_GLOBAL             36 (json)
                LOAD_ATTR               38 (dumps)
                PUSH_NULL
                LOAD_FAST                4 (report)
                LOAD_SMALL_INT           2
                LOAD_CONST               5 (True)
                LOAD_CONST               6 (('indent', 'sort_keys'))
                CALL_KW                  3
                CALL                     1
                POP_TOP

 271    L7:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST                4 (report)
                LOAD_ATTR               41 (get + NULL|self)
                LOAD_CONST               7 ('failed')
                LOAD_SMALL_INT           0
                CALL                     2
                CALL                     1
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 272            LOAD_SMALL_INT           1
                RETURN_VALUE

 273    L8:     LOAD_FAST                4 (report)
                LOAD_ATTR               41 (get + NULL|self)
                LOAD_CONST               8 ('warnings')
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN

 274            LOAD_SMALL_INT           1
                RETURN_VALUE

 275    L9:     LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 247            LOAD_GLOBAL              4 (SystemExit)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       61 (to L19)
                NOT_TAKEN
                STORE_FAST               3 (e)

 249   L11:     LOAD_FAST                3 (e)
                LOAD_ATTR                6 (code)
                LOAD_CONST               9 ((0, None))
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

 247   L19:     RERAISE                  0

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
