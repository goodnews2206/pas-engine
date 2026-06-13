# PAS — Engineering Sequence and Status

PAS is built as an **ordered sequence of checkpoints**. The sequence is the spine of the engineering effort. Checkpoints are not interchangeable, and they are not optional steps you can reorder. Always know which checkpoint is "done," which is "current," and which is "next."

> **Rule of thumb:** if you don't know the current checkpoint, you are not ready to make engineering changes. Confirm status first.

## Completed sequence

**PAS211D through PAS211K.2B are complete.**

This spans the PAS211D … PAS211K.2B band of checkpoints. Treat everything in that range as shipped and stable unless a later note says otherwise. Do not "redo" completed checkpoints; build forward.

## Current status

- **PAS211K.2C — BLOCKED.** Blocked by a **Railway subscription issue**. This is an infrastructure/billing blocker, not a code blocker. It must be resolved at the Railway account level before PAS211K.2C can proceed. Do not attempt to work around it by altering deployment configuration in ways that violate the standing rules.
- **PAS211K.3 — NEXT ACTIONABLE CHECKPOINT.** Because PAS211K.2C is blocked externally, **PAS211K.3 is the next checkpoint that can actually be worked**. When asked "what's next," the answer is PAS211K.3 — while noting that 2C remains open and blocked.

## Test baseline

**Baseline: 1252 passed / 0 failed.**

- This is the known-good green baseline. Any change that drops below 1252 passing or introduces a failure is a regression and must be explained.
- For docs-only changes, **do not run the full suite** — there is nothing to verify in code.
- For engineering changes, run the **full simulation matrix** before committing, and confirm the baseline still holds (see `PAS_ENGINEERING_RULES.md`).

## How to report status

When summarizing engineering state, always give:

1. Last completed checkpoint (currently **PAS211K.2B**).
2. Current checkpoint + state (currently **PAS211K.2C — blocked, Railway subscription**).
3. Next actionable checkpoint (currently **PAS211K.3**).
4. Test baseline and whether it still holds (**1252 / 0**).
5. Any blockers and whether they are code or infrastructure.

## Dependency / build status (read before any deploy reasoning)

- `constraints.txt` is **committed**.
- `pip` is **pinned to 26.1.2**.
- `nixpacks` uses the **constraints** file during build.
- These three facts are load-bearing for reproducible builds. **Do not modify** `requirements.txt`, `constraints.txt`, or `nixpacks.toml` without explicit instruction. Do not "upgrade pip" or "unpin" anything casually.

## Standing do-not-touch for this product

- Do not touch **PAS209**.
- Do not apply migrations.
- Do not delete `__pycache__`.
- Do not push. Do not merge. (See `PAS_ENGINEERING_RULES.md` for the full list.)

## Snapshot date

This status reflects the project memory snapshot as of the latest update. Checkpoints advance; **re-confirm the current checkpoint at the start of each engineering session** rather than trusting this file blindly.
