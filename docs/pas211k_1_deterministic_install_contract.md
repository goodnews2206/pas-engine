# PAS211K.1 — Deterministic Install Contract

> Docs-only checkpoint. This file defines the contract; the enforcing changes
> land in PAS211K.2 (Python lock/constraints), PAS211K.3 (Node frozen install +
> runtime pinning) and PAS211K.4 (CI + Dependabot). Items not yet enforced are
> marked **(future)**.

## Executive Summary

PAS must install **the same intended dependency versions** everywhere it runs:

- developer machines
- CI runners
- Railway (backend) / Vercel (frontend) and any other deploy system
- future regional deployments
- future contractor / new-hire machines

A paying-client production system cannot depend on ad-hoc installs or drifting
package versions. The product principle is therefore:

> **No ad-hoc installs. No silent version drift. No blind force-upgrades.**

Every install — local, CI, or deploy — must resolve to the versions the team
intended and validated, not to "whatever the registry served today." Version
changes are deliberate, reviewed, and tested — never a side effect of running an
install command.

## Current Dependency Reality

Snapshot at `main` = `54e561e9393f362521a8d3a29aa696b805ae6645` (PAS211K audit):

- **Python direct dependencies are exact-pinned** in `requirements.txt` (every
  line uses `==`).
- **Python transitive dependencies are NOT locked yet** — sub-dependencies (e.g.
  starlette under fastapi, anyio, certifi, and the supabase sub-stack
  gotrue/postgrest/realtime/storage3) resolve fresh at install time, so two
  machines or two dates can get different transitive versions.
- **Frontend uses pnpm** with a committed `web/pnpm-lock.yaml`
  (`lockfileVersion 9.0`) that pins exact transitive versions.
- **`npm` is the wrong mental model for this repo** — there is no
  `package-lock.json` and no `yarn.lock`. Reasoning about this app as an
  "npm project" (e.g. `npm ci`, `npm install`) is incorrect; it is a pnpm
  project.
- **No `.github` CI / Dependabot exists yet** — there is no automated locked
  install, no dependency review, and no vulnerability alerting.
- **Python deploy runtime is 3.11** (`nixpacks.toml` installs `python311`) while
  the **locally observed runtime was 3.14** — a real dev/prod drift.
- **Node runtime is not pinned** — no `engines`, no `packageManager`, no
  `.nvmrc`; the deploy platform picks a default.
- **No direct Postgres / ORM dependency found** — PAS uses the **Supabase client
  pattern** (`create_client`, PostgREST/HTTP). The Supavisor / direct-connection
  connection-pool issue is therefore **not current**, but this conclusion **must
  be revisited if a direct DB driver** (psycopg, asyncpg, SQLAlchemy, etc.) is
  ever added.

## Deterministic Install Rules

1. **Backend installs must use locked constraints** once PAS211K.2 lands (today:
   `requirements.txt` only — direct-pinned but transitively unlocked).
2. **Frontend installs must use `pnpm install --frozen-lockfile`** once
   PAS211K.3 documents/enforces it — so a stray range can never silently update
   the lock.
3. **Developers must not run `npm install` in `web/`** — it is the wrong package
   manager and can desync or rewrite the dependency graph.
4. **Developers must not run `npm audit fix --force`** (or `pnpm` force
   equivalents) — force-upgrades cross semver and bypass review/tests.
5. **Dependency upgrades must be explicit PRs with tests** — never an incidental
   result of an install command.
6. **Production deploy must not infer dependency versions differently from
   local/CI** — the same lock/constraints drive all three.
7. **No package install command may modify lockfiles during deploy** — deploy
   installs are read-only against the committed lock; a deploy that would change
   the lock must fail, not "fix" it.

## Fresh Machine Setup Target

The intended end-state flow (mark **(future)** parts honestly):

1. `git clone` the repo.
2. Use the **pinned Python runtime** — Python **3.11** to match deploy. **(future:
   `.python-version` / `runtime.txt`, PAS211K.3)**
3. Create a virtualenv: `python3.11 -m venv venv` and activate it.
4. **Install backend from deterministic lock/constraints.**
   - today: `pip install -r requirements.txt`
   - **(future, PAS211K.2):** `pip install -r requirements.txt -c constraints.txt`
     (or `--require-hashes` against a generated lock).
5. **Install frontend with a frozen lockfile:** in `web/`,
   `pnpm install --frozen-lockfile`. **(documented now; enforced in CI at PAS211K.4)**
6. `python -m compileall -q app scripts tests`.
7. `pytest tests/mvp` (current clean baseline: **1252 passed / 0 failed**).
8. **(if practical)** in `web/`: `pnpm run type-check` and/or `pnpm run build`.

Until PAS211K.2/.3/.4 land, steps 2 and 4 are partially manual; the contract
above is the target every later checkpoint converges on.

## Backend Install Contract

- **Current command:** `pip install -r requirements.txt` (from `nixpacks.toml`
  and local setup).
- **Future command (PAS211K.2):** `pip install -r requirements.txt -c constraints.txt`
  — or install from a generated, hash-pinned lock (`pip install --require-hashes
  -r requirements.lock`).
- **Why `requirements.txt` alone is insufficient for transitives:** it pins only
  the **direct** packages. pip then resolves their dependencies to the newest
  compatible versions available at install time, so the *full* installed set is
  not reproducible across machines or dates even though the top-level pins match.
- **How constraints/lockfile will solve it:** a constraints/lock file enumerates
  **every** package (direct + transitive) at an exact version (ideally with
  hashes), so pip can only install that exact graph. The same lock drives local,
  CI, and deploy installs → identical environments.
- **Dev/test dependency separation (later):** test-only tooling (e.g. `pytest`,
  currently undeclared) belongs in a separate `requirements-dev.txt` (or a dev
  extra) so production images don't carry test deps and the test environment is
  itself reproducible.

## Frontend Install Contract

- **Current `pnpm-lock.yaml` status:** committed at `web/pnpm-lock.yaml`
  (`lockfileVersion 9.0`), pinning exact transitive versions. `package.json`
  uses caret ranges, but the lock is authoritative.
- **Required command:** `pnpm install --frozen-lockfile` — installs exactly the
  locked graph and **fails** (rather than rewriting the lock) if `package.json`
  and the lock disagree.
- **`packageManager` and `engines` should be added later (PAS211K.3)** — e.g.
  `"packageManager": "pnpm@<version>"` and `"engines": { "node": "<range>" }` in
  `web/package.json`, so the toolchain itself is pinned.
- **`npm install` should not be used for this app** — it ignores the pnpm lock,
  may create a competing `package-lock.json`, and breaks determinism.

## Runtime Version Contract

- **Python** should be pinned/aligned to **3.11** (matching `nixpacks`) unless a
  version change is made deliberately. The locally observed 3.14 is drift to
  close.
- **Node** should be **pinned** (via `engines` + `packageManager`, optionally
  `.nvmrc`) so local, CI, and deploy use the same major/minor.
- **Local dev, CI, and deployment must agree** on both runtimes — a version that
  only matches in one place is a latent production difference.
- **Runtime version changes require an explicit PR + full validation**
  (compileall + `pytest tests/mvp`, and frontend type-check/build), never an
  implicit platform default bump.

## CI / Dependabot Future (PAS211K.4)

PAS211K.4 should add, under `.github/`:

- A **GitHub Actions workflow** that, on PRs to `main`:
  - performs a **locked backend install** (constraints/`--require-hashes`),
  - runs **`pnpm install --frozen-lockfile`** for the frontend,
  - runs `python -m compileall -q app scripts tests`,
  - runs `pytest tests/mvp`,
  - runs the frontend **type-check / build** if practical,
  - (network is available in CI) runs `pnpm audit`.
- **Dependabot** (`.github/dependabot.yml`) for both the **pip** and
  **pnpm/npm** ecosystems.
- A defined **dependency review cadence** (see runbook preview below).

The point of CI here is to **test locked installs** — to prove that a clean,
frozen install still passes the suite, catching lock drift before it reaches a
client.

## Monthly Dependency Review Runbook Preview (PAS211K.5)

Intended monthly cadence (formalized in PAS211K.5):

1. Review **Dependabot alerts / PRs**.
2. Run **audit commands** (`pnpm audit`; `pip` advisory check / locked-install
   verification).
3. **Update lockfiles intentionally** — regenerate the lock/constraints for the
   chosen bumps; never hand-edit.
4. Run the **full backend tests** (`pytest tests/mvp`).
5. Run the **frontend build / type-check**.
6. **Document the risk / change** (what moved, why, blast radius).
7. **Merge small dependency PRs separately** so each bump is bisectable and
   independently revertable.

## Anti-Patterns

- **No `npm audit fix --force`** (or pnpm force equivalents) — crosses semver,
  skips review/tests.
- **No casual `pip install --upgrade`** — mutates the environment outside the
  lock/constraints.
- **No editing lockfiles by hand** — locks are generated artifacts; hand edits
  desync them from reality.
- **No deleting lockfiles** — deleting `pnpm-lock.yaml` (or a future Python lock)
  destroys reproducibility.
- **No ignoring lockfile drift** — a deploy/CI install that wants to change the
  lock is a failure signal, not a convenience to wave through.
- **No different Node/Python versions across environments** — dev, CI, and
  deploy must agree.
- **No direct Postgres driver added without a connection-pooling review** — the
  current "no pool risk" conclusion holds only while PAS stays on the Supabase
  client pattern.

## Next Checkpoints

- **PAS211K.2** — Python lock / constraints strategy.
- **PAS211K.3** — Node runtime / package-manager / frozen-install enforcement
  (incl. `.python-version`/`runtime.txt`, `engines`, `packageManager`).
- **PAS211K.4** — Dependabot + CI dependency review.
- **PAS211K.5** — monthly dependency review runbook.
- **PAS214P** — performance / region / timezone / connection readiness (revisit
  connection pooling here if a direct DB driver is introduced).
