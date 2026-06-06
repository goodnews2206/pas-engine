# ingestion/email_forwarder_secret_store

- **pyc:** `app\services\ingestion\__pycache__\email_forwarder_secret_store.cpython-314.pyc`
- **expected source path (absent):** `app\services\ingestion/email_forwarder_secret_store.py`
- **co_filename (from bytecode):** `app\services\ingestion\email_forwarder_secret_store.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** ingestion

## Module docstring

```
PAS167 / PAS168 — Email forwarder secret store.

Centralises the resolution of a brokerage's
``email_forwarder_secret`` so that:

* The route + service no longer reach into the brokerage row
  directly (single seam → easier audit, single place to add
  per-brokerage key-id support).
* The encrypted-column path can be flipped on incrementally
  via a literal-True env flag without changing PAS164 / PAS165
  / PAS166 behaviour for any brokerage that hasn't migrated.
* Plaintext fallback remains supported with an explicit
  structural warning (``plaintext_forwarder_secret_fallback``)
  so the operator dashboard can count "how many brokerages
  haven't migrated yet".
* No fake encryption: if the real crypto helper
  (``cryptography.fernet.Fernet``) is not importable,
  ``encrypt`` and ``decrypt`` return the structural failure
  ``crypto_unavailable``. We never invent a reversible
  encoding that pretends to be encryption.

PAS168 additions:

* **Kid-aware envelope.** The encrypted column carries a
  ``<kid>:<fernet token>`` envelope. The kid identifies which
  symmetric key encrypted the secret so the operator can
  rotate the key without losing access to historical
  ciphertext (the helper looks up the right key by kid).
* **Per-kid key resolution.** Keys are resolved from
  ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>`` env vars
  (case-insensitive kid). The active kid for new encryptions
  is set via ``PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID``.
* **Legacy fallback.** A ciphertext without a kid prefix is
  treated as a legacy single-key Fernet token and decrypted
  with the optional ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY``
  env var (preserves PAS167 single-key deployments).

Hard doctrine:

* No helper here raises. Every failure path returns a
  structural envelope.
* The raw secret is NEVER logged, NEVER placed in an event
  payload, NEVER returned in any public/report envelope.
  ``get_email_forwarder_secret`` may return the secret to the
  in-process route/service caller — it is the caller's
  responsibility to keep it out of responses + events (the
  route does, today).
* No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /
  vendor / embedding import.
```

## Imports

`Any`, `Dict`, `Fernet`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `cryptography.fernet`, `logging`, `os`, `re`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_key_material_for_kid`, `_kid_from_config`, `_load_fernet`, `_probe_field`, `_resolve_active_kid`, `_split_envelope`, `_wrap_envelope`, `decrypt_email_forwarder_secret`, `email_forwarder_secret_encryption_enabled`, `encrypt_email_forwarder_secret`, `get_email_forwarder_secret`, `redact_secret_for_log`

## Env-key candidates

`PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID`, `PAS_EMAIL_FORWARDER_SECRET_ENCRYPTION_ENABLED`, `PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY`, `PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_`

## String constants (redacted where noted)

- '\nPAS167 / PAS168 — Email forwarder secret store.\n\nCentralises the resolution of a brokerage\'s\n``email_forwarder_secret`` so that:\n\n* The route + service no longer reach into the brokerage row\n  directly (single seam → easier audit, single place to add\n  per-brokerage key-id support).\n* The encrypted-column path can be flipped on incrementally\n  via a literal-True env flag without changing PAS164 / PAS165\n  / PAS166 behaviour for any brokerage that hasn\'t migrated.\n* Plaintext fallback remains supported with an explicit\n  structural warning (``plaintext_forwarder_secret_fallback``)\n  so the operator dashboard can count "how many brokerages\n  haven\'t migrated yet".\n* No fake encryption: if the real crypto helper\n  (``cryptography.fernet.Fernet``) is not importable,\n  ``encrypt`` and ``decrypt`` return the structural failure\n  ``crypto_unavailable``. We never invent a reversible\n  encoding that pretends to be encryption.\n\nPAS168 additions:\n\n* **Kid-aware envelope.** The encrypted column carries a\n  ``<kid>:<fernet token>`` envelope. The kid identifies which\n  symmetric key encrypted the secret so the operator can\n  rotate the key without losing access to historical\n  ciphertext (the helper looks up the right key by kid).\n* **Per-kid key resolution.** Keys are resolved from\n  ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>`` env vars\n  (case-insensitive kid). The active kid for new encryptions\n  is set via ``PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID``.\n* **Legacy fallback.** A ciphertext without a kid prefix is\n  treated as a legacy single-key Fernet token and decrypted\n  with the optional ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY``\n  env var (preserves PAS167 single-key deployments).\n\nHard doctrine:\n\n* No helper here raises. Every failure path returns a\n  structural envelope.\n* The raw secret is NEVER logged, NEVER placed in an event\n  payload, NEVER returned in any public/report envelope.\n  ``get_email_forwarder_secret`` may return the secret to the\n  in-process route/service caller — it is the caller\'s\n  responsibility to keep it out of responses + events (the\n  route does, today).\n* No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n  vendor / embedding import.\n'
- 'pas.ingestion.email_forwarder_secret_store'
- 'PAS_EMAIL_FORWARDER_SECRET_ENCRYPTION_ENABLED'
- 'true'
- 'PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID'
- 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_'
- 'PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY'
- 'email_forwarder_secret'
- 'email_forwarder_secret_encrypted'
- 'email_forwarder_secret_kid'
- 'email_forwarder_secret_migration_status'
- '^[A-Za-z0-9._\\-]{1,64}$'
- '^([A-Za-z0-9._\\-]{1,64}):([A-Za-z0-9_\\-=]+)$'
- 'config_or_env'
- 'key_id'
- 'Any'
- 'return'
- 'bool'
- 'Resolve whether the encrypted-column path is enabled.\n\nPrecedence:\n\n1. ``config_or_env`` — if it is a dict carrying\n   ``email_forwarder_secret_encryption_enabled`` set to\n   the literal Python ``True``, encryption is enabled.\n   Strings / ints / ``"true"`` do NOT enable.\n2. The environment variable\n   ``PAS_EMAIL_FORWARDER_SECRET_ENCRYPTION_ENABLED``: enabled\n   only when the value (case-insensitive, trimmed) is the\n   literal string ``"true"``.  Anything else (missing,\n   ``"yes"``, ``"1"``, ``"on"``, …) keeps it disabled.\n\nDefault: DISABLED. This is the safest default — every\ndeployment that has not gone through the operator-driven\nmigration continues to use the plaintext path with a\nstructural warning, no behaviour change.\n\nNEVER raises.\n'
- 'email_forwarder_secret_encryption_enabled'
- "Try to import the ``cryptography`` Fernet primitive.\n\nReturns the ``Fernet`` class on success, ``None`` if the\npackage isn't installed. NEVER raises.\n"
- 'Optional[str]'
- 'Return the active kid from a dict-shaped config, if any.\nNEVER raises.'
- 'email_forwarder_secret_active_kid'
- 'Resolve the kid that NEW encryptions should use.\n\nPrecedence:\n\n1. ``config_or_env["email_forwarder_secret_active_kid"]``.\n2. The env var ``PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID``.\n3. ``None`` (no active kid configured — operator must\n   supply one before the rotation script can run).\n\nNEVER raises. NEVER echoes the kid in an error.\n'
- 'kid'
- 'Optional[bytes]'
- 'Resolve the key material (raw bytes ready for Fernet)\nfor ``kid``.\n\nPrecedence:\n\n1. ``config_or_env["email_forwarder_secret_keys"]`` — when\n   this is a dict mapping kid → raw fernet key string.\n   Useful for tests that want to stub keys without\n   touching the env.\n2. The env var\n   ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>``\n   (case-insensitive kid; the env lookup uses the\n   upper-cased kid).\n3. If ``kid`` is ``None`` (legacy ciphertext), the env var\n   ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY`` (the PAS167\n   single-key fallback).\n\nNEVER raises. NEVER echoes the key value.\n'
- 'email_forwarder_secret_keys'
- 'utf-8'
- 'email_forwarder_secret_fernet_key'
- 'value'
- 'str'
- 'Return a structural redaction tag for ``value``. NEVER\nechoes the value or any prefix/suffix of it.'
- '<absent>'
- '<redacted>'
- 'token'
- 'Build the ``<kid>:<fernet token>`` envelope. Both\ncomponents are assumed structurally valid.'
- 'encrypted'
- 'Tuple[Optional[str], str]'
- 'Parse the encrypted column value. Returns\n``(kid, token)``. If the value does not match the\n``<kid>:<token>`` shape, returns ``(None, encrypted)`` so\nthe caller can attempt a legacy single-key decrypt.'
- 'secret'
- 'Dict[str, Any]'
- 'Encrypt ``secret`` for at-rest storage in the brokerage\nrow\'s encrypted column.\n\nReturns a structural envelope::\n\n    {\n      "status":     "ok" | "failed",\n      "encrypted":  None | "<kid>:<fernet token>",\n      "key_id":     None | "<kid used>",\n      "warnings":   [<structural tokens>],\n      "error_code": None | "<structural token>",\n    }\n\nBehaviour:\n\n* ``key_id`` (kwarg) overrides the env-bound active kid.\n  If neither is set, returns ``error_code="missing_active_kid"``.\n* The kid must match ``_KID_RE`` (lowercase alphanumeric +\n  ``-._``, 1..64 chars). A malformed kid → ``error_code=\n  "invalid_kid"``.\n* If the per-kid key is not configured → ``error_code=\n  "crypto_key_missing"``.\n* If the ``cryptography`` package isn\'t importable →\n  ``error_code="crypto_unavailable"``.\n\nNEVER raises. NEVER echoes the secret / key / kid value in\nerrors.\n'
- 'status'
- 'failed'
- 'warnings'
- 'error_code'
- 'missing_secret'
- 'crypto_unavailable'
- 'missing_active_kid'
- 'invalid_kid'
- 'crypto_key_missing'
- 'encrypt_email_forwarder_secret unexpected error type='
- 'crypto_error:'
- 'Decrypt ``encrypted`` to recover the original forwarder\nsecret.\n\nReturns a structural envelope::\n\n    {\n      "status":     "ok" | "failed",\n      "secret":     None | "<plaintext>",\n      "key_id":     None | "<kid used>",\n      "warnings":   [<structural tokens>],\n      "error_code": None | "<structural token>",\n    }\n\nBehaviour:\n\n* If ``encrypted`` matches the ``<kid>:<token>`` envelope,\n  the embedded kid wins (regardless of the ``key_id``\n  kwarg).\n* Else the legacy single-key path is tried (with the\n  ``key_id`` kwarg or env legacy key).\n* Unknown kid → ``error_code="crypto_key_missing"``.\n* Malformed ciphertext → ``error_code=\n  "forwarder_secret_decrypt_failed"``.\n* ``cryptography`` package missing → ``error_code=\n  "crypto_unavailable"``.\n\nThe returned ``secret`` is intended for the in-process\nroute/service only and MUST NEVER appear in responses or\nevent payloads. NEVER raises. NEVER echoes the ciphertext\nor the key.\n'
- 'missing_encrypted'
- 'decrypt_email_forwarder_secret failed type='
- 'forwarder_secret_decrypt_failed'
- 'brokerage'
- 'field'
- 'Read a string-shaped field from the brokerage row, looking\nat the top level plus the bounded nested holders. NEVER\nraises. NEVER echoes the value.'
- 'Optional[Dict[str, Any]]'
- 'Resolve the brokerage\'s forwarder secret using the\nPAS167 + PAS168 precedence rules.\n\nReturns a structural envelope::\n\n    {\n      "status":             "ok" | "missing" | "failed",\n      "secret":             None | "<plaintext, internal-only>",\n      "encryption_enabled": bool,\n      "plaintext_fallback": bool,\n      "migration_status":   None | "plaintext" | "encrypted"\n                              | "rotation_required" | "disabled",\n      "warnings":           [<structural tokens>],\n      "error_code":         None | "<structural token>",\n    }\n\nPrecedence:\n\n1. If encryption is **disabled** (default), use the\n   plaintext column directly.\n2. If encryption is **enabled** AND an encrypted ciphertext\n   is present on the row, try to decrypt (kid-aware). On\n   success → ``ok``. On decrypt failure → ``failed``; do\n   NOT silently fall back to plaintext.\n3. If encryption is **enabled** AND no encrypted ciphertext\n   is present BUT a plaintext column value exists, return\n   ``ok`` with the plaintext secret AND the\n   ``plaintext_forwarder_secret_fallback`` warning.\n4. If neither is present, return ``missing``.\n\nNEVER raises.\n'
- 'encryption_enabled'
- 'plaintext_fallback'
- 'migration_status'
- 'missing'
- 'plaintext_forwarder_secret_fallback'

## Disassembly

```
  0           RESUME                   0

  1           LOAD_CONST               0 ('\nPAS167 / PAS168 — Email forwarder secret store.\n\nCentralises the resolution of a brokerage\'s\n``email_forwarder_secret`` so that:\n\n* The route + service no longer reach into the brokerage row\n  directly (single seam → easier audit, single place to add\n  per-brokerage key-id support).\n* The encrypted-column path can be flipped on incrementally\n  via a literal-True env flag without changing PAS164 / PAS165\n  / PAS166 behaviour for any brokerage that hasn\'t migrated.\n* Plaintext fallback remains supported with an explicit\n  structural warning (``plaintext_forwarder_secret_fallback``)\n  so the operator dashboard can count "how many brokerages\n  haven\'t migrated yet".\n* No fake encryption: if the real crypto helper\n  (``cryptography.fernet.Fernet``) is not importable,\n  ``encrypt`` and ``decrypt`` return the structural failure\n  ``crypto_unavailable``. We never invent a reversible\n  encoding that pretends to be encryption.\n\nPAS168 additions:\n\n* **Kid-aware envelope.** The encrypted column carries a\n  ``<kid>:<fernet token>`` envelope. The kid identifies which\n  symmetric key encrypted the secret so the operator can\n  rotate the key without losing access to historical\n  ciphertext (the helper looks up the right key by kid).\n* **Per-kid key resolution.** Keys are resolved from\n  ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_<KID>`` env vars\n  (case-insensitive kid). The active kid for new encryptions\n  is set via ``PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID``.\n* **Legacy fallback.** A ciphertext without a kid prefix is\n  treated as a legacy single-key Fernet token and decrypted\n  with the optional ``PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY``\n  env var (preserves PAS167 single-key deployments).\n\nHard doctrine:\n\n* No helper here raises. Every failure path returns a\n  structural envelope.\n* The raw secret is NEVER logged, NEVER placed in an event\n  payload, NEVER returned in any public/report envelope.\n  ``get_email_forwarder_secret`` may return the secret to the\n  in-process route/service caller — it is the caller\'s\n  responsibility to keep it out of responses + events (the\n  route does, today).\n* No Gmail / Google / OAuth / IMAP / POP3 / inbox-scan /\n  vendor / embedding import.\n')
              STORE_NAME               0 (__doc__)

 53           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('annotations',))
              IMPORT_NAME              1 (__future__)
              IMPORT_FROM              2 (annotations)
              STORE_NAME               2 (annotations)
              POP_TOP

 55           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              3 (logging)
              STORE_NAME               3 (logging)

 56           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              4 (os)
              STORE_NAME               4 (os)

 57           LOAD_SMALL_INT           0
              LOAD_CONST               2 (None)
              IMPORT_NAME              5 (re)
              STORE_NAME               5 (re)

 58           LOAD_SMALL_INT           0
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

 61           LOAD_NAME                3 (logging)
              LOAD_ATTR               24 (getLogger)
              PUSH_NULL
              LOAD_CONST               4 ('pas.ingestion.email_forwarder_secret_store')
              CALL                     1
              STORE_NAME              13 (logger)

 68           LOAD_CONST               5 ('PAS_EMAIL_FORWARDER_SECRET_ENCRYPTION_ENABLED')
              STORE_NAME              14 (_ENV_ENCRYPTION_FLAG)

 69           LOAD_CONST               6 ('true')
              STORE_NAME              15 (_ENV_TRUE_LITERAL)

 72           LOAD_CONST               7 ('PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID')
              STORE_NAME              16 (_ENV_ACTIVE_KID)

 76           LOAD_CONST               8 ('PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY_')
              STORE_NAME              17 (_ENV_PER_KID_PREFIX)

 80           LOAD_CONST               9 ('PAS_EMAIL_FORWARDER_SECRET_FERNET_KEY')
              STORE_NAME              18 (_ENV_LEGACY_KEY)

 83           LOAD_CONST              10 ('email_forwarder_secret')
              STORE_NAME              19 (_PLAINTEXT_FIELD)

 84           LOAD_CONST              11 ('email_forwarder_secret_encrypted')
              STORE_NAME              20 (_ENCRYPTED_FIELD)

 85           LOAD_CONST              12 ('email_forwarder_secret_kid')
              STORE_NAME              21 (_KEY_ID_FIELD)

 86           LOAD_CONST              13 ('email_forwarder_secret_migration_status')
              STORE_NAME              22 (_MIGRATION_STATUS_FIELD)

 87           LOAD_CONST              41 (('features', 'config'))
              STORE_NAME              23 (_NEST_KEYS)

 94           LOAD_NAME                5 (re)
              LOAD_ATTR               48 (compile)
              PUSH_NULL
              LOAD_CONST              14 ('^[A-Za-z0-9._\\-]{1,64}$')
              CALL                     1
              STORE_NAME              25 (_KID_RE)

 95           LOAD_NAME                5 (re)
              LOAD_ATTR               48 (compile)
              PUSH_NULL
              LOAD_CONST              15 ('^([A-Za-z0-9._\\-]{1,64}):([A-Za-z0-9_\\-=]+)$')
              CALL                     1
              STORE_NAME              26 (_ENVELOPE_RE)

102           LOAD_CONST              42 ((None,))
              LOAD_CONST              16 (<code object __annotate__ at 0x0000018C17FA35A0, file "app\services\ingestion\email_forwarder_secret_store.py", line 102>)
              MAKE_FUNCTION
              LOAD_CONST              17 (<code object email_forwarder_secret_encryption_enabled at 0x0000018C17F01460, file "app\services\ingestion\email_forwarder_secret_store.py", line 102>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              27 (email_forwarder_secret_encryption_enabled)

144           LOAD_CONST              18 (<code object _load_fernet at 0x0000018C18090690, file "app\services\ingestion\email_forwarder_secret_store.py", line 144>)
              MAKE_FUNCTION
              STORE_NAME              28 (_load_fernet)

161           LOAD_CONST              19 (<code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_forwarder_secret_store.py", line 161>)
              MAKE_FUNCTION
              LOAD_CONST              20 (<code object _kid_from_config at 0x0000018C1804C9F0, file "app\services\ingestion\email_forwarder_secret_store.py", line 161>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              29 (_kid_from_config)

172           LOAD_CONST              42 ((None,))
              LOAD_CONST              21 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_forwarder_secret_store.py", line 172>)
              MAKE_FUNCTION
              LOAD_CONST              22 (<code object _resolve_active_kid at 0x0000018C17EC4280, file "app\services\ingestion\email_forwarder_secret_store.py", line 172>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   1 (defaults)
              STORE_NAME              30 (_resolve_active_kid)

197           LOAD_CONST              23 ('config_or_env')

200           LOAD_CONST               2 (None)

197           BUILD_MAP                1
              LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\email_forwarder_secret_store.py", line 197>)
              MAKE_FUNCTION
              LOAD_CONST              25 (<code object _key_material_for_kid at 0x0000018C17F83BE0, file "app\services\ingestion\email_forwarder_secret_store.py", line 197>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              31 (_key_material_for_kid)

262           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_forwarder_secret_store.py", line 262>)
              MAKE_FUNCTION
              LOAD_CONST              27 (<code object redact_secret_for_log at 0x0000018C18053870, file "app\services\ingestion\email_forwarder_secret_store.py", line 262>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              32 (redact_secret_for_log)

274           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_forwarder_secret_store.py", line 274>)
              MAKE_FUNCTION
              LOAD_CONST              29 (<code object _wrap_envelope at 0x0000018C18069290, file "app\services\ingestion\email_forwarder_secret_store.py", line 274>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              33 (_wrap_envelope)

280           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_forwarder_secret_store.py", line 280>)
              MAKE_FUNCTION
              LOAD_CONST              31 (<code object _split_envelope at 0x0000018C18048730, file "app\services\ingestion\email_forwarder_secret_store.py", line 280>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              34 (_split_envelope)

297           LOAD_CONST              32 ('key_id')

300           LOAD_CONST               2 (None)

297           LOAD_CONST              23 ('config_or_env')

301           LOAD_CONST               2 (None)

297           BUILD_MAP                2
              LOAD_CONST              33 (<code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\email_forwarder_secret_store.py", line 297>)
              MAKE_FUNCTION
              LOAD_CONST              34 (<code object encrypt_email_forwarder_secret at 0x0000018C17F81110, file "app\services\ingestion\email_forwarder_secret_store.py", line 297>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              35 (encrypt_email_forwarder_secret)

407           LOAD_CONST              32 ('key_id')

410           LOAD_CONST               2 (None)

407           LOAD_CONST              23 ('config_or_env')

411           LOAD_CONST               2 (None)

407           BUILD_MAP                2
              LOAD_CONST              35 (<code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\email_forwarder_secret_store.py", line 407>)
              MAKE_FUNCTION
              LOAD_CONST              36 (<code object decrypt_email_forwarder_secret at 0x0000018C17D457A0, file "app\services\ingestion\email_forwarder_secret_store.py", line 407>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              36 (decrypt_email_forwarder_secret)

523           LOAD_CONST              37 (<code object __annotate__ at 0x0000018C18025230, file "app\services\ingestion\email_forwarder_secret_store.py", line 523>)
              MAKE_FUNCTION
              LOAD_CONST              38 (<code object _probe_field at 0x0000018C17ED54B0, file "app\services\ingestion\email_forwarder_secret_store.py", line 523>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              STORE_NAME              37 (_probe_field)

541           LOAD_CONST              23 ('config_or_env')

544           LOAD_CONST               2 (None)

541           BUILD_MAP                1
              LOAD_CONST              39 (<code object __annotate__ at 0x0000018C18025030, file "app\services\ingestion\email_forwarder_secret_store.py", line 541>)
              MAKE_FUNCTION
              LOAD_CONST              40 (<code object get_email_forwarder_secret at 0x0000018C17F841C0, file "app\services\ingestion\email_forwarder_secret_store.py", line 541>)
              MAKE_FUNCTION
              SET_FUNCTION_ATTRIBUTE  16 (annotate)
              SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
              STORE_NAME              38 (get_email_forwarder_secret)

661           BUILD_LIST               0
              LOAD_CONST              43 (('email_forwarder_secret_encryption_enabled', 'get_email_forwarder_secret', 'encrypt_email_forwarder_secret', 'decrypt_email_forwarder_secret', 'redact_secret_for_log'))
              LIST_EXTEND              1
              STORE_NAME              39 (__all__)
              LOAD_CONST               2 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA35A0, file "app\services\ingestion\email_forwarder_secret_store.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')

103           LOAD_CONST               2 ('Any')

102           LOAD_CONST               3 ('return')

104           LOAD_CONST               4 ('bool')

102           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object email_forwarder_secret_encryption_enabled at 0x0000018C17F01460, file "app\services\ingestion\email_forwarder_secret_store.py", line 102>:
102           RESUME                   0

126           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       34 (to L2)
              NOT_TAKEN

127           LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)

128           LOAD_CONST               1 ('email_forwarder_secret_encryption_enabled')

127           CALL                     1
              STORE_FAST               1 (explicit)

130           LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               2 (True)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN

131           LOAD_CONST               2 (True)
              RETURN_VALUE

132   L1:     LOAD_FAST_BORROW         1 (explicit)
              LOAD_CONST               3 (False)
              IS_OP                    0 (is)
              POP_JUMP_IF_FALSE        3 (to L2)
              NOT_TAKEN

133           LOAD_CONST               3 (False)
              RETURN_VALUE

134   L2:     LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_GLOBAL             10 (_ENV_ENCRYPTION_FLAG)
              CALL                     1
              STORE_FAST               2 (raw)

135           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL             12 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       42 (to L3)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR               15 (strip + NULL|self)
              CALL                     0
              LOAD_ATTR               17 (lower + NULL|self)
              CALL                     0
              LOAD_GLOBAL             18 (_ENV_TRUE_LITERAL)
              COMPARE_OP              88 (bool(==))
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

136           LOAD_CONST               2 (True)
              RETURN_VALUE

137   L3:     LOAD_CONST               3 (False)
              RETURN_VALUE

Disassembly of <code object _load_fernet at 0x0000018C18090690, file "app\services\ingestion\email_forwarder_secret_store.py", line 144>:
 144           RESUME                   0

 150           NOP

 151   L1:     LOAD_SMALL_INT           0
               LOAD_CONST               1 (('Fernet',))
               IMPORT_NAME              0 (cryptography.fernet)
               IMPORT_FROM              1 (Fernet)
               STORE_FAST               0 (Fernet)
               POP_TOP

 152           LOAD_FAST_BORROW         0 (Fernet)
       L2:     RETURN_VALUE

  --   L3:     PUSH_EXC_INFO

 153           LOAD_GLOBAL              4 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L5)
               NOT_TAKEN
               POP_TOP

 154   L4:     POP_EXCEPT
               LOAD_CONST               2 (None)
               RETURN_VALUE

 153   L5:     RERAISE                  0

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [0]
  L3 to L4 -> L6 [1] lasti
  L5 to L6 -> L6 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA33C0, file "app\services\ingestion\email_forwarder_secret_store.py", line 161>:
161           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _kid_from_config at 0x0000018C1804C9F0, file "app\services\ingestion\email_forwarder_secret_store.py", line 161>:
161           RESUME                   0

164           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

165           LOAD_CONST               1 (None)
              RETURN_VALUE

166   L1:     LOAD_FAST_BORROW         0 (config_or_env)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('email_forwarder_secret_active_kid')
              CALL                     1
              STORE_FAST               1 (v)

167           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (v)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

168           LOAD_FAST_BORROW         1 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

169   L2:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\ingestion\email_forwarder_secret_store.py", line 172>:
172           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('config_or_env')

173           LOAD_CONST               2 ('Any')

172           LOAD_CONST               3 ('return')

174           LOAD_CONST               4 ('Optional[str]')

172           BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _resolve_active_kid at 0x0000018C17EC4280, file "app\services\ingestion\email_forwarder_secret_store.py", line 172>:
172           RESUME                   0

186           LOAD_GLOBAL              1 (_kid_from_config + NULL)
              LOAD_FAST_BORROW         0 (config_or_env)
              CALL                     1
              STORE_FAST               1 (cfg)

187           LOAD_FAST_BORROW         1 (cfg)
              TO_BOOL
              POP_JUMP_IF_FALSE       32 (to L2)
              NOT_TAKEN

188           LOAD_GLOBAL              2 (_KID_RE)
              LOAD_ATTR                5 (match + NULL|self)
              LOAD_FAST_BORROW         1 (cfg)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         1 (cfg)
              RETURN_VALUE
      L1:     LOAD_CONST               1 (None)
              RETURN_VALUE

189   L2:     LOAD_GLOBAL              6 (os)
              LOAD_ATTR                8 (environ)
              LOAD_ATTR               11 (get + NULL|self)
              LOAD_GLOBAL             12 (_ENV_ACTIVE_KID)
              CALL                     1
              STORE_FAST               2 (raw)

190           LOAD_GLOBAL             15 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (raw)
              LOAD_GLOBAL             16 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       54 (to L3)
              NOT_TAKEN

191           LOAD_FAST_BORROW         2 (raw)
              LOAD_ATTR               19 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (raw)

192           LOAD_FAST_BORROW         2 (raw)
              TO_BOOL
              POP_JUMP_IF_FALSE       30 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL              2 (_KID_RE)
              LOAD_ATTR                5 (match + NULL|self)
              LOAD_FAST_BORROW         2 (raw)
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L3)
              NOT_TAKEN

193           LOAD_FAST_BORROW         2 (raw)
              RETURN_VALUE

194   L3:     LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\ingestion\email_forwarder_secret_store.py", line 197>:
197           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kid')

198           LOAD_CONST               2 ('Optional[str]')

197           LOAD_CONST               3 ('config_or_env')

200           LOAD_CONST               4 ('Any')

197           LOAD_CONST               5 ('return')

201           LOAD_CONST               6 ('Optional[bytes]')

197           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _key_material_for_kid at 0x0000018C17F83BE0, file "app\services\ingestion\email_forwarder_secret_store.py", line 197>:
 197            RESUME                   0

 222            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (config_or_env)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE      234 (to L6)
                NOT_TAKEN

 223            LOAD_FAST_BORROW         1 (config_or_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               1 ('email_forwarder_secret_keys')
                CALL                     1
                STORE_FAST               2 (keys_map)

 224            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (keys_map)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       98 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (kid)
                POP_JUMP_IF_NONE        94 (to L3)
                NOT_TAKEN

 225            LOAD_FAST_BORROW         2 (keys_map)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         0 (kid)
                CALL                     1
                STORE_FAST               3 (v)

 226            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (v)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (v)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L3)
                NOT_TAKEN

 227            NOP

 228    L1:     LOAD_FAST_BORROW         3 (v)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1
        L2:     RETURN_VALUE

 232    L3:     LOAD_FAST_BORROW         1 (config_or_env)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               4 ('email_forwarder_secret_fernet_key')
                CALL                     1
                STORE_FAST               4 (legacy)

 233            LOAD_FAST_BORROW         0 (kid)
                POP_JUMP_IF_NOT_NONE    77 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (legacy)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L6)
                NOT_TAKEN
                LOAD_FAST_BORROW         4 (legacy)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L6)
                NOT_TAKEN

 234            NOP

 235    L4:     LOAD_FAST_BORROW         4 (legacy)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1
        L5:     RETURN_VALUE

 240    L6:     LOAD_FAST_BORROW         0 (kid)
                POP_JUMP_IF_NONE       198 (to L11)
                NOT_TAKEN

 241            LOAD_GLOBAL             14 (_KID_RE)
                LOAD_ATTR               17 (match + NULL|self)
                LOAD_FAST_BORROW         0 (kid)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L7)
                NOT_TAKEN

 242            LOAD_CONST               2 (None)
                RETURN_VALUE

 243    L7:     LOAD_GLOBAL             18 (_ENV_PER_KID_PREFIX)
                LOAD_FAST_BORROW         0 (kid)
                LOAD_ATTR               21 (upper + NULL|self)
                CALL                     0
                LOAD_ATTR               23 (replace + NULL|self)
                LOAD_CONST               5 ('-')
                LOAD_CONST               6 ('_')
                CALL                     2
                LOAD_ATTR               23 (replace + NULL|self)
                LOAD_CONST               7 ('.')
                LOAD_CONST               6 ('_')
                CALL                     2
                BINARY_OP                0 (+)
                STORE_FAST               5 (env_name)

 244            LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (environ)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         5 (env_name)
                CALL                     1
                STORE_FAST               6 (raw)

 245            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (raw)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L10)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (raw)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L10)
                NOT_TAKEN

 246            NOP

 247    L8:     LOAD_FAST_BORROW         6 (raw)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1
        L9:     RETURN_VALUE

 250   L10:     LOAD_CONST               2 (None)
                RETURN_VALUE

 253   L11:     LOAD_GLOBAL             24 (os)
                LOAD_ATTR               26 (environ)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_GLOBAL             28 (_ENV_LEGACY_KEY)
                CALL                     1
                STORE_FAST               6 (raw)

 254            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         6 (raw)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       55 (to L14)
                NOT_TAKEN
                LOAD_FAST_BORROW         6 (raw)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       33 (to L14)
                NOT_TAKEN

 255            NOP

 256   L12:     LOAD_FAST_BORROW         6 (raw)
                LOAD_ATTR                9 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               11 (encode + NULL|self)
                LOAD_CONST               3 ('utf-8')
                CALL                     1
       L13:     RETURN_VALUE

 259   L14:     LOAD_CONST               2 (None)
                RETURN_VALUE

  --   L15:     PUSH_EXC_INFO

 229            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L17)
                NOT_TAKEN
                POP_TOP

 230   L16:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 229   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 236            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L21)
                NOT_TAKEN
                POP_TOP

 237   L20:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 236   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L23:     PUSH_EXC_INFO

 248            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L25)
                NOT_TAKEN
                POP_TOP

 249   L24:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 248   L25:     RERAISE                  0

  --   L26:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L27:     PUSH_EXC_INFO

 257            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L29)
                NOT_TAKEN
                POP_TOP

 258   L28:     POP_EXCEPT
                LOAD_CONST               2 (None)
                RETURN_VALUE

 257   L29:     RERAISE                  0

  --   L30:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L15 [0]
  L4 to L5 -> L19 [0]
  L8 to L9 -> L23 [0]
  L12 to L13 -> L27 [0]
  L15 to L16 -> L18 [1] lasti
  L17 to L18 -> L18 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L21 to L22 -> L22 [1] lasti
  L23 to L24 -> L26 [1] lasti
  L25 to L26 -> L26 [1] lasti
  L27 to L28 -> L30 [1] lasti
  L29 to L30 -> L30 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3B40, file "app\services\ingestion\email_forwarder_secret_store.py", line 262>:
262           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object redact_secret_for_log at 0x0000018C18053870, file "app\services\ingestion\email_forwarder_secret_store.py", line 262>:
262           RESUME                   0

265           LOAD_FAST_BORROW         0 (value)
              TO_BOOL
              POP_JUMP_IF_FALSE       23 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

266   L1:     LOAD_CONST               1 ('<absent>')
              RETURN_VALUE

267   L2:     LOAD_CONST               2 ('<redacted>')
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "app\services\ingestion\email_forwarder_secret_store.py", line 274>:
274           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('kid')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('token')
              LOAD_CONST               2 ('str')
              LOAD_CONST               4 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _wrap_envelope at 0x0000018C18069290, file "app\services\ingestion\email_forwarder_secret_store.py", line 274>:
274           RESUME                   0

277           LOAD_FAST_BORROW         0 (kid)
              FORMAT_SIMPLE
              LOAD_CONST               1 (':')
              LOAD_FAST_BORROW         1 (token)
              FORMAT_SIMPLE
              BUILD_STRING             3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3C30, file "app\services\ingestion\email_forwarder_secret_store.py", line 280>:
280           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('encrypted')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[Optional[str], str]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _split_envelope at 0x0000018C18048730, file "app\services\ingestion\email_forwarder_secret_store.py", line 280>:
280           RESUME                   0

285           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (encrypted)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

286           LOAD_CONST               2 ((None, ''))
              RETURN_VALUE

287   L1:     LOAD_GLOBAL              4 (_ENVELOPE_RE)
              LOAD_ATTR                7 (match + NULL|self)
              LOAD_FAST_BORROW         0 (encrypted)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              CALL                     1
              STORE_FAST               1 (m)

288           LOAD_FAST_BORROW         1 (m)
              TO_BOOL
              POP_JUMP_IF_FALSE       35 (to L2)
              NOT_TAKEN

289           LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR               11 (group + NULL|self)
              LOAD_SMALL_INT           1
              CALL                     1
              LOAD_FAST_BORROW         1 (m)
              LOAD_ATTR               11 (group + NULL|self)
              LOAD_SMALL_INT           2
              CALL                     1
              BUILD_TUPLE              2
              RETURN_VALUE

290   L2:     LOAD_CONST               1 (None)
              LOAD_FAST_BORROW         0 (encrypted)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app\services\ingestion\email_forwarder_secret_store.py", line 297>:
297           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('secret')

298           LOAD_CONST               2 ('str')

297           LOAD_CONST               3 ('key_id')

300           LOAD_CONST               4 ('Optional[str]')

297           LOAD_CONST               5 ('config_or_env')

301           LOAD_CONST               6 ('Any')

297           LOAD_CONST               7 ('return')

302           LOAD_CONST               8 ('Dict[str, Any]')

297           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object encrypt_email_forwarder_secret at 0x0000018C17F81110, file "app\services\ingestion\email_forwarder_secret_store.py", line 297>:
 297            RESUME                   0

 331            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 332            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (secret)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (secret)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L2)
                NOT_TAKEN

 334    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 335            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 336            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 337            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 338            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('missing_secret')

 333            BUILD_MAP                5
                RETURN_VALUE

 341    L2:     LOAD_GLOBAL              7 (_load_fernet + NULL)
                CALL                     0
                STORE_FAST               4 (Fernet)

 342            LOAD_FAST_BORROW         4 (Fernet)
                POP_JUMP_IF_NOT_NONE    13 (to L3)
                NOT_TAKEN

 344            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 345            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 346            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 347            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 348            LOAD_CONST               7 ('error_code')
                LOAD_CONST               9 ('crypto_unavailable')

 343            BUILD_MAP                5
                RETURN_VALUE

 352    L3:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (key_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (key_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (key_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               4 (None)
        L5:     STORE_FAST               5 (kid)

 353            LOAD_FAST_BORROW         5 (kid)
                POP_JUMP_IF_NOT_NONE    12 (to L6)
                NOT_TAKEN

 354            LOAD_GLOBAL              9 (_resolve_active_kid + NULL)
                LOAD_FAST_BORROW         2 (config_or_env)
                CALL                     1
                STORE_FAST               5 (kid)

 355    L6:     LOAD_FAST_BORROW         5 (kid)
                POP_JUMP_IF_NOT_NONE    13 (to L7)
                NOT_TAKEN

 357            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 358            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 359            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 360            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 361            LOAD_CONST               7 ('error_code')
                LOAD_CONST              10 ('missing_active_kid')

 356            BUILD_MAP                5
                RETURN_VALUE

 363    L7:     LOAD_GLOBAL             10 (_KID_RE)
                LOAD_ATTR               13 (match + NULL|self)
                LOAD_FAST_BORROW         5 (kid)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L8)
                NOT_TAKEN

 365            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 366            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 367            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 368            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 369            LOAD_CONST               7 ('error_code')
                LOAD_CONST              11 ('invalid_kid')

 364            BUILD_MAP                5
                RETURN_VALUE

 372    L8:     LOAD_GLOBAL             15 (_key_material_for_kid + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 82 (kid, config_or_env)
                LOAD_CONST              12 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST               6 (key_bytes)

 373            LOAD_FAST_BORROW         6 (key_bytes)
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L9)
                NOT_TAKEN

 375            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 376            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 377            LOAD_CONST               5 ('key_id')
                LOAD_FAST_BORROW         5 (kid)

 378            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 379            LOAD_CONST               7 ('error_code')
                LOAD_CONST              13 ('crypto_key_missing')

 374            BUILD_MAP                5
                RETURN_VALUE

 382    L9:     NOP

 383   L10:     LOAD_FAST_BORROW         4 (Fernet)
                PUSH_NULL
                LOAD_FAST_BORROW         6 (key_bytes)
                CALL                     1
                STORE_FAST               7 (f)

 384            LOAD_FAST_BORROW         7 (f)
                LOAD_ATTR               17 (encrypt + NULL|self)
                LOAD_FAST_BORROW         0 (secret)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                LOAD_ATTR               19 (encode + NULL|self)
                LOAD_CONST              14 ('utf-8')
                CALL                     1
                CALL                     1
                LOAD_ATTR               21 (decode + NULL|self)
                LOAD_CONST              14 ('utf-8')
                CALL                     1
                STORE_FAST               8 (token)

 399   L11:     LOAD_CONST               1 ('status')
                LOAD_CONST              17 ('ok')

 400            LOAD_CONST               3 ('encrypted')
                LOAD_GLOBAL             33 (_wrap_envelope + NULL)
                LOAD_FAST_LOAD_FAST     88 (kid, token)
                CALL                     2

 401            LOAD_CONST               5 ('key_id')
                LOAD_FAST                5 (kid)

 402            LOAD_CONST               6 ('warnings')
                LOAD_FAST                3 (warnings)

 403            LOAD_CONST               7 ('error_code')
                LOAD_CONST               4 (None)

 398            BUILD_MAP                5
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 385            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       88 (to L17)
                NOT_TAKEN
                STORE_FAST               9 (e)

 386   L13:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 387            LOAD_CONST              15 ('encrypt_email_forwarder_secret unexpected error type=')

 388            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 387            BUILD_STRING             2

 386            CALL                     1
                POP_TOP

 391            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 392            LOAD_CONST               3 ('encrypted')
                LOAD_CONST               4 (None)

 393            LOAD_CONST               5 ('key_id')
                LOAD_FAST                5 (kid)

 394            LOAD_CONST               6 ('warnings')
                LOAD_FAST                3 (warnings)

 395            LOAD_CONST               7 ('error_code')
                LOAD_CONST              16 ('crypto_error:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 390            BUILD_MAP                5
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               4 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 385   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L10 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025330, file "app\services\ingestion\email_forwarder_secret_store.py", line 407>:
407           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('encrypted')

408           LOAD_CONST               2 ('str')

407           LOAD_CONST               3 ('key_id')

410           LOAD_CONST               4 ('Optional[str]')

407           LOAD_CONST               5 ('config_or_env')

411           LOAD_CONST               6 ('Any')

407           LOAD_CONST               7 ('return')

412           LOAD_CONST               8 ('Dict[str, Any]')

407           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object decrypt_email_forwarder_secret at 0x0000018C17D457A0, file "app\services\ingestion\email_forwarder_secret_store.py", line 407>:
 407            RESUME                   0

 444            BUILD_LIST               0
                STORE_FAST               3 (warnings)

 445            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (encrypted)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (encrypted)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L2)
                NOT_TAKEN

 447    L1:     LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 448            LOAD_CONST               3 ('secret')
                LOAD_CONST               4 (None)

 449            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 450            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 451            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('missing_encrypted')

 446            BUILD_MAP                5
                RETURN_VALUE

 454    L2:     LOAD_GLOBAL              7 (_load_fernet + NULL)
                CALL                     0
                STORE_FAST               4 (Fernet)

 455            LOAD_FAST_BORROW         4 (Fernet)
                POP_JUMP_IF_NOT_NONE    13 (to L3)
                NOT_TAKEN

 457            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 458            LOAD_CONST               3 ('secret')
                LOAD_CONST               4 (None)

 459            LOAD_CONST               5 ('key_id')
                LOAD_CONST               4 (None)

 460            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 461            LOAD_CONST               7 ('error_code')
                LOAD_CONST               9 ('crypto_unavailable')

 456            BUILD_MAP                5
                RETURN_VALUE

 464    L3:     LOAD_GLOBAL              9 (_split_envelope + NULL)
                LOAD_FAST_BORROW         0 (encrypted)
                CALL                     1
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   86 (embedded_kid, token)

 465            LOAD_FAST                5 (embedded_kid)
                STORE_FAST               7 (effective_kid)

 466            LOAD_FAST_BORROW         7 (effective_kid)
                POP_JUMP_IF_NOT_NONE    61 (to L4)
                NOT_TAKEN

 468            LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (key_id)
                LOAD_GLOBAL              2 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       39 (to L4)
                NOT_TAKEN
                LOAD_FAST_BORROW         1 (key_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN

 469            LOAD_FAST_BORROW         1 (key_id)
                LOAD_ATTR                5 (strip + NULL|self)
                CALL                     0
                STORE_FAST               7 (effective_kid)

 471    L4:     LOAD_GLOBAL             11 (_key_material_for_kid + NULL)

 472            LOAD_FAST_BORROW_LOAD_FAST_BORROW 114 (effective_kid, config_or_env)

 471            LOAD_CONST              10 (('config_or_env',))
                CALL_KW                  2
                STORE_FAST               8 (key_bytes)

 474            LOAD_FAST_BORROW         8 (key_bytes)
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L5)
                NOT_TAKEN

 476            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 477            LOAD_CONST               3 ('secret')
                LOAD_CONST               4 (None)

 478            LOAD_CONST               5 ('key_id')
                LOAD_FAST_BORROW         7 (effective_kid)

 479            LOAD_CONST               6 ('warnings')
                LOAD_FAST_BORROW         3 (warnings)

 480            LOAD_CONST               7 ('error_code')
                LOAD_CONST              11 ('crypto_key_missing')

 475            BUILD_MAP                5
                RETURN_VALUE

 483    L5:     NOP

 484    L6:     LOAD_FAST_BORROW         4 (Fernet)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (key_bytes)
                CALL                     1
                STORE_FAST               9 (f)

 485            LOAD_FAST_BORROW         9 (f)
                LOAD_ATTR               13 (decrypt + NULL|self)
                LOAD_FAST_BORROW         6 (token)
                LOAD_ATTR               15 (encode + NULL|self)
                LOAD_CONST              12 ('utf-8')
                CALL                     1
                CALL                     1
                STORE_FAST              10 (plain)

 499    L7:     NOP

 500    L8:     LOAD_FAST               10 (plain)
                LOAD_ATTR               27 (decode + NULL|self)
                LOAD_CONST              12 ('utf-8')
                CALL                     1
                STORE_FAST              12 (decoded)

 511    L9:     LOAD_CONST               1 ('status')
                LOAD_CONST              15 ('ok')

 512            LOAD_CONST               3 ('secret')
                LOAD_FAST               12 (decoded)

 513            LOAD_CONST               5 ('key_id')
                LOAD_FAST                7 (effective_kid)

 514            LOAD_CONST               6 ('warnings')
                LOAD_FAST                3 (warnings)

 515            LOAD_CONST               7 ('error_code')
                LOAD_CONST               4 (None)

 510            BUILD_MAP                5
                RETURN_VALUE

  --   L10:     PUSH_EXC_INFO

 486            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       66 (to L15)
                NOT_TAKEN
                STORE_FAST              11 (e)

 487   L11:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 488            LOAD_CONST              13 ('decrypt_email_forwarder_secret failed type=')

 489            LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST               11 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE

 488            BUILD_STRING             2

 487            CALL                     1
                POP_TOP

 492            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 493            LOAD_CONST               3 ('secret')
                LOAD_CONST               4 (None)

 494            LOAD_CONST               5 ('key_id')
                LOAD_FAST                7 (effective_kid)

 495            LOAD_CONST               6 ('warnings')
                LOAD_FAST                3 (warnings)

 496            LOAD_CONST               7 ('error_code')
                LOAD_CONST              14 ('forwarder_secret_decrypt_failed')

 491            BUILD_MAP                5
       L12:     SWAP                     2
       L13:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RETURN_VALUE

  --   L14:     LOAD_CONST               4 (None)
                STORE_FAST              11 (e)
                DELETE_FAST             11 (e)
                RERAISE                  1

 486   L15:     RERAISE                  0

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L17:     PUSH_EXC_INFO

 501            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       16 (to L19)
                NOT_TAKEN
                POP_TOP

 503            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 504            LOAD_CONST               3 ('secret')
                LOAD_CONST               4 (None)

 505            LOAD_CONST               5 ('key_id')
                LOAD_FAST                7 (effective_kid)

 506            LOAD_CONST               6 ('warnings')
                LOAD_FAST                3 (warnings)

 507            LOAD_CONST               7 ('error_code')
                LOAD_CONST              14 ('forwarder_secret_decrypt_failed')

 502            BUILD_MAP                5
                SWAP                     2
       L18:     POP_EXCEPT
                RETURN_VALUE

 501   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L10 [0]
  L8 to L9 -> L17 [0]
  L10 to L11 -> L16 [1] lasti
  L11 to L12 -> L14 [1] lasti
  L12 to L13 -> L16 [1] lasti
  L14 to L16 -> L16 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L19 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app\services\ingestion\email_forwarder_secret_store.py", line 523>:
523           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('field')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Optional[str]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _probe_field at 0x0000018C17ED54B0, file "app\services\ingestion\email_forwarder_secret_store.py", line 523>:
523           RESUME                   0

527           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (brokerage)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

528           LOAD_CONST               1 (None)
              RETURN_VALUE

529   L1:     LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         1 (field)
              CALL                     1
              STORE_FAST               2 (top)

530           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (top)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       39 (to L2)
              NOT_TAKEN
              LOAD_FAST_BORROW         2 (top)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_FALSE       17 (to L2)
              NOT_TAKEN

531           LOAD_FAST_BORROW         2 (top)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              RETURN_VALUE

532   L2:     LOAD_GLOBAL             10 (_NEST_KEYS)
              GET_ITER
      L3:     FOR_ITER               125 (to L7)
              STORE_FAST               3 (holder_key)

533           LOAD_FAST_BORROW         0 (brokerage)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         3 (holder_key)
              CALL                     1
              STORE_FAST               4 (holder)

534           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         4 (holder)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           44 (to L3)

535   L4:     LOAD_FAST_BORROW         4 (holder)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         1 (field)
              CALL                     1
              STORE_FAST               5 (v)

536           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         5 (v)
              LOAD_GLOBAL              6 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           85 (to L3)
      L5:     LOAD_FAST_BORROW         5 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD          109 (to L3)

537   L6:     LOAD_FAST_BORROW         5 (v)
              LOAD_ATTR                9 (strip + NULL|self)
              CALL                     0
              SWAP                     2
              POP_TOP
              RETURN_VALUE

532   L7:     END_FOR
              POP_ITER

538           LOAD_CONST               1 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\ingestion\email_forwarder_secret_store.py", line 541>:
541           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage')

542           LOAD_CONST               2 ('Optional[Dict[str, Any]]')

541           LOAD_CONST               3 ('config_or_env')

544           LOAD_CONST               4 ('Any')

541           LOAD_CONST               5 ('return')

545           LOAD_CONST               6 ('Dict[str, Any]')

541           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_email_forwarder_secret at 0x0000018C17F841C0, file "app\services\ingestion\email_forwarder_secret_store.py", line 541>:
541            RESUME                   0

578            LOAD_GLOBAL              1 (email_forwarder_secret_encryption_enabled + NULL)

579            LOAD_FAST_BORROW         1 (config_or_env)
               POP_JUMP_IF_NONE         3 (to L1)
               NOT_TAKEN
               LOAD_FAST                1 (config_or_env)
               JUMP_FORWARD             1 (to L2)
       L1:     LOAD_FAST                0 (brokerage)

578    L2:     CALL                     1
               STORE_FAST               2 (encryption_enabled)

582            LOAD_GLOBAL              3 (_probe_field + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL              4 (_PLAINTEXT_FIELD)
               CALL                     2
               STORE_FAST               3 (plaintext)

583            LOAD_GLOBAL              3 (_probe_field + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL              6 (_ENCRYPTED_FIELD)
               CALL                     2
               STORE_FAST               4 (encrypted)

584            LOAD_GLOBAL              3 (_probe_field + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL              8 (_KEY_ID_FIELD)
               CALL                     2
               STORE_FAST               5 (row_kid)

585            LOAD_GLOBAL              3 (_probe_field + NULL)
               LOAD_FAST_BORROW         0 (brokerage)
               LOAD_GLOBAL             10 (_MIGRATION_STATUS_FIELD)
               CALL                     2
               STORE_FAST               6 (migration_status)

587            BUILD_LIST               0
               STORE_FAST               7 (warnings)

589            LOAD_FAST_BORROW         2 (encryption_enabled)
               TO_BOOL
               POP_JUMP_IF_TRUE        41 (to L4)
               NOT_TAKEN

590            LOAD_FAST_BORROW         3 (plaintext)
               TO_BOOL
               POP_JUMP_IF_FALSE       17 (to L3)
               NOT_TAKEN

592            LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('ok')

593            LOAD_CONST               4 ('secret')
               LOAD_FAST_BORROW         3 (plaintext)

594            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST               6 (False)

595            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST               6 (False)

596            LOAD_CONST               8 ('migration_status')
               LOAD_FAST_BORROW         6 (migration_status)

597            LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         7 (warnings)

598            LOAD_CONST              10 ('error_code')
               LOAD_CONST               1 (None)

591            BUILD_MAP                7
               RETURN_VALUE

601    L3:     LOAD_CONST               2 ('status')
               LOAD_CONST              11 ('missing')

602            LOAD_CONST               4 ('secret')
               LOAD_CONST               1 (None)

603            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST               6 (False)

604            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST               6 (False)

605            LOAD_CONST               8 ('migration_status')
               LOAD_FAST_BORROW         6 (migration_status)

606            LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         7 (warnings)

607            LOAD_CONST              10 ('error_code')
               LOAD_CONST               1 (None)

600            BUILD_MAP                7
               RETURN_VALUE

611    L4:     LOAD_FAST_BORROW         4 (encrypted)
               TO_BOOL
               POP_JUMP_IF_FALSE      149 (to L10)
               NOT_TAKEN

612            LOAD_GLOBAL             13 (decrypt_email_forwarder_secret + NULL)

613            LOAD_FAST                4 (encrypted)

614            LOAD_FAST                5 (row_kid)

615            LOAD_FAST_BORROW         1 (config_or_env)
               POP_JUMP_IF_NONE         3 (to L5)
               NOT_TAKEN
               LOAD_FAST                1 (config_or_env)
               JUMP_FORWARD             1 (to L6)
       L5:     LOAD_FAST                0 (brokerage)

612    L6:     LOAD_CONST              12 (('key_id', 'config_or_env'))
               CALL_KW                  3
               STORE_FAST               8 (decrypted)

617            LOAD_FAST_BORROW         8 (decrypted)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST               2 ('status')
               CALL                     1
               LOAD_CONST               3 ('ok')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       32 (to L7)
               NOT_TAKEN

619            LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('ok')

620            LOAD_CONST               4 ('secret')
               LOAD_FAST_BORROW         8 (decrypted)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST               4 ('secret')
               CALL                     1

621            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST              13 (True)

622            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST               6 (False)

623            LOAD_CONST               8 ('migration_status')
               LOAD_FAST_BORROW         6 (migration_status)

624            LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         7 (warnings)

625            LOAD_CONST              10 ('error_code')
               LOAD_CONST               1 (None)

618            BUILD_MAP                7
               RETURN_VALUE

628    L7:     LOAD_CONST               2 ('status')
               LOAD_CONST              14 ('failed')

629            LOAD_CONST               4 ('secret')
               LOAD_CONST               1 (None)

630            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST              13 (True)

631            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST               6 (False)

632            LOAD_CONST               8 ('migration_status')
               LOAD_FAST                6 (migration_status)

633            LOAD_CONST               9 ('warnings')
               LOAD_GLOBAL             17 (list + NULL)
               LOAD_FAST_BORROW         8 (decrypted)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST               9 ('warnings')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L8)
               NOT_TAKEN
               POP_TOP
               BUILD_LIST               0
       L8:     CALL                     1

634            LOAD_CONST              10 ('error_code')
               LOAD_FAST_BORROW         8 (decrypted)
               LOAD_ATTR               15 (get + NULL|self)
               LOAD_CONST              10 ('error_code')
               CALL                     1
               COPY                     1
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L9)
               NOT_TAKEN
               POP_TOP

635            LOAD_CONST              15 ('forwarder_secret_decrypt_failed')

627    L9:     BUILD_MAP                7
               RETURN_VALUE

638   L10:     LOAD_FAST_BORROW         3 (plaintext)
               TO_BOOL
               POP_JUMP_IF_FALSE       34 (to L11)
               NOT_TAKEN

639            LOAD_FAST_BORROW         7 (warnings)
               LOAD_ATTR               19 (append + NULL|self)
               LOAD_CONST              16 ('plaintext_forwarder_secret_fallback')
               CALL                     1
               POP_TOP

641            LOAD_CONST               2 ('status')
               LOAD_CONST               3 ('ok')

642            LOAD_CONST               4 ('secret')
               LOAD_FAST_BORROW         3 (plaintext)

643            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST              13 (True)

644            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST              13 (True)

645            LOAD_CONST               8 ('migration_status')
               LOAD_FAST_BORROW         6 (migration_status)

646            LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         7 (warnings)

647            LOAD_CONST              10 ('error_code')
               LOAD_CONST               1 (None)

640            BUILD_MAP                7
               RETURN_VALUE

651   L11:     LOAD_CONST               2 ('status')
               LOAD_CONST              11 ('missing')

652            LOAD_CONST               4 ('secret')
               LOAD_CONST               1 (None)

653            LOAD_CONST               5 ('encryption_enabled')
               LOAD_CONST              13 (True)

654            LOAD_CONST               7 ('plaintext_fallback')
               LOAD_CONST               6 (False)

655            LOAD_CONST               8 ('migration_status')
               LOAD_FAST_BORROW         6 (migration_status)

656            LOAD_CONST               9 ('warnings')
               LOAD_FAST_BORROW         7 (warnings)

657            LOAD_CONST              10 ('error_code')
               LOAD_CONST               1 (None)

650            BUILD_MAP                7
               RETURN_VALUE
```
