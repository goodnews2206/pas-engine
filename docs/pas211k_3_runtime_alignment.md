# PAS211K.3 Runtime Alignment

> Status: **active checkpoint (PAS211K.3)** — this document (PAS211K.3A) records the
> source-of-truth decisions from the read-only K.3 runtime alignment audit. It is
> **documentation only**: no runtime, dependency, config, workflow, or app code is
> changed by this checkpoint.

---

## A. Title

**PAS211K.3 Runtime Alignment**

## B. Current checkpoint state

- **PAS211K.2B — completed.** Python transitive dependencies pinned; `constraints.txt`
  committed; pip pinned to `26.1.2`; nixpacks uses the constraints install path.
- **PAS211K.2C — blocked** by a Railway subscription/billing issue. This is an
  infrastructure/account blocker, not a code blocker. Deploy validation is parked here.
- **PAS211K.3 — active.** Runtime alignment. The K.3 audit was completed read-only.
- **Latest verified test baseline:** **1252 passed / 0 failed.**

## C. Runtime alignment purpose

PAS211K.3 aligns runtime assumptions across every surface that runs or builds PAS so
they agree on the same versions and the same source of truth:

- **Backend deploy** (Railway via Nixpacks)
- **Local development** (backend Python; frontend Node/pnpm)
- **CI** (GitHub Actions constraint generation, future runtime verification)
- **Frontend** (`web/`, Next.js)
- **Vercel** (frontend hosting runtime)
- **Future workflows** (CI runtime verification in K.3D)

The goal is to remove silent drift — places where the runtime version is implicit,
duplicated, or assumed — by naming a single authoritative source for each surface and
documenting the known, accepted divergences.

## D. Backend Python source of truth

- The **deployment Python source of truth is `nixpacks.toml`.**
- `nixpacks.toml` uses **nixpkgs `python311`**.
- PAS should **remain Python 3.11 aligned** across deploy, local, and CI.
- **`runtime.txt` should NOT be added.** Nixpacks does not consume `runtime.txt`; it is a
  Heroku/buildpack-style mechanism. Adding it here would create a **phantom source of
  truth** that looks authoritative but is never read by this Nixpacks setup.
- **`.python-version` may be added later** (PAS211K.3C) **only as a local-dev
  convenience**, clearly marked as non-authoritative. It does **not** carry deploy
  authority — `nixpacks.toml` remains the deploy source of truth.

## E. pip and dependency source of truth

- Production **pip is pinned to `26.1.2`** in `nixpacks.toml`.
- Production install uses:

  ```
  pip install -r requirements.txt -c constraints.txt
  ```

- **`requirements.txt`** remains the **direct dependency source** (human-maintained SoT).
- **`constraints.txt`** remains the **frozen production dependency graph** (generated
  artifact; `DO NOT HAND-EDIT`).
- **K.3 must NOT regenerate or edit `constraints.txt`** and must not edit
  `requirements.txt`. These are out of scope for the entire K.3 sequence.

## F. CI Python alignment

- The GitHub Actions constraints workflow
  (`.github/workflows/pas211k-2b-generate-constraints.yml`) uses **Python 3.11 on
  `ubuntu-24.04`**.
- The CI environment is **close to, but not byte-identical with** the Railway/Nixpacks
  environment (nixpkgs `python311`). This is explicitly recorded in the generated
  `constraints.txt` header.
- This divergence is **acceptable for constraints generation**. It is **not** a substitute
  for deployment proof. **Deployment proof remains PAS211K.2C** and resumes only when
  Railway is restored.

## G. Start command source of truth

Current start command (identical across all three definitions):

```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Precedence (most → least authoritative):**

1. **`railway.toml` `[deploy].startCommand`** — the likely **platform-level authority**.
   Railway applies this as the deploy start command.
2. **`nixpacks.toml` `[start]`** — the **Nixpacks fallback / image start definition**.
3. **`Procfile`** — retained for compatibility but **likely inert** when both
   `railway.toml` and `nixpacks.toml` define start behavior (Nixpacks only auto-uses a
   Procfile when no `[start]` is defined).

State and rules:

- All three are **currently identical**.
- **Do NOT delete or consolidate them in PAS211K.3A.**
- Future cleanup may **retire the `Procfile` only after deploy behavior is proven**
  (i.e., not before Railway is restored and PAS211K.2C confirms the effective start path).

## H. Frontend runtime gap

The frontend (`web/`) has **no pinned runtime version**. Findings:

- Node version is currently **implicit** (relies on local/Vercel defaults).
- **No root `.nvmrc`.**
- **No `web/.nvmrc`.**
- **`web/package.json` has no `engines.node`.**
- **`web/package.json` has no `packageManager`.**
- The **pnpm version is implied** by `web/pnpm-lock.yaml` (`lockfileVersion '9.0'`) and by
  `web/.npmrc` / `web/pnpm-workspace.yaml` comments referencing pnpm 11 approval config —
  but it is **not pinned anywhere**.

This is the **highest K.3 implementation drift risk**: local dev, CI, and Vercel can each
silently resolve a different Node and/or pnpm version.

## I. Frontend runtime recommendation

- **Do NOT add a root `.nvmrc`** — the frontend lives in `web/`; pin there, not at the
  Python repo root.
- **Add `web/.nvmrc`** in PAS211K.3B to pin Node for local + Vercel.
- **Add `engines.node`** to `web/package.json` in PAS211K.3B to declare the supported Node
  range.
- **Add `packageManager`** (with a pinned pnpm version, Corepack-style) to
  `web/package.json` in PAS211K.3B.
- **Discourage npm usage** after pnpm is pinned (enforce pnpm via `engines` +
  `packageManager`).
- **Do NOT edit `web/pnpm-lock.yaml`** unless the package-manager tooling itself requires
  it **and** the resulting diff is reviewed.

## J. K.3 implementation sequence

- **PAS211K.3A — Runtime alignment documentation** (this document; docs-only).
- **PAS211K.3B — Frontend Node/pnpm runtime pinning**
  (`web/.nvmrc`, `engines.node`, `packageManager`).
- **PAS211K.3C — Optional local Python version declaration**
  (`.python-version` as local-dev convenience only; non-authoritative).
- **PAS211K.3D — CI runtime verification workflow**
  (additive workflow asserting Python/Node/pnpm align with declared sources of truth).

## K. Railway / deploy status

- **PAS211K.3 must NOT attempt deploy validation.**
- Deploy validation remains **parked in PAS211K.2C** until the Railway
  subscription/billing issue is resolved and Railway is restored.
- None of K.3A–K.3D require Railway availability; all are deploy-independent.

## L. Explicit non-goals

PAS211K.3 (and this PAS211K.3A document specifically) does **not**:

- deploy;
- upgrade dependencies;
- regenerate `constraints.txt`;
- edit `requirements.txt` (or `requirements-dev.txt`);
- clean up or consolidate the start command (`railway.toml` / `nixpacks.toml` / `Procfile`);
- change app code;
- apply migrations.
