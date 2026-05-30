# PAS Operational Demo Layer — Product Plan

> Status: plan only (Step 12B). Owner: ORVN Labs. Created 2026-05-30.
> **Frontend-only product plan. No implementation in this document.**
>
> Scope: turn the PAS web app from an *explanatory* demo shell into an
> *operational* demo of a live brokerage workspace — still demo-only,
> still rehearsal-labelled, still zero live behaviour.
>
> This is **not** backend integration, **not** production behaviour,
> **not** real customer data. Every object described here is a typed,
> clearly-fictional, frontend-only demo object.

---

## 0. Doctrine and constraints (binding on every step below)

**PAS — making brokerages queryable, adaptive, and operationally
intelligent.**

Product rules: **extremely simple · extremely functional · extremely
beautiful.**

Strategic direction: PAS should be good enough that brokerages
increasingly place their operations *inside* it. PAS can integrate with
existing systems, but the experience should gradually make PAS the
preferred operating layer. PAS feels like a **calm, trusted operations
partner** — not a CRM, not a chatbot, not Slack, not a noisy AI
dashboard.

**Hard constraints for the whole implementation arc:**

- No UI implemented in this doc — plan only.
- No backend, no `app/main.py`, no CORS, no API calls, no auth
  implementation, no Supabase browser access, no mutations, no secrets.
- No production data. No live behaviour claimed.
- Demo / rehearsal labels stay visible on every surface.
- PAS must not change live customer behaviour.
- No fake customer names implying real clients — only clearly
  fictional demo data (see §7.1 naming convention).

---

## 1. What exists today

Shipped and live on Vercel **in demo mode** (Steps 1–11; Step 12 demo
deployment executed). All surfaces are static/demo-only with no network
calls.

| Surface | State today |
|---|---|
| Vercel deployment | Demo mode, `NEXT_PUBLIC_PAS_API_BASE_URL` unset → no backend calls. |
| Command Center | Six-section intelligence overview, static demo data. |
| Composer | Local state machine (idle → typing → thinking → responded), no network. |
| Notifications drawer | Bell + badge + drawer, five severity levels, 15 demo items; reply field is a placeholder. |
| Module skeletons | 11 module routes with module-specific empty states. |
| API boundary scaffold | Typed read-only client, `IS_DEMO_MODE` gating, `GET /health` probe, connection-status chip. No live wiring beyond health. |
| Demo/rehearsal labels | DemoBanner (full-width), per-card "Simulated" pills, "PAS has not changed live customer behavior." disclaimers. |
| PAS209 backend | Bounded action-proposal package **merged to backend** (PR #40) — **but no frontend action-proposal UI integration yet.** |

**Implication:** the app today *explains* what PAS will do. It does not
yet *show a brokerage being operated*.

---

## 2. Current weaknesses

1. Modules are **too explanatory** — paragraphs where there should be
   operational objects.
2. Pages **don't show enough operational objects** (leads, calls,
   callbacks as real rows/cards).
3. **PAS Brain is not visible** — the "queryable, adaptive" promise has
   no surface.
4. **Integrations are not interactive** — no marketplace, no detail.
5. **No Agents section** — the people PAS coordinates are absent.
6. **No first-class permissions/roles surface.**
7. **No visible sign-in/sign-out/account control.**
8. **Notification reply fields appear non-functional** — dead UI.
9. **In-app communication is missing** — no place to discuss the work.
10. Net effect: the product feels like **potential, not operational
    power**.

---

## 3. Target experience

A Broker Owner opening PAS should feel, within seconds:

- "PAS **understands** my brokerage."
- "PAS **knows what needs attention**."
- "PAS is **watching commitments**." (callbacks, promises, follow-ups)
- "PAS can **explain why**." (evidence on demand)
- "PAS can **coordinate the team**." (communication on the work)
- "PAS can **propose bounded actions**." (named, scoped, reversible)
- "PAS **will not act without permission**." (approval-gated, always)

Every module must make at least one of these felt — not stated.

---

## 4. Product habit loop

The daily dependency loop PAS must earn. Each turn deepens trust and
makes PAS harder to leave.

```
        ┌─────────────────────────────────────────────┐
        │ 1. Open Command Center (the operating home)  │
        │ 2. Review the attention queue                │
        │ 3. Ask PAS what matters (composer)           │
        │ 4. Approve / decline bounded proposals       │
        │ 5. Discuss objects in PAS Room / threads     │
        │ 6. Assign / reassign ownership               │
        │ 7. Inspect evidence (receipts)               │
        │ 8. Trust PAS more → return tomorrow          │
        └──────────────────────────┬──────────────────┘
                                   └──► back to 1
```

The loop is the product. Modules are surfaces the loop passes through;
PAS Room and the attention queue are where it concentrates.

---

## 5. In-app communication layer

> The simplest, most functional, most beautiful version. **Not a Slack
> clone.** Communication is **attached to operational work, not
> separated from it.** The goal is **company memory, not chat noise.**

### 5.1 Two shapes of communication

| Shape | What it is |
|---|---|
| **PAS Room** | One brokerage-wide operating room. The calm, low-volume feed of what PAS noticed, what was decided, and what the team coordinated. Not a general chat — an operations log you can talk in. |
| **Object threads** | A thread *lives on* each operational object: a lead, callback, proposal, recommendation, booking, or call. Discussion stays welded to the work it concerns. |

### 5.2 Message types (small, typed vocabulary — not freeform chat)

- **Human message** — a person says something on an object or in the Room.
- **PAS message** — PAS surfaces a signal, answers a mention, or explains.
- **Approval message** — "Approved / Declined: <proposal>" with actor + time (demo-only).
- **Assignment message** — "Assigned <object> to <agent>" (demo-only).
- **Evidence reference** — an inline link to a call, signal, or digest.
- **Decision record** — an immutable summary line that becomes company memory.

### 5.3 Behaviours

- **PAS mentions/replies:** `@PAS why is this lead at risk?` renders an
  inline PAS reply *in the thread* (demo-only canned reasoning, labelled).
- **Role-aware visibility:** an Agent sees their objects' threads; a
  Team Lead sees their team's; Owner/Admin see all. Visibility echoes
  the role bundle (§8 Permissions) — display-only, not a security
  boundary.
- **Attachments/evidence links:** threads can reference evidence
  signals and digests; clicking opens the evidence (read-only).
- **Decision history:** approval + assignment + decision records form a
  searchable, append-only history per object.
- **Search / queryability:** the Room and threads are queryable ("show
  every callback we discussed this week", "what did PAS flag on lead
  D-1042") — this is the "queryable brokerage" doctrine made visible.

### 5.4 What it must NOT become

No DMs, no channels sprawl, no emoji-reaction theatre, no presence
noise, no "someone is typing" pressure. If a message isn't about an
operational object or a decision, it doesn't belong.

---

## 6. PAS Brain visibility

PAS Brain is how PAS proves it is *adaptive* and *queryable*. Today it
is invisible; the plan gives it three surfaces.

| Surface | What it shows |
|---|---|
| **Command Center insight strip** | One calm strip near the top: "PAS has learned 3 patterns this week" + the single most useful current insight, with an evidence link. |
| **PAS Brain module/panel** | A dedicated surface listing memory candidates, learned signals, and example queries. |
| **Inline confidence labels** | Wherever PAS asserts something, a small confidence label (e.g. *observed · likely · uncertain*) + evidence source. |

PAS Brain content types:

- **Memory candidates** — things PAS noticed that *could* become durable
  memory, pending human confirmation ("Agents on the Riverside demo team
  return Zillow leads faster on Tuesdays — remember this?").
- **Learned signals** — patterns PAS already tracks (callback-keeping
  rate, objection frequency).
- **Query examples** — seeded prompts that show what PAS can answer.
- **Confidence labels** — every claim is graded, never absolute.
- **Evidence sources** — each memory/signal links to its receipts.
- **What PAS knows / does not know yet** — an explicit "edge of
  knowledge" list. Honesty is a trust feature.

All Brain content is demo-only and labelled; "memory" here is seeded
fictional data, not learned from real activity.

---

## 7. Operational demo data model

Typed, **frontend-only** demo objects. No network, no persistence beyond
in-memory/build-time constants. Every object carries
`demoOnly: true` and `noLiveBehavior: true`.

### 7.1 Naming convention (fictional-only)

- Brokerage: **"Northwind Realty (DEMO)"** — obviously fictional.
- People: role-tagged demo names, e.g. **"Demo Agent · Riverside Team"**,
  **"Demo Owner · Northwind"**. No names implying real clients.
- Leads/objects: opaque demo IDs, e.g. **`Lead D-1042 (simulated)`**.
- Every list view shows a "Simulated data" chip.

### 7.2 Object catalogue (shape sketches, not final code)

```
Agent           { id, name(demoLabelled), role, responseSpeedMs, callbacksOwned,
                  activeLeads, coverageStatus, coachingFlags[], permissions:RoleBundle }
User            { id, name(demoLabelled), email(demo), role, status }
Role            'BrokerOwner'|'Admin'|'TeamLead'|'Agent'|'Viewer'|'ORVNInternalAdmin'
Permission      { key, label, allowed:boolean }      // simple toggle, not RBAC matrix
RoleBundle      { role:Role, permissions:Permission[] }
Lead            { id, source, owner:Agent, stage, lastTouch, riskLevel, nextAction, pasNote }
Call            { id, lead, outcome, transcriptPreview, objection, sentiment, evidenceRefs[], nextAction }
Callback        { id, promisedAt, dueAt, owner:Agent, sourceCall:Call, status, riskLevel, proposedRecovery }
Booking         { id, sourceLead:Lead, agent:Agent, status, evidenceRefs[], calendarState }
PipelineRisk    { id, severity, reason, affectedLeads:Lead[], suggestedRecovery }
Recommendation  { id, title, evidenceRefs[], urgency, impact, possibleAction }
ActionProposal  { id, title, scope, expiresAt, evidenceRefs[], actionPreview, auditLanguage, status }
EvidenceSignal  { id, kind, source('call'|'signal'|'recommendation'|'proposal'), summary, link }
Integration     { id, name, category, status, readScope[], writeScope[], health, setupSteps[], lastSync }
MemoryCandidate { id, statement, confidence('observed'|'likely'|'uncertain'), evidenceRefs[], status }
Notification    { id, severity, title, body, module, ts, isRead, isDemoLabelled }
NotificationReply { id, notificationId, text, capturedAt, demoOnly:true }   // local-only
RoomMessage     { id, authorType('human'|'pas'), author, type, body, evidenceRefs[], ts }
ObjectThread    { id, objectType, objectId, messages:RoomMessage[] }
```

These types are the **single source of demo truth** for every module
upgrade below — Step A builds them once; later steps consume them.

---

## 8. Module upgrades

Every module must answer the **five operational questions** (§11):
*what is happening · why it matters · what PAS suggests · what evidence
supports it · who needs to act.*

**Command Center** — the operating home: attention queue · PAS Brain
insight strip · open proposals · overdue commitments · system health ·
team communication preview (latest PAS Room activity).

**Leads** — list/table/cards of leads: source · owner · stage · last
touch · risk · next action · PAS note. Row → lead thread + evidence.

**Calls** — call records: outcome · transcript preview · objection ·
sentiment · evidence · next action.

**Callbacks** — *flagship module:* promised callback · due time · owner ·
source call · status · risk · PAS-proposed recovery. This is where
"PAS watches commitments" is most felt.

**Bookings** — appointments: source lead · assigned agent · status ·
evidence · calendar state.

**Pipeline Risks** — risk cards: severity · reason · affected leads ·
suggested recovery.

**Recommendations** — cards: evidence · urgency · impact · possible
action.

**Action Proposals** — bounded proposals with **approve/decline
demo-only** behaviour: expiry · scope · evidence · action preview ·
audit language. *(This is the frontend surface PAS209's backend will
later feed — §10 Step D/I notes the seam; no wiring in this arc.)*

**Evidence Digest** — receipts linked to calls, signals,
recommendations, proposals.

**Simulation Lab** — scenario cards · rehearsal runs · outcome
comparisons.

**Integrations** — interactive **marketplace** + **detail drawer** (demo
mode):

| Category | Demo connectors |
|---|---|
| CRM | Follow Up Boss, Lofty, kvCORE, HubSpot, Salesforce |
| Lead sources | Zillow, Realtor.com, Facebook Lead Ads, Website Forms |
| Calendar/booking | Google Calendar, Cal.com |
| Communication | Gmail, Slack, Twilio |
| Workspace | Google Sheets, Notion |

Each card shows status · read scope · write scope · health · setup
steps · last sync. Click → integration detail drawer (demo-only; no
OAuth, no network). **Read scope is always presented before write
scope**; write scope is described as approval-gated and not active.

**Settings** — workspace profile · members · roles & permissions ·
notification rules · approval policies · quiet hours · PAS
behaviour/tone/disclosure settings · **sign-out / account area (shell
only)**.

**Agents** — *new `/agents` route + nav entry:* per-agent response speed
· callbacks owned · active leads · coverage status · coaching flags ·
permissions (role bundle).

**Permissions** — simple **role bundles, not a complex RBAC matrix**:
Broker Owner · Admin/Ops Manager · Team Lead · Agent · Viewer · ORVN
Internal Admin. Built-in bundles with simple toggles. Display-only in
this arc; backend-validated enforcement remains sequence Step 18.

**Auth/account** — sign-in/sign-out is **future implementation**. This
arc shows the **account menu shell** only (avatar → menu with
profile/role/sign-out items that are inert in demo). No real auth.

---

## 9. Notification reply behaviour

Preferred: **allow local demo reply.**

- The reply field accepts text and a submit.
- On submit, show the confirmation:
  **"PAS captured this instruction in demo mode. No live action was
  taken."**
- The reply is stored as a local `NotificationReply` object (in-memory
  only). **No backend call. No mutation. No persistence across reload.**

This converts a dead placeholder into a felt interaction while staying
strictly demo-safe.

---

## 10. Implementation sequence (safe PRs)

Each letter is its own PR, each self-contained and demo-safe. Order is
dependency-driven: the data model first, then surfaces that consume it.

| PR | Scope | Depends on |
|---|---|---|
| **A** | Demo data model (§7) — typed objects, fictional seed data, labels. | — |
| **B** | Agents route + nav entry. | A |
| **C** | Integrations marketplace + detail drawer (demo). | A |
| **D** | Leads / Calls / Callbacks operational modules. | A |
| **E** | Settings: roles/permissions + account shell. | A |
| **F** | PAS Brain surface (insight strip + module + confidence labels). | A |
| **G** | PAS Room + in-app communication shell (Room + object threads). | A, D |
| **H** | Notification local demo replies (§9). | A |
| **I** | Command Center refinement — pull A–H together into the operating home. | A–H |

Each PR ends green on `pnpm build` and `compileall`, carries demo
labels, and adds no network behaviour. The PAS209 frontend seam (an
Action Proposals surface fed by real backend) is **out of this arc** —
it begins at sequence Step 14/19, after CORS (Step 13) and the
read-only surface integration.

---

## 11. Design rules

- **White mode**, mature, calm, operational.
- No AI-SaaS gimmicks. No gradients-as-personality. No emoji confetti.
- **No Slack clone. No CRM clone.**
- No excessive explanatory copy — **more operational objects, fewer
  paragraphs.**
- Every section must answer, in this order:
  1. **What is happening?**
  2. **Why does it matter?**
  3. **What does PAS suggest?**
  4. **What evidence supports it?**
  5. **Who needs to act?**

If a surface cannot answer those five, it is not ready.

---

## 12. Safety rules (non-negotiable, every PR)

- All demo data clearly labelled (`demoOnly` + visible "Simulated"
  chips + DemoBanner).
- No live action, no API calls, no hidden network behaviour.
- No production claims.
- Approval/assignment language always says **demo-only** until backend
  integration lands.
- "PAS has not changed live customer behavior." disclaimer stays on
  every surface that shows operational objects.
- No real or real-sounding client names — fictional demo data only.

---

## 13. Major decisions captured

1. **Communication is welded to work**, not a separate chat product —
   PAS Room (brokerage-wide) + object threads (per lead/callback/etc.),
   small typed message vocabulary, queryable as company memory.
2. **PAS Brain gets three surfaces** (insight strip, module, inline
   confidence) so "queryable + adaptive" becomes visible, with an
   explicit "what PAS does not know yet."
3. **One demo data model first (PR A)**; every module upgrade consumes
   it — no per-module ad-hoc data.
4. **Agents and Permissions become first-class** but permissions stay
   *simple role bundles*, not an RBAC matrix.
5. **Auth is shell-only** this arc; real sign-in is sequence Step 17.
6. **Notification replies become locally interactive** with an explicit
   demo-only confirmation — no backend.
7. **Callbacks is the flagship** module — it's where "PAS watches
   commitments" is most tangible.
8. **PAS209 stays backend-only** in this arc; its frontend surface is a
   later, separately-sequenced step.

---

---

## 14. PR A implementation note (2026-05-30)

**PR A — typed operational demo data model — created.** Branch
`pas-web-demo-data-model`.

- Location: `web/lib/demo/operational/` — `types.ts` (interfaces +
  closed vocabularies + `DEMO_META`), `assertions.ts` (safety helpers),
  one file per collection (agents, permissions/users, leads, calls,
  callbacks, bookings, risks, recommendations, proposals, evidence,
  integrations, brain, communication), and an `index.ts` barrel with a
  `DEMO_DATA_MODEL` sanity summary.
- **No UI** was built. No routes/components changed. No backend, CORS,
  API, auth, Supabase, mutations, or secrets.
- Every exported demo object carries `demoOnly: true` +
  `noLiveBehavior: true`; all data is clearly fictional ("Northwind
  Realty (DEMO)", `Lead D-1042 (simulated)`, `*.local`/`example.invalid`
  emails, no phone numbers).
- **All later modules (PRs B–I) consume this model** — they import demo
  data from `web/lib/demo/operational`, never define their own.

---

## 15. PR B implementation note (2026-05-30)

**PR B — Agents operational demo route — created.** Branch
`pas-web-agents-route`.

- New route `/agents` under the **People** family (the family now appears
  in the sidebar). Registry: `web/lib/navigation/routes.ts` —
  `status: "operational-demo"`, `demoOnly: true`, `noLiveBehavior: true`,
  gated (display-only) on a new `view_agents` permission granted to
  Broker Owner, Admin/Ops, Team Lead, ORVN Internal Admin (not Agent,
  not Viewer) in `web/lib/session/demoSession.ts`.
- UI: `web/app/agents/` + `web/components/modules/agents/`
  (`AgentsOverview`, `AgentCard`, `AgentCoveragePanel`,
  `AgentSignalsPanel`). All static RSC — no client JS, no network.
- Consumes the PR A model: `DEMO_AGENTS`, `DEMO_USERS`, `DEMO_CALLBACKS`,
  `DEMO_CALLS`, `DEMO_LEADS`. Signals are **derived from the data**, not
  hardcoded.
- Answers: who is available · who owns follow-up · where coverage is
  weak · which agents need attention · what PAS recommends watching.
- Demo/rehearsal labels preserved (demo pill, rehearsal note,
  "PAS has not changed live customer behavior."). No backend, CORS, API,
  auth enforcement, Supabase, mutations, or secrets.

---

## 16. PR C implementation note (2026-05-30)

**PR C — Integrations marketplace + detail drawer — created.** Branch
`pas-web-integrations-marketplace`.

- `/integrations` upgraded from the explanatory skeleton to an
  operational demo marketplace. Registry status →
  `"operational-demo"`. Route stays in the System family with the
  existing `manage_integrations` gate.
- UI: `web/app/integrations/` + `web/components/modules/integrations/`
  (`IntegrationsOverview` [client — drawer state only], `IntegrationCard`,
  `IntegrationDetailDrawer` [client — ESC/focus-trap/scroll-lock],
  `IntegrationHealthPanel`, `IntegrationSetupSteps`, and a `meta.ts`
  label/format helper).
- Consumes `DEMO_INTEGRATIONS` (PR A) only — categories CRM, Lead
  source, Calendar/booking, Communication, Workspace; 16 connectors.
  Read scope is always shown before write scope; writes are labelled
  "approval required".
- Detail drawer is demo-only: status, health, read/write scopes, setup
  steps, permissions requested, last sync, connection notes, and an
  explicit "No OAuth flow has started" warning. Action buttons are
  inert/disabled.
- **No OAuth, no `fetch()`, no API, no CORS, no backend, no auth, no
  Supabase, no mutations, no secrets.** Demo/rehearsal labels preserved.

---

## 17. PR D implementation note (2026-05-30)

**PR D — Leads / Calls / Callbacks operational demos — created.** Branch
`pas-web-leads-calls-callbacks-demo`.

- `/leads`, `/calls`, `/callbacks` upgraded from skeletons to operational
  demo modules. Registry status → `"operational-demo"` for all three.
- Shared layer: `web/components/modules/continuity/` — `ContinuityHeader`,
  `ContinuityMetricStrip`, `OperationalRecordCard`, `EvidenceMiniList`,
  `OwnershipBadge`, `RiskChip`, a `severity.ts` helper, and one shared
  `continuity.module.css`.
- Modules: `web/components/modules/{leads,calls,callbacks}/`. **Callbacks
  is the flagship** — a top "Commitment Watch" section (overdue · due
  soon · at risk · recovery proposed) plus per-callback recovery
  proposals and evidence receipts.
- Relations resolved from the model by id: callbacks/calls per lead,
  owner via `agentId`, evidence via `evidenceIds` (and id-mention match),
  recovery proposal via callback-id mention, call→callback via
  `sourceCallId`. No per-component fabricated records.
- All static RSC. Demo/rehearsal labels preserved. **No backend, CORS,
  API, `fetch()`, auth, Supabase, mutations, calling/SMS/email, or
  secrets.** Severity is never colour alone (rail + chip + text).

---

## 18. PR E implementation note (2026-05-30)

**PR E — Settings controls + account shell — created.** Branch
`pas-web-settings-controls-demo`.

- `/settings` upgraded from skeleton to a calm trust-controls surface.
  Registry status → `"operational-demo"`.
- UI: `web/app/settings/` + `web/components/modules/settings/` —
  `SettingsOverview` + panels: `WorkspaceProfilePanel`,
  `AccountShellPanel`, `MembersPanel`, `RolePermissionsPanel`,
  `ApprovalPolicyPanel`, `NotificationRulesPanel`, `PasBehaviorPanel`
  (one shared `SettingsOverview.module.css`). All static RSC.
- Consumes `ROLE_BUNDLES`, `DEMO_USERS`, `DEMO_AGENTS`,
  `DEMO_INTEGRATIONS` (write-enabled count), and `DEMO_SESSION`
  (account/workspace). Approval-policy / notification-rule / PAS-behavior
  copy is local UI policy text, clearly demo-only.
- Roles shown as **six simple bundle cards** (purpose · permission count
  · can / cannot) — no RBAC matrix. Account shell shows the demo
  session with an **inert, disabled sign-out** ("Sign out connects when
  real authentication is enabled.").
- **No real auth, no login flow, no real sign-out, no `fetch()`, no API,
  no CORS, no backend, no Supabase, no mutations, no secrets.** Demo
  labels preserved; severity never colour-alone.

---

*End of plan. No code, no backend, no live behaviour — plan only.*
