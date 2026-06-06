# memory/review_export

- **pyc:** `app\services\memory\__pycache__\review_export.cpython-314.pyc`
- **expected source path (absent):** `app\services\memory/review_export.py`
- **co_filename (from bytecode):** `app\services\memory\review_export.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** memory

## Module docstring

```
PAS152 — Memory review CSV export (read-only, structural).

Bounded, tenant-scoped CSV projection over the same PAS144C
``pas_memory_review_events`` audit table that PAS150 / PAS151 already
read. Gives operators an offline-analysis path (paste into a
spreadsheet, dump into a notebook) WITHOUT needing direct Supabase
access and WITHOUT exposing any of the reason / metadata / evidence /
transcript surface that the PAS149 drilldown deliberately gates.

Hard contract:
  * **Tenant-scoped.** Every public helper that touches Supabase
    requires ``brokerage_id``. There is no unscoped path.
  * **Bounded.** ``memory_review_events_csv_for_brokerage`` caps the
    row fetch at ``_MAX_EXPORT_LIMIT`` (500, mirrors PAS150). The
    query has both a ``brokerage_id`` equality and an ``ORDER BY
    created_at DESC LIMIT n`` — NOT a full-table scan.
  * **Structural output only.** The CSV carries four base columns
    (``created_at``, ``to_status``, ``actor_type``, ``actor_id``)
    plus two derived columns (``day``, ``status_group``). Reason
    text, metadata JSONB, evidence, transcript, raw prompts and
    lineage are NEVER read or surfaced. The projection physically
    does not look at those keys.
  * **CSV escaping via the stdlib ``csv`` module.** No manual
    string concatenation. Embedded commas, quotes, newlines in
    structural tokens are escaped correctly.
  * **Fail-closed.** Bad input, reader failure, malformed event row
    — every path returns a structured envelope with a header-only
    CSV and warning tokens. Nothing in this module raises.

Public surface:
  - csv_rows_from_review_events(events)                  -> list[dict]
  - render_review_events_csv(rows)                        -> str
  - memory_review_events_csv_for_brokerage(
        brokerage_id, since=None, limit=500)              -> dict
  - CSV_COLUMNS, FORBIDDEN_EXPORT_FIELDS, _MAX_EXPORT_LIMIT
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.db.supabase_client`, `csv`, `get_supabase`, `io`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_limit`, `_coerce_actor_id_filter`, `_coerce_actor_type_filter`, `_coerce_since`, `_coerce_to_status_filter`, `_empty_csv`, `_get_db`, `_list_review_events_for_brokerage`, `_parse_iso_day`, `_safe_str`, `_status_group`, `csv_rows_from_review_events`, `memory_review_events_csv_for_brokerage`, `render_review_events_csv`

## Env-key candidates

`APPROVED`, `EXPIRED`, `QUARANTINED`, `REJECTED`, `UNKNOWN`

## String constants (redacted where noted)

- '\nPAS152 — Memory review CSV export (read-only, structural).\n\nBounded, tenant-scoped CSV projection over the same PAS144C\n``pas_memory_review_events`` audit table that PAS150 / PAS151 already\nread. Gives operators an offline-analysis path (paste into a\nspreadsheet, dump into a notebook) WITHOUT needing direct Supabase\naccess and WITHOUT exposing any of the reason / metadata / evidence /\ntranscript surface that the PAS149 drilldown deliberately gates.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``memory_review_events_csv_for_brokerage`` caps the\n    row fetch at ``_MAX_EXPORT_LIMIT`` (500, mirrors PAS150). The\n    query has both a ``brokerage_id`` equality and an ``ORDER BY\n    created_at DESC LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** The CSV carries four base columns\n    (``created_at``, ``to_status``, ``actor_type``, ``actor_id``)\n    plus two derived columns (``day``, ``status_group``). Reason\n    text, metadata JSONB, evidence, transcript, raw prompts and\n    lineage are NEVER read or surfaced. The projection physically\n    does not look at those keys.\n  * **CSV escaping via the stdlib ``csv`` module.** No manual\n    string concatenation. Embedded commas, quotes, newlines in\n    structural tokens are escaped correctly.\n  * **Fail-closed.** Bad input, reader failure, malformed event row\n    — every path returns a structured envelope with a header-only\n    CSV and warning tokens. Nothing in this module raises.\n\nPublic surface:\n  - csv_rows_from_review_events(events)                  -> list[dict]\n  - render_review_events_csv(rows)                        -> str\n  - memory_review_events_csv_for_brokerage(\n        brokerage_id, since=None, limit=500)              -> dict\n  - CSV_COLUMNS, FORBIDDEN_EXPORT_FIELDS, _MAX_EXPORT_LIMIT\n'
- 'pas.memory.review_export'
- 'to_status'
- 'actor_type'
- 'actor_id'
- 'pas_memory_review_events'
- 'since'
- 'limit'
- 'val'
- 'Any'
- 'return'
- 'Optional[str]'
- 'Return a trimmed string for non-empty ``val`` or None.'
- 'value'
- 'Extract the YYYY-MM-DD prefix from an ISO-8601 timestamp.\n\nReturns the validated day token or None on any malformed input.\nSame structural slice as review_stats._parse_iso_day — audit\nrows are stored UTC by Supabase contract.\n'
- 'str'
- 'Coarse-grained group for the ``status_group`` derived column.\n\n* ``approved``       → APPROVED\n* ``rejected``       → REJECTED\n* ``expired``        → EXPIRED\n* ``quarantined``    → QUARANTINED\n\nAnything else gets ``unknown``. Pure deterministic.\n'
- 'APPROVED'
- 'approved'
- 'REJECTED'
- 'rejected'
- 'EXPIRED'
- 'expired'
- 'QUARANTINED'
- 'quarantined'
- 'unknown'
- 'int'
- 'Coerce a caller-supplied limit; clamp to [1, _MAX_EXPORT_LIMIT].'
- 'Tuple[Optional[str], Optional[str]]'
- 'Coerce caller-supplied ``since``. Mirrors review_stats._coerce_since\nbut kept local. Returns (cleaned_value, warning_token_or_None).'
- 'Coerce caller-supplied ``to_status`` filter.\n\nReturns (cleaned_value, warning_token_or_None). ``None`` /\nblank input yields (None, None) — i.e. "no filter, no warning".\nLowercase variants are normalised to the canonical uppercase\nenum. Anything outside ``ALLOWED_TO_STATUSES`` is dropped with\n``invalid_to_status_filter``.\n'
- 'Coerce caller-supplied ``actor_type`` filter.\n\nSame shape as ``_coerce_to_status_filter`` but against\n``ALLOWED_ACTOR_TYPES``. ``invalid_actor_type_filter`` token\non bad input.\n'
- "Coerce caller-supplied ``actor_id`` filter.\n\nFree-text structural identifier — we trim whitespace, cap\nlength, and refuse non-string input. The warning token is\ndeliberately structural (``invalid_actor_id_filter``) and\nnever echoes the offending value, so a crafted id can't be\nsmuggled into the response via the warnings list.\n"
- 'events'
- 'List[Dict[str, str]]'
- 'Project audit-event rows into CSV-ready row dicts.\n\nPure deterministic helper. Reads ONLY ``created_at``,\n``to_status``, ``actor_type``, ``actor_id`` off each row. Every\nother key on the upstream row — including ``reason``,\n``metadata``, ``evidence``, ``transcript``, ``review_id``,\n``memory_id``, ``brokerage_id``, ``from_status`` — is ignored\non purpose.\n\nReturns a list of dicts each shaped exactly to ``CSV_COLUMNS``.\nRows with an unknown ``to_status`` are dropped silently — the\nenvelope helper adds a single aggregate warning token for them.\nRows where ``created_at`` is missing keep the ``day`` column\nempty but still pass through.\n\nNever raises.\n'
- 'UNKNOWN'
- 'created_at'
- 'day'
- 'status_group'
- 'rows'
- 'Render projected rows as a deterministic CSV string.\n\nUses the stdlib ``csv`` module with ``QUOTE_MINIMAL`` and an\nexplicit column order matching ``CSV_COLUMNS``. The first line\nis always the header. Embedded commas, quotes, and newlines in\nstructural tokens (e.g. an actor_id containing a comma) are\nescaped per RFC 4180. Line terminator is ``\\r\\n`` (csv module\ndefault) for spreadsheet compatibility.\n\nPure deterministic. Never raises.\n'
- 'ignore'
- 'Lazy Supabase resolver. Mirrors review_stats._get_db.'
- 'brokerage_id'
- 'Tuple[List[Dict[str, Any]], List[str]]'
- 'Tenant-scoped, bounded fetch of audit-event rows.\n\nSame shape as ``review_stats._list_review_events_for_brokerage``\n— kept local so a future widening of that reader cannot silently\naffect the export surface. SELECT projection is identical: four\nstructural columns plus ``created_at`` for the derived ``day``.\n\nPAS153 adds three optional equality filters — ``to_status``,\n``actor_type``, ``actor_id`` — which the caller MUST have\nalready passed through the corresponding coercion helpers.\nThe reader trusts that any non-None value here is structurally\nvalid (closed enum for the first two, length-capped string\nfor the third). The reader does NOT widen the SELECT\nprojection — filters narrow rows only, never columns.\n\nReturns (rows, warnings). Never raises. Returns ([], [token]) on\nany Supabase failure.\n'
- 'to_status, actor_type, actor_id, created_at'
- 'data'
- 'review_export reader failed (non-critical) | brokerage='
- ' | error_type='
- 'reader_failed:'
- 'unexpected_reader_shape'
- 'result_truncated_at_limit'
- 'Render a header-only CSV. Used when input is rejected or the\nreader fails — the operator gets a valid, parseable file rather\nthan an empty blob.'
- 'Dict[str, Any]'
- 'Return a closed-shape CSV envelope for one tenant.\n\n``brokerage_id`` is REQUIRED. There is no path through this\nhelper that omits the tenant filter or falls back to a\ncross-tenant scan.\n\nPAS153 adds three optional equality filters:\n\n* ``to_status``  — one of ``APPROVED`` / ``REJECTED`` /\n  ``EXPIRED`` / ``QUARANTINED``. Lowercase variants are\n  normalised. Invalid values are dropped with\n  ``invalid_to_status_filter``.\n* ``actor_type`` — one of ``OPERATOR`` / ``SYSTEM`` /\n  ``ADMIN`` / ``SECURITY``. Lowercase variants are\n  normalised. Invalid values are dropped with\n  ``invalid_actor_type_filter``.\n* ``actor_id``   — free-text identifier; whitespace-trimmed,\n  length-capped to ``_ACTOR_ID_MAX_LEN``. Empty/whitespace-\n  only inputs are dropped with ``invalid_actor_id_filter``.\n  The offending value is NEVER echoed in warnings.\n\nFilters that the helper rejects are dropped silently from\nthe query and surfaced as a structural warning token only.\nThe CSV column set is unchanged.\n\nResponse (always 200 from the route caller\'s perspective):\n    {\n        "status":       "ok" | "failed",\n        "csv":          "<rendered csv with header row>",\n        "row_count":    <int>,\n        "warnings":     [<str>, ...],\n    }\n\nOn ``status="failed"`` the CSV is still a valid header-only\ndocument so the downloader does not break.\n'
- 'status'
- 'failed'
- 'csv'
- 'row_count'
- 'warnings'
- 'missing_brokerage_id'
- 'unknown_status_events_ignored:'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS152 — Memory review CSV export (read-only, structural).\n\nBounded, tenant-scoped CSV projection over the same PAS144C\n``pas_memory_review_events`` audit table that PAS150 / PAS151 already\nread. Gives operators an offline-analysis path (paste into a\nspreadsheet, dump into a notebook) WITHOUT needing direct Supabase\naccess and WITHOUT exposing any of the reason / metadata / evidence /\ntranscript surface that the PAS149 drilldown deliberately gates.\n\nHard contract:\n  * **Tenant-scoped.** Every public helper that touches Supabase\n    requires ``brokerage_id``. There is no unscoped path.\n  * **Bounded.** ``memory_review_events_csv_for_brokerage`` caps the\n    row fetch at ``_MAX_EXPORT_LIMIT`` (500, mirrors PAS150). The\n    query has both a ``brokerage_id`` equality and an ``ORDER BY\n    created_at DESC LIMIT n`` — NOT a full-table scan.\n  * **Structural output only.** The CSV carries four base columns\n    (``created_at``, ``to_status``, ``actor_type``, ``actor_id``)\n    plus two derived columns (``day``, ``status_group``). Reason\n    text, metadata JSONB, evidence, transcript, raw prompts and\n    lineage are NEVER read or surfaced. The projection physically\n    does not look at those keys.\n  * **CSV escaping via the stdlib ``csv`` module.** No manual\n    string concatenation. Embedded commas, quotes, newlines in\n    structural tokens are escaped correctly.\n  * **Fail-closed.** Bad input, reader failure, malformed event row\n    — every path returns a structured envelope with a header-only\n    CSV and warning tokens. Nothing in this module raises.\n\nPublic surface:\n  - csv_rows_from_review_events(events)                  -> list[dict]\n  - render_review_events_csv(rows)                        -> str\n  - memory_review_events_csv_for_brokerage(\n        brokerage_id, since=None, limit=500)              -> dict\n  - CSV_COLUMNS, FORBIDDEN_EXPORT_FIELDS, _MAX_EXPORT_LIMIT\n')
              STORE_NAME               0 (__doc__)

 39           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 41           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (csv)
              STORE_NAME               3 (csv)

 42           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (io)
              STORE_NAME               4 (io)

 43           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (logging)
              STORE_NAME               5 (logging)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
              IMPORT_NAME              6 (typing)
              IMPORT_FROM              7 (Any)
              STORE_NAME               7 (Any)
              IMPORT_FROM              8 (Dict)
              STORE_NAME               8 (Dict)
              IMPORT_FROM              9 (List)
              STORE_NAME               9 (List)
              IMPORT_FROM             10 (Optional)
              STORE_NAME              10 (Optional)
              IMPORT_FROM             11 (Tuple)
              STORE_NAME              11 (Tuple)
              POP_TOP

 46           LOAD_NAME                5 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.memory.review_export')
              CALL                     1
              STORE_NAME              13 (logger)

 50           LOAD_CONST              39 (('APPROVED', 'REJECTED', 'EXPIRED', 'QUARANTINED'))
              STORE_NAME              14 (ALLOWED_TO_STATUSES)

 51           LOAD_CONST              40 (('OPERATOR', 'SYSTEM', 'ADMIN', 'SECURITY'))
              STORE_NAME              15 (ALLOWED_ACTOR_TYPES)

 65           LOAD_CONST              41 (('created_at', 'to_status', 'actor_type', 'actor_id', 'day', 'status_group'))
              STORE_NAME              16 (CSV_COLUMNS)

 77           LOAD_CONST              42 (('review_id', 'memory_id', 'brokerage_id', 'from_status', 'reason', 'metadata', 'metadata_blob', 'evidence', 'lineage', 'transcript', 'raw_transcript', 'full_transcript', 'raw_text', 'raw_prompt', 'injected_prompt', 'messages', 'utterances', 'input_text', 'output_text', 'memory_content'))
              STORE_NAME              17 (FORBIDDEN_EXPORT_FIELDS)

 95           LOAD_CONST               8 (500)
              STORE_NAME              18 (_MAX_EXPORT_LIMIT)

 96           LOAD_CONST               8 (500)
              STORE_NAME              19 (_DEFAULT_EXPORT_LIMIT)

 98           LOAD_CONST               9 ('pas_memory_review_events')
              STORE_NAME              20 (_TABLE_REVIEW)

108           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\review_export.py", line 108>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _safe_str at 0x0000018C18038F30, file "app\services\memory\review_export.py", line 108>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_safe_str)

116           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\review_export.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _parse_iso_day at 0x0000018C17EDA4B0, file "app\services\memory\review_export.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_parse_iso_day)

150           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\review_export.py", line 150>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _status_group at 0x0000018C180532D0, file "app\services\memory\review_export.py", line 150>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_status_group)

171           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\memory\review_export.py", line 171>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _clamp_limit at 0x0000018C17FF0F30, file "app\services\memory\review_export.py", line 171>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_clamp_limit)

184           LOAD_CONST              18 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\review_export.py", line 184>)
              MAKE_FUNCTION
              LOAD_CONST              19 (<code object _coerce_since at 0x0000018C1794E810, file "app\services\memory\review_export.py", line 184>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_coerce_since)

202           LOAD_SMALL_INT         128
              STORE_NAME              26 (_ACTOR_ID_MAX_LEN)

205           LOAD_CONST              20 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\review_export.py", line 205>)
              MAKE_FUNCTION
              LOAD_CONST              21 (<code object _coerce_to_status_filter at 0x0000018C1800AD80, file "app\services\memory\review_export.py", line 205>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (_coerce_to_status_filter)

227           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\review_export.py", line 227>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _coerce_actor_type_filter at 0x0000018C1800ABF0, file "app\services\memory\review_export.py", line 227>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_coerce_actor_type_filter)

247           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\review_export.py", line 247>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _coerce_actor_id_filter at 0x0000018C1800AF10, file "app\services\memory\review_export.py", line 247>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_coerce_actor_id_filter)

275           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2880, file "app\services\memory\review_export.py", line 275>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object csv_rows_from_review_events at 0x0000018C181A2A00, file "app\services\memory\review_export.py", line 275>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (csv_rows_from_review_events)

322           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\memory\review_export.py", line 322>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object render_review_events_csv at 0x0000018C17E92390, file "app\services\memory\review_export.py", line 322>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (render_review_events_csv)

364           LOAD_CONST              30 (<code object _get_db at 0x0000018C17FA3A50, file "app\services\memory\review_export.py", line 364>)
              MAKE_FUNCTION
              STORE_NAME              32 (_get_db)

370           LOAD_CONST              31 ('since')

373           LOAD_CONST               2 (None)

370           LOAD_CONST              32 ('limit')

374           LOAD_NAME               19 (_DEFAULT_EXPORT_LIMIT)

370           LOAD_CONST               5 ('to_status')

375           LOAD_CONST               2 (None)

370           LOAD_CONST               6 ('actor_type')

376           LOAD_CONST               2 (None)

370           LOAD_CONST               7 ('actor_id')

377           LOAD_CONST               2 (None)

370           BUILD_MAP                5
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C180C4140, file "app\services\memory\review_export.py", line 370>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object _list_review_events_for_brokerage at 0x0000018C17E84250, file "app\services\memory\review_export.py", line 370>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              33 (_list_review_events_for_brokerage)

438           LOAD_CONST              35 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\memory\review_export.py", line 438>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object _empty_csv at 0x0000018C17FA1E30, file "app\services\memory\review_export.py", line 438>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_empty_csv)

447           LOAD_CONST               2 (None)

448           LOAD_NAME               19 (_DEFAULT_EXPORT_LIMIT)

449           LOAD_CONST               2 (None)

450           LOAD_CONST               2 (None)

451           LOAD_CONST               2 (None)

445           BUILD_TUPLE              5
              LOAD_CONST              37 (<code object __annotate__ at 0x0000018C180C4470, file "app\services\memory\review_export.py", line 445>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object memory_review_events_csv_for_brokerage at 0x0000018C17E8D300, file "app\services\memory\review_export.py", line 445>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              35 (memory_review_events_csv_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\memory\review_export.py", line 108>:
108           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('val')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _safe_str at 0x0000018C18038F30, file "app\services\memory\review_export.py", line 108>:
108           RESUME                   0

110           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (val)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

111           LOAD_CONST               1 (None)
              RETURN_VALUE

112   L1:     LOAD_FAST_BORROW         0 (val)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

113           LOAD_FAST                1 (s)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (None)
      L2:     RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\memory\review_export.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _parse_iso_day at 0x0000018C17EDA4B0, file "app\services\memory\review_export.py", line 116>:
 116            RESUME                   0

 123            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (value)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 124            LOAD_CONST               1 (None)
                RETURN_VALUE

 125    L1:     LOAD_FAST_BORROW         0 (value)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (s)

 126            LOAD_GLOBAL              7 (len + NULL)
                LOAD_FAST_BORROW         1 (s)
                CALL                     1
                LOAD_SMALL_INT          10
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L2)
                NOT_TAKEN

 127            LOAD_CONST               1 (None)
                RETURN_VALUE

 128    L2:     LOAD_FAST_BORROW         1 (s)
                LOAD_CONST               2 (slice(None, 10, None))
                BINARY_OP               26 ([])
                STORE_FAST               2 (head)

 129            LOAD_FAST_BORROW         2 (head)
                LOAD_SMALL_INT           4
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('-')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_TRUE        15 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (head)
                LOAD_SMALL_INT           7
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('-')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 130    L3:     LOAD_CONST               1 (None)
                RETURN_VALUE

 131    L4:     NOP

 132    L5:     LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               4 (slice(0, 4, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               3 (y)

 133            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               5 (slice(5, 7, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               4 (m)

 134            LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (head)
                LOAD_CONST               6 (slice(8, 10, None))
                BINARY_OP               26 ([])
                CALL                     1
                STORE_FAST               5 (d)

 139            LOAD_SMALL_INT           1
                LOAD_FAST                4 (m)
                SWAP                     2
                COPY                     2
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       10 (to L7)
                NOT_TAKEN
                LOAD_SMALL_INT          12
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_TRUE         7 (to L9)
                NOT_TAKEN
                NOP

 140    L6:     LOAD_CONST               1 (None)
                RETURN_VALUE

 139    L7:     POP_TOP

 140    L8:     LOAD_CONST               1 (None)
                RETURN_VALUE

 141    L9:     LOAD_SMALL_INT           1
                LOAD_FAST                5 (d)
                SWAP                     2
                COPY                     2
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_FALSE       10 (to L11)
                NOT_TAKEN
                LOAD_SMALL_INT          31
                COMPARE_OP              58 (bool(<=))
                POP_JUMP_IF_TRUE         7 (to L13)
                NOT_TAKEN
                NOP

 142   L10:     LOAD_CONST               1 (None)
                RETURN_VALUE

 141   L11:     POP_TOP

 142   L12:     LOAD_CONST               1 (None)
                RETURN_VALUE

 143   L13:     LOAD_FAST_BORROW         3 (y)
                LOAD_SMALL_INT           1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L15)
                NOT_TAKEN

 144   L14:     LOAD_CONST               1 (None)
                RETURN_VALUE

 143   L15:     NOP

 147            LOAD_FAST_BORROW         2 (head)
                RETURN_VALUE

  --   L16:     PUSH_EXC_INFO

 145            LOAD_GLOBAL             10 (ValueError)
                LOAD_GLOBAL             12 (TypeError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L18)
                NOT_TAKEN
                POP_TOP

 146   L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

 145   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L16 [0]
  L7 to L8 -> L16 [0]
  L9 to L10 -> L16 [0]
  L11 to L12 -> L16 [0]
  L13 to L14 -> L16 [0]
  L16 to L17 -> L19 [1] lasti
  L18 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "app\services\memory\review_export.py", line 150>:
150           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('to_status')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _status_group at 0x0000018C180532D0, file "app\services\memory\review_export.py", line 150>:
150           RESUME                   0

160           LOAD_FAST_BORROW         0 (to_status)
              LOAD_CONST               1 ('APPROVED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

161           LOAD_CONST               2 ('approved')
              RETURN_VALUE

162   L1:     LOAD_FAST_BORROW         0 (to_status)
              LOAD_CONST               3 ('REJECTED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

163           LOAD_CONST               4 ('rejected')
              RETURN_VALUE

164   L2:     LOAD_FAST_BORROW         0 (to_status)
              LOAD_CONST               5 ('EXPIRED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

165           LOAD_CONST               6 ('expired')
              RETURN_VALUE

166   L3:     LOAD_FAST_BORROW         0 (to_status)
              LOAD_CONST               7 ('QUARANTINED')
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

167           LOAD_CONST               8 ('quarantined')
              RETURN_VALUE

168   L4:     LOAD_CONST               9 ('unknown')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\memory\review_export.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _clamp_limit at 0x0000018C17FF0F30, file "app\services\memory\review_export.py", line 171>:
 171           RESUME                   0

 173           LOAD_FAST_BORROW         0 (value)
               POP_JUMP_IF_NOT_NONE     7 (to L1)
               NOT_TAKEN

 174           LOAD_GLOBAL              0 (_DEFAULT_EXPORT_LIMIT)
               RETURN_VALUE

 175   L1:     NOP

 176   L2:     LOAD_GLOBAL              3 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (n)

 179   L3:     LOAD_FAST                1 (n)
               LOAD_SMALL_INT           0
               COMPARE_OP              58 (bool(<=))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 180           LOAD_GLOBAL              0 (_DEFAULT_EXPORT_LIMIT)
               RETURN_VALUE

 181   L4:     LOAD_GLOBAL              9 (min + NULL)
               LOAD_FAST                1 (n)
               LOAD_GLOBAL             10 (_MAX_EXPORT_LIMIT)
               CALL                     2
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 177           LOAD_GLOBAL              4 (TypeError)
               LOAD_GLOBAL              6 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

 178           LOAD_GLOBAL              0 (_DEFAULT_EXPORT_LIMIT)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 177   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\memory\review_export.py", line 184>:
184           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_since at 0x0000018C1794E810, file "app\services\memory\review_export.py", line 184>:
184           RESUME                   0

187           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

188           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

189   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

190           LOAD_CONST               5 ((None, 'since_ignored_non_string'))
              RETURN_VALUE

191   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

192           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

193           LOAD_CONST               4 ((None, None))
              RETURN_VALUE

194   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          10
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_TRUE        44 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               2 (slice(None, 4, None))
              BINARY_OP               26 ([])
              LOAD_ATTR                9 (isdigit + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       15 (to L4)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (s)
              LOAD_SMALL_INT           4
              BINARY_OP               26 ([])
              LOAD_CONST               3 ('-')
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L5)
              NOT_TAKEN

195   L4:     LOAD_CONST               6 ((None, 'since_ignored_invalid_format'))
              RETURN_VALUE

196   L5:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\memory\review_export.py", line 205>:
205           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_to_status_filter at 0x0000018C1800AD80, file "app\services\memory\review_export.py", line 205>:
205           RESUME                   0

214           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

215           LOAD_CONST               2 ((None, None))
              RETURN_VALUE

216   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

217           LOAD_CONST               3 ((None, 'invalid_to_status_filter'))
              RETURN_VALUE

218   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

219           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

220           LOAD_CONST               2 ((None, None))
              RETURN_VALUE

221   L3:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

222           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              8 (ALLOWED_TO_STATUSES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        5 (to L4)
              NOT_TAKEN

223           LOAD_FAST_BORROW         2 (up)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

224   L4:     LOAD_CONST               3 ((None, 'invalid_to_status_filter'))
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3780, file "app\services\memory\review_export.py", line 227>:
227           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_actor_type_filter at 0x0000018C1800ABF0, file "app\services\memory\review_export.py", line 227>:
227           RESUME                   0

234           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

235           LOAD_CONST               2 ((None, None))
              RETURN_VALUE

236   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

237           LOAD_CONST               3 ((None, 'invalid_actor_type_filter'))
              RETURN_VALUE

238   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

239           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

240           LOAD_CONST               2 ((None, None))
              RETURN_VALUE

241   L3:     LOAD_FAST_BORROW         1 (s)
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               2 (up)

242           LOAD_FAST_BORROW         2 (up)
              LOAD_GLOBAL              8 (ALLOWED_ACTOR_TYPES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        5 (to L4)
              NOT_TAKEN

243           LOAD_FAST_BORROW         2 (up)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

244   L4:     LOAD_CONST               3 ((None, 'invalid_actor_type_filter'))
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\memory\review_export.py", line 247>:
247           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], Optional[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _coerce_actor_id_filter at 0x0000018C1800AF10, file "app\services\memory\review_export.py", line 247>:
247           RESUME                   0

256           LOAD_FAST_BORROW         0 (value)
              POP_JUMP_IF_NOT_NONE     3 (to L1)
              NOT_TAKEN

257           LOAD_CONST               2 ((None, None))
              RETURN_VALUE

258   L1:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

259           LOAD_CONST               3 ((None, 'invalid_actor_id_filter'))
              RETURN_VALUE

260   L2:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

261           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

265           LOAD_CONST               3 ((None, 'invalid_actor_id_filter'))
              RETURN_VALUE

266   L3:     LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_ACTOR_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE       10 (to L4)
              NOT_TAKEN

267           LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              LOAD_GLOBAL              8 (_ACTOR_ID_MAX_LEN)
              BINARY_SLICE
              STORE_FAST               1 (s)

268   L4:     LOAD_FAST_BORROW         1 (s)
              LOAD_CONST               1 (None)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2880, file "app\services\memory\review_export.py", line 275>:
275           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('events')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Dict[str, str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object csv_rows_from_review_events at 0x0000018C181A2A00, file "app\services\memory\review_export.py", line 275>:
275           RESUME                   0

293           BUILD_LIST               0
              STORE_FAST               1 (out)

294           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (events)
              LOAD_GLOBAL              2 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

295           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

296   L1:     LOAD_FAST_BORROW         0 (events)
              GET_ITER
      L2:     FOR_ITER               233 (to L9)
              STORE_FAST               2 (raw)

297           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL              4 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN

298           JUMP_BACKWARD           27 (to L2)

299   L3:     LOAD_GLOBAL              7 (_safe_str + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               1 ('to_status')
              CALL                     1
              CALL                     1
              STORE_FAST               3 (to_status)

300           LOAD_FAST_BORROW         3 (to_status)
              LOAD_GLOBAL             10 (ALLOWED_TO_STATUSES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN

301           JUMP_BACKWARD           66 (to L2)

302   L4:     LOAD_GLOBAL              7 (_safe_str + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               2 ('actor_type')
              CALL                     1
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               3 ('UNKNOWN')
      L5:     STORE_FAST               4 (actor_type)

303           LOAD_GLOBAL              7 (_safe_str + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               4 ('actor_id')
              CALL                     1
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               5 ('unknown')
      L6:     STORE_FAST               5 (actor_id)

304           LOAD_GLOBAL              7 (_safe_str + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_CONST               6 ('created_at')
              CALL                     1
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L7)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               7 ('')
      L7:     STORE_FAST               6 (created_at)

305           LOAD_GLOBAL             13 (_parse_iso_day + NULL)
              LOAD_FAST_BORROW         6 (created_at)
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L8)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               7 ('')
      L8:     STORE_FAST               7 (day)

311           LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR               15 (append + NULL|self)

312           LOAD_CONST               6 ('created_at')
              LOAD_FAST_BORROW         6 (created_at)

313           LOAD_CONST               1 ('to_status')
              LOAD_FAST_BORROW         3 (to_status)

314           LOAD_CONST               2 ('actor_type')
              LOAD_FAST_BORROW         4 (actor_type)

315           LOAD_CONST               4 ('actor_id')
              LOAD_FAST_BORROW         5 (actor_id)

316           LOAD_CONST               8 ('day')
              LOAD_FAST_BORROW         7 (day)

317           LOAD_CONST               9 ('status_group')
              LOAD_GLOBAL             17 (_status_group + NULL)
              LOAD_FAST_BORROW         3 (to_status)
              CALL                     1

311           BUILD_MAP                6
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          235 (to L2)

296   L9:     END_FOR
              POP_ITER

319           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\memory\review_export.py", line 322>:
322           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('rows')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object render_review_events_csv at 0x0000018C17E92390, file "app\services\memory\review_export.py", line 322>:
322           RESUME                   0

334           LOAD_GLOBAL              0 (io)
              LOAD_ATTR                2 (StringIO)
              PUSH_NULL
              CALL                     0
              STORE_FAST               1 (buf)

335           LOAD_GLOBAL              4 (csv)
              LOAD_ATTR                6 (DictWriter)
              PUSH_NULL

336           LOAD_FAST_BORROW         1 (buf)

337           LOAD_GLOBAL              9 (list + NULL)
              LOAD_GLOBAL             10 (CSV_COLUMNS)
              CALL                     1

338           LOAD_CONST               1 ('ignore')

339           LOAD_GLOBAL              4 (csv)
              LOAD_ATTR               12 (QUOTE_MINIMAL)

335           LOAD_CONST               2 (('fieldnames', 'extrasaction', 'quoting'))
              CALL_KW                  4
              STORE_FAST               2 (writer)

341           LOAD_FAST_BORROW         2 (writer)
              LOAD_ATTR               15 (writeheader + NULL|self)
              CALL                     0
              POP_TOP

342           LOAD_GLOBAL             17 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (rows)
              LOAD_GLOBAL              8 (list)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE      107 (to L7)
              NOT_TAKEN

343           LOAD_FAST_BORROW         0 (rows)
              GET_ITER
      L1:     FOR_ITER               100 (to L6)
              STORE_FAST               3 (r)

344           LOAD_GLOBAL             17 (isinstance + NULL)
              LOAD_FAST_BORROW         3 (r)
              LOAD_GLOBAL             18 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

345           JUMP_BACKWARD           27 (to L1)

349   L2:     BUILD_MAP                0
              STORE_FAST               4 (projected)

350           LOAD_GLOBAL             10 (CSV_COLUMNS)
              GET_ITER
      L3:     FOR_ITER                44 (to L5)
              STORE_FAST               5 (col)

351           LOAD_FAST_BORROW         3 (r)
              LOAD_ATTR               21 (get + NULL|self)
              LOAD_FAST_BORROW         5 (col)
              LOAD_CONST               3 ('')
              CALL                     2
              STORE_FAST               6 (v)

352           LOAD_FAST_BORROW         6 (v)
              POP_JUMP_IF_NOT_NONE     7 (to L4)
              NOT_TAKEN

353           LOAD_CONST               3 ('')
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (projected, col)
              STORE_SUBSCR
              JUMP_BACKWARD           31 (to L3)

355   L4:     LOAD_GLOBAL             23 (str + NULL)
              LOAD_FAST_BORROW         6 (v)
              CALL                     1
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (projected, col)
              STORE_SUBSCR
              JUMP_BACKWARD           46 (to L3)

350   L5:     END_FOR
              POP_ITER

356           LOAD_FAST_BORROW         2 (writer)
              LOAD_ATTR               25 (writerow + NULL|self)
              LOAD_FAST_BORROW         4 (projected)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD          102 (to L1)

343   L6:     END_FOR
              POP_ITER

357   L7:     LOAD_FAST_BORROW         1 (buf)
              LOAD_ATTR               27 (getvalue + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C17FA3A50, file "app\services\memory\review_export.py", line 364>:
364           RESUME                   0

366           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('get_supabase',))
              IMPORT_NAME              0 (app.db.supabase_client)
              IMPORT_FROM              1 (get_supabase)
              STORE_FAST               0 (get_supabase)
              POP_TOP

367           LOAD_FAST_BORROW         0 (get_supabase)
              PUSH_NULL
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4140, file "app\services\memory\review_export.py", line 370>:
370           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

371           LOAD_CONST               2 ('str')

370           LOAD_CONST               3 ('since')

373           LOAD_CONST               4 ('Optional[str]')

370           LOAD_CONST               5 ('limit')

374           LOAD_CONST               6 ('int')

370           LOAD_CONST               7 ('to_status')

375           LOAD_CONST               4 ('Optional[str]')

370           LOAD_CONST               8 ('actor_type')

376           LOAD_CONST               4 ('Optional[str]')

370           LOAD_CONST               9 ('actor_id')

377           LOAD_CONST               4 ('Optional[str]')

370           LOAD_CONST              10 ('return')

378           LOAD_CONST              11 ('Tuple[List[Dict[str, Any]], List[str]]')

370           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object _list_review_events_for_brokerage at 0x0000018C17E84250, file "app\services\memory\review_export.py", line 370>:
 370            RESUME                   0

 397            BUILD_LIST               0
                STORE_FAST               6 (warnings)

 398            NOP

 399    L1:     LOAD_GLOBAL              1 (_get_db + NULL)
                CALL                     0
                STORE_FAST               7 (db)

 401            LOAD_FAST_BORROW         7 (db)
                LOAD_ATTR                3 (table + NULL|self)
                LOAD_GLOBAL              4 (_TABLE_REVIEW)
                CALL                     1

 402            LOAD_ATTR                7 (select + NULL|self)
                LOAD_CONST               1 ('to_status, actor_type, actor_id, created_at')
                CALL                     1

 403            LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               2 ('brokerage_id')
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     2

 404            LOAD_ATTR               11 (order + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_CONST               4 (True)
                LOAD_CONST               5 (('desc',))
                CALL_KW                  2

 405            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1

 400            STORE_FAST               8 (query)

 407            LOAD_FAST_BORROW         1 (since)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L2)
                NOT_TAKEN

 408            LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR               15 (gte + NULL|self)
                LOAD_CONST               3 ('created_at')
                LOAD_FAST_BORROW         1 (since)
                CALL                     2
                STORE_FAST               8 (query)

 412    L2:     LOAD_FAST_BORROW         3 (to_status)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L5)
        L3:     NOT_TAKEN

 413    L4:     LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               6 ('to_status')
                LOAD_FAST_BORROW         3 (to_status)
                CALL                     2
                STORE_FAST               8 (query)

 414    L5:     LOAD_FAST_BORROW         4 (actor_type)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L8)
        L6:     NOT_TAKEN

 415    L7:     LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               7 ('actor_type')
                LOAD_FAST_BORROW         4 (actor_type)
                CALL                     2
                STORE_FAST               8 (query)

 416    L8:     LOAD_FAST_BORROW         5 (actor_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L11)
        L9:     NOT_TAKEN

 417   L10:     LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR                9 (eq + NULL|self)
                LOAD_CONST               8 ('actor_id')
                LOAD_FAST_BORROW         5 (actor_id)
                CALL                     2
                STORE_FAST               8 (query)

 418   L11:     LOAD_FAST_BORROW         8 (query)
                LOAD_ATTR               17 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 419            LOAD_GLOBAL             19 (list + NULL)
                LOAD_GLOBAL             21 (getattr + NULL)
                LOAD_FAST_BORROW         9 (result)
                LOAD_CONST               9 ('data')
                LOAD_CONST              10 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     CALL                     1
                STORE_FAST              10 (rows)

 427   L15:     LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST               10 (rows)
                LOAD_GLOBAL             18 (list)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         6 (to L16)
                NOT_TAKEN

 428            BUILD_LIST               0
                LOAD_CONST              14 ('unexpected_reader_shape')
                BUILD_LIST               1
                BUILD_TUPLE              2
                RETURN_VALUE

 429   L16:     LOAD_GLOBAL             35 (len + NULL)
                LOAD_FAST               10 (rows)
                CALL                     1
                LOAD_FAST                2 (limit)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       18 (to L17)
                NOT_TAKEN

 430            LOAD_FAST                6 (warnings)
                LOAD_ATTR               37 (append + NULL|self)
                LOAD_CONST              15 ('result_truncated_at_limit')
                CALL                     1
                POP_TOP

 431   L17:     LOAD_FAST_LOAD_FAST    166 (rows, warnings)
                BUILD_TUPLE              2
                RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 420            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L23)
                NOT_TAKEN
                STORE_FAST              11 (e)

 421   L19:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 422            LOAD_CONST              11 ('review_export reader failed (non-critical) | brokerage=')

 423            LOAD_FAST                0 (brokerage_id)
                FORMAT_SIMPLE
                LOAD_CONST              12 (' | error_type=')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 422            BUILD_STRING             4

 421            CALL                     1
                POP_TOP

 425            BUILD_LIST               0
                LOAD_CONST              13 ('reader_failed:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1
                BUILD_TUPLE              2
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST              10 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 420   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L3 -> L18 [0]
  L4 to L6 -> L18 [0]
  L7 to L9 -> L18 [0]
  L10 to L12 -> L18 [0]
  L13 to L15 -> L18 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\memory\review_export.py", line 438>:
438           RESUME                   0
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

Disassembly of <code object _empty_csv at 0x0000018C17FA1E30, file "app\services\memory\review_export.py", line 438>:
438           RESUME                   0

442           LOAD_GLOBAL              1 (render_review_events_csv + NULL)
              BUILD_LIST               0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180C4470, file "app\services\memory\review_export.py", line 445>:
445           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

446           LOAD_CONST               2 ('Any')

445           LOAD_CONST               3 ('since')

447           LOAD_CONST               2 ('Any')

445           LOAD_CONST               4 ('limit')

448           LOAD_CONST               2 ('Any')

445           LOAD_CONST               5 ('to_status')

449           LOAD_CONST               2 ('Any')

445           LOAD_CONST               6 ('actor_type')

450           LOAD_CONST               2 ('Any')

445           LOAD_CONST               7 ('actor_id')

451           LOAD_CONST               2 ('Any')

445           LOAD_CONST               8 ('return')

452           LOAD_CONST               9 ('Dict[str, Any]')

445           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object memory_review_events_csv_for_brokerage at 0x0000018C17E8D300, file "app\services\memory\review_export.py", line 445>:
445            RESUME                   0

489            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_GLOBAL              2 (str)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE       23 (to L1)
               NOT_TAKEN
               LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE        20 (to L2)
               NOT_TAKEN

491    L1:     LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('failed')

492            LOAD_CONST               3 ('csv')
               LOAD_GLOBAL              7 (_empty_csv + NULL)
               CALL                     0

493            LOAD_CONST               4 ('row_count')
               LOAD_SMALL_INT           0

494            LOAD_CONST               5 ('warnings')
               LOAD_CONST               6 ('missing_brokerage_id')
               BUILD_LIST               1

490            BUILD_MAP                4
               RETURN_VALUE

496    L2:     LOAD_FAST_BORROW         0 (brokerage_id)
               LOAD_ATTR                5 (strip + NULL|self)
               CALL                     0
               STORE_FAST               0 (brokerage_id)

498            LOAD_GLOBAL              9 (_coerce_since + NULL)
               LOAD_FAST_BORROW         1 (since)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  103 (cleaned_since, since_warning)

499            LOAD_GLOBAL             11 (_clamp_limit + NULL)
               LOAD_FAST_BORROW         2 (limit)
               CALL                     1
               STORE_FAST               8 (capped)

505            LOAD_GLOBAL             13 (_coerce_to_status_filter + NULL)
               LOAD_FAST_BORROW         3 (to_status)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  154 (f_to_status, to_status_warning)

506            LOAD_GLOBAL             15 (_coerce_actor_type_filter + NULL)
               LOAD_FAST_BORROW         4 (actor_type)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  188 (f_actor_type, actor_type_warning)

507            LOAD_GLOBAL             17 (_coerce_actor_id_filter + NULL)
               LOAD_FAST_BORROW         5 (actor_id)
               CALL                     1
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST  222 (f_actor_id, actor_id_warning)

509            LOAD_GLOBAL             19 (_list_review_events_for_brokerage + NULL)

510            LOAD_FAST_BORROW         0 (brokerage_id)

511            LOAD_FAST_BORROW         6 (cleaned_since)

512            LOAD_FAST_BORROW         8 (capped)

513            LOAD_FAST_BORROW         9 (f_to_status)

514            LOAD_FAST_BORROW        11 (f_actor_type)

515            LOAD_FAST_BORROW        13 (f_actor_id)

509            LOAD_CONST               7 (('since', 'limit', 'to_status', 'actor_type', 'actor_id'))
               CALL_KW                  6
               UNPACK_SEQUENCE          2
               STORE_FAST              15 (rows)
               STORE_FAST              16 (reader_warnings)

518            LOAD_GLOBAL             21 (csv_rows_from_review_events + NULL)
               LOAD_FAST_BORROW        15 (rows)
               CALL                     1
               STORE_FAST              17 (projected)

519            LOAD_GLOBAL             23 (render_review_events_csv + NULL)
               LOAD_FAST_BORROW        17 (projected)
               CALL                     1
               STORE_FAST              18 (csv_text)

521            LOAD_GLOBAL             25 (list + NULL)
               LOAD_FAST_BORROW        16 (reader_warnings)
               CALL                     1
               STORE_FAST              19 (warnings)

522            LOAD_FAST_BORROW         7 (since_warning)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L3)
               NOT_TAKEN

523            LOAD_FAST_BORROW        19 (warnings)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_FAST_BORROW         7 (since_warning)
               CALL                     1
               POP_TOP

524    L3:     LOAD_FAST_BORROW        10 (to_status_warning)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L4)
               NOT_TAKEN

525            LOAD_FAST_BORROW        19 (warnings)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_FAST_BORROW        10 (to_status_warning)
               CALL                     1
               POP_TOP

526    L4:     LOAD_FAST_BORROW        12 (actor_type_warning)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L5)
               NOT_TAKEN

527            LOAD_FAST_BORROW        19 (warnings)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_FAST_BORROW        12 (actor_type_warning)
               CALL                     1
               POP_TOP

528    L5:     LOAD_FAST_BORROW        14 (actor_id_warning)
               TO_BOOL
               POP_JUMP_IF_FALSE       18 (to L6)
               NOT_TAKEN

529            LOAD_FAST_BORROW        19 (warnings)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_FAST_BORROW        14 (actor_id_warning)
               CALL                     1
               POP_TOP

534    L6:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        15 (rows)
               LOAD_GLOBAL             24 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_FALSE      112 (to L11)
               NOT_TAKEN

535            LOAD_SMALL_INT           0
               STORE_FAST              20 (dropped)

536            LOAD_FAST_BORROW        15 (rows)
               GET_ITER
       L7:     FOR_ITER                75 (to L10)
               STORE_FAST              21 (r)

537            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW        21 (r)
               LOAD_GLOBAL             28 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L7)

538    L8:     LOAD_GLOBAL             31 (_safe_str + NULL)
               LOAD_FAST_BORROW        21 (r)
               LOAD_ATTR               33 (get + NULL|self)
               LOAD_CONST               8 ('to_status')
               CALL                     1
               CALL                     1
               STORE_FAST              22 (ts)

539            LOAD_FAST_BORROW        22 (ts)
               LOAD_GLOBAL             34 (ALLOWED_TO_STATUSES)
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               JUMP_BACKWARD           66 (to L7)

540    L9:     LOAD_FAST_BORROW        20 (dropped)
               LOAD_SMALL_INT           1
               BINARY_OP               13 (+=)
               STORE_FAST              20 (dropped)
               JUMP_BACKWARD           77 (to L7)

536   L10:     END_FOR
               POP_ITER

541            LOAD_FAST_BORROW        20 (dropped)
               TO_BOOL
               POP_JUMP_IF_FALSE       21 (to L11)
               NOT_TAKEN

542            LOAD_FAST_BORROW        19 (warnings)
               LOAD_ATTR               27 (append + NULL|self)
               LOAD_CONST               9 ('unknown_status_events_ignored:')
               LOAD_FAST_BORROW        20 (dropped)
               FORMAT_SIMPLE
               BUILD_STRING             2
               CALL                     1
               POP_TOP

545   L11:     LOAD_CONST               1 ('status')
               LOAD_CONST              10 ('ok')

546            LOAD_CONST               3 ('csv')
               LOAD_FAST_BORROW        18 (csv_text)

547            LOAD_CONST               4 ('row_count')
               LOAD_GLOBAL             37 (len + NULL)
               LOAD_FAST_BORROW        17 (projected)
               CALL                     1

548            LOAD_CONST               5 ('warnings')
               LOAD_FAST_BORROW        19 (warnings)

544            BUILD_MAP                4
               RETURN_VALUE
```
