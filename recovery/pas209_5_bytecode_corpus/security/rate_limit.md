# security/rate_limit

- **pyc:** `app\services\security\__pycache__\rate_limit.cpython-314.pyc`
- **expected source path (absent):** `app\services\security/rate_limit.py`
- **co_filename (from bytecode):** `app/services/security/rate_limit.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** security

## Module docstring

```
PAS-SECURITY-02 — Per-tenant / per-surface rate limit service.

Wraps :mod:`app.services.security.rate_limit_store` with a
closed policy table, deterministic bucket-key construction,
and a structural 429-style envelope helper. Replaces the
PAS-SECURITY-01 in-process IP-based limiter for surfaces
where the counter MUST be brokerage-scoped and survive
process restarts.

Doctrine:

* **Conservative defaults.** Sensitive surfaces get
  tight defaults. Operators can tune later via config; PAS-
  SECURITY-02 hard-codes a safe baseline.
* **Tenant / brokerage scoped where possible.** When the
  caller is authenticated, the bucket is keyed on
  ``brokerage_id``. Pre-auth surfaces fall back to an
  anonymised actor fingerprint (sha256 of the bounded IP
  string passed in by the caller — the raw IP is NEVER
  stored).
* **No raw IP / user-agent / API key / signature** stored or
  returned. The bucket key + actor_id fields are sha256
  fingerprints.
* **Structural 429-style envelope.** Routes return the closed
  envelope produced by ``rate_limit_public_error(...)`` —
  never the raw policy or the raw bucket key.
* **NEVER raises.** All helpers return structural envelopes.
* **Failure isolation.** Counter store errors do NOT block
  the caller; ``check_rate_limit`` falls back to
  ``allowed=True`` with a structural warning so production
  traffic is never deadlocked by a limiter outage.

Public surface:

  * ``ALLOWED_SURFACES``                     — closed enum.
  * ``DEFAULT_POLICIES``                     — surface → policy map.
  * ``build_rate_limit_bucket_key(...)``    — deterministic.
  * ``resolve_rate_limit_policy(surface)``  — closed lookup.
  * ``check_rate_limit(...)``               — verdict envelope.
  * ``record_rate_limit_hit(...)``          — thin wrapper.
  * ``rate_limit_report(...)``              — bounded read.
  * ``rate_limit_public_error(envelope)``   — 429-style public envelope.
```

## Imports

`Any`, `Dict`, `List`, `Optional`, `Tuple`, `_STRUCTURAL_COLUMNS`, `__future__`, `annotations`, `app.db.supabase_client`, `app.services.security.rate_limit_store`, `datetime`, `get_supabase`, `hashlib`, `increment_counter`, `json`, `logging`, `timedelta`, `timezone`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_bound_str`, `_iso`, `_now_dt`, `_safe_verdict`, `_sha256_hex`, `_window_for`, `build_rate_limit_bucket_key`, `check_rate_limit`, `rate_limit_public_error`, `rate_limit_report`, `record_rate_limit_hit`, `resolve_rate_limit_policy`

## Env-key candidates

`ALLOWED_ACTOR_TYPES`, `ALLOWED_SURFACES`, `ANON`, `DEFAULT_POLICIES`

## String constants (redacted where noted)

- '\nPAS-SECURITY-02 — Per-tenant / per-surface rate limit service.\n\nWraps :mod:`app.services.security.rate_limit_store` with a\nclosed policy table, deterministic bucket-key construction,\nand a structural 429-style envelope helper. Replaces the\nPAS-SECURITY-01 in-process IP-based limiter for surfaces\nwhere the counter MUST be brokerage-scoped and survive\nprocess restarts.\n\nDoctrine:\n\n* **Conservative defaults.** Sensitive surfaces get\n  tight defaults. Operators can tune later via config; PAS-\n  SECURITY-02 hard-codes a safe baseline.\n* **Tenant / brokerage scoped where possible.** When the\n  caller is authenticated, the bucket is keyed on\n  ``brokerage_id``. Pre-auth surfaces fall back to an\n  anonymised actor fingerprint (sha256 of the bounded IP\n  string passed in by the caller — the raw IP is NEVER\n  stored).\n* **No raw IP / user-agent / API key / signature** stored or\n  returned. The bucket key + actor_id fields are sha256\n  fingerprints.\n* **Structural 429-style envelope.** Routes return the closed\n  envelope produced by ``rate_limit_public_error(...)`` —\n  never the raw policy or the raw bucket key.\n* **NEVER raises.** All helpers return structural envelopes.\n* **Failure isolation.** Counter store errors do NOT block\n  the caller; ``check_rate_limit`` falls back to\n  ``allowed=True`` with a structural warning so production\n  traffic is never deadlocked by a limiter outage.\n\nPublic surface:\n\n  * ``ALLOWED_SURFACES``                     — closed enum.\n  * ``DEFAULT_POLICIES``                     — surface → policy map.\n  * ``build_rate_limit_bucket_key(...)``    — deterministic.\n  * ``resolve_rate_limit_policy(surface)``  — closed lookup.\n  * ``check_rate_limit(...)``               — verdict envelope.\n  * ``record_rate_limit_hit(...)``          — thin wrapper.\n  * ``rate_limit_report(...)``              — bounded read.\n  * ``rate_limit_public_error(envelope)``   — 429-style public envelope.\n'
- 'pas.security.rate_limit'
- 'email_ingestion'
- 'slack_command'
- 'admin'
- 'tenant_api'
- 'api_key_rotation'
- 'webhook_generic'
- 'webhook_followupboss'
- 'webhook_gohighlevel'
- 'webhook_zapier'
- 'Tuple[str, ...]'
- 'ALLOWED_SURFACES'
- 'ALLOWED_ACTOR_TYPES'
- 'max_requests'
- 'window_seconds'
- 'Dict[str, Dict[str, int]]'
- 'DEFAULT_POLICIES'
- 'brokerage_id'
- 'actor_type'
- 'actor_token'
- 'window_start'
- 'backend'
- 'bucket_key'
- 'request_count'
- 'blocked_count'
- 'limit'
- 'window_end'
- 'retry_after_seconds'
- 'warnings'
- 'error_code'
- 'now'
- 'blocked'
- 'surface'
- 'return'
- 'datetime'
- 'str'
- 'seconds'
- 'value'
- 'Any'
- 'max_len'
- 'int'
- 'Optional[str]'
- 'utf-8'
- 'Optional[datetime]'
- 'Tuple[datetime, datetime]'
- 'Compute the canonical window for the given epoch slice.\nBuckets are aligned to ``window_seconds`` boundaries so\nthat a single counter row covers each tenant-window pair.'
- 'Deterministic sha256 hex key over (surface,\nbrokerage_id_or_anon, actor_token, window_start_iso).\nNEVER raises. Returns None on invalid input.'
- 'anon'
- 'ANON'
- 'actor_fp'
- 'build_rate_limit_bucket_key error type='
- 'Dict[str, Any]'
- 'Return the closed policy for a surface. NEVER raises.\nUnknown surface → status="failed".'
- 'status'
- 'failed'
- 'policy'
- 'invalid_surface'
- 'allowed'
- 'bool'
- 'Optional[int]'
- 'Optional[List[str]]'
- 'Atomically increment + check the rate-limit counter\nfor the (surface, brokerage_id, actor_token) bucket.\nNEVER raises.\n\nReturns:\n  * ``allowed=True``  — request is under the policy cap.\n  * ``allowed=False`` — request would exceed the cap; the\n    caller should return a 429-style response via\n    ``rate_limit_public_error(...)``.\n\nOn counter-store failure, the verdict ALWAYS returns\n``allowed=True`` with a structural warning. PAS-SECURITY-02\ninvariant: a limiter outage MUST NOT deadlock production\ntraffic. Operators are expected to monitor the rate-limit\naudit events out-of-band.\n'
- 'rate_limit_invalid_surface'
- 'rate_limit_bucket_key_failed'
- 'bucket_key_failed'
- 'event'
- 'security.rate_limit.allowed'
- 'check_rate_limit increment error type='
- 'rate_limit_store_unexpected:'
- 'rate_limit_store_unexpected'
- 'counter'
- 'rate_limit_store_unavailable'
- 'security.rate_limit.blocked'
- 'check_rate_limit blocked-increment error type='
- 'Thin wrapper used when a caller wants to record a hit\nwithout consulting the policy (e.g. to record an\nout-of-band external block). NEVER raises.'
- 'record_rate_limit_hit error type='
- 'rate_limit_unexpected:'
- 'unexpected:'
- 'Bounded read of the rate-limit counter table. NEVER\nraises. NEVER returns PII / raw IP / raw key.'
- 'rows'
- 'count'
- 'rate_limit_report db client unavailable type='
- 'skipped'
- 'pas_rate_limit_counters'
- 'data'
- 'rate_limit_report read error type='
- 'db_read_failed:'
- 'verdict'
- 'Return the closed-shape 429-style public envelope from\na ``check_rate_limit`` verdict. NEVER raises. NEVER\ncarries the bucket key / actor fingerprint / raw IP.'
- 'rate_limit_exceeded'
- 'rate_limit_public_error error type='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS-SECURITY-02 — Per-tenant / per-surface rate limit service.\n\nWraps :mod:`app.services.security.rate_limit_store` with a\nclosed policy table, deterministic bucket-key construction,\nand a structural 429-style envelope helper. Replaces the\nPAS-SECURITY-01 in-process IP-based limiter for surfaces\nwhere the counter MUST be brokerage-scoped and survive\nprocess restarts.\n\nDoctrine:\n\n* **Conservative defaults.** Sensitive surfaces get\n  tight defaults. Operators can tune later via config; PAS-\n  SECURITY-02 hard-codes a safe baseline.\n* **Tenant / brokerage scoped where possible.** When the\n  caller is authenticated, the bucket is keyed on\n  ``brokerage_id``. Pre-auth surfaces fall back to an\n  anonymised actor fingerprint (sha256 of the bounded IP\n  string passed in by the caller — the raw IP is NEVER\n  stored).\n* **No raw IP / user-agent / API key / signature** stored or\n  returned. The bucket key + actor_id fields are sha256\n  fingerprints.\n* **Structural 429-style envelope.** Routes return the closed\n  envelope produced by ``rate_limit_public_error(...)`` —\n  never the raw policy or the raw bucket key.\n* **NEVER raises.** All helpers return structural envelopes.\n* **Failure isolation.** Counter store errors do NOT block\n  the caller; ``check_rate_limit`` falls back to\n  ``allowed=True`` with a structural warning so production\n  traffic is never deadlocked by a limiter outage.\n\nPublic surface:\n\n  * ``ALLOWED_SURFACES``                     — closed enum.\n  * ``DEFAULT_POLICIES``                     — surface → policy map.\n  * ``build_rate_limit_bucket_key(...)``    — deterministic.\n  * ``resolve_rate_limit_policy(surface)``  — closed lookup.\n  * ``check_rate_limit(...)``               — verdict envelope.\n  * ``record_rate_limit_hit(...)``          — thin wrapper.\n  * ``rate_limit_report(...)``              — bounded read.\n  * ``rate_limit_public_error(envelope)``   — 429-style public envelope.\n')
               STORE_NAME               1 (__doc__)

  46           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  48           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (hashlib)
               STORE_NAME               4 (hashlib)

  49           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (json)
               STORE_NAME               5 (json)

  50           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              6 (logging)
               STORE_NAME               6 (logging)

  51           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('datetime', 'timedelta', 'timezone'))
               IMPORT_NAME              7 (datetime)
               IMPORT_FROM              7 (datetime)
               STORE_NAME               7 (datetime)
               IMPORT_FROM              8 (timedelta)
               STORE_NAME               8 (timedelta)
               IMPORT_FROM              9 (timezone)
               STORE_NAME               9 (timezone)
               POP_TOP

  52           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Dict', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME             10 (typing)
               IMPORT_FROM             11 (Any)
               STORE_NAME              11 (Any)
               IMPORT_FROM             12 (Dict)
               STORE_NAME              12 (Dict)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               IMPORT_FROM             15 (Tuple)
               STORE_NAME              15 (Tuple)
               POP_TOP

  55           LOAD_NAME                6 (logging)
               LOAD_ATTR               32 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.security.rate_limit')
               CALL                     1
               STORE_NAME              17 (logger)

  59           LOAD_CONST              65 (('email_ingestion', 'slack_command', 'admin', 'tenant_api', 'api_key_rotation', 'webhook_generic', 'webhook_followupboss', 'webhook_gohighlevel', 'webhook_zapier'))
               STORE_NAME              18 (ALLOWED_SURFACES)
               LOAD_CONST              15 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              16 ('ALLOWED_SURFACES')
               STORE_SUBSCR

  73           LOAD_CONST              66 (('TENANT', 'OPERATOR', 'ADMIN', 'SYSTEM', 'ANON'))
               STORE_NAME              20 (ALLOWED_ACTOR_TYPES)
               LOAD_CONST              15 ('Tuple[str, ...]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              17 ('ALLOWED_ACTOR_TYPES')
               STORE_SUBSCR

  83           LOAD_CONST               6 ('email_ingestion')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  84           LOAD_CONST               7 ('slack_command')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          30
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  85           LOAD_CONST               8 ('admin')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  86           LOAD_CONST               9 ('tenant_api')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT         120
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  87           LOAD_CONST              10 ('api_key_rotation')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT           3
               LOAD_CONST              19 ('window_seconds')
               LOAD_CONST              20 (3600)
               BUILD_MAP                2

  88           LOAD_CONST              11 ('webhook_generic')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  89           LOAD_CONST              12 ('webhook_followupboss')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  90           LOAD_CONST              13 ('webhook_gohighlevel')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  91           LOAD_CONST              14 ('webhook_zapier')
               LOAD_CONST              18 ('max_requests')
               LOAD_SMALL_INT          60
               LOAD_CONST              19 ('window_seconds')
               LOAD_SMALL_INT          60
               BUILD_MAP                2

  82           BUILD_MAP                9
               STORE_NAME              21 (DEFAULT_POLICIES)
               LOAD_CONST              21 ('Dict[str, Dict[str, int]]')
               LOAD_NAME               19 (__annotations__)
               LOAD_CONST              22 ('DEFAULT_POLICIES')
               STORE_SUBSCR

  95           LOAD_SMALL_INT         200
               STORE_NAME              22 (_BROKERAGE_ID_MAX_LEN)

  96           LOAD_SMALL_INT         200
               STORE_NAME              23 (_ACTOR_TOKEN_MAX_LEN)

  97           LOAD_SMALL_INT          64
               STORE_NAME              24 (_ACTOR_FINGERPRINT_BYTES)

  98           LOAD_CONST              23 (500)
               STORE_NAME              25 (_LIST_HARD_CAP)

  99           LOAD_SMALL_INT          50
               STORE_NAME              26 (_DEFAULT_LIMIT)

 102           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/rate_limit.py", line 102>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _now_dt at 0x0000018C18053870, file "app/services/security/rate_limit.py", line 102>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              27 (_now_dt)

 106           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/rate_limit.py", line 106>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _iso at 0x0000018C18026430, file "app/services/security/rate_limit.py", line 106>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              28 (_iso)

 110           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18025730, file "app/services/security/rate_limit.py", line 110>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _bound_str at 0x0000018C17972550, file "app/services/security/rate_limit.py", line 110>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              29 (_bound_str)

 119           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/rate_limit.py", line 119>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _sha256_hex at 0x0000018C18038A30, file "app/services/security/rate_limit.py", line 119>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              30 (_sha256_hex)

 123           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C18025F30, file "app/services/security/rate_limit.py", line 123>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _window_for at 0x0000018C1794EF50, file "app/services/security/rate_limit.py", line 123>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_window_for)

 143           LOAD_CONST              34 ('brokerage_id')

 146           LOAD_CONST               2 (None)

 143           LOAD_CONST              35 ('actor_type')

 147           LOAD_CONST               2 (None)

 143           LOAD_CONST              36 ('actor_token')

 148           LOAD_CONST               2 (None)

 143           LOAD_CONST              37 ('window_start')

 149           LOAD_CONST               2 (None)

 143           BUILD_MAP                4
               LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18025230, file "app/services/security/rate_limit.py", line 143>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object build_rate_limit_bucket_key at 0x0000018C17CD4970, file "app/services/security/rate_limit.py", line 143>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              32 (build_rate_limit_bucket_key)

 177           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/rate_limit.py", line 177>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object resolve_rate_limit_policy at 0x0000018C17FA92F0, file "app/services/security/rate_limit.py", line 177>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (resolve_rate_limit_policy)

 198           LOAD_CONST              42 ('backend')

 202           LOAD_CONST               2 (None)

 198           LOAD_CONST              43 ('bucket_key')

 203           LOAD_CONST               2 (None)

 198           LOAD_CONST              44 ('request_count')

 204           LOAD_SMALL_INT           0

 198           LOAD_CONST              45 ('blocked_count')

 205           LOAD_SMALL_INT           0

 198           LOAD_CONST              46 ('limit')

 206           LOAD_SMALL_INT           0

 198           LOAD_CONST              37 ('window_start')

 207           LOAD_CONST               2 (None)

 198           LOAD_CONST              47 ('window_end')

 208           LOAD_CONST               2 (None)

 198           LOAD_CONST              48 ('retry_after_seconds')

 209           LOAD_CONST               2 (None)

 198           LOAD_CONST              49 ('warnings')

 210           LOAD_CONST               2 (None)

 198           LOAD_CONST              50 ('error_code')

 211           LOAD_CONST               2 (None)

 198           BUILD_MAP               10
               LOAD_CONST              51 (<code object __annotate__ at 0x0000018C18053990, file "app/services/security/rate_limit.py", line 198>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object _safe_verdict at 0x0000018C17FF13B0, file "app/services/security/rate_limit.py", line 198>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              34 (_safe_verdict)

 232           LOAD_CONST              34 ('brokerage_id')

 235           LOAD_CONST               2 (None)

 232           LOAD_CONST              35 ('actor_type')

 236           LOAD_CONST               2 (None)

 232           LOAD_CONST              36 ('actor_token')

 237           LOAD_CONST               2 (None)

 232           LOAD_CONST              53 ('now')

 238           LOAD_CONST               2 (None)

 232           BUILD_MAP                4
               LOAD_CONST              54 (<code object __annotate__ at 0x0000018C18025D30, file "app/services/security/rate_limit.py", line 232>)
               MAKE_FUNCTION
               LOAD_CONST              55 (<code object check_rate_limit at 0x0000018C17ED9FB0, file "app/services/security/rate_limit.py", line 232>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              35 (check_rate_limit)

 378           LOAD_CONST              34 ('brokerage_id')

 381           LOAD_CONST               2 (None)

 378           LOAD_CONST              35 ('actor_type')

 382           LOAD_CONST               2 (None)

 378           LOAD_CONST              36 ('actor_token')

 383           LOAD_CONST               2 (None)

 378           LOAD_CONST              56 ('blocked')

 384           LOAD_CONST              57 (False)

 378           LOAD_CONST              53 ('now')

 385           LOAD_CONST               2 (None)

 378           BUILD_MAP                5
               LOAD_CONST              58 (<code object __annotate__ at 0x0000018C1812C140, file "app/services/security/rate_limit.py", line 378>)
               MAKE_FUNCTION
               LOAD_CONST              59 (<code object record_rate_limit_hit at 0x0000018C17F41160, file "app/services/security/rate_limit.py", line 378>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              36 (record_rate_limit_hit)

 452           LOAD_CONST              60 ('surface')

 454           LOAD_CONST               2 (None)

 452           LOAD_CONST              34 ('brokerage_id')

 455           LOAD_CONST               2 (None)

 452           LOAD_CONST              46 ('limit')

 456           LOAD_NAME               26 (_DEFAULT_LIMIT)

 452           BUILD_MAP                3
               LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18025E30, file "app/services/security/rate_limit.py", line 452>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object rate_limit_report at 0x0000018C17789BE0, file "app/services/security/rate_limit.py", line 452>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              37 (rate_limit_report)

 517           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/rate_limit.py", line 517>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object rate_limit_public_error at 0x0000018C17D8C220, file "app/services/security/rate_limit.py", line 517>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (rate_limit_public_error)

 552           BUILD_LIST               0
               LOAD_CONST              67 (('ALLOWED_SURFACES', 'ALLOWED_ACTOR_TYPES', 'DEFAULT_POLICIES', 'build_rate_limit_bucket_key', 'resolve_rate_limit_policy', 'check_rate_limit', 'record_rate_limit_hit', 'rate_limit_report', 'rate_limit_public_error'))
               LIST_EXTEND              1
               STORE_NAME              39 (__all__)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA21F0, file "app/services/security/rate_limit.py", line 102>:
102           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('datetime')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now_dt at 0x0000018C18053870, file "app/services/security/rate_limit.py", line 102>:
102           RESUME                   0

103           LOAD_GLOBAL              0 (datetime)
              LOAD_ATTR                2 (now)
              PUSH_NULL
              LOAD_GLOBAL              4 (timezone)
              LOAD_ATTR                6 (utc)
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2F10, file "app/services/security/rate_limit.py", line 106>:
106           RESUME                   0
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

Disassembly of <code object _iso at 0x0000018C18026430, file "app/services/security/rate_limit.py", line 106>:
106           RESUME                   0

107           LOAD_FAST_BORROW         0 (dt)
              LOAD_ATTR                1 (isoformat + NULL|self)
              LOAD_CONST               0 ('seconds')
              LOAD_CONST               1 (('timespec',))
              CALL_KW                  1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025730, file "app/services/security/rate_limit.py", line 110>:
110           RESUME                   0
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

Disassembly of <code object _bound_str at 0x0000018C17972550, file "app/services/security/rate_limit.py", line 110>:
110           RESUME                   0

111           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (value)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

112           LOAD_CONST               0 (None)
              RETURN_VALUE

113   L1:     LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               2 (s)

114           LOAD_FAST_BORROW         2 (s)
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

115   L2:     LOAD_CONST               0 (None)
              RETURN_VALUE

116   L3:     LOAD_FAST_BORROW         2 (s)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA31E0, file "app/services/security/rate_limit.py", line 119>:
119           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('value')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _sha256_hex at 0x0000018C18038A30, file "app/services/security/rate_limit.py", line 119>:
119           RESUME                   0

120           LOAD_GLOBAL              0 (hashlib)
              LOAD_ATTR                2 (sha256)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (value)
              LOAD_ATTR                5 (encode + NULL|self)
              LOAD_CONST               0 ('utf-8')
              CALL                     1
              CALL                     1
              LOAD_ATTR                7 (hexdigest + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "app/services/security/rate_limit.py", line 123>:
123           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('now')

125           LOAD_CONST               2 ('Optional[datetime]')

123           LOAD_CONST               3 ('window_seconds')

126           LOAD_CONST               4 ('int')

123           LOAD_CONST               5 ('return')

127           LOAD_CONST               6 ('Tuple[datetime, datetime]')

123           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _window_for at 0x0000018C1794EF50, file "app/services/security/rate_limit.py", line 123>:
123           RESUME                   0

131           LOAD_FAST                0 (now)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE        11 (to L1)
              NOT_TAKEN
              POP_TOP
              LOAD_GLOBAL              1 (_now_dt + NULL)
              CALL                     0
      L1:     STORE_FAST               0 (now)

132           LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         0 (now)
              LOAD_ATTR                5 (timestamp + NULL|self)
              CALL                     0
              CALL                     1
              STORE_FAST               2 (ts)

133           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (ts, window_seconds)
              BINARY_OP                2 (//)
              LOAD_FAST_BORROW         1 (window_seconds)
              BINARY_OP                5 (*)
              STORE_FAST               3 (bucket_start_ts)

134           LOAD_GLOBAL              6 (datetime)
              LOAD_ATTR                8 (fromtimestamp)
              PUSH_NULL
              LOAD_FAST_BORROW         3 (bucket_start_ts)
              LOAD_GLOBAL             10 (timezone)
              LOAD_ATTR               12 (utc)
              LOAD_CONST               1 (('tz',))
              CALL_KW                  2
              STORE_FAST               4 (start)

135           LOAD_FAST_BORROW         4 (start)
              LOAD_GLOBAL             15 (timedelta + NULL)
              LOAD_FAST_BORROW         1 (window_seconds)
              LOAD_CONST               2 (('seconds',))
              CALL_KW                  1
              BINARY_OP                0 (+)
              STORE_FAST               5 (end)

136           LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (start, end)
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025230, file "app/services/security/rate_limit.py", line 143>:
143           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

145           LOAD_CONST               2 ('str')

143           LOAD_CONST               3 ('brokerage_id')

146           LOAD_CONST               4 ('Optional[str]')

143           LOAD_CONST               5 ('actor_type')

147           LOAD_CONST               4 ('Optional[str]')

143           LOAD_CONST               6 ('actor_token')

148           LOAD_CONST               4 ('Optional[str]')

143           LOAD_CONST               7 ('window_start')

149           LOAD_CONST               4 ('Optional[str]')

143           LOAD_CONST               8 ('return')

150           LOAD_CONST               4 ('Optional[str]')

143           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object build_rate_limit_bucket_key at 0x0000018C17CD4970, file "app/services/security/rate_limit.py", line 143>:
 143            RESUME                   0

 154            LOAD_FAST_BORROW         0 (surface)
                LOAD_GLOBAL              0 (ALLOWED_SURFACES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN

 155            LOAD_CONST               1 (None)
                RETURN_VALUE

 156    L1:     LOAD_FAST_BORROW         1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L2)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_bound_str + NULL)
                LOAD_FAST_BORROW         1 (brokerage_id)
                LOAD_GLOBAL              4 (_BROKERAGE_ID_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L3)
        L2:     LOAD_CONST               1 (None)
        L3:     STORE_FAST               5 (bid)

 157            LOAD_FAST_BORROW         3 (actor_token)
                TO_BOOL
                POP_JUMP_IF_FALSE       17 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              3 (_bound_str + NULL)
                LOAD_FAST_BORROW         3 (actor_token)
                LOAD_GLOBAL              6 (_ACTOR_TOKEN_MAX_LEN)
                CALL                     2
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               1 (None)
        L5:     STORE_FAST               6 (actor)

 158            LOAD_FAST_BORROW         6 (actor)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              9 (_sha256_hex + NULL)
                LOAD_FAST_BORROW         6 (actor)
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               2 ('anon')
        L7:     STORE_FAST               7 (actor_fp)

 159            LOAD_FAST_BORROW         2 (actor_type)
                POP_JUMP_IF_NONE        14 (to L8)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (actor_type)
                LOAD_GLOBAL             10 (ALLOWED_ACTOR_TYPES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE        3 (to L8)
                NOT_TAKEN

 160            LOAD_CONST               1 (None)
                RETURN_VALUE

 161    L8:     NOP

 162    L9:     LOAD_GLOBAL             12 (json)
                LOAD_ATTR               14 (dumps)
                PUSH_NULL

 163            LOAD_CONST               3 ('surface')
                LOAD_FAST                0 (surface)

 164            LOAD_CONST               4 ('brokerage_id')
                LOAD_FAST                5 (bid)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L12)
       L10:     NOT_TAKEN
       L11:     POP_TOP
                LOAD_CONST               2 ('anon')

 165   L12:     LOAD_CONST               5 ('actor_type')
                LOAD_FAST                2 (actor_type)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
       L13:     NOT_TAKEN
       L14:     POP_TOP
                LOAD_CONST               6 ('ANON')

 166   L15:     LOAD_CONST               7 ('actor_fp')
                LOAD_FAST                7 (actor_fp)

 167            LOAD_CONST               8 ('window_start')
                LOAD_FAST                4 (window_start)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
       L16:     NOT_TAKEN
       L17:     POP_TOP
                LOAD_CONST               9 ('')

 162   L18:     BUILD_MAP                5

 168            LOAD_CONST              10 (True)
                LOAD_CONST              13 ((',', ':'))

 162            LOAD_CONST              11 (('sort_keys', 'separators'))
                CALL_KW                  3
                STORE_FAST               8 (canonical)

 169            LOAD_GLOBAL              9 (_sha256_hex + NULL)
                LOAD_FAST_BORROW         8 (canonical)
                CALL                     1
       L19:     RETURN_VALUE

  --   L20:     PUSH_EXC_INFO

 170            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L24)
                NOT_TAKEN
                STORE_FAST               9 (e)

 171   L21:     LOAD_GLOBAL             18 (logger)
                LOAD_ATTR               21 (warning + NULL|self)

 172            LOAD_CONST              12 ('build_rate_limit_bucket_key error type=')
                LOAD_GLOBAL             23 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               24 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 171            CALL                     1
                POP_TOP

 174   L22:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L23:     LOAD_CONST               1 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 170   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L9 to L10 -> L20 [0]
  L11 to L13 -> L20 [0]
  L14 to L16 -> L20 [0]
  L17 to L19 -> L20 [0]
  L20 to L21 -> L25 [1] lasti
  L21 to L22 -> L23 [1] lasti
  L23 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "app/services/security/rate_limit.py", line 177>:
177           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object resolve_rate_limit_policy at 0x0000018C17FA92F0, file "app/services/security/rate_limit.py", line 177>:
177           RESUME                   0

180           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (surface)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (surface)
              LOAD_GLOBAL              4 (ALLOWED_SURFACES)
              CONTAINS_OP              1 (not in)
              POP_JUMP_IF_FALSE        9 (to L2)
              NOT_TAKEN

182   L1:     LOAD_CONST               1 ('status')
              LOAD_CONST               2 ('failed')

183           LOAD_CONST               3 ('policy')
              LOAD_CONST               4 (None)

184           LOAD_CONST               5 ('error_code')
              LOAD_CONST               6 ('invalid_surface')

181           BUILD_MAP                3
              RETURN_VALUE

186   L2:     LOAD_GLOBAL              6 (DEFAULT_POLICIES)
              LOAD_ATTR                9 (get + NULL|self)
              LOAD_FAST_BORROW         0 (surface)
              CALL                     1
              STORE_FAST               1 (pol)

188           LOAD_CONST               1 ('status')
              LOAD_CONST               7 ('ok')

189           LOAD_CONST               3 ('policy')
              LOAD_GLOBAL             11 (dict + NULL)
              LOAD_FAST                1 (pol)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              POP_TOP
              BUILD_MAP                0
      L3:     CALL                     1

190           LOAD_CONST               5 ('error_code')
              LOAD_CONST               4 (None)

187           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18053990, file "app/services/security/rate_limit.py", line 198>:
198           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('allowed')

200           LOAD_CONST               2 ('bool')

198           LOAD_CONST               3 ('surface')

201           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST               5 ('backend')

202           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST               6 ('bucket_key')

203           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST               7 ('request_count')

204           LOAD_CONST               8 ('int')

198           LOAD_CONST               9 ('blocked_count')

205           LOAD_CONST               8 ('int')

198           LOAD_CONST              10 ('limit')

206           LOAD_CONST               8 ('int')

198           LOAD_CONST              11 ('window_start')

207           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST              12 ('window_end')

208           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST              13 ('retry_after_seconds')

209           LOAD_CONST              14 ('Optional[int]')

198           LOAD_CONST              15 ('warnings')

210           LOAD_CONST              16 ('Optional[List[str]]')

198           LOAD_CONST              17 ('error_code')

211           LOAD_CONST               4 ('Optional[str]')

198           LOAD_CONST              18 ('return')

212           LOAD_CONST              19 ('Dict[str, Any]')

198           BUILD_MAP               13
              RETURN_VALUE

Disassembly of <code object _safe_verdict at 0x0000018C17FF13B0, file "app/services/security/rate_limit.py", line 198>:
198           RESUME                   0

217           LOAD_CONST               0 ('allowed')
              LOAD_GLOBAL              1 (bool + NULL)
              LOAD_FAST_BORROW         0 (allowed)
              CALL                     1

218           LOAD_CONST               1 ('surface')
              LOAD_FAST                1 (surface)

219           LOAD_CONST               2 ('backend')
              LOAD_FAST                2 (backend)

220           LOAD_CONST               3 ('bucket_key')
              LOAD_FAST                3 (bucket_key)

221           LOAD_CONST               4 ('request_count')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         4 (request_count)
              CALL                     1

222           LOAD_CONST               5 ('blocked_count')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         5 (blocked_count)
              CALL                     1

223           LOAD_CONST               6 ('limit')
              LOAD_GLOBAL              3 (int + NULL)
              LOAD_FAST_BORROW         6 (limit)
              CALL                     1

224           LOAD_CONST               7 ('window_start')
              LOAD_FAST                7 (window_start)

225           LOAD_CONST               8 ('window_end')
              LOAD_FAST                8 (window_end)

226           LOAD_CONST               9 ('retry_after_seconds')
              LOAD_FAST                9 (retry_after_seconds)

227           LOAD_CONST              10 ('warnings')
              LOAD_GLOBAL              5 (list + NULL)
              LOAD_FAST               10 (warnings)
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L1:     CALL                     1

228           LOAD_CONST              11 ('error_code')
              LOAD_FAST_BORROW        11 (error_code)

216           BUILD_MAP               12
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025D30, file "app/services/security/rate_limit.py", line 232>:
232           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

234           LOAD_CONST               2 ('str')

232           LOAD_CONST               3 ('brokerage_id')

235           LOAD_CONST               4 ('Optional[str]')

232           LOAD_CONST               5 ('actor_type')

236           LOAD_CONST               4 ('Optional[str]')

232           LOAD_CONST               6 ('actor_token')

237           LOAD_CONST               4 ('Optional[str]')

232           LOAD_CONST               7 ('now')

238           LOAD_CONST               8 ('Any')

232           LOAD_CONST               9 ('return')

239           LOAD_CONST              10 ('Dict[str, Any]')

232           BUILD_MAP                6
              RETURN_VALUE

Disassembly of <code object check_rate_limit at 0x0000018C17ED9FB0, file "app/services/security/rate_limit.py", line 232>:
 232            RESUME                   0

 256            LOAD_GLOBAL              1 (resolve_rate_limit_policy + NULL)
                LOAD_FAST_BORROW         0 (surface)
                CALL                     1
                STORE_FAST               5 (pol_env)

 257            LOAD_FAST_BORROW         5 (pol_env)
                LOAD_CONST               1 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               2 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       56 (to L3)
                NOT_TAKEN

 258            LOAD_GLOBAL              3 (_safe_verdict + NULL)

 259            LOAD_CONST               3 (True)

 260            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (surface)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L1)
                NOT_TAKEN
                LOAD_FAST                0 (surface)
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_CONST               4 (None)

 261    L2:     LOAD_CONST               5 ('rate_limit_invalid_surface')
                BUILD_LIST               1

 262            LOAD_FAST_BORROW         5 (pol_env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('error_code')
                CALL                     1

 258            LOAD_CONST               7 (('allowed', 'surface', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 264    L3:     LOAD_FAST_BORROW         5 (pol_env)
                LOAD_CONST               8 ('policy')
                BINARY_OP               26 ([])
                STORE_FAST               6 (policy)

 265            LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         6 (policy)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               9 ('max_requests')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
        L4:     CALL                     1
                STORE_FAST               7 (max_req)

 266            LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_BORROW         6 (policy)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              10 ('window_seconds')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L5)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT          60
        L5:     CALL                     1
                STORE_FAST               8 (win_sec)

 268            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         4 (now)
                LOAD_GLOBAL             12 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L6)
                NOT_TAKEN
                LOAD_FAST                4 (now)
                JUMP_FORWARD             9 (to L7)
        L6:     LOAD_GLOBAL             15 (_now_dt + NULL)
                CALL                     0
        L7:     STORE_FAST               9 (now_dt)

 269            LOAD_GLOBAL             17 (_window_for + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 152 (now_dt, win_sec)
                LOAD_CONST              11 (('now', 'window_seconds'))
                CALL_KW                  2
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  171 (start, end)

 270            LOAD_GLOBAL             19 (build_rate_limit_bucket_key + NULL)

 271            LOAD_FAST_BORROW         0 (surface)

 272            LOAD_FAST_BORROW         1 (brokerage_id)

 273            LOAD_FAST_BORROW         2 (actor_type)

 274            LOAD_FAST_BORROW         3 (actor_token)

 275            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST_BORROW        10 (start)
                CALL                     1

 270            LOAD_CONST              12 (('surface', 'brokerage_id', 'actor_type', 'actor_token', 'window_start'))
                CALL_KW                  5
                STORE_FAST              12 (bucket)

 277            LOAD_FAST_BORROW        12 (bucket)
                POP_JUMP_IF_NOT_NONE    17 (to L8)
                NOT_TAKEN

 278            LOAD_GLOBAL              3 (_safe_verdict + NULL)

 279            LOAD_CONST               3 (True)

 280            LOAD_FAST_BORROW         0 (surface)

 281            LOAD_CONST              13 ('rate_limit_bucket_key_failed')
                BUILD_LIST               1

 282            LOAD_CONST              14 ('bucket_key_failed')

 278            LOAD_CONST               7 (('allowed', 'surface', 'warnings', 'error_code'))
                CALL_KW                  4
                RETURN_VALUE

 285    L8:     NOP

 286    L9:     LOAD_SMALL_INT           0
                LOAD_CONST              15 (('increment_counter',))
                IMPORT_NAME             11 (app.services.security.rate_limit_store)
                IMPORT_FROM             12 (increment_counter)
                STORE_FAST              13 (increment_counter)
                POP_TOP

 287            LOAD_FAST               13 (increment_counter)
                PUSH_NULL

 288            LOAD_FAST               12 (bucket)

 289            LOAD_FAST                0 (surface)

 290            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST_BORROW        10 (start)
                CALL                     1

 291            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST_BORROW        11 (end)
                CALL                     1

 292            LOAD_FAST                1 (brokerage_id)

 293            LOAD_FAST                2 (actor_type)

 294            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (actor_token)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L12)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (actor_token)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L12)
       L10:     NOT_TAKEN
       L11:     LOAD_GLOBAL             27 (_sha256_hex + NULL)
                LOAD_FAST_BORROW         3 (actor_token)
                CALL                     1
                JUMP_FORWARD             1 (to L13)
       L12:     LOAD_CONST               4 (None)

 295   L13:     LOAD_SMALL_INT           1

 296            LOAD_SMALL_INT           0

 297            LOAD_CONST              16 ('event')
                LOAD_CONST              17 ('security.rate_limit.allowed')
                BUILD_MAP                1

 287            LOAD_CONST              18 (('bucket_key', 'surface', 'window_start', 'window_end', 'brokerage_id', 'actor_type', 'actor_id', 'request_count_delta', 'blocked_delta', 'metadata'))
                CALL_KW                 10
                STORE_FAST              14 (env)

 314   L14:     LOAD_FAST               14 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('counter')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                POP_TOP
                BUILD_MAP                0
       L15:     STORE_FAST              16 (counter)

 315            LOAD_FAST               14 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              24 ('backend')
                CALL                     1
                STORE_FAST              17 (backend)

 316            LOAD_GLOBAL             39 (list + NULL)
                LOAD_FAST               14 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              25 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
                NOT_TAKEN
                POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              18 (warnings)

 317            LOAD_FAST               14 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                LOAD_CONST               2 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       62 (to L17)
                NOT_TAKEN

 318            LOAD_GLOBAL              3 (_safe_verdict + NULL)

 319            LOAD_CONST               3 (True)

 320            LOAD_FAST                0 (surface)

 321            LOAD_FAST               17 (backend)

 322            LOAD_FAST               12 (bucket)

 323            LOAD_FAST                7 (max_req)

 324            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               10 (start)
                CALL                     1

 325            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               11 (end)
                CALL                     1

 326            LOAD_FAST               18 (warnings)
                LOAD_CONST              26 ('rate_limit_store_unavailable')
                BUILD_LIST               1
                BINARY_OP                0 (+)

 327            LOAD_FAST               14 (env)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST               6 ('error_code')
                CALL                     1

 318            LOAD_CONST              27 (('allowed', 'surface', 'backend', 'bucket_key', 'limit', 'window_start', 'window_end', 'warnings', 'error_code'))
                CALL_KW                  9
                RETURN_VALUE

 330   L17:     LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST               16 (counter)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              28 ('request_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L18)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L18:     CALL                     1
                STORE_FAST              19 (req_count)

 331            LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST               16 (counter)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              29 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L19)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT           0
       L19:     CALL                     1
                STORE_FAST              20 (blk_count)

 332            LOAD_FAST               19 (req_count)
                LOAD_FAST                7 (max_req)
                COMPARE_OP              42 (<=)
                STORE_FAST              21 (allowed)

 333            LOAD_FAST               21 (allowed)
                TO_BOOL
                POP_JUMP_IF_TRUE       148 (to L31)
                NOT_TAKEN

 336            NOP

 337   L20:     LOAD_SMALL_INT           0
                LOAD_CONST              15 (('increment_counter',))
                IMPORT_NAME             11 (app.services.security.rate_limit_store)
                IMPORT_FROM             12 (increment_counter)
                STORE_FAST              22 (_inc)
                POP_TOP

 338            LOAD_FAST               22 (_inc)
                PUSH_NULL

 339            LOAD_FAST               12 (bucket)

 340            LOAD_FAST                0 (surface)

 341            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               10 (start)
                CALL                     1

 342            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               11 (end)
                CALL                     1

 343            LOAD_FAST                1 (brokerage_id)

 344            LOAD_FAST                2 (actor_type)

 345            LOAD_GLOBAL              5 (isinstance + NULL)
                LOAD_FAST                3 (actor_token)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L23)
                NOT_TAKEN
                LOAD_FAST                3 (actor_token)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L23)
       L21:     NOT_TAKEN
       L22:     LOAD_GLOBAL             27 (_sha256_hex + NULL)
                LOAD_FAST                3 (actor_token)
                CALL                     1
                JUMP_FORWARD             1 (to L24)
       L23:     LOAD_CONST               4 (None)

 346   L24:     LOAD_SMALL_INT           0

 347            LOAD_SMALL_INT           1

 348            LOAD_CONST              16 ('event')
                LOAD_CONST              30 ('security.rate_limit.blocked')
                BUILD_MAP                1

 338            LOAD_CONST              18 (('bucket_key', 'surface', 'window_start', 'window_end', 'brokerage_id', 'actor_type', 'actor_id', 'request_count_delta', 'blocked_delta', 'metadata'))
                CALL_KW                 10
                STORE_FAST              23 (env2)

 350            LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST               23 (env2)
                LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              23 ('counter')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L27)
       L25:     NOT_TAKEN
       L26:     POP_TOP
                BUILD_MAP                0
       L27:     LOAD_ATTR                9 (get + NULL|self)
                LOAD_CONST              29 ('blocked_count')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L30)
       L28:     NOT_TAKEN
       L29:     POP_TOP
                LOAD_FAST               20 (blk_count)
       L30:     CALL                     1
                STORE_FAST              20 (blk_count)

 356   L31:     LOAD_CONST               4 (None)
                STORE_FAST              24 (retry_after)

 357            LOAD_FAST               21 (allowed)
                TO_BOOL
                POP_JUMP_IF_TRUE        43 (to L33)
                NOT_TAKEN

 358            NOP

 359   L32:     LOAD_GLOBAL             41 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL             11 (int + NULL)
                LOAD_FAST_LOAD_FAST    185 (end, now_dt)
                BINARY_OP               10 (-)
                LOAD_ATTR               43 (total_seconds + NULL|self)
                CALL                     0
                CALL                     1
                CALL                     2
                STORE_FAST              24 (retry_after)

 363   L33:     LOAD_GLOBAL              3 (_safe_verdict + NULL)

 364            LOAD_FAST               21 (allowed)

 365            LOAD_FAST                0 (surface)

 366            LOAD_FAST               17 (backend)

 367            LOAD_FAST               12 (bucket)

 368            LOAD_FAST               19 (req_count)

 369            LOAD_FAST               20 (blk_count)

 370            LOAD_FAST                7 (max_req)

 371            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               10 (start)
                CALL                     1

 372            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               11 (end)
                CALL                     1

 373            LOAD_FAST               24 (retry_after)

 374            LOAD_FAST               18 (warnings)

 363            LOAD_CONST              32 (('allowed', 'surface', 'backend', 'bucket_key', 'request_count', 'blocked_count', 'limit', 'window_start', 'window_end', 'retry_after_seconds', 'warnings'))
                CALL_KW                 11
                RETURN_VALUE

  --   L34:     PUSH_EXC_INFO

 299            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      114 (to L39)
                NOT_TAKEN
                STORE_FAST              15 (e)

 300   L35:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 301            LOAD_CONST              19 ('check_rate_limit increment error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 300            CALL                     1
                POP_TOP

 303            LOAD_GLOBAL              3 (_safe_verdict + NULL)

 304            LOAD_CONST               3 (True)

 305            LOAD_FAST                0 (surface)

 306            LOAD_FAST               12 (bucket)

 307            LOAD_FAST                7 (max_req)

 308            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               10 (start)
                CALL                     1

 309            LOAD_GLOBAL             21 (_iso + NULL)
                LOAD_FAST               11 (end)
                CALL                     1

 310            LOAD_CONST              20 ('rate_limit_store_unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 311            LOAD_CONST              21 ('rate_limit_store_unexpected')

 303            LOAD_CONST              22 (('allowed', 'surface', 'bucket_key', 'limit', 'window_start', 'window_end', 'warnings', 'error_code'))
                CALL_KW                  8
       L36:     SWAP                     2
       L37:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RETURN_VALUE

  --   L38:     LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 299   L39:     RERAISE                  0

  --   L40:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L41:     PUSH_EXC_INFO

 351            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       55 (to L45)
                NOT_TAKEN
                STORE_FAST              15 (e)

 352   L42:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 353            LOAD_CONST              31 ('check_rate_limit blocked-increment error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               15 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 352            CALL                     1
                POP_TOP
       L43:     POP_EXCEPT
                LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                EXTENDED_ARG             1
                JUMP_BACKWARD_NO_INTERRUPT 279 (to L31)

  --   L44:     LOAD_CONST               4 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 351   L45:     RERAISE                  0

  --   L46:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L47:     PUSH_EXC_INFO

 360            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        6 (to L49)
                NOT_TAKEN
                POP_TOP

 361            LOAD_FAST                8 (win_sec)
                STORE_FAST              24 (retry_after)
       L48:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 250 (to L33)

 360   L49:     RERAISE                  0

  --   L50:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L9 to L10 -> L34 [0]
  L11 to L14 -> L34 [0]
  L20 to L21 -> L41 [0]
  L22 to L25 -> L41 [0]
  L26 to L28 -> L41 [0]
  L29 to L31 -> L41 [0]
  L32 to L33 -> L47 [0]
  L34 to L35 -> L40 [1] lasti
  L35 to L36 -> L38 [1] lasti
  L36 to L37 -> L40 [1] lasti
  L38 to L40 -> L40 [1] lasti
  L41 to L42 -> L46 [1] lasti
  L42 to L43 -> L44 [1] lasti
  L44 to L46 -> L46 [1] lasti
  L47 to L48 -> L50 [1] lasti
  L49 to L50 -> L50 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C1812C140, file "app/services/security/rate_limit.py", line 378>:
378           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

380           LOAD_CONST               2 ('str')

378           LOAD_CONST               3 ('brokerage_id')

381           LOAD_CONST               4 ('Optional[str]')

378           LOAD_CONST               5 ('actor_type')

382           LOAD_CONST               4 ('Optional[str]')

378           LOAD_CONST               6 ('actor_token')

383           LOAD_CONST               4 ('Optional[str]')

378           LOAD_CONST               7 ('blocked')

384           LOAD_CONST               8 ('bool')

378           LOAD_CONST               9 ('now')

385           LOAD_CONST              10 ('Any')

378           LOAD_CONST              11 ('return')

386           LOAD_CONST              12 ('Dict[str, Any]')

378           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object record_rate_limit_hit at 0x0000018C17F41160, file "app/services/security/rate_limit.py", line 378>:
 378            RESUME                   0

 390            LOAD_GLOBAL              1 (resolve_rate_limit_policy + NULL)
                LOAD_FAST_BORROW         0 (surface)
                CALL                     1
                STORE_FAST               6 (pol_env)

 391            LOAD_FAST_BORROW         6 (pol_env)
                LOAD_CONST               1 ('status')
                BINARY_OP               26 ([])
                LOAD_CONST               2 ('ok')
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       24 (to L1)
                NOT_TAKEN

 393            LOAD_CONST               1 ('status')
                LOAD_CONST               3 ('failed')

 394            LOAD_CONST               4 ('error_code')
                LOAD_FAST_BORROW         6 (pol_env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               4 ('error_code')
                CALL                     1

 395            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 392            BUILD_MAP                3
                RETURN_VALUE

 397    L1:     LOAD_GLOBAL              5 (int + NULL)
                LOAD_FAST_BORROW         6 (pol_env)
                LOAD_CONST               6 ('policy')
                BINARY_OP               26 ([])
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               7 ('window_seconds')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L2)
                NOT_TAKEN
                POP_TOP
                LOAD_SMALL_INT          60
        L2:     CALL                     1
                STORE_FAST               7 (win_sec)

 398            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         5 (now)
                LOAD_GLOBAL              8 (datetime)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_FAST                5 (now)
                JUMP_FORWARD             9 (to L4)
        L3:     LOAD_GLOBAL             11 (_now_dt + NULL)
                CALL                     0
        L4:     STORE_FAST               8 (now_dt)

 399            LOAD_GLOBAL             13 (_window_for + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 135 (now_dt, win_sec)
                LOAD_CONST               8 (('now', 'window_seconds'))
                CALL_KW                  2
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  154 (start, end)

 400            LOAD_GLOBAL             15 (build_rate_limit_bucket_key + NULL)

 401            LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (surface, brokerage_id)

 402            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (actor_type, actor_token)

 403            LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW         9 (start)
                CALL                     1

 400            LOAD_CONST               9 (('surface', 'brokerage_id', 'actor_type', 'actor_token', 'window_start'))
                CALL_KW                  5
                STORE_FAST              11 (bucket)

 405            LOAD_FAST_BORROW        11 (bucket)
                POP_JUMP_IF_NOT_NONE     9 (to L5)
                NOT_TAKEN

 407            LOAD_CONST               1 ('status')
                LOAD_CONST               3 ('failed')

 408            LOAD_CONST               4 ('error_code')
                LOAD_CONST              11 ('bucket_key_failed')

 409            LOAD_CONST               5 ('warnings')
                BUILD_LIST               0

 406            BUILD_MAP                3
                RETURN_VALUE

 411    L5:     NOP

 412    L6:     LOAD_SMALL_INT           0
                LOAD_CONST              12 (('increment_counter',))
                IMPORT_NAME              9 (app.services.security.rate_limit_store)
                IMPORT_FROM             10 (increment_counter)
                STORE_FAST              12 (increment_counter)
                POP_TOP

 413            LOAD_FAST               12 (increment_counter)
                PUSH_NULL

 414            LOAD_FAST               11 (bucket)

 415            LOAD_FAST                0 (surface)

 416            LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW         9 (start)
                CALL                     1

 417            LOAD_GLOBAL             17 (_iso + NULL)
                LOAD_FAST_BORROW        10 (end)
                CALL                     1

 418            LOAD_FAST                1 (brokerage_id)

 419            LOAD_FAST                2 (actor_type)

 420            LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         3 (actor_token)
                LOAD_GLOBAL             22 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       20 (to L9)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (actor_token)
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L9)
        L7:     NOT_TAKEN
        L8:     LOAD_GLOBAL             25 (_sha256_hex + NULL)
                LOAD_FAST_BORROW         3 (actor_token)
                CALL                     1
                JUMP_FORWARD             1 (to L10)
        L9:     LOAD_CONST              10 (None)

 421   L10:     LOAD_FAST_BORROW         4 (blocked)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L13)
       L11:     NOT_TAKEN
       L12:     LOAD_SMALL_INT           0
                JUMP_FORWARD             1 (to L14)
       L13:     LOAD_SMALL_INT           1

 422   L14:     LOAD_FAST_BORROW         4 (blocked)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L17)
       L15:     NOT_TAKEN
       L16:     LOAD_SMALL_INT           1
                JUMP_FORWARD             1 (to L18)
       L17:     LOAD_SMALL_INT           0

 424   L18:     LOAD_CONST              13 ('event')

 426            LOAD_FAST_BORROW         4 (blocked)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L21)
       L19:     NOT_TAKEN

 425   L20:     LOAD_CONST              14 ('security.rate_limit.blocked')
                JUMP_FORWARD             1 (to L22)

 427   L21:     LOAD_CONST              15 ('security.rate_limit.allowed')

 423   L22:     BUILD_MAP                1

 413            LOAD_CONST              16 (('bucket_key', 'surface', 'window_start', 'window_end', 'brokerage_id', 'actor_type', 'actor_id', 'request_count_delta', 'blocked_delta', 'metadata'))
                CALL_KW                 10
                STORE_FAST              13 (env)

 432            LOAD_CONST               1 ('status')
                LOAD_FAST_BORROW        13 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               1 ('status')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L25)
       L23:     NOT_TAKEN
       L24:     POP_TOP
                LOAD_CONST               2 ('ok')

 433   L25:     LOAD_CONST              17 ('backend')
                LOAD_FAST_BORROW        13 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST              17 ('backend')
                CALL                     1

 434            LOAD_CONST               5 ('warnings')
                LOAD_GLOBAL             27 (list + NULL)
                LOAD_FAST_BORROW        13 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               5 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L28)
       L26:     NOT_TAKEN
       L27:     POP_TOP
                BUILD_LIST               0
       L28:     CALL                     1

 435            LOAD_CONST               4 ('error_code')
                LOAD_FAST_BORROW        13 (env)
                LOAD_ATTR                3 (get + NULL|self)
                LOAD_CONST               4 ('error_code')
                CALL                     1

 431            BUILD_MAP                4
       L29:     RETURN_VALUE

  --   L30:     PUSH_EXC_INFO

 437            LOAD_GLOBAL             28 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      107 (to L35)
                NOT_TAKEN
                STORE_FAST              14 (e)

 438   L31:     LOAD_GLOBAL             30 (logger)
                LOAD_ATTR               33 (warning + NULL|self)

 439            LOAD_CONST              18 ('record_rate_limit_hit error type=')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 438            CALL                     1
                POP_TOP

 442            LOAD_CONST               1 ('status')
                LOAD_CONST               3 ('failed')

 443            LOAD_CONST               5 ('warnings')
                LOAD_CONST              19 ('rate_limit_unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 444            LOAD_CONST               4 ('error_code')
                LOAD_CONST              20 ('unexpected:')
                LOAD_GLOBAL             35 (type + NULL)
                LOAD_FAST               14 (e)
                CALL                     1
                LOAD_ATTR               36 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 441            BUILD_MAP                3
       L32:     SWAP                     2
       L33:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RETURN_VALUE

  --   L34:     LOAD_CONST              10 (None)
                STORE_FAST              14 (e)
                DELETE_FAST             14 (e)
                RERAISE                  1

 437   L35:     RERAISE                  0

  --   L36:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L6 to L7 -> L30 [0]
  L8 to L11 -> L30 [0]
  L12 to L15 -> L30 [0]
  L16 to L19 -> L30 [0]
  L20 to L23 -> L30 [0]
  L24 to L26 -> L30 [0]
  L27 to L29 -> L30 [0]
  L30 to L31 -> L36 [1] lasti
  L31 to L32 -> L34 [1] lasti
  L32 to L33 -> L36 [1] lasti
  L34 to L36 -> L36 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025E30, file "app/services/security/rate_limit.py", line 452>:
452           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

454           LOAD_CONST               2 ('Optional[str]')

452           LOAD_CONST               3 ('brokerage_id')

455           LOAD_CONST               2 ('Optional[str]')

452           LOAD_CONST               4 ('limit')

456           LOAD_CONST               5 ('int')

452           LOAD_CONST               6 ('return')

457           LOAD_CONST               7 ('Dict[str, Any]')

452           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object rate_limit_report at 0x0000018C17789BE0, file "app/services/security/rate_limit.py", line 452>:
 452            RESUME                   0

 460            NOP

 461    L1:     LOAD_FAST_BORROW         0 (surface)
                POP_JUMP_IF_NONE        24 (to L3)
                NOT_TAKEN
                LOAD_FAST_BORROW         0 (surface)
                LOAD_GLOBAL              0 (ALLOWED_SURFACES)
                CONTAINS_OP              1 (not in)
                POP_JUMP_IF_FALSE       13 (to L3)
                NOT_TAKEN

 463            LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')

 464            LOAD_CONST               4 ('rows')
                BUILD_LIST               0

 465            LOAD_CONST               5 ('count')
                LOAD_SMALL_INT           0

 466            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 467            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_surface')

 462            BUILD_MAP                5
        L2:     RETURN_VALUE

 469    L3:     LOAD_GLOBAL              3 (max + NULL)
                LOAD_SMALL_INT           1
                LOAD_GLOBAL              5 (min + NULL)
                LOAD_GLOBAL              7 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (limit)
                LOAD_GLOBAL              8 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L4)
                NOT_TAKEN
                LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (limit)
                CALL                     1
                JUMP_FORWARD             5 (to L5)
        L4:     LOAD_GLOBAL             10 (_DEFAULT_LIMIT)
        L5:     LOAD_GLOBAL             12 (_LIST_HARD_CAP)
                CALL                     2
                CALL                     2
                STORE_FAST               3 (capped)

 470            LOAD_SMALL_INT           0
                LOAD_CONST               9 (('get_supabase',))
                IMPORT_NAME              7 (app.db.supabase_client)
                IMPORT_FROM              8 (get_supabase)
                STORE_FAST               4 (get_supabase)
                POP_TOP

 471            LOAD_FAST_BORROW         4 (get_supabase)
                PUSH_NULL
                CALL                     0
                STORE_FAST               5 (db)

 483    L6:     NOP

 484    L7:     LOAD_SMALL_INT           0
                LOAD_CONST              13 (('_STRUCTURAL_COLUMNS',))
                IMPORT_NAME             14 (app.services.security.rate_limit_store)
                IMPORT_FROM             15 (_STRUCTURAL_COLUMNS)
                STORE_FAST               7 (_STRUCTURAL_COLUMNS)
                POP_TOP

 486            LOAD_FAST                5 (db)
                LOAD_ATTR               33 (table + NULL|self)
                LOAD_CONST              14 ('pas_rate_limit_counters')
                CALL                     1

 487            LOAD_ATTR               35 (select + NULL|self)
                LOAD_CONST              15 (',')
                LOAD_ATTR               37 (join + NULL|self)
                LOAD_FAST                7 (_STRUCTURAL_COLUMNS)
                CALL                     1
                CALL                     1

 488            LOAD_ATTR               39 (order + NULL|self)
                LOAD_CONST              16 ('window_end')
                LOAD_CONST              17 (True)
                LOAD_CONST              18 (('desc',))
                CALL_KW                  2

 489            LOAD_ATTR               41 (limit + NULL|self)
                LOAD_FAST                3 (capped)
                CALL                     1

 485            STORE_FAST               8 (query)

 491            LOAD_FAST                0 (surface)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L10)
        L8:     NOT_TAKEN

 492    L9:     LOAD_FAST                8 (query)
                LOAD_ATTR               43 (eq + NULL|self)
                LOAD_CONST              19 ('surface')
                LOAD_FAST                0 (surface)
                CALL                     2
                STORE_FAST               8 (query)

 493   L10:     LOAD_FAST                1 (brokerage_id)
                TO_BOOL
                POP_JUMP_IF_FALSE       19 (to L13)
       L11:     NOT_TAKEN

 494   L12:     LOAD_FAST                8 (query)
                LOAD_ATTR               43 (eq + NULL|self)
                LOAD_CONST              20 ('brokerage_id')
                LOAD_FAST                1 (brokerage_id)
                CALL                     2
                STORE_FAST               8 (query)

 495   L13:     LOAD_FAST                8 (query)
                LOAD_ATTR               45 (execute + NULL|self)
                CALL                     0
                STORE_FAST               9 (result)

 496            LOAD_GLOBAL             47 (list + NULL)
                LOAD_GLOBAL             49 (getattr + NULL)
                LOAD_FAST                9 (result)
                LOAD_CONST              21 ('data')
                LOAD_CONST               1 (None)
                CALL                     3
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L16)
       L14:     NOT_TAKEN
       L15:     POP_TOP
                BUILD_LIST               0
       L16:     CALL                     1
                STORE_FAST              10 (rows)

 498            LOAD_CONST               2 ('status')
                LOAD_CONST              22 ('ok')

 499            LOAD_CONST               4 ('rows')
                LOAD_FAST               10 (rows)

 500            LOAD_CONST               5 ('count')
                LOAD_GLOBAL             51 (len + NULL)
                LOAD_FAST               10 (rows)
                CALL                     1

 501            LOAD_CONST               6 ('warnings')
                BUILD_LIST               0

 502            LOAD_CONST               7 ('error_code')
                LOAD_CONST               1 (None)

 497            BUILD_MAP                5
       L17:     RETURN_VALUE

  --   L18:     PUSH_EXC_INFO

 472            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       67 (to L23)
                NOT_TAKEN
                STORE_FAST               6 (e)

 473   L19:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 474            LOAD_CONST              10 ('rate_limit_report db client unavailable type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 473            CALL                     1
                POP_TOP

 477            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 478            LOAD_CONST               4 ('rows')
                BUILD_LIST               0

 479            LOAD_CONST               5 ('count')
                LOAD_SMALL_INT           0

 480            LOAD_CONST               6 ('warnings')
                LOAD_CONST              12 ('rate_limit_store_unavailable')
                BUILD_LIST               1

 481            LOAD_CONST               7 ('error_code')
                LOAD_CONST              12 ('rate_limit_store_unavailable')

 476            BUILD_MAP                5
       L20:     SWAP                     2
       L21:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L22:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 472   L23:     RERAISE                  0

  --   L24:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L25:     PUSH_EXC_INFO

 504            LOAD_GLOBAL             18 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       89 (to L30)
                NOT_TAKEN
                STORE_FAST               6 (e)

 505   L26:     LOAD_GLOBAL             20 (logger)
                LOAD_ATTR               23 (warning + NULL|self)

 506            LOAD_CONST              23 ('rate_limit_report read error type=')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 505            CALL                     1
                POP_TOP

 509            LOAD_CONST               2 ('status')
                LOAD_CONST              11 ('skipped')

 510            LOAD_CONST               4 ('rows')
                BUILD_LIST               0

 511            LOAD_CONST               5 ('count')
                LOAD_SMALL_INT           0

 512            LOAD_CONST               6 ('warnings')
                LOAD_CONST              24 ('db_read_failed:')
                LOAD_GLOBAL             25 (type + NULL)
                LOAD_FAST                6 (e)
                CALL                     1
                LOAD_ATTR               26 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 513            LOAD_CONST               7 ('error_code')
                LOAD_CONST              12 ('rate_limit_store_unavailable')

 508            BUILD_MAP                5
       L27:     SWAP                     2
       L28:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RETURN_VALUE

  --   L29:     LOAD_CONST               1 (None)
                STORE_FAST               6 (e)
                DELETE_FAST              6 (e)
                RERAISE                  1

 504   L30:     RERAISE                  0

  --   L31:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [0]
  L3 to L6 -> L18 [0]
  L7 to L8 -> L25 [0]
  L9 to L11 -> L25 [0]
  L12 to L14 -> L25 [0]
  L15 to L17 -> L25 [0]
  L18 to L19 -> L24 [1] lasti
  L19 to L20 -> L22 [1] lasti
  L20 to L21 -> L24 [1] lasti
  L22 to L24 -> L24 [1] lasti
  L25 to L26 -> L31 [1] lasti
  L26 to L27 -> L29 [1] lasti
  L27 to L28 -> L31 [1] lasti
  L29 to L31 -> L31 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "app/services/security/rate_limit.py", line 517>:
517           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('verdict')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object rate_limit_public_error at 0x0000018C17D8C220, file "app/services/security/rate_limit.py", line 517>:
 517            RESUME                   0

 521            NOP

 522    L1:     LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         0 (verdict)
                LOAD_GLOBAL              2 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_TRUE        13 (to L3)
                NOT_TAKEN

 524            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 525            LOAD_CONST               3 ('error_code')
                LOAD_CONST               4 ('rate_limit_exceeded')

 526            LOAD_CONST               5 ('surface')
                LOAD_CONST               6 (None)

 527            LOAD_CONST               7 ('retry_after_seconds')
                LOAD_CONST               6 (None)

 528            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 523            BUILD_MAP                5
        L2:     RETURN_VALUE

 530    L3:     LOAD_FAST_BORROW         0 (verdict)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               5 ('surface')
                CALL                     1
                STORE_FAST               1 (surface)

 531            LOAD_FAST_BORROW         0 (verdict)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               7 ('retry_after_seconds')
                CALL                     1
                STORE_FAST               2 (retry_after)

 533            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 534            LOAD_CONST               3 ('error_code')
                LOAD_CONST               4 ('rate_limit_exceeded')

 535            LOAD_CONST               5 ('surface')
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         1 (surface)
                LOAD_GLOBAL              6 (str)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L4)
                NOT_TAKEN
                LOAD_FAST                1 (surface)
                JUMP_FORWARD             1 (to L5)
        L4:     LOAD_CONST               6 (None)

 536    L5:     LOAD_CONST               7 ('retry_after_seconds')
                LOAD_GLOBAL              1 (isinstance + NULL)
                LOAD_FAST_BORROW         2 (retry_after)
                LOAD_GLOBAL              8 (int)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL              9 (int + NULL)
                LOAD_FAST_BORROW         2 (retry_after)
                CALL                     1
                JUMP_FORWARD             1 (to L7)
        L6:     LOAD_CONST               6 (None)

 537    L7:     LOAD_CONST               8 ('warnings')
                LOAD_GLOBAL             11 (list + NULL)
                LOAD_FAST_BORROW         0 (verdict)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_CONST               8 ('warnings')
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L10)
        L8:     NOT_TAKEN
        L9:     POP_TOP
                BUILD_LIST               0
       L10:     CALL                     1

 532            BUILD_MAP                5
       L11:     RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 539            LOAD_GLOBAL             12 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       66 (to L17)
                NOT_TAKEN
                STORE_FAST               3 (e)

 540   L13:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 541            LOAD_CONST               9 ('rate_limit_public_error error type=')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                3 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 540            CALL                     1
                POP_TOP

 544            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')

 545            LOAD_CONST               3 ('error_code')
                LOAD_CONST               4 ('rate_limit_exceeded')

 546            LOAD_CONST               5 ('surface')
                LOAD_CONST               6 (None)

 547            LOAD_CONST               7 ('retry_after_seconds')
                LOAD_CONST               6 (None)

 548            LOAD_CONST               8 ('warnings')
                BUILD_LIST               0

 543            BUILD_MAP                5
       L14:     SWAP                     2
       L15:     POP_EXCEPT
                LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RETURN_VALUE

  --   L16:     LOAD_CONST               6 (None)
                STORE_FAST               3 (e)
                DELETE_FAST              3 (e)
                RERAISE                  1

 539   L17:     RERAISE                  0

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L3 to L8 -> L12 [0]
  L9 to L11 -> L12 [0]
  L12 to L13 -> L18 [1] lasti
  L13 to L14 -> L16 [1] lasti
  L14 to L15 -> L18 [1] lasti
  L16 to L18 -> L18 [1] lasti
```
