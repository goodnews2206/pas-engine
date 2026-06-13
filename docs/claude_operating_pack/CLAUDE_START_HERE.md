# CLAUDE — START HERE

This is the **ORVN/PAS Claude Operating Pack**. It is a portable context bundle. Upload the whole `claude_operating_pack/` folder into a Claude Max project so Claude understands ORVN Labs, the PAS product, the engineering sequence, product strategy, content strategy, ICP, tone, and working rules — without me re-explaining each session.

---

## What this pack is

A self-contained briefing. Read it in order, then operate from it. Nothing here is app code; it is *context and instructions*.

## Read order

1. **CLAUDE_START_HERE.md** ← you are here. Orientation + working rules.
2. **PAS_MASTER_CONTEXT.md** — ORVN Labs, what PAS is, what it is *not*.
3. **PAS_SEQUENCE_AND_STATUS.md** — engineering checkpoints, current status, baseline.
4. **PAS_ENGINEERING_RULES.md** — non-negotiable rules for any engineering work.
5. **PAS_PRODUCT_ARCHITECTURE.md** — backend/frontend/data layout, web-first/PWA stance.
6. **PAS_MEMORY_ARCHITECTURE.md** — the four-tier memory hierarchy and PAS Brain.
7. **ORVN_CONTENT_STRATEGY.md** — ICP, core topics, narrative spine.
8. **DANIEL_VOICE_AND_TONE.md** — how Daniel writes and speaks.
9. **ICP_AND_MARKET_CONTEXT.md** — who we sell to and the market reality.
10. **CLAUDE_CONTENT_WORKFLOW.md** — the repeatable research→content pipeline.
11. **CLAUDE_RESEARCH_AND_CONTENT_PROMPTS.md** — copy-paste master prompts.

## How to use it

- **Engineering session?** Start with rules (4), status (3), architecture (5), memory (6). Audit before you touch anything.
- **Content session?** Start with strategy (7), voice (8), ICP (9), workflow (10), prompts (11).
- **Cold start in Claude Max?** Paste the master prompt from file 11 § "Master Boot Prompt."

---

## Working rules (apply to every session)

These mirror the engineering discipline in file 4 but apply to *all* work:

1. **Audit before acting.** Read the relevant context files and existing state before proposing changes.
2. **Preserve the sequence.** PAS checkpoints are ordered (PAS211D → PAS211K.3 …). Do not skip, reorder, or invent steps.
3. **Never push without authorization.** No `git push`. Ever, unless explicitly told this session.
4. **Never merge without authorization.** No merges without an explicit go.
5. **No destructive operations without explicit approval.** No deletes, force-pushes, history rewrites, dropped tables, or migrations on a whim.
6. **Stay inside scope.** If asked for docs, change only docs. Name anything you touched outside the requested scope.
7. **Verify after change.** State what passed, what failed, and what was skipped — plainly, with output.
8. **Don't echo secrets.** Use the temp-file + SHA-256 fingerprint + cleanup pattern. Never print credentials.
9. **Tone matters.** Founder/operator voice — calm, analytical, direct. No hype, no startup-bro.

## Hard "do not touch" list (standing)

- Do **not** modify `requirements.txt`, `constraints.txt`, or `nixpacks.toml` without explicit instruction.
- Do **not** apply migrations.
- Do **not** touch **PAS209**.
- Do **not** delete `__pycache__`.
- Do **not** push. Do **not** merge.

---

## One-line identity

**ORVN Labs builds PAS — operational intelligence infrastructure for US real estate brokerages. Web-first, becoming a PWA. Not a CRM, not a chatbot, not a social app.**
