# scripts_readiness/package_backup

- **pyc:** `scripts\__pycache__\package_backup.cpython-314.pyc`
- **expected source path (absent):** `scripts/package_backup.py`
- **co_filename (from bytecode):** `scripts\package_backup.py`
- **source present:** False
- **python magic:** `2b0e0d0a` (CPython 3.14)
- **subsystem:** scripts_readiness

## Module docstring

```
PAS143G — Encrypted offsite backup packaging.

Turns a verified PAS143D backup directory into a single
recovery_<timestamp>.pasbak archive that an operator can ship offsite
(USB / S3 / cold storage) without exposing raw dump bytes or PII.

Crypto contract:
  - Stdlib only (hashlib + hmac + secrets). No new deps.
  - KDF:  PBKDF2-HMAC-SHA256, 200,000 iterations, 64 bytes out
          → first 32 = encryption key, second 32 = MAC key.
  - Encryption: HMAC-CTR keystream XORed against the plaintext.
                (HMAC-SHA256(enc_key, nonce || counter_be_8) per 32-byte block.)
  - Integrity: HMAC-SHA256 over (magic|version|flags|lens|salt|nonce|header).
  - Per-archive 32-byte salt + 32-byte nonce, both via secrets.token_bytes.

Archive byte layout:
    MAGIC[8]      = b'PASBAK01'
    VERSION[1]    = 0x01
    FLAGS[1]      = 0x01 (encrypted)
    SALT_LEN[2]   = 0x0020 (BE)
    NONCE_LEN[2]  = 0x0020 (BE)
    HEADER_LEN[4] (BE)
    SALT[32]
    NONCE[32]
    HEADER_JSON[HEADER_LEN]   ← inspectable WITHOUT passphrase
    MAC[32]                    ← HMAC over everything above
    CIPHERTEXT[rest]           ← gzip-then-encrypt of the backup tarball

Operator contract:
  - Passphrase ONLY via env var (--passphrase-env VAR_NAME). Never on
    the command line. Never echoed. Empty/missing rejected.
  - Refuses to package an unverified backup unless --allow-unverified.
  - Refuses if the verification report flagged a checksum mismatch.

Usage:
  PAS_BAK_PASS=<phrase> python scripts/package_backup.py \
      --input-dir backups/20260509_141500/ \
      --output-dir recovery/ \
      --passphrase-env PAS_BAK_PASS

  python scripts/package_backup.py --inspect --input-dir backups/...
  python scripts/package_backup.py --dry-run    --input-dir backups/...

Exit codes:
    0  — packaged + manifest written (or dry-run / inspect succeeded)
    2  — bad CLI arguments
    3  — passphrase missing or empty
    4  — backup unverified and --allow-unverified not passed
    5  — backup verification recorded a hard failure (checksum etc.)
    6  — input directory missing or malformed
```

## Imports

`List`, `Optional`, `Path`, `Tuple`, `__future__`, `annotations`, `argparse`, `datetime`, `gzip`, `hashlib`, `hmac`, `io`, `json`, `os`, `pathlib`, `secrets`, `struct`, `sys`, `tarfile`, `typing`

## Classes

_none_

## Functions / methods

`__annotate__`, `_build_tar_gz`, `_hmac_ctr_stream`, `_read_passphrase`, `_resolve_output_path`, `_status`, `_walk_files`, `build_recovery_manifest`, `compute_mac`, `derive_keys`, `encrypt`, `has_checksum_mismatch`, `main`, `manifest_hash`, `now_stamp`, `read_archive_full`, `read_archive_header`, `read_backup_manifest`, `read_verification_report`, `serialize_manifest`, `verification_summary`, `verify_archive_mac_from_disk`, `write_archive`

## Env-key candidates

`ARCHIVE_VERSION`, `FAIL`, `FLAG_ENCRYPTED`, `KDF_DKLEN`, `KDF_ITERATIONS`, `MAC_LEN`, `MAGIC`, `NONCE_LEN`, `PASS`, `SALT_LEN`, `TOOL_VERSION`

## String constants (redacted where noted)

- "\nPAS143G — Encrypted offsite backup packaging.\n\nTurns a verified PAS143D backup directory into a single\nrecovery_<timestamp>.pasbak archive that an operator can ship offsite\n(USB / S3 / cold storage) without exposing raw dump bytes or PII.\n\nCrypto contract:\n  - Stdlib only (hashlib + hmac + secrets). No new deps.\n  - KDF:  PBKDF2-HMAC-SHA256, 200,000 iterations, 64 bytes out\n          → first 32 = encryption key, second 32 = MAC key.\n  - Encryption: HMAC-CTR keystream XORed against the plaintext.\n                (HMAC-SHA256(enc_key, nonce || counter_be_8) per 32-byte block.)\n  - Integrity: HMAC-SHA256 over (magic|version|flags|lens|salt|nonce|header).\n  - Per-archive 32-byte salt + 32-byte nonce, both via secrets.token_bytes.\n\nArchive byte layout:\n    MAGIC[8]      = b'PASBAK01'\n    VERSION[1]    = 0x01\n    FLAGS[1]      = 0x01 (encrypted)\n    SALT_LEN[2]   = 0x0020 (BE)\n    NONCE_LEN[2]  = 0x0020 (BE)\n    HEADER_LEN[4] (BE)\n    SALT[32]\n    NONCE[32]\n    HEADER_JSON[HEADER_LEN]   ← inspectable WITHOUT passphrase\n    MAC[32]                    ← HMAC over everything above\n    CIPHERTEXT[rest]           ← gzip-then-encrypt of the backup tarball\n\nOperator contract:\n  - Passphrase ONLY via env var (--passphrase-env VAR_NAME). Never on\n    the command line. Never echoed. Empty/missing rejected.\n  - Refuses to package an unverified backup unless --allow-unverified.\n  - Refuses if the verification report flagged a checksum mismatch.\n\nUsage:\n  PAS_BAK_PASS=<phrase> python scripts/package_backup.py \\\n      --input-dir backups/20260509_141500/ \\\n      --output-dir recovery/ \\\n      --passphrase-env PAS_BAK_PASS\n\n  python scripts/package_backup.py --inspect --input-dir backups/...\n  python scripts/package_backup.py --dry-run    --input-dir backups/...\n\nExit codes:\n    0  — packaged + manifest written (or dry-run / inspect succeeded)\n    2  — bad CLI arguments\n    3  — passphrase missing or empty\n    4  — backup unverified and --allow-unverified not passed\n    5  — backup verification recorded a hard failure (checksum etc.)\n    6  — input directory missing or malformed\n"
- 'utf-8'
- 'bytes'
- 'MAGIC'
- 'int'
- 'ARCHIVE_VERSION'
- 'FLAG_ENCRYPTED'
- 'KDF_ITERATIONS'
- 'KDF_DKLEN'
- 'SALT_LEN'
- 'NONCE_LEN'
- 'MAC_LEN'
- 'pas143g.package_backup.v1'
- 'str'
- 'TOOL_VERSION'
- '>HHI'
- 'passphrase'
- 'salt'
- 'return'
- 'Tuple[bytes, bytes]'
- 'PBKDF2-HMAC-SHA256 → (enc_key, mac_key). Both 32 bytes.'
- 'passphrase must be a non-empty string'
- 'salt must be exactly '
- ' bytes'
- 'sha256'
- 'enc_key'
- 'nonce'
- 'length'
- '\nGenerate `length` bytes of pseudorandom output using HMAC-SHA256\nin counter mode. Each 32-byte block is HMAC(enc_key, nonce || ctr_be_8).\n'
- 'big'
- 'plaintext'
- 'XOR `plaintext` with the HMAC-CTR keystream. Symmetric.'
- 'nonce must be exactly '
- 'mac_key'
- 'parts'
- 'HMAC-SHA256 over the concatenation of `parts`.'
- 'input_dir'
- 'Path'
- 'List[Path]'
- 'Return all files under input_dir, sorted for determinism.'
- 'Tuple[bytes, List[str]]'
- '\nCompress input_dir into a deterministic tar.gz blob.\n\nDeterminism guards:\n  - file order sorted\n  - mtime forced to 0 (pre-epoch UTC)\n  - uid/gid/uname/gname blanked\n  - gzip mtime=0\n'
- 'Optional[dict]'
- 'backup_manifest.json'
- 'verification_report.json'
- 'report'
- 'dict'
- '\nCompress a verification_report.json into a small dict suitable for\nembedding in the recovery manifest. NEVER includes raw paths or\nsecrets.\n'
- 'present'
- 'all_passed'
- 'checks_run'
- 'checks_failed'
- 'checks'
- 'bool'
- 'True iff the verification report flagged a SHA-256 mismatch.'
- 'name'
- 'sha-256'
- 'checksum'
- 'arc_names'
- 'List[str]'
- 'plaintext_sha256'
- 'archive_version'
- 'encrypted'
- 'verification'
- '\nPure manifest builder. The same inputs always produce the same\nmanifest dict — used to assert deterministic SHA256.\n'
- 'tool_version'
- 'created_at'
- 'original_backup_dir'
- 'included_files'
- 'file_count'
- 'verification_summary'
- 'manifest'
- 'Stable JSON serialization (sorted keys, no whitespace surprises).'
- 'SHA-256 over the stable serialization. Used in the inspectable header.'
- '%Y%m%d_%H%M%S'
- 'output_path'
- 'inspectable_header'
- 'ciphertext'
- 'None'
- 'Write the binary archive to output_path. MAC covers all bytes\nwritten before the MAC field.'
- 'path'
- '\nRead MAGIC + VERSION + FLAGS + lengths + salt + nonce + header\n+ MAC, WITHOUT decrypting the ciphertext. Used by the inspect\ntool — never touches the passphrase.\n\nReturns:\n  {\n    "magic":     bytes,\n    "version":   int,\n    "flags":     int,\n    "encrypted": bool,\n    "salt":      bytes,\n    "nonce":     bytes,\n    "header":    dict (parsed inspectable JSON),\n    "mac":       bytes,\n    "header_offset": int,\n    "ciphertext_offset": int,\n    "ciphertext_len": int,\n  }\n\nRaises ValueError on malformed archives.\n'
- 'archive too short to contain a header'
- 'bad magic — not a PASBAK archive'
- 'unsupported archive version '
- 'archive truncated — declared lengths overflow file'
- 'header is not valid JSON: '
- 'magic'
- 'version'
- 'flags'
- 'header'
- 'header_len'
- 'mac'
- 'header_offset'
- 'ciphertext_offset'
- 'ciphertext_len'
- 'Same as read_archive_header but also returns the raw ciphertext.'
- '\nVerify the archive MAC by re-reading the on-disk pre-MAC bytes\nEXACTLY (no re-serialisation of the parsed JSON header). Constant-\ntime compare. Never raises (returns False on any IO/parse error).\n'
- 'label'
- 'detail'
- 'PASS'
- 'FAIL'
- ' — '
- 'arg_value'
- 'Optional[str]'
- 'stamp'
- 'recovery'
- 'recovery_'
- '.pasbak'
- 'env_var'
- 'Read passphrase from env. Empty / missing returns None.'
- 'argv'
- 'Optional[list]'
- 'package_backup'
- 'PAS143G — encrypted backup packaging.'
- '--input-dir'
- 'Verified PAS143D backup directory.'
- '--output-dir'
- 'Where to write the .pasbak archive (default: ./recovery).'
- '--passphrase-env'
- 'Name of the env var holding the passphrase.'
- '--dry-run'
- 'store_true'
- 'Print what would happen without writing the archive.'
- '--inspect'
- 'Print the planned manifest + file list and exit.'
- '--allow-unverified'
- 'Permit packaging when verification_report.json is absent.'
- 'Input directory exists'
- 'Input directory non-empty'
- 'no files found'
- 'backup_manifest.json present'
- 'missing or unreadable'
- 'verification_report.json present'
- 'Re-run scripts/verify_backup.py first, or pass --allow-unverified.'
- 'Backup integrity (no checksum mismatch)'
- 'Verification recorded a SHA-256 mismatch — refuse to package.'
- 'checks_run='
- ' all_passed='
- '== INSPECT — would package the following =='
- '  files:        '
- '  plaintext:    '
- ' bytes (sha256='
- '  archive_version: '
- '  manifest_hash: '
- 'Passphrase resolution'
- 'Pass --passphrase-env VAR_NAME with a non-empty value.'
- 'env='
- ' (length not echoed)'
- 'Dry-run plan'
- '  would write archive with:'
- '    file_count:    '
- '    plaintext:     '
- '    salt:          '
- ' bytes (random)'
- '    nonce:         '
- '    manifest_hash: '
- 'Archive written'
- ' bytes), sha256='

## Disassembly

```
  --           MAKE_CELL                0 (__conditional_annotations__)

   0           RESUME                   0

   1           BUILD_SET                0
               STORE_NAME               0 (__conditional_annotations__)
               SETUP_ANNOTATIONS
               LOAD_CONST               0 ("\nPAS143G — Encrypted offsite backup packaging.\n\nTurns a verified PAS143D backup directory into a single\nrecovery_<timestamp>.pasbak archive that an operator can ship offsite\n(USB / S3 / cold storage) without exposing raw dump bytes or PII.\n\nCrypto contract:\n  - Stdlib only (hashlib + hmac + secrets). No new deps.\n  - KDF:  PBKDF2-HMAC-SHA256, 200,000 iterations, 64 bytes out\n          → first 32 = encryption key, second 32 = MAC key.\n  - Encryption: HMAC-CTR keystream XORed against the plaintext.\n                (HMAC-SHA256(enc_key, nonce || counter_be_8) per 32-byte block.)\n  - Integrity: HMAC-SHA256 over (magic|version|flags|lens|salt|nonce|header).\n  - Per-archive 32-byte salt + 32-byte nonce, both via secrets.token_bytes.\n\nArchive byte layout:\n    MAGIC[8]      = b'PASBAK01'\n    VERSION[1]    = 0x01\n    FLAGS[1]      = 0x01 (encrypted)\n    SALT_LEN[2]   = 0x0020 (BE)\n    NONCE_LEN[2]  = 0x0020 (BE)\n    HEADER_LEN[4] (BE)\n    SALT[32]\n    NONCE[32]\n    HEADER_JSON[HEADER_LEN]   ← inspectable WITHOUT passphrase\n    MAC[32]                    ← HMAC over everything above\n    CIPHERTEXT[rest]           ← gzip-then-encrypt of the backup tarball\n\nOperator contract:\n  - Passphrase ONLY via env var (--passphrase-env VAR_NAME). Never on\n    the command line. Never echoed. Empty/missing rejected.\n  - Refuses to package an unverified backup unless --allow-unverified.\n  - Refuses if the verification report flagged a checksum mismatch.\n\nUsage:\n  PAS_BAK_PASS=<phrase> python scripts/package_backup.py \\\n      --input-dir backups/20260509_141500/ \\\n      --output-dir recovery/ \\\n      --passphrase-env PAS_BAK_PASS\n\n  python scripts/package_backup.py --inspect --input-dir backups/...\n  python scripts/package_backup.py --dry-run    --input-dir backups/...\n\nExit codes:\n    0  — packaged + manifest written (or dry-run / inspect succeeded)\n    2  — bad CLI arguments\n    3  — passphrase missing or empty\n    4  — backup unverified and --allow-unverified not passed\n    5  — backup verification recorded a hard failure (checksum etc.)\n    6  — input directory missing or malformed\n")
               STORE_NAME               1 (__doc__)

  54           LOAD_SMALL_INT           0
               LOAD_CONST               1 (('annotations',))
               IMPORT_NAME              2 (__future__)
               IMPORT_FROM              3 (annotations)
               STORE_NAME               3 (annotations)
               POP_TOP

  56           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              4 (argparse)
               STORE_NAME               4 (argparse)

  57           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              5 (datetime)
               STORE_NAME               6 (_dt)

  58           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              7 (gzip)
               STORE_NAME               7 (gzip)

  59           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              8 (hashlib)
               STORE_NAME               8 (hashlib)

  60           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME              9 (hmac)
               STORE_NAME               9 (hmac)

  61           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             10 (io)
               STORE_NAME              10 (io)

  62           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             11 (json)
               STORE_NAME              11 (json)

  63           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             12 (os)
               STORE_NAME              12 (os)

  64           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             13 (secrets)
               STORE_NAME              13 (secrets)

  65           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             14 (struct)
               STORE_NAME              14 (struct)

  66           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             15 (sys)
               STORE_NAME              15 (sys)

  67           LOAD_SMALL_INT           0
               LOAD_CONST               2 (None)
               IMPORT_NAME             16 (tarfile)
               STORE_NAME              16 (tarfile)

  68           LOAD_SMALL_INT           0
               LOAD_CONST               3 (('Path',))
               IMPORT_NAME             17 (pathlib)
               IMPORT_FROM             18 (Path)
               STORE_NAME              18 (Path)
               POP_TOP

  69           LOAD_SMALL_INT           0
               LOAD_CONST               4 (('List', 'Optional', 'Tuple'))
               IMPORT_NAME             19 (typing)
               IMPORT_FROM             20 (List)
               STORE_NAME              20 (List)
               IMPORT_FROM             21 (Optional)
               STORE_NAME              21 (Optional)
               IMPORT_FROM             22 (Tuple)
               STORE_NAME              22 (Tuple)
               POP_TOP

  73           LOAD_NAME               15 (sys)
               LOAD_ATTR               46 (stdout)
               LOAD_NAME               15 (sys)
               LOAD_ATTR               48 (stderr)
               BUILD_TUPLE              2
               GET_ITER
       L1:     FOR_ITER                22 (to L4)
               STORE_NAME              25 (_stream)

  74           NOP

  75   L2:     LOAD_NAME               25 (_stream)
               LOAD_ATTR               53 (reconfigure + NULL|self)
               LOAD_CONST               5 ('utf-8')
               LOAD_CONST               6 (('encoding',))
               CALL_KW                  1
               POP_TOP
       L3:     JUMP_BACKWARD           24 (to L1)

  73   L4:     END_FOR
               POP_ITER

  84           LOAD_CONST               7 (b'PASBAK01')
               STORE_NAME              28 (MAGIC)
               LOAD_CONST               8 ('bytes')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST               9 ('MAGIC')
               STORE_SUBSCR

  85           LOAD_SMALL_INT           1
               STORE_NAME              30 (ARCHIVE_VERSION)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              11 ('ARCHIVE_VERSION')
               STORE_SUBSCR

  86           LOAD_SMALL_INT           1
               STORE_NAME              31 (FLAG_ENCRYPTED)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              12 ('FLAG_ENCRYPTED')
               STORE_SUBSCR

  88           LOAD_CONST              13 (200000)
               STORE_NAME              32 (KDF_ITERATIONS)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              14 ('KDF_ITERATIONS')
               STORE_SUBSCR

  89           LOAD_SMALL_INT          64
               STORE_NAME              33 (KDF_DKLEN)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              15 ('KDF_DKLEN')
               STORE_SUBSCR

  90           LOAD_SMALL_INT          32
               STORE_NAME              34 (SALT_LEN)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              16 ('SALT_LEN')
               STORE_SUBSCR

  91           LOAD_SMALL_INT          32
               STORE_NAME              35 (NONCE_LEN)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              17 ('NONCE_LEN')
               STORE_SUBSCR

  92           LOAD_SMALL_INT          32
               STORE_NAME              36 (MAC_LEN)
               LOAD_CONST              10 ('int')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              18 ('MAC_LEN')
               STORE_SUBSCR

  93           LOAD_CONST              19 ('pas143g.package_backup.v1')
               STORE_NAME              37 (TOOL_VERSION)
               LOAD_CONST              20 ('str')
               LOAD_NAME               29 (__annotations__)
               LOAD_CONST              21 ('TOOL_VERSION')
               STORE_SUBSCR

 100           LOAD_CONST              22 (<code object __annotate__ at 0x0000018C18026030, file "scripts\package_backup.py", line 100>)
               MAKE_FUNCTION
               LOAD_CONST              23 (<code object derive_keys at 0x0000018C17ECDD80, file "scripts\package_backup.py", line 100>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              38 (derive_keys)

 116           LOAD_CONST              24 (<code object __annotate__ at 0x0000018C18024F30, file "scripts\package_backup.py", line 116>)
               MAKE_FUNCTION
               LOAD_CONST              25 (<code object _hmac_ctr_stream at 0x0000018C17FEDC30, file "scripts\package_backup.py", line 116>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              39 (_hmac_ctr_stream)

 134           LOAD_CONST              26 (<code object __annotate__ at 0x0000018C18025F30, file "scripts\package_backup.py", line 134>)
               MAKE_FUNCTION
               LOAD_CONST              27 (<code object encrypt at 0x0000018C17FF13B0, file "scripts\package_backup.py", line 134>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              40 (encrypt)

 143           LOAD_NAME               40 (encrypt)
               STORE_NAME              41 (decrypt)

 146           LOAD_CONST              28 (<code object __annotate__ at 0x0000018C18024E30, file "scripts\package_backup.py", line 146>)
               MAKE_FUNCTION
               LOAD_CONST              29 (<code object compute_mac at 0x0000018C17FF1230, file "scripts\package_backup.py", line 146>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              42 (compute_mac)

 158           LOAD_CONST              30 (<code object __annotate__ at 0x0000018C17FA3A50, file "scripts\package_backup.py", line 158>)
               MAKE_FUNCTION
               LOAD_CONST              31 (<code object _walk_files at 0x0000018C17FF10B0, file "scripts\package_backup.py", line 158>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              43 (_walk_files)

 165           LOAD_CONST              32 (<code object __annotate__ at 0x0000018C17FA30F0, file "scripts\package_backup.py", line 165>)
               MAKE_FUNCTION
               LOAD_CONST              33 (<code object _build_tar_gz at 0x0000018C17D6DFC0, file "scripts\package_backup.py", line 165>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              44 (_build_tar_gz)

 201           LOAD_CONST              34 (<code object __annotate__ at 0x0000018C17FA3F00, file "scripts\package_backup.py", line 201>)
               MAKE_FUNCTION
               LOAD_CONST              35 (<code object read_backup_manifest at 0x0000018C17FA92F0, file "scripts\package_backup.py", line 201>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              45 (read_backup_manifest)

 211           LOAD_CONST              36 (<code object __annotate__ at 0x0000018C17FA2010, file "scripts\package_backup.py", line 211>)
               MAKE_FUNCTION
               LOAD_CONST              37 (<code object read_verification_report at 0x0000018C1800AA60, file "scripts\package_backup.py", line 211>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              46 (read_verification_report)

 221           LOAD_CONST              38 (<code object __annotate__ at 0x0000018C17FA22E0, file "scripts\package_backup.py", line 221>)
               MAKE_FUNCTION
               LOAD_CONST              39 (<code object verification_summary at 0x0000018C1794ED80, file "scripts\package_backup.py", line 221>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              47 (verification_summary)

 239           LOAD_CONST              40 (<code object __annotate__ at 0x0000018C17FA24C0, file "scripts\package_backup.py", line 239>)
               MAKE_FUNCTION
               LOAD_CONST              41 (<code object has_checksum_mismatch at 0x0000018C179A7290, file "scripts\package_backup.py", line 239>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              48 (has_checksum_mismatch)

 255           LOAD_CONST              42 (<code object __annotate__ at 0x0000018C180F4580, file "scripts\package_backup.py", line 255>)
               MAKE_FUNCTION
               LOAD_CONST              43 (<code object build_recovery_manifest at 0x0000018C1801C410, file "scripts\package_backup.py", line 255>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              49 (build_recovery_manifest)

 281           LOAD_CONST              44 (<code object __annotate__ at 0x0000018C17FA25B0, file "scripts\package_backup.py", line 281>)
               MAKE_FUNCTION
               LOAD_CONST              45 (<code object serialize_manifest at 0x0000018C1802CAE0, file "scripts\package_backup.py", line 281>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              50 (serialize_manifest)

 291           LOAD_CONST              46 (<code object __annotate__ at 0x0000018C17FA23D0, file "scripts\package_backup.py", line 291>)
               MAKE_FUNCTION
               LOAD_CONST              47 (<code object manifest_hash at 0x0000018C1802C620, file "scripts\package_backup.py", line 291>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              51 (manifest_hash)

 296           LOAD_CONST              48 (<code object __annotate__ at 0x0000018C17FA2D30, file "scripts\package_backup.py", line 296>)
               MAKE_FUNCTION
               LOAD_CONST              49 (<code object now_stamp at 0x0000018C180110B0, file "scripts\package_backup.py", line 296>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              52 (now_stamp)

 306           LOAD_CONST              50 ('>HHI')
               STORE_NAME              53 (_LENGTHS_STRUCT)

 309           LOAD_CONST              51 (<code object __annotate__ at 0x0000018C180F4360, file "scripts\package_backup.py", line 309>)
               MAKE_FUNCTION
               LOAD_CONST              52 (<code object write_archive at 0x0000018C17ED1700, file "scripts\package_backup.py", line 309>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              54 (write_archive)

 346           LOAD_CONST              53 (<code object __annotate__ at 0x0000018C17FA2A60, file "scripts\package_backup.py", line 346>)
               MAKE_FUNCTION
               LOAD_CONST              54 (<code object read_archive_header at 0x0000018C177C5D50, file "scripts\package_backup.py", line 346>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              55 (read_archive_header)

 421           LOAD_CONST              55 (<code object __annotate__ at 0x0000018C17FA2C40, file "scripts\package_backup.py", line 421>)
               MAKE_FUNCTION
               LOAD_CONST              56 (<code object read_archive_full at 0x0000018C18060DB0, file "scripts\package_backup.py", line 421>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              56 (read_archive_full)

 430           LOAD_CONST              57 (<code object __annotate__ at 0x0000018C18024930, file "scripts\package_backup.py", line 430>)
               MAKE_FUNCTION
               LOAD_CONST              58 (<code object verify_archive_mac_from_disk at 0x0000018C17D76C00, file "scripts\package_backup.py", line 430>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              57 (verify_archive_mac_from_disk)

 454           LOAD_CONST              68 (('',))
               LOAD_CONST              59 (<code object __annotate__ at 0x0000018C18026130, file "scripts\package_backup.py", line 454>)
               MAKE_FUNCTION
               LOAD_CONST              60 (<code object _status at 0x0000018C18038670, file "scripts\package_backup.py", line 454>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              58 (_status)

 466           LOAD_CONST              61 (<code object __annotate__ at 0x0000018C18026530, file "scripts\package_backup.py", line 466>)
               MAKE_FUNCTION
               LOAD_CONST              62 (<code object _resolve_output_path at 0x0000018C17F962B0, file "scripts\package_backup.py", line 466>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              59 (_resolve_output_path)

 472           LOAD_CONST              63 (<code object __annotate__ at 0x0000018C17FA3690, file "scripts\package_backup.py", line 472>)
               MAKE_FUNCTION
               LOAD_CONST              64 (<code object _read_passphrase at 0x0000018C18039070, file "scripts\package_backup.py", line 472>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               STORE_NAME              60 (_read_passphrase)

 482           LOAD_CONST              69 ((None,))
               LOAD_CONST              65 (<code object __annotate__ at 0x0000018C17FA3870, file "scripts\package_backup.py", line 482>)
               MAKE_FUNCTION
               LOAD_CONST              66 (<code object main at 0x0000018C17E8AEE0, file "scripts\package_backup.py", line 482>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE  16 (annotate)
               SET_FUNCTION_ATTRIBUTE   1 (defaults)
               STORE_NAME              61 (main)

 608           LOAD_NAME               62 (__name__)
               LOAD_CONST              67 ('__main__')
               COMPARE_OP              88 (bool(==))
               POP_JUMP_IF_FALSE       14 (to L5)
               NOT_TAKEN

 609           LOAD_NAME               63 (SystemExit)
               PUSH_NULL
               LOAD_NAME               61 (main)
               PUSH_NULL
               CALL                     0
               CALL                     1
               RAISE_VARARGS            1

 608   L5:     LOAD_CONST               2 (None)
               RETURN_VALUE

  --   L6:     PUSH_EXC_INFO

  76           LOAD_NAME               27 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        6 (to L8)
               NOT_TAKEN
               POP_TOP

  77   L7:     POP_EXCEPT
               EXTENDED_ARG             1
               JUMP_BACKWARD          262 (to L1)

  76   L8:     RERAISE                  0

  --   L9:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L6 [1]
  L6 to L7 -> L9 [2] lasti
  L8 to L9 -> L9 [2] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026030, file "scripts\package_backup.py", line 100>:
100           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('passphrase')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('salt')
              LOAD_CONST               4 ('bytes')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Tuple[bytes, bytes]')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object derive_keys at 0x0000018C17ECDD80, file "scripts\package_backup.py", line 100>:
100           RESUME                   0

102           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (passphrase)
              LOAD_GLOBAL              2 (str)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE        9 (to L1)
              NOT_TAKEN
              LOAD_FAST_BORROW         0 (passphrase)
              TO_BOOL
              POP_JUMP_IF_TRUE        12 (to L2)
              NOT_TAKEN

103   L1:     LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               1 ('passphrase must be a non-empty string')
              CALL                     1
              RAISE_VARARGS            1

104   L2:     LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         1 (salt)
              LOAD_GLOBAL              6 (bytes)
              LOAD_GLOBAL              8 (bytearray)
              BUILD_TUPLE              2
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_FALSE       21 (to L3)
              NOT_TAKEN
              LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         1 (salt)
              CALL                     1
              LOAD_GLOBAL             12 (SALT_LEN)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE       20 (to L4)
              NOT_TAKEN

105   L3:     LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               2 ('salt must be exactly ')
              LOAD_GLOBAL             12 (SALT_LEN)
              FORMAT_SIMPLE
              LOAD_CONST               3 (' bytes')
              BUILD_STRING             3
              CALL                     1
              RAISE_VARARGS            1

106   L4:     LOAD_GLOBAL             14 (hashlib)
              LOAD_ATTR               16 (pbkdf2_hmac)
              PUSH_NULL

107           LOAD_CONST               4 ('sha256')

108           LOAD_FAST_BORROW         0 (passphrase)
              LOAD_ATTR               19 (encode + NULL|self)
              LOAD_CONST               5 ('utf-8')
              CALL                     1

109           LOAD_GLOBAL              7 (bytes + NULL)
              LOAD_FAST_BORROW         1 (salt)
              CALL                     1

110           LOAD_GLOBAL             20 (KDF_ITERATIONS)

111           LOAD_GLOBAL             22 (KDF_DKLEN)

106           LOAD_CONST               6 (('dklen',))
              CALL_KW                  5
              STORE_FAST               2 (full)

113           LOAD_FAST_BORROW         2 (full)
              LOAD_CONST               7 (slice(None, 32, None))
              BINARY_OP               26 ([])
              LOAD_FAST_BORROW         2 (full)
              LOAD_CONST               8 (slice(32, 64, None))
              BINARY_OP               26 ([])
              BUILD_TUPLE              2
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18024F30, file "scripts\package_backup.py", line 116>:
116           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('enc_key')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               3 ('nonce')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               4 ('length')
              LOAD_CONST               5 ('int')
              LOAD_CONST               6 ('return')
              LOAD_CONST               2 ('bytes')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _hmac_ctr_stream at 0x0000018C17FEDC30, file "scripts\package_backup.py", line 116>:
116           RESUME                   0

121           LOAD_GLOBAL              1 (bytearray + NULL)
              CALL                     0
              STORE_FAST               3 (out)

122           LOAD_SMALL_INT           0
              STORE_FAST               4 (counter)

123   L1:     LOAD_GLOBAL              3 (len + NULL)
              LOAD_FAST_BORROW         3 (out)
              CALL                     1
              LOAD_FAST_BORROW         2 (length)
              COMPARE_OP              18 (bool(<))
              POP_JUMP_IF_FALSE      103 (to L2)
              NOT_TAKEN

124           LOAD_GLOBAL              4 (hmac)
              LOAD_ATTR                6 (new)
              PUSH_NULL

125           LOAD_FAST_BORROW         0 (enc_key)

126           LOAD_FAST_BORROW_LOAD_FAST_BORROW 20 (nonce, counter)
              LOAD_ATTR                9 (to_bytes + NULL|self)
              LOAD_SMALL_INT           8
              LOAD_CONST               1 ('big')
              CALL                     2
              BINARY_OP                0 (+)

127           LOAD_GLOBAL             10 (hashlib)
              LOAD_ATTR               12 (sha256)

124           CALL                     3

128           LOAD_ATTR               15 (digest + NULL|self)
              CALL                     0

124           STORE_FAST               5 (chunk)

129           LOAD_FAST_BORROW         3 (out)
              LOAD_ATTR               17 (extend + NULL|self)
              LOAD_FAST_BORROW         5 (chunk)
              CALL                     1
              POP_TOP

130           LOAD_FAST_BORROW         4 (counter)
              LOAD_SMALL_INT           1
              BINARY_OP               13 (+=)
              STORE_FAST               4 (counter)
              JUMP_BACKWARD          118 (to L1)

131   L2:     LOAD_GLOBAL             19 (bytes + NULL)
              LOAD_FAST_BORROW         3 (out)
              LOAD_CONST               2 (None)
              LOAD_FAST_BORROW         2 (length)
              BINARY_SLICE
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18025F30, file "scripts\package_backup.py", line 134>:
134           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('plaintext')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               3 ('enc_key')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               4 ('nonce')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               5 ('return')
              LOAD_CONST               2 ('bytes')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object encrypt at 0x0000018C17FF13B0, file "scripts\package_backup.py", line 134>:
134           RESUME                   0

136           LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         2 (nonce)
              CALL                     1
              LOAD_GLOBAL              2 (NONCE_LEN)
              COMPARE_OP             119 (bool(!=))
              POP_JUMP_IF_FALSE       20 (to L1)
              NOT_TAKEN

137           LOAD_GLOBAL              5 (ValueError + NULL)
              LOAD_CONST               1 ('nonce must be exactly ')
              LOAD_GLOBAL              2 (NONCE_LEN)
              FORMAT_SIMPLE
              LOAD_CONST               2 (' bytes')
              BUILD_STRING             3
              CALL                     1
              RAISE_VARARGS            1

138   L1:     LOAD_GLOBAL              7 (_hmac_ctr_stream + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (enc_key, nonce)
              LOAD_GLOBAL              1 (len + NULL)
              LOAD_FAST_BORROW         0 (plaintext)
              CALL                     1
              CALL                     3
              STORE_FAST               3 (stream)

139           LOAD_GLOBAL              9 (bytes + NULL)
              LOAD_CONST               3 (<code object <genexpr> at 0x0000018C180F4470, file "scripts\package_backup.py", line 139>)
              MAKE_FUNCTION
              LOAD_GLOBAL             11 (zip + NULL)
              LOAD_FAST_BORROW_LOAD_FAST_BORROW 3 (plaintext, stream)
              CALL                     2
              GET_ITER
              CALL                     0
              CALL                     1
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C180F4470, file "scripts\package_backup.py", line 139>:
 139           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                15 (to L3)
               UNPACK_SEQUENCE          2
               STORE_FAST_STORE_FAST   18 (p, s)
               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (p, s)
               BINARY_OP               12 (^)
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           17 (to L2)
       L3:     END_FOR
               POP_ITER
               LOAD_CONST               0 (None)
               RETURN_VALUE

  --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L4 -> L4 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024E30, file "scripts\package_backup.py", line 146>:
146           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('mac_key')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               3 ('parts')
              LOAD_CONST               2 ('bytes')
              LOAD_CONST               4 ('return')
              LOAD_CONST               2 ('bytes')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object compute_mac at 0x0000018C17FF1230, file "scripts\package_backup.py", line 146>:
146           RESUME                   0

148           LOAD_GLOBAL              0 (hmac)
              LOAD_ATTR                2 (new)
              PUSH_NULL
              LOAD_FAST_BORROW         0 (mac_key)
              LOAD_CONST               1 (b'')
              LOAD_GLOBAL              4 (hashlib)
              LOAD_ATTR                6 (sha256)
              CALL                     3
              STORE_FAST               2 (h)

149           LOAD_FAST_BORROW         1 (parts)
              GET_ITER
      L1:     FOR_ITER                20 (to L2)
              STORE_FAST               3 (p)

150           LOAD_FAST_BORROW         2 (h)
              LOAD_ATTR                9 (update + NULL|self)
              LOAD_FAST_BORROW         3 (p)
              CALL                     1
              POP_TOP
              JUMP_BACKWARD           22 (to L1)

149   L2:     END_FOR
              POP_ITER

151           LOAD_FAST_BORROW         2 (h)
              LOAD_ATTR               11 (digest + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3A50, file "scripts\package_backup.py", line 158>:
158           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('input_dir')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('List[Path]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _walk_files at 0x0000018C17FF10B0, file "scripts\package_backup.py", line 158>:
  --           MAKE_CELL                0 (input_dir)

 158           RESUME                   0

 160           LOAD_DEREF               0 (input_dir)
               LOAD_ATTR                1 (rglob + NULL|self)
               LOAD_CONST               1 ('*')
               CALL                     1
               GET_ITER
               LOAD_FAST_AND_CLEAR      1 (p)
               SWAP                     2
       L1:     BUILD_LIST               0
               SWAP                     2
       L2:     FOR_ITER                28 (to L5)
               STORE_FAST_LOAD_FAST    17 (p, p)
               LOAD_ATTR                3 (is_file + NULL|self)
               CALL                     0
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           26 (to L2)
       L4:     LOAD_FAST_BORROW         1 (p)
               LIST_APPEND              2
               JUMP_BACKWARD           30 (to L2)
       L5:     END_FOR
               POP_ITER
       L6:     STORE_FAST               2 (files)
               STORE_FAST               1 (p)

 161           LOAD_FAST_BORROW         2 (files)
               LOAD_ATTR                5 (sort + NULL|self)
               LOAD_FAST_BORROW         0 (input_dir)
               BUILD_TUPLE              1
               LOAD_CONST               2 (<code object <lambda> at 0x0000018C1802C880, file "scripts\package_backup.py", line 161>)
               MAKE_FUNCTION
               SET_FUNCTION_ATTRIBUTE   8 (closure)
               LOAD_CONST               3 (('key',))
               CALL_KW                  1
               POP_TOP

 162           LOAD_FAST_BORROW         2 (files)
               RETURN_VALUE

  --   L7:     SWAP                     2
               POP_TOP

 160           SWAP                     2
               STORE_FAST               1 (p)
               RERAISE                  0
ExceptionTable:
  L1 to L3 -> L7 [2]
  L4 to L6 -> L7 [2]

Disassembly of <code object <lambda> at 0x0000018C1802C880, file "scripts\package_backup.py", line 161>:
  --           COPY_FREE_VARS           1

 161           RESUME                   0
               LOAD_GLOBAL              1 (str + NULL)
               LOAD_FAST_BORROW         0 (p)
               LOAD_ATTR                3 (relative_to + NULL|self)
               LOAD_DEREF               1 (input_dir)
               CALL                     1
               CALL                     1
               LOAD_ATTR                5 (replace + NULL|self)
               LOAD_CONST               0 ('\\')
               LOAD_CONST               1 ('/')
               CALL                     2
               RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA30F0, file "scripts\package_backup.py", line 165>:
165           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('input_dir')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Tuple[bytes, List[str]]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object _build_tar_gz at 0x0000018C17D6DFC0, file "scripts\package_backup.py", line 165>:
 165            RESUME                   0

 175            LOAD_GLOBAL              1 (_walk_files + NULL)
                LOAD_FAST_BORROW         0 (input_dir)
                CALL                     1
                STORE_FAST               1 (files)

 176            BUILD_LIST               0
                STORE_FAST               2 (arc_names)

 178            LOAD_GLOBAL              2 (io)
                LOAD_ATTR                4 (BytesIO)
                PUSH_NULL
                CALL                     0
                STORE_FAST               3 (bio)

 181            LOAD_GLOBAL              6 (gzip)
                LOAD_ATTR                8 (GzipFile)
                PUSH_NULL
                LOAD_FAST_BORROW         3 (bio)
                LOAD_CONST               1 ('wb')
                LOAD_SMALL_INT           0
                LOAD_CONST               2 (('fileobj', 'mode', 'mtime'))
                CALL_KW                  3
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L1:     STORE_FAST               4 (gz)

 182            LOAD_GLOBAL             10 (tarfile)
                LOAD_ATTR               12 (open)
                PUSH_NULL
                LOAD_FAST_BORROW         4 (gz)
                LOAD_CONST               3 ('w')
                LOAD_CONST               4 (('fileobj', 'mode'))
                CALL_KW                  2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_FAST               5 (tar)

 183            LOAD_FAST_BORROW         1 (files)
                GET_ITER
        L3:     FOR_ITER               171 (to L6)
                STORE_FAST               6 (f)

 184            LOAD_GLOBAL             15 (str + NULL)
                LOAD_FAST_BORROW         6 (f)
                LOAD_ATTR               17 (relative_to + NULL|self)
                LOAD_FAST_BORROW         0 (input_dir)
                CALL                     1
                CALL                     1
                LOAD_ATTR               19 (replace + NULL|self)
                LOAD_CONST               5 ('\\')
                LOAD_CONST               6 ('/')
                CALL                     2
                STORE_FAST               7 (arc_name)

 185            LOAD_FAST_BORROW         2 (arc_names)
                LOAD_ATTR               21 (append + NULL|self)
                LOAD_FAST_BORROW         7 (arc_name)
                CALL                     1
                POP_TOP

 186            LOAD_FAST_BORROW         5 (tar)
                LOAD_ATTR               23 (gettarinfo + NULL|self)
                LOAD_GLOBAL             15 (str + NULL)
                LOAD_FAST_BORROW         6 (f)
                CALL                     1
                LOAD_FAST_BORROW         7 (arc_name)
                LOAD_CONST               7 (('arcname',))
                CALL_KW                  2
                STORE_FAST               8 (info)

 187            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (info)
                STORE_ATTR              12 (mtime)

 188            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (info)
                STORE_ATTR              13 (uid)

 189            LOAD_SMALL_INT           0
                LOAD_FAST_BORROW         8 (info)
                STORE_ATTR              14 (gid)

 190            LOAD_CONST               8 ('')
                LOAD_FAST_BORROW         8 (info)
                STORE_ATTR              15 (uname)

 191            LOAD_CONST               8 ('')
                LOAD_FAST_BORROW         8 (info)
                STORE_ATTR              16 (gname)

 192            LOAD_GLOBAL             13 (open + NULL)
                LOAD_FAST_BORROW         6 (f)
                LOAD_CONST               9 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L4:     STORE_FAST               9 (fh)

 193            LOAD_FAST_BORROW         5 (tar)
                LOAD_ATTR               35 (addfile + NULL|self)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (info, fh)
                CALL                     2
                POP_TOP

 192    L5:     LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                CALL                     3
                POP_TOP
                JUMP_BACKWARD          173 (to L3)

 183    L6:     END_FOR
                POP_ITER

 182    L7:     LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                CALL                     3
                POP_TOP

 181    L8:     LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                LOAD_CONST              10 (None)
                CALL                     3
                POP_TOP

 194    L9:     LOAD_FAST_BORROW         3 (bio)
                LOAD_ATTR               37 (getvalue + NULL|self)
                CALL                     0
                LOAD_FAST_BORROW         2 (arc_names)
                BUILD_TUPLE              2
                RETURN_VALUE

 192   L10:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L11)
                NOT_TAKEN
                RERAISE                  2
       L11:     POP_TOP
       L12:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD          226 (to L3)

  --   L13:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 182   L14:     PUSH_EXC_INFO
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
                JUMP_BACKWARD_NO_INTERRUPT 62 (to L8)

  --   L17:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 181   L18:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L19)
                NOT_TAKEN
                RERAISE                  2
       L19:     POP_TOP
       L20:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                JUMP_BACKWARD_NO_INTERRUPT 73 (to L9)

  --   L21:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L18 [2] lasti
  L2 to L4 -> L14 [4] lasti
  L4 to L5 -> L10 [7] lasti
  L5 to L7 -> L14 [4] lasti
  L7 to L8 -> L18 [2] lasti
  L10 to L12 -> L13 [9] lasti
  L12 to L14 -> L14 [4] lasti
  L14 to L16 -> L17 [6] lasti
  L16 to L18 -> L18 [2] lasti
  L18 to L20 -> L21 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA3F00, file "scripts\package_backup.py", line 201>:
201           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('input_dir')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object read_backup_manifest at 0x0000018C17FA92F0, file "scripts\package_backup.py", line 201>:
 201           RESUME                   0

 202           LOAD_FAST_BORROW         0 (input_dir)
               LOAD_CONST               0 ('backup_manifest.json')
               BINARY_OP               11 (/)
               STORE_FAST               1 (p)

 203           LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                1 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 204           LOAD_CONST               1 (None)
               RETURN_VALUE

 205   L1:     NOP

 206   L2:     LOAD_GLOBAL              2 (json)
               LOAD_ATTR                4 (loads)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                7 (read_text + NULL|self)
               LOAD_CONST               2 ('utf-8')
               LOAD_CONST               3 (('encoding',))
               CALL_KW                  1
               CALL                     1
       L3:     RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 207           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 208   L5:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

 207   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2010, file "scripts\package_backup.py", line 211>:
211           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('input_dir')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('Optional[dict]')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object read_verification_report at 0x0000018C1800AA60, file "scripts\package_backup.py", line 211>:
 211           RESUME                   0

 212           LOAD_FAST_BORROW         0 (input_dir)
               LOAD_CONST               0 ('verification_report.json')
               BINARY_OP               11 (/)
               STORE_FAST               1 (p)

 213           LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                1 (exists + NULL|self)
               CALL                     0
               TO_BOOL
               POP_JUMP_IF_TRUE         3 (to L1)
               NOT_TAKEN

 214           LOAD_CONST               1 (None)
               RETURN_VALUE

 215   L1:     NOP

 216   L2:     LOAD_GLOBAL              2 (json)
               LOAD_ATTR                4 (loads)
               PUSH_NULL
               LOAD_FAST_BORROW         1 (p)
               LOAD_ATTR                7 (read_text + NULL|self)
               LOAD_CONST               2 ('utf-8')
               LOAD_CONST               3 (('encoding',))
               CALL_KW                  1
               CALL                     1
       L3:     RETURN_VALUE

  --   L4:     PUSH_EXC_INFO

 217           LOAD_GLOBAL              8 (Exception)
               CHECK_EXC_MATCH
               POP_JUMP_IF_FALSE        5 (to L6)
               NOT_TAKEN
               POP_TOP

 218   L5:     POP_EXCEPT
               LOAD_CONST               1 (None)
               RETURN_VALUE

 217   L6:     RERAISE                  0

  --   L7:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L2 to L3 -> L4 [0]
  L4 to L5 -> L7 [1] lasti
  L6 to L7 -> L7 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA22E0, file "scripts\package_backup.py", line 221>:
221           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object verification_summary at 0x0000018C1794ED80, file "scripts\package_backup.py", line 221>:
221           RESUME                   0

227           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE        11 (to L1)
              NOT_TAKEN

228           LOAD_CONST               1 ('present')
              LOAD_CONST               2 (False)
              LOAD_CONST               3 ('all_passed')
              LOAD_CONST               4 (None)
              LOAD_CONST               5 ('checks_run')
              LOAD_SMALL_INT           0
              LOAD_CONST               6 ('checks_failed')
              LOAD_SMALL_INT           0
              BUILD_MAP                4
              RETURN_VALUE

229   L1:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('checks')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     STORE_FAST               1 (checks)

230           LOAD_GLOBAL              7 (sum + NULL)
              LOAD_CONST               8 (<code object <genexpr> at 0x0000018C17972550, file "scripts\package_backup.py", line 230>)
              MAKE_FUNCTION
              LOAD_FAST_BORROW         1 (checks)
              GET_ITER
              CALL                     0
              CALL                     1
              STORE_FAST               2 (failed)

232           LOAD_CONST               1 ('present')
              LOAD_CONST               9 (True)

233           LOAD_CONST               3 ('all_passed')
              LOAD_GLOBAL              9 (bool + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('all_passed')
              CALL                     1
              CALL                     1

234           LOAD_CONST               5 ('checks_run')
              LOAD_GLOBAL             11 (len + NULL)
              LOAD_FAST_BORROW         1 (checks)
              CALL                     1

235           LOAD_CONST               6 ('checks_failed')
              LOAD_FAST_BORROW         2 (failed)

231           BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object <genexpr> at 0x0000018C17972550, file "scripts\package_backup.py", line 230>:
 230           RETURN_GENERATOR
               POP_TOP
       L1:     RESUME                   0
               LOAD_FAST                0 (.0)
       L2:     FOR_ITER                56 (to L7)
               STORE_FAST               1 (c)
               LOAD_GLOBAL              1 (isinstance + NULL)
               LOAD_FAST_BORROW         1 (c)
               LOAD_GLOBAL              2 (dict)
               CALL                     2
               TO_BOOL
       L3:     POP_JUMP_IF_TRUE         3 (to L4)
               NOT_TAKEN
               JUMP_BACKWARD           27 (to L2)
       L4:     LOAD_FAST_BORROW         1 (c)
               LOAD_ATTR                5 (get + NULL|self)
               LOAD_CONST               0 ('ok')
               CALL                     1
               TO_BOOL
       L5:     POP_JUMP_IF_FALSE        3 (to L6)
               NOT_TAKEN
               JUMP_BACKWARD           52 (to L2)
       L6:     LOAD_SMALL_INT           1
               YIELD_VALUE              0
               RESUME                   5
               POP_TOP
               JUMP_BACKWARD           58 (to L2)
       L7:     END_FOR
               POP_ITER
               LOAD_CONST               1 (None)
               RETURN_VALUE

  --   L8:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
               RERAISE                  1
ExceptionTable:
  L1 to L3 -> L8 [0] lasti
  L4 to L5 -> L8 [0] lasti
  L6 to L8 -> L8 [0] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA24C0, file "scripts\package_backup.py", line 239>:
239           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('report')
              LOAD_CONST               2 ('Optional[dict]')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bool')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object has_checksum_mismatch at 0x0000018C179A7290, file "scripts\package_backup.py", line 239>:
239           RESUME                   0

241           LOAD_GLOBAL              1 (isinstance + NULL)
              LOAD_FAST_BORROW         0 (report)
              LOAD_GLOBAL              2 (dict)
              CALL                     2
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

242           LOAD_CONST               1 (False)
              RETURN_VALUE

243   L1:     LOAD_FAST_BORROW         0 (report)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               2 ('checks')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN
              POP_TOP
              BUILD_LIST               0
      L2:     GET_ITER
      L3:     FOR_ITER                86 (to L7)
              STORE_FAST               1 (c)

244           LOAD_FAST_BORROW         1 (c)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               3 ('name')
              CALL                     1
              COPY                     1
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L4)
              NOT_TAKEN
              POP_TOP
              LOAD_CONST               4 ('')
      L4:     LOAD_ATTR                7 (lower + NULL|self)
              CALL                     0
              STORE_FAST               2 (name)

245           LOAD_CONST               5 ('sha-256')
              LOAD_FAST_BORROW         2 (name)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE        10 (to L5)
              NOT_TAKEN
              LOAD_CONST               6 ('checksum')
              LOAD_FAST_BORROW         2 (name)
              CONTAINS_OP              0 (in)
              POP_JUMP_IF_TRUE         3 (to L5)
              NOT_TAKEN
              JUMP_BACKWARD           60 (to L3)

246   L5:     LOAD_FAST_BORROW         1 (c)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_CONST               7 ('ok')
              CALL                     1
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L6)
              NOT_TAKEN
              JUMP_BACKWARD           85 (to L3)

247   L6:     POP_TOP
              LOAD_CONST               8 (True)
              RETURN_VALUE

243   L7:     END_FOR
              POP_ITER

248           LOAD_CONST               1 (False)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180F4580, file "scripts\package_backup.py", line 255>:
255           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('input_dir')

257           LOAD_CONST               2 ('Path')

255           LOAD_CONST               3 ('arc_names')

258           LOAD_CONST               4 ('List[str]')

255           LOAD_CONST               5 ('plaintext_sha256')

259           LOAD_CONST               6 ('str')

255           LOAD_CONST               7 ('archive_version')

260           LOAD_CONST               8 ('int')

255           LOAD_CONST               9 ('encrypted')

261           LOAD_CONST              10 ('bool')

255           LOAD_CONST              11 ('verification')

262           LOAD_CONST              12 ('dict')

255           LOAD_CONST              13 ('return')

263           LOAD_CONST              12 ('dict')

255           BUILD_MAP                7
              RETURN_VALUE

Disassembly of <code object build_recovery_manifest at 0x0000018C1801C410, file "scripts\package_backup.py", line 255>:
255           RESUME                   0

269           LOAD_CONST               1 ('archive_version')
              LOAD_FAST_BORROW         3 (archive_version)

270           LOAD_CONST               2 ('tool_version')
              LOAD_GLOBAL              0 (TOOL_VERSION)

271           LOAD_CONST               3 ('encrypted')
              LOAD_GLOBAL              3 (bool + NULL)
              LOAD_FAST_BORROW         4 (encrypted)
              CALL                     1

272           LOAD_CONST               4 ('created_at')
              LOAD_GLOBAL              4 (_dt)
              LOAD_ATTR                6 (datetime)
              LOAD_ATTR                9 (now + NULL|self)
              LOAD_GLOBAL              4 (_dt)
              LOAD_ATTR               10 (timezone)
              LOAD_ATTR               12 (utc)
              CALL                     1
              LOAD_ATTR               15 (isoformat + NULL|self)
              CALL                     0

273           LOAD_CONST               5 ('original_backup_dir')
              LOAD_GLOBAL             17 (str + NULL)
              LOAD_FAST_BORROW         0 (input_dir)
              CALL                     1
              LOAD_ATTR               19 (replace + NULL|self)
              LOAD_CONST               6 ('\\')
              LOAD_CONST               7 ('/')
              CALL                     2

274           LOAD_CONST               8 ('included_files')
              LOAD_GLOBAL             21 (list + NULL)
              LOAD_FAST_BORROW         1 (arc_names)
              CALL                     1

275           LOAD_CONST               9 ('file_count')
              LOAD_GLOBAL             23 (len + NULL)
              LOAD_FAST_BORROW         1 (arc_names)
              CALL                     1

276           LOAD_CONST              10 ('sha256')
              LOAD_FAST_BORROW         2 (plaintext_sha256)

277           LOAD_CONST              11 ('verification_summary')
              LOAD_FAST_BORROW         5 (verification)

268           BUILD_MAP                9
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA25B0, file "scripts\package_backup.py", line 281>:
281           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('bytes')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object serialize_manifest at 0x0000018C1802CAE0, file "scripts\package_backup.py", line 281>:
281           RESUME                   0

283           LOAD_GLOBAL              0 (json)
              LOAD_ATTR                2 (dumps)
              PUSH_NULL

284           LOAD_FAST_BORROW         0 (manifest)

285           LOAD_CONST               1 (True)

286           LOAD_CONST               5 ((',', ':'))

287           LOAD_CONST               2 (False)

283           LOAD_CONST               3 (('sort_keys', 'separators', 'ensure_ascii'))
              CALL_KW                  4

288           LOAD_ATTR                5 (encode + NULL|self)
              LOAD_CONST               4 ('utf-8')
              CALL                     1

283           RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA23D0, file "scripts\package_backup.py", line 291>:
291           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('manifest')
              LOAD_CONST               2 ('dict')
              LOAD_CONST               3 ('return')
              LOAD_CONST               4 ('str')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object manifest_hash at 0x0000018C1802C620, file "scripts\package_backup.py", line 291>:
291           RESUME                   0

293           LOAD_GLOBAL              0 (hashlib)
              LOAD_ATTR                2 (sha256)
              PUSH_NULL
              LOAD_GLOBAL              5 (serialize_manifest + NULL)
              LOAD_FAST_BORROW         0 (manifest)
              CALL                     1
              CALL                     1
              LOAD_ATTR                7 (hexdigest + NULL|self)
              CALL                     0
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA2D30, file "scripts\package_backup.py", line 296>:
296           RESUME                   0
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

Disassembly of <code object now_stamp at 0x0000018C180110B0, file "scripts\package_backup.py", line 296>:
296           RESUME                   0

297           LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                2 (datetime)
              LOAD_ATTR                5 (now + NULL|self)
              LOAD_GLOBAL              0 (_dt)
              LOAD_ATTR                6 (timezone)
              LOAD_ATTR                8 (utc)
              CALL                     1
              LOAD_ATTR               11 (strftime + NULL|self)
              LOAD_CONST               0 ('%Y%m%d_%H%M%S')
              CALL                     1
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C180F4360, file "scripts\package_backup.py", line 309>:
309           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('output_path')

311           LOAD_CONST               2 ('Path')

309           LOAD_CONST               3 ('salt')

312           LOAD_CONST               4 ('bytes')

309           LOAD_CONST               5 ('nonce')

313           LOAD_CONST               4 ('bytes')

309           LOAD_CONST               6 ('inspectable_header')

314           LOAD_CONST               4 ('bytes')

309           LOAD_CONST               7 ('ciphertext')

315           LOAD_CONST               4 ('bytes')

309           LOAD_CONST               8 ('mac_key')

316           LOAD_CONST               4 ('bytes')

309           LOAD_CONST               9 ('encrypted')

317           LOAD_CONST              10 ('bool')

309           LOAD_CONST              11 ('return')

318           LOAD_CONST              12 ('None')

309           BUILD_MAP                8
              RETURN_VALUE

Disassembly of <code object write_archive at 0x0000018C17ED1700, file "scripts\package_backup.py", line 309>:
 309            RESUME                   0

 321            LOAD_FAST_BORROW         6 (encrypted)
                TO_BOOL
                POP_JUMP_IF_FALSE        7 (to L1)
                NOT_TAKEN
                LOAD_GLOBAL              0 (FLAG_ENCRYPTED)
                JUMP_FORWARD             1 (to L2)
        L1:     LOAD_SMALL_INT           0
        L2:     STORE_FAST               7 (flags)

 322            LOAD_FAST_BORROW         6 (encrypted)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L3)
                NOT_TAKEN
                LOAD_FAST                1 (salt)
                JUMP_FORWARD             1 (to L4)
        L3:     LOAD_CONST               1 (b'')
        L4:     STORE_FAST               8 (salt_bytes)

 323            LOAD_FAST_BORROW         6 (encrypted)
                TO_BOOL
                POP_JUMP_IF_FALSE        3 (to L5)
                NOT_TAKEN
                LOAD_FAST                2 (nonce)
                JUMP_FORWARD             1 (to L6)
        L5:     LOAD_CONST               1 (b'')
        L6:     STORE_FAST               9 (nonce_bytes)

 325            LOAD_GLOBAL              2 (struct)
                LOAD_ATTR                4 (pack)
                PUSH_NULL

 326            LOAD_GLOBAL              6 (_LENGTHS_STRUCT)

 327            LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         8 (salt_bytes)
                CALL                     1
                LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         9 (nonce_bytes)
                CALL                     1
                LOAD_GLOBAL              9 (len + NULL)
                LOAD_FAST_BORROW         3 (inspectable_header)
                CALL                     1

 325            CALL                     4
                STORE_FAST              10 (header_lengths)

 331            LOAD_GLOBAL             10 (MAGIC)

 332            LOAD_GLOBAL             13 (bytes + NULL)
                LOAD_GLOBAL             14 (ARCHIVE_VERSION)
                LOAD_FAST_BORROW         7 (flags)
                BUILD_LIST               2
                CALL                     1

 331            BINARY_OP                0 (+)

 333            LOAD_FAST_BORROW        10 (header_lengths)

 331            BINARY_OP                0 (+)

 334            LOAD_FAST_BORROW         8 (salt_bytes)

 331            BINARY_OP                0 (+)

 335            LOAD_FAST_BORROW         9 (nonce_bytes)

 331            BINARY_OP                0 (+)

 336            LOAD_FAST_BORROW         3 (inspectable_header)

 331            BINARY_OP                0 (+)

 330            STORE_FAST              11 (pre_mac)

 338            LOAD_GLOBAL             17 (compute_mac + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (mac_key, pre_mac)
                CALL                     2
                STORE_FAST              12 (mac)

 340            LOAD_GLOBAL             19 (open + NULL)
                LOAD_FAST_BORROW         0 (output_path)
                LOAD_CONST               2 ('wb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L7:     STORE_FAST              13 (fh)

 341            LOAD_FAST_BORROW        13 (fh)
                LOAD_ATTR               21 (write + NULL|self)
                LOAD_FAST_BORROW        11 (pre_mac)
                CALL                     1
                POP_TOP

 342            LOAD_FAST_BORROW        13 (fh)
                LOAD_ATTR               21 (write + NULL|self)
                LOAD_FAST_BORROW        12 (mac)
                CALL                     1
                POP_TOP

 343            LOAD_FAST_BORROW        13 (fh)
                LOAD_ATTR               21 (write + NULL|self)
                LOAD_FAST_BORROW         4 (ciphertext)
                CALL                     1
                POP_TOP

 340    L8:     LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                LOAD_CONST               3 (None)
                CALL                     3
                POP_TOP
                LOAD_CONST               3 (None)
                RETURN_VALUE
        L9:     PUSH_EXC_INFO
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
                LOAD_CONST               3 (None)
                RETURN_VALUE

  --   L12:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L7 to L8 -> L9 [2] lasti
  L9 to L11 -> L12 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2A60, file "scripts\package_backup.py", line 346>:
346           RESUME                   0
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object read_archive_header at 0x0000018C177C5D50, file "scripts\package_backup.py", line 346>:
 346            RESUME                   0

 369            LOAD_FAST_BORROW         0 (path)
                LOAD_ATTR                1 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        21 (to L1)
                NOT_TAKEN

 370            LOAD_GLOBAL              3 (FileNotFoundError + NULL)
                LOAD_GLOBAL              5 (str + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                CALL                     1
                RAISE_VARARGS            1

 372    L1:     LOAD_GLOBAL              7 (open + NULL)
                LOAD_FAST_BORROW         0 (path)
                LOAD_CONST               1 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L2:     STORE_FAST               1 (fh)

 373            LOAD_FAST_BORROW         1 (fh)
                LOAD_ATTR                9 (read + NULL|self)
                CALL                     0
                STORE_FAST               2 (data)

 372    L3:     LOAD_CONST               2 (None)
                LOAD_CONST               2 (None)
                LOAD_CONST               2 (None)
                CALL                     3
                POP_TOP

 375    L4:     LOAD_GLOBAL             11 (len + NULL)
                LOAD_FAST_CHECK          2 (data)
                CALL                     1
                LOAD_GLOBAL             11 (len + NULL)
                LOAD_GLOBAL             12 (MAGIC)
                CALL                     1
                LOAD_SMALL_INT           2
                BINARY_OP                0 (+)
                LOAD_GLOBAL             14 (struct)
                LOAD_ATTR               16 (calcsize)
                PUSH_NULL
                LOAD_GLOBAL             18 (_LENGTHS_STRUCT)
                CALL                     1
                BINARY_OP                0 (+)
                LOAD_GLOBAL             20 (MAC_LEN)
                BINARY_OP                0 (+)
                COMPARE_OP              18 (bool(<))
                POP_JUMP_IF_FALSE       12 (to L5)
                NOT_TAKEN

 376            LOAD_GLOBAL             23 (ValueError + NULL)
                LOAD_CONST               3 ('archive too short to contain a header')
                CALL                     1
                RAISE_VARARGS            1

 377    L5:     LOAD_FAST_BORROW         2 (data)
                LOAD_CONST               2 (None)
                LOAD_GLOBAL             11 (len + NULL)
                LOAD_GLOBAL             12 (MAGIC)
                CALL                     1
                BINARY_SLICE
                LOAD_GLOBAL             12 (MAGIC)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       12 (to L6)
                NOT_TAKEN

 378            LOAD_GLOBAL             23 (ValueError + NULL)
                LOAD_CONST               4 ('bad magic — not a PASBAK archive')
                CALL                     1
                RAISE_VARARGS            1

 380    L6:     LOAD_GLOBAL             11 (len + NULL)
                LOAD_GLOBAL             12 (MAGIC)
                CALL                     1
                STORE_FAST               3 (pos)

 381            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                BINARY_OP               26 ([])
                STORE_FAST_LOAD_FAST    67 (version, pos)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 382            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                BINARY_OP               26 ([])
                STORE_FAST_LOAD_FAST    83 (flags, pos)
                LOAD_SMALL_INT           1
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 383            LOAD_FAST_BORROW         4 (version)
                LOAD_GLOBAL             24 (ARCHIVE_VERSION)
                COMPARE_OP             119 (bool(!=))
                POP_JUMP_IF_FALSE       15 (to L7)
                NOT_TAKEN

 384            LOAD_GLOBAL             23 (ValueError + NULL)
                LOAD_CONST               5 ('unsupported archive version ')
                LOAD_FAST_BORROW         4 (version)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                RAISE_VARARGS            1

 386    L7:     LOAD_GLOBAL             14 (struct)
                LOAD_ATTR               26 (unpack)
                PUSH_NULL

 387            LOAD_GLOBAL             18 (_LENGTHS_STRUCT)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                LOAD_FAST_BORROW         3 (pos)
                LOAD_GLOBAL             14 (struct)
                LOAD_ATTR               16 (calcsize)
                PUSH_NULL
                LOAD_GLOBAL             18 (_LENGTHS_STRUCT)
                CALL                     1
                BINARY_OP                0 (+)
                BINARY_SLICE

 386            CALL                     2
                UNPACK_SEQUENCE          3
                STORE_FAST_STORE_FAST  103 (salt_len, nonce_len)
                STORE_FAST               8 (header_len)

 389            LOAD_FAST_BORROW         3 (pos)
                LOAD_GLOBAL             14 (struct)
                LOAD_ATTR               16 (calcsize)
                PUSH_NULL
                LOAD_GLOBAL             18 (_LENGTHS_STRUCT)
                CALL                     1
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 391            LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (pos, salt_len)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         7 (nonce_len)
                BINARY_OP                0 (+)
                LOAD_FAST_BORROW         8 (header_len)
                BINARY_OP                0 (+)
                LOAD_GLOBAL             20 (MAC_LEN)
                BINARY_OP                0 (+)
                LOAD_GLOBAL             11 (len + NULL)
                LOAD_FAST_BORROW         2 (data)
                CALL                     1
                COMPARE_OP             148 (bool(>))
                POP_JUMP_IF_FALSE       12 (to L8)
                NOT_TAKEN

 392            LOAD_GLOBAL             23 (ValueError + NULL)
                LOAD_CONST               6 ('archive truncated — declared lengths overflow file')
                CALL                     1
                RAISE_VARARGS            1

 394    L8:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (pos, salt_len)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST_LOAD_FAST   147 (salt, pos)
                LOAD_FAST_BORROW         6 (salt_len)
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 395            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (pos, nonce_len)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST_LOAD_FAST   163 (nonce, pos)
                LOAD_FAST_BORROW         7 (nonce_len)
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 396            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 56 (pos, header_len)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST_LOAD_FAST   179 (header_bytes, pos)
                STORE_FAST              12 (header_offset)

 397            LOAD_FAST_BORROW_LOAD_FAST_BORROW 56 (pos, header_len)
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 398            LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (data, pos)
                LOAD_FAST_BORROW         3 (pos)
                LOAD_GLOBAL             20 (MAC_LEN)
                BINARY_OP                0 (+)
                BINARY_SLICE
                STORE_FAST_LOAD_FAST   211 (mac, pos)
                LOAD_GLOBAL             20 (MAC_LEN)
                BINARY_OP               13 (+=)
                STORE_FAST               3 (pos)

 400            NOP

 401    L9:     LOAD_FAST_BORROW         8 (header_len)
                TO_BOOL
                POP_JUMP_IF_FALSE       38 (to L12)
       L10:     NOT_TAKEN
       L11:     LOAD_GLOBAL             28 (json)
                LOAD_ATTR               30 (loads)
                PUSH_NULL
                LOAD_FAST_BORROW        11 (header_bytes)
                LOAD_ATTR               33 (decode + NULL|self)
                LOAD_CONST               7 ('utf-8')
                CALL                     1
                CALL                     1
                JUMP_FORWARD             1 (to L13)
       L12:     BUILD_MAP                0
       L13:     STORE_FAST              14 (header)

 406   L14:     LOAD_CONST               9 ('magic')
                LOAD_GLOBAL             12 (MAGIC)

 407            LOAD_CONST              10 ('version')
                LOAD_FAST                4 (version)

 408            LOAD_CONST              11 ('flags')
                LOAD_FAST                5 (flags)

 409            LOAD_CONST              12 ('encrypted')
                LOAD_GLOBAL             37 (bool + NULL)
                LOAD_FAST                5 (flags)
                LOAD_GLOBAL             38 (FLAG_ENCRYPTED)
                BINARY_OP                1 (&)
                CALL                     1

 410            LOAD_CONST              13 ('salt')
                LOAD_FAST                9 (salt)

 411            LOAD_CONST              14 ('nonce')
                LOAD_FAST               10 (nonce)

 412            LOAD_CONST              15 ('header')
                LOAD_FAST               14 (header)

 413            LOAD_CONST              16 ('header_len')
                LOAD_FAST                8 (header_len)

 414            LOAD_CONST              17 ('mac')
                LOAD_FAST               13 (mac)

 415            LOAD_CONST              18 ('header_offset')
                LOAD_FAST               12 (header_offset)

 416            LOAD_CONST              19 ('ciphertext_offset')
                LOAD_FAST                3 (pos)

 417            LOAD_CONST              20 ('ciphertext_len')
                LOAD_GLOBAL             11 (len + NULL)
                LOAD_FAST                2 (data)
                CALL                     1
                LOAD_FAST                3 (pos)
                BINARY_OP               10 (-)

 405            BUILD_MAP               12
                RETURN_VALUE

 372   L15:     PUSH_EXC_INFO
                WITH_EXCEPT_START
                TO_BOOL
                POP_JUMP_IF_TRUE         2 (to L16)
                NOT_TAKEN
                RERAISE                  2
       L16:     POP_TOP
       L17:     POP_EXCEPT
                POP_TOP
                POP_TOP
                POP_TOP
                EXTENDED_ARG             2
                JUMP_BACKWARD_NO_INTERRUPT 566 (to L4)

  --   L18:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L19:     PUSH_EXC_INFO

 402            LOAD_GLOBAL             34 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE       20 (to L22)
                NOT_TAKEN
                STORE_FAST              15 (e)

 403   L20:     LOAD_GLOBAL             23 (ValueError + NULL)
                LOAD_CONST               8 ('header is not valid JSON: ')
                LOAD_FAST               15 (e)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                RAISE_VARARGS            1

  --   L21:     LOAD_CONST               2 (None)
                STORE_FAST              15 (e)
                DELETE_FAST             15 (e)
                RERAISE                  1

 402   L22:     RERAISE                  0

  --   L23:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L2 to L3 -> L15 [2] lasti
  L9 to L10 -> L19 [0]
  L11 to L14 -> L19 [0]
  L15 to L17 -> L18 [4] lasti
  L19 to L20 -> L23 [1] lasti
  L20 to L21 -> L21 [1] lasti
  L21 to L23 -> L23 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C17FA2C40, file "scripts\package_backup.py", line 421>:
421           RESUME                   0
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
              LOAD_CONST               4 ('dict')
              BUILD_MAP                2
              RETURN_VALUE

Disassembly of <code object read_archive_full at 0x0000018C18060DB0, file "scripts\package_backup.py", line 421>:
 421           RESUME                   0

 423           LOAD_GLOBAL              1 (read_archive_header + NULL)
               LOAD_FAST_BORROW         0 (path)
               CALL                     1
               STORE_FAST               1 (info)

 424           LOAD_GLOBAL              3 (open + NULL)
               LOAD_FAST_BORROW         0 (path)
               LOAD_CONST               1 ('rb')
               CALL                     2
               COPY                     1
               LOAD_SPECIAL             1 (__exit__)
               SWAP                     2
               SWAP                     3
               LOAD_SPECIAL             0 (__enter__)
               CALL                     0
       L1:     STORE_FAST               2 (fh)

 425           LOAD_FAST_BORROW         2 (fh)
               LOAD_ATTR                5 (seek + NULL|self)
               LOAD_FAST_BORROW         1 (info)
               LOAD_CONST               2 ('ciphertext_offset')
               BINARY_OP               26 ([])
               CALL                     1
               POP_TOP

 426           LOAD_FAST_BORROW         2 (fh)
               LOAD_ATTR                7 (read + NULL|self)
               CALL                     0
               LOAD_FAST_BORROW         1 (info)
               LOAD_CONST               3 ('ciphertext')
               STORE_SUBSCR

 424   L2:     LOAD_CONST               4 (None)
               LOAD_CONST               4 (None)
               LOAD_CONST               4 (None)
               CALL                     3
               POP_TOP

 427           LOAD_FAST_BORROW         1 (info)
               RETURN_VALUE

 424   L3:     PUSH_EXC_INFO
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

 427           LOAD_FAST                1 (info)
               RETURN_VALUE

  --   L6:     COPY                     3
               POP_EXCEPT
               RERAISE                  1
ExceptionTable:
  L1 to L2 -> L3 [2] lasti
  L3 to L5 -> L6 [4] lasti

Disassembly of <code object __annotate__ at 0x0000018C18024930, file "scripts\package_backup.py", line 430>:
430           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('path')
              LOAD_CONST               2 ('Path')
              LOAD_CONST               3 ('mac_key')
              LOAD_CONST               4 ('bytes')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('bool')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object verify_archive_mac_from_disk at 0x0000018C17D76C00, file "scripts\package_backup.py", line 430>:
 430            RESUME                   0

 436            NOP

 437    L1:     LOAD_GLOBAL              1 (read_archive_header + NULL)
                LOAD_FAST_BORROW         0 (path)
                CALL                     1
                STORE_FAST               2 (info)

 440    L2:     LOAD_FAST                2 (info)
                LOAD_CONST               2 ('header_offset')
                BINARY_OP               26 ([])
                LOAD_FAST                2 (info)
                LOAD_CONST               3 ('header_len')
                BINARY_OP               26 ([])
                BINARY_OP                0 (+)
                STORE_FAST               3 (pre_mac_end)

 441            NOP

 442    L3:     LOAD_GLOBAL              5 (open + NULL)
                LOAD_FAST                0 (path)
                LOAD_CONST               4 ('rb')
                CALL                     2
                COPY                     1
                LOAD_SPECIAL             1 (__exit__)
                SWAP                     2
                SWAP                     3
                LOAD_SPECIAL             0 (__enter__)
                CALL                     0
        L4:     STORE_FAST               4 (fh)

 443            LOAD_FAST                4 (fh)
                LOAD_ATTR                7 (read + NULL|self)
                LOAD_FAST                3 (pre_mac_end)
                CALL                     1
                STORE_FAST               5 (pre_mac_bytes)

 442    L5:     LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                LOAD_CONST               5 (None)
                CALL                     3
                POP_TOP

 446    L6:     LOAD_GLOBAL              9 (compute_mac + NULL)
                LOAD_FAST                1 (mac_key)
                LOAD_FAST_CHECK          5 (pre_mac_bytes)
                CALL                     2
                STORE_FAST               6 (actual)

 447            LOAD_GLOBAL             10 (hmac)
                LOAD_ATTR               12 (compare_digest)
                PUSH_NULL
                LOAD_FAST                2 (info)
                LOAD_CONST               6 ('mac')
                BINARY_OP               26 ([])
                LOAD_FAST                6 (actual)
                CALL                     2
                RETURN_VALUE

  --    L7:     PUSH_EXC_INFO

 438            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L9)
                NOT_TAKEN
                POP_TOP

 439    L8:     POP_EXCEPT
                LOAD_CONST               1 (False)
                RETURN_VALUE

 438    L9:     RERAISE                  0

  --   L10:     COPY                     3
                POP_EXCEPT
                RERAISE                  1

 442   L11:     PUSH_EXC_INFO
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
       L14:     JUMP_BACKWARD_NO_INTERRUPT 76 (to L6)

  --   L15:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
       L16:     PUSH_EXC_INFO

 444            LOAD_GLOBAL              2 (Exception)
                CHECK_EXC_MATCH
                POP_JUMP_IF_FALSE        5 (to L18)
                NOT_TAKEN
                POP_TOP

 445   L17:     POP_EXCEPT
                LOAD_CONST               1 (False)
                RETURN_VALUE

 444   L18:     RERAISE                  0

  --   L19:     COPY                     3
                POP_EXCEPT
                RERAISE                  1
ExceptionTable:
  L1 to L2 -> L7 [0]
  L3 to L4 -> L16 [0]
  L4 to L5 -> L11 [2] lasti
  L5 to L6 -> L16 [0]
  L7 to L8 -> L10 [1] lasti
  L9 to L10 -> L10 [1] lasti
  L11 to L13 -> L15 [4] lasti
  L13 to L14 -> L16 [0]
  L15 to L16 -> L16 [0]
  L16 to L17 -> L19 [1] lasti
  L18 to L19 -> L19 [1] lasti

Disassembly of <code object __annotate__ at 0x0000018C18026130, file "scripts\package_backup.py", line 454>:
454           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('label')
              LOAD_CONST               2 ('str')
              LOAD_CONST               3 ('ok')
              LOAD_CONST               4 ('bool')
              LOAD_CONST               5 ('detail')
              LOAD_CONST               2 ('str')
              LOAD_CONST               6 ('return')
              LOAD_CONST               7 ('None')
              BUILD_MAP                4
              RETURN_VALUE

Disassembly of <code object _status at 0x0000018C18038670, file "scripts\package_backup.py", line 454>:
454           RESUME                   0

455           LOAD_FAST_BORROW         1 (ok)
              TO_BOOL
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_CONST               0 ('PASS')
              JUMP_FORWARD             1 (to L2)
      L1:     LOAD_CONST               1 ('FAIL')
      L2:     STORE_FAST               3 (tag)

456           LOAD_CONST               2 ('[')
              LOAD_FAST_BORROW         3 (tag)
              FORMAT_SIMPLE
              LOAD_CONST               3 ('] ')
              LOAD_FAST_BORROW         0 (label)
              FORMAT_SIMPLE
              BUILD_STRING             4
              STORE_FAST               4 (line)

457           LOAD_FAST_BORROW         2 (detail)
              TO_BOOL
              POP_JUMP_IF_FALSE       13 (to L3)
              NOT_TAKEN

458           LOAD_FAST_BORROW         4 (line)
              LOAD_CONST               4 (' — ')
              LOAD_FAST_BORROW         2 (detail)
              FORMAT_SIMPLE
              BUILD_STRING             2
              BINARY_OP               13 (+=)
              STORE_FAST               4 (line)

459   L3:     LOAD_GLOBAL              1 (print + NULL)
              LOAD_FAST_BORROW         4 (line)
              CALL                     1
              POP_TOP
              LOAD_CONST               5 (None)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C18026530, file "scripts\package_backup.py", line 466>:
466           RESUME                   0
              LOAD_FAST_BORROW         0 (format)
              LOAD_SMALL_INT           2
              COMPARE_OP             132 (>)
              POP_JUMP_IF_FALSE        3 (to L1)
              NOT_TAKEN
              LOAD_COMMON_CONSTANT     1 (NotImplementedError)
              RAISE_VARARGS            1
      L1:     LOAD_CONST               1 ('arg_value')
              LOAD_CONST               2 ('Optional[str]')
              LOAD_CONST               3 ('stamp')
              LOAD_CONST               4 ('str')
              LOAD_CONST               5 ('return')
              LOAD_CONST               6 ('Path')
              BUILD_MAP                3
              RETURN_VALUE

Disassembly of <code object _resolve_output_path at 0x0000018C17F962B0, file "scripts\package_backup.py", line 466>:
466           RESUME                   0

467           LOAD_FAST_BORROW         0 (arg_value)
              TO_BOOL
              POP_JUMP_IF_FALSE       12 (to L1)
              NOT_TAKEN
              LOAD_GLOBAL              1 (Path + NULL)
              LOAD_FAST_BORROW         0 (arg_value)
              CALL                     1
              JUMP_FORWARD            27 (to L2)
      L1:     LOAD_GLOBAL              0 (Path)
              LOAD_ATTR                2 (cwd)
              PUSH_NULL
              CALL                     0
              LOAD_CONST               0 ('recovery')
              BINARY_OP               11 (/)
      L2:     STORE_FAST               2 (base)

468           LOAD_FAST_BORROW         2 (base)
              LOAD_ATTR                5 (mkdir + NULL|self)
              LOAD_CONST               1 (True)
              LOAD_CONST               1 (True)
              LOAD_CONST               2 (('parents', 'exist_ok'))
              CALL_KW                  2
              POP_TOP

469           LOAD_FAST_BORROW         2 (base)
              LOAD_CONST               3 ('recovery_')
              LOAD_FAST_BORROW         1 (stamp)
              FORMAT_SIMPLE
              LOAD_CONST               4 ('.pasbak')
              BUILD_STRING             3
              BINARY_OP               11 (/)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3690, file "scripts\package_backup.py", line 472>:
472           RESUME                   0
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

Disassembly of <code object _read_passphrase at 0x0000018C18039070, file "scripts\package_backup.py", line 472>:
472           RESUME                   0

474           LOAD_FAST_BORROW         0 (env_var)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L1)
              NOT_TAKEN

475           LOAD_CONST               1 (None)
              RETURN_VALUE

476   L1:     LOAD_GLOBAL              0 (os)
              LOAD_ATTR                2 (environ)
              LOAD_ATTR                5 (get + NULL|self)
              LOAD_FAST_BORROW         0 (env_var)
              CALL                     1
              STORE_FAST               1 (val)

477           LOAD_FAST_BORROW         1 (val)
              TO_BOOL
              POP_JUMP_IF_TRUE         3 (to L2)
              NOT_TAKEN

478           LOAD_CONST               1 (None)
              RETURN_VALUE

479   L2:     LOAD_FAST_BORROW         1 (val)
              RETURN_VALUE

Disassembly of <code object __annotate__ at 0x0000018C17FA3870, file "scripts\package_backup.py", line 482>:
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

Disassembly of <code object main at 0x0000018C17E8AEE0, file "scripts\package_backup.py", line 482>:
 482            RESUME                   0

 483            LOAD_GLOBAL              0 (argparse)
                LOAD_ATTR                2 (ArgumentParser)
                PUSH_NULL

 484            LOAD_CONST               0 ('package_backup')

 485            LOAD_CONST               1 ('PAS143G — encrypted backup packaging.')

 483            LOAD_CONST               2 (('prog', 'description'))
                CALL_KW                  2
                STORE_FAST               1 (parser)

 487            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               3 ('--input-dir')
                LOAD_CONST               4 (True)

 488            LOAD_CONST               5 ('Verified PAS143D backup directory.')

 487            LOAD_CONST               6 (('required', 'help'))
                CALL_KW                  3
                POP_TOP

 489            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST               7 ('--output-dir')
                LOAD_CONST               8 (None)

 490            LOAD_CONST               9 ('Where to write the .pasbak archive (default: ./recovery).')

 489            LOAD_CONST              10 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 491            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              11 ('--passphrase-env')
                LOAD_CONST               8 (None)

 492            LOAD_CONST              12 ('Name of the env var holding the passphrase.')

 491            LOAD_CONST              10 (('default', 'help'))
                CALL_KW                  3
                POP_TOP

 493            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              13 ('--dry-run')
                LOAD_CONST              14 ('store_true')

 494            LOAD_CONST              15 ('Print what would happen without writing the archive.')

 493            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 495            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              17 ('--inspect')
                LOAD_CONST              14 ('store_true')

 496            LOAD_CONST              18 ('Print the planned manifest + file list and exit.')

 495            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 497            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                5 (add_argument + NULL|self)
                LOAD_CONST              19 ('--allow-unverified')
                LOAD_CONST              14 ('store_true')

 498            LOAD_CONST              20 ('Permit packaging when verification_report.json is absent.')

 497            LOAD_CONST              16 (('action', 'help'))
                CALL_KW                  3
                POP_TOP

 499            LOAD_FAST_BORROW         1 (parser)
                LOAD_ATTR                7 (parse_args + NULL|self)
                LOAD_FAST_BORROW         0 (argv)
                CALL                     1
                STORE_FAST               2 (args)

 501            LOAD_GLOBAL              9 (Path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               10 (input_dir)
                CALL                     1
                STORE_FAST               3 (input_dir)

 502            LOAD_FAST_BORROW         3 (input_dir)
                LOAD_ATTR               13 (exists + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_FALSE       23 (to L1)
                NOT_TAKEN
                LOAD_FAST_BORROW         3 (input_dir)
                LOAD_ATTR               15 (is_dir + NULL|self)
                CALL                     0
                TO_BOOL
                POP_JUMP_IF_TRUE        25 (to L2)
                NOT_TAKEN

 503    L1:     LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              21 ('Input directory exists')
                LOAD_CONST              22 (False)
                LOAD_GLOBAL             19 (str + NULL)
                LOAD_FAST_BORROW         3 (input_dir)
                CALL                     1
                CALL                     3
                POP_TOP

 504            LOAD_SMALL_INT           6
                RETURN_VALUE

 506    L2:     LOAD_GLOBAL             21 (_walk_files + NULL)
                LOAD_FAST_BORROW         3 (input_dir)
                CALL                     1
                STORE_FAST               4 (files)

 507            LOAD_FAST_BORROW         4 (files)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L3)
                NOT_TAKEN

 508            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              23 ('Input directory non-empty')
                LOAD_CONST              22 (False)
                LOAD_CONST              24 ('no files found')
                CALL                     3
                POP_TOP

 509            LOAD_SMALL_INT           6
                RETURN_VALUE

 511    L3:     LOAD_GLOBAL             23 (read_backup_manifest + NULL)
                LOAD_FAST_BORROW         3 (input_dir)
                CALL                     1
                STORE_FAST               5 (backup_manifest)

 512            LOAD_FAST_BORROW         5 (backup_manifest)
                POP_JUMP_IF_NOT_NONE    16 (to L4)
                NOT_TAKEN

 513            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              25 ('backup_manifest.json present')
                LOAD_CONST              22 (False)
                LOAD_CONST              26 ('missing or unreadable')
                CALL                     3
                POP_TOP

 514            LOAD_SMALL_INT           6
                RETURN_VALUE

 515    L4:     LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              25 ('backup_manifest.json present')
                LOAD_CONST               4 (True)
                CALL                     2
                POP_TOP

 517            LOAD_GLOBAL             25 (read_verification_report + NULL)
                LOAD_FAST_BORROW         3 (input_dir)
                CALL                     1
                STORE_FAST               6 (verif)

 518            LOAD_GLOBAL             27 (verification_summary + NULL)
                LOAD_FAST_BORROW         6 (verif)
                CALL                     1
                STORE_FAST               7 (summary)

 519            LOAD_FAST_BORROW         6 (verif)
                POP_JUMP_IF_NOT_NONE    34 (to L5)
                NOT_TAKEN
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               28 (allow_unverified)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L5)
                NOT_TAKEN

 520            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              27 ('verification_report.json present')
                LOAD_CONST              22 (False)

 521            LOAD_CONST              28 ('Re-run scripts/verify_backup.py first, or pass --allow-unverified.')

 520            CALL                     3
                POP_TOP

 522            LOAD_SMALL_INT           4
                RETURN_VALUE

 523    L5:     LOAD_FAST_BORROW         6 (verif)
                POP_JUMP_IF_NONE        33 (to L6)
                NOT_TAKEN
                LOAD_GLOBAL             31 (has_checksum_mismatch + NULL)
                LOAD_FAST_BORROW         6 (verif)
                CALL                     1
                TO_BOOL
                POP_JUMP_IF_FALSE       16 (to L6)
                NOT_TAKEN

 524            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              29 ('Backup integrity (no checksum mismatch)')
                LOAD_CONST              22 (False)

 525            LOAD_CONST              30 ('Verification recorded a SHA-256 mismatch — refuse to package.')

 524            CALL                     3
                POP_TOP

 526            LOAD_SMALL_INT           5
                RETURN_VALUE

 527    L6:     LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              31 ('verification_report.json')
                LOAD_CONST               4 (True)

 528            LOAD_CONST              32 ('checks_run=')
                LOAD_FAST_BORROW         7 (summary)
                LOAD_CONST              33 ('checks_run')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              34 (' all_passed=')
                LOAD_FAST_BORROW         7 (summary)
                LOAD_CONST              35 ('all_passed')
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                BUILD_STRING             4

 527            CALL                     3
                POP_TOP

 533            LOAD_GLOBAL             33 (_build_tar_gz + NULL)
                LOAD_FAST_BORROW         3 (input_dir)
                CALL                     1
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  137 (plaintext, arc_names)

 534            LOAD_GLOBAL             34 (hashlib)
                LOAD_ATTR               36 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW         8 (plaintext)
                CALL                     1
                LOAD_ATTR               39 (hexdigest + NULL|self)
                CALL                     0
                STORE_FAST              10 (plaintext_sha)

 536            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               40 (inspect)
                TO_BOOL
                POP_JUMP_IF_FALSE      217 (to L13)
                NOT_TAKEN

 538            LOAD_GLOBAL             43 (build_recovery_manifest + NULL)

 539            LOAD_FAST_BORROW         3 (input_dir)

 540            LOAD_FAST_BORROW         9 (arc_names)

 541            LOAD_FAST_BORROW        10 (plaintext_sha)

 542            LOAD_GLOBAL             44 (ARCHIVE_VERSION)

 543            LOAD_CONST               4 (True)

 544            LOAD_FAST_BORROW         7 (summary)

 538            LOAD_CONST              36 (('input_dir', 'arc_names', 'plaintext_sha256', 'archive_version', 'encrypted', 'verification'))
                CALL_KW                  6
                STORE_FAST              11 (manifest)

 546            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              37 ('== INSPECT — would package the following ==')
                CALL                     1
                POP_TOP

 547            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              38 ('  files:        ')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW         9 (arc_names)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 548            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              39 ('  plaintext:    ')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW         8 (plaintext)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              40 (' bytes (sha256=')
                LOAD_FAST_BORROW        10 (plaintext_sha)
                LOAD_CONST              41 (slice(None, 16, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              42 ('…)')
                BUILD_STRING             5
                CALL                     1
                POP_TOP

 549            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              43 ('  archive_version: ')
                LOAD_GLOBAL             44 (ARCHIVE_VERSION)
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 550            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              44 ('  manifest_hash: ')
                LOAD_GLOBAL             51 (manifest_hash + NULL)
                LOAD_FAST_BORROW        11 (manifest)
                CALL                     1
                LOAD_CONST              41 (slice(None, 16, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              45 ('…')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 551            LOAD_GLOBAL             47 (print + NULL)
                LOAD_GLOBAL             52 (json)
                LOAD_ATTR               54 (dumps)
                PUSH_NULL
                LOAD_FAST_BORROW        11 (manifest)
                LOAD_ATTR               57 (items + NULL|self)
                CALL                     0
                GET_ITER
                LOAD_FAST_AND_CLEAR     12 (k)
                LOAD_FAST_AND_CLEAR     13 (v)
                SWAP                     3
        L7:     BUILD_MAP                0
                SWAP                     2
        L8:     FOR_ITER                16 (to L11)
                UNPACK_SEQUENCE          2
                STORE_FAST_STORE_FAST  205 (k, v)
                LOAD_FAST_BORROW        12 (k)
                LOAD_CONST              46 ('included_files')
                COMPARE_OP             119 (bool(!=))
        L9:     POP_JUMP_IF_TRUE         3 (to L10)
                NOT_TAKEN
                JUMP_BACKWARD           14 (to L8)
       L10:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (k, v)
                MAP_ADD                  2
                JUMP_BACKWARD           18 (to L8)
       L11:     END_FOR
                POP_ITER
       L12:     SWAP                     3
                STORE_FAST              13 (v)
                STORE_FAST              12 (k)

 552            LOAD_SMALL_INT           2

 551            LOAD_CONST              47 (('indent',))
                CALL_KW                  2
                CALL                     1
                POP_TOP

 553            LOAD_SMALL_INT           0
                RETURN_VALUE

 556   L13:     LOAD_GLOBAL             59 (_read_passphrase + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               60 (passphrase_env)
                CALL                     1
                STORE_FAST              14 (passphrase)

 557            LOAD_FAST_BORROW        14 (passphrase)
                TO_BOOL
                POP_JUMP_IF_TRUE        16 (to L14)
                NOT_TAKEN

 558            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              48 ('Passphrase resolution')
                LOAD_CONST              22 (False)

 559            LOAD_CONST              49 ('Pass --passphrase-env VAR_NAME with a non-empty value.')

 558            CALL                     3
                POP_TOP

 560            LOAD_SMALL_INT           3
                RETURN_VALUE

 561   L14:     LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              48 ('Passphrase resolution')
                LOAD_CONST               4 (True)

 562            LOAD_CONST              50 ('env=')
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               60 (passphrase_env)
                FORMAT_SIMPLE
                LOAD_CONST              51 (' (length not echoed)')
                BUILD_STRING             3

 561            CALL                     3
                POP_TOP

 564            LOAD_GLOBAL             62 (secrets)
                LOAD_ATTR               64 (token_bytes)
                PUSH_NULL
                LOAD_GLOBAL             66 (SALT_LEN)
                CALL                     1
                STORE_FAST              15 (salt)

 565            LOAD_GLOBAL             62 (secrets)
                LOAD_ATTR               64 (token_bytes)
                PUSH_NULL
                LOAD_GLOBAL             68 (NONCE_LEN)
                CALL                     1
                STORE_FAST              16 (nonce)

 566            LOAD_GLOBAL             71 (derive_keys + NULL)
                LOAD_FAST_BORROW_LOAD_FAST_BORROW 239 (passphrase, salt)
                CALL                     2
                UNPACK_SEQUENCE          2
                STORE_FAST              17 (enc_key)
                STORE_FAST              18 (mac_key)

 568            LOAD_GLOBAL             43 (build_recovery_manifest + NULL)

 569            LOAD_FAST_BORROW         3 (input_dir)

 570            LOAD_FAST_BORROW         9 (arc_names)

 571            LOAD_FAST_BORROW        10 (plaintext_sha)

 572            LOAD_GLOBAL             44 (ARCHIVE_VERSION)

 573            LOAD_CONST               4 (True)

 574            LOAD_FAST_BORROW         7 (summary)

 568            LOAD_CONST              36 (('input_dir', 'arc_names', 'plaintext_sha256', 'archive_version', 'encrypted', 'verification'))
                CALL_KW                  6
                STORE_FAST              11 (manifest)

 577            LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               72 (dry_run)
                TO_BOOL
                POP_JUMP_IF_FALSE      142 (to L15)
                NOT_TAKEN

 578            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              52 ('Dry-run plan')
                LOAD_CONST               4 (True)
                CALL                     2
                POP_TOP

 579            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              53 ('  would write archive with:')
                CALL                     1
                POP_TOP

 580            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              54 ('    file_count:    ')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW         9 (arc_names)
                CALL                     1
                FORMAT_SIMPLE
                BUILD_STRING             2
                CALL                     1
                POP_TOP

 581            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              55 ('    plaintext:     ')
                LOAD_GLOBAL             49 (len + NULL)
                LOAD_FAST_BORROW         8 (plaintext)
                CALL                     1
                FORMAT_SIMPLE
                LOAD_CONST              56 (' bytes')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 582            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              57 ('    salt:          ')
                LOAD_GLOBAL             66 (SALT_LEN)
                FORMAT_SIMPLE
                LOAD_CONST              58 (' bytes (random)')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 583            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              59 ('    nonce:         ')
                LOAD_GLOBAL             68 (NONCE_LEN)
                FORMAT_SIMPLE
                LOAD_CONST              58 (' bytes (random)')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 584            LOAD_GLOBAL             47 (print + NULL)
                LOAD_CONST              60 ('    manifest_hash: ')
                LOAD_GLOBAL             51 (manifest_hash + NULL)
                LOAD_FAST_BORROW        11 (manifest)
                CALL                     1
                LOAD_CONST              41 (slice(None, 16, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              45 ('…')
                BUILD_STRING             3
                CALL                     1
                POP_TOP

 585            LOAD_SMALL_INT           0
                RETURN_VALUE

 587   L15:     LOAD_GLOBAL             75 (now_stamp + NULL)
                CALL                     0
                STORE_FAST              19 (stamp)

 588            LOAD_GLOBAL             77 (_resolve_output_path + NULL)
                LOAD_FAST_BORROW         2 (args)
                LOAD_ATTR               78 (output_dir)
                LOAD_FAST_BORROW        19 (stamp)
                CALL                     2
                STORE_FAST              20 (out_path)

 589            LOAD_GLOBAL             81 (serialize_manifest + NULL)
                LOAD_FAST_BORROW        11 (manifest)
                CALL                     1
                STORE_FAST              21 (inspectable_header_bytes)

 590            LOAD_GLOBAL             83 (encrypt + NULL)
                LOAD_FAST_BORROW         8 (plaintext)
                LOAD_FAST_BORROW        17 (enc_key)
                LOAD_FAST_BORROW        16 (nonce)
                CALL                     3
                STORE_FAST              22 (ciphertext)

 592            LOAD_GLOBAL             85 (write_archive + NULL)

 593            LOAD_FAST_BORROW        20 (out_path)

 594            LOAD_FAST_BORROW        15 (salt)

 595            LOAD_FAST_BORROW        16 (nonce)

 596            LOAD_FAST_BORROW        21 (inspectable_header_bytes)

 597            LOAD_FAST_BORROW        22 (ciphertext)

 598            LOAD_FAST_BORROW        18 (mac_key)

 599            LOAD_CONST               4 (True)

 592            LOAD_CONST              61 (('output_path', 'salt', 'nonce', 'inspectable_header', 'ciphertext', 'mac_key', 'encrypted'))
                CALL_KW                  7
                POP_TOP

 602            LOAD_GLOBAL             34 (hashlib)
                LOAD_ATTR               36 (sha256)
                PUSH_NULL
                LOAD_FAST_BORROW        20 (out_path)
                LOAD_ATTR               87 (read_bytes + NULL|self)
                CALL                     0
                CALL                     1
                LOAD_ATTR               39 (hexdigest + NULL|self)
                CALL                     0
                STORE_FAST              23 (archive_sha)

 603            LOAD_GLOBAL             17 (_status + NULL)
                LOAD_CONST              62 ('Archive written')
                LOAD_CONST               4 (True)

 604            LOAD_FAST_BORROW        20 (out_path)
                FORMAT_SIMPLE
                LOAD_CONST              63 (' (')
                LOAD_FAST_BORROW        20 (out_path)
                LOAD_ATTR               89 (stat + NULL|self)
                CALL                     0
                LOAD_ATTR               90 (st_size)
                FORMAT_SIMPLE
                LOAD_CONST              64 (' bytes), sha256=')
                LOAD_FAST_BORROW        23 (archive_sha)
                LOAD_CONST              65 (slice(None, 12, None))
                BINARY_OP               26 ([])
                FORMAT_SIMPLE
                LOAD_CONST              45 ('…')
                BUILD_STRING             6

 603            CALL                     3
                POP_TOP

 605            LOAD_SMALL_INT           0
                RETURN_VALUE

  --   L16:     SWAP                     2
                POP_TOP

 551            SWAP                     3
                STORE_FAST              13 (v)
                STORE_FAST              12 (k)
                RERAISE                  0
ExceptionTable:
  L7 to L9 -> L16 [7]
  L10 to L12 -> L16 [7]
```
