# operator/merkle_inclusion_proofs

- **pyc:** `app\services\operator\__pycache__\merkle_inclusion_proofs.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/merkle_inclusion_proofs.py`
- **co_filename (from bytecode):** `app\services\operator\merkle_inclusion_proofs.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS177 — Merkle inclusion proof generation + verification.

Deterministic, read-only proof surface that lets tenants
independently verify that a specific audit row was included
in a published Merkle root.

The proof shape:

    {
      "leaf_hash":         "<sha256 hex>",
      "merkle_root":       "<sha256 hex>",
      "proof":             [<step>, ...],
      "leaf_index":        int,
      "leaf_count":        int,
      "deterministic":     True,
    }

Each ``step`` is::

    {"sibling": "<sha256 hex>", "direction": "left" | "right"}

``direction`` is the side the *sibling* sits on relative to
the current node as the proof walks the tree upward. Verifier
hashes ``left || right`` at each step, where the current
running hash takes whichever side ``direction`` points away
from.

Doctrine:

* **Deterministic.** Mirrors `audit_chain_verifier.compute_merkle_root`
  exactly. Odd leaves are hashed with themselves at each
  level. Internal nodes are ``sha256(left || right)`` over
  lower-cased hex concatenation.
* **Read-only.** No DB writes. The DB-touching helper
  ``proof_for_audit_entry`` does only SELECTs.
* **No PII.** The proof carries only sha256 hex digests +
  structural integer indices. NEVER carries action_id /
  brokerage_id / metadata / raw payload.
* **NEVER raises.** Malformed proofs fail closed (return
  ``valid=False``); DB unavailable returns
  ``status="skipped"``.
* **Self-contained verification.** ``verify_inclusion_proof``
  takes the proof + the leaf_hash + the expected merkle_root
  and returns a structural envelope. Verifier does not
  consult the DB.

Public surface:

  * ``build_merkle_tree(leaves)`` — list of layers.
  * ``generate_inclusion_proof(leaves, leaf_index)`` — proof envelope.
  * ``verify_inclusion_proof(proof_envelope)`` — boolean + structural.
  * ``proof_for_audit_entry(brokerage_id, audit_entry_id, merkle_root_id=None)`` — DB-aware helper.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `__future__`, `annotations`, `app.db.supabase_client`, `get_supabase`, `hashlib`, `logging`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_failed_proof`, `_failed_verification`, `_get_db_safe`, `_hash_pair`, `_is_sha256_hex`, `build_merkle_tree`, `generate_inclusion_proof`, `proof_for_audit_entry`, `verify_inclusion_proof`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS177 — Merkle inclusion proof generation + verification.\n\nDeterministic, read-only proof surface that lets tenants\nindependently verify that a specific audit row was included\nin a published Merkle root.\n\nThe proof shape:\n\n    {\n      "leaf_hash":         "<sha256 hex>",\n      "merkle_root":       "<sha256 hex>",\n      "proof":             [<step>, ...],\n      "leaf_index":        int,\n      "leaf_count":        int,\n      "deterministic":     True,\n    }\n\nEach ``step`` is::\n\n    {"sibling": "<sha256 hex>", "direction": "left" | "right"}\n\n``direction`` is the side the *sibling* sits on relative to\nthe current node as the proof walks the tree upward. Verifier\nhashes ``left || right`` at each step, where the current\nrunning hash takes whichever side ``direction`` points away\nfrom.\n\nDoctrine:\n\n* **Deterministic.** Mirrors `audit_chain_verifier.compute_merkle_root`\n  exactly. Odd leaves are hashed with themselves at each\n  level. Internal nodes are ``sha256(left || right)`` over\n  lower-cased hex concatenation.\n* **Read-only.** No DB writes. The DB-touching helper\n  ``proof_for_audit_entry`` does only SELECTs.\n* **No PII.** The proof carries only sha256 hex digests +\n  structural integer indices. NEVER carries action_id /\n  brokerage_id / metadata / raw payload.\n* **NEVER raises.** Malformed proofs fail closed (return\n  ``valid=False``); DB unavailable returns\n  ``status="skipped"``.\n* **Self-contained verification.** ``verify_inclusion_proof``\n  takes the proof + the leaf_hash + the expected merkle_root\n  and returns a structural envelope. Verifier does not\n  consult the DB.\n\nPublic surface:\n\n  * ``build_merkle_tree(leaves)`` — list of layers.\n  * ``generate_inclusion_proof(leaves, leaf_index)`` — proof envelope.\n  * ``verify_inclusion_proof(proof_envelope)`` — boolean + structural.\n  * ``proof_for_audit_entry(brokerage_id, audit_entry_id, merkle_root_id=None)`` — DB-aware helper.\n'
- 'pas.operator.merkle_inclusion_proofs'
- 'pas_operator_actions_log'
- 'pas_audit_merkle_roots'
- 'merkle_root_id'
- 'value'
- 'Any'
- 'return'
- 'bool'
- '0123456789abcdef'
- 'left'
- 'str'
- 'right'
- 'sha256 over lower-cased hex concatenation. NEVER raises.'
- 'utf-8'
- '_hash_pair unexpected error type='
- 🔒 '<REDACTED:secret-like value, len=64>'
- 'leaves'
- 'Dict[str, Any]'
- 'Build a deterministic binary Merkle tree from a list of\nsha256-hex leaves. Returns a structural envelope with one\nentry per layer (root first).\n\nReturns::\n\n    {\n      "status":    "ok" | "failed",\n      "layers":    [[<hash>, ...], ...],\n      "leaf_count": int,\n      "root":      "<sha256 hex>" | "0" * 64,\n      "error_code": None | "<structural>",\n    }\n\nNEVER raises. NEVER returns PII (leaves are sha256 hex\ndigests already).\n'
- 'status'
- 'failed'
- 'layers'
- 'leaf_count'
- 'root'
- 'error_code'
- 'leaves_not_list'
- 'leaf_index'
- 'Generate the structural inclusion proof for the leaf at\n``leaf_index`` in ``leaves``. Returns the proof envelope.\n\nNEVER raises. NEVER returns PII.\n'
- 'invalid_leaf_index'
- 'tree_build_failed'
- 'empty_leaves'
- 'leaf_index_out_of_range'
- 'sibling'
- 'direction'
- 'leaf_hash'
- 'merkle_root'
- 'proof'
- 'deterministic'
- 'warnings'
- 'proof_envelope'
- 'Verify a structural inclusion proof. Returns a\ndeterministic verdict envelope.\n\nReturns::\n\n    {\n      "status":     "ok" | "failed",\n      "valid":      bool,\n      "warnings":   [<structural>],\n      "error_code": None | "<structural>",\n    }\n\nNEVER raises. Malformed proofs fail closed\n(``valid=False``).\n'
- 'invalid_envelope_shape'
- 'invalid_leaf_hash'
- 'invalid_merkle_root'
- 'invalid_proof_list'
- 'malformed_proof_step'
- 'invalid_sibling_hash'
- 'invalid_direction'
- 'valid'
- 'proof_does_not_match_root'
- 'merkle_inclusion_proofs db client unavailable type='
- 'max_len'
- 'int'
- 'Optional[str]'
- 'brokerage_id'
- 'audit_entry_id'
- 'DB-aware: locate the audit row by ``audit_entry_id``,\nlocate the most-recent Merkle root window that includes\nits ``occurred_at`` (or the explicit ``merkle_root_id``\nwhen supplied), build the proof, and return a structural\nenvelope.\n\nNEVER raises. NEVER returns PII.\n'
- 'missing_brokerage_id'
- 'missing_audit_entry_id'
- 'skipped'
- 'audit_store_unavailable'
- 'action_id, occurred_at, brokerage_id, row_hash'
- 'action_id'
- 'data'
- 'proof_for_audit_entry audit read error type='
- 'db_read_failed:'
- 'audit_entry_not_found_or_cross_brokerage'
- 'row_hash'
- 'occurred_at'
- 'audit_entry_missing_row_hash'
- 'audit_entry_missing_occurred_at'
- 'root_id, window_start, window_end, merkle_root, brokerage_id, rows_in_window'
- 'root_id'
- 'window_start'
- 'window_end'
- 'proof_for_audit_entry merkle read error type='
- 'merkle_root_window_not_found'
- 'merkle_window_malformed'
- 'action_id, row_hash, occurred_at'
- 'proof_for_audit_entry window read error type='
- 'audit_entry_outside_window'
- 'proof_generation_failed'
- 'persisted_merkle_root_malformed'
- 'computed_root_does_not_match_persisted'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS177 — Merkle inclusion proof generation + verification.\n\nDeterministic, read-only proof surface that lets tenants\nindependently verify that a specific audit row was included\nin a published Merkle root.\n\nThe proof shape:\n\n    {\n      "leaf_hash":         "<sha256 hex>",\n      "merkle_root":       "<sha256 hex>",\n      "proof":             [<step>, ...],\n      "leaf_index":        int,\n      "leaf_count":        int,\n      "deterministic":     True,\n    }\n\nEach ``step`` is::\n\n    {"sibling": "<sha256 hex>", "direction": "left" | "right"}\n\n``direction`` is the side the *sibling* sits on relative to\nthe current node as the proof walks the tree upward. Verifier\nhashes ``left || right`` at each step, where the current\nrunning hash takes whichever side ``direction`` points away\nfrom.\n\nDoctrine:\n\n* **Deterministic.** Mirrors `audit_chain_verifier.compute_merkle_root`\n  exactly. Odd leaves are hashed with themselves at each\n  level. Internal nodes are ``sha256(left || right)`` over\n  lower-cased hex concatenation.\n* **Read-only.** No DB writes. The DB-touching helper\n  ``proof_for_audit_entry`` does only SELECTs.\n* **No PII.** The proof carries only sha256 hex digests +\n  structural integer indices. NEVER carries action_id /\n  brokerage_id / metadata / raw payload.\n* **NEVER raises.** Malformed proofs fail closed (return\n  ``valid=False``); DB unavailable returns\n  ``status="skipped"``.\n* **Self-contained verification.** ``verify_inclusion_proof``\n  takes the proof + the leaf_hash + the expected merkle_root\n  and returns a structural envelope. Verifier does not\n  consult the DB.\n\nPublic surface:\n\n  * ``build_merkle_tree(leaves)`` — list of layers.\n  * ``generate_inclusion_proof(leaves, leaf_index)`` — proof envelope.\n  * ``verify_inclusion_proof(proof_envelope)`` — boolean + structural.\n  * ``proof_for_audit_entry(brokerage_id, audit_entry_id, merkle_root_id=None)`` — DB-aware helper.\n')
              STORE_NAME               0 (__doc__)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 58           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (hashlib)
              STORE_NAME               3 (hashlib)

 59           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (logging)
              STORE_NAME               4 (logging)

 60           LOAD_SMALL_INT           0
              LOAD_CONST               3 (('Any', 'Dict', 'List', 'Optional'))
              IMPORT_NAME              5 (typing)
              IMPORT_FROM              6 (Any)
              STORE_NAME               6 (Any)
              IMPORT_FROM              7 (Dict)
              STORE_NAME               7 (Dict)
              IMPORT_FROM              8 (List)
              STORE_NAME               8 (List)
              IMPORT_FROM              9 (Optional)
              STORE_NAME               9 (Optional)
              POP_TOP

 63           LOAD_NAME                4 (logging)
              LOAD_ATTR               20 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.operator.merkle_inclusion_proofs')
              CALL                     1
              STORE_NAME              11 (logger)

 66           LOAD_CONST               5 ('pas_operator_actions_log')
              STORE_NAME              12 (_AUDIT_TABLE)

 67           LOAD_CONST               6 ('pas_audit_merkle_roots')
              STORE_NAME              13 (_MERKLE_TABLE)

 74           LOAD_CONST               7 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\merkle_inclusion_proofs.py", line 74>)
              MAKE_FUNCTION
              LOAD_CONST               8 (<code object _is_sha256_hex at 0x0000018C1794ED80, file "app\services\operator\merkle_inclusion_proofs.py", line 74>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              14 (_is_sha256_hex)

 83           LOAD_CONST               9 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\merkle_inclusion_proofs.py", line 83>)
              MAKE_FUNCTION
              LOAD_CONST              10 (<code object _hash_pair at 0x0000018C1794E9E0, file "app\services\operator\merkle_inclusion_proofs.py", line 83>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              15 (_hash_pair)

 98           LOAD_CONST              11 (<code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\merkle_inclusion_proofs.py", line 98>)
              MAKE_FUNCTION
              LOAD_CONST              12 (<code object build_merkle_tree at 0x0000018C17E955C0, file "app\services\operator\merkle_inclusion_proofs.py", line 98>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              16 (build_merkle_tree)

155           LOAD_CONST              13 (<code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\merkle_inclusion_proofs.py", line 155>)
              MAKE_FUNCTION
              LOAD_CONST              14 (<code object generate_inclusion_proof at 0x0000018C17D78310, file "app\services\operator\merkle_inclusion_proofs.py", line 155>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              17 (generate_inclusion_proof)

210           LOAD_CONST              15 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\merkle_inclusion_proofs.py", line 210>)
              MAKE_FUNCTION
              LOAD_CONST              16 (<code object verify_inclusion_proof at 0x0000018C1778AA50, file "app\services\operator\merkle_inclusion_proofs.py", line 210>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              18 (verify_inclusion_proof)

261           LOAD_CONST              17 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\merkle_inclusion_proofs.py", line 261>)
              MAKE_FUNCTION
              LOAD_CONST              18 (<code object _failed_proof at 0x0000018C18025030, file "app\services\operator\merkle_inclusion_proofs.py", line 261>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              19 (_failed_proof)

275           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\merkle_inclusion_proofs.py", line 275>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _failed_verification at 0x0000018C17FA2B50, file "app\services\operator\merkle_inclusion_proofs.py", line 275>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              20 (_failed_verification)

288           LOAD_CONST              21 (<code object _get_db_safe at 0x0000018C17FF13B0, file "app\services\operator\merkle_inclusion_proofs.py", line 288>)
              MAKE_FUNCTION
              STORE_NAME              21 (_get_db_safe)

300           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18026130, file "app\services\operator\merkle_inclusion_proofs.py", line 300>)
              MAKE_FUNCTION
              LOAD_CONST              23 (<code object _bound_str at 0x0000018C17972550, file "app\services\operator\merkle_inclusion_proofs.py", line 300>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              22 (_bound_str)

309           LOAD_CONST              24 ('merkle_root_id')

313           LOAD_CONST               2 (None)

309           BUILD_MAP                1
              LOAD_CONST              25 (<code object __annotate__ at 0x0000018C18026230, file "app\services\operator\merkle_inclusion_proofs.py", line 309>)
              MAKE_FUNCTION
              LOAD_CONST              26 (<code object proof_for_audit_entry at 0x0000018C181A10A0, file "app\services\operator\merkle_inclusion_proofs.py", line 309>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              23 (proof_for_audit_entry)

539           BUILD_LIST               0
              LOAD_CONST              27 (('build_merkle_tree', 'generate_inclusion_proof', 'verify_inclusion_proof', 'proof_for_audit_entry'))
              LIST_EXTEND              1
              STORE_NAME              24 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\merkle_inclusion_proofs.py", line 74>:
 74           RESUME                   0
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
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _is_sha256_hex at 0x0000018C1794ED80, file "app\services\operator\merkle_inclusion_proofs.py", line 74>:
 74           RESUME                   0

 75           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 76           LOAD_CONST               0 (False)
              RETURN_VALUE

 77   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               1 (s)

 78           LOAD_GLOBAL              9 (len + NULL)
              LOAD_FAST_BORROW         1 (s)
              CALL                     1
              LOAD_SMALL_INT          64
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

 79           LOAD_CONST               0 (False)
              RETURN_VALUE

 80   L2:     LOAD_GLOBAL             10 (all)
              COPY                     1
              LOAD_COMMON_CONSTANT     3 (<built-in function all>)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE       28 (to L6)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025530, file "app\services\operator\merkle_inclusion_proofs.py", line 80>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
      L3:     FOR_ITER                12 (to L5)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           11 (to L3)
      L4:     POP_ITER
              LOAD_CONST               0 (False)
              RETURN_VALUE
      L5:     END_FOR
              POP_ITER
              LOAD_CONST               2 (True)
              RETURN_VALUE
      L6:     PUSH_NULL
              LOAD_CONST               1 (<code object <genexpr> at 0x0000018C18025530, file "app\services\operator\merkle_inclusion_proofs.py", line 80>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (s)
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C18025530, file "app\services\operator\merkle_inclusion_proofs.py", line 80>:
  80           RETURN_GENERATOR
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

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\merkle_inclusion_proofs.py", line 83>:
 83           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('left')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('right')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _hash_pair at 0x0000018C1794E9E0, file "app\services\operator\merkle_inclusion_proofs.py", line 83>:
  83           RESUME                   0

  85           NOP

  86   L1:     LOAD_GLOBAL              0 (hashlib)
               LOAD_ATTR                2 (sha256)
               PUSH_NULL
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (left, right)
               BINARY_OP                0 (+)
               LOAD_ATTR                5 (encode + NULL|self)
               LOAD_CONST               1 ('utf-8')
               CALL                     1
               CALL                     1
               LOAD_ATTR                7 (hexdigest + NULL|self)
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

  87           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       56 (to L8)
               NOT_TAKEN
               STORE_FAST               2 (e)

  88   L4:     LOAD_GLOBAL             10 (logger)
               LOAD_ATTR               13 (warning + NULL|self)

  89           LOAD_CONST               2 ('_hash_pair unexpected error type=')
               LOAD_GLOBAL             15 (type + NULL)
               LOAD_FAST                2 (e)
               CALL                     1
               LOAD_ATTR               16 (__name__)
               FORMAT_SIMPLE
               BUILD_STRING             2

  88           CALL                     1
               POP_TOP

  91           LOAD_CONST               4 ('0000000000000000000000000000000000000000000000000000000000000000')
       L5:     SWAP                     2
       L6:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RETURN_VALUE

  --   L7:     LOAD_CONST               3 (None)
               STORE_FAST               2 (e)
               DELETE_FAST              2 (e)
               RERAISE                  1

  87   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L9 [1] lasti
  L4 to L5 -> L7 [1] lasti
  L5 to L6 -> L9 [1] lasti
  L7 to L9 -> L9 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "app\services\operator\merkle_inclusion_proofs.py", line 98>:
 98           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('leaves')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object build_merkle_tree at 0x0000018C17E955C0, file "app\services\operator\merkle_inclusion_proofs.py", line 98>:
  98            RESUME                   0

 116            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (leaves)
                LOAD_GLOBAL              2 (list)
                LOAD_GLOBAL              4 (tuple)
                BUILD_TUPLE              2
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L1)
                NOT_TAKEN

 118            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 119            LOAD_CONST               3 ('layers')
                BUILD_LIST               0

 120            LOAD_CONST               4 ('leaf_count')
                LOAD_SMALL_INT           0

 121            LOAD_CONST               5 ('root')
                LOAD_CONST              10 ('0000000000000000000000000000000000000000000000000000000000000000')

 122            LOAD_CONST               6 ('error_code')
                LOAD_CONST               7 ('leaves_not_list')

 117            BUILD_MAP                5
                RETURN_VALUE

 125    L1:     LOAD_FAST_BORROW         0 (leaves)
                GET_ITER

 124            LOAD_FAST_AND_CLEAR      1 (leaf)
                SWAP                     2
        L2:     BUILD_LIST               0
                SWAP                     2

 125    L3:     FOR_ITER                52 (to L6)
                STORE_FAST               1 (leaf)
                LOAD_GLOBAL              7 (_is_sha256_hex + NULL)
                LOAD_FAST_BORROW         1 (leaf)
                CALL                     1
                TO_BOOL
        L4:     POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                JUMP_BACKWARD           22 (to L3)
        L5:     LOAD_FAST_BORROW         1 (leaf)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (lower + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           54 (to L3)
        L6:     END_FOR
                POP_ITER

 124    L7:     STORE_FAST               2 (clean_leaves)
                STORE_FAST               1 (leaf)

 127            LOAD_FAST_BORROW         2 (clean_leaves)
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L8)
                NOT_TAKEN

 129            LOAD_CONST               1 ('status')
                LOAD_CONST               8 ('ok')

 130            LOAD_CONST               3 ('layers')
                BUILD_LIST               0

 131            LOAD_CONST               4 ('leaf_count')
                LOAD_SMALL_INT           0

 132            LOAD_CONST               5 ('root')
                LOAD_CONST              10 ('0000000000000000000000000000000000000000000000000000000000000000')

 133            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 (None)

 128            BUILD_MAP                5
                RETURN_VALUE

 135    L8:     LOAD_GLOBAL              3 (list + NULL)
                LOAD_FAST_BORROW         2 (clean_leaves)
                CALL                     1
                BUILD_LIST               1
                STORE_FAST               3 (layers)

 136    L9:     LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         3 (layers)
                LOAD_CONST              11 (-1)
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE      134 (to L14)
                NOT_TAKEN

 137            LOAD_FAST_BORROW         3 (layers)
                LOAD_CONST              11 (-1)
                BINARY_OP               26 ([])
                STORE_FAST               4 (layer)

 138            BUILD_LIST               0
                STORE_FAST               5 (next_layer)

 139            LOAD_SMALL_INT           0
                STORE_FAST               6 (i)

 140   L10:     LOAD_FAST_BORROW         6 (i)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (layer)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       86 (to L13)
                NOT_TAKEN

 141            LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (layer, i)
                BINARY_OP               26 ([])
                STORE_FAST               7 (left)

 142            LOAD_FAST_BORROW         6 (i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (layer)
                CALL                     1
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       16 (to L11)
                NOT_TAKEN
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (layer, i)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                BINARY_OP               26 ([])
                JUMP_FORWARD             1 (to L12)
       L11:     LOAD_FAST                7 (left)
       L12:     STORE_FAST               8 (right)

 143            LOAD_FAST_BORROW         5 (next_layer)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_GLOBAL             17 (_hash_pair + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (left, right)
                CALL                     2
                CALL                     1
                POP_TOP

 144            LOAD_FAST_BORROW         6 (i)
                LOAD_SMALL_INT           2
                BINARY_OP               13 (+=)
                STORE_FAST               6 (i)
                JUMP_BACKWARD          101 (to L10)

 145   L13:     LOAD_FAST_BORROW         3 (layers)
                LOAD_ATTR               15 (append + NULL|self)
                LOAD_FAST_BORROW         5 (next_layer)
                CALL                     1
                POP_TOP
                JUMP_BACKWARD          156 (to L9)

 147   L14:     LOAD_CONST               1 ('status')
                LOAD_CONST               8 ('ok')

 148            LOAD_CONST               3 ('layers')
                LOAD_FAST_BORROW         3 (layers)

 149            LOAD_CONST               4 ('leaf_count')
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         2 (clean_leaves)
                CALL                     1

 150            LOAD_CONST               5 ('root')
                LOAD_FAST_BORROW         3 (layers)
                LOAD_CONST              11 (-1)
                BINARY_OP               26 ([])
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])

 151            LOAD_CONST               6 ('error_code')
                LOAD_CONST               9 (None)

 146            BUILD_MAP                5
                RETURN_VALUE

  --   L15:     SWAP                     2
                POP_TOP

 124            SWAP                     2
                STORE_FAST               1 (leaf)
                RERAISE                  0
ExceptionTable:
  L2 to L4 -> L15 [2]
  L5 to L7 -> L15 [2]

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\merkle_inclusion_proofs.py", line 155>:
155           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('leaves')

156           LOAD_CONST               2 ('Any')

155           LOAD_CONST               3 ('leaf_index')

157           LOAD_CONST               2 ('Any')

155           LOAD_CONST               4 ('return')

158           LOAD_CONST               5 ('Dict[str, Any]')

155           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object generate_inclusion_proof at 0x0000018C17D78310, file "app\services\operator\merkle_inclusion_proofs.py", line 155>:
 155            RESUME                   0

 164            NOP

 165    L1:     LOAD_GLOBAL              1 (int + NULL)
                LOAD_FAST_BORROW         1 (leaf_index)
                CALL                     1
                STORE_FAST               2 (idx)

 168    L2:     LOAD_GLOBAL              9 (build_merkle_tree + NULL)
                LOAD_FAST                0 (leaves)
                CALL                     1
                STORE_FAST               3 (tree)

 169            LOAD_FAST                3 (tree)
                LOAD_CONST               2 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               3 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       37 (to L4)
                NOT_TAKEN

 170            LOAD_GLOBAL              7 (_failed_proof + NULL)
                LOAD_FAST                3 (tree)
                LOAD_ATTR               11 (get + NULL|self)
                LOAD_CONST               4 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L3)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST               5 ('tree_build_failed')
        L3:     CALL                     1
                RETURN_VALUE

 171    L4:     LOAD_FAST                3 (tree)
                LOAD_CONST               6 ('leaf_count')
                BINARY_OP               26 ([])
                STORE_FAST               4 (leaf_count)

 172            LOAD_FAST                4 (leaf_count)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       12 (to L5)
                NOT_TAKEN

 173            LOAD_GLOBAL              7 (_failed_proof + NULL)
                LOAD_CONST               7 ('empty_leaves')
                CALL                     1
                RETURN_VALUE

 174    L5:     LOAD_FAST                2 (idx)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_TRUE         7 (to L6)
                NOT_TAKEN
                LOAD_FAST_LOAD_FAST     36 (idx, leaf_count)
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       12 (to L7)
                NOT_TAKEN

 175    L6:     LOAD_GLOBAL              7 (_failed_proof + NULL)
                LOAD_CONST               8 ('leaf_index_out_of_range')
                CALL                     1
                RETURN_VALUE

 176    L7:     LOAD_FAST                3 (tree)
                LOAD_CONST               9 ('layers')
                BINARY_OP               26 ([])
                STORE_FAST               5 (layers)

 177            BUILD_LIST               0
                STORE_FAST               6 (proof_steps)

 178            LOAD_FAST                2 (idx)
                STORE_FAST               7 (cur_idx)

 179            LOAD_FAST                5 (layers)
                LOAD_CONST              10 (None)
                LOAD_CONST              23 (-1)
                BINARY_SLICE
                GET_ITER
        L8:     FOR_ITER               105 (to L13)
                STORE_FAST               8 (layer)

 180            LOAD_FAST                7 (cur_idx)
                LOAD_SMALL_INT           2
                BINARY_OP                6 (%)
                LOAD_SMALL_INT           0
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_FALSE       13 (to L9)
                NOT_TAKEN

 181            LOAD_FAST                7 (cur_idx)
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                STORE_FAST               9 (sibling_idx)

 182            LOAD_CONST              11 ('right')
                STORE_FAST              10 (direction)
                JUMP_FORWARD            11 (to L10)

 184    L9:     LOAD_FAST                7 (cur_idx)
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                STORE_FAST               9 (sibling_idx)

 185            LOAD_CONST              12 ('left')
                STORE_FAST              10 (direction)

 186   L10:     LOAD_FAST                9 (sibling_idx)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST                8 (layer)
                CALL                     1
                COMPARE_OP             188 (bool(>=))
                POP_JUMP_IF_FALSE       12 (to L11)
                NOT_TAKEN

 188            LOAD_FAST_LOAD_FAST    135 (layer, cur_idx)
                BINARY_OP               26 ([])
                STORE_FAST              11 (sibling_hash)

 189            LOAD_CONST              11 ('right')
                STORE_FAST              10 (direction)
                JUMP_FORWARD             8 (to L12)

 191   L11:     LOAD_FAST_LOAD_FAST    137 (layer, sibling_idx)
                BINARY_OP               26 ([])
                STORE_FAST              11 (sibling_hash)

 192   L12:     LOAD_FAST                6 (proof_steps)
                LOAD_ATTR               15 (append + NULL|self)

 193            LOAD_CONST              13 ('sibling')
                LOAD_FAST               11 (sibling_hash)

 194            LOAD_CONST              14 ('direction')
                LOAD_FAST               10 (direction)

 192            BUILD_MAP                2
                CALL                     1
                POP_TOP

 196            LOAD_FAST                7 (cur_idx)
                LOAD_SMALL_INT           2
                BINARY_OP               15 (//=)
                STORE_FAST               7 (cur_idx)
                JUMP_BACKWARD          107 (to L8)

 179   L13:     END_FOR
                POP_ITER

 198            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('ok')

 199            LOAD_CONST              15 ('leaf_hash')
                LOAD_FAST                5 (layers)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                LOAD_FAST                2 (idx)
                BINARY_OP               26 ([])

 200            LOAD_CONST              16 ('merkle_root')
                LOAD_FAST                3 (tree)
                LOAD_CONST              17 ('root')
                BINARY_OP               26 ([])

 201            LOAD_CONST              18 ('proof')
                LOAD_FAST                6 (proof_steps)

 202            LOAD_CONST              19 ('leaf_index')
                LOAD_FAST                2 (idx)

 203            LOAD_CONST               6 ('leaf_count')
                LOAD_FAST                4 (leaf_count)

 204            LOAD_CONST              20 ('deterministic')
                LOAD_CONST              21 (True)

 205            LOAD_CONST              22 ('warnings')
                BUILD_LIST               0

 206            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 (None)

 197            BUILD_MAP                9
                RETURN_VALUE

  --   L14:     PUSH_EXC_INFO

 166            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       15 (to L16)
                NOT_TAKEN
                POP_TOP

 167            LOAD_GLOBAL              7 (_failed_proof + NULL)
                LOAD_CONST               1 ('invalid_leaf_index')
                CALL                     1
                SWAP                     2
       L15:     POP_EXCEPT
                RETURN_VALUE

 166   L16:     RERAISE                  0

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L14 [0]
  L14 to L15 -> L17 [1] lasti
  L16 to L17 -> L17 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\merkle_inclusion_proofs.py", line 210>:
210           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('proof_envelope')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object verify_inclusion_proof at 0x0000018C1778AA50, file "app\services\operator\merkle_inclusion_proofs.py", line 210>:
210            RESUME                   0

226            BUILD_LIST               0
               STORE_FAST               1 (warnings)

227            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         0 (proof_envelope)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L1)
               NOT_TAKEN

228            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST               1 ('invalid_envelope_shape')
               CALL                     1
               RETURN_VALUE

229    L1:     LOAD_FAST_BORROW         0 (proof_envelope)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               2 ('leaf_hash')
               CALL                     1
               STORE_FAST               2 (leaf_hash)

230            LOAD_FAST_BORROW         0 (proof_envelope)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               3 ('merkle_root')
               CALL                     1
               STORE_FAST               3 (merkle_root)

231            LOAD_FAST_BORROW         0 (proof_envelope)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               4 ('proof')
               CALL                     1
               STORE_FAST               4 (proof)

232            LOAD_GLOBAL              9 (_is_sha256_hex + NULL)
               LOAD_FAST_BORROW         2 (leaf_hash)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L2)
               NOT_TAKEN

233            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST               5 ('invalid_leaf_hash')
               CALL                     1
               RETURN_VALUE

234    L2:     LOAD_GLOBAL              9 (_is_sha256_hex + NULL)
               LOAD_FAST_BORROW         3 (merkle_root)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L3)
               NOT_TAKEN

235            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST               6 ('invalid_merkle_root')
               CALL                     1
               RETURN_VALUE

236    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         4 (proof)
               LOAD_GLOBAL             10 (list)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        12 (to L4)
               NOT_TAKEN

237            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST               7 ('invalid_proof_list')
               CALL                     1
               RETURN_VALUE

238    L4:     LOAD_FAST_BORROW         2 (leaf_hash)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               STORE_FAST               5 (cur)

239            LOAD_FAST_BORROW         4 (proof)
               GET_ITER
       L5:     FOR_ITER               210 (to L10)
               STORE_FAST               6 (step)

240            LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         6 (step)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
               POP_JUMP_IF_TRUE        14 (to L6)
               NOT_TAKEN

241            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST               8 ('malformed_proof_step')
               CALL                     1
               SWAP                     2
               POP_TOP
               RETURN_VALUE

242    L6:     LOAD_FAST_BORROW         6 (step)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST               9 ('sibling')
               CALL                     1
               STORE_FAST               7 (sibling)

243            LOAD_FAST_BORROW         6 (step)
               LOAD_ATTR                7 (get + NULL|self)
               LOAD_CONST              10 ('direction')
               CALL                     1
               STORE_FAST               8 (direction)

244            LOAD_GLOBAL              9 (_is_sha256_hex + NULL)
               LOAD_FAST_BORROW         7 (sibling)
               CALL                     1
               TO_BOOL
               POP_JUMP_IF_TRUE        14 (to L7)
               NOT_TAKEN

245            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST              11 ('invalid_sibling_hash')
               CALL                     1
               SWAP                     2
               POP_TOP
               RETURN_VALUE

246    L7:     LOAD_FAST_BORROW         8 (direction)
               LOAD_CONST              21 (('left', 'right'))
               CONTAINS_OP              1 (not in)
               POP_JUMP_IF_FALSE       14 (to L8)
               NOT_TAKEN

247            LOAD_GLOBAL              5 (_failed_verification + NULL)
               LOAD_CONST              13 ('invalid_direction')
               CALL                     1
               SWAP                     2
               POP_TOP
               RETURN_VALUE

248    L8:     LOAD_FAST_BORROW         8 (direction)
               LOAD_CONST              12 ('right')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       42 (to L9)
               NOT_TAKEN

249            LOAD_GLOBAL             17 (_hash_pair + NULL)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 87 (cur, sibling)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               CALL                     2
               STORE_FAST               5 (cur)
               JUMP_BACKWARD          170 (to L5)

251    L9:     LOAD_GLOBAL             17 (_hash_pair + NULL)
               LOAD_FAST_BORROW         7 (sibling)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         5 (cur)
               CALL                     2
               STORE_FAST               5 (cur)
               JUMP_BACKWARD          212 (to L5)

239   L10:     END_FOR
               POP_ITER

252            LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (cur, merkle_root)
               LOAD_ATTR               13 (strip + NULL|self)
               CALL                     0
               LOAD_ATTR               15 (lower + NULL|self)
               CALL                     0
               COMPARE_OP              72 (==)
               STORE_FAST               9 (valid)

254            LOAD_CONST              14 ('status')
               LOAD_CONST              15 ('ok')

255            LOAD_CONST              16 ('valid')
               LOAD_GLOBAL             19 (bool + NULL)
               LOAD_FAST_BORROW         9 (valid)
               CALL                     1

256            LOAD_CONST              17 ('warnings')
               LOAD_FAST                1 (warnings)

257            LOAD_CONST              18 ('error_code')
               LOAD_FAST_BORROW         9 (valid)
               TO_BOOL
               POP_JUMP_IF_FALSE        4 (to L11)
               NOT_TAKEN
               LOAD_CONST              19 (None)

253            BUILD_MAP                4
               RETURN_VALUE

257   L11:     LOAD_CONST              20 ('proof_does_not_match_root')

253            BUILD_MAP                4
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\merkle_inclusion_proofs.py", line 261>:
261           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('error_code')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _failed_proof at 0x0000018C18025030, file "app\services\operator\merkle_inclusion_proofs.py", line 261>:
261           RESUME                   0

263           LOAD_CONST               0 ('status')
              LOAD_CONST               1 ('failed')

264           LOAD_CONST               2 ('leaf_hash')
              LOAD_CONST               3 (None)

265           LOAD_CONST               4 ('merkle_root')
              LOAD_CONST               3 (None)

266           LOAD_CONST               5 ('proof')
              BUILD_LIST               0

267           LOAD_CONST               6 ('leaf_index')
              LOAD_CONST               3 (None)

268           LOAD_CONST               7 ('leaf_count')
              LOAD_SMALL_INT           0

269           LOAD_CONST               8 ('deterministic')
              LOAD_CONST               9 (True)

270           LOAD_CONST              10 ('warnings')
              BUILD_LIST               0

271           LOAD_CONST              11 ('error_code')
              LOAD_FAST_BORROW         0 (error_code)

262           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\merkle_inclusion_proofs.py", line 275>:
275           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('error_code')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _failed_verification at 0x0000018C17FA2B50, file "app\services\operator\merkle_inclusion_proofs.py", line 275>:
275           RESUME                   0

277           LOAD_CONST               0 ('status')
              LOAD_CONST               1 ('failed')

278           LOAD_CONST               2 ('valid')
              LOAD_CONST               3 (False)

279           LOAD_CONST               4 ('warnings')
              BUILD_LIST               0

280           LOAD_CONST               5 ('error_code')
              LOAD_FAST_BORROW         0 (error_code)

276           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _get_db_safe at 0x0000018C17FF13B0, file "app\services\operator\merkle_inclusion_proofs.py", line 288>:
 288           RESUME                   0

 289           NOP

 290   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('get_supabase',))
               IMPORT_NAME              0 (app.db.supabase_client)
               IMPORT_FROM              1 (get_supabase)
               STORE_FAST               0 (get_supabase)
               POP_TOP

 291           LOAD_FAST_BORROW         0 (get_supabase)
               PUSH_NULL
               CALL                     0
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 292           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE       55 (to L7)
               NOT_TAKEN
               STORE_FAST               1 (e)

 293   L4:     LOAD_GLOBAL              6 (logger)
               LOAD_ATTR                9 (warning + NULL|self)

 294           LOAD_CONST               2 ('merkle_inclusion_proofs db client unavailable type=')

 295           LOAD_GLOBAL             11 (type + NULL)
               LOAD_FAST                1 (e)
               CALL                     1
               LOAD_ATTR               12 (__name__)
               FORMAT_SIMPLE

 294           BUILD_STRING             2

 293           CALL                     1
               POP_TOP

 297   L5:     POP_EXCEPT
               LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               LOAD_CONST               3 (None)
               RETURN_VALUE

  --   L6:     LOAD_CONST               3 (None)
               STORE_FAST               1 (e)
               DELETE_FAST              1 (e)
               RERAISE                  1

 292   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L8 [1] lasti
  L4 to L5 -> L6 [1] lasti
  L6 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\services\operator\merkle_inclusion_proofs.py", line 300>:
300           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('max_len')
              LOAD_CONST               4 ('int')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _bound_str at 0x0000018C17972550, file "app\services\operator\merkle_inclusion_proofs.py", line 300>:
300           RESUME                   0

301           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

302           LOAD_CONST               0 (None)
              RETURN_VALUE

303   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

304           LOAD_FAST_BORROW         2 (s)
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN
              LOAD_GLOBAL              7 (len + NULL)
              LOAD_FAST_BORROW         2 (s)
              CALL                     1
              LOAD_FAST_BORROW         1 (max_len)
              COMPARE_OP             148 (bool(>))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

305   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

306   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\operator\merkle_inclusion_proofs.py", line 309>:
309           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_id')

311           LOAD_CONST               2 ('str')

309           LOAD_CONST               3 ('audit_entry_id')

312           LOAD_CONST               2 ('str')

309           LOAD_CONST               4 ('merkle_root_id')

313           LOAD_CONST               5 ('Optional[str]')

309           LOAD_CONST               6 ('return')

314           LOAD_CONST               7 ('Dict[str, Any]')

309           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object proof_for_audit_entry at 0x0000018C181A10A0, file "app\services\operator\merkle_inclusion_proofs.py", line 309>:
 309            RESUME                   0

 323            LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         0 (brokerage_id)
                LOAD_SMALL_INT         200
                CALL                     2
                STORE_FAST               3 (bid)

 324            LOAD_FAST_BORROW         3 (bid)
                POP_JUMP_IF_NOT_NONE    11 (to L1)
                NOT_TAKEN

 326            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 327            LOAD_CONST               4 ('error_code')
                LOAD_CONST               5 ('missing_brokerage_id')

 328            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 329            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 325            BUILD_MAP                4
                RETURN_VALUE

 331    L1:     LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (audit_entry_id)
                LOAD_SMALL_INT         200
                CALL                     2
                STORE_FAST               4 (aid)

 332            LOAD_FAST_BORROW         4 (aid)
                POP_JUMP_IF_NOT_NONE    11 (to L2)
                NOT_TAKEN

 334            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 335            LOAD_CONST               4 ('error_code')
                LOAD_CONST               8 ('missing_audit_entry_id')

 336            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 337            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 333            BUILD_MAP                4
                RETURN_VALUE

 339    L2:     LOAD_FAST_BORROW         2 (merkle_root_id)
                POP_JUMP_IF_NONE        13 (to L3)
                NOT_TAKEN
                LOAD_GLOBAL              1 (_bound_str + NULL)
                LOAD_FAST_BORROW         2 (merkle_root_id)
                LOAD_SMALL_INT         200
                CALL                     2
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (None)
        L4:     STORE_FAST               5 (mrid)

 341            LOAD_GLOBAL              3 (_get_db_safe + NULL)
                CALL                     0
                STORE_FAST               6 (db)

 342            LOAD_FAST_BORROW         6 (db)
                POP_JUMP_IF_NOT_NONE    12 (to L5)
                NOT_TAKEN

 344            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('skipped')

 345            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 ('audit_store_unavailable')

 346            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 347            LOAD_CONST               7 ('warnings')
                LOAD_CONST              10 ('audit_store_unavailable')
                BUILD_LIST               1

 343            BUILD_MAP                4
                RETURN_VALUE

 352    L5:     NOP

 354    L6:     LOAD_FAST_BORROW         6 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL              6 (_AUDIT_TABLE)
                CALL                     1

 355            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              11 ('action_id, occurred_at, brokerage_id, row_hash')
                CALL                     1

 356            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST              12 ('action_id')
                LOAD_FAST_BORROW         4 (aid)
                CALL                     2

 357            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST_BORROW         3 (bid)
                CALL                     2

 358            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 359            LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0

 353            STORE_FAST               7 (ar)

 361            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST_BORROW         7 (ar)
                LOAD_CONST              14 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                BUILD_LIST               0
        L9:     CALL                     1
                STORE_FAST               8 (ar_rows)

 373   L10:     LOAD_FAST                8 (ar_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L11)
                NOT_TAKEN

 375            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 376            LOAD_CONST               4 ('error_code')
                LOAD_CONST              17 ('audit_entry_not_found_or_cross_brokerage')

 377            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 378            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 374            BUILD_MAP                4
                RETURN_VALUE

 380   L11:     LOAD_FAST                8 (ar_rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              10 (entry)

 381            LOAD_FAST               10 (entry)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              18 ('row_hash')
                CALL                     1
                STORE_FAST              11 (row_hash)

 382            LOAD_FAST               10 (entry)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              19 ('occurred_at')
                CALL                     1
                STORE_FAST              12 (occurred_at)

 383            LOAD_GLOBAL             33 (_is_sha256_hex + NULL)
                LOAD_FAST               11 (row_hash)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L12)
                NOT_TAKEN

 385            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 386            LOAD_CONST               4 ('error_code')
                LOAD_CONST              20 ('audit_entry_missing_row_hash')

 387            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 388            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 384            BUILD_MAP                4
                RETURN_VALUE

 390   L12:     LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               12 (occurred_at)
                LOAD_GLOBAL             36 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L13)
                NOT_TAKEN
                LOAD_FAST               12 (occurred_at)
                LOAD_ATTR               39 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L14)
                NOT_TAKEN

 392   L13:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 393            LOAD_CONST               4 ('error_code')
                LOAD_CONST              21 ('audit_entry_missing_occurred_at')

 394            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 395            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 391            BUILD_MAP                4
                RETURN_VALUE

 401   L14:     NOP

 402   L15:     LOAD_FAST                5 (mrid)
                POP_JUMP_IF_NONE        83 (to L16)
                NOT_TAKEN

 404            LOAD_FAST                6 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL             40 (_MERKLE_TABLE)
                CALL                     1

 405            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              22 ('root_id, window_start, window_end, merkle_root, brokerage_id, rows_in_window')
                CALL                     1

 407            LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST              23 ('root_id')
                LOAD_FAST                5 (mrid)
                CALL                     2

 408            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 409            LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0

 403            STORE_FAST              13 (mr)
                JUMP_FORWARD           114 (to L17)

 413   L16:     LOAD_FAST                6 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL             40 (_MERKLE_TABLE)
                CALL                     1

 414            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              22 ('root_id, window_start, window_end, merkle_root, brokerage_id, rows_in_window')
                CALL                     1

 416            LOAD_ATTR               43 (lt + NULL|self)
                LOAD_CONST              24 ('window_start')
                LOAD_FAST               12 (occurred_at)
                CALL                     2

 417            LOAD_ATTR               45 (gt + NULL|self)
                LOAD_CONST              25 ('window_end')
                LOAD_FAST               12 (occurred_at)
                CALL                     2

 418            LOAD_ATTR               47 (order + NULL|self)
                LOAD_CONST              25 ('window_end')
                LOAD_CONST              26 (True)
                LOAD_CONST              27 (('desc',))
                CALL_KW                  2

 419            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_SMALL_INT           1
                CALL                     1

 420            LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0

 412            STORE_FAST              13 (mr)

 422   L17:     LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST               13 (mr)
                LOAD_CONST              14 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L20)
       L18:     NOT_TAKEN
       L19:     POP_TOP
                BUILD_LIST               0
       L20:     CALL                     1
                STORE_FAST              14 (mr_rows)

 434   L21:     LOAD_FAST               14 (mr_rows)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L22)
                NOT_TAKEN

 436            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 437            LOAD_CONST               4 ('error_code')
                LOAD_CONST              29 ('merkle_root_window_not_found')

 438            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 439            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 435            BUILD_MAP                4
                RETURN_VALUE

 441   L22:     LOAD_FAST               14 (mr_rows)
                LOAD_SMALL_INT           0
                BINARY_OP               26 ([])
                STORE_FAST              15 (merkle)

 442            LOAD_FAST               15 (merkle)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              24 ('window_start')
                CALL                     1
                STORE_FAST              16 (window_start)

 443            LOAD_FAST               15 (merkle)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              25 ('window_end')
                CALL                     1
                STORE_FAST              17 (window_end)

 444            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               16 (window_start)
                LOAD_GLOBAL             36 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L23)
                NOT_TAKEN
                LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               17 (window_end)
                LOAD_GLOBAL             36 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L24)
                NOT_TAKEN

 446   L23:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 447            LOAD_CONST               4 ('error_code')
                LOAD_CONST              30 ('merkle_window_malformed')

 448            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 449            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 445            BUILD_MAP                4
                RETURN_VALUE

 457   L24:     LOAD_FAST               15 (merkle)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                CALL                     1
                STORE_FAST              18 (merkle_bid)

 458            NOP

 460   L25:     LOAD_FAST                6 (db)
                LOAD_ATTR                5 (table + NULL|self)
                LOAD_GLOBAL              6 (_AUDIT_TABLE)
                CALL                     1

 461            LOAD_ATTR                9 (select + NULL|self)
                LOAD_CONST              31 ('action_id, row_hash, occurred_at')
                CALL                     1

 462            LOAD_ATTR               45 (gt + NULL|self)
                LOAD_CONST              19 ('occurred_at')
                LOAD_FAST               16 (window_start)
                CALL                     2

 463            LOAD_ATTR               43 (lt + NULL|self)
                LOAD_CONST              19 ('occurred_at')
                LOAD_FAST               17 (window_end)
                CALL                     2

 464            LOAD_ATTR               47 (order + NULL|self)
                LOAD_CONST              19 ('occurred_at')
                LOAD_CONST              32 (False)
                LOAD_CONST              27 (('desc',))
                CALL_KW                  2

 465            LOAD_ATTR               13 (limit + NULL|self)
                LOAD_CONST              33 (10000)
                CALL                     1

 459            STORE_FAST              19 (query)

 467            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               18 (merkle_bid)
                LOAD_GLOBAL             36 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       41 (to L28)
                NOT_TAKEN
                LOAD_FAST               18 (merkle_bid)
                LOAD_ATTR               39 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L28)
       L26:     NOT_TAKEN

 468   L27:     LOAD_FAST               19 (query)
                LOAD_ATTR               11 (eq + NULL|self)
                LOAD_CONST              13 ('brokerage_id')
                LOAD_FAST               18 (merkle_bid)
                CALL                     2
                STORE_FAST              19 (query)

 469   L28:     LOAD_FAST               19 (query)
                LOAD_ATTR               15 (execute + NULL|self)
                CALL                     0
                STORE_FAST              20 (wr)

 470            LOAD_GLOBAL             17 (list + NULL)
                LOAD_GLOBAL             19 (getattr + NULL)
                LOAD_FAST               20 (wr)
                LOAD_CONST              14 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L31)
       L29:     NOT_TAKEN
       L30:     POP_TOP
                BUILD_LIST               0
       L31:     CALL                     1
                STORE_FAST              21 (window_rows)

 483   L32:     BUILD_LIST               0
                STORE_FAST              22 (leaves)

 484            LOAD_CONST              42 (-1)
                STORE_FAST              23 (leaf_index)

 485            LOAD_GLOBAL             49 (enumerate + NULL)
                LOAD_FAST               21 (window_rows)
                CALL                     1
                GET_ITER
       L33:     FOR_ITER               153 (to L37)
                UNPACK_SEQUENCE          2
                STORE_FAST              24 (i)
                STORE_FAST              25 (r)

 486            LOAD_GLOBAL             35 (isinstance + NULL)
                LOAD_FAST               25 (r)
                LOAD_GLOBAL             50 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L34)
                NOT_TAKEN

 487            JUMP_BACKWARD           30 (to L33)

 488   L34:     LOAD_FAST               25 (r)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              18 ('row_hash')
                CALL                     1
                STORE_FAST              26 (h)

 489            LOAD_GLOBAL             33 (_is_sha256_hex + NULL)
                LOAD_FAST               26 (h)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L35)
                NOT_TAKEN

 490            JUMP_BACKWARD           66 (to L33)

 491   L35:     LOAD_FAST               22 (leaves)
                LOAD_ATTR               53 (append + NULL|self)
                LOAD_FAST               26 (h)
                LOAD_ATTR               39 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               55 (lower + NULL|self)
                CALL                     0
                CALL                     1
                POP_TOP

 492            LOAD_FAST               25 (r)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              12 ('action_id')
                CALL                     1
                LOAD_FAST                4 (aid)
                COMPARE_OP              88 (bool(==))
                POP_JUMP_IF_TRUE         3 (to L36)
                NOT_TAKEN
                JUMP_BACKWARD          135 (to L33)

 493   L36:     LOAD_GLOBAL             57 (len + NULL)
                LOAD_FAST               22 (leaves)
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP               10 (-)
                STORE_FAST              23 (leaf_index)
                JUMP_BACKWARD          155 (to L33)

 485   L37:     END_FOR
                POP_ITER

 494            LOAD_FAST               23 (leaf_index)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       11 (to L38)
                NOT_TAKEN

 496            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 497            LOAD_CONST               4 ('error_code')
                LOAD_CONST              35 ('audit_entry_outside_window')

 498            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 499            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 495            BUILD_MAP                4
                RETURN_VALUE

 502   L38:     LOAD_GLOBAL             59 (generate_inclusion_proof + NULL)
                LOAD_FAST               22 (leaves)
                LOAD_FAST               23 (leaf_index)
                CALL                     2
                STORE_FAST              27 (proof)

 503            LOAD_FAST               27 (proof)
                LOAD_CONST               2 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST              36 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       77 (to L41)
                NOT_TAKEN

 505            LOAD_CONST               2 ('status')
                LOAD_FAST               27 (proof)
                LOAD_CONST               2 ('status')
                BINARY_OP               26 ([])

 506            LOAD_CONST               4 ('error_code')
                LOAD_FAST               27 (proof)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               4 ('error_code')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L39)
                NOT_TAKEN
                POP_TOP
                LOAD_CONST              37 ('proof_generation_failed')

 507   L39:     LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 508            LOAD_CONST               7 ('warnings')
                LOAD_GLOBAL             17 (list + NULL)
                LOAD_FAST               27 (proof)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST               7 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L40)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L40:     CALL                     1

 504            BUILD_MAP                4
                RETURN_VALUE

 513   L41:     LOAD_FAST               15 (merkle)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              38 ('merkle_root')
                CALL                     1
                STORE_FAST              28 (persisted_root)

 514            LOAD_GLOBAL             33 (_is_sha256_hex + NULL)
                LOAD_FAST               28 (persisted_root)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L42)
                NOT_TAKEN

 516            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 517            LOAD_CONST               4 ('error_code')
                LOAD_CONST              39 ('persisted_merkle_root_malformed')

 518            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 519            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 515            BUILD_MAP                4
                RETURN_VALUE

 521   L42:     LOAD_FAST               27 (proof)
                LOAD_CONST              38 ('merkle_root')
                BINARY_OP               26 ([])
                LOAD_FAST               28 (persisted_root)
                LOAD_ATTR               39 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               55 (lower + NULL|self)
                CALL                     0
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       11 (to L43)
                NOT_TAKEN

 523            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 524            LOAD_CONST               4 ('error_code')
                LOAD_CONST              40 ('computed_root_does_not_match_persisted')

 525            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 526            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 522            BUILD_MAP                4
                RETURN_VALUE

 529   L43:     LOAD_CONST               2 ('status')
                LOAD_CONST              36 ('ok')

 530            LOAD_CONST               6 ('proof')
                LOAD_FAST               27 (proof)

 531            LOAD_CONST              41 ('merkle_root_id')
                LOAD_FAST               15 (merkle)
                LOAD_ATTR               31 (get + NULL|self)
                LOAD_CONST              23 ('root_id')
                CALL                     1

 532            LOAD_CONST              24 ('window_start')
                LOAD_FAST               16 (window_start)

 533            LOAD_CONST              25 ('window_end')
                LOAD_FAST               17 (window_end)

 534            LOAD_CONST               7 ('warnings')
                BUILD_LIST               0

 535            LOAD_CONST               4 ('error_code')
                LOAD_CONST               1 (None)

 528            BUILD_MAP                7
                RETURN_VALUE

  --   L44:     PUSH_EXC_INFO

 362            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L49)
                NOT_TAKEN
                STORE_FAST               9 (e)

 363   L45:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 364            LOAD_CONST              15 ('proof_for_audit_entry audit read error type=')

 365            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 364            BUILD_STRING             2

 363            CALL                     1
                POP_TOP

 368            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('skipped')

 369            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 ('audit_store_unavailable')

 370            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 371            LOAD_CONST               7 ('warnings')
                LOAD_CONST              16 ('db_read_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 367            BUILD_MAP                4
       L46:     SWAP                     2
       L47:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L48:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 362   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L51:     PUSH_EXC_INFO

 423            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L56)
                NOT_TAKEN
                STORE_FAST               9 (e)

 424   L52:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 425            LOAD_CONST              28 ('proof_for_audit_entry merkle read error type=')

 426            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 425            BUILD_STRING             2

 424            CALL                     1
                POP_TOP

 429            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('skipped')

 430            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 ('audit_store_unavailable')

 431            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 432            LOAD_CONST               7 ('warnings')
                LOAD_CONST              16 ('db_read_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 428            BUILD_MAP                4
       L53:     SWAP                     2
       L54:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L55:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 423   L56:     RERAISE                  0

  --   L57:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L58:     PUSH_EXC_INFO

 471            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       87 (to L63)
                NOT_TAKEN
                STORE_FAST               9 (e)

 472   L59:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 473            LOAD_CONST              34 ('proof_for_audit_entry window read error type=')

 474            LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE

 473            BUILD_STRING             2

 472            CALL                     1
                POP_TOP

 477            LOAD_CONST               2 ('status')
                LOAD_CONST               9 ('skipped')

 478            LOAD_CONST               4 ('error_code')
                LOAD_CONST              10 ('audit_store_unavailable')

 479            LOAD_CONST               6 ('proof')
                LOAD_CONST               1 (None)

 480            LOAD_CONST               7 ('warnings')
                LOAD_CONST              16 ('db_read_failed:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 476            BUILD_MAP                4
       L60:     SWAP                     2
       L61:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L62:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 471   L63:     RERAISE                  0

  --   L64:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L44 [0]
  L8 to L10 -> L44 [0]
  L15 to L18 -> L51 [0]
  L19 to L21 -> L51 [0]
  L25 to L26 -> L58 [0]
  L27 to L29 -> L58 [0]
  L30 to L32 -> L58 [0]
  L44 to L45 -> L50 [1] lasti
  L45 to L46 -> L48 [1] lasti
  L46 to L47 -> L50 [1] lasti
  L48 to L50 -> L50 [1] lasti
  L51 to L52 -> L57 [1] lasti
  L52 to L53 -> L55 [1] lasti
  L53 to L54 -> L57 [1] lasti
  L55 to L57 -> L57 [1] lasti
  L58 to L59 -> L64 [1] lasti
  L59 to L60 -> L62 [1] lasti
  L60 to L61 -> L64 [1] lasti
  L62 to L64 -> L64 [1] lasti
```
