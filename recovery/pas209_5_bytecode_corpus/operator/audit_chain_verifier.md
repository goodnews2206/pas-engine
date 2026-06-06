# operator/audit_chain_verifier

- **pyc:** `app\services\operator\__pycache__\audit_chain_verifier.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/audit_chain_verifier.py`
- **co_filename (from bytecode):** `app\services\operator\audit_chain_verifier.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS176 — Audit chain verifier + Merkle root computation.

Operator-callable surface for "is the audit chain intact, and
what is the Merkle root of the most recent window?". Builds
on PAS175's row-level hash chain with three additions:

* **Merkle root computation** over a window of audit rows.
* **Window verification** that combines the PAS175
  `verify_audit_chain` walk with persisting a Merkle root
  to the v24 ``pas_audit_merkle_roots`` table.
* **Structural chain-break alert** that builds a closed-
  shape Alert and routes through PAS171's pilot Slack
  transport. NO autonomous remediation; the alert is
  informational only.

Doctrine:

* **Read-only on the audit log.** This module NEVER updates
  or deletes audit rows; it reads + computes + emits.
* **Merkle root insert is operator-driven.** The verifier
  exposes `persist_merkle_root(...)` but only the operator
  script calls it; there is no scheduler / cron / startup
  hook.
* **Deterministic Merkle.** Same row set → same root, byte-
  for-byte. Internal nodes use sha256 over the canonical
  concatenation of left + right hashes. Odd leaves are
  hashed with themselves.
* **No PII in any envelope.** Merkle leaves are the
  row_hash values (already PII-free per PAS175 doctrine).
  Window descriptors are timestamps + counts only.
* **No automatic remediation.** The Slack alert is
  structural; the operator decides what to do.
* **NEVER raises.** DB unavailable → ``status="skipped"``.

Public surface:

  * ``compute_merkle_root(row_hashes)`` — pure function.
  * ``verify_window(brokerage_id=None, window_hours=24, now=None)`` — read-only.
  * ``persist_merkle_root(window_envelope, generated_by=None)`` — INSERT into v24 table.
  * ``emit_chain_break_alert(verification_envelope, webhook_url=None, brokerage=None)`` — opt-in Slack route.
```

## Imports

`Alert`, `Any`, `Dict`, `GENESIS_HASH`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.monitoring.contracts`, `app.services.monitoring.slack_alert_transport`, `app.services.operator.audit_integrity`, `compute_row_hash`, `datetime`, `get_supabase`, `hashlib`, `logging`, `send_pilot_alert_to_slack`, `timedelta`, `timezone`, `typing`, `uuid`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_brokerage_id`, `_bound_generated_by`, `_clamp_window_hours`, `_get_db_safe`, `_iso`, `_now_dt`, `compute_merkle_root`, `emit_chain_break_alert`, `persist_merkle_root`, `verify_window`

## Env-key candidates

`HIGH`, `INTEGRITY`

## String constants (redacted where noted)

- '\nPAS176 — Audit chain verifier + Merkle root computation.\n\nOperator-callable surface for "is the audit chain intact, and\nwhat is the Merkle root of the most recent window?". Builds\non PAS175\'s row-level hash chain with three additions:\n\n* **Merkle root computation** over a window of audit rows.\n* **Window verification** that combines the PAS175\n  `verify_audit_chain` walk with persisting a Merkle root\n  to the v24 ``pas_audit_merkle_roots`` table.\n* **Structural chain-break alert** that builds a closed-\n  shape Alert and routes through PAS171\'s pilot Slack\n  transport. NO autonomous remediation; the alert is\n  informational only.\n\nDoctrine:\n\n* **Read-only on the audit log.** This module NEVER updates\n  or deletes audit rows; it reads + computes + emits.\n* **Merkle root insert is operator-driven.** The verifier\n  exposes `persist_merkle_root(...)` but only the operator\n  script calls it; there is no scheduler / cron / startup\n  hook.\n* **Deterministic Merkle.** Same row set → same root, byte-\n  for-byte. Internal nodes use sha256 over the canonical\n  concatenation of left + right hashes. Odd leaves are\n  hashed with themselves.\n* **No PII in any envelope.** Merkle leaves are the\n  row_hash values (already PII-free per PAS175 doctrine).\n  Window descriptors are timestamps + counts only.\n* **No automatic remediation.** The Slack alert is\n  structural; the operator decides what to do.\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n\nPublic surface:\n\n  * ``compute_merkle_root(row_hashes)`` — pure function.\n  * ``verify_window(brokerage_id=None, window_hours=24, now=None)`` — read-only.\n  * ``persist_merkle_root(window_envelope, generated_by=None)`` — INSERT into v24 table.\n  * ``emit_chain_break_alert(verification_envelope, webhook_url=None, brokerage=None)`` — opt-in Slack route.\n'
- 'pas.operator.audit_chain_verifier'
- 'pas_audit_merkle_roots'
- 'brokerage_id'
- 'window_hours'
- 'now'
- 'generated_by'
- 'webhook_url'
- 'brokerage'
- 'include_metadata'
- 'Any'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'audit_chain_verifier db client unavailable type='
- 'value'
- 'int'
- 'Optional[str]'
- 'row_hashes'
- 'Compute a Merkle root over an ordered list of sha256-hex\nrow_hash strings. Deterministic. NEVER raises.\n\nAlgorithm:\n  * Empty list → ``"0" * 64`` (canonical empty root).\n  * Single leaf → that leaf\'s hash returned as-is.\n  * Otherwise: repeatedly pair leaves left-to-right; if\n    the layer has an odd count, the final leaf is\n    hashed with itself. Each internal node is\n    ``sha256(left || right)`` over the lower-cased hex\n    concatenation. Repeat until one node remains.\n'
- 'utf-8'
- 'compute_merkle_root unexpected error type='
- 🔒 '<REDACTED:secret-like value, len=64>'
- '0123456789abcdef'
- 'Dict[str, Any]'
- 'Verify the audit chain for the window ending at ``now``\nspanning ``window_hours`` back. Computes the chain-break\nlist AND the Merkle root over the window\'s row_hash values.\n\nReturns a closed-shape envelope::\n\n    {\n      "status":          "ok" | "skipped",\n      "brokerage_id":    Optional[str],\n      "window_hours":    int,\n      "window_start":    "<iso>",\n      "window_end":      "<iso>",\n      "rows_in_window":  int,\n      "chain_status":    "ok" | "genesis" | "degraded",\n      "breaks_count":    int,\n      "breaks":          [<structural break>, ...],\n      "merkle_root":     "<sha256 hex>",\n      "warnings":        [<structural>],\n      "error_code":      None | "<structural>",\n    }\n\nNEVER raises. NEVER returns PII.\n'
- 'status'
- 'skipped'
- 'window_start'
- 'window_end'
- 'rows_in_window'
- 'chain_status'
- 'genesis'
- 'breaks_count'
- 'breaks'
- 'merkle_root'
- 'warnings'
- 'audit_store_unavailable'
- 'error_code'
- 'pas_operator_actions_log'
- 'action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash'
- 'occurred_at'
- 'data'
- 'verify_window read error type='
- 'db_read_failed:'
- 'action_id'
- 'prev_hash'
- 'row_hash'
- 'break_type'
- 'missing_prev_hash'
- 'prev_hash_mismatch'
- 'missing_row_hash'
- 'row_hash_mismatch'
- 'degraded'
- 'window_envelope'
- 'INSERT a row into ``pas_audit_merkle_roots`` from a\nverify_window envelope. Append-only — NEVER updates an\nexisting root. NEVER raises.\n\nReturns a structural envelope with the persisted row_id\non success or a skipped envelope on DB-unavailable.'
- 'failed'
- 'invalid_window_envelope'
- 'window_envelope_not_ok'
- 'invalid_merkle_root_shape'
- 'root_id'
- 'generated_at'
- 'merkle_row'
- 'persist_merkle_root db error type='
- 'db_write_failed:'
- 'verification_envelope'
- 'bool'
- 'If the verification envelope shows ``chain_status="degraded"``,\nconstruct a structural Alert and route it through PAS171\'s\npilot Slack transport. NEVER raises. NEVER emits when the\nchain is intact.\n\nReturns one of:\n  * ``status="skipped"`` + ``chain_intact`` — no alert needed.\n  * ``status="skipped"`` + ``slack_webhook_not_configured``\n    when the operator has no webhook set.\n  * ``status="sent"`` — alert was POSTed.\n  * ``status="failed"`` / ``"refused"`` / ``"rate_limited"``\n    — surfaced from PAS171\'s transport.\n'
- 'invalid_verification_envelope'
- 'chain_intact'
- 'audit.chain.broken:'
- 'global'
- 'INTEGRITY'
- 'HIGH'
- 'PAS operator audit chain integrity break detected'
- 'Verification of the operator audit chain detected '
- ' break(s) in window starting '
- '. Operator must investigate. No autonomous remediation has been performed.'
- 'app.services.operator.audit_chain_verifier'
- 'warning_count'
- 'audit_chain_broken'
- 'severity'
- 'emit_chain_break_alert unexpected error type='
- 'unexpected:'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS176 — Audit chain verifier + Merkle root computation.\n\nOperator-callable surface for "is the audit chain intact, and\nwhat is the Merkle root of the most recent window?". Builds\non PAS175\'s row-level hash chain with three additions:\n\n* **Merkle root computation** over a window of audit rows.\n* **Window verification** that combines the PAS175\n  `verify_audit_chain` walk with persisting a Merkle root\n  to the v24 ``pas_audit_merkle_roots`` table.\n* **Structural chain-break alert** that builds a closed-\n  shape Alert and routes through PAS171\'s pilot Slack\n  transport. NO autonomous remediation; the alert is\n  informational only.\n\nDoctrine:\n\n* **Read-only on the audit log.** This module NEVER updates\n  or deletes audit rows; it reads + computes + emits.\n* **Merkle root insert is operator-driven.** The verifier\n  exposes `persist_merkle_root(...)` but only the operator\n  script calls it; there is no scheduler / cron / startup\n  hook.\n* **Deterministic Merkle.** Same row set → same root, byte-\n  for-byte. Internal nodes use sha256 over the canonical\n  concatenation of left + right hashes. Odd leaves are\n  hashed with themselves.\n* **No PII in any envelope.** Merkle leaves are the\n  row_hash values (already PII-free per PAS175 doctrine).\n  Window descriptors are timestamps + counts only.\n* **No automatic remediation.** The Slack alert is\n  structural; the operator decides what to do.\n* **NEVER raises.** DB unavailable → ``status="skipped"``.\n\nPublic surface:\n\n  * ``compute_merkle_root(row_hashes)`` — pure function.\n  * ``verify_window(brokerage_id=None, window_hours=24, now=None)`` — read-only.\n  * ``persist_merkle_root(window_envelope, generated_by=None)`` — INSERT into v24 table.\n  * ``emit_chain_break_alert(verification_envelope, webhook_url=None, brokerage=None)`` — opt-in Slack route.\n')
              STORE_NAME               0 (__doc__)

 44           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 46           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (hashlib)
              STORE_NAME               3 (hashlib)

 47           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (logging)
              STORE_NAME               4 (logging)

 48           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (uuid)
              STORE_NAME               5 (uuid)

 49           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
              IMPORT_NAME              6 (datetime)
              IMPORT_FROM              6 (datetime)
              STORE_NAME               6 (datetime)
              IMPORT_FROM              7 (timedelta)
              STORE_NAME               7 (timedelta)
              IMPORT_FROM              8 (timezone)
              STORE_NAME               8 (timezone)
              POP_TOP

 50           LOAD_SMALL_INT           0
              LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              9 (typing)
              IMPORT_FROM             10 (Any)
              STORE_NAME              10 (Any)
              IMPORT_FROM             11 (Dict)
              STORE_NAME              11 (Dict)
              IMPORT_FROM             12 (List)
              STORE_NAME              12 (List)
              IMPORT_FROM             13 (Optional)
              STORE_NAME              13 (Optional)
              POP_TOP

 53           LOAD_NAME                4 (logging)
              LOAD_ATTR               28 (getLogger)
              PUSH_NULL
              LOAD_CONST               5 ('pas.operator.audit_chain_verifier')
              CALL                     1
              STORE_NAME              15 (logger)

 56           LOAD_CONST               6 ('pas_audit_merkle_roots')
              STORE_NAME              16 (_MERKLE_TABLE)

 59           LOAD_SMALL_INT          24
              STORE_NAME              17 (_DEFAULT_WINDOW_HOURS)

 60           LOAD_SMALL_INT           1
              STORE_NAME              18 (_MIN_WINDOW_HOURS)

 61           LOAD_CONST              35 (720)
              STORE_NAME              19 (_MAX_WINDOW_HOURS)

 64           LOAD_CONST               7 (10000)
              STORE_NAME              20 (_LIST_HARD_CAP)

 71           LOAD_CONST              36 ((None,))
              LOAD_CONST               8 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\audit_chain_verifier.py", line 71>)
              MAKE_FUNCTION
              LOAD_CONST               9 (<code object _now_dt at 0x0000018C179C3C30, file "app\services\operator\audit_chain_verifier.py", line 71>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              21 (_now_dt)

 79           LOAD_CONST              10 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\audit_chain_verifier.py", line 79>)
              MAKE_FUNCTION
              LOAD_CONST              11 (<code object _iso at 0x0000018C18024C30, file "app\services\operator\audit_chain_verifier.py", line 79>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_iso)

 83           LOAD_CONST              12 (<code object _get_db_safe at 0x0000018C17FF1530, file "app\services\operator\audit_chain_verifier.py", line 83>)
              MAKE_FUNCTION
              STORE_NAME              23 (_get_db_safe)

 95           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\audit_chain_verifier.py", line 95>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object _clamp_window_hours at 0x0000018C17F95E60, file "app\services\operator\audit_chain_verifier.py", line 95>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              24 (_clamp_window_hours)

107           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\audit_chain_verifier.py", line 107>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object _bound_brokerage_id at 0x0000018C18010B30, file "app\services\operator\audit_chain_verifier.py", line 107>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              25 (_bound_brokerage_id)

116           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\audit_chain_verifier.py", line 116>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _bound_generated_by at 0x0000018C18010DF0, file "app\services\operator\audit_chain_verifier.py", line 116>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              26 (_bound_generated_by)

129           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\audit_chain_verifier.py", line 129>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object compute_merkle_root at 0x0000018C17E80BD0, file "app\services\operator\audit_chain_verifier.py", line 129>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              27 (compute_merkle_root)

185           LOAD_CONST              21 ('brokerage_id')

187           LOAD_CONST               2 (None)

185           LOAD_CONST              22 ('window_hours')

188           LOAD_NAME               17 (_DEFAULT_WINDOW_HOURS)

185           LOAD_CONST              23 ('now')

189           LOAD_CONST               2 (None)

185           BUILD_MAP                3
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\audit_chain_verifier.py", line 185>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object verify_window at 0x0000018C17D51480, file "app\services\operator\audit_chain_verifier.py", line 185>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              28 (verify_window)

377           LOAD_CONST              26 ('generated_by')

380           LOAD_CONST               2 (None)

377           BUILD_MAP                1
              LOAD_CONST              27 (<code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\audit_chain_verifier.py", line 377>)
              MAKE_FUNCTION
              LOAD_CONST              28 (<code object persist_merkle_root at 0x0000018C17D7DA00, file "app\services\operator\audit_chain_verifier.py", line 377>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              29 (persist_merkle_root)

449           LOAD_CONST              29 ('webhook_url')

452           LOAD_CONST               2 (None)

449           LOAD_CONST              30 ('brokerage')

453           LOAD_CONST               2 (None)

449           LOAD_CONST              31 ('include_metadata')

454           LOAD_CONST              32 (True)

449           BUILD_MAP                3
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18024930, file "app\services\operator\audit_chain_verifier.py", line 449>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object emit_chain_break_alert at 0x0000018C17EF9A30, file "app\services\operator\audit_chain_verifier.py", line 449>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              30 (emit_chain_break_alert)

532           BUILD_LIST               0
              LOAD_CONST              37 (('compute_merkle_root', 'verify_window', 'persist_merkle_root', 'emit_chain_break_alert'))
              LIST_EXTEND              1
              STORE_NAME              31 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\operator\audit_chain_verifier.py", line 71>:
 71           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('datetime')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C179C3C30, file "app\services\operator\audit_chain_verifier.py", line 71>:
 71           RESUME                   0

 72           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_GLOBAL              2 (datetime)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       78 (to L2)
              NOT_TAKEN

 73           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                4 (tzinfo)
              POP_JUMP_IF_NOT_NONE    33 (to L1)
              NOT_TAKEN

 74           LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                7 (replace + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              LOAD_CONST               1 (('tzinfo',))
              CALL_KW                  1
              RETURN_VALUE

 75   L1:     LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR               13 (astimezone + NULL|self)
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

 76   L2:     LOAD_GLOBAL              2 (datetime)
              LOAD_ATTR               14 (now)
              PUSH_NULL
              LOAD_GLOBAL              8 (timezone)
              LOAD_ATTR               10 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\audit_chain_verifier.py", line 79>:
 79           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('dt')
              LOAD_CONST               2 ('datetime')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _iso at 0x0000018C18024C30, file "app\services\operator\audit_chain_verifier.py", line 79>:
 79           RESUME                   0

 80           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF1530, file "app\services\operator\audit_chain_verifier.py", line 83>:
  83           RESUME                   0

  84           NOP

  85   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

  86           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  87           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

  88   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

  89           LOAD_CONST               2 ('audit_chain_verifier db client unavailable type=')

  90           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

  89           BUILD_STRING             2

  88           CALL                     1
               POP_TOP

  92   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

  87   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\audit_chain_verifier.py", line 95>:
 95           RESUME                   0
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

Disassembly of <code object _clamp_window_hours at 0x0000018C17F95E60, file "app\services\operator\audit_chain_verifier.py", line 95>:
  95           RESUME                   0

  96           NOP

  97   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               1 (v)

 100   L2:     LOAD_FAST                1 (v)
               LOAD_GLOBAL              8 (_MIN_WINDOW_HOURS)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        7 (to L3)
               NOT_TAKEN

 101           LOAD_GLOBAL              8 (_MIN_WINDOW_HOURS)
               RETURN_VALUE

 102   L3:     LOAD_FAST                1 (v)
               LOAD_GLOBAL             10 (_MAX_WINDOW_HOURS)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        7 (to L4)
               NOT_TAKEN

 103           LOAD_GLOBAL             10 (_MAX_WINDOW_HOURS)
               RETURN_VALUE

 104   L4:     LOAD_FAST                1 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

  98           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       10 (to L7)
               NOT_TAKEN
               POP_TOP

  99           LOAD_GLOBAL              6 (_DEFAULT_WINDOW_HOURS)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

  98   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\audit_chain_verifier.py", line 107>:
107           RESUME                   0
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

Disassembly of <code object _bound_brokerage_id at 0x0000018C18010B30, file "app\services\operator\audit_chain_verifier.py", line 107>:
107           RESUME                   0

108           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

109           LOAD_CONST               0 (None)
              RETURN_VALUE

110   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

111           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

112   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

113   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\audit_chain_verifier.py", line 116>:
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

Disassembly of <code object _bound_generated_by at 0x0000018C18010DF0, file "app\services\operator\audit_chain_verifier.py", line 116>:
116           RESUME                   0

117           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

118           LOAD_CONST               0 (None)
              RETURN_VALUE

119   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

120           LOAD_FAST_BORROW         1 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT         200
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

121   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

122   L3:     LOAD_FAST_BORROW         1 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "app\services\operator\audit_chain_verifier.py", line 129>:
129           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('row_hashes')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object compute_merkle_root at 0x0000018C17E80BD0, file "app\services\operator\audit_chain_verifier.py", line 129>:
 129            RESUME                   0

 142            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (row_hashes)
                LOAD_GLOBAL              2 (list)
                LOAD_GLOBAL              4 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L1)
                NOT_TAKEN

 143            LOAD_CONST               7 ('0000000000000000000000000000000000000000000000000000000000000000')
                RETURN_VALUE

 144    L1:     BUILD_LIST               0
                STORE_FAST               1 (leaves)

 145            LOAD_FAST_BORROW         0 (row_hashes)
                GET_ITER
        L2:     FOR_ITER               152 (to L11)
                STORE_FAST               2 (h)

 146            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (h)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN

 147            JUMP_BACKWARD           27 (to L2)

 148    L3:     LOAD_FAST_BORROW         2 (h)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                STORE_FAST               3 (h_clean)

 149            LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         3 (h_clean)
                CALL                     1
                LOAD_SMALL_INT          64
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN

 150            JUMP_BACKWARD           75 (to L2)

 151    L4:     LOAD_GLOBAL             14 (all)
                COPY                     1
                LOAD_COMMON_CONSTANT     3 (<built-in function all>)
                IS_OP                    0 (is)
                POP_JUMP_IF_FALSE       28 (to L8)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024E30, file "app\services\operator\audit_chain_verifier.py", line 151>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (h_clean)
                GET_ITER
                CALL                     0
        L5:     FOR_ITER                12 (to L7)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                JUMP_BACKWARD           11 (to L5)
        L6:     POP_ITER
                LOAD_CONST               2 (False)
                JUMP_FORWARD            17 (to L9)
        L7:     END_FOR
                POP_ITER
                LOAD_CONST               3 (True)
                JUMP_FORWARD            13 (to L9)
        L8:     PUSH_NULL
                LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18024E30, file "app\services\operator\audit_chain_verifier.py", line 151>)
                MAKE_FUNCTION
                LOAD_FAST_BORROW         3 (h_clean)
                GET_ITER
                CALL                     0
                CALL                     1
        L9:     TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN

 152            JUMP_BACKWARD          135 (to L2)

 153   L10:     LOAD_FAST_BORROW         1 (leaves)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW         3 (h_clean)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          154 (to L2)

 145   L11:     END_FOR
                POP_ITER

 154            LOAD_FAST_BORROW         1 (leaves)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

 155            LOAD_CONST               7 ('0000000000000000000000000000000000000000000000000000000000000000')
                RETURN_VALUE

 156   L12:     LOAD_FAST                1 (leaves)
                STORE_FAST               4 (layer)

 157   L13:     LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (layer)
                CALL                     1
                LOAD_SMALL_INT           1
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE      162 (to L20)
                NOT_TAKEN

 158            BUILD_LIST               0
                STORE_FAST               5 (next_layer)

 159            LOAD_SMALL_INT           0
                STORE_FAST               6 (i)

 160   L14:     LOAD_FAST_BORROW         6 (i)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (layer)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE      138 (to L19)
                NOT_TAKEN

 161            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (layer, i)
                BINARY_OP               26 ([])
                STORE_FAST               7 (left)

 162            LOAD_FAST_BORROW         6 (i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (layer)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       17 (to L15)
                NOT_TAKEN

 163            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (layer, i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                BINARY_OP               26 ([])
                STORE_FAST               8 (right)
                JUMP_FORWARD             2 (to L16)

 165   L15:     LOAD_FAST                7 (left)
                STORE_FAST               8 (right)

 166   L16:     NOP

 167   L17:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (left, right)
                BINARY_OP                0 (+)
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST               4 ('utf-8')
                CALL                     1
                STORE_FAST               9 (concat)

 168            LOAD_GLOBAL             20 (hashlib)
                LOAD_ATTR               22 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         9 (concat)
                CALL                     1
                LOAD_ATTR               25 (hexdigest + NULL|self)
                CALL                     0
                STORE_FAST              10 (node)

 175   L18:     LOAD_FAST_BORROW         5 (next_layer)
                LOAD_ATTR               17 (append + NULL|self)
                LOAD_FAST_BORROW        10 (node)
                CALL                     1
                POP_TOP

 176            LOAD_FAST_BORROW         6 (i)
                LOAD_SMALL_INT           2
                BINARY_OP               13 (+=)
                STORE_FAST               6 (i)
                JUMP_BACKWARD          153 (to L14)

 177   L19:     LOAD_FAST                5 (next_layer)
                STORE_FAST               4 (layer)
                JUMP_BACKWARD          177 (to L13)

 178   L20:     LOAD_FAST_BORROW         4 (layer)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                RETURN_VALUE

  --   L21:     PUSH_EXC_INFO

 169            LOAD_GLOBAL             26 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       56 (to L25)
                NOT_TAKEN
                STORE_FAST              11 (e)

 170   L22:     LOAD_GLOBAL             28 (logger)
                LOAD_ATTR               31 (warning + NULL|self)

 171            LOAD_CONST               5 ('compute_merkle_root unexpected error type=')

 172            LOAD_GLOBAL             33 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               34 (__name__)
                FORMAT_SIMPLE

 171            BUILD_STRING             2

 170            CALL                     1
                POP_TOP

 174            LOAD_CONST               7 ('0000000000000000000000000000000000000000000000000000000000000000')
                STORE_FAST              10 (node)
       L23:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                JUMP_BACKWARD_NO_INTERRUPT 102 (to L18)

  --   L24:     LOAD_CONST               6 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 169   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L17 to L18 -> L21 [0]
  L21 to L22 -> L26 [1] lasti
  L22 to L23 -> L24 [1] lasti
  L24 to L26 -> L26 [1] lasti

Disassembly of <code object <genexpr> at 0x0000018C18024E30, file "app\services\operator\audit_chain_verifier.py", line 151>:
 151           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                 9 (to L3)
               STORE_FAST_LOAD_FAST    17 (c, c)
               LOAD_CONST               0 ('0123456789abcdef')
               CONTAINS_OP              0 (in)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           11 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024B30, file "app\services\operator\audit_chain_verifier.py", line 185>:
185           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

187           LOAD_CONST               2 ('Optional[str]')

185           LOAD_CONST               3 ('window_hours')

188           LOAD_CONST               4 ('int')

185           LOAD_CONST               5 ('now')

189           LOAD_CONST               6 ('Any')

185           LOAD_CONST               7 ('return')

190           LOAD_CONST               8 ('Dict[str, Any]')

185           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object verify_window at 0x0000018C17D51480, file "app\services\operator\audit_chain_verifier.py", line 185>:
 185            RESUME                   0

 214            LOAD_FAST_BORROW         0 (brokerage_id)
                POP_JUMP_IF_NONE        12 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_brokerage_id + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                CALL                     1
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               1 (None)
        L2:     STORE_FAST               3 (bid)

 215            LOAD_GLOBAL              3 (_clamp_window_hours + NULL)
                LOAD_FAST_BORROW         1 (window_hours)
                CALL                     1
                STORE_FAST               4 (hours)

 216            LOAD_GLOBAL              5 (_now_dt + NULL)
                LOAD_FAST_BORROW         2 (now)
                CALL                     1
                STORE_FAST               5 (now_dt)

 217            LOAD_FAST                5 (now_dt)
                STORE_FAST               6 (window_end)

 218            LOAD_FAST_BORROW         5 (now_dt)
                LOAD_GLOBAL              7 (timedelta + NULL)
                LOAD_FAST_BORROW         4 (hours)
                LOAD_CONST               2 (('hours',))
                CALL_KW                  1
                BINARY_OP               10 (-)
                STORE_FAST               7 (window_start)

 220            LOAD_GLOBAL              9 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               8 (db)

 221            LOAD_FAST_BORROW         8 (db)
                POP_JUMP_IF_NOT_NONE    46 (to L3)
                NOT_TAKEN

 223            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 224            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)

 225            LOAD_CONST               6 ('window_hours')
                LOAD_FAST_BORROW         4 (hours)

 226            LOAD_CONST               7 ('window_start')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         7 (window_start)
                CALL                     1

 227            LOAD_CONST               8 ('window_end')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         6 (window_end)
                CALL                     1

 228            LOAD_CONST               9 ('rows_in_window')
                LOAD_SMALL_INT           0

 229            LOAD_CONST              10 ('chain_status')
                LOAD_CONST              11 ('genesis')

 230            LOAD_CONST              12 ('breaks_count')
                LOAD_SMALL_INT           0

 231            LOAD_CONST              13 ('breaks')
                BUILD_LIST               0

 232            LOAD_CONST              14 ('merkle_root')
                LOAD_CONST              38 ('0000000000000000000000000000000000000000000000000000000000000000')

 233            LOAD_CONST              15 ('warnings')
                LOAD_CONST              16 ('audit_store_unavailable')
                BUILD_LIST               1

 234            LOAD_CONST              17 ('error_code')
                LOAD_CONST              16 ('audit_store_unavailable')

 222            BUILD_MAP               12
                RETURN_VALUE

 240    L3:     NOP

 242    L4:     LOAD_FAST_BORROW         8 (db)
                LOAD_ATTR               13 (table + NULL|self)
                LOAD_CONST              18 ('pas_operator_actions_log')
                CALL                     1

 243            LOAD_ATTR               15 (select + NULL|self)

 244            LOAD_CONST              19 ('action_id, occurred_at, brokerage_id, actor_type, actor_id, action, target_type, target_id, status, warning_count, metadata, prev_hash, row_hash')

 243            CALL                     1

 248            LOAD_ATTR               17 (gt + NULL|self)
                LOAD_CONST              20 ('occurred_at')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         7 (window_start)
                CALL                     1
                CALL                     2

 249            LOAD_ATTR               19 (lt + NULL|self)
                LOAD_CONST              20 ('occurred_at')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST_BORROW         6 (window_end)
                LOAD_GLOBAL              7 (timedelta + NULL)
                LOAD_SMALL_INT           1
                LOAD_CONST              21 (('seconds',))
                CALL_KW                  1
                BINARY_OP                0 (+)
                CALL                     1
                CALL                     2

 250            LOAD_ATTR               21 (order + NULL|self)
                LOAD_CONST              20 ('occurred_at')
                LOAD_CONST              22 (False)
                LOAD_CONST              23 (('desc',))
                CALL_KW                  2

 251            LOAD_ATTR               23 (limit + NULL|self)
                LOAD_GLOBAL             24 (_LIST_HARD_CAP)
                CALL                     1

 241            STORE_FAST               9 (query)

 253            LOAD_FAST_BORROW         3 (bid)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L5)
                NOT_TAKEN

 254            LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               27 (eq + NULL|self)
                LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2
                STORE_FAST               9 (query)

 255    L5:     LOAD_FAST_BORROW         9 (query)
                LOAD_ATTR               29 (execute + NULL|self)
                CALL                     0
                STORE_FAST              10 (result)

 256            LOAD_GLOBAL             31 (list + NULL)
                LOAD_GLOBAL             33 (getattr + NULL)
                LOAD_FAST_BORROW        10 (result)
                LOAD_CONST              24 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                BUILD_LIST               0
        L8:     CALL                     1
                STORE_FAST              11 (rows)

 276    L9:     LOAD_FAST               11 (rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        45 (to L10)
                NOT_TAKEN

 278            LOAD_CONST               3 ('status')
                LOAD_CONST              27 ('ok')

 279            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                3 (bid)

 280            LOAD_CONST               6 ('window_hours')
                LOAD_FAST                4 (hours)

 281            LOAD_CONST               7 ('window_start')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                7 (window_start)
                CALL                     1

 282            LOAD_CONST               8 ('window_end')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                6 (window_end)
                CALL                     1

 283            LOAD_CONST               9 ('rows_in_window')
                LOAD_SMALL_INT           0

 284            LOAD_CONST              10 ('chain_status')
                LOAD_CONST              11 ('genesis')

 285            LOAD_CONST              12 ('breaks_count')
                LOAD_SMALL_INT           0

 286            LOAD_CONST              13 ('breaks')
                BUILD_LIST               0

 287            LOAD_CONST              14 ('merkle_root')
                LOAD_CONST              38 ('0000000000000000000000000000000000000000000000000000000000000000')

 288            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 289            LOAD_CONST              17 ('error_code')
                LOAD_CONST               1 (None)

 277            BUILD_MAP               12
                RETURN_VALUE

 295   L10:     LOAD_SMALL_INT           0
                LOAD_CONST              28 (('compute_row_hash', 'GENESIS_HASH'))
                IMPORT_NAME             22 (app.services.operator.audit_integrity)
                IMPORT_FROM             23 (compute_row_hash)
                STORE_FAST              13 (compute_row_hash)
                IMPORT_FROM             24 (GENESIS_HASH)
                STORE_FAST              14 (GENESIS_HASH)
                POP_TOP

 299            BUILD_LIST               0
                STORE_FAST              15 (breaks)

 300            LOAD_FAST               14 (GENESIS_HASH)
                STORE_FAST              16 (expected_prev)

 301            BUILD_LIST               0
                STORE_FAST              17 (row_hashes)

 307            LOAD_FAST               11 (rows)
                GET_ITER
       L11:     EXTENDED_ARG             1
                FOR_ITER               454 (to L22)
                STORE_FAST              18 (r)

 308            LOAD_GLOBAL             51 (isinstance + NULL)
                LOAD_FAST               18 (r)
                LOAD_GLOBAL             52 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
                NOT_TAKEN

 309            JUMP_BACKWARD           28 (to L11)

 310   L12:     LOAD_FAST               18 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              29 ('action_id')
                CALL                     1
                STORE_FAST              19 (action_id)

 311            LOAD_FAST               18 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              20 ('occurred_at')
                CALL                     1
                STORE_FAST              20 (occurred_at)

 312            LOAD_FAST               18 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              30 ('prev_hash')
                CALL                     1
                STORE_FAST              21 (stored_prev)

 313            LOAD_FAST               18 (r)
                LOAD_ATTR               55 (get + NULL|self)
                LOAD_CONST              31 ('row_hash')
                CALL                     1
                STORE_FAST              22 (stored_row)

 314            LOAD_FAST               13 (compute_row_hash)
                PUSH_NULL
                LOAD_FAST               16 (expected_prev)
                LOAD_FAST               18 (r)
                CALL                     2
                STORE_FAST              23 (recomputed_hash)

 315            LOAD_GLOBAL             51 (isinstance + NULL)
                LOAD_FAST               21 (stored_prev)
                LOAD_GLOBAL             56 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L13)
                NOT_TAKEN
                LOAD_FAST               21 (stored_prev)
                LOAD_ATTR               59 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L14)
                NOT_TAKEN

 316   L13:     LOAD_FAST               15 (breaks)
                LOAD_ATTR               61 (append + NULL|self)

 317            LOAD_CONST              29 ('action_id')
                LOAD_FAST               19 (action_id)

 318            LOAD_CONST              20 ('occurred_at')
                LOAD_FAST               20 (occurred_at)

 319            LOAD_CONST              32 ('break_type')
                LOAD_CONST              33 ('missing_prev_hash')

 316            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            46 (to L15)

 321   L14:     LOAD_FAST               21 (stored_prev)
                LOAD_FAST               16 (expected_prev)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       40 (to L15)
                NOT_TAKEN

 327            LOAD_GLOBAL             63 (len + NULL)
                LOAD_FAST               17 (row_hashes)
                CALL                     1
                LOAD_SMALL_INT           0
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       24 (to L15)
                NOT_TAKEN

 328            LOAD_FAST               15 (breaks)
                LOAD_ATTR               61 (append + NULL|self)

 329            LOAD_CONST              29 ('action_id')
                LOAD_FAST               19 (action_id)

 330            LOAD_CONST              20 ('occurred_at')
                LOAD_FAST               20 (occurred_at)

 331            LOAD_CONST              32 ('break_type')
                LOAD_CONST              34 ('prev_hash_mismatch')

 328            BUILD_MAP                3
                CALL                     1
                POP_TOP

 333   L15:     LOAD_GLOBAL             51 (isinstance + NULL)
                LOAD_FAST               22 (stored_row)
                LOAD_GLOBAL             56 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L16)
                NOT_TAKEN
                LOAD_FAST               22 (stored_row)
                LOAD_ATTR               59 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L17)
                NOT_TAKEN

 334   L16:     LOAD_FAST               15 (breaks)
                LOAD_ATTR               61 (append + NULL|self)

 335            LOAD_CONST              29 ('action_id')
                LOAD_FAST               19 (action_id)

 336            LOAD_CONST              20 ('occurred_at')
                LOAD_FAST               20 (occurred_at)

 337            LOAD_CONST              32 ('break_type')
                LOAD_CONST              35 ('missing_row_hash')

 334            BUILD_MAP                3
                CALL                     1
                POP_TOP
                JUMP_FORWARD            30 (to L18)

 339   L17:     LOAD_FAST               22 (stored_row)
                LOAD_FAST               23 (recomputed_hash)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       24 (to L18)
                NOT_TAKEN

 340            LOAD_FAST               15 (breaks)
                LOAD_ATTR               61 (append + NULL|self)

 341            LOAD_CONST              29 ('action_id')
                LOAD_FAST               19 (action_id)

 342            LOAD_CONST              20 ('occurred_at')
                LOAD_FAST               20 (occurred_at)

 343            LOAD_CONST              32 ('break_type')
                LOAD_CONST              36 ('row_hash_mismatch')

 340            BUILD_MAP                3
                CALL                     1
                POP_TOP

 348   L18:     LOAD_GLOBAL             51 (isinstance + NULL)
                LOAD_FAST               22 (stored_row)
                LOAD_GLOBAL             56 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       68 (to L19)
                NOT_TAKEN
                LOAD_FAST               22 (stored_row)
                LOAD_ATTR               59 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       46 (to L19)
                NOT_TAKEN

 349            LOAD_FAST               17 (row_hashes)
                LOAD_ATTR               61 (append + NULL|self)
                LOAD_FAST               22 (stored_row)
                LOAD_ATTR               59 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               65 (lower + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP

 351   L19:     LOAD_GLOBAL             51 (isinstance + NULL)
                LOAD_FAST               22 (stored_row)
                LOAD_GLOBAL             56 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       25 (to L20)
                NOT_TAKEN
                LOAD_FAST               22 (stored_row)
                LOAD_ATTR               59 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                LOAD_FAST               22 (stored_row)
                JUMP_FORWARD             1 (to L21)

 352   L20:     LOAD_FAST               23 (recomputed_hash)

 350   L21:     STORE_FAST              16 (expected_prev)
                EXTENDED_ARG             1
                JUMP_BACKWARD          457 (to L11)

 307   L22:     END_FOR
                POP_ITER

 355            LOAD_GLOBAL             67 (compute_merkle_root + NULL)
                LOAD_FAST               17 (row_hashes)
                CALL                     1
                STORE_FAST              24 (merkle)

 356            LOAD_FAST               15 (breaks)
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L23)
                NOT_TAKEN
                LOAD_CONST              27 ('ok')
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST              37 ('degraded')
       L24:     STORE_FAST              25 (chain_status)

 358            LOAD_CONST               3 ('status')
                LOAD_CONST              27 ('ok')

 359            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                3 (bid)

 360            LOAD_CONST               6 ('window_hours')
                LOAD_FAST                4 (hours)

 361            LOAD_CONST               7 ('window_start')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                7 (window_start)
                CALL                     1

 362            LOAD_CONST               8 ('window_end')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                6 (window_end)
                CALL                     1

 363            LOAD_CONST               9 ('rows_in_window')
                LOAD_GLOBAL             63 (len + NULL)
                LOAD_FAST               11 (rows)
                CALL                     1

 364            LOAD_CONST              10 ('chain_status')
                LOAD_FAST               25 (chain_status)

 365            LOAD_CONST              12 ('breaks_count')
                LOAD_GLOBAL             63 (len + NULL)
                LOAD_FAST               15 (breaks)
                CALL                     1

 366            LOAD_CONST              13 ('breaks')
                LOAD_FAST               15 (breaks)

 367            LOAD_CONST              14 ('merkle_root')
                LOAD_FAST               24 (merkle)

 368            LOAD_CONST              15 ('warnings')
                BUILD_LIST               0

 369            LOAD_CONST              17 ('error_code')
                LOAD_CONST               1 (None)

 357            BUILD_MAP               12
                RETURN_VALUE

  --   L25:     PUSH_EXC_INFO

 257            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      121 (to L30)
                NOT_TAKEN
                STORE_FAST              12 (e)

 258   L26:     LOAD_GLOBAL             36 (logger)
                LOAD_ATTR               39 (warning + NULL|self)

 259            LOAD_CONST              25 ('verify_window read error type=')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 258            CALL                     1
                POP_TOP

 262            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('skipped')

 263            LOAD_CONST               5 ('brokerage_id')
                LOAD_FAST                3 (bid)

 264            LOAD_CONST               6 ('window_hours')
                LOAD_FAST                4 (hours)

 265            LOAD_CONST               7 ('window_start')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                7 (window_start)
                CALL                     1

 266            LOAD_CONST               8 ('window_end')
                LOAD_GLOBAL             11 (_iso + NULL)
                LOAD_FAST                6 (window_end)
                CALL                     1

 267            LOAD_CONST               9 ('rows_in_window')
                LOAD_SMALL_INT           0

 268            LOAD_CONST              10 ('chain_status')
                LOAD_CONST              11 ('genesis')

 269            LOAD_CONST              12 ('breaks_count')
                LOAD_SMALL_INT           0

 270            LOAD_CONST              13 ('breaks')
                BUILD_LIST               0

 271            LOAD_CONST              14 ('merkle_root')
                LOAD_CONST              38 ('0000000000000000000000000000000000000000000000000000000000000000')

 272            LOAD_CONST              15 ('warnings')
                LOAD_CONST              26 ('db_read_failed:')
                LOAD_GLOBAL             41 (type + NULL)
                LOAD_FAST               12 (e)
                CALL                     1
                LOAD_ATTR               42 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 273            LOAD_CONST              17 ('error_code')
                LOAD_CONST              16 ('audit_store_unavailable')

 261            BUILD_MAP               12
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               1 (None)
                STORE_FAST              12 (e)
                DELETE_FAST             12 (e)
                RERAISE                  1

 257   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L4 to L6 -> L25 [0]
  L7 to L9 -> L25 [0]
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app\services\operator\audit_chain_verifier.py", line 377>:
377           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('window_envelope')

378           LOAD_CONST               2 ('Dict[str, Any]')

377           LOAD_CONST               3 ('generated_by')

380           LOAD_CONST               4 ('Optional[str]')

377           LOAD_CONST               5 ('return')

381           LOAD_CONST               2 ('Dict[str, Any]')

377           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object persist_merkle_root at 0x0000018C17D7DA00, file "app\services\operator\audit_chain_verifier.py", line 377>:
 377            RESUME                   0

 388            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L1)
                NOT_TAKEN

 390            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 391            LOAD_CONST               3 ('error_code')
                LOAD_CONST               4 ('invalid_window_envelope')

 392            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 389            BUILD_MAP                3
                RETURN_VALUE

 394    L1:     LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST               6 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       10 (to L2)
                NOT_TAKEN

 396            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('skipped')

 397            LOAD_CONST               3 ('error_code')
                LOAD_CONST               8 ('window_envelope_not_ok')

 398            LOAD_CONST               5 ('warnings')
                LOAD_CONST               8 ('window_envelope_not_ok')
                BUILD_LIST               1

 395            BUILD_MAP                3
                RETURN_VALUE

 400    L2:     LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               9 ('merkle_root')
                CALL                     1
                STORE_FAST               2 (merkle)

 401            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (merkle)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         2 (merkle)
                CALL                     1
                LOAD_SMALL_INT          64
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE        9 (to L4)
                NOT_TAKEN

 403    L3:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 404            LOAD_CONST               3 ('error_code')
                LOAD_CONST              10 ('invalid_merkle_root_shape')

 405            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 402            BUILD_MAP                3
                RETURN_VALUE

 407    L4:     LOAD_GLOBAL             11 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               3 (db)

 408            LOAD_FAST_BORROW         3 (db)
                POP_JUMP_IF_NOT_NONE    10 (to L5)
                NOT_TAKEN

 410            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('skipped')

 411            LOAD_CONST               5 ('warnings')
                LOAD_CONST              12 ('audit_store_unavailable')
                BUILD_LIST               1

 412            LOAD_CONST               3 ('error_code')
                LOAD_CONST              12 ('audit_store_unavailable')

 409            BUILD_MAP                3
                RETURN_VALUE

 415    L5:     LOAD_CONST              13 ('root_id')
                LOAD_GLOBAL              7 (str + NULL)
                LOAD_GLOBAL             12 (uuid)
                LOAD_ATTR               14 (uuid4)
                PUSH_NULL
                CALL                     0
                CALL                     1

 416            LOAD_CONST              14 ('window_start')
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              14 ('window_start')
                CALL                     1

 417            LOAD_CONST              15 ('window_end')
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              15 ('window_end')
                CALL                     1

 418            LOAD_CONST              16 ('brokerage_id')
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              16 ('brokerage_id')
                CALL                     1

 419            LOAD_CONST               9 ('merkle_root')
                LOAD_FAST                2 (merkle)

 420            LOAD_CONST              17 ('rows_in_window')
                LOAD_GLOBAL             17 (int + NULL)
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              17 ('rows_in_window')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L6)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L6:     CALL                     1

 421            LOAD_CONST              18 ('chain_status')
                LOAD_FAST_BORROW         0 (window_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              18 ('chain_status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               6 ('ok')

 422    L7:     LOAD_CONST              19 ('generated_by')
                LOAD_GLOBAL             19 (_bound_generated_by + NULL)
                LOAD_FAST_BORROW         1 (generated_by)
                CALL                     1

 423            LOAD_CONST              20 ('generated_at')
                LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_GLOBAL             23 (_now_dt + NULL)
                CALL                     0
                CALL                     1

 414            BUILD_MAP                9
                STORE_FAST               4 (row)

 425            NOP

 426    L8:     LOAD_FAST_BORROW         3 (db)
                LOAD_ATTR               25 (table + NULL|self)
                LOAD_GLOBAL             26 (_MERKLE_TABLE)
                CALL                     1
                LOAD_ATTR               29 (insert + NULL|self)
                LOAD_FAST_BORROW         4 (row)
                CALL                     1
                LOAD_ATTR               31 (execute + NULL|self)
                CALL                     0
                STORE_FAST               5 (result)

 427            LOAD_GLOBAL             33 (list + NULL)
                LOAD_GLOBAL             35 (getattr + NULL)
                LOAD_FAST_BORROW         5 (result)
                LOAD_CONST              21 ('data')
                LOAD_CONST              11 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               6 (rows)

 429            LOAD_CONST               1 ('status')
                LOAD_CONST               6 ('ok')

 430            LOAD_CONST              22 ('merkle_row')
                LOAD_FAST_BORROW         6 (rows)
                TO_BOOL
                POP_JUMP_IF_FALSE       10 (to L12)
       L10:     NOT_TAKEN
       L11:     LOAD_FAST_BORROW         6 (rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_FAST                4 (row)

 431   L13:     LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 432            LOAD_CONST               3 ('error_code')
                LOAD_CONST              11 (None)

 428            BUILD_MAP                4
       L14:     RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 434            LOAD_GLOBAL             36 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       85 (to L20)
                NOT_TAKEN
                STORE_FAST               7 (e)

 435   L16:     LOAD_GLOBAL             38 (logger)
                LOAD_ATTR               41 (warning + NULL|self)

 436            LOAD_CONST              23 ('persist_merkle_root db error type=')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 435            CALL                     1
                POP_TOP

 439            LOAD_CONST               1 ('status')
                LOAD_CONST               7 ('skipped')

 440            LOAD_CONST               5 ('warnings')
                LOAD_CONST              24 ('db_write_failed:')
                LOAD_GLOBAL             43 (type + NULL)
                LOAD_FAST                7 (e)
                CALL                     1
                LOAD_ATTR               44 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 441            LOAD_CONST               3 ('error_code')
                LOAD_CONST              12 ('audit_store_unavailable')

 438            BUILD_MAP                3
       L17:     SWAP                     2
       L18:     POP_EXCEPT
                LOAD_CONST              11 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RETURN_VALUE

  --   L19:     LOAD_CONST              11 (None)
                STORE_FAST               7 (e)
                DELETE_FAST              7 (e)
                RERAISE                  1

 434   L20:     RERAISE                  0

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L8 to L10 -> L15 [0]
  L11 to L14 -> L15 [0]
  L15 to L16 -> L21 [1] lasti
  L16 to L17 -> L19 [1] lasti
  L17 to L18 -> L21 [1] lasti
  L19 to L21 -> L21 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\operator\audit_chain_verifier.py", line 449>:
449           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('verification_envelope')

450           LOAD_CONST               2 ('Dict[str, Any]')

449           LOAD_CONST               3 ('webhook_url')

452           LOAD_CONST               4 ('Optional[str]')

449           LOAD_CONST               5 ('brokerage')

453           LOAD_CONST               6 ('Any')

449           LOAD_CONST               7 ('include_metadata')

454           LOAD_CONST               8 ('bool')

449           LOAD_CONST               9 ('return')

455           LOAD_CONST               2 ('Dict[str, Any]')

449           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object emit_chain_break_alert at 0x0000018C17EF9A30, file "app\services\operator\audit_chain_verifier.py", line 449>:
 449            RESUME                   0

 469            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (verification_envelope)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         9 (to L1)
                NOT_TAKEN

 471            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 472            LOAD_CONST               3 ('warnings')
                BUILD_LIST               0

 473            LOAD_CONST               4 ('error_code')
                LOAD_CONST               5 ('invalid_verification_envelope')

 470            BUILD_MAP                3
                RETURN_VALUE

 475    L1:     LOAD_FAST_BORROW         0 (verification_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               6 ('chain_status')
                CALL                     1
                LOAD_CONST               7 ('degraded')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       10 (to L2)
                NOT_TAKEN

 477            LOAD_CONST               1 ('status')
                LOAD_CONST               8 ('skipped')

 478            LOAD_CONST               3 ('warnings')
                LOAD_CONST               9 ('chain_intact')
                BUILD_LIST               1

 479            LOAD_CONST               4 ('error_code')
                LOAD_CONST               9 ('chain_intact')

 476            BUILD_MAP                3
                RETURN_VALUE

 481    L2:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_FAST_BORROW         0 (verification_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              10 ('breaks_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L3:     CALL                     1
                STORE_FAST               4 (breaks_count)

 482            LOAD_FAST_BORROW         0 (verification_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              11 ('window_start')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              12 ('')
        L4:     STORE_FAST               5 (window_start)

 483            LOAD_FAST_BORROW         0 (verification_envelope)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                CALL                     1
                STORE_FAST               6 (bid)

 487            NOP

 488    L5:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              9 (_now_dt + NULL)
                CALL                     0
                LOAD_ATTR               11 (timestamp + NULL|self)
                CALL                     0
                CALL                     1
                STORE_FAST               7 (ts)

 489            LOAD_CONST              14 ('audit.chain.broken:')
                LOAD_FAST                6 (bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L8)
        L6:     NOT_TAKEN
        L7:     POP_TOP
                LOAD_CONST              15 ('global')
        L8:     FORMAT_SIMPLE
                LOAD_CONST              16 (':')
                LOAD_FAST_BORROW         7 (ts)
                FORMAT_SIMPLE
                BUILD_STRING             4
                STORE_FAST               8 (alert_id)

 490            LOAD_SMALL_INT           0
                LOAD_CONST              17 (('Alert',))
                IMPORT_NAME              6 (app.services.monitoring.contracts)
                IMPORT_FROM              7 (Alert)
                STORE_FAST               9 (Alert)
                POP_TOP

 491            LOAD_FAST                9 (Alert)
                PUSH_NULL

 492            LOAD_FAST                8 (alert_id)

 493            LOAD_CONST              18 ('INTEGRITY')

 494            LOAD_CONST              19 ('HIGH')

 495            LOAD_CONST              20 ('PAS operator audit chain integrity break detected')

 497            LOAD_CONST              21 ('Verification of the operator audit chain detected ')

 498            LOAD_FAST_BORROW         4 (breaks_count)
                FORMAT_SIMPLE
                LOAD_CONST              22 (' break(s) in window starting ')

 499            LOAD_FAST_BORROW         5 (window_start)
                FORMAT_SIMPLE
                LOAD_CONST              23 ('. Operator must investigate. No autonomous remediation has been performed.')

 497            BUILD_STRING             5

 502            LOAD_CONST              24 ('app.services.operator.audit_chain_verifier')

 503            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (bid)
                LOAD_GLOBAL             16 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L9)
                NOT_TAKEN
                LOAD_FAST                6 (bid)
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              25 (None)

 505   L10:     LOAD_CONST              26 ('warning_count')
                LOAD_FAST_BORROW         4 (breaks_count)

 506            LOAD_CONST               4 ('error_code')
                LOAD_CONST              27 ('audit_chain_broken')

 507            LOAD_CONST              28 ('severity')
                LOAD_CONST              19 ('HIGH')

 504            BUILD_MAP                3

 491            LOAD_CONST              29 (('id', 'category', 'severity', 'title', 'description', 'source', 'affected_brokerage', 'metadata'))
                CALL_KW                  8
                STORE_FAST              10 (alert)

 510            LOAD_SMALL_INT           0
                LOAD_CONST              30 (('send_pilot_alert_to_slack',))
                IMPORT_NAME              9 (app.services.monitoring.slack_alert_transport)
                IMPORT_FROM             10 (send_pilot_alert_to_slack)
                STORE_FAST              11 (send_pilot_alert_to_slack)
                POP_TOP

 513            LOAD_FAST_BORROW        11 (send_pilot_alert_to_slack)
                PUSH_NULL

 514            LOAD_FAST_BORROW        10 (alert)

 515            LOAD_FAST_BORROW         1 (webhook_url)

 516            LOAD_FAST_BORROW         2 (brokerage)

 517            LOAD_FAST_BORROW         3 (include_metadata)

 513            LOAD_CONST              31 (('webhook_url', 'brokerage', 'include_metadata'))
                CALL_KW                  4
                STORE_FAST              12 (env)

 519            LOAD_FAST_BORROW        12 (env)
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 520            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      107 (to L17)
                NOT_TAKEN
                STORE_FAST              13 (e)

 521   L13:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 522            LOAD_CONST              32 ('emit_chain_break_alert unexpected error type=')

 523            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 522            BUILD_STRING             2

 521            CALL                     1
                POP_TOP

 526            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 527            LOAD_CONST               3 ('warnings')
                LOAD_CONST              33 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 528            LOAD_CONST               4 ('error_code')
                LOAD_CONST              33 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST               13 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 525            BUILD_MAP                3
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST              25 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST              25 (None)
                STORE_FAST              13 (e)
                DELETE_FAST             13 (e)
                RERAISE                  1

 520   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L5 to L6 -> L12 [0]
  L7 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
