# PAS — Engineering Rules

These rules are **non-negotiable**. They override convenience, speed, and any default agent behavior. When a rule conflicts with a request, surface the conflict — do not silently break the rule.

## The core rules

1. **Audit before implementation.**
   Read the relevant code, tests, and context before changing anything. Understand the current checkpoint and baseline first. No blind edits.

2. **Preserve the sequence.**
   PAS is built as ordered checkpoints (PAS211D → … → PAS211K.2B done; K.2C blocked; K.3 next). Do not skip, reorder, or invent checkpoints. Build forward from the current point.

3. **Never push without authorization.**
   No `git push` under any circumstance unless explicitly authorized *this session*. Pushing is a separate, explicitly-approved step — never bundled into "make the change."

4. **Never merge without authorization.**
   No merges, no fast-forwards, no PR merges without an explicit go.

5. **Post-merge verify.**
   After any merge or significant change, verify: run the appropriate tests, confirm the baseline (1252 passed / 0 failed) still holds, and report results plainly.

6. **No destructive operations without explicit approval.**
   No force-push, no history rewrite, no `reset --hard`, no deleting branches/files/tables, no dropping data, no migrations. If a task seems to require one, stop and ask.

## Change discipline (how to make an engineering change)

- **Additive, single-file diffs** where possible. Prefer the smallest change that works. Avoid sprawling multi-file rewrites.
- **Run the full simulation matrix before committing.** Confirm the green baseline holds.
- **Commit and push are separate steps.** Commit only when asked or clearly authorized; push is its own explicitly-authorized action.
- **Branch first** if work would otherwise land on a protected branch. Never push to `main` without authorization — the harness blocks this and so do these rules.

## Standing "do not touch" list

- Do **not** modify `requirements.txt`.
- Do **not** modify `constraints.txt`.
- Do **not** modify `nixpacks.toml`.
- Do **not** apply migrations.
- Do **not** touch **PAS209**.
- Do **not** delete `__pycache__`.
- Do **not** push.
- Do **not** merge.

## Dependency invariants (do not break)

- `constraints.txt` is committed and authoritative.
- `pip` is pinned to **26.1.2**.
- `nixpacks` builds against `constraints.txt`.
- Reproducible builds depend on all three. Leave them alone unless explicitly told to change them, and even then, change exactly what's asked and nothing more.

## Secrets handling

- **Never echo secrets** into logs, terminal output, or files.
- Pattern: write the secret to a **temp file**, compute a **SHA-256 fingerprint** to confirm identity, use it, then **clean up** the temp file.
- Reference a credential by its fingerprint, never its value.

## Scope discipline

- If the task is docs-only, change only docs. **Do not run the full test suite for docs-only work** — there is nothing to verify in code.
- Always report whether anything outside the requested scope changed. If nothing did, say so explicitly.

## When in doubt

Stop and ask. A blocked task that preserves the baseline and the sequence is always better than an unblocked task that quietly violated a rule.
