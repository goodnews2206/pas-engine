# PAS Frontend Foundation Plan

> Status: draft v1. Owner: ORVN Labs. Last updated: 2026-05-25.
> Sibling to `docs/pas_uiux_reference_study.md` and
> `docs/pas_design_system_definition.md`. Defines the *shape* of the
> frontend before any implementation. **No frontend code yet.**

## 0. Scope

This document defines:

- the architecture philosophy for the web app,
- the shell + routing + state boundaries,
- where PAS communication and notifications mount globally,
- how the app behaves on mobile / tablet / desktop / future native,
- the order of implementation work.

It does **not** pick concrete dependency versions, file paths, or
component code. Those are downstream decisions that ship in v1.x once
this foundation is approved.

---

## 1. Frontend architecture philosophy

### 1.1 The shape of the system

The frontend is a **thin, opinionated view over the PAS API**. The
truth lives in the backend; the frontend renders, interprets user
intent, and routes intent back to the API. Five rules:

1. **Server is source of truth.** Every business value comes from
   the API. UI never invents data; it presents and queries.
2. **No business logic in the UI.** Validation echoes the API;
   permission gating echoes the API. UI cannot be more permissive
   than the server.
3. **Single API surface.** All reads/writes go through the PAS API,
   never to external integrations directly from the browser.
4. **Streaming-friendly by default.** PAS replies, audit feeds, and
   notification deliveries arrive incrementally. The UI is built to
   stream from day one.
5. **Stateless components, declarative state.** State is named,
   scoped, and observable; nothing lives in implicit DOM order.

### 1.2 Framework choice (intent, not commitment)

- **Likely:** Next.js (React, App Router) for routing + SSR
  affordances + first-class streaming, deployed on Vercel.
- **Acceptable alternatives:** Remix, SvelteKit (only if the
  ecosystem investment is justified).
- **Out of scope for v1:** plain SPAs without routing affordances,
  framework-less stacks.

The architecture below is framework-agnostic; the concrete dep
choice lands in the foundation PR.

### 1.3 What we will not do

- **No global Redux-style store.** Server state via a fetch-cache
  layer; UI state local to where it lives.
- **No CSS-in-JS for runtime styling.** Tokens compile to CSS
  variables or Tailwind preset.
- **No re-implementing the design system inline.** Every visible
  treatment is a token from `docs/pas_design_system_definition.md`.
- **No premature micro-frontends.** One app, one shell, one router.

---

## 2. App shell structure

The shell is the persistent skeleton inside which every module
renders. Five regions:

```
┌──────────────────────────────────────────────────────────┐
│  Top bar                                                 │
│  (tenant strip · command bar · presence · bell · profile)│
├──────────┬───────────────────────────────────────────────┤
│          │                                               │
│ Sidebar  │              Module main                      │
│          │                                               │
│ (modules │   (the active route's content)                │
│  by role)│                                               │
│          ├───────────────────────────────────────────────┤
│          │  PAS composer (persistent, dockable)          │
└──────────┴───────────────────────────────────────────────┘

Overlay region (peek pane · inspector · approval drawer · modals)
mounts on top of the shell, anchored right (panels) or center (modal).
```

### 2.1 Region responsibilities

| Region | Responsibility |
|---|---|
| Top bar | Tenant + scope context, global command, presence, notifications, profile. |
| Sidebar | Role-shaped module list with families (Operate / Notice / People / System / ORVN). |
| Module main | Route-driven content. The only region that changes on navigation. |
| PAS composer | Persistent intent surface. Always present. |
| Overlay | Stacked panels (peek > inspector > approval drawer > modal). Esc walks the stack. |

### 2.2 Shell invariants

- The shell **never** unmounts on route change.
- The composer **never** unmounts.
- The top bar's tenant strip and presence indicator are reactive,
  not cached on page load.
- Sidebar items appear or disappear only when the role bundle
  changes; no client-side flicker on initial route render.

---

## 3. Responsive layout structure

Breakpoints (from Design System §20): **375 / 768 / 1024 / 1440**.

| Width | Layout |
|---|---|
| ≤767 | Single-column. Sidebar replaced by bottom tab bar + "More" sheet. PAS composer pinned above tab bar. Overlay panels take over full screen. |
| 768–1023 | Two-column where useful (e.g. list + detail). Sidebar collapsed by default; expandable. Overlay drawers retain 480 px max width. |
| 1024–1439 | Full sidebar + main + optional peek. Overlay stacks: peek behind inspector behind approval drawer. |
| ≥1440 | Full sidebar + main + peek + inspector concurrently. Overlay approval drawer stacks above. |

Responsive switches are CSS-driven; no JS branching for layout
selection. JS only kicks in for behavioural differences (e.g.
swipe-to-close on mobile drawers).

---

## 4. Route structure

Routes mirror the Dashboard Information Architecture's module
families. Top-level shape:

```
/                                    → redirect → /command-center
/command-center
/leads                               → /leads/:id (inspector)
/calls                               → /calls/:id (inspector)
/callbacks                           → /callbacks/:id
/bookings                            → /bookings/:id
/agents                              → /agents/:id
/proactive
  /observer
  /recommendations                   → /:id (drawer)
  /action-proposals                  → /:id (drawer)
  /pipeline-risks
  /evidence-digest                   → /:id
/people
  /communications                    → /thread/:id
  /notifications
/system
  /integrations                      → /:connector
  /pas-brain                         → /:entry
  /audit                             → /:event
  /settings
  /billing                           → owner-only
  /simulation-lab                    → /:scenario
/orvn                                → role-gated
  /tenants                           → /:id
  /incidents                         → /:id
```

### 4.1 Route rules

- **Inspectors are overlays, not routes.** Opening a row updates a
  query string (`?inspect=<id>`) but does not push a new route — the
  back button collapses the inspector first.
- **Drawers (approvals) push to the URL.** Approving from any
  surface routes to `?approve=<proposal-id>`; deep-linkable.
- **Threads have their own route.** PAS conversation threads are
  shareable inside the workspace.
- **Role gating happens at the route layer.** A non-Owner hitting
  `/system/billing` gets a 403 surface — not a hidden redirect.

### 4.2 Tenant + scope routing

- Tenant is **path-implicit** via auth context (not in the URL by
  default). ORVN routes carry `?tenant=<slug>` when impersonating.
- Scope (Team Lead viewing a specific team) carries in `?scope=` and
  shows the scope strip below the top bar.

---

## 5. State boundaries

Four kinds of state, with explicit boundaries:

| Kind | Owner | Lifetime | Examples |
|---|---|---|---|
| **Server state** | Fetch cache (e.g. TanStack Query, SWR, RSC fetch). | Until invalidated by mutation or revalidation rule. | Leads list, call records, recommendations, audit entries. |
| **UI state** | Component-local. | Until the component unmounts. | Sort order, filter chips, inspector open/closed. |
| **Session state** | Shell-level. Persists across routes. | Until sign-out. | Active tenant, role, density preference, sidebar collapse. |
| **Realtime state** | Realtime subscription layer (websocket / SSE). | While the connection is alive. | Presence, "PAS is thinking", new notifications, audit feed. |

Rules:
- **No cross-kind leakage.** UI state never persists across routes
  unless promoted to session state with an explicit reason.
- **Server state is never duplicated.** A single fetch-cache entry
  is the truth; components subscribe to it.
- **Optimistic updates** are allowed only when the API returns the
  authoritative value within the response.

---

## 6. Streaming responses

PAS speaks. Streaming is a first-class concern, not a polish item.

### 6.1 Where streaming appears

- **PAS composer thread.** Token-level append while PAS is replying.
- **Peek pane.** Same stream as the composer, presented in the
  full-thread shape.
- **Evidence digest expansion.** When PAS expands an evidence
  request inline, the embedded section streams in.
- **Audit feed live mode.** Optional live tail (off by default) for
  ORVN debugging.

### 6.2 Streaming rules

- **Stream into a placeholder.** The container exists before tokens
  arrive — no layout jitter on first token.
- **Backpressure.** If the user is mid-input while PAS is streaming
  a reply, the user's input is preserved; PAS's tokens flow to the
  preceding bubble.
- **Cancel.** Every streaming response has an explicit cancel
  affordance (Esc on the composer; "Stop" button on peek/full).
- **Reduced motion.** With `prefers-reduced-motion: reduce`, tokens
  arrive in larger chunks (every ~80 ms) without per-character fade.

---

## 7. PAS communication global mount

The PAS composer mounts inside the shell, beneath the module main,
above the bottom edge. **One instance** for the whole app, never
duplicated per route.

### 7.1 Mount contract

- The composer subscribes to the **PAS thread service** which holds
  the current thread, history, and presence.
- Opening peek pane on a thread does not create a second composer —
  the peek pane mirrors the same thread, anchored to the right.
- The full-thread route mounts a third view of the same thread; the
  three surfaces (composer, peek, full) are always synced.

### 7.2 Cross-module behaviour

- Asking PAS to "show today's callbacks" inside the composer
  triggers an inline section render *in the thread*, not a
  navigation. The user stays on the current module.
- If the user explicitly clicks a result, *then* navigation happens
  via the same shell router as the sidebar.

---

## 8. Notifications global mount

A single **notification service** runs inside the shell. It receives
the realtime stream and exposes:

- the **bell badge** (top bar),
- the **bell drawer** (right side, severity-grouped),
- the **toast region** (top-right; reserved for Urgent +
  Approval Required severities, deliberately rare),
- the **persistent banner region** (top of the module main; Critical
  only).

### 8.1 Mount rules

- One service for the whole app. Components subscribe; nobody
  re-subscribes per route.
- **Toasts are confirmation, not interruption.** Toasts auto-dismiss
  after 4 s for FYI/confirmation, and persist for Urgent until
  acknowledged.
- **Critical never toasts.** It banners and pushes.
- The toast queue is single-file — no stacked toasts.

---

## 9. Mobile shell behaviour

- **Bottom tab bar** (max 5 items, role-shaped per Dashboard IA
  §9.1).
- **Composer pinned above the tab bar.** Expanding it overlays the
  module main; collapsing returns.
- **Sidebar replaced by a "More" sheet** that lists every module
  the role has, grouped by family.
- **Approval drawer** takes over the full screen on mobile (no
  side-by-side with main).
- **Inspector** behaves like a route — back button closes inspector
  before navigating.

---

## 10. Tablet behaviour (768–1023)

- **Sidebar collapsed by default**, expandable to the desktop
  treatment.
- **Two-column module layouts** where useful (list + detail).
- **Peek pane allowed** but at 320 px (reduced from 360); if peek +
  inspector both open, inspector replaces peek.
- **Composer expanded height** capped at 160 px to preserve module
  surface.

---

## 11. Desktop behaviour (1024+)

- **Full shell**: sidebar (expanded if ≥1280), main, composer,
  peek when active, inspector when active, approval drawer when
  invoked.
- **Multi-monitor friendly**: routes are stable on reload; deep
  links recreate the inspector / approval drawer state.
- **Keyboard-first**: Cmd/Ctrl+K command bar, single-letter module
  jumps optional (defer to v1.x).

---

## 12. Future desktop-app possibility

- **Out of scope for v1.** The product survives without it.
- **Architecture preserves the path.** A future Tauri / Electron
  shell wraps the same web app; no special browser-only APIs.
- **Notifications.** A native shell unlocks native notifications and
  reliable background presence — both pre-defined in the
  Notification Architecture; the desktop wrapper only changes the
  delivery channel.
- **Decision trigger:** add when ≥3 brokerages ask for it
  explicitly, or when the realtime channel meaningfully benefits
  from native sockets.

---

## 13. Future realtime layer

Realtime is a v1 requirement for *some* surfaces:

| Surface | Realtime need |
|---|---|
| PAS thinking presence | Required v1. |
| New notification arrival | Required v1. |
| Critical banner reveal | Required v1. |
| Audit live tail | Optional v1; default v1.x. |
| Presence (user online) | v1.x. |
| Action proposal expiry countdown | Required v1; client clock with periodic server reconcile. |

### 13.1 Transport

- **Server-sent events (SSE) preferred** for v1: one-way, simple,
  HTTP-native, cache-friendly on Vercel-style edges.
- **WebSocket** retained for v1.x where bidirectional is needed
  (presence push from client back to server).
- **Reconnect strategy:** exponential backoff with a visible
  "reconnecting…" presence chip.

### 13.2 Realtime invariants

- Realtime **must not contain authority decisions.** A realtime
  message that says "the proposal was approved" is an event; the
  source of truth is the API response, which the realtime layer
  echoes.
- Realtime is **best-effort.** UI degrades to poll if the stream
  is unhealthy; presence shows "Realtime degraded".

---

## 14. Frontend implementation sequence

Mirrors Product Design Book §10 and §11, with explicit shell-first
ordering. Each step is its own PR.

1. **Repo + tooling foundation.** Framework, package manager,
   linter, formatter, type checking, CI hook. No business code.
2. **Design tokens.** Compiled from
   `docs/pas_design_system_definition.md` — typography, spacing,
   radius, elevation, animation, severity, demo tokens. No
   components yet.
3. **App shell.** Top bar (chrome only), sidebar (chrome only),
   composer (chrome only), main slot, overlay region. No routes
   yet.
4. **Routing skeleton.** All routes mounted with placeholder
   "Coming soon" content. Role gating wired at the route layer.
5. **Auth + tenant context.** Sign-in, tenant strip, role bundle
   resolution, sign-out.
6. **PAS communication shell.** Composer + peek + full thread,
   wired to a mock stream first, then to the real PAS API. Inline
   section embed mechanism (mock first).
7. **Notification shell.** Bell, drawer, toast region, persistent
   banner region. Mock event stream first.
8. **PAS205–PAS208 read-only surfaces.** Proactive Observer,
   Recommendations, Evidence Digest, Action Proposals (read-only
   first).
9. **Operate-family modules.** Command Center first, then Leads /
   Calls / Callbacks / Bookings / Agents.
10. **Integrations framework.** Connector list, connect flow,
    health card. Read scopes only.
11. **Realtime layer (v1 scope).** PAS thinking presence,
    notification arrivals, Critical banner.
12. **Approval flows end-to-end.** Approval drawer wired to
    Action Proposals; mutation gated through the API; audit
    emission.
13. **Mobile polish pass.** Bottom tab bar, "More" sheet, drawer
    full-screen behaviour, composer pinned.
14. **Dark theme + density polish.** Token-only changes; visual QA.
15. **Pre-delivery checklist sweep** (Design System §29) against
    every shipped surface.

---

## 15. Performance + observability contract

- **First meaningful paint ≤1.5 s** on a cold load to Command
  Center (assumes warm cache; cold-CDN budget is 2.5 s).
- **Route transitions ≤200 ms** to first content (skeleton allowed).
- **Streaming first-token ≤500 ms** when PAS is healthy.
- **No layout shift** during streaming or skeleton-to-content
  transitions.
- **Error rates surfaced** to the user via the notification system
  when an API call fails repeatedly; transient errors retry
  silently up to a small bound.
- **Client telemetry is opt-in** per tenant; ORVN sees aggregate
  metrics, never per-user tracking.

---

## 16. Frontend foundation invariants (checklist)

The frontend is correctly founded only if every one of these holds:

1. The shell never unmounts on navigation.
2. PAS communication is reachable from every dashboard page via
   the persistent composer.
3. Server state is the single source of truth; no client-side
   business logic.
4. UI cannot offer an action the API would reject.
5. Routes are role-gated at the route layer, not just visually.
6. Streaming is first-class — composer + peek + full thread share
   the same stream.
7. Notification service runs in exactly one instance per session.
8. Toasts are rare; banners are rarer; bell is the default surface.
9. Mobile preserves every module the role has on desktop.
10. Every shipped surface passes the pre-delivery checklist
    (Design System §29).

---

## 17. Open frontend questions

- **Framework commitment.** Next.js looks right; final commit lands
  with the foundation PR.
- **Server components vs client components** split — what runs
  where for streaming + auth context?
- **Auth provider.** First-party vs Clerk / Auth0 / Supabase Auth.
- **Multi-tenant routing.** Path-implicit via session is simpler;
  path-explicit (`/t/<slug>/…`) is shareable but verbose. Decide
  before route lock-in.
- **Realtime transport at scale.** SSE works for v1; do we need a
  socket service tier (e.g. Pusher, Ably, self-host) for v1.x?
- **i18n.** v1 is English-only; structurally ready for i18n is
  cheap if planned now and expensive if retrofitted.
- **Telemetry vendor.** PostHog / Mixpanel / Segment / self-host;
  privacy and tenant-isolation constraints.

---

*End of v1.*
