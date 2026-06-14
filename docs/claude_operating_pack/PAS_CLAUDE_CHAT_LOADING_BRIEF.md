# PAS — Claude Chat Loading Brief

> A 1–2 page quick-load for Claude Chat. Read this first, then read the full report
> (`PAS_FULL_OPERATING_REPORT_FOR_CLAUDE_CHAT.md`) before doing any PAS work.
>
> **Snapshot date:** 2026-06-14 · **Repo:** `goodnews2206/pas-engine` ·
> **Branch/HEAD:** `main` @ `62d3d4d` (PR #75, K.3B) · **Tree:** clean / in sync with origin.

---

## What PAS is

PAS is **ORVN Labs' AI first-contact and brokerage operating-intelligence infrastructure** for US
real estate brokerages. It handles first-contact operations — **lead qualification, routing,
booking, logging, and learning** — and accumulates a durable operational-memory layer, the
**PAS Brain**.

**PAS is NOT** a CRM, NOT a chatbot, NOT merely a dashboard. It is infrastructure: the layer a
brokerage runs *on*. It gives brokerages **speed-to-lead**, **continuity** (follow-up that doesn't
depend on human memory), and **memory** (institutional knowledge that survives turnover).

*Naming note:* the repo carries three names — "Performative AI SuperStaff" (README), "operational
intelligence infrastructure" (operating pack), and the current reset **"Proactive Assistant for
Scale"** (`docs/pas300_product_direction_reset.md`). Reconcile; don't pick one blindly.

---

## Current repo state

- **Repo root:** `C:\Users\hp\Downloads\pas-engine\pas-engine` (git repo is nested one level under
  the working dir).
- **Remote:** `https://github.com/goodnews2206/pas-engine.git`.
- **Branch:** `main`, HEAD `62d3d4d` (Merge PR #75 — `pas211k-3b-frontend-runtime-pinning`).
- **Working tree:** clean, in sync with `origin/main`.
- **Backend:** mature, test-covered FastAPI app (`app/`), Supabase data, Railway/Vercel deploy.
- **Frontend (`web/`):** Next.js 15 — **demo-only, no auth, no backend wiring yet.**
- **Open PRs:** UNVERIFIED (`gh` CLI unavailable); git log shows PRs #56–#75 merged.

---

## Current checkpoint

- **Active band: PAS211K.3 — Runtime Alignment.** K.3A (docs) and K.3B (frontend Node/pnpm pinning)
  are **merged**. **K.3C** (optional `.python-version`) and **K.3D** (CI runtime-verification
  workflow) are **pending**.
- **PAS211K.2C (deploy validation) is BLOCKED** by a **Railway subscription/billing** issue
  (infra, not code). K.3 is deploy-independent.
- ⚠️ `PAS_SEQUENCE_AND_STATUS.md` lags `main` (says K.3 "next"; K.3A/B are already merged). Trust
  live git over the status doc.
- **Test baseline (per docs): 1252 passed / 0 failed** — not re-run this session (UNVERIFIED live).

---

## Workflow pattern (no-skip)

**Audit → user approval → implement on a checkpoint branch → targeted then full validation →
final report → commit → push (separately authorized) → PR → PR-verification report → manual merge
(explicit approval only) → post-merge verification → only then next checkpoint.**

- No implementation before audit. No push before validation. No merge before PR verification. No
  next checkpoint before post-merge verification.
- Prefer **small, additive, single-file diffs** over broad rewrites.
- Required reports: audit, implementation, PR-verification, post-merge, plus a blocker report when
  blocked.

---

## Guardrails (hard)

- **Never** touch/expose secrets or `.env` (temp file → SHA-256 fingerprint → cleanup).
- **Never** push or merge without explicit this-session authorization. **Never** force-push,
  `reset --hard`, rewrite history, or delete branches/files.
- **Do not** modify `requirements.txt`, `constraints.txt`, `nixpacks.toml` (pip pinned `26.1.2`).
- **Do not** apply migrations. **Do not** touch **PAS209**. **Do not** delete `__pycache__`.
- **Never** weaken tenant isolation/RLS; **never** trust inbound brokerage/tenant IDs.
- **Never** auto-approve PAS Brain memory candidates (manual review only until a checkpoint
  authorizes automation).
- **Never** touch Railway/Vercel/Supabase settings unless the checkpoint authorizes it.
- **Never** confuse the PAS repo with the ORVN website repo (or `goodnews2206/Orvn-labs`).

---

## Next safe action

Confirm with Daniel, then (recommended) begin **PAS211K.3C** or **PAS211K.3D** with an **audit
report first** — both are deploy-independent and low-risk. Do **not** attempt deploy (K.2C is
Railway-blocked) and do **not** start a broad rewrite.

---

## Instruction

> **Before doing any PAS work:** read the full report
> (`PAS_FULL_OPERATING_REPORT_FOR_CLAUDE_CHAT.md`), then confirm the live repo, branch, `git
> status`, latest commits, and active checkpoint. Do not write code until Daniel provides the
> latest repo status and explicitly authorizes the next checkpoint.
