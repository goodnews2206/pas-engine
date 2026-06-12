# PAS211K.2 — Python Constraints Generation Plan + Guardrails

> Planning / guardrail checkpoint (docs-only). It defines **how** `constraints.txt`
> must be generated, validated, and enforced — so the actual file is never
> produced from the wrong environment. Generation + the install-command change
> happen in **PAS211K.2B**, not here.
>
> **Status — PAS211K.2B completed:** `constraints.txt` (generated on Python
> 3.11.15 / Linux, pip 26.1.2) is committed at the repo root, and `nixpacks.toml`
> now installs with `pip install -r requirements.txt -c constraints.txt` after
> pinning `pip==26.1.2`. `requirements.txt` is unchanged.

## Executive Summary

PAS211K.2 selected a generated **`constraints.txt`** (full transitive pin) used
alongside the existing, unchanged `requirements.txt`:

```
pip install -r requirements.txt -c constraints.txt
```

This closes the transitive-drift gap (today `requirements.txt` pins only the 12
direct packages; their sub-dependencies resolve fresh at install time) while
keeping `requirements.txt` as the human-auditable source of intent and changing
the Railway build by a single flag.

**But the constraints file must NOT be generated from the current local
environment.** The observed local interpreter is **Python 3.14 on Windows**,
while Railway/Nixpacks deploys on **Python 3.11 on Linux**. A `pip freeze`
captured on 3.14/Windows would pin:

- versions chosen by the 3.14 resolver (not 3.11),
- packages selected by **platform markers** for Windows (not Linux),
- potentially different wheels/build backends.

Installing such a file on Railway could pin wrong versions or **break the deploy
outright**. Determinism is only valuable if it reproduces the *deploy* graph — so
the constraints must be generated in an environment that matches deployment.

## Required Generation Environment

`constraints.txt` MUST be generated in an environment that is:

- **Python 3.11** (matching `nixpacks.toml` `python311`) — not 3.12/3.13/3.14.
- **Linux** (or a Railway-equivalent / Railway build itself) — not Windows/macOS.
- A **clean virtualenv** created fresh for the purpose.
- Free of **preinstalled / globally-leaked packages** that could contaminate the
  frozen output (no `--system`, no reusing an existing venv).
- The **same architecture family** as deployment where practical (x86_64 Linux).

Acceptable concrete options (any one):
1. The Railway build environment itself (generate during a build step and capture
   the output).
2. A Linux x86_64 host / VM / container running Python 3.11.
3. A Python 3.11 `docker run` on a Linux image (e.g. `python:3.11-slim`).

The current Windows / Python 3.14 machine is **explicitly disqualified** as a
generation source.

## Generation Commands (intended — DO NOT run locally unless the env matches)

Run these **only** inside the Required Generation Environment above:

```bash
# 1. Fresh, clean virtualenv on Python 3.11
python3.11 -m venv /tmp/pas-constraints-venv
. /tmp/pas-constraints-venv/bin/activate

# 2. Deliberate pip handling (pin, don't blindly float — see Nixpacks plan)
python -m pip install "pip==<chosen-version>"     # or a deliberate, recorded upgrade

# 3. Install EXACTLY the current direct deps
pip install -r requirements.txt

# 4. Capture the fully-resolved graph (direct + transitive)
pip freeze > constraints.raw.txt
#   (pip freeze --all only if pip/setuptools/wheel must also be pinned —
#    decide deliberately; default plain `pip freeze`)

# 5. Scrub: drop editable installs, local paths, and the project itself
#    - remove any line starting with "-e " or containing a local file path
#    - remove any "pas"/project self-reference if present
#    - keep a header comment noting interpreter, OS, date, and "generated, do not hand-edit"
#    -> write the cleaned result to constraints.txt

# 6. Inspect the file by eye (see Review Rules)

# 7. Sanity-check the env
python -m pip check

# 8. Reproducibility: SECOND clean venv installs via the constraint
python3.11 -m venv /tmp/pas-verify-venv
. /tmp/pas-verify-venv/bin/activate
pip install -r requirements.txt -c constraints.txt
python -m pip check
```

These are documented intent. **They are not executed in this checkpoint** and
must not be run on the local Windows/3.14 interpreter.

## Validation Commands

After `constraints.txt` is generated (PAS211K.2B), validate in the 3.11
environment:

- `python -m pip check` — no broken/conflicting requirements.
- `python -m compileall -q app scripts tests` — bytecode compiles.
- `pytest tests/mvp -q` — expect the clean baseline **1252 passed / 0 failed**.
- **Optional second clean venv reproducibility check** — install
  `-r requirements.txt -c constraints.txt` in a fresh 3.11 venv on a different
  machine/date and confirm an identical environment.
- **Compare `pip freeze` output with `constraints.txt`** — the installed set must
  match the constraints exactly (no unconstrained transitive slipping in).

## Review Rules

Before commit, `constraints.txt` must:

- include **direct AND transitive** dependencies,
- use **exact pins** (`==`) on every line,
- contain **no local paths** (no `C:\...`, no `/Users/...`, no `file://`),
- contain **no editable installs** (`-e ...`),
- contain **no OS-specific accidental artifacts** (no Windows-only/3.14-only
  pins that won't exist on 3.11/Linux),
- contain **no secrets** (no index URLs with embedded tokens, no credentials),
- be **generated from Python 3.11 / Linux**,
- be **reviewed by eye** before commit (it is a generated artifact, but a human
  confirms the above).

## Nixpacks / Railway Change Plan (PAS211K.2B)

After constraints are generated and validated, change `nixpacks.toml` install
from:

```toml
"/opt/venv/bin/pip install -r requirements.txt"
```

to:

```toml
"/opt/venv/bin/pip install -r requirements.txt -c constraints.txt"
```

`requirements.txt` stays the source of truth; the build model is otherwise
unchanged.

**Pip handling decision:** the current build runs
`pip install --upgrade pip`, which floats the installer to whatever is latest at
build time — a small but real source of non-determinism. PAS211K.2B should
**pin pip deliberately** (e.g. `pip install "pip==<version>"`) or drop the
`--upgrade` so the installer version is also reproducible. Record the chosen pip
version alongside the constraints.

## Failure Modes

- **Constraints generated on the wrong interpreter/platform** — 3.14/Windows pins
  applied to 3.11/Linux → wrong versions or a broken Railway install. *(The whole
  reason for this guardrail.)*
- **Constraints out of sync with `requirements.txt`** — a direct dep is changed
  without regenerating constraints; `-c` then either conflicts or silently keeps
  the stale pin. *(Mitigate: regenerate on every `requirements.txt` change; CI
  check in K.4.)*
- **pip resolver conflict** — constraints pin a transitive version incompatible
  with a (later) direct change → install fails. *(Mitigate: regenerate + validate
  in 3.11 before merge.)*
- **Railway install fails** — markers/wheels not available for the deploy
  platform. *(Mitigate: generate on the deploy platform.)*
- **Hidden transitive CVE stays pinned until review** — pinning freezes a
  vulnerable transitive until a deliberate bump. *(Mitigate: Dependabot + monthly
  review, K.4/K.5.)*
- **Local dev on a different Python** — 3.14 locally vs 3.11 pinned constraints
  can still diverge for local installs. *(Mitigate: runtime alignment in
  PAS211K.3.)*

## Do / Do Not

**Do not:**
- generate constraints from **Python 3.14 / Windows**,
- **hand-edit** constraints except the header/comment block,
- **upgrade direct deps** during constraints generation (pin the *current* set),
- **add hashes** yet (`--require-hashes` is a later, optional hardening),
- **replace** `requirements.txt` (it stays the source of truth),
- introduce **pip-tools / uv / Poetry** in this phase.

**Do:**
- generate in a clean **Python 3.11 / Linux** venv,
- capture interpreter + OS + date + pip version in the file header,
- review against the Review Rules before commit,
- validate with `pip check` + `compileall` + `pytest tests/mvp`.

## Next Implementation Step

**PAS211K.2B** — Generate `constraints.txt` in a Python 3.11 Linux /
Railway-equivalent environment per this plan, scrub + review it, update
`nixpacks.toml` to `pip install -r requirements.txt -c constraints.txt` (and pin
pip), then validate (`pip check`, `compileall`, `pytest tests/mvp` → 1252/0)
before commit.
