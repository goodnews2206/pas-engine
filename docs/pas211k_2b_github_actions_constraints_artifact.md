# PAS211K.2B-prep — GitHub Actions Constraints Artifact Workflow

> Prep checkpoint for **PAS211K.2B**. Adds a manual GitHub Actions workflow that
> generates a Python `constraints.txt` **artifact** in a Python 3.11 Linux
> environment for human review. It does **not** commit anything — the artifact
> is downloaded, reviewed, scrubbed, and committed by hand in PAS211K.2B proper.

## Purpose

PAS211K.2A defined the plan and guardrails for a generated `constraints.txt`
(full transitive pin) consumed via `pip install -r requirements.txt -c
constraints.txt`. That plan requires generation in a **Python 3.11 / Linux /
Railway-equivalent** environment. This checkpoint provides that environment as a
manual GitHub Actions job, since the local machine cannot satisfy the
requirement.

## Why GitHub Actions instead of local generation

The local environment **cannot** generate constraints per the plan:

- Local interpreter is **Python 3.14 on Windows** — explicitly forbidden for
  generation (wrong interpreter and wrong platform → wrong pins / broken Railway
  install).
- **No Docker** engine available → cannot run a `python:3.11-slim` container.
- **No WSL** distro installed (only the `wsl.exe` stub) → no local Linux 3.11.
- **No Railway CLI** and Railway itself is currently unavailable (subscription).

GitHub Actions provides a clean, reproducible, fully logged **Ubuntu 24.04 +
Python 3.11** runner with artifact upload — a faithful "Python 3.11 Linux"
environment for resolving the transitive dependency graph.

## Why Vercel is unsuitable

Vercel builds the Next.js frontend from `web/` using pnpm. It is not a
general-purpose Python 3.11 Linux runner: there is no clean controllable venv,
no way to run `pip freeze` / `pip check` / `pytest tests/mvp`, and no
build-artifact mechanism for this purpose. (Vercel is the frontend deploy only;
its preview status has no bearing on constraints generation.)

## Why Railway is preferred but currently unavailable

Railway is the **actual deploy platform** and builds via **nixpacks with
`python311` from Nixpkgs** (see `nixpacks.toml`). Generating on Railway would be
the highest-fidelity option — same image, same Python 3.11 Linux, same
architecture → zero platform drift. Railway is currently **unavailable due to
subscription issues**, so GitHub Actions is the chosen fallback. When Railway is
restored, the produced `constraints.txt` should ideally be cross-checked against
a Railway run.

## What the workflow does

File: `.github/workflows/pas211k-2b-generate-constraints.yml`

- Trigger: **`workflow_dispatch` only** (manual; no push / pull_request trigger).
- Runner: **`ubuntu-24.04`**.
- `actions/checkout@v4`, `actions/setup-python@v5` with `python-version: "3.11"`.
- Creates a **clean virtualenv** (`python3.11 -m venv .venv`).
- Mirrors the nixpacks build by running `pip install --upgrade pip`, then
  `pip install -r requirements.txt`.
- Records **Python version, OS/kernel, pip version, and UTC timestamp** in the
  `constraints.txt` header (and echoes them to the build log).
- Generates `constraints.raw.txt` via `pip freeze` (**production-only set** —
  the freeze happens before any dev/test deps are installed).
- Generates `constraints.txt` = header + raw freeze output.
- Validates: `python -m pip check`, `python -m compileall -q app scripts tests`.
- **Only then** installs dev/test deps (`pip install -r requirements-dev.txt`)
  and runs `pytest tests/mvp -q`.
- Uploads both files as an artifact named **`pas211k-2b-python-constraints`**,
  with **`if: always()`** so the artifact is available even if pytest (or another
  later step) fails.
- Uses a **read-only** `contents: read` token.

### Why `requirements-dev.txt` exists (PAS211K.2B-prep.2)

PAS211K.1 flagged that `pytest` was **undeclared** — it lived only in developer
machines, so a clean Python 3.11 CI venv (which installs `requirements.txt`
only) had no test runner and `pytest tests/mvp -q` failed. `requirements-dev.txt`
declares that **test-only** tooling reproducibly:

- `pytest` is **test-only, not a production/runtime dependency** — it must not
  enter `requirements.txt`, production images, or the deploy model.
- The workflow installs `requirements-dev.txt` **after** the production
  constraints are frozen, so dev/test packages **never leak** into
  `constraints.txt` / `constraints.raw.txt`. The uploaded artifact remains a
  pure production graph.
- The artifact upload uses **`if: always()`** so the generated constraints stay
  **inspectable even when a validation step fails** (the prior run lost the
  artifact because the upload sat after a failing pytest with no `always()`).

PAS211K.2B proper still **reviews/scrubs** the artifact against the review
checklist before any commit — `requirements-dev.txt` does not change that gate.

## What the workflow does NOT do

- Does **not** commit `constraints.txt` (or anything) to the repository.
- Does **not** push, open a PR, or modify `nixpacks.toml` / `requirements.txt`.
- Does **not** run automatically — manual dispatch only.
- Does **not** scrub the freeze output — editable/local/self lines (if any) are
  removed during human review in PAS211K.2B.
- Does **not** add Dependabot or general CI (out of scope for this prep).
- Does **not** pin pip; it mirrors the existing floated-pip install behavior and
  records the resolved pip version so PAS211K.2B can decide to pin it.

## How to run the workflow (manual dispatch)

1. Push this branch and open/merge it so the workflow exists on the default
   branch (a `workflow_dispatch` workflow must be present on the default branch
   to appear in the Actions UI).
2. GitHub → **Actions** tab → select **"PAS211K.2B Generate Python Constraints
   Artifact"** in the left sidebar.
3. Click **"Run workflow"**, choose the branch, and confirm.
4. Wait for the run to complete green (all validation steps must pass).

## How to download the artifact

1. Open the completed run under the **Actions** tab.
2. Scroll to the **Artifacts** section at the bottom of the run summary.
3. Download **`pas211k-2b-python-constraints`** (a zip containing
   `constraints.txt` and `constraints.raw.txt`).

## Review checklist for `constraints.txt`

Before using/committing the artifact in PAS211K.2B, confirm it:

- [ ] includes **direct AND transitive** dependencies,
- [ ] uses **exact pins** (`==`) on every dependency line,
- [ ] contains **no local paths** (no `C:\...`, `/Users/...`, `file://`),
- [ ] contains **no editable installs** (`-e ...`),
- [ ] contains **no project self-reference** (no `pas`/local package line),
- [ ] contains **no OS-/interpreter-specific accidental artifacts** (nothing
      Windows-only or 3.14-only that won't exist on 3.11/Linux),
- [ ] contains **no secrets** (no index URLs with embedded tokens/credentials),
- [ ] header records **Python 3.11 / Linux**, pip version, and date,
- [ ] was **reviewed by eye** (it is generated, but a human confirms the above).

## Next step after artifact download

**PAS211K.2B proper:**

1. Download and **review/scrub** the artifact per the checklist above.
2. **Commit `constraints.txt`** to the repo (source of truth stays
   `requirements.txt`).
3. **Update `nixpacks.toml`** install command from
   `pip install -r requirements.txt` to
   `pip install -r requirements.txt -c constraints.txt`, and **deliberately pin
   pip** (or drop `--upgrade`) per the recorded version.
4. **Validate**: `pip check`, `compileall`, `pytest tests/mvp` (→ 1252 / 0), plus
   the optional second clean-venv reproducibility check.

## Limitations

GitHub Actions provides **CPython 3.11 on Linux (x86_64, glibc)** — the
variables that drive transitive resolution (interpreter major.minor, OS, libc,
architecture, manylinux wheel selection) match Railway. However, Railway builds
with **`python311` from Nixpkgs**, which can differ from the actions/python build
at the **patch level**, and the base image differs. The result is therefore a
faithful but **not byte-identical** Railway/Nixpacks equivalent. The header
stamp (interpreter + OS + pip + date) makes any divergence auditable; cross-check
against Railway when it becomes available.

## No auto-commit guarantee

This workflow only **uploads an artifact**. It has a read-only token
(`contents: read`), contains no `git commit`/`git push`/PR step, and runs only on
manual dispatch. No change reaches the repository without a deliberate human
commit in PAS211K.2B.
