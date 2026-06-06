# PAS209.5 — Provenance Preservation & Recovery Corpus

**Date:** 2026-06-06
**Type:** Preservation + documentation only — no source restored, no replacement modules written, no bytecode deleted, PAS209 and the parked stash untouched, PAS210 not implemented.
**Artifacts produced this checkpoint:**
- `recovery/pas209_5_bytecode_corpus/` — 216 per-module text artifacts + `index.md`
- `recovery/pas209_5_bytecode_corpus/_extract_corpus.py` — the stdlib-only extractor (reproducible)
- this document

---

## 1. Why this checkpoint exists

The provenance audit (see [pas_reconciliation_2026-06-06.md](pas_reconciliation_2026-06-06.md) and the PAS Provenance Recovery Audit) established that the PAS160–190 work was **never committed to git** and exists nowhere as clean source — not in history, reflog, branches, `stash@{0}`, or `backups/`. Its **only surviving residue is stale `__pycache__` bytecode.**

That residue is fragile: it is git-ignored, and the prior reconciliation report's own action list includes "remove stale `__pycache__`." A routine cache purge, `git clean`, or recompilation under a different interpreter would **permanently destroy the only recoverable copy of ~180 lost modules.**

PAS209.5 freezes that residue into durable, reviewable, version-controlled text **before** any cleanup, rebuild, or PAS210 work begins.

---

## 2. What was preserved

A stdlib-only extractor (`marshal` + `dis`, no third-party decompiler) walked every **source-less** `.pyc` under `app/services/**`, `app/routes/**`, and `scripts/**`, and emitted one Markdown artifact per module containing:

- module path + expected (absent) source path
- `co_filename` recorded inside the bytecode
- CPython magic number (`2b0e0d0a` = CPython 3.14)
- module docstring (frequently the full original design doctrine — recovered verbatim)
- class names, function/method names
- top-level + nested string constants
- environment-key candidates
- discoverable imported module names
- full disassembly (`dis`) output

### Coverage (216 modules)

| Subsystem | Modules |
|---|---|
| ingestion | 15 |
| memory | 28 |
| security | 12 |
| operator | 18 |
| learning | 13 |
| monitoring | 6 |
| optimization | 7 |
| replay | 4 |
| tenant | 5 |
| callbacks | 3 |
| worker | 3 |
| outbound | 2 |
| brokerage | 4 |
| simulation | 2 |
| slack | 1 |
| routes | 16 |
| scripts_readiness | 77 |
| **TOTAL** | **216** |

`simulation` (2) and `slack` (1) are individual source-less modules inside otherwise-committed subsystems; they are captured for completeness. `scripts_readiness` (77) covers the PAS144–190 readiness/security checker lineage whose source is absent (PAS191–209 checker source remains committed and was therefore skipped).

The grouped, linked listing is in [`recovery/pas209_5_bytecode_corpus/index.md`](../recovery/pas209_5_bytecode_corpus/index.md).

---

## 3. Required statements of record

1. **`__pycache__` is currently the only surviving recovery source for the ~180 lost PAS160–190 modules.** There is no clean-source copy in git, reflog, any branch, the parked stash, or `backups/`.
2. **This corpus is NOT restored source code.** It contains no `.py` modules that can be imported or run.
3. **This corpus IS a reconstruction specification.** Docstrings, names, constants, env keys, imports, and disassembly together describe each module's behaviour and contracts faithfully enough to rebuild it deliberately.
4. **Clean automated decompilation is not available for CPython 3.14.** No CPython-3.14 decompiler is installed, and `uncompyle6` / `decompyle3` do not target 3.14; `pycdc` has only partial bleeding-edge support and is absent. Reconstruction must proceed from disassembly + constants, not from a decompiler.
5. **The next decision is per-subsystem: rebuild, retire, or ignore.** This checkpoint deliberately makes no such decision — it only preserves the evidence so the decision can be made safely.
6. **Nothing should delete stale bytecode until this corpus is committed and verified.** Once the corpus is committed (this checkpoint) and reviewed, the `__pycache__` residue is no longer the sole copy and may be cleaned under a separate, explicit decision.

---

## 4. Secret handling

String constants were scanned and **sensitive-looking values were redacted in place** before writing, replaced with `<REDACTED:…>` markers and flagged with 🔒. Redaction targeted PEM blocks, Fernet-shaped keys, long high-entropy base64/hex blobs (e.g. SHA-256 digests, key material, merkle hashes), and `secret/password/token/api_key`-bearing literals.

- **Modules with at least one redaction:** 22
- **Total redactions:** 22

Environment-variable **names** (identifiers such as `PAS_EMAIL_FORWARDER_SECRET_ACTIVE_KID`) are intentionally **preserved** — they are configuration contract, not secrets. Only *values* that resembled secrets were removed. Redaction is conservative by design; a few redacted blobs are likely benign digests/fixtures, but values were hidden rather than risk leaking real key material.

---

## 5. Fidelity note & caveats

- The bytecode reflects the **last local build** that also generated the May 2026 reports. Its exact correspondence to those report timestamps is unverified; reconstructed modules must be re-validated against the report contracts and freshly tested, never trusted blind.
- Disassembly preserves control flow and logic precisely; it does **not** preserve comments, exact local-variable scoping nuances, or formatting. Reconstruction is a deliberate authoring task informed by the corpus, not a mechanical copy.
- The extractor (`_extract_corpus.py`) is committed alongside the corpus so the extraction is fully reproducible from the same bytecode.

---

## 6. What this checkpoint does NOT do

- Does not restore or write any `.py` module under `app/` or `scripts/`.
- Does not delete or modify any `__pycache__` bytecode.
- Does not implement PAS210, modify PAS209, or touch/apply the parked stash.
- Does not decide which subsystems to rebuild.
- Does not push.

---

## 7. Recommended next steps (not executed here)

1. **Review & verify** the committed corpus (spot-check high-value modules: `ingestion/email_forwarder_secret_store`, `memory/candidate_pipeline`, `memory/review*`, `security/rate_limit`, `security/api_key_rotation`).
2. **Only then** consider the separate cleanup of stale `__pycache__`.
3. **Record per-subsystem rebuild / retire / ignore decisions**, prioritising the doctrine core — **ingestion** (lead/email) and **memory** (candidate → review → approval → rollout) — plus the **security** hardening that is the real PAS169 launch gate.
4. **Fix the two runtime-breaking lazy imports** in `app/routes/slack_command.py` (`app.services.security.rate_limit`, `app.services.operator.circuit_breaker_policy`).
5. **Then proceed to PAS210 — Live Operational Snapshot Bridge**, which can ship on the call/event data the committed voice engine already produces, with ingestion/memory reconstruction sequenced alongside.

---

*End of PAS209.5 record. Preservation and documentation only.*
