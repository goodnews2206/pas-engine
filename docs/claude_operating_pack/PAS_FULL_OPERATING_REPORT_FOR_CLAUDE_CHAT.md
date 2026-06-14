# PAS Full Operating Report for Claude Chat Handoff

> Generated as a **documentation/report-generation task only**. No code, logic, migrations,
> secrets, dependencies, or deployment configuration were changed to produce this report.
>
> **Report generated:** 2026-06-14
> **Repo path used during generation:** `C:\Users\hp\Downloads\pas-engine\pas-engine`
> **Repo:** `goodnews2206/pas-engine` (verified via `git remote -v`)
> **Branch / HEAD at generation:** `main` @ `62d3d4d` (Merge PR #75 — `pas211k-3b-frontend-runtime-pinning`)
> **Working tree at generation:** clean (`## main...origin/main`, in sync)

---

## 0. How to Use This Report

This report is a **portable operating context** for PAS (the ORVN Labs product). It is meant
to be uploaded or pasted into **Claude Chat** (or any Claude session) so that a future Claude
can continue PAS development with full strategic, architectural, and engineering context —
without Daniel having to re-explain the project each time.

It is a **companion** to the existing `docs/claude_operating_pack/` bundle in the repo (the
"Claude Operating Pack"). Where that pack is split across many short files, this report is a
single consolidated handoff that also grounds itself directly in the current repository state,
git history, tests, and code.

**Instruction to future Claude:**

> **Before doing any PAS work, read this report fully, then confirm current repo, branch, git
> status, latest commits, and active checkpoint before acting.** Do not implement anything from
> memory alone. The repo state in this report is a *snapshot*; re-verify it live at the start of
> every session, because checkpoints advance and branches move.

When in doubt, the precedence order for "what is true" is:

1. **Live repo state** (current `git status`, `git log`, file contents) — always wins.
2. **In-repo docs** (`docs/`, especially `docs/claude_operating_pack/` and the per-checkpoint
   `docs/pas*.md` files).
3. **This report** (a synthesized snapshot — accurate as of 2026-06-14, but can age).
4. **Memory / recollection** — never authoritative; always verify against the above.

---

## 1. Executive Summary

**PAS is ORVN Labs' AI first-contact and brokerage operating-intelligence infrastructure** for
US real estate brokerages.

- **PAS is not a CRM**, not a chatbot, and not merely a dashboard. (This is stated explicitly
  and repeatedly across the repo's own docs — see `docs/claude_operating_pack/PAS_MASTER_CONTEXT.md`
  and `docs/pas300_product_direction_reset.md`.)
- **PAS handles first-contact operations** for brokerages: lead qualification, routing, booking,
  logging, and learning from interactions.
- **PAS Brain** is the durable operational-memory layer — the institutional memory of the
  brokerage that survives staff turnover and handoffs.

PAS exists to close the structural gaps where brokerages leak money: slow speed-to-lead,
inconsistent follow-up, "CRM graveyards" no one maintains, the limits of human availability, and
institutional memory walking out the door when a person leaves.

**Naming note (important — the repo carries three overlapping names; reconcile, don't pick one
blindly):**

| Name | Source in repo | Status |
|---|---|---|
| **Performative AI SuperStaff** | `README.md` (top of file) | Original MVP framing (inbound voice agent). Still the README title. |
| **Operational intelligence infrastructure** | `docs/claude_operating_pack/PAS_MASTER_CONTEXT.md` | The strategic positioning used across the operating pack. |
| **Proactive Assistant for Scale** | `docs/pas300_product_direction_reset.md` (§2, "Naming reset") | The **most recent** naming reset (PAS300), explicitly superseding "Performative AI Superstaff" and "generic dashboard" framings. |

The user's positioning language ("AI First Contact infrastructure," "Performative AI System,"
"making the company queryable," "brokerage memory") is consistent with the operating pack and
PAS300. Where this report uses such language and it is not verbatim in a repo file, it is labelled
**"User positioning context."**

---

## 2. Product Definition and Strategic Thesis

### What PAS does
PAS sits **underneath** a brokerage's operations and provides three things brokerages almost
never have (per `PAS_MASTER_CONTEXT.md`):

1. **Speed** — leads acted on in seconds, not hours (speed-to-lead).
2. **Continuity** — follow-up that does not depend on whether a human remembered.
3. **Memory** — a persistent operational record of the brokerage, its people, its leads, and its
   patterns (the **PAS Brain**).

The original/working product surface (per `README.md`) is a **first-contact voice + intake agent**:
it answers/handles a lead contact, captures intent (buy/sell/rent), budget, and timeline in the
lead's own words, handles objections in real time, books a viewing or schedules a callback, and
logs every step to an append-only event stream (`pas_events`).

### Why it exists — the brokerage problem (repo-supported)
US real estate brokerages leak money through their **operations**, not their marketing
(`PAS_MASTER_CONTEXT.md` §"The core problem PAS solves"):

- Leads arrive and sit (slow speed-to-lead).
- Leads fall through the cracks (lead leakage).
- ISA (Inside Sales Agent) functions underperform or churn.
- Follow-up is inconsistent and human-dependent.
- No one can see whether agents actually did what they were supposed to (accountability gap).
- The brokerage has **no memory** — every departure and handoff resets to zero.

### Why infrastructure, not a tool (repo-supported)
Tools are optional, swappable, and sit on the surface. **Infrastructure is the thing the business
runs *on*.** PAS is positioned as the operational substrate of a brokerage, not another app in the
stack (`PAS_MASTER_CONTEXT.md` §"Why 'infrastructure' and not 'tool'"). PAS300 sharpens this into:
PAS must become a **daily operating companion** — "the first thing they open in the morning, trust
through the day, and review before they close it" — not a dashboard you occasionally check.

### Repo-supported / user-positioning language
- **Repo-supported:** "operational intelligence infrastructure," "PAS Brain," "brokerage memory,"
  "speed-to-lead," "lead leakage," "first-contact," "queryable / adaptive / operationally
  intelligent" (PAS300 doctrine), "approval-gated," "evidence-backed," "human-safe."
- **User positioning context** (consistent with repo, not always verbatim): "AI First Contact
  infrastructure," "Performative AI System," "making the company queryable," "first-contact
  infrastructure."

---

## 3. Architecture Overview

PAS is a **Python/FastAPI backend** (entry `app/main.py`) with a **Next.js frontend** in `web/`,
backed by **Supabase**, deployed with **Railway** (backend) and **Vercel** (frontend). The backend
is the mature, test-covered surface; the frontend is currently a **demo-only shell** not yet wired
to the backend.

> Status legend: **Mature** = test-covered and merged; **Active** = current checkpoint band;
> **Demo-only** = present but not wired to live data; **Blocked** = externally gated;
> **UNVERIFIED** = cannot be confirmed from repo alone.

| Component | Location(s) | Purpose | Status | Risks / blockers |
|---|---|---|---|---|
| **Backend / API** | `app/main.py`, `app/routes/*` | FastAPI app; all HTTP/WS routes | Mature | — |
| **Conversation engine** | `app/engine/state_machine.py` | GREETING→INTENT→BUDGET→TIMELINE→BOOKING→CLOSING + OBJECTION state machine | Mature | Voice path depends on external vendors |
| **Voice / telephony adapter** | `app/routes/twilio_webhook.py`, `app/routes/websocket_handler.py`, `app/utils/audio.py`, `app/utils/twilio_replay.py` | Twilio inbound webhook + media-stream WS; replay/test mode | Mature (hardened in PAS211J) | Twilio trial/account gating (see §15) |
| **STT** | `app/services/stt/deepgram_client.py` | Deepgram streaming transcription | Mature | Vendor key required |
| **TTS** | `app/services/tts/elevenlabs_client.py` | ElevenLabs speech synthesis | Mature | Vendor key required |
| **Booking** | `app/services/booking/calcom_client.py` | Cal.com viewing booking | Mature | Cal.com 404 seen on demo (see §15) |
| **LLM abstraction** | `app/services/llm/{base,factory,anthropic_provider,openai_provider,claude_client}.py` | Provider-agnostic LLM (Anthropic default; OpenAI provider present) | Mature | — |
| **Email / digital lead ingestion** | `app/routes/lead_ingestion.py`, `app/services/ingestion/{lead_contracts,lead_normalizers,lead_dedupe,lead_ingestion}.py` | Inbound digital lead intake, normalization, durable dedupe | Mature (PAS213 / PAS213B) | — |
| **Outbound / pending-call pipeline** | `app/routes/outbound.py`, `app/services/outbound/*`, `app/services/worker/*`, `app/utils/call_store.py` | Pending-call creation and worker processing | Mature | — |
| **Memory candidate pipeline** | `app/services/memory/{candidate_contracts,candidate_generation,candidate_store,approved_memory_retrieval,memory_context_boundary}.py` | Generate → store → **manual review** → approved-memory retrieval; governed context boundary | Mature (PAS212 band) | Auto-approval must remain OFF until a future checkpoint authorizes it |
| **PAS Brain (memory hierarchy)** | conceptual; realized via memory + `app/db/lead_memory.py`, Supabase | Durable institutional memory (see §10) | Partial / evolving | Full "queryable company" is PAS306 (spec, not built) |
| **Events / logging** | `app/db/event_logger.py`, `app/services/events/contract.py`, `app/routes/events.py` | Append-only `pas_events` stream + event contract | Mature | Forbidden fields must stay out of payloads (see §9) |
| **Intelligence** | `app/services/intelligence/{leakage,queries,recommendations,sanitize,scoring}.py` | Leakage detection, scoring, recommendations, output sanitization | Mature | — |
| **Proactive layer** | `app/services/proactive/{observer,observer_digest,recommendations,action_proposals,supabase_snapshot_adapter,live_snapshot_bridge}.py` | Proactive observer, needs-attention, bounded action proposals | Mature (PAS205–PAS210) | Action proposals are bounded/approval-gated |
| **Simulation / evaluation** | `app/services/simulation/*` | Scenario simulation, strategy comparison, behavioral eval, evidence digests | Mature (PAS193–PAS202) | — |
| **Slack / operator surface** | `app/routes/slack_command.py`, `app/services/slack/*` | Slack NL commands, operator + broker conversation intents, digests | Mature (PAS191–PAS207) | — |
| **Admin / portal dashboards** | `app/routes/admin.py`, `app/routes/portal.py`, `app/static/dashboard/*` | Admin Operations Console + Brokerage Command Centre over `pas_events` | Mature | — |
| **Notifications** | `app/services/notifications/{email_client,email_sender,slack_client,sms_client,lead_alerts,formatter}.py` | Email/Slack/SMS lead alerts | Mature | Vendor keys required |
| **Auth / principal boundary** | `app/auth/{principal,resolver,authz}.py` | Principal resolver / JWT boundary (PAS211G/G.1); RBAC plan documented | Active band | Full admin JWT RBAC is planned (PAS211G doc), not all built — **UNVERIFIED how much is wired** |
| **Tenant isolation / RLS** | Supabase RLS (`scripts/migrate_v9_tenant_rls_policies.sql`), enforced in `app/db/*` | Multi-tenant data isolation | Mature (PAS211E) | Never weaken; never trust inbound tenant IDs |
| **Security services** | `app/services/security/{pii_safety,prompt_safety,rate_limit,secret_hash,secret_redaction}.py` | PII safety, prompt/memory injection safety, rate limiting, secret hashing/redaction | Mature (PAS211D–I) | — |
| **Secrets encryption / rotation** | `scripts/migrate_v10_secrets_encryption_rotation.sql`, `app/services/security/secret_hash.py` | Encrypted operator secrets + rotation (KID envelope) | Mature (PAS211F) | Crypto dependency must stay pinned |
| **Data layer** | `app/db/{supabase_client,call_logger,event_logger,audit_log,brokerage_store,agent_store,booking_store,error_store,invite_store,lead_memory}.py` | Supabase persistence | Mature | Do **not** apply migrations without authorization |
| **Frontend / web** | `web/` (Next.js 15, App Router, React 19) | Web-first product shell, becoming a PWA | **Demo-only** (no backend wiring, no auth) | Highest product-gap; see §13 |

---

## 4. Completed PAS Milestones

> **Evidence basis:** the `PAS160–PAS169` band is evidenced by **readiness-check scripts** present
> in `scripts/` (compiled artifacts visible under `scripts/__pycache__/`); the `PAS191–PAS213B`
> band is evidenced by **per-checkpoint docs** (`docs/pas*.md`) and **merged PRs** in `git log`;
> the `PAS211D–PAS211K` band is evidenced by **both docs and merged PRs** (see §5). Where a status
> is not directly provable from the repo, it is marked **UNVERIFIED**.

| Checkpoint | Purpose | Status | Evidence in repo | Commit / PR | Validation evidence | Notes / caveats |
|---|---|---|---|---|---|---|
| PAS160 | MVP sequence check | Complete (inferred) | `scripts/…/pas160_mvp_sequence_check` | not in last-30 log | readiness script | Predecessor band; pre-dates visible log window |
| PAS161 | Lead ingestion readiness | Complete (inferred) | `pas161_lead_ingestion_readiness_check` | — | readiness script | — |
| PAS162 | Pending-calls readiness | Complete (inferred) | `pas162_pending_calls_readiness_check` | — | readiness script | — |
| PAS163 | Candidate pipeline readiness | Complete (inferred) | `pas163_candidate_pipeline_readiness_check` | — | readiness script | — |
| PAS164 | Email ingestion readiness | Complete (inferred) | `pas164_email_ingestion_readiness_check` | — | readiness script | — |
| PAS165 | Email auth + dedupe readiness | Complete (inferred) | `pas165_email_auth_dedupe_readiness_check` | — | readiness script | — |
| PAS166 | Email dedupe policy readiness | Complete (inferred) | `pas166_email_dedupe_policy_readiness_check` | — | readiness script | — |
| PAS167 | Email secret reaper readiness | Complete (inferred) | `pas167_email_secret_reaper_readiness_check` | — | readiness script | — |
| PAS168 | Email secret rotation readiness | Complete (inferred) | `pas168_email_secret_rotation_readiness_check` | — | readiness script | — |
| PAS169 | Launch readiness + crypto roundtrip | Complete (inferred) | `pas169_launch_readiness_check`, `pas169_crypto_roundtrip_check`, `pas169_launch_readiness_report.json` | — | readiness script + JSON report at repo root | — |
| PAS211D | Critical security fix pack 1 (demo + rate-limit exposure) | **Complete** | `docs/pas211d_critical_security_fix_pack_1.md`, `tests/mvp/test_pas211d_*` | `594542f` / PR #60 | merged to `main` | — |
| PAS211E | Tenant isolation + RLS hardening | **Complete** | `docs/pas211e_*`, `tests/mvp/test_pas211e_tenant_isolation_rls.py`, `scripts/migrate_v9_tenant_rls_policies.sql` | `21e75e6` / PR #61 | merged to `main` | RLS migration committed (apply separately, authorized only) |
| PAS211F | Secrets encryption + rotation | **Complete** | `docs/pas211f_*`, `tests/mvp/test_pas211f_*`, `scripts/migrate_v10_secrets_encryption_rotation.sql` | `13bf70c` / PR #62 | merged to `main` | KID envelope; crypto dep pinned |
| PAS211G | Admin JWT RBAC + scoped client **plan** | **Complete (plan/docs)** | `docs/pas211g_admin_jwt_rbac_scoped_client_plan.md` | `d69b72f` / PR #63 | merged to `main` | Plan only — not full implementation |
| PAS211G.1 | Principal resolver boundary | **Complete** | `docs/pas211g_1_principal_jwt_boundary.md`, `app/auth/principal.py`, `tests/mvp/test_pas211g_1_principal_resolver.py` | `d223ab8` / PR #64 | merged to `main` | — |
| PAS211H | Prompt + memory injection safety | **Complete** | `docs/pas211h_*`, `app/services/security/prompt_safety.py`, `tests/mvp/test_pas211h_*` | `888100d` / PR #65 | merged to `main` | — |
| PAS211I | PII retention + readiness cleanup | **Complete** | `docs/pas211i_*`, `app/services/security/pii_safety.py`, `tests/mvp/test_pas211i_pii_retention.py` | `8e84aac` / PR #66 | merged to `main` | — |
| PAS211J | Twilio webhook hardening (verification + replay protection) | **Complete** | `docs/pas211j_*`, `app/utils/twilio_replay.py`, `tests/mvp/test_pas211j_*` | `524c172` / PR #67 | merged to `main` | — |
| PAS211K.1 | Deterministic install contract (docs) | **Complete** | `docs/pas211k_1_deterministic_install_contract.md` | `8bac8ff` / PR #68 | merged to `main` | — |
| PAS211K.2A | Python constraints generation plan (docs) | **Complete** | `docs/pas211k_2_python_constraints_generation_plan.md` | `7a108eb` / PR #69 | merged to `main` | — |
| PAS211K.2B (prep) | GitHub Actions constraints artifact workflow | **Complete** | `.github/workflows/pas211k-2b-generate-constraints.yml`, `docs/pas211k_2b_*` | `b99564a` / PR #70; `10b8638` / PR #71 | merged to `main` | Manual workflow + test-deps declared |
| PAS211K.2B | Pin Python transitive deps (`constraints.txt`) | **Complete** | `constraints.txt`, `nixpacks.toml` | `33e0731` / PR #72 | merged to `main`; pip pinned `26.1.2` | Do **not** hand-edit `constraints.txt` |
| PAS211K.2C | Deploy validation | **BLOCKED** | n/a | — | — | Blocked by **Railway subscription/billing** (infra, not code) |
| PAS211K.3A | Runtime alignment documentation | **Complete** | `docs/pas211k_3_runtime_alignment.md` | `fe1edd9` / PR #74 | merged to `main` | Docs-only; defines K.3 sub-sequence |
| PAS211K.3B | Frontend Node/pnpm runtime pinning | **Complete** | `web/.nvmrc` (=24), `web/package.json` (`engines.node: 24.x`, `packageManager: pnpm@11.3.0`) | `34d9251` / PR #75 | merged to `main` (current HEAD) | — |
| PAS211K.3C | Optional local Python version declaration (`.python-version`) | **Pending** | planned in K.3 doc §J | — | — | Non-authoritative local-dev only |
| PAS211K.3D | CI runtime verification workflow | **Pending** | planned in K.3 doc §J | — | — | Additive workflow asserting runtime alignment |
| Docs: Claude operating pack | Portable Claude context bundle | **Complete** | `docs/claude_operating_pack/*` | `432f125` / PR #73 | merged to `main` | This report extends that pack |

**Other completed bands evidenced by docs + tests (not in the prompt's checklist but real):**
PAS191–PAS192 (Slack NL commands / operator experience), PAS193–PAS202 (simulation, strategy
comparison, recommendation layer/review, manual test package/runtime, runtime inspection,
behavioral evaluation, evidence digest + surface), PAS203/PAS203B (Slack evidence digest),
PAS204 (broker conversation intelligence), PAS205 (proactive observer), PAS206 (Supabase snapshot
adapter), PAS207 (needs-attention digest), PAS208 (proactive recommendations), PAS209 (action
proposals — **DO NOT TOUCH**, see §8), PAS210 (live snapshot bridge / demo environment),
PAS211A (production config guards), PAS212 (memory candidate stack + approved-memory retrieval +
context boundary), PAS213/PAS213B (digital lead ingestion + durable dedupe + migration runbook),
PAS300 (product direction reset — "Proactive Assistant for Scale"), PAS301–PAS303 (auth/workspace,
role UX map, agent cockpit spec — **docs/specs only, not built**).

---

## 5. Current Repo State

| Field | Value |
|---|---|
| Repo root | `C:\Users\hp\Downloads\pas-engine\pas-engine` (nested under the outer working dir) |
| Remote | `origin → https://github.com/goodnews2206/pas-engine.git` (fetch + push) |
| Current branch | `main` |
| `main` HEAD | `62d3d4d` — *Merge pull request #75 from goodnews2206/pas211k-3b-frontend-runtime-pinning* |
| Working tree | **Clean** before this report; `## main...origin/main` (in sync with origin, 0 ahead / 0 behind) |
| Latest commits (top 6) | `62d3d4d` merge #75 · `34d9251` build(web): pin Node and pnpm runtime · `524405a` merge #74 · `fe1edd9` docs(runtime): K.3 alignment · `92323b5` merge #73 · `432f125` docs(context): add Claude operating pack |
| Local branches | `main` (checked out), plus many feature branches (e.g. `docs/claude-operating-pack`, `pas-web-*`, `pas191-*`…`pas211*`, `pas300`-era) — see Appendix |
| Remote branches | Mirror of the merged checkpoint branches (each merged PR's source branch still present on `origin`) |
| Known open PRs | **UNVERIFIED** — `gh` CLI is **not installed/available** in this environment, so GitHub PR state could not be queried. Git log shows PRs **#56–#75 already merged** into `main`. |
| Safe to work in? | **Yes** — correct repo confirmed, clean tree, in sync with origin |
| Stale / diverged branches? | Many merged feature branches remain (not deleted, per the "do not delete" posture). `main` itself is not diverged. **UNVERIFIED** whether any unmerged feature branch carries pending value. |
| Current checkpoint branch present? | No dedicated K.3C/K.3D branch is checked out; HEAD is `main` post-K.3B. |

**Repo-vs-doc discrepancy to flag:** `docs/claude_operating_pack/PAS_SEQUENCE_AND_STATUS.md` states
"**PAS211K.3 — NEXT ACTIONABLE CHECKPOINT**" and lists last-completed as **PAS211K.2B**. The git
history shows **PAS211K.3A and PAS211K.3B are already merged** (PRs #74, #75). So the active band is
**PAS211K.3, with K.3A + K.3B done and K.3C + K.3D pending.** Treat the status doc as slightly
behind `main`; the live git history is authoritative.

---

## 6. Current Checkpoint / Active Work

- **Checkpoint:** **PAS211K.3 — Runtime Alignment** (active band).
- **Purpose:** remove silent runtime drift by naming one authoritative source per surface
  (backend Python via `nixpacks.toml` = `python311`; pip pinned `26.1.2`; frontend Node/pnpm pinned
  in `web/`). Defined in `docs/pas211k_3_runtime_alignment.md`.
- **Completed within K.3:**
  - **K.3A** — runtime-alignment documentation (merged, PR #74).
  - **K.3B** — frontend Node/pnpm pinning: `web/.nvmrc` (`24`), `engines.node: "24.x"`,
    `packageManager: "pnpm@11.3.0"` (merged, PR #75; current HEAD).
- **Pending within K.3:**
  - **K.3C** — optional `.python-version` as a *non-authoritative* local-dev convenience.
  - **K.3D** — additive **CI runtime-verification workflow** asserting Python/Node/pnpm align with
    declared sources of truth.
- **Blockers:**
  - **PAS211K.2C (deploy validation) remains BLOCKED** by a Railway subscription/billing issue
    (infrastructure/account level, **not code**). K.3 is explicitly **deploy-independent** and does
    not require Railway.
- **Next exact action (recommended):** the next *actionable* checkpoint is **PAS211K.3C** (tiny,
  docs/config-adjacent) or **PAS211K.3D** (additive CI workflow). Per the no-skip rule, this should
  begin with an **audit report**, not implementation.
- **Type of next action:** **audit → (small) implementation → validation**, on a fresh checkpoint
  branch, then PR. *Not* a deploy (2C is blocked); *not* a broad rewrite.

> **If ambiguous in a live session: "Current checkpoint needs user confirmation."** Confirm with
> Daniel whether to proceed with K.3C, K.3D, or to revisit K.2C if Railway has been restored.

---

## 7. Engineering Operating Pattern

This mirrors `docs/claude_operating_pack/PAS_ENGINEERING_RULES.md` and `CLAUDE_START_HERE.md`.

### 7.1 No-Skip Rule
- No implementation before an **audit**.
- No **push** before **validation**.
- No **merge** before **PR verification**.
- No **next checkpoint** before **post-merge verification**.
- No **broad rewrites** when a small checkpoint will do (additive, single-file diffs preferred).

### 7.2 Standard Sequence
1. Repo safety check (correct repo? clean tree?).
2. Branch / status check (which checkpoint is current?).
3. Read relevant docs / code / tests.
4. **Audit report.**
5. **User approval.**
6. Implementation on a **checkpoint branch**.
7. Targeted validation (run the most relevant tests first).
8. Full validation where feasible (full simulation matrix / suite).
9. **Implementation final report.**
10. Commit.
11. Push branch (**separate, explicitly authorized step**).
12. Open PR.
13. **PR verification report.**
14. Manual merge **only after explicit approval**.
15. **Post-merge verification** on `main`.
16. Only then begin the next checkpoint.

### 7.3 Report-First Discipline
Required reports: **Audit report**, **Implementation final report**, **PR verification report**,
**Post-merge verification report**, and a **Blocker report** whenever blocked.

### 7.4 Branch Discipline
- Never work directly on `main` unless explicitly instructed (and the harness blocks pushes to
  `main` regardless).
- Use **checkpoint branches** (naming convention visible in repo: `pas211k-3b-frontend-runtime-pinning`,
  etc.).
- Never rewrite pushed history; never force-push.
- Never merge stale branches. If a branch has diverged heavily, **create a fresh branch from
  current `main`** and reapply only the missing value.
- **Never confuse the PAS repo with the ORVN website repo** (or `goodnews2206/Orvn-labs`).

### 7.5 Validation Discipline
- Run relevant tests before commit; targeted first, then full where feasible.
- **Baseline: 1252 passed / 0 failed** (per `PAS_SEQUENCE_AND_STATUS.md`). Any drop is a regression
  and must be explained. **UNVERIFIED in this session** — not re-run (this is a docs-only task).
- For **docs-only** changes, do **not** run the full suite — there is nothing to verify in code.
- Never fake test results. If validation can't run, explain why. If a failure is out of scope,
  report it clearly rather than silently absorbing it.

---

## 8. Guardrails and Forbidden Actions

> Marking: **[Repo]** = supported by a file/doc in the repo; **[Convention]** = from the operating
> pattern / project memory.

- **Never touch secrets or `.env`; never expose secrets.** **[Repo]** (`PAS_ENGINEERING_RULES.md`
  §"Secrets handling"). Pattern: temp file → SHA-256 fingerprint → use → cleanup; reference by
  fingerprint, never value.
- **Never run destructive git** (no `reset --hard`, no history rewrite, no branch/file deletion).
  **[Repo]**
- **Never force-push.** **[Repo]**
- **Never push without explicit this-session authorization.** **[Repo]** (the harness *also* blocks
  push-to-`main`). **[Convention]**
- **Never merge without explicit authorization.** **[Repo]**
- **Do not modify `requirements.txt`, `constraints.txt`, or `nixpacks.toml`** without explicit
  instruction (reproducible-build invariants; pip pinned `26.1.2`). **[Repo]**
- **Do not apply migrations** (e.g. `scripts/migrate_v9_*`, `v10_*`) unless a checkpoint explicitly
  authorizes it. **[Repo]**
- **Do not touch PAS209.** **[Repo]** (standing do-not-touch; the action-proposals / recovery corpus
  band — `app/services/proactive/action_proposals.py`, `recovery/pas209_5_bytecode_corpus/`).
- **Do not delete `__pycache__`.** **[Repo]**
- **Do not alter protected checkpoint files** unless the active checkpoint explicitly allows it.
  **[Convention]**
- **Never weaken tenant isolation / RLS.** **[Repo]** (`scripts/migrate_v9_tenant_rls_policies.sql`;
  PAS211E).
- **Never trust tenant/brokerage IDs from inbound payloads.** **[Convention/Repo]** (principal
  resolver boundary, PAS211G/G.1).
- **Never store forbidden raw sensitive data** if the architecture forbids it (PII safety, PAS211I).
  **[Repo]**
- **Never auto-approve PAS Brain memory candidates** unless a future checkpoint explicitly
  authorizes it — manual review first. **[Repo]** (memory candidate pipeline, PAS212).
- **Never make unsupported product/customer/proof claims.** **[Convention]** (PAS300 "evidence-backed,"
  demo-only labeling).
- **Never modify the ORVN website repo while working on PAS.** **[Convention]**
- **Never touch Railway / Vercel / Supabase settings** unless the checkpoint explicitly authorizes
  it. **[Convention/Repo]**

---

## 9. Data, Security, and Tenant Isolation Rules

- **Multi-tenant by `brokerage_id`.** Isolation enforced at the data layer and via Supabase RLS
  (`scripts/migrate_v9_tenant_rls_policies.sql`, PAS211E). The brokerage/portal surfaces are scoped
  to the authenticated brokerage (`app/routes/portal.py`).
- **`brokerage_id` source of truth:** must be derived from the **authenticated principal / server
  side**, never trusted from an inbound payload (principal resolver — `app/auth/principal.py`,
  `app/auth/resolver.py`, PAS211G/G.1).
- **RLS policies:** present as migration `v9`; do not weaken or bypass.
- **Email/webhook signature enforcement:** Twilio webhook verification + replay protection
  (`app/utils/twilio_replay.py`, PAS211J); email auth/dedupe readiness (PAS165–PAS167). Inbound
  signatures must be verified before processing.
- **Durable dedupe:** digital lead ingestion uses durable persistence + dedupe
  (`app/services/ingestion/lead_dedupe.py`, `scripts/migrate_v8_digital_ingestion_dedupe.sql`,
  PAS213B; runbook `docs/pas213b_1_dedupe_migration_runbook.md`).
- **Encryption / KID envelope:** operator secrets encrypted with key-ID envelope + rotation
  (`scripts/migrate_v10_secrets_encryption_rotation.sql`, `app/services/security/secret_hash.py`,
  PAS211F). Crypto dependency must remain pinned.
- **Secret hashing/redaction:** `app/services/security/{secret_hash,secret_redaction}.py` — secrets
  are fingerprinted/redacted, never logged in the clear.
- **Event payload restrictions:** events flow to an append-only `pas_events` stream via
  `app/db/event_logger.py` under a contract (`app/services/events/contract.py`). Output is sanitized
  before exposure (`app/services/intelligence/sanitize.py`, `app/services/workflows/sanitize.py`):
  admin sees full payloads; brokerage sees **sanitized** payloads with plain-English labels.
- **Forbidden event fields:** raw secrets, unredacted PII, and cross-tenant identifiers must not be
  written into event payloads. **[Specific forbidden-field list: UNVERIFIED — confirm against
  `app/services/events/contract.py` before relying on exact field names.]**
- **Audit / logging:** `app/db/audit_log.py` + operator audit hash backfill
  (`scripts/backfill_operator_audit_hashes.py`); audit-chain readiness checks (PAS174–PAS178).
- **Data that can/cannot be stored:** durable operational records and approved memory — yes;
  unreviewed memory candidates as trusted knowledge — no (manual approval required); raw sensitive
  PII beyond retention policy — no (PAS211I).

---

## 10. Memory Architecture / PAS Brain

Per `docs/claude_operating_pack/PAS_MEMORY_ARCHITECTURE.md`, memory is a **four-tier hierarchy**,
ephemeral → durable:

```
Session Memory → User Memory → Operational Memory → PAS Brain
 (ephemeral)     (per person)    (per brokerage)     (durable, institutional)
```

1. **Session Memory** — single interaction; working memory (RAM analogy).
2. **User Memory** — per person (agent/ISA/team lead); persists across that user's sessions.
3. **Operational Memory** — the brokerage's shared operational state; "did the follow-up actually
   happen?" lives here.
4. **PAS Brain** — durable institutional memory that survives turnover and handoffs; the moat.

**Candidate pipeline (repo-grounded, PAS212):**
`app/services/memory/candidate_generation.py` → `candidate_store.py` (governed by
`candidate_contracts.py`) → **manual review first** → `approved_memory_retrieval.py` exposes only
approved memory, behind `memory_context_boundary.py` (a governed context boundary so memory cannot
leak across tenants or into prompts unsafely; reinforced by PAS211H prompt/memory injection safety).

- **Manual review now; automatic mode later** — automatic approval is **only** permitted after a
  future checkpoint explicitly validates and authorizes it. Until then, **never auto-approve**.
- **What PAS Brain stores:** approved, governed operational knowledge (leads, patterns,
  interactions, commitments).
- **What PAS Brain must not expose:** unreviewed candidates, cross-tenant data, raw secrets/PII,
  unsanitized payloads.
- **Why it's the moat:** institutional knowledge that does not walk out the door when a person
  leaves — *"your brokerage finally has a memory."* PAS300 §12 extends this to a **queryable,
  evidence-backed, approval-gated** Brain (spec PAS306, not yet built).

---

## 11. Email Lead Ingestion and First-Contact Pipeline

- **Target inbound sources:** digital lead sources (email/web form leads). The email-ingestion band
  (PAS164–PAS168) plus the digital-lead rebuild (PAS213/PAS213B) are the canonical path.
- **Endpoint / route:** `app/routes/lead_ingestion.py`.
- **Parser / normalization:** `app/services/ingestion/lead_normalizers.py`,
  `lead_contracts.py` (typed contracts), `lead_ingestion.py` (orchestration).
- **Signature verification:** email auth/dedupe + secret reaper/rotation readiness (PAS165–PAS168).
- **Dedupe:** durable dedupe (`app/services/ingestion/lead_dedupe.py`,
  `scripts/migrate_v8_digital_ingestion_dedupe.sql`, PAS213B).
- **Pending-call creation:** ingestion feeds the pending-call / outbound pipeline (§12).
- **Worker / CLI:** `app/services/worker/*` processes queued work; readiness scripts under
  `scripts/`.
- **Outbound call adapter:** `app/routes/outbound.py` + `app/services/outbound/*`.
- **Memory candidate generation:** ingestion/interactions can emit memory candidates (§10).
- **Event emission:** every step logs to `pas_events` via `app/db/event_logger.py`.
- **Error paths:** `app/db/error_store.py`; lead alerts via `app/services/notifications/lead_alerts.py`.
- **Current status:** **Mature / merged** (PAS213B durable ingestion is the latest in this band).
- **Open blockers:** none code-level identified; deploy proof gated by Railway (PAS211K.2C).

---

## 12. Voice / Calling / Pending Call Pipeline

Per `README.md` architecture + `app/` code:

- **Inbound voice:** Twilio → `POST /twilio/voice` (`app/routes/twilio_webhook.py`) returns TwiML
  opening a media-stream WebSocket (`/ws/media-stream/{call_sid}`, `app/routes/websocket_handler.py`).
- **STT/TTS:** Deepgram (`app/services/stt/deepgram_client.py`) ↔ ElevenLabs
  (`app/services/tts/elevenlabs_client.py`); audio utils in `app/utils/audio.py`.
- **State machine:** `app/engine/state_machine.py` —
  `GREETING → INTENT → BUDGET → TIMELINE → BOOKING → CLOSING`, with an **OBJECTION** branch
  (any state) that calls the LLM for a short rebuttal then resumes.
- **Objection handling:** LLM-backed (`app/services/llm/*`), bounded (README cites ~100-token cap).
- **Booking / routing:** Cal.com on consent (`app/services/booking/calcom_client.py`); else a
  **callback** is scheduled (the seeded demo `SIM-YC-W26-CALLBACK-001` exercises the callback
  branch).
- **Voicemail / callback:** callback request + follow-up scheduling is a first-class branch (see
  README demo workflow: `callback_requested → followup_scheduled → completed`).
- **Pending calls / outbound:** `app/routes/outbound.py`, `app/services/outbound/*`,
  `app/utils/call_store.py`; worker processing in `app/services/worker/*`.
- **Replay / test modes:** `app/utils/twilio_replay.py` (PAS211J replay protection) + simulation
  layer (`app/services/simulation/*`) for deterministic, phone-free runs.
- **Call state / records:** `app/db/call_logger.py`; outcome + transcript persisted on WS close.
- **Current status:** **Mature**; hardened in PAS211J.
- **Risks / blockers:** vendor keys required (Twilio/Deepgram/ElevenLabs/Cal.com); **Twilio trial
  gating** and a **Cal.com 404 on the demo** were noted in the 2026-05-02 environment snapshot
  (project memory) — **re-verify live** (see §15).

---

## 13. Frontend / Web / Dashboard / PWA State

The frontend **is** in the PAS repo, at `web/` (it is *not* the separate ORVN marketing site).

- **Stack:** Next.js 15 (App Router), React 19, TypeScript (`web/package.json`, `web/README.md`).
- **Runtime pinning (PAS211K.3B):** `web/.nvmrc` = `24`; `engines.node: "24.x"`;
  `packageManager: "pnpm@11.3.0"`. pnpm is the enforced package manager; npm is discouraged.
- **Modules present (demo):** app shell (TopBar/Sidebar/Composer), Command Center intelligence
  layout (7 sections), notification center (client island, ~15 demo notifications), 11 module
  empty states, role-aware navigation (demo session).
- **Deployment:** Vercel, Root Directory `web`, target domain `pas.orvnlabs.com`
  (`docs/pas_web_vercel_deployment.md`).
- **Crucial caveat — NOT connected:** **no backend API wiring, no auth (no Clerk/Auth0/Supabase
  Auth), no realtime/SSE/WebSocket/push, no live data source.** Everything is explicitly labelled
  **demo / rehearsal**; "PAS has not changed live customer behavior."
- **Strategic state (PAS300):** the A–I demo arc proved PAS can be *assembled* as a product shell,
  but **not** that it drives a daily habit. PAS301–PAS303 (auth/workspace model, role-specific UX
  map, agent cockpit spec) are written as **specs/docs only** — none are built. This is the largest
  product gap.
- **How it relates to PAS Brain / product surface:** the frontend is the future home of the Agent
  Cockpit, PAS Chat, and the Brain knowledge surface (PAS303/PAS305/PAS306), but today it is a
  static shell ahead of the backend wiring.

---

## 14. Testing and Readiness Benchmarks

> **Baseline (per docs): 1252 passed / 0 failed.** Not re-run in this docs-only session →
> **last-known status UNVERIFIED live.** Test root: `tests/` (52 test files; `tests/mvp/*` carries
> the per-checkpoint suites).

| Command | Purpose | When to run | Last known status | Evidence | Notes |
|---|---|---|---|---|---|
| `pytest` (full) | Full backend suite / simulation matrix | Before any engineering commit (not docs-only) | 1252/0 (per docs) | `PAS_SEQUENCE_AND_STATUS.md` | Run from repo root in `venv` |
| `pytest tests/mvp/test_pas211k_*` | Targeted K-band checks | When touching K.3 | UNVERIFIED | `tests/mvp/` | Targeted-first discipline |
| `pytest tests/mvp/test_pas211e_tenant_isolation_rls.py` | RLS / tenant isolation | When touching tenancy/RLS | UNVERIFIED | file present | — |
| `pytest tests/mvp/test_pas211f_secrets_encryption_rotation.py` | Secrets encryption/rotation | When touching secrets/crypto | UNVERIFIED | file present | — |
| `pytest tests/mvp/test_pas211j_twilio_webhook_hardening.py` | Twilio webhook verify/replay | When touching voice/webhook | UNVERIFIED | file present | — |
| `pytest tests/mvp/test_pas213b_durable_ingestion.py` | Durable lead ingestion + dedupe | When touching ingestion | UNVERIFIED | file present | — |
| `pytest tests/mvp/test_pas212*` | Memory candidate pipeline / boundary | When touching memory | UNVERIFIED | files present | — |
| `python scripts/pas169_launch_readiness_check.py` | Launch readiness | Pre-launch reasoning | report present (`pas169_launch_readiness_report.json`) | `scripts/` | One of many `pasNNN_*_readiness_check.py` |
| `python scripts/pas169_crypto_roundtrip_check.py` | Crypto roundtrip | Crypto changes | UNVERIFIED | `scripts/` | — |
| `python scripts/integrity_check.py` | Integrity check | Periodic | report present (`integrity_check_report.json`) | `scripts/` | — |
| `web: pnpm install && pnpm build` | Frontend production build | Frontend changes | UNVERIFIED | `web/package.json` | Node 24, pnpm 11.3.0 |
| `web: pnpm type-check` | TS type check (`tsc --noEmit`) | Frontend changes | UNVERIFIED | `web/package.json` | — |
| CI: `.github/workflows/pas211k-2b-generate-constraints.yml` | Constraints artifact generation | Manual dispatch | UNVERIFIED | workflow file | Only CI workflow present; K.3D would add runtime verification |

There are **many** `scripts/pasNNN_*_readiness_check.py` scripts (PAS145, PAS158, PAS160–PAS208+) —
each gates its checkpoint. Treat the readiness script for a band as its acceptance check.

---

## 15. Known Blockers / Risks / Open Questions

### Verified blockers (from repo/docs)
- **PAS211K.2C deploy validation is BLOCKED** by a **Railway subscription/billing** issue
  (infrastructure/account level, not code). All of K.3 is deploy-independent.
- **Only one CI workflow exists** (`pas211k-2b-generate-constraints.yml`); there is **no CI
  runtime-verification / test-on-PR workflow yet** (that is the planned K.3D).

### Inferred risks
- **Frontend runtime drift was the highest K.3 risk** and is now *mitigated* by K.3B pinning — but
  the frontend remains **entirely demo-only** (no auth, no backend wiring), which is the biggest
  product-readiness gap before any real launch.
- **Vendor dependency**: voice/booking depend on Twilio, Deepgram, ElevenLabs, Anthropic, Cal.com,
  Supabase keys — any missing/expired key breaks the live path.
- **Status doc lag**: `PAS_SEQUENCE_AND_STATUS.md` trails `main` (says K.3 "next" when K.3A/B are
  merged). Risk of acting on stale status — always re-confirm via git.
- **Merged feature branches not pruned**: many remain on `origin`; low risk but clutter.

### Questions for Daniel (NEEDS USER CONFIRMATION)
- Is **Railway** restored? If yes, does PAS211K.2C resume, or proceed to K.3C/K.3D first?
- Confirm the **active next checkpoint**: K.3C (`.python-version`), K.3D (CI runtime verification),
  or something else?
- **Twilio trial gating** and the **Cal.com 404 on demo** were noted on 2026-05-02 (project memory).
  Are these still open? (Not re-verifiable from the repo alone — **UNVERIFIED**.)
- Are there **open PRs**? (Could not check — `gh` unavailable.)
- Which **naming** is canonical going forward — "Proactive Assistant for Scale" (PAS300) — and
  should the README title be updated accordingly?

---

## 16. Next Benchmarks / Roadmap Ahead

### Immediate next checkpoint
**PAS211K.3C** (optional non-authoritative `.python-version`) and/or **PAS211K.3D** (additive CI
runtime-verification workflow). Both are deploy-independent and low-risk. Begin with an audit.

### Next 3–5 engineering benchmarks (visible in repo)
1. **PAS211K.3C** — local Python version declaration (non-authoritative).
2. **PAS211K.3D** — CI runtime verification workflow.
3. **PAS211K.2C** — deploy validation (**unblock Railway first**).
4. **PAS301** — Auth / Session / Workspace model (currently spec only — `docs/pas301_*`).
5. **PAS303** — Agent Cockpit build (currently spec only — `docs/pas303_*`); the agent-adoption wedge.

### Launch / demo readiness requirements
- **Demo-readiness:** seeded demo call (`SIM-YC-W26-CALLBACK-001`) resolves on both Admin and
  Brokerage surfaces; confirm Cal.com booking path and Twilio number are live (both flagged
  **UNVERIFIED** from the 2026-05-02 snapshot).
- **Launch-readiness gates:** Railway deploy proven (K.2C); full suite green (1252/0); readiness
  scripts pass; secrets encrypted + rotated (PAS211F); RLS enforced (PAS211E); webhook hardened
  (PAS211J); PII retention compliant (PAS211I).

### Before production launch
- Real **auth** + **workspace isolation** (PAS301) wired into the frontend.
- Backend ↔ frontend wiring (frontend is demo-only today).
- Deploy proven on Railway + Vercel; CI runtime verification (K.3D) green.

### Before onboarding a brokerage
- Tenant isolation/RLS validated end-to-end; per-brokerage scoping confirmed on portal surfaces;
  operator/Slack surfaces validated; onboarding flow (`app/routes/onboarding.py`) exercised.

### Before automatic PAS Brain mode
- Manual-review track validated at volume; an explicit checkpoint **authorizing** auto-approval
  with guardrails; memory context boundary + injection safety proven (PAS211H, PAS212D).

> **Recommended next sequence — needs user confirmation:** K.3C → K.3D → (unblock) K.2C →
> then resume the PAS300 product arc (PAS301 auth/workspace → PAS303 agent cockpit) for the
> frontend-wiring push.

---

## 17. How Future Claude Sessions Must Behave

1. **Read this report before acting.**
2. **Confirm live repo status** (repo, branch, `git status`, `git log`, active checkpoint) before
   any work.
3. **Never implement from memory alone** — ground every change in current files/tests/docs.
4. **Never skip the audit.** Audit → approval → implement.
5. **Never merge without Daniel's explicit authorization**; never push without explicit
   this-session authorization.
6. **Always produce the required final reports** (audit, implementation, PR verification,
   post-merge).
7. **Preserve scope** — docs-only stays docs-only; name anything touched outside scope.
8. **Stop when uncertain** — a blocked-but-safe task beats an unblocked rule violation.
9. **Prefer small, checkpointed changes** over broad rewrites.
10. **Never confuse the PAS repo (`goodnews2206/pas-engine`) with the ORVN website repo** or
    `goodnews2206/Orvn-labs`.

---

## 18. Claude Chat Continuation Prompt

Paste this into Claude Chat alongside this report:

> Read the attached PAS Full Operating Report. Confirm your understanding of PAS, the current repo
> state, the active checkpoint, the guardrails, the workflow sequence, and the next safe action. Do
> not write code until I provide the latest repo status and explicitly authorize the next
> checkpoint.

---

## 19. Appendix

### Exact repo path used during generation
`C:\Users\hp\Downloads\pas-engine\pas-engine` (the git repo is nested one level under the outer
working directory `C:\Users\hp\Downloads\pas-engine`).

### Important branches
- `main` (HEAD `62d3d4d`) — canonical.
- Recently merged checkpoint branches: `pas211k-3b-frontend-runtime-pinning`,
  `pas211k-3a-runtime-alignment-doc`, `docs/claude-operating-pack`,
  `pas211k-2b-python-constraints-install-path`, `pas211j-twilio-webhook-hardening`,
  `pas211i-pii-retention-readiness-cleanup`, `pas211h-prompt-memory-injection-safety`,
  `pas211g-1-principal-jwt-boundary`, `pas211f-secrets-encryption-rotation`,
  `pas211e-tenant-isolation-rls-hardening`, `pas211d-critical-security-fix-pack-1`.
- Large `pas-web-*` family (frontend A–I arc) and `pas191`–`pas211` feature branches still present.

### Important commits
- `62d3d4d` merge #75 (K.3B, current HEAD) · `34d9251` pin Node/pnpm · `fe1edd9` K.3 alignment doc ·
  `432f125` Claude operating pack · `33e0731` pin Python transitive deps · `524c172` Twilio webhook
  hardening · `21e75e6` tenant isolation/RLS · `13bf70c` secrets encryption/rotation.

### Important docs / files
- `README.md` (voice MVP architecture + seeded demo).
- `docs/claude_operating_pack/` (the operating pack — start at `CLAUDE_START_HERE.md`).
- `docs/pas300_product_direction_reset.md` (current product doctrine + PAS301–308 sequence).
- `docs/pas211k_3_runtime_alignment.md` (active checkpoint definition).
- `constraints.txt`, `nixpacks.toml`, `railway.toml`, `Procfile` (build/runtime sources of truth).
- `scripts/migrate_v*.sql` (migrations — **apply only when authorized**), `scripts/schema.sql`,
  `scripts/seed_demo_brokerage.sql`.
- `web/` (Next.js frontend; `web/README.md`, `web/package.json`, `web/.nvmrc`).

### Key commands
- Safety: `git rev-parse --show-toplevel`, `git remote -v`, `git status --short --branch`,
  `git branch --show-current`, `git log --oneline -n 30`.
- Backend tests: `pytest` (full) / `pytest tests/mvp/test_pasNNN_*.py` (targeted).
- Readiness: `python scripts/pasNNN_*_readiness_check.py`.
- Frontend: `cd web && pnpm install && pnpm build && pnpm type-check`.

### Glossary
- **PAS** — the product. Names in repo: "Performative AI SuperStaff" (README), "operational
  intelligence infrastructure" (operating pack), "Proactive Assistant for Scale" (PAS300, current).
- **PAS Brain** — durable institutional memory layer (tier 4 of the memory hierarchy).
- **ORVN Labs** — the company building PAS.
- **Checkpoint** — an ordered, non-skippable unit of engineering work (`PASNNN[.x]`).
- **Baseline** — the known-good green test count (**1252/0**).
- **RLS** — Supabase Row-Level Security (tenant isolation).
- **KID envelope** — key-ID-based secret encryption + rotation scheme (PAS211F).
- **A–I arc** — the frontend operational-demo-layer sequence that PAS300 reset.

### Open unknowns (UNVERIFIED — confirm with Daniel / live repo)
- Live test status (1252/0 not re-run this session).
- Open PR list (`gh` unavailable).
- Railway billing status; Twilio trial gating; Cal.com demo 404.
- Exact forbidden-field list in the event contract.
- How much of admin JWT RBAC (PAS211G) is wired vs. planned.
- Which naming is canonical going forward.
