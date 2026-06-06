# tenant/tenant_incident_projection

- **pyc:** `app\services\tenant\__pycache__\tenant_incident_projection.cpython-314.pyc`
- **expected source path (absent):** `app\services\tenant/tenant_incident_projection.py`
- **co_filename (from bytecode):** `app\services\tenant\tenant_incident_projection.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** tenant

## Module docstring

```
PAS189 — Tenant-facing incident projection (safe read-only).

Projects rows from ``pas_operator_incidents`` (the PAS188
ledger) into a SAFE, brokerage-scoped view that a tenant
operator can read via X-API-Key.

Doctrine:

* **Brokerage-scoped.** Callers MUST pass a resolved
  ``brokerage_id`` (the route layer resolves this from
  the tenant's X-API-Key — never from a query / path
  parameter the tenant supplies). This module asserts
  that the brokerage_id is non-empty + bounded.
* **Read-only.** No create / update / delete surface.
  No autonomous opener (PAS188 doctrine carry-forward).
* **Safe projection.** The tenant sees ONLY:
      - ``incident_id``
      - ``severity``
      - ``status``
      - ``opened_at``
      - ``resolved_at``
      - ``resolution_code``
  The tenant does NOT see:
      - ``summary`` (operator free-text)
      - ``metadata`` (operator notes, resolution_text)
      - ``opened_by_actor_*`` / ``resolved_by_actor_*``
        (operator identity)
      - any other brokerage's incidents
* **Cross-brokerage leakage is a P0 violation.** The
  forbidden-token scanner is a defence in depth; the
  primary guard is the eq("brokerage_id", bid) filter
  on the DB query.
* **NEVER raises.** DB-unavailable -> ``status="skipped"``
  + warning; the envelope still has a ``rows: []``
  shape so the route can return it.

Public surface:

  * ``list_tenant_incidents_for_brokerage(brokerage_id, *, severity, status, limit)``
  * ``get_tenant_incident_for_brokerage(brokerage_id, incident_id)``
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `get_supabase`, `logging`, `re`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_clamp_int`, `_final`, `_get_db`, `_project_row`, `_safe_brokerage`, `_safe_incident_id`, `_safe_iso_date`, `_safe_severity`, `_safe_status`, `_scan_for_forbidden`, `get_tenant_incident_for_brokerage`, `list_tenant_incidents_for_brokerage`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS189 — Tenant-facing incident projection (safe read-only).\n\nProjects rows from ``pas_operator_incidents`` (the PAS188\nledger) into a SAFE, brokerage-scoped view that a tenant\noperator can read via X-API-Key.\n\nDoctrine:\n\n* **Brokerage-scoped.** Callers MUST pass a resolved\n  ``brokerage_id`` (the route layer resolves this from\n  the tenant\'s X-API-Key — never from a query / path\n  parameter the tenant supplies). This module asserts\n  that the brokerage_id is non-empty + bounded.\n* **Read-only.** No create / update / delete surface.\n  No autonomous opener (PAS188 doctrine carry-forward).\n* **Safe projection.** The tenant sees ONLY:\n      - ``incident_id``\n      - ``severity``\n      - ``status``\n      - ``opened_at``\n      - ``resolved_at``\n      - ``resolution_code``\n  The tenant does NOT see:\n      - ``summary`` (operator free-text)\n      - ``metadata`` (operator notes, resolution_text)\n      - ``opened_by_actor_*`` / ``resolved_by_actor_*``\n        (operator identity)\n      - any other brokerage\'s incidents\n* **Cross-brokerage leakage is a P0 violation.** The\n  forbidden-token scanner is a defence in depth; the\n  primary guard is the eq("brokerage_id", bid) filter\n  on the DB query.\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning; the envelope still has a ``rows: []``\n  shape so the route can return it.\n\nPublic surface:\n\n  * ``list_tenant_incidents_for_brokerage(brokerage_id, *, severity, status, limit)``\n  * ``get_tenant_incident_for_brokerage(brokerage_id, incident_id)``\n'
- 'pas.tenant.incident_projection'
- 'pas_operator_incidents'
- 'severity'
- 'status'
- '^\\d{4}-\\d{2}-\\d{2}(?:[T\\s]\\d{2}:\\d{2}(?::\\d{2})?(?:\\.\\d+)?(?:Z|[+\\-]\\d{2}:?\\d{2})?)?$'
- 'limit'
- 'offset'
- 'date_from'
- 'date_to'
- 'value'
- 'Any'
- 'return'
- 'Optional[str]'
- 'int'
- 'default'
- 'Defensive ISO date/datetime validator. Returns the\ntrimmed string on match, None otherwise. Does NOT parse\nto a datetime object — the value is passed to the DB\nlayer as-is (Supabase / PostgreSQL accepts ISO-8601).'
- 'envelope'
- 'obj'
- 'env'
- 'Dict[str, Any]'
- 'surface'
- 'str'
- 'tenant_incident_projection surface='
- ' collapsed — forbidden token leaked'
- 'failed'
- 'error_code'
- 'tenant_incident_envelope_forbidden_token'
- 'warnings'
- 'row'
- 'brokerage_id'
- 'Bounded, brokerage-scoped tenant incident list.\n\nReturns::\n\n    {\n      "status":       "ok" | "skipped" | "failed",\n      "surface":      "tenant.incidents.list",\n      "brokerage_id": "<bid>",\n      "rows":         [ { ...closed tenant allow-list... } ],\n      "count":        <int>,\n      "warnings":     [...],\n      "error_code":   null | "<closed code>",\n    }\n'
- 'tenant.incidents.list'
- 'invalid_brokerage_id'
- 'skipped'
- 'rows'
- 'count'
- 'db_unavailable'
- 'opened_at'
- 'tenant_incident_projection list query error type='
- 'db_query_failed:'
- 'db_query_failed'
- 'data'
- 'filter_count'
- 'list_tenant_incidents_for_brokerage error type='
- 'unexpected:'
- 'incident_id'
- 'Brokerage-scoped tenant incident fetch. Returns the\nSAFE projection or ``status="failed"`` /\n``incident_not_found`` if no row matches BOTH the\nbrokerage_id AND the incident_id.'
- 'tenant.incidents.get'
- 'invalid_incident_id'
- 'tenant_incident_projection get query error type='
- 'incident_not_found'
- 'get_tenant_incident_for_brokerage error type='

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS189 — Tenant-facing incident projection (safe read-only).\n\nProjects rows from ``pas_operator_incidents`` (the PAS188\nledger) into a SAFE, brokerage-scoped view that a tenant\noperator can read via X-API-Key.\n\nDoctrine:\n\n* **Brokerage-scoped.** Callers MUST pass a resolved\n  ``brokerage_id`` (the route layer resolves this from\n  the tenant\'s X-API-Key — never from a query / path\n  parameter the tenant supplies). This module asserts\n  that the brokerage_id is non-empty + bounded.\n* **Read-only.** No create / update / delete surface.\n  No autonomous opener (PAS188 doctrine carry-forward).\n* **Safe projection.** The tenant sees ONLY:\n      - ``incident_id``\n      - ``severity``\n      - ``status``\n      - ``opened_at``\n      - ``resolved_at``\n      - ``resolution_code``\n  The tenant does NOT see:\n      - ``summary`` (operator free-text)\n      - ``metadata`` (operator notes, resolution_text)\n      - ``opened_by_actor_*`` / ``resolved_by_actor_*``\n        (operator identity)\n      - any other brokerage\'s incidents\n* **Cross-brokerage leakage is a P0 violation.** The\n  forbidden-token scanner is a defence in depth; the\n  primary guard is the eq("brokerage_id", bid) filter\n  on the DB query.\n* **NEVER raises.** DB-unavailable -> ``status="skipped"``\n  + warning; the envelope still has a ``rows: []``\n  shape so the route can return it.\n\nPublic surface:\n\n  * ``list_tenant_incidents_for_brokerage(brokerage_id, *, severity, status, limit)``\n  * ``get_tenant_incident_for_brokerage(brokerage_id, incident_id)``\n')
              STORE_NAME               0 (__doc__)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              4 (typing)
              IMPORT_FROM              5 (Any)
              STORE_NAME               5 (Any)
              IMPORT_FROM              6 (Dict)
              STORE_NAME               6 (Dict)
              IMPORT_FROM              7 (List)
              STORE_NAME               7 (List)
              IMPORT_FROM              8 (Optional)
              STORE_NAME               8 (Optional)
              POP_TOP

 50           LOAD_NAME                3 (logging)
              LOAD_ATTR               18 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.tenant.incident_projection')
              CALL                     1
              STORE_NAME              10 (logger)

 57           LOAD_CONST               5 ('pas_operator_incidents')
              STORE_NAME              11 (_TABLE_NAME)

 59           LOAD_SMALL_INT         200
              STORE_NAME              12 (_BROKERAGE_ID_MAX_LEN)

 60           LOAD_SMALL_INT          64
              STORE_NAME              13 (_INCIDENT_ID_MAX_LEN)

 62           LOAD_NAME               14 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              36 (frozenset({'S2', 'S5', 'S1', 'S3', 'S6', 'S4'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              15 (_VALID_SEVERITIES)

 63           LOAD_NAME               14 (frozenset)
              PUSH_NULL
              BUILD_SET                0
              LOAD_CONST              37 (frozenset({'DUPLICATE', 'INVESTIGATING', 'OPEN', 'RESOLVED', 'WONT_FIX'}))
              SET_UPDATE               1
              CALL                     1
              STORE_NAME              16 (_VALID_STATUSES)

 69           LOAD_CONST              38 (('incident_id', 'severity', 'status', 'opened_at', 'resolved_at', 'resolution_code'))
              STORE_NAME              17 (_TENANT_ROW_ALLOWLIST)

 78           LOAD_CONST              39 (('phone', 'email', 'name_token', 'transcript', 'raw_payload', 'raw_email', 'raw_body', 'secret', 'signature', 'dedupe_key', 'api_key', 'token', 'stack_trace', 'prompt_text', 'env_values', 'operator_notes', 'rationale_text', 'resolution_text', 'summary', 'opened_by_actor', 'resolved_by_actor', 'metadata'))
              STORE_NAME              18 (_FORBIDDEN_RESPONSE_TOKENS)

 97           LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\tenant\tenant_incident_projection.py", line 97>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _safe_brokerage at 0x0000018C17F96420, file "app\services\tenant\tenant_incident_projection.py", line 97>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_safe_brokerage)

106           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA2F10, file "app\services\tenant\tenant_incident_projection.py", line 106>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _safe_incident_id at 0x0000018C17F96590, file "app\services\tenant\tenant_incident_projection.py", line 106>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_safe_incident_id)

115           LOAD_CONST              12 (<code object __annotate__ at 0x0000018C17FA21F0, file "app\services\tenant\tenant_incident_projection.py", line 115>)
              MAKE_FUNCTION
              LOAD_CONST              13 (<code object _safe_severity at 0x0000018C17972D90, file "app\services\tenant\tenant_incident_projection.py", line 115>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              21 (_safe_severity)

124           LOAD_CONST              14 (<code object __annotate__ at 0x0000018C17FA31E0, file "app\services\tenant\tenant_incident_projection.py", line 124>)
              MAKE_FUNCTION
              LOAD_CONST              15 (<code object _safe_status at 0x0000018C17972550, file "app\services\tenant\tenant_incident_projection.py", line 124>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_safe_status)

133           LOAD_CONST              16 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\tenant\tenant_incident_projection.py", line 133>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object _clamp_int at 0x0000018C180392F0, file "app\services\tenant\tenant_incident_projection.py", line 133>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              23 (_clamp_int)

148           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME             24 (re)
              STORE_NAME              25 (_re)

150           LOAD_NAME               25 (_re)
              LOAD_ATTR               52 (compile)
              PUSH_NULL

151           LOAD_CONST              18 ('^\\d{4}-\\d{2}-\\d{2}(?:[T\\s]\\d{2}:\\d{2}(?::\\d{2})?(?:\\.\\d+)?(?:Z|[+\\-]\\d{2}:?\\d{2})?)?$')

150           CALL                     1
              STORE_NAME              27 (_ISO_DATE_RE)

156           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA3690, file "app\services\tenant\tenant_incident_projection.py", line 156>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _safe_iso_date at 0x0000018C1800B0A0, file "app\services\tenant\tenant_incident_projection.py", line 156>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              28 (_safe_iso_date)

171           LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\tenant\tenant_incident_projection.py", line 171>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _scan_for_forbidden at 0x0000018C18025E30, file "app\services\tenant\tenant_incident_projection.py", line 171>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_scan_for_forbidden)

195           LOAD_CONST              23 (<code object __annotate__ at 0x0000018C18026330, file "app\services\tenant\tenant_incident_projection.py", line 195>)
              MAKE_FUNCTION
              LOAD_CONST              24 (<code object _final at 0x0000018C17FE1680, file "app\services\tenant\tenant_incident_projection.py", line 195>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              30 (_final)

211           LOAD_CONST              25 (<code object __annotate__ at 0x0000018C17FA3F00, file "app\services\tenant\tenant_incident_projection.py", line 211>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object _project_row at 0x0000018C18053750, file "app\services\tenant\tenant_incident_projection.py", line 211>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              31 (_project_row)

219           LOAD_CONST              27 (<code object _get_db at 0x0000018C18053630, file "app\services\tenant\tenant_incident_projection.py", line 219>)
              MAKE_FUNCTION
              STORE_NAME              32 (_get_db)

231           LOAD_CONST               6 ('severity')

234           LOAD_CONST               2 (None)

231           LOAD_CONST               7 ('status')

235           LOAD_CONST               2 (None)

231           LOAD_CONST              28 ('limit')

236           LOAD_SMALL_INT          25

231           LOAD_CONST              29 ('offset')

237           LOAD_SMALL_INT           0

231           LOAD_CONST              30 ('date_from')

238           LOAD_CONST               2 (None)

231           LOAD_CONST              31 ('date_to')

239           LOAD_CONST               2 (None)

231           BUILD_MAP                6
              LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18128250, file "app\services\tenant\tenant_incident_projection.py", line 231>)
              MAKE_FUNCTION
              LOAD_CONST              33 (<code object list_tenant_incidents_for_brokerage at 0x0000018C17D94CE0, file "app\services\tenant\tenant_incident_projection.py", line 231>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              33 (list_tenant_incidents_for_brokerage)

365           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025F30, file "app\services\tenant\tenant_incident_projection.py", line 365>)
              MAKE_FUNCTION
              LOAD_CONST              35 (<code object get_tenant_incident_for_brokerage at 0x0000018C181B3A50, file "app\services\tenant\tenant_incident_projection.py", line 365>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (get_tenant_incident_for_brokerage)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\tenant\tenant_incident_projection.py", line 97>:
 97           RESUME                   0
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

Disassembly of <code object _safe_brokerage at 0x0000018C17F96420, file "app\services\tenant\tenant_incident_projection.py", line 97>:
 97           RESUME                   0

 98           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 99           LOAD_CONST               0 (None)
              RETURN_VALUE

100   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

101           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_BROKERAGE_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

102   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

103   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app\services\tenant\tenant_incident_projection.py", line 106>:
106           RESUME                   0
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

Disassembly of <code object _safe_incident_id at 0x0000018C17F96590, file "app\services\tenant\tenant_incident_projection.py", line 106>:
106           RESUME                   0

107           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

108           LOAD_CONST               0 (None)
              RETURN_VALUE

109   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

110           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_GLOBAL              8 (_INCIDENT_ID_MAX_LEN)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

111   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

112   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app\services\tenant\tenant_incident_projection.py", line 115>:
115           RESUME                   0
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

Disassembly of <code object _safe_severity at 0x0000018C17972D90, file "app\services\tenant\tenant_incident_projection.py", line 115>:
115           RESUME                   0

116           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

117           LOAD_CONST               0 (None)
              RETURN_VALUE

118   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

119           LOAD_FAST_BORROW         1 (s)
              LOAD_GLOBAL              8 (_VALID_SEVERITIES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

120           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

121   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app\services\tenant\tenant_incident_projection.py", line 124>:
124           RESUME                   0
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

Disassembly of <code object _safe_status at 0x0000018C17972550, file "app\services\tenant\tenant_incident_projection.py", line 124>:
124           RESUME                   0

125           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

126           LOAD_CONST               0 (None)
              RETURN_VALUE

127   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (upper + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

128           LOAD_FAST_BORROW         1 (s)
              LOAD_GLOBAL              8 (_VALID_STATUSES)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

129           LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

130   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\tenant\tenant_incident_projection.py", line 133>:
133           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('lo')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('hi')
              LOAD_CONST               4 ('int')
              LOAD_CONST               6 ('default')
              LOAD_CONST               4 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               4 ('int')
              BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _clamp_int at 0x0000018C180392F0, file "app\services\tenant\tenant_incident_projection.py", line 133>:
 133           RESUME                   0

 134           NOP

 135   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 138   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 139           LOAD_FAST                1 (lo)
               RETURN_VALUE

 140   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 141           LOAD_FAST                2 (hi)
               RETURN_VALUE

 142   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 136           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 137           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 136   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app\services\tenant\tenant_incident_projection.py", line 156>:
156           RESUME                   0
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

Disassembly of <code object _safe_iso_date at 0x0000018C1800B0A0, file "app\services\tenant\tenant_incident_projection.py", line 156>:
156           RESUME                   0

161           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

162           LOAD_CONST               1 (None)
              RETURN_VALUE

163   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

164           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          64
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

165   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

166   L3:     LOAD_GLOBAL              8 (_ISO_DATE_RE)
              LOAD_ATTR               11 (match + NULL|self)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              POP_JUMP_IF_NOT_NONE     3 (to L4)
              NOT_TAKEN

167           LOAD_CONST               1 (None)
              RETURN_VALUE

168   L4:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\tenant\tenant_incident_projection.py", line 171>:
171           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('envelope')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _scan_for_forbidden at 0x0000018C18025E30, file "app\services\tenant\tenant_incident_projection.py", line 171>:
  --           MAKE_CELL                1 (walk)

 171           RESUME                   0

 172           LOAD_CONST               0 (<code object __annotate__ at 0x0000018C17FA2E20, file "app\services\tenant\tenant_incident_projection.py", line 172>)
               MAKE_FUNCTION
               LOAD_FAST_BORROW         1 (walk)
               BUILD_TUPLE              1
               LOAD_CONST               1 (<code object walk at 0x0000018C17CC2460, file "app\services\tenant\tenant_incident_projection.py", line 172>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_DEREF              1 (walk)

 192           LOAD_DEREF               1 (walk)
               PUSH_NULL
               LOAD_FAST_BORROW         0 (envelope)
               CALL                     1
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2E20, file "app\services\tenant\tenant_incident_projection.py", line 172>:
172           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('obj')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object walk at 0x0000018C17CC2460, file "app\services\tenant\tenant_incident_projection.py", line 172>:
  --            COPY_FREE_VARS           1

 172            RESUME                   0

 173            NOP

 174    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      111 (to L16)
        L2:     NOT_TAKEN

 175    L3:     LOAD_FAST_BORROW         0 (obj)
                LOAD_ATTR                5 (items + NULL|self)
                CALL                     0
                GET_ITER
        L4:     FOR_ITER                88 (to L14)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   18 (k, v)

 176            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (k)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       42 (to L10)
                NOT_TAKEN

 177            LOAD_FAST_BORROW         1 (k)
                LOAD_ATTR                9 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (kl)

 178            LOAD_GLOBAL             10 (_FORBIDDEN_RESPONSE_TOKENS)
                GET_ITER
        L5:     FOR_ITER                15 (to L9)
                STORE_FAST               4 (tok)

 179            LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (tok, kl)
                CONTAINS_OP              0 (in)
        L6:     POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)

 180    L7:     LOAD_FAST_BORROW         4 (tok)
                SWAP                     2
                POP_TOP
                SWAP                     2
                POP_TOP
        L8:     RETURN_VALUE

 178    L9:     END_FOR
                POP_ITER

 181   L10:     LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 182            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L11:     POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN
                JUMP_BACKWARD           86 (to L4)

 183   L12:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L13:     RETURN_VALUE

 175   L14:     END_FOR
                POP_ITER

 191   L15:     LOAD_CONST               0 (None)
                RETURN_VALUE

 184   L16:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (obj)
                LOAD_GLOBAL             12 (list)
                LOAD_GLOBAL             14 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L22)
                NOT_TAKEN

 185            LOAD_FAST_BORROW         0 (obj)
                GET_ITER
       L17:     FOR_ITER                23 (to L21)
                STORE_FAST               2 (v)

 186            LOAD_DEREF               6 (walk)
                PUSH_NULL
                LOAD_FAST_BORROW         2 (v)
                CALL                     1
                STORE_FAST               5 (sub)

 187            LOAD_FAST_BORROW         5 (sub)
                TO_BOOL
       L18:     POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                JUMP_BACKWARD           21 (to L17)

 188   L19:     LOAD_FAST_BORROW         5 (sub)
                SWAP                     2
                POP_TOP
       L20:     RETURN_VALUE

 185   L21:     END_FOR
                POP_ITER

 191   L22:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 189            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 190   L24:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 189   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L23 [0]
  L3 to L6 -> L23 [0]
  L7 to L8 -> L23 [0]
  L9 to L11 -> L23 [0]
  L12 to L13 -> L23 [0]
  L14 to L15 -> L23 [0]
  L16 to L18 -> L23 [0]
  L19 to L20 -> L23 [0]
  L21 to L22 -> L23 [0]
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\services\tenant\tenant_incident_projection.py", line 195>:
195           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('env')
              LOAD_CONST               2 ('Dict[str, Any]')
              LOAD_CONST               3 ('surface')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _final at 0x0000018C17FE1680, file "app\services\tenant\tenant_incident_projection.py", line 195>:
195           RESUME                   0

196           LOAD_GLOBAL              1 (_scan_for_forbidden + NULL)
              LOAD_FAST_BORROW         0 (env)
              CALL                     1
              STORE_FAST               2 (leak)

197           LOAD_FAST_BORROW         2 (leak)
              TO_BOOL
              POP_JUMP_IF_FALSE       37 (to L1)
              NOT_TAKEN

198           LOAD_GLOBAL              2 (logger)
              LOAD_ATTR                5 (warning + NULL|self)

199           LOAD_CONST               0 ('tenant_incident_projection surface=')
              LOAD_FAST_BORROW         1 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               1 (' collapsed — forbidden token leaked')
              BUILD_STRING             3

198           CALL                     1
              POP_TOP

203           LOAD_CONST               2 ('status')
              LOAD_CONST               3 ('failed')

204           LOAD_CONST               4 ('surface')
              LOAD_FAST_BORROW         1 (surface)

205           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('tenant_incident_envelope_forbidden_token')

206           LOAD_CONST               7 ('warnings')
              LOAD_CONST               6 ('tenant_incident_envelope_forbidden_token')
              BUILD_LIST               1

202           BUILD_MAP                4
              RETURN_VALUE

208   L1:     LOAD_FAST_BORROW         0 (env)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "app\services\tenant\tenant_incident_projection.py", line 211>:
211           RESUME                   0
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

Disassembly of <code object _project_row at 0x0000018C18053750, file "app\services\tenant\tenant_incident_projection.py", line 211>:
211           RESUME                   0

212           BUILD_MAP                0
              STORE_FAST               1 (out)

213           LOAD_GLOBAL              0 (_TENANT_ROW_ALLOWLIST)
              GET_ITER
      L1:     FOR_ITER                21 (to L3)
              STORE_FAST               2 (k)

214           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (k, row)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L1)

215   L2:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 2 (row, k)
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (out, k)
              STORE_SUBSCR
              JUMP_BACKWARD           23 (to L1)

213   L3:     END_FOR
              POP_ITER

216           LOAD_FAST_BORROW         1 (out)
              RETURN_VALUE

Disassembly of <code object _get_db at 0x0000018C18053630, file "app\services\tenant\tenant_incident_projection.py", line 219>:
 219           RESUME                   0

 220           NOP

 221   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 222           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 223           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 224   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 223   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18128250, file "app\services\tenant\tenant_incident_projection.py", line 231>:
231           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

232           LOAD_CONST               2 ('Any')

231           LOAD_CONST               3 ('severity')

234           LOAD_CONST               2 ('Any')

231           LOAD_CONST               4 ('status')

235           LOAD_CONST               2 ('Any')

231           LOAD_CONST               5 ('limit')

236           LOAD_CONST               2 ('Any')

231           LOAD_CONST               6 ('offset')

237           LOAD_CONST               2 ('Any')

231           LOAD_CONST               7 ('date_from')

238           LOAD_CONST               2 ('Any')

231           LOAD_CONST               8 ('date_to')

239           LOAD_CONST               2 ('Any')

231           LOAD_CONST               9 ('return')

240           LOAD_CONST              10 ('Dict[str, Any]')

231           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object list_tenant_incidents_for_brokerage at 0x0000018C17D94CE0, file "app\services\tenant\tenant_incident_projection.py", line 231>:
 231            RESUME                   0

 255            LOAD_CONST               1 ('tenant.incidents.list')
                STORE_FAST               7 (surface)

 256            NOP

 257    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               8 (bid)

 258            LOAD_FAST_BORROW         8 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 259            LOAD_GLOBAL              3 (_final + NULL)

 260            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 261            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         7 (surface)

 262            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 263            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 259            BUILD_MAP                4

 264            LOAD_FAST_BORROW         7 (surface)

 259            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 265    L3:     LOAD_FAST_BORROW         1 (severity)
                POP_JUMP_IF_NONE        12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              5 (_safe_severity + NULL)
                LOAD_FAST_BORROW         1 (severity)
                CALL                     1
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               9 (None)
        L5:     STORE_FAST               9 (sev)

 266            LOAD_FAST_BORROW         2 (status)
                POP_JUMP_IF_NONE        12 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              7 (_safe_status + NULL)
                LOAD_FAST_BORROW         2 (status)
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               9 (None)
        L7:     STORE_FAST              10 (stat)

 267            LOAD_GLOBAL              9 (_clamp_int + NULL)
                LOAD_FAST_BORROW         3 (limit)
                LOAD_SMALL_INT           1
                LOAD_SMALL_INT         100
                LOAD_SMALL_INT          25
                CALL                     4
                STORE_FAST              11 (cap)

 268            LOAD_GLOBAL              9 (_clamp_int + NULL)
                LOAD_FAST_BORROW         4 (offset)
                LOAD_SMALL_INT           0
                LOAD_CONST              10 (5000)
                LOAD_SMALL_INT           0
                CALL                     4
                STORE_FAST              12 (off)

 269            LOAD_FAST_BORROW         5 (date_from)
                POP_JUMP_IF_NONE        12 (to L8)
                NOT_TAKEN
                LOAD_GLOBAL             11 (_safe_iso_date + NULL)
                LOAD_FAST_BORROW         5 (date_from)
                CALL                     1
                JUMP_FORWARD             1 (to L9)
        L8:     LOAD_CONST               9 (None)
        L9:     STORE_FAST              13 (dfrom)

 270            LOAD_FAST_BORROW         6 (date_to)
                POP_JUMP_IF_NONE        12 (to L10)
                NOT_TAKEN
                LOAD_GLOBAL             11 (_safe_iso_date + NULL)
                LOAD_FAST_BORROW         6 (date_to)
                CALL                     1
                JUMP_FORWARD             1 (to L11)
       L10:     LOAD_CONST               9 (None)
       L11:     STORE_FAST              14 (dto)

 271            LOAD_GLOBAL             13 (_get_db + NULL)
                CALL                     0
                STORE_FAST              15 (db)

 272            LOAD_FAST_BORROW        15 (db)
                POP_JUMP_IF_NOT_NONE    29 (to L13)
                NOT_TAKEN

 273            LOAD_GLOBAL              3 (_final + NULL)

 274            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 275            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         7 (surface)

 276            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         8 (bid)

 277            LOAD_CONST              13 ('rows')
                BUILD_LIST               0

 278            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 279            LOAD_CONST               7 ('warnings')
                LOAD_CONST              15 ('db_unavailable')
                BUILD_LIST               1

 280            LOAD_CONST               5 ('error_code')
                LOAD_CONST              15 ('db_unavailable')

 273            BUILD_MAP                7

 281            LOAD_FAST_BORROW         7 (surface)

 273            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L12:     RETURN_VALUE

 282   L13:     NOP

 286   L14:     LOAD_FAST_BORROW        15 (db)
                LOAD_ATTR               15 (table + NULL|self)
                LOAD_GLOBAL             16 (_TABLE_NAME)
                CALL                     1
                LOAD_ATTR               19 (select + NULL|self)
                LOAD_CONST              16 ('*')
                CALL                     1
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         8 (bid)
                CALL                     2
                STORE_FAST              16 (q)

 287            LOAD_FAST_BORROW         9 (sev)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L17)
       L15:     NOT_TAKEN

 288   L16:     LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST              17 ('severity')
                LOAD_FAST_BORROW         9 (sev)
                CALL                     2
                STORE_FAST              16 (q)

 289   L17:     LOAD_FAST_BORROW        10 (stat)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L20)
       L18:     NOT_TAKEN

 290   L19:     LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               21 (eq + NULL|self)
                LOAD_CONST               2 ('status')
                LOAD_FAST_BORROW        10 (stat)
                CALL                     2
                STORE_FAST              16 (q)

 291   L20:     LOAD_FAST_BORROW        13 (dfrom)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L23)
       L21:     NOT_TAKEN

 293   L22:     LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               23 (gte + NULL|self)
                LOAD_CONST              18 ('opened_at')
                LOAD_FAST_BORROW        13 (dfrom)
                CALL                     2
                STORE_FAST              16 (q)

 294   L23:     LOAD_FAST_BORROW        14 (dto)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L26)
       L24:     NOT_TAKEN

 296   L25:     LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               25 (lte + NULL|self)
                LOAD_CONST              18 ('opened_at')
                LOAD_FAST_BORROW        14 (dto)
                CALL                     2
                STORE_FAST              16 (q)

 301   L26:     LOAD_GLOBAL             27 (min + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (cap, off)
                BINARY_OP                0 (+)
                LOAD_SMALL_INT         200
                CALL                     2
                STORE_FAST              17 (fetch)

 302            LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               29 (order + NULL|self)
                LOAD_CONST              18 ('opened_at')
                LOAD_CONST              19 (True)
                LOAD_CONST              20 (('desc',))
                CALL_KW                  2
                LOAD_ATTR               31 (limit + NULL|self)
                LOAD_FAST_BORROW        17 (fetch)
                CALL                     1
                STORE_FAST              16 (q)

 303            LOAD_FAST_BORROW        16 (q)
                LOAD_ATTR               33 (execute + NULL|self)
                CALL                     0
                STORE_FAST              18 (resp)

 318   L27:     LOAD_GLOBAL             45 (getattr + NULL)
                LOAD_FAST               18 (resp)
                LOAD_CONST              24 ('data')
                LOAD_CONST               9 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
       L28:     NOT_TAKEN
       L29:     POP_TOP
                BUILD_LIST               0
       L30:     STORE_FAST              20 (data)

 321            LOAD_FAST               20 (data)
                LOAD_FAST_LOAD_FAST    204 (off, off)
                LOAD_FAST               11 (cap)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST              21 (sliced_data)

 322            BUILD_LIST               0
                STORE_FAST              22 (rows)

 323            LOAD_FAST               21 (sliced_data)
                GET_ITER
       L31:     FOR_ITER                79 (to L34)
                STORE_FAST              23 (r)

 324            LOAD_GLOBAL             47 (isinstance + NULL)
                LOAD_FAST               23 (r)
                LOAD_GLOBAL             48 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L32)
                NOT_TAKEN

 325            JUMP_BACKWARD           27 (to L31)

 329   L32:     LOAD_FAST               23 (r)
                LOAD_ATTR               51 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                STORE_FAST              24 (row_bid)

 330            LOAD_FAST               24 (row_bid)
                LOAD_FAST                8 (bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L33)
                NOT_TAKEN

 331            JUMP_BACKWARD           53 (to L31)

 332   L33:     LOAD_FAST               22 (rows)
                LOAD_ATTR               53 (append + NULL|self)
                LOAD_GLOBAL             55 (_project_row + NULL)
                LOAD_FAST               23 (r)
                CALL                     1
                CALL                     1
                POP_TOP
                JUMP_BACKWARD           81 (to L31)

 323   L34:     END_FOR
                POP_ITER

 335            LOAD_GLOBAL             57 (sum + NULL)
                LOAD_CONST              25 (<code object <genexpr> at 0x0000018C18026530, file "app\services\tenant\tenant_incident_projection.py", line 335>)
                MAKE_FUNCTION

 336            LOAD_FAST_LOAD_FAST    154 (sev, stat)
                LOAD_FAST_LOAD_FAST    222 (dfrom, dto)
                BUILD_TUPLE              4
                GET_ITER

 335            CALL                     0
                CALL                     1
                STORE_FAST              25 (filter_count)

 338            LOAD_GLOBAL              3 (_final + NULL)

 339            LOAD_CONST               2 ('status')
                LOAD_CONST              26 ('ok')

 340            LOAD_CONST               4 ('surface')
                LOAD_FAST                7 (surface)

 341            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                8 (bid)

 342            LOAD_CONST              13 ('rows')
                LOAD_FAST               22 (rows)

 343            LOAD_CONST              14 ('count')
                LOAD_GLOBAL             59 (len + NULL)
                LOAD_FAST               22 (rows)
                CALL                     1

 344            LOAD_CONST              27 ('limit')
                LOAD_FAST               11 (cap)

 345            LOAD_CONST              28 ('offset')
                LOAD_FAST               12 (off)

 346            LOAD_CONST              29 ('filter_count')
                LOAD_FAST               25 (filter_count)

 347            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 348            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 (None)

 338            BUILD_MAP               10

 349            LOAD_FAST                7 (surface)

 338            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L35:     RETURN_VALUE

  --   L36:     PUSH_EXC_INFO

 304            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      104 (to L42)
                NOT_TAKEN
                STORE_FAST              19 (e)

 305   L37:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 306            LOAD_CONST              21 ('tenant_incident_projection list query error type=')

 307            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 306            BUILD_STRING             2

 305            CALL                     1
                POP_TOP

 309            LOAD_GLOBAL              3 (_final + NULL)

 310            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 311            LOAD_CONST               4 ('surface')
                LOAD_FAST                7 (surface)

 312            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                8 (bid)

 313            LOAD_CONST              13 ('rows')
                BUILD_LIST               0

 314            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 315            LOAD_CONST               7 ('warnings')
                LOAD_CONST              22 ('db_query_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 316            LOAD_CONST               5 ('error_code')
                LOAD_CONST              23 ('db_query_failed')

 309            BUILD_MAP                7

 317            LOAD_FAST                7 (surface)

 309            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L38:     SWAP                     2
       L39:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
       L40:     RETURN_VALUE

  --   L41:     LOAD_CONST               9 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 304   L42:     RERAISE                  0

  --   L43:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L44:     PUSH_EXC_INFO

 350            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      101 (to L49)
                NOT_TAKEN
                STORE_FAST              19 (e)

 351   L45:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 352            LOAD_CONST              30 ('list_tenant_incidents_for_brokerage error type=')

 353            LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE

 352            BUILD_STRING             2

 351            CALL                     1
                POP_TOP

 355            LOAD_GLOBAL              3 (_final + NULL)

 356            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 357            LOAD_CONST               4 ('surface')
                LOAD_FAST                7 (surface)

 358            LOAD_CONST              13 ('rows')
                BUILD_LIST               0

 359            LOAD_CONST              14 ('count')
                LOAD_SMALL_INT           0

 360            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 361            LOAD_CONST               5 ('error_code')
                LOAD_CONST              31 ('unexpected:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               19 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 355            BUILD_MAP                6

 362            LOAD_FAST                7 (surface)

 355            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L46:     SWAP                     2
       L47:     POP_EXCEPT
                LOAD_CONST               9 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RETURN_VALUE

  --   L48:     LOAD_CONST               9 (None)
                STORE_FAST              19 (e)
                DELETE_FAST             19 (e)
                RERAISE                  1

 350   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L44 [0]
  L3 to L12 -> L44 [0]
  L14 to L15 -> L36 [0]
  L16 to L18 -> L36 [0]
  L19 to L21 -> L36 [0]
  L22 to L24 -> L36 [0]
  L25 to L27 -> L36 [0]
  L27 to L28 -> L44 [0]
  L29 to L35 -> L44 [0]
  L36 to L37 -> L43 [1] lasti
  L37 to L38 -> L41 [1] lasti
  L38 to L39 -> L43 [1] lasti
  L39 to L40 -> L44 [0]
  L41 to L43 -> L43 [1] lasti
  L43 to L44 -> L44 [0]
  L44 to L45 -> L50 [1] lasti
  L45 to L46 -> L48 [1] lasti
  L46 to L47 -> L50 [1] lasti
  L48 to L50 -> L50 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18026530, file "app\services\tenant\tenant_incident_projection.py", line 335>:
 335           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)

 336   L2:     FOR_ITER                12 (to L5)
               STORE_FAST_LOAD_FAST    17 (x, x)
       L3:     POP_JUMP_IF_NOT_NONE     3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD            8 (to L2)
       L4:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           14 (to L2)
       L5:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L6 [0] lasti
  L4 to L6 -> L6 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app\services\tenant\tenant_incident_projection.py", line 365>:
365           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

366           LOAD_CONST               2 ('Any')

365           LOAD_CONST               3 ('incident_id')

367           LOAD_CONST               2 ('Any')

365           LOAD_CONST               4 ('return')

368           LOAD_CONST               5 ('Dict[str, Any]')

365           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_tenant_incident_for_brokerage at 0x0000018C181B3A50, file "app\services\tenant\tenant_incident_projection.py", line 365>:
 365            RESUME                   0

 373            LOAD_CONST               1 ('tenant.incidents.get')
                STORE_FAST               2 (surface)

 374            NOP

 375    L1:     LOAD_GLOBAL              1 (_safe_brokerage + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                STORE_FAST               3 (bid)

 376            LOAD_GLOBAL              3 (_safe_incident_id + NULL)
                LOAD_FAST_BORROW         1 (incident_id)
                CALL                     1
                STORE_FAST               4 (iid)

 377            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L3)
                NOT_TAKEN

 378            LOAD_GLOBAL              5 (_final + NULL)

 379            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 380            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 381            LOAD_CONST               5 ('error_code')
                LOAD_CONST               6 ('invalid_brokerage_id')

 382            LOAD_CONST               7 ('warnings')
                LOAD_CONST               6 ('invalid_brokerage_id')
                BUILD_LIST               1

 378            BUILD_MAP                4

 383            LOAD_FAST_BORROW         2 (surface)

 378            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L2:     RETURN_VALUE

 384    L3:     LOAD_FAST_BORROW         4 (iid)
                TO_BOOL
                POP_JUMP_IF_TRUE        23 (to L7)
        L4:     NOT_TAKEN

 385    L5:     LOAD_GLOBAL              5 (_final + NULL)

 386            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 387            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 388            LOAD_CONST               5 ('error_code')
                LOAD_CONST               9 ('invalid_incident_id')

 389            LOAD_CONST               7 ('warnings')
                LOAD_CONST               9 ('invalid_incident_id')
                BUILD_LIST               1

 385            BUILD_MAP                4

 390            LOAD_FAST_BORROW         2 (surface)

 385            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L6:     RETURN_VALUE

 391    L7:     LOAD_GLOBAL              7 (_get_db + NULL)
                CALL                     0
                STORE_FAST               5 (db)

 392            LOAD_FAST_BORROW         5 (db)
                POP_JUMP_IF_NOT_NONE    25 (to L9)
                NOT_TAKEN

 393            LOAD_GLOBAL              5 (_final + NULL)

 394            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 395            LOAD_CONST               4 ('surface')
                LOAD_FAST_BORROW         2 (surface)

 396            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 397            LOAD_CONST               7 ('warnings')
                LOAD_CONST              13 ('db_unavailable')
                BUILD_LIST               1

 398            LOAD_CONST               5 ('error_code')
                LOAD_CONST              13 ('db_unavailable')

 393            BUILD_MAP                5

 399            LOAD_FAST_BORROW         2 (surface)

 393            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
        L8:     RETURN_VALUE

 400    L9:     NOP

 403   L10:     LOAD_FAST_BORROW         5 (db)
                LOAD_ATTR                9 (table + NULL|self)
                LOAD_GLOBAL             10 (_TABLE_NAME)
                CALL                     1

 404            LOAD_ATTR               13 (select + NULL|self)
                LOAD_CONST              14 ('*')
                CALL                     1

 405            LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 406            LOAD_ATTR               15 (eq + NULL|self)
                LOAD_CONST              15 ('incident_id')
                LOAD_FAST_BORROW         4 (iid)
                CALL                     2

 407            LOAD_ATTR               17 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 402            STORE_FAST               6 (q)

 409            LOAD_FAST_BORROW         6 (q)
                LOAD_ATTR               19 (execute + NULL|self)
                CALL                     0
                STORE_FAST               7 (resp)

 422   L11:     LOAD_GLOBAL             31 (getattr + NULL)
                LOAD_FAST                7 (resp)
                LOAD_CONST              19 ('data')
                LOAD_CONST              10 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L14)
       L12:     NOT_TAKEN
       L13:     POP_TOP
                BUILD_LIST               0
       L14:     STORE_FAST               9 (data)

 423            LOAD_FAST                9 (data)
                TO_BOOL
                POP_JUMP_IF_FALSE       30 (to L17)
       L15:     NOT_TAKEN
       L16:     LOAD_GLOBAL             33 (isinstance + NULL)
                LOAD_FAST                9 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_GLOBAL             34 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L19)
                NOT_TAKEN

 424   L17:     LOAD_GLOBAL              5 (_final + NULL)

 425            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 426            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 427            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                3 (bid)

 428            LOAD_CONST               5 ('error_code')
                LOAD_CONST              20 ('incident_not_found')

 429            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('incident_not_found')
                BUILD_LIST               1

 424            BUILD_MAP                5

 430            LOAD_FAST                2 (surface)

 424            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L18:     RETURN_VALUE

 431   L19:     LOAD_FAST                9 (data)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              10 (row)

 432            LOAD_FAST               10 (row)
                LOAD_ATTR               37 (get + NULL|self)
                LOAD_CONST              12 ('brokerage_id')
                CALL                     1
                LOAD_FAST                3 (bid)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       25 (to L21)
                NOT_TAKEN

 434            LOAD_GLOBAL              5 (_final + NULL)

 435            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 436            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 437            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                3 (bid)

 438            LOAD_CONST               5 ('error_code')
                LOAD_CONST              20 ('incident_not_found')

 439            LOAD_CONST               7 ('warnings')
                LOAD_CONST              20 ('incident_not_found')
                BUILD_LIST               1

 434            BUILD_MAP                5

 440            LOAD_FAST                2 (surface)

 434            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L20:     RETURN_VALUE

 441   L21:     LOAD_GLOBAL              5 (_final + NULL)

 442            LOAD_CONST               2 ('status')
                LOAD_CONST              21 ('ok')

 443            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 444            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                3 (bid)

 445            LOAD_CONST              22 ('row')
                LOAD_GLOBAL             39 (_project_row + NULL)
                LOAD_FAST               10 (row)
                CALL                     1

 446            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 447            LOAD_CONST               5 ('error_code')
                LOAD_CONST              10 (None)

 441            BUILD_MAP                6

 448            LOAD_FAST                2 (surface)

 441            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L22:     RETURN_VALUE

  --   L23:     PUSH_EXC_INFO

 410            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      100 (to L29)
                NOT_TAKEN
                STORE_FAST               8 (e)

 411   L24:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 412            LOAD_CONST              16 ('tenant_incident_projection get query error type=')

 413            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 412            BUILD_STRING             2

 411            CALL                     1
                POP_TOP

 415            LOAD_GLOBAL              5 (_final + NULL)

 416            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 417            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 418            LOAD_CONST              12 ('brokerage_id')
                LOAD_FAST                3 (bid)

 419            LOAD_CONST               7 ('warnings')
                LOAD_CONST              17 ('db_query_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 420            LOAD_CONST               5 ('error_code')
                LOAD_CONST              18 ('db_query_failed')

 415            BUILD_MAP                5

 421            LOAD_FAST                2 (surface)

 415            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L25:     SWAP                     2
       L26:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
       L27:     RETURN_VALUE

  --   L28:     LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 410   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L31:     PUSH_EXC_INFO

 449            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L36)
                NOT_TAKEN
                STORE_FAST               8 (e)

 450   L32:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 451            LOAD_CONST              23 ('get_tenant_incident_for_brokerage error type=')

 452            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 451            BUILD_STRING             2

 450            CALL                     1
                POP_TOP

 454            LOAD_GLOBAL              5 (_final + NULL)

 455            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 456            LOAD_CONST               4 ('surface')
                LOAD_FAST                2 (surface)

 457            LOAD_CONST               5 ('error_code')
                LOAD_CONST              24 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 458            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 454            BUILD_MAP                4

 459            LOAD_FAST                2 (surface)

 454            LOAD_CONST               8 (('surface',))
                CALL_KW                  2
       L33:     SWAP                     2
       L34:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L35:     LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 449   L36:     RERAISE                  0

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L31 [0]
  L3 to L4 -> L31 [0]
  L5 to L6 -> L31 [0]
  L7 to L8 -> L31 [0]
  L10 to L11 -> L23 [0]
  L11 to L12 -> L31 [0]
  L13 to L15 -> L31 [0]
  L16 to L18 -> L31 [0]
  L19 to L20 -> L31 [0]
  L21 to L22 -> L31 [0]
  L23 to L24 -> L30 [1] lasti
  L24 to L25 -> L28 [1] lasti
  L25 to L26 -> L30 [1] lasti
  L26 to L27 -> L31 [0]
  L28 to L30 -> L30 [1] lasti
  L30 to L31 -> L31 [0]
  L31 to L32 -> L37 [1] lasti
  L32 to L33 -> L35 [1] lasti
  L33 to L34 -> L37 [1] lasti
  L35 to L37 -> L37 [1] lasti
```
