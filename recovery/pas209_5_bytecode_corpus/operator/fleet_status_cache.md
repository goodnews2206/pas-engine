# operator/fleet_status_cache

- **pyc:** `app\services\operator\__pycache__\fleet_status_cache.cpython-314.pyc`
- **expected source path (absent):** `app\services\operator/fleet_status_cache.py`
- **co_filename (from bytecode):** `app\services\operator\fleet_status_cache.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** operator

## Module docstring

```
PAS188 — Fleet-status TTL cache (in-process, read-only).

Caches the result of ``fleet_status.fleet_brokerage_health_summary``
(and the three derived roll-ups) so that at >10 brokerages,
a burst of operator dashboard refreshes does not fan out to
N * 6 per-brokerage signal calls.

Doctrine:

* **In-process only.** No Redis. No Memcache. No external
  dependency. PAS188 is additive surgical and adds NO new
  package to ``requirements.txt``.
* **TTL-bounded.** Default 60 s; clamped to [5, 600].
* **Read-only.** The cache wraps the existing read-only
  fleet_status functions. The cache itself NEVER mutates
  anything outside its own dict.
* **No autonomous warming.** No background thread. No
  scheduler. No cron. Cache entries are populated lazily
  on first request; ``invalidate()`` is operator-callable
  but PAS188 does NOT install a periodic invalidator.
* **No PII.** The cached envelopes inherit the forbidden-
  token scanner from ``fleet_status`` (which collapses
  the envelope on leak before it ever reaches the cache).
* **Never raises.** Cache miss / cache lookup failure
  collapses to a direct uncached call; cache write
  failures are swallowed.

Public surface:

  * ``get_fleet_brokerage_health_summary(...)``
  * ``get_fleet_chain_status_report(...)``
  * ``get_fleet_rollout_readiness_summary(...)``
  * ``get_fleet_exception_report(...)``
  * ``invalidate(...)``
  * ``cache_stats()``
  * ``configure_ttl(seconds)``
```

## Imports

`Any`, `Callable`, `Dict`, `Iterable`, `List`, `Optional`, `Tuple`, `__future__`, `annotations`, `app.services.operator.fleet_status`, `fleet_brokerage_health_summary`, `fleet_chain_status_report`, `fleet_exception_report`, `fleet_rollout_readiness_summary`, `logging`, `monotonic`, `threading`, `time`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_key`, `_lookup`, `_normalise_ids`, `_now`, `_safe_int`, `_store`, `_wrap`, `cache_stats`, `configure_ttl`, `get_fleet_brokerage_health_summary`, `get_fleet_chain_status_report`, `get_fleet_exception_report`, `get_fleet_rollout_readiness_summary`, `invalidate`, `invalidate_for_brokerage`

## Env-key candidates

_none_

## String constants (redacted where noted)

- '\nPAS188 — Fleet-status TTL cache (in-process, read-only).\n\nCaches the result of ``fleet_status.fleet_brokerage_health_summary``\n(and the three derived roll-ups) so that at >10 brokerages,\na burst of operator dashboard refreshes does not fan out to\nN * 6 per-brokerage signal calls.\n\nDoctrine:\n\n* **In-process only.** No Redis. No Memcache. No external\n  dependency. PAS188 is additive surgical and adds NO new\n  package to ``requirements.txt``.\n* **TTL-bounded.** Default 60 s; clamped to [5, 600].\n* **Read-only.** The cache wraps the existing read-only\n  fleet_status functions. The cache itself NEVER mutates\n  anything outside its own dict.\n* **No autonomous warming.** No background thread. No\n  scheduler. No cron. Cache entries are populated lazily\n  on first request; ``invalidate()`` is operator-callable\n  but PAS188 does NOT install a periodic invalidator.\n* **No PII.** The cached envelopes inherit the forbidden-\n  token scanner from ``fleet_status`` (which collapses\n  the envelope on leak before it ever reaches the cache).\n* **Never raises.** Cache miss / cache lookup failure\n  collapses to a direct uncached call; cache write\n  failures are swallowed.\n\nPublic surface:\n\n  * ``get_fleet_brokerage_health_summary(...)``\n  * ``get_fleet_chain_status_report(...)``\n  * ``get_fleet_rollout_readiness_summary(...)``\n  * ``get_fleet_exception_report(...)``\n  * ``invalidate(...)``\n  * ``cache_stats()``\n  * ``configure_ttl(seconds)``\n'
- 'pas.operator.fleet_status_cache'
- 'float'
- '_TTL_SECONDS'
- 'Dict[str, Tuple[float, Dict[str, Any]]]'
- '_CACHE'
- 'hits'
- 'misses'
- 'writes'
- 'invalidations'
- 'errors'
- 'fleet.brokerage_health'
- 'fleet.chain_status'
- 'fleet.rollout_readiness'
- 'fleet.exceptions'
- 'brokerage_ids'
- 'limit'
- 'surface'
- 'return'
- 'Optional[Iterable[Any]]'
- 'Tuple[str, ...]'
- 'str'
- 'ids'
- 'int'
- '|limit='
- '|ids='
- 'value'
- 'Any'
- 'default'
- 'key'
- 'payload'
- 'Dict[str, Any]'
- 'None'
- 'Optional[Dict[str, Any]]'
- 'Callable[..., Dict[str, Any]]'
- 'fleet_status_cache underlying surface='
- ' failed type='
- 'status'
- 'skipped'
- 'ops.'
- 'rows'
- 'count'
- 'warnings'
- 'underlying_failed:'
- 'error_code'
- 'underlying_failed'
- 'brokerage_id'
- 'PAS190 — drop any cached entry whose key tuple mentions\n``brokerage_id``. Bounded scan over `_CACHE.keys()`.\n\nThe cache key format produced by `_key` is\n``"<surface>|limit=<N>|ids=<csv>"``. We match\n`brokerage_id` against the csv segment so that an\noperator action against one brokerage does not blow\ncached entries that do not mention it.\n\nWhole-surface invalidation remains available as a\nfallback via :func:`invalidate`.'
- 'failed'
- 'cleared'
- 'scope'
- 'per_brokerage'
- 'invalid_brokerage_id'
- 'brokerage:'
- 'fleet_status_cache invalidate_for_brokerage error type='
- 'unexpected:'
- 'Optional[str]'
- 'Operator-callable cache invalidation. With no\narguments, clears all surfaces. With ``surface=<name>``,\nclears only entries for that surface.'
- 'all'
- 'fleet_status_cache invalidate error type='
- 'Snapshot of cache state. Read-only — does NOT\nmutate counters.'
- 'ops.fleet.cache_stats'
- 'ttl_seconds'
- 'entries'
- 'seconds'
- 'Operator-tunable TTL. Bounded; never raises.'
- 'invalid_ttl'

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ('\nPAS188 — Fleet-status TTL cache (in-process, read-only).\n\nCaches the result of ``fleet_status.fleet_brokerage_health_summary``\n(and the three derived roll-ups) so that at >10 brokerages,\na burst of operator dashboard refreshes does not fan out to\nN * 6 per-brokerage signal calls.\n\nDoctrine:\n\n* **In-process only.** No Redis. No Memcache. No external\n  dependency. PAS188 is additive surgical and adds NO new\n  package to ``requirements.txt``.\n* **TTL-bounded.** Default 60 s; clamped to [5, 600].\n* **Read-only.** The cache wraps the existing read-only\n  fleet_status functions. The cache itself NEVER mutates\n  anything outside its own dict.\n* **No autonomous warming.** No background thread. No\n  scheduler. No cron. Cache entries are populated lazily\n  on first request; ``invalidate()`` is operator-callable\n  but PAS188 does NOT install a periodic invalidator.\n* **No PII.** The cached envelopes inherit the forbidden-\n  token scanner from ``fleet_status`` (which collapses\n  the envelope on leak before it ever reaches the cache).\n* **Never raises.** Cache miss / cache lookup failure\n  collapses to a direct uncached call; cache write\n  failures are swallowed.\n\nPublic surface:\n\n  * ``get_fleet_brokerage_health_summary(...)``\n  * ``get_fleet_chain_status_report(...)``\n  * ``get_fleet_rollout_readiness_summary(...)``\n  * ``get_fleet_exception_report(...)``\n  * ``invalidate(...)``\n  * ``cache_stats()``\n  * ``configure_ttl(seconds)``\n')
               STORE_NAME               1 (__doc__)

  40           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  42           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (logging)
               STORE_NAME               4 (logging)

  43           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (threading)
               STORE_NAME               5 (threading)

  44           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('monotonic',))
               IMPORT_NAME              6 (time)
               IMPORT_FROM              7 (monotonic)
               STORE_NAME               7 (monotonic)
               POP_TOP

  45           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('Any', 'Callable', 'Dict', 'Iterable', 'List', 'Optional', 'Tuple'))
               IMPORT_NAME              8 (typing)
               IMPORT_FROM              9 (Any)
               STORE_NAME               9 (Any)
               IMPORT_FROM             10 (Callable)
               STORE_NAME              10 (Callable)
               IMPORT_FROM             11 (Dict)
               STORE_NAME              11 (Dict)
               IMPORT_FROM             12 (Iterable)
               STORE_NAME              12 (Iterable)
               IMPORT_FROM             13 (List)
               STORE_NAME              13 (List)
               IMPORT_FROM             14 (Optional)
               STORE_NAME              14 (Optional)
               IMPORT_FROM             15 (Tuple)
               STORE_NAME              15 (Tuple)
               POP_TOP

  48           LOAD_NAME                4 (logging)
               LOAD_ATTR               32 (getLogger)
               PUSH_NULL
               LOAD_CONST               5 ('pas.operator.fleet_status_cache')
               CALL                     1
               STORE_NAME              17 (logger)

  55           LOAD_CONST               6 (60.0)
               STORE_NAME              18 (_TTL_DEFAULT)

  56           LOAD_CONST               7 (5.0)
               STORE_NAME              19 (_TTL_MIN)

  57           LOAD_CONST               8 (600.0)
               STORE_NAME              20 (_TTL_MAX)

  59           LOAD_NAME                5 (threading)
               LOAD_ATTR               42 (RLock)
               PUSH_NULL
               CALL                     0
               STORE_NAME              22 (_LOCK)

  60           LOAD_NAME               18 (_TTL_DEFAULT)
               STORE_GLOBAL            23 (_TTL_SECONDS)
               LOAD_CONST               9 ('float')
               LOAD_NAME               24 (__annotations__)
               LOAD_CONST              10 ('_TTL_SECONDS')
               STORE_SUBSCR

  61           BUILD_MAP                0
               STORE_NAME              25 (_CACHE)
               LOAD_CONST              11 ('Dict[str, Tuple[float, Dict[str, Any]]]')
               LOAD_NAME               24 (__annotations__)
               LOAD_CONST              12 ('_CACHE')
               STORE_SUBSCR

  63           LOAD_CONST              13 ('hits')
               LOAD_SMALL_INT           0

  64           LOAD_CONST              14 ('misses')
               LOAD_SMALL_INT           0

  65           LOAD_CONST              15 ('writes')
               LOAD_SMALL_INT           0

  66           LOAD_CONST              16 ('invalidations')
               LOAD_SMALL_INT           0

  67           LOAD_CONST              17 ('errors')
               LOAD_SMALL_INT           0

  62           BUILD_MAP                5
               STORE_NAME              26 (_STATS)

  72           LOAD_CONST              18 ('fleet.brokerage_health')
               STORE_NAME              27 (_SURFACE_HEALTH)

  73           LOAD_CONST              19 ('fleet.chain_status')
               STORE_NAME              28 (_SURFACE_CHAIN)

  74           LOAD_CONST              20 ('fleet.rollout_readiness')
               STORE_NAME              29 (_SURFACE_ROLLOUT)

  75           LOAD_CONST              21 ('fleet.exceptions')
               STORE_NAME              30 (_SURFACE_EXCEPT)

  82           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\fleet_status_cache.py", line 82>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object _now at 0x0000018C17FA2C40, file "app\services\operator\fleet_status_cache.py", line 82>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              31 (_now)

  86           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\fleet_status_cache.py", line 86>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _normalise_ids at 0x0000018C1794EBB0, file "app\services\operator\fleet_status_cache.py", line 86>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              32 (_normalise_ids)

  99           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025530, file "app\services\operator\fleet_status_cache.py", line 99>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object _key at 0x0000018C180533F0, file "app\services\operator\fleet_status_cache.py", line 99>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              33 (_key)

 103           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\fleet_status_cache.py", line 103>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object _safe_int at 0x0000018C18038CB0, file "app\services\operator\fleet_status_cache.py", line 103>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              34 (_safe_int)

 115           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\fleet_status_cache.py", line 115>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _store at 0x0000018C17D8E300, file "app\services\operator\fleet_status_cache.py", line 115>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              35 (_store)

 125           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\fleet_status_cache.py", line 125>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _lookup at 0x0000018C17D6DFC0, file "app\services\operator\fleet_status_cache.py", line 125>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              36 (_lookup)

 145           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C18025030, file "app\services\operator\fleet_status_cache.py", line 145>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object _wrap at 0x0000018C181F3A80, file "app\services\operator\fleet_status_cache.py", line 145>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              37 (_wrap)

 191           LOAD_CONST              36 ('brokerage_ids')

 193           LOAD_CONST               2 (None)

 191           LOAD_CONST              37 ('limit')

 194           LOAD_SMALL_INT          50

 191           BUILD_MAP                2
               LOAD_CONST              38 (<code object __annotate__ at 0x0000018C18026130, file "app\services\operator\fleet_status_cache.py", line 191>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object get_fleet_brokerage_health_summary at 0x0000018C180C4360, file "app\services\operator\fleet_status_cache.py", line 191>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              38 (get_fleet_brokerage_health_summary)

 207           LOAD_CONST              36 ('brokerage_ids')

 209           LOAD_CONST               2 (None)

 207           LOAD_CONST              37 ('limit')

 210           LOAD_SMALL_INT          50

 207           BUILD_MAP                2
               LOAD_CONST              40 (<code object __annotate__ at 0x0000018C18026230, file "app\services\operator\fleet_status_cache.py", line 207>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object get_fleet_chain_status_report at 0x0000018C180C4580, file "app\services\operator\fleet_status_cache.py", line 207>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              39 (get_fleet_chain_status_report)

 223           LOAD_CONST              36 ('brokerage_ids')

 225           LOAD_CONST               2 (None)

 223           LOAD_CONST              37 ('limit')

 226           LOAD_SMALL_INT          50

 223           BUILD_MAP                2
               LOAD_CONST              42 (<code object __annotate__ at 0x0000018C18026330, file "app\services\operator\fleet_status_cache.py", line 223>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object get_fleet_rollout_readiness_summary at 0x0000018C180C4690, file "app\services\operator\fleet_status_cache.py", line 223>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              40 (get_fleet_rollout_readiness_summary)

 239           LOAD_CONST              36 ('brokerage_ids')

 241           LOAD_CONST               2 (None)

 239           LOAD_CONST              37 ('limit')

 242           LOAD_SMALL_INT          50

 239           BUILD_MAP                2
               LOAD_CONST              44 (<code object __annotate__ at 0x0000018C18026430, file "app\services\operator\fleet_status_cache.py", line 239>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object get_fleet_exception_report at 0x0000018C180C47A0, file "app\services\operator\fleet_status_cache.py", line 239>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              41 (get_fleet_exception_report)

 255           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\fleet_status_cache.py", line 255>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object invalidate_for_brokerage at 0x0000018C181B4450, file "app\services\operator\fleet_status_cache.py", line 255>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (invalidate_for_brokerage)

 310           LOAD_CONST              48 ('surface')
               LOAD_CONST               2 (None)
               BUILD_MAP                1
               LOAD_CONST              49 (<code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\fleet_status_cache.py", line 310>)
               MAKE_FUNCTION
               LOAD_CONST              50 (<code object invalidate at 0x0000018C17E94F70, file "app\services\operator\fleet_status_cache.py", line 310>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
               STORE_NAME              43 (invalidate)

 347           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\fleet_status_cache.py", line 347>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object cache_stats at 0x0000018C17F5F9F0, file "app\services\operator\fleet_status_cache.py", line 347>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (cache_stats)

 364           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\fleet_status_cache.py", line 364>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object configure_ttl at 0x0000018C179C3A50, file "app\services\operator\fleet_status_cache.py", line 364>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (configure_ttl)
               LOAD_CONST               2 (None)
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3960, file "app\services\operator\fleet_status_cache.py", line 82>:
 82           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('float')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object _now at 0x0000018C17FA2C40, file "app\services\operator\fleet_status_cache.py", line 82>:
 82           RESUME                   0

 83           LOAD_GLOBAL              1 (monotonic + NULL)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA32D0, file "app\services\operator\fleet_status_cache.py", line 86>:
 86           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')
              LOAD_CONST               2 ('Optional[Iterable[Any]]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[str, ...]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _normalise_ids at 0x0000018C1794EBB0, file "app\services\operator\fleet_status_cache.py", line 86>:
 86           RESUME                   0

 87           LOAD_FAST_BORROW         0 (brokerage_ids)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

 88           LOAD_CONST               1 (())
              RETURN_VALUE

 89   L1:     BUILD_LIST               0
              STORE_FAST               1 (out)

 90           LOAD_FAST_BORROW         0 (brokerage_ids)
              GET_ITER
      L2:     FOR_ITER                70 (to L5)
              STORE_FAST               2 (v)

 91           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         2 (v)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L3)
              NOT_TAKEN
              JUMP_BACKWARD           27 (to L2)

 92   L3:     LOAD_FAST_BORROW         2 (v)
              LOAD_ATTR                5 (strip + NULL|self)
              CALL                     0
              STORE_FAST               3 (s)

 93           LOAD_FAST_BORROW         3 (s)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              JUMP_BACKWARD           53 (to L2)

 94   L4:     LOAD_FAST_BORROW         1 (out)
              LOAD_ATTR                7 (append + NULL|self)
              LOAD_FAST_BORROW         3 (s)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           72 (to L2)

 90   L5:     END_FOR
              POP_ITER

 95           LOAD_GLOBAL              9 (sorted + NULL)
              LOAD_GLOBAL             11 (set + NULL)
              LOAD_FAST_BORROW         1 (out)
              CALL                     1
              CALL                     1
              STORE_FAST               1 (out)

 96           LOAD_GLOBAL             13 (tuple + NULL)
              LOAD_FAST_BORROW         1 (out)
              LOAD_CONST               0 (slice(None, 200, None))
              BINARY_OP               26 ([])
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025530, file "app\services\operator\fleet_status_cache.py", line 99>:
 99           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('ids')
              LOAD_CONST               4 ('Tuple[str, ...]')
              LOAD_CONST               5 ('limit')
              LOAD_CONST               6 ('int')
              LOAD_CONST               7 ('return')
              LOAD_CONST               2 ('str')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _key at 0x0000018C180533F0, file "app\services\operator\fleet_status_cache.py", line 99>:
 99           RESUME                   0

100           LOAD_FAST_BORROW         0 (surface)
              FORMAT_SIMPLE
              LOAD_CONST               0 ('|limit=')
              LOAD_GLOBAL              1 (int + NULL)
              LOAD_FAST_BORROW         2 (limit)
              CALL                     1
              FORMAT_SIMPLE
              LOAD_CONST               1 ('|ids=')
              LOAD_CONST               2 (',')
              LOAD_ATTR                3 (join + NULL|self)
              LOAD_FAST_BORROW         1 (ids)
              CALL                     1
              FORMAT_SIMPLE
              BUILD_STRING             5
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024C30, file "app\services\operator\fleet_status_cache.py", line 103>:
103           RESUME                   0
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

Disassembly of <code object _safe_int at 0x0000018C18038CB0, file "app\services\operator\fleet_status_cache.py", line 103>:
 103           RESUME                   0

 104           NOP

 105   L1:     LOAD_GLOBAL              1 (int + NULL)
               LOAD_FAST_BORROW         0 (value)
               CALL                     1
               STORE_FAST               4 (v)

 108   L2:     LOAD_FAST_LOAD_FAST     65 (v, lo)
               COMPARE_OP              18 (bool(<))
               POP_JUMP_IF_FALSE        3 (to L3)
               NOT_TAKEN

 109           LOAD_FAST                1 (lo)
               RETURN_VALUE

 110   L3:     LOAD_FAST_LOAD_FAST     66 (v, hi)
               COMPARE_OP             148 (bool(>))
               POP_JUMP_IF_FALSE        3 (to L4)
               NOT_TAKEN

 111           LOAD_FAST                2 (hi)
               RETURN_VALUE

 112   L4:     LOAD_FAST                4 (v)
               RETURN_VALUE

  --   L5:     PUSH_EXC_INFO

 106           LOAD_GLOBAL              2 (TypeError)
               LOAD_GLOBAL              4 (ValueError)
               BUILD_TUPLE              2
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L7)
               NOT_TAKEN
               POP_TOP

 107           LOAD_FAST                3 (default)
               SWAP                     2
       L6:     POP_EXCEPT
               RETURN_VALUE

 106   L7:     RERAISE                  0

  --   L8:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L5 [0]
  L5 to L6 -> L8 [1] lasti
  L7 to L8 -> L8 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "app\services\operator\fleet_status_cache.py", line 115>:
115           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('key')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('payload')
              LOAD_CONST               4 ('Dict[str, Any]')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('None')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _store at 0x0000018C17D8E300, file "app\services\operator\fleet_status_cache.py", line 115>:
 115            RESUME                   0

 116            NOP

 117    L1:     LOAD_GLOBAL              0 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 118            LOAD_GLOBAL              3 (_now + NULL)
                CALL                     0
                LOAD_FAST_BORROW         1 (payload)
                BUILD_TUPLE              2
                LOAD_GLOBAL              4 (_CACHE)
                LOAD_FAST_BORROW         0 (key)
                STORE_SUBSCR

 119            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               0 ('writes')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               0 ('writes')
                STORE_SUBSCR

 117    L3:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
        L4:     LOAD_CONST               1 (None)
                RETURN_VALUE
        L5:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L6)
                NOT_TAKEN
                RERAISE                  2
        L6:     POP_TOP
        L7:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
        L8:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --    L9:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L10:     PUSH_EXC_INFO

 120            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       85 (to L19)
                NOT_TAKEN
                POP_TOP

 121            LOAD_GLOBAL              0 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L11:     POP_TOP

 122            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('errors')
                STORE_SUBSCR

 121   L12:     LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
       L13:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE
       L14:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L15)
                NOT_TAKEN
                RERAISE                  2
       L15:     POP_TOP
       L16:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
       L17:     POP_EXCEPT
                LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 120   L19:     RERAISE                  0

  --   L20:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L10 [0]
  L2 to L3 -> L5 [2] lasti
  L3 to L4 -> L10 [0]
  L5 to L7 -> L9 [4] lasti
  L7 to L8 -> L10 [0]
  L9 to L10 -> L10 [0]
  L10 to L11 -> L20 [1] lasti
  L11 to L12 -> L14 [3] lasti
  L12 to L13 -> L20 [1] lasti
  L14 to L16 -> L18 [5] lasti
  L16 to L17 -> L20 [1] lasti
  L18 to L20 -> L20 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA34B0, file "app\services\operator\fleet_status_cache.py", line 125>:
125           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('key')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[Dict[str, Any]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _lookup at 0x0000018C17D6DFC0, file "app\services\operator\fleet_status_cache.py", line 125>:
 125            RESUME                   0

 126            NOP

 127    L1:     LOAD_GLOBAL              0 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 128            LOAD_GLOBAL              2 (_CACHE)
                LOAD_ATTR                5 (get + NULL|self)
                LOAD_FAST_BORROW         0 (key)
                CALL                     1
                STORE_FAST               1 (entry)

 129            LOAD_FAST_BORROW         1 (entry)
                POP_JUMP_IF_NOT_NONE    48 (to L5)
                NOT_TAKEN

 130            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               1 ('misses')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               1 ('misses')
                STORE_SUBSCR

 131            NOP

 127    L3:     LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
        L4:     LOAD_CONST               0 (None)
                RETURN_VALUE

 132    L5:     LOAD_FAST_BORROW         1 (entry)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST   35 (ts, payload)

 133            LOAD_GLOBAL             11 (_now + NULL)
                CALL                     0
                LOAD_FAST_BORROW         2 (ts)
                BINARY_OP               10 (-)
                LOAD_GLOBAL             12 (_TTL_SECONDS)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       70 (to L8)
                NOT_TAKEN

 134            LOAD_GLOBAL              2 (_CACHE)
                LOAD_ATTR               15 (pop + NULL|self)
                LOAD_FAST_BORROW         0 (key)
                LOAD_CONST               0 (None)
                CALL                     2
                POP_TOP

 135            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               1 ('misses')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               1 ('misses')
                STORE_SUBSCR

 136            NOP

 127    L6:     LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
        L7:     LOAD_CONST               0 (None)
                RETURN_VALUE

 137    L8:     LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('hits')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               2 ('hits')
                STORE_SUBSCR

 138            LOAD_FAST_BORROW         3 (payload)

 127    L9:     SWAP                     3
                SWAP                     2
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
       L10:     RETURN_VALUE
       L11:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L12)
                NOT_TAKEN
                RERAISE                  2
       L12:     POP_TOP
       L13:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
       L14:     LOAD_CONST               0 (None)
                RETURN_VALUE

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L16:     PUSH_EXC_INFO

 139            LOAD_GLOBAL             16 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       84 (to L24)
                NOT_TAKEN
                POP_TOP

 140            LOAD_GLOBAL              0 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L17:     POP_TOP

 141            LOAD_GLOBAL              7 (int + NULL)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               3 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL              8 (_STATS)
                LOAD_CONST               3 ('errors')
                STORE_SUBSCR

 140   L18:     LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                LOAD_CONST               0 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L23)
       L19:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L20)
                NOT_TAKEN
                RERAISE                  2
       L20:     POP_TOP
       L21:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L23)

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 142   L23:     POP_EXCEPT
                LOAD_CONST               0 (None)
                RETURN_VALUE

 139   L24:     RERAISE                  0

  --   L25:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L16 [0]
  L2 to L3 -> L11 [2] lasti
  L3 to L4 -> L16 [0]
  L5 to L6 -> L11 [2] lasti
  L6 to L7 -> L16 [0]
  L8 to L9 -> L11 [2] lasti
  L9 to L10 -> L16 [0]
  L11 to L13 -> L15 [4] lasti
  L13 to L14 -> L16 [0]
  L15 to L16 -> L16 [0]
  L16 to L17 -> L25 [1] lasti
  L17 to L18 -> L19 [3] lasti
  L18 to L19 -> L25 [1] lasti
  L19 to L21 -> L22 [5] lasti
  L21 to L23 -> L25 [1] lasti
  L24 to L25 -> L25 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18025030, file "app\services\operator\fleet_status_cache.py", line 145>:
145           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')

146           LOAD_CONST               2 ('str')

145           LOAD_CONST               3 ('fn')

147           LOAD_CONST               4 ('Callable[..., Dict[str, Any]]')

145           LOAD_CONST               5 ('brokerage_ids')

148           LOAD_CONST               6 ('Optional[Iterable[Any]]')

145           LOAD_CONST               7 ('limit')

149           LOAD_CONST               8 ('Any')

145           LOAD_CONST               9 ('return')

150           LOAD_CONST              10 ('Dict[str, Any]')

145           BUILD_MAP                5
              RETURN_VALUE

Disassembly of <code object _wrap at 0x0000018C181F3A80, file "app\services\operator\fleet_status_cache.py", line 145>:
 145            RESUME                   0

 151            LOAD_GLOBAL              1 (_safe_int + NULL)
                LOAD_FAST_BORROW         3 (limit)
                LOAD_SMALL_INT           1
                LOAD_SMALL_INT         200
                LOAD_SMALL_INT          50
                LOAD_CONST               1 (('lo', 'hi', 'default'))
                CALL_KW                  4
                STORE_FAST               4 (capped)

 152            LOAD_GLOBAL              3 (_normalise_ids + NULL)
                LOAD_FAST_BORROW         2 (brokerage_ids)
                CALL                     1
                STORE_FAST               5 (ids)

 153            LOAD_GLOBAL              5 (_key + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 5 (surface, ids)
                LOAD_FAST_BORROW         4 (capped)
                CALL                     3
                STORE_FAST               6 (key)

 154            LOAD_GLOBAL              7 (_lookup + NULL)
                LOAD_FAST_BORROW         6 (key)
                CALL                     1
                STORE_FAST               7 (hit)

 155            LOAD_FAST_BORROW         7 (hit)
                POP_JUMP_IF_NONE        13 (to L3)
                NOT_TAKEN

 157            NOP

 158    L1:     LOAD_GLOBAL              9 (dict + NULL)
                LOAD_FAST_BORROW         7 (hit)
                CALL                     1
        L2:     RETURN_VALUE

 161    L3:     NOP

 162    L4:     LOAD_FAST                1 (fn)
                PUSH_NULL
                LOAD_FAST                2 (brokerage_ids)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE        22 (to L9)
        L5:     NOT_TAKEN
        L6:     POP_TOP
                LOAD_GLOBAL             13 (list + NULL)
                LOAD_FAST_BORROW         5 (ids)
                CALL                     1
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L9)
        L7:     NOT_TAKEN
        L8:     POP_TOP
                LOAD_CONST               2 (None)

 163    L9:     LOAD_FAST_BORROW         4 (capped)

 162            LOAD_CONST               3 (('brokerage_ids', 'limit'))
                CALL_KW                  2
                STORE_FAST               8 (result)

 177   L10:     LOAD_GLOBAL             23 (isinstance + NULL)
                LOAD_FAST                8 (result)
                LOAD_GLOBAL              8 (dict)
                CALL                     2
                TO_BOOL
                POP_JUMP_IF_FALSE       36 (to L11)
                NOT_TAKEN

 181            LOAD_FAST                8 (result)
                LOAD_ATTR               25 (get + NULL|self)
                LOAD_CONST               6 ('status')
                CALL                     1
                STORE_FAST              10 (st)

 182            LOAD_FAST               10 (st)
                LOAD_CONST              16 (('ok', 'skipped'))
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       12 (to L11)
                NOT_TAKEN

 183            LOAD_GLOBAL             27 (_store + NULL)
                LOAD_FAST_LOAD_FAST    104 (key, result)
                CALL                     2
                POP_TOP

 184   L11:     LOAD_FAST                8 (result)
                RETURN_VALUE

  --   L12:     PUSH_EXC_INFO

 159            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        4 (to L14)
                NOT_TAKEN
                POP_TOP

 160   L13:     POP_EXCEPT
                JUMP_BACKWARD_NO_INTERRUPT 112 (to L3)

 159   L14:     RERAISE                  0

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L16:     PUSH_EXC_INFO

 164            LOAD_GLOBAL             10 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       97 (to L21)
                NOT_TAKEN
                STORE_FAST               9 (e)

 165   L17:     LOAD_GLOBAL             14 (logger)
                LOAD_ATTR               17 (warning + NULL|self)

 166            LOAD_CONST               4 ('fleet_status_cache underlying surface=')
                LOAD_FAST                0 (surface)
                FORMAT_SIMPLE
                LOAD_CONST               5 (' failed type=')

 167            LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE

 166            BUILD_STRING             4

 165            CALL                     1
                POP_TOP

 170            LOAD_CONST               6 ('status')
                LOAD_CONST               7 ('skipped')

 171            LOAD_CONST               8 ('surface')
                LOAD_CONST               9 ('ops.')
                LOAD_FAST                0 (surface)
                FORMAT_SIMPLE
                BUILD_STRING             2

 172            LOAD_CONST              10 ('rows')
                BUILD_LIST               0

 173            LOAD_CONST              11 ('count')
                LOAD_SMALL_INT           0

 174            LOAD_CONST              12 ('warnings')
                LOAD_CONST              13 ('underlying_failed:')
                LOAD_GLOBAL             19 (type + NULL)
                LOAD_FAST                9 (e)
                CALL                     1
                LOAD_ATTR               20 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2
                BUILD_LIST               1

 175            LOAD_CONST              14 ('error_code')
                LOAD_CONST              15 ('underlying_failed')

 169            BUILD_MAP                6
       L18:     SWAP                     2
       L19:     POP_EXCEPT
                LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RETURN_VALUE

  --   L20:     LOAD_CONST               2 (None)
                STORE_FAST               9 (e)
                DELETE_FAST              9 (e)
                RERAISE                  1

 164   L21:     RERAISE                  0

  --   L22:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L12 [0]
  L4 to L5 -> L16 [0]
  L6 to L7 -> L16 [0]
  L8 to L10 -> L16 [0]
  L12 to L13 -> L15 [1] lasti
  L14 to L15 -> L15 [1] lasti
  L16 to L17 -> L22 [1] lasti
  L17 to L18 -> L20 [1] lasti
  L18 to L19 -> L22 [1] lasti
  L20 to L22 -> L22 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "app\services\operator\fleet_status_cache.py", line 191>:
191           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

193           LOAD_CONST               2 ('Optional[Iterable[Any]]')

191           LOAD_CONST               3 ('limit')

194           LOAD_CONST               4 ('Any')

191           LOAD_CONST               5 ('return')

195           LOAD_CONST               6 ('Dict[str, Any]')

191           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_brokerage_health_summary at 0x0000018C180C4360, file "app\services\operator\fleet_status_cache.py", line 191>:
191           RESUME                   0

196           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('fleet_brokerage_health_summary',))
              IMPORT_NAME              0 (app.services.operator.fleet_status)
              IMPORT_FROM              1 (fleet_brokerage_health_summary)
              STORE_FAST               2 (fleet_brokerage_health_summary)
              POP_TOP

199           LOAD_GLOBAL              5 (_wrap + NULL)

200           LOAD_GLOBAL              6 (_SURFACE_HEALTH)

201           LOAD_FAST_BORROW         2 (fleet_brokerage_health_summary)

202           LOAD_FAST_BORROW         0 (brokerage_ids)

203           LOAD_FAST_BORROW         1 (limit)

199           CALL                     4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026230, file "app\services\operator\fleet_status_cache.py", line 207>:
207           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

209           LOAD_CONST               2 ('Optional[Iterable[Any]]')

207           LOAD_CONST               3 ('limit')

210           LOAD_CONST               4 ('Any')

207           LOAD_CONST               5 ('return')

211           LOAD_CONST               6 ('Dict[str, Any]')

207           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_chain_status_report at 0x0000018C180C4580, file "app\services\operator\fleet_status_cache.py", line 207>:
207           RESUME                   0

212           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('fleet_chain_status_report',))
              IMPORT_NAME              0 (app.services.operator.fleet_status)
              IMPORT_FROM              1 (fleet_chain_status_report)
              STORE_FAST               2 (fleet_chain_status_report)
              POP_TOP

215           LOAD_GLOBAL              5 (_wrap + NULL)

216           LOAD_GLOBAL              6 (_SURFACE_CHAIN)

217           LOAD_FAST_BORROW         2 (fleet_chain_status_report)

218           LOAD_FAST_BORROW         0 (brokerage_ids)

219           LOAD_FAST_BORROW         1 (limit)

215           CALL                     4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026330, file "app\services\operator\fleet_status_cache.py", line 223>:
223           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

225           LOAD_CONST               2 ('Optional[Iterable[Any]]')

223           LOAD_CONST               3 ('limit')

226           LOAD_CONST               4 ('Any')

223           LOAD_CONST               5 ('return')

227           LOAD_CONST               6 ('Dict[str, Any]')

223           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_rollout_readiness_summary at 0x0000018C180C4690, file "app\services\operator\fleet_status_cache.py", line 223>:
223           RESUME                   0

228           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('fleet_rollout_readiness_summary',))
              IMPORT_NAME              0 (app.services.operator.fleet_status)
              IMPORT_FROM              1 (fleet_rollout_readiness_summary)
              STORE_FAST               2 (fleet_rollout_readiness_summary)
              POP_TOP

231           LOAD_GLOBAL              5 (_wrap + NULL)

232           LOAD_GLOBAL              6 (_SURFACE_ROLLOUT)

233           LOAD_FAST_BORROW         2 (fleet_rollout_readiness_summary)

234           LOAD_FAST_BORROW         0 (brokerage_ids)

235           LOAD_FAST_BORROW         1 (limit)

231           CALL                     4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026430, file "app\services\operator\fleet_status_cache.py", line 239>:
239           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('brokerage_ids')

241           LOAD_CONST               2 ('Optional[Iterable[Any]]')

239           LOAD_CONST               3 ('limit')

242           LOAD_CONST               4 ('Any')

239           LOAD_CONST               5 ('return')

243           LOAD_CONST               6 ('Dict[str, Any]')

239           BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object get_fleet_exception_report at 0x0000018C180C47A0, file "app\services\operator\fleet_status_cache.py", line 239>:
239           RESUME                   0

244           LOAD_SMALL_INT           0
              LOAD_CONST               1 (('fleet_exception_report',))
              IMPORT_NAME              0 (app.services.operator.fleet_status)
              IMPORT_FROM              1 (fleet_exception_report)
              STORE_FAST               2 (fleet_exception_report)
              POP_TOP

247           LOAD_GLOBAL              5 (_wrap + NULL)

248           LOAD_GLOBAL              6 (_SURFACE_EXCEPT)

249           LOAD_FAST_BORROW         2 (fleet_exception_report)

250           LOAD_FAST_BORROW         0 (brokerage_ids)

251           LOAD_FAST_BORROW         1 (limit)

247           CALL                     4
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2100, file "app\services\operator\fleet_status_cache.py", line 255>:
255           RESUME                   0
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

Disassembly of <code object invalidate_for_brokerage at 0x0000018C181B4450, file "app\services\operator\fleet_status_cache.py", line 255>:
 255            RESUME                   0

 267            NOP

 268    L1:     LOAD_FAST                0 (brokerage_id)
                COPY                     1
                TO_BOOL
                POP_JUMP_IF_TRUE         3 (to L4)
        L2:     NOT_TAKEN
        L3:     POP_TOP
                LOAD_CONST               1 ('')
        L4:     LOAD_ATTR                1 (strip + NULL|self)
                CALL                     0
                STORE_FAST               1 (bid)

 269            LOAD_FAST_BORROW         1 (bid)
                TO_BOOL
                POP_JUMP_IF_TRUE        11 (to L8)
        L5:     NOT_TAKEN

 270    L6:     LOAD_CONST               2 ('status')
                LOAD_CONST               3 ('failed')
                LOAD_CONST               4 ('cleared')
                LOAD_SMALL_INT           0

 271            LOAD_CONST               5 ('scope')
                LOAD_CONST               6 ('per_brokerage')

 272            LOAD_CONST               7 ('error_code')
                LOAD_CONST               8 ('invalid_brokerage_id')

 270            BUILD_MAP                4
        L7:     RETURN_VALUE

 273    L8:     LOAD_SMALL_INT           0
                STORE_FAST               2 (removed)

 274            LOAD_GLOBAL              2 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L9:     POP_TOP

 275            LOAD_GLOBAL              5 (list + NULL)
                LOAD_GLOBAL              6 (_CACHE)
                LOAD_ATTR                9 (keys + NULL|self)
                CALL                     0
                CALL                     1
                GET_ITER
       L10:     FOR_ITER               199 (to L21)
                STORE_FAST               3 (key)

 277            LOAD_CONST               9 ('|ids=')
                STORE_FAST               4 (ids_marker)

 278            LOAD_FAST_BORROW         3 (key)
                LOAD_ATTR               11 (find + NULL|self)
                LOAD_FAST_BORROW         4 (ids_marker)
                CALL                     1
                STORE_FAST               5 (idx)

 279            LOAD_FAST_BORROW         5 (idx)
                LOAD_SMALL_INT           0
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        3 (to L11)
                NOT_TAKEN

 280            JUMP_BACKWARD           31 (to L10)

 281   L11:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (key, idx)
                LOAD_GLOBAL             13 (len + NULL)
                LOAD_FAST_BORROW         4 (ids_marker)
                CALL                     1
                BINARY_OP                0 (+)
                LOAD_CONST              10 (None)
                BINARY_SLICE
                STORE_FAST               6 (ids_csv)

 283            LOAD_FAST_LOAD_FAST     22 (bid, ids_csv)
                LOAD_ATTR               15 (split + NULL|self)
                LOAD_CONST              11 (',')
                CALL                     1
                GET_ITER
                LOAD_FAST_AND_CLEAR      7 (c)
                SWAP                     2
       L12:     BUILD_LIST               0
                SWAP                     2
       L13:     FOR_ITER                42 (to L16)
                STORE_FAST_LOAD_FAST   119 (c, c)
                LOAD_ATTR                1 (strip + NULL|self)
                CALL                     0
                TO_BOOL
       L14:     POP_JUMP_IF_TRUE         3 (to L15)
                NOT_TAKEN
                JUMP_BACKWARD           26 (to L13)
       L15:     LOAD_FAST_BORROW         7 (c)
                LOAD_ATTR                1 (strip + NULL|self)
                CALL                     0
                LIST_APPEND              2
                JUMP_BACKWARD           44 (to L13)
       L16:     END_FOR
                POP_ITER
       L17:     SWAP                     2
                STORE_FAST               7 (c)
                CONTAINS_OP              0 (in)
                POP_JUMP_IF_FALSE       34 (to L18)
                NOT_TAKEN

 284            LOAD_GLOBAL              6 (_CACHE)
                LOAD_ATTR               17 (pop + NULL|self)
                LOAD_FAST_BORROW         3 (key)
                LOAD_CONST              10 (None)
                CALL                     2
                POP_TOP

 285            LOAD_FAST_BORROW         2 (removed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (removed)
                JUMP_BACKWARD          158 (to L10)

 289   L18:     LOAD_FAST_BORROW         6 (ids_csv)
                TO_BOOL
       L19:     POP_JUMP_IF_FALSE        3 (to L20)
                NOT_TAKEN
                JUMP_BACKWARD          168 (to L10)

 290   L20:     LOAD_GLOBAL              6 (_CACHE)
                LOAD_ATTR               17 (pop + NULL|self)
                LOAD_FAST_BORROW         3 (key)
                LOAD_CONST              10 (None)
                CALL                     2
                POP_TOP

 291            LOAD_FAST_BORROW         2 (removed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               2 (removed)
                JUMP_BACKWARD          201 (to L10)

 275   L21:     END_FOR
                POP_ITER

 292            LOAD_GLOBAL             19 (int + NULL)
                LOAD_GLOBAL             20 (_STATS)
                LOAD_CONST              12 ('invalidations')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             20 (_STATS)
                LOAD_CONST              12 ('invalidations')
                STORE_SUBSCR

 274   L22:     LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                CALL                     3
                POP_TOP

 294   L23:     LOAD_CONST               2 ('status')
                LOAD_CONST              13 ('ok')

 295            LOAD_CONST               4 ('cleared')
                LOAD_FAST_BORROW         2 (removed)

 296            LOAD_CONST               5 ('scope')
                LOAD_CONST              14 ('brokerage:')
                LOAD_FAST_BORROW         1 (bid)
                FORMAT_SIMPLE
                BUILD_STRING             2

 293            BUILD_MAP                3
       L24:     RETURN_VALUE

  --   L25:     SWAP                     2
                POP_TOP

 283            SWAP                     2
                STORE_FAST               7 (c)
                RERAISE                  0

 274   L26:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L27)
                NOT_TAKEN
                RERAISE                  2
       L27:     POP_TOP
       L28:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 32 (to L23)

  --   L29:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L30:     PUSH_EXC_INFO

 298            LOAD_GLOBAL             22 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE      165 (to L42)
                NOT_TAKEN
                STORE_FAST               8 (e)

 299   L31:     LOAD_GLOBAL             24 (logger)
                LOAD_ATTR               27 (warning + NULL|self)

 300            LOAD_CONST              15 ('fleet_status_cache invalidate_for_brokerage error type=')

 301            LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE

 300            BUILD_STRING             2

 299            CALL                     1
                POP_TOP

 303            LOAD_GLOBAL              2 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
       L32:     POP_TOP

 304            LOAD_GLOBAL             19 (int + NULL)
                LOAD_GLOBAL             20 (_STATS)
                LOAD_CONST              16 ('errors')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             20 (_STATS)
                LOAD_CONST              16 ('errors')
                STORE_SUBSCR

 303   L33:     LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                CALL                     3
                POP_TOP
                JUMP_FORWARD            19 (to L38)
       L34:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L35)
                NOT_TAKEN
                RERAISE                  2
       L35:     POP_TOP
       L36:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_FORWARD             3 (to L38)

  --   L37:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 305   L38:     LOAD_CONST               2 ('status')
                LOAD_CONST              17 ('skipped')
                LOAD_CONST               4 ('cleared')
                LOAD_SMALL_INT           0

 306            LOAD_CONST               5 ('scope')
                LOAD_CONST               6 ('per_brokerage')

 307            LOAD_CONST               7 ('error_code')
                LOAD_CONST              18 ('unexpected:')
                LOAD_GLOBAL             29 (type + NULL)
                LOAD_FAST                8 (e)
                CALL                     1
                LOAD_ATTR               30 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 305            BUILD_MAP                4
       L39:     SWAP                     2
       L40:     POP_EXCEPT
                LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RETURN_VALUE

  --   L41:     LOAD_CONST              10 (None)
                STORE_FAST               8 (e)
                DELETE_FAST              8 (e)
                RERAISE                  1

 298   L42:     RERAISE                  0

  --   L43:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L30 [0]
  L3 to L5 -> L30 [0]
  L6 to L7 -> L30 [0]
  L8 to L9 -> L30 [0]
  L9 to L12 -> L26 [2] lasti
  L12 to L14 -> L25 [6]
  L15 to L17 -> L25 [6]
  L17 to L19 -> L26 [2] lasti
  L20 to L22 -> L26 [2] lasti
  L22 to L24 -> L30 [0]
  L25 to L26 -> L26 [2] lasti
  L26 to L28 -> L29 [4] lasti
  L28 to L30 -> L30 [0]
  L30 to L31 -> L43 [1] lasti
  L31 to L32 -> L41 [1] lasti
  L32 to L33 -> L34 [3] lasti
  L33 to L34 -> L41 [1] lasti
  L34 to L36 -> L37 [5] lasti
  L36 to L39 -> L41 [1] lasti
  L39 to L40 -> L43 [1] lasti
  L41 to L43 -> L43 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2970, file "app\services\operator\fleet_status_cache.py", line 310>:
310           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('surface')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object invalidate at 0x0000018C17E94F70, file "app\services\operator\fleet_status_cache.py", line 310>:
 310            RESUME                   0

 314            NOP

 315    L1:     LOAD_GLOBAL              0 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     POP_TOP

 316            LOAD_FAST_BORROW         0 (surface)
                POP_JUMP_IF_NOT_NONE    90 (to L5)
                NOT_TAKEN

 317            LOAD_GLOBAL              3 (len + NULL)
                LOAD_GLOBAL              4 (_CACHE)
                CALL                     1
                STORE_FAST               1 (count)

 318            LOAD_GLOBAL              4 (_CACHE)
                LOAD_ATTR                7 (clear + NULL|self)
                CALL                     0
                POP_TOP

 319            LOAD_GLOBAL              9 (int + NULL)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               2 ('invalidations')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               2 ('invalidations')
                STORE_SUBSCR

 321            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('ok')

 322            LOAD_CONST               5 ('cleared')
                LOAD_FAST_BORROW         1 (count)

 323            LOAD_CONST               6 ('scope')
                LOAD_CONST               7 ('all')

 320            BUILD_MAP                3

 315    L3:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
        L4:     RETURN_VALUE

 325    L5:     LOAD_FAST_BORROW         0 (surface)
                FORMAT_SIMPLE
                LOAD_CONST               8 ('|')
                BUILD_STRING             2
                STORE_FAST               2 (prefix)

 326            LOAD_SMALL_INT           0
                STORE_FAST               3 (removed)

 327            LOAD_GLOBAL             13 (list + NULL)
                LOAD_GLOBAL              4 (_CACHE)
                LOAD_ATTR               15 (keys + NULL|self)
                CALL                     0
                CALL                     1
                GET_ITER
        L6:     FOR_ITER                59 (to L9)
                STORE_FAST               4 (k)

 328            LOAD_FAST_BORROW         4 (k)
                LOAD_ATTR               17 (startswith + NULL|self)
                LOAD_FAST_BORROW         2 (prefix)
                CALL                     1
                TO_BOOL
        L7:     POP_JUMP_IF_TRUE         3 (to L8)
                NOT_TAKEN
                JUMP_BACKWARD           28 (to L6)

 329    L8:     LOAD_GLOBAL              4 (_CACHE)
                LOAD_ATTR               19 (pop + NULL|self)
                LOAD_FAST_BORROW         4 (k)
                LOAD_CONST               1 (None)
                CALL                     2
                POP_TOP

 330            LOAD_FAST_BORROW         3 (removed)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               3 (removed)
                JUMP_BACKWARD           61 (to L6)

 327    L9:     END_FOR
                POP_ITER

 331            LOAD_GLOBAL              9 (int + NULL)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               2 ('invalidations')
                BINARY_OP               26 ([])
                CALL                     1
                LOAD_SMALL_INT           1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             10 (_STATS)
                LOAD_CONST               2 ('invalidations')
                STORE_SUBSCR

 333            LOAD_CONST               3 ('status')
                LOAD_CONST               4 ('ok')

 334            LOAD_CONST               5 ('cleared')
                LOAD_FAST_BORROW         3 (removed)

 335            LOAD_CONST               6 ('scope')
                LOAD_FAST_BORROW         0 (surface)

 332            BUILD_MAP                3

 315   L10:     SWAP                     3
                SWAP                     2
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                LOAD_CONST               1 (None)
                CALL                     3
                POP_TOP
       L11:     RETURN_VALUE
       L12:     PUSH_EXC_INFO
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
       L15:     LOAD_CONST               1 (None)
                RETURN_VALUE

  --   L16:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L17:     PUSH_EXC_INFO

 337            LOAD_GLOBAL             20 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       82 (to L22)
                NOT_TAKEN
                STORE_FAST               5 (e)

 338   L18:     LOAD_GLOBAL             22 (logger)
                LOAD_ATTR               25 (warning + NULL|self)

 339            LOAD_CONST               9 ('fleet_status_cache invalidate error type=')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 338            CALL                     1
                POP_TOP

 342            LOAD_CONST               3 ('status')
                LOAD_CONST              10 ('skipped')

 343            LOAD_CONST              11 ('error_code')
                LOAD_CONST              12 ('unexpected:')
                LOAD_GLOBAL             27 (type + NULL)
                LOAD_FAST                5 (e)
                CALL                     1
                LOAD_ATTR               28 (__name__)
                FORMAT_SIMPLE
                BUILD_STRING             2

 341            BUILD_MAP                2
       L19:     SWAP                     2
       L20:     POP_EXCEPT
                LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RETURN_VALUE

  --   L21:     LOAD_CONST               1 (None)
                STORE_FAST               5 (e)
                DELETE_FAST              5 (e)
                RERAISE                  1

 337   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L17 [0]
  L2 to L3 -> L12 [2] lasti
  L3 to L4 -> L17 [0]
  L5 to L7 -> L12 [2] lasti
  L8 to L10 -> L12 [2] lasti
  L10 to L11 -> L17 [0]
  L12 to L14 -> L16 [4] lasti
  L14 to L15 -> L17 [0]
  L16 to L17 -> L17 [0]
  L17 to L18 -> L23 [1] lasti
  L18 to L19 -> L21 [1] lasti
  L19 to L20 -> L23 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "app\services\operator\fleet_status_cache.py", line 347>:
347           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('return')
              LOAD_CONST               2 ('Dict[str, Any]')
              BUILD_MAP                1
              RETURN_VALUE

Disassembly of <code object cache_stats at 0x0000018C17F5F9F0, file "app\services\operator\fleet_status_cache.py", line 347>:
 347           RESUME                   0

 350           LOAD_GLOBAL              0 (_LOCK)
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     POP_TOP

 352           LOAD_CONST               1 ('status')
               LOAD_CONST               2 ('ok')

 353           LOAD_CONST               3 ('surface')
               LOAD_CONST               4 ('ops.fleet.cache_stats')

 354           LOAD_CONST               5 ('ttl_seconds')
               LOAD_GLOBAL              3 (float + NULL)
               LOAD_GLOBAL              4 (_TTL_SECONDS)
               CALL                     1

 355           LOAD_CONST               6 ('entries')
               LOAD_GLOBAL              7 (len + NULL)
               LOAD_GLOBAL              8 (_CACHE)
               CALL                     1

 356           LOAD_CONST               7 ('hits')
               LOAD_GLOBAL             11 (int + NULL)
               LOAD_GLOBAL             12 (_STATS)
               LOAD_CONST               7 ('hits')
               BINARY_OP               26 ([])
               CALL                     1

 357           LOAD_CONST               8 ('misses')
               LOAD_GLOBAL             11 (int + NULL)
               LOAD_GLOBAL             12 (_STATS)
               LOAD_CONST               8 ('misses')
               BINARY_OP               26 ([])
               CALL                     1

 358           LOAD_CONST               9 ('writes')
               LOAD_GLOBAL             11 (int + NULL)
               LOAD_GLOBAL             12 (_STATS)
               LOAD_CONST               9 ('writes')
               BINARY_OP               26 ([])
               CALL                     1

 359           LOAD_CONST              10 ('invalidations')
               LOAD_GLOBAL             11 (int + NULL)
               LOAD_GLOBAL             12 (_STATS)
               LOAD_CONST              10 ('invalidations')
               BINARY_OP               26 ([])
               CALL                     1

 360           LOAD_CONST              11 ('errors')
               LOAD_GLOBAL             11 (int + NULL)
               LOAD_GLOBAL             12 (_STATS)
               LOAD_CONST              11 ('errors')
               BINARY_OP               26 ([])
               CALL                     1

 351           BUILD_MAP                9

 350   L2:     SWAP                     3
               SWAP                     2
               LOAD_CONST              12 (None)
               LOAD_CONST              12 (None)
               LOAD_CONST              12 (None)
               CALL                     3
               POP_TOP
               RETURN_VALUE
       L3:     PUSH_EXC_INFO
               WITH_EXCEPT_START
               TO_BOOL
               POP_JUMP_IF_TRUE         2 (to L4)
               NOT_TAKEN
               RERAISE                  2
       L4:     POP_TOP
       L5:     POP_EXCEPT
               POP_TOP
               POP_TOP
               POP_TOP
               LOAD_CONST              12 (None)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2B50, file "app\services\operator\fleet_status_cache.py", line 364>:
364           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('seconds')
              LOAD_CONST               2 ('Any')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Dict[str, Any]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object configure_ttl at 0x0000018C179C3A50, file "app\services\operator\fleet_status_cache.py", line 364>:
 364            RESUME                   0

 367            NOP

 368    L1:     LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST_BORROW         0 (seconds)
                CALL                     1
                STORE_FAST               1 (v)

 371    L2:     LOAD_FAST                1 (v)
                LOAD_GLOBAL              6 (_TTL_MIN)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE        7 (to L3)
                NOT_TAKEN

 372            LOAD_GLOBAL              6 (_TTL_MIN)
                STORE_FAST               1 (v)

 373    L3:     LOAD_FAST                1 (v)
                LOAD_GLOBAL              8 (_TTL_MAX)
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE        7 (to L4)
                NOT_TAKEN

 374            LOAD_GLOBAL              8 (_TTL_MAX)
                STORE_FAST               1 (v)

 375    L4:     LOAD_GLOBAL             10 (_LOCK)
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L5:     POP_TOP

 376            LOAD_FAST                1 (v)
                STORE_GLOBAL             6 (_TTL_SECONDS)

 375    L6:     LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                CALL                     3
                POP_TOP

 377    L7:     LOAD_CONST               1 ('status')
                LOAD_CONST               6 ('ok')
                LOAD_CONST               7 ('ttl_seconds')
                LOAD_GLOBAL              1 (float + NULL)
                LOAD_FAST                1 (v)
                CALL                     1
                BUILD_MAP                2
                RETURN_VALUE

  --    L8:     PUSH_EXC_INFO

 369            LOAD_GLOBAL              2 (TypeError)
                LOAD_GLOBAL              4 (ValueError)
                BUILD_TUPLE              2
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       10 (to L10)
                NOT_TAKEN
                POP_TOP

 370            LOAD_CONST               1 ('status')
                LOAD_CONST               2 ('failed')
                LOAD_CONST               3 ('error_code')
                LOAD_CONST               4 ('invalid_ttl')
                BUILD_MAP                2
                SWAP                     2
        L9:     POP_EXCEPT
                RETURN_VALUE

 369   L10:     RERAISE                  0

  --   L11:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 375   L12:     PUSH_EXC_INFO
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
                JUMP_BACKWARD_NO_INTERRUPT 60 (to L7)

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L8 [0]
  L5 to L6 -> L12 [2] lasti
  L8 to L9 -> L11 [1] lasti
  L10 to L11 -> L11 [1] lasti
  L12 to L14 -> L15 [4] lasti
```
