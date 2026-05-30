# PAS Web Foundation v1

> Status: shipped (Steps 1–11). Owner: ORVN Labs. Sequence reconciled
> 2026-05-30. Next pending step: 12 (Vercel deployment — **not yet
> executed**).
>
> **This document is the authoritative implementation log of record.**
> The numbered sequence here is canonical;
> `docs/pas_frontend_foundation_plan.md §14` has been reconciled to
> match it. If the two ever diverge again, this log wins.
>
> Step 1+2 branch: `pas-web-foundation-v1` (merged to main 2026-05-25).
> Step 3 branch: `pas-web-app-shell-chrome` (merged to main 2026-05-25).
> Step 4 branch: `pas-web-route-skeletons` (merged).
> Step 5 branch: `pas-web-session-permission-scaffold` (merged).
> Step 6 branch: `pas-web-composer-shell` (merged).
> Step 7 branch: `pas-web-notification-presence-shell` (merged).
> Step 8 branch: `pas-web-command-center-layout` (merged).
> Step 9 branch: `pas-web-module-empty-states` (merged).
> Step 10 branch: `pas-web-vercel-deployment-prep` (merged, PR #39).
> Step 11 branch: `pas-web-api-boundary-scaffold` (merged, PR #42).

## What this is

Step 1 of the PAS frontend implementation sequence
(`docs/pas_frontend_foundation_plan.md §14`).

This step establishes the isolated Next.js project under `/web/` with
zero business logic. It proves the toolchain works and compiles the
design system tokens into CSS custom properties before any component
or route is built.

---

## What was created

```
web/
├── .gitignore              Next.js-specific ignores (node_modules, .next, env files)
├── package.json            Dependencies: Next.js ^15, React ^19, TypeScript ^5
├── tsconfig.json           Strict TypeScript, App Router + bundler module resolution
├── next.config.ts          Minimal config; no rewrites yet (API wiring is a later step)
└── app/
    ├── globals.css         Design system token scaffold (all §1–§28 of design system)
    ├── layout.tsx          Root layout — Inter + JetBrains Mono via next/font/google
    ├── page.module.css     Homepage styles (tokens only, no ad-hoc values)
    └── page.tsx            Homepage placeholder
```

---

## Framework choices

| Decision | Choice | Reason |
|---|---|---|
| Framework | Next.js ^15, App Router | Streaming-first, RSC, route-layer role gating (`docs/pas_frontend_foundation_plan.md §1.2`) |
| Language | TypeScript, strict | Type safety from day one |
| Package manager | pnpm | Fast, deterministic |
| Fonts | Inter (sans), JetBrains Mono | Design system §1.1; loaded via `next/font/google` (zero CLS) |
| Styling | CSS custom properties in `globals.css` | All token values in one file, no runtime CSS-in-JS, no Tailwind yet |
| UI kit | None | Not required for Step 1; design system is the source of truth |

---

## Design tokens compiled

Every structural token from `docs/pas_design_system_definition.md` is
in `web/app/globals.css`:

- §1 — Typography scale + families + weight scale
- §2 — Spacing (0 → 96 px) + module gutters
- §3 — Radius (none → pill)
- §5 — Shadows (soft, overlay)
- §6 — Animation durations + easings
- §8 — Grid max/min widths
- §9 §11 §16 — Shell dimensions (sidebar, topbar, composer)
- §10 — Panel widths (peek, inspector, approval, modal)
- §20 — Breakpoints (375 / 768 / 1024 / 1440)
- §22 — Colours (surfaces, ink, border, brand, severity signals, demo, roles)
- §28 — Density row heights
- §6 §21 — Reduced-motion override

Signature brand hex uses the legacy dashboard palette as a starting
point; final values confirmed in v1.x with design sign-off.

---

## Local dev

```bash
cd web
pnpm install
pnpm dev         # http://localhost:3000
```

## Build

```bash
cd web
pnpm build
pnpm start       # preview production build
```

## Type check (without building)

```bash
cd web
pnpm type-check
```

---

## Deployment (Vercel)

Connect the GitHub repo to a new Vercel project and set:

| Vercel setting | Value |
|---|---|
| Root directory | `web` |
| Framework preset | Next.js |
| Build command | `pnpm build` |
| Output directory | (Vercel auto-detects from Next.js) |

**Before the first deploy:** add the Vercel domain to `app/main.py`
`CORSMiddleware` allow-list. The domain is not known until the Vercel
project is created, so this is intentionally deferred.

---

## What is NOT here (by design)

- No auth — Step 5 of the implementation sequence
- No API calls — Step 6+; domain is unknown until Vercel project created
- No CORS change — dependent on Vercel domain
- No shell chrome (top bar, sidebar, composer) — Step 3
- No routes — Step 4
- No Tailwind — not required; CSS custom properties are sufficient for
  the token layer; revisit before component library starts
- No backend changes — `/web` is fully isolated from `/app`

---

## Step 3 — App shell chrome

`docs/pas_frontend_foundation_plan.md §14` Step 3: **App shell.**
Branch: `pas-web-app-shell-chrome`.

### Shell components created

```
web/components/shell/
├── Shell.tsx / Shell.module.css        Root frame: DemoBanner + Sidebar + main column
├── Sidebar.tsx / Sidebar.module.css    Left nav: wordmark, workspace, role, module groups
├── TopBar.tsx / TopBar.module.css      56 px header: title, search entry, bell, profile
├── TenantStrip.tsx / TenantStrip.module.css  Context strip + severity level indicators
├── DemoBanner.tsx / DemoBanner.module.css    Persistent amber rehearsal banner
└── Composer.tsx / Composer.module.css        Persistent bottom PAS composer
```

### Shell layout (desktop)

```
[DemoBanner — full width amber strip]
[Sidebar 256px] [TopBar 56px]
                [TenantStrip 36px — workspace context + severity levels]
                [Content — scrollable, gutter: 32px]
                  [CommandCenter placeholder cards]
                [Composer 56px — persistent PAS entry]
```

### Sidebar navigation

Three groups rendered for Broker Owner role. People family is hidden
because no People modules are active in the 12-module shell scope —
follows Dashboard IA §2.2: "Families with zero visible modules for a
role are hidden entirely."

| Group   | Modules |
|---------|---------|
| Operate | Command Center (active), Leads, Calls, Callbacks, Bookings |
| Notice  | Pipeline Risks, Recommendations, Action Proposals, Evidence Digest |
| System  | Simulation Lab, Integrations, Settings |

### Responsive behaviour

| Breakpoint | Sidebar | Top bar | Tenant strip |
|---|---|---|---|
| ≥1280 px | 256 px expanded, full labels | Full — title + search + bell | Full — all context + severity labels |
| 768–1279 px | 64 px collapsed, dot indicators only | Full | Severity dots only (labels hidden) |
| ≤767 px | Hidden | Condensed — title + bell only | Hidden |

### Command Center placeholder

Four static cards using empty-state copy from Product Design Book §4
and §8. Every card carries:
- A left-rail severity accent (3 px)
- A "Simulated" demo pill (Design System §26)
- Evidence hint in footer

| Card | Left rail | Copy source |
|---|---|---|
| Needs your attention | signal-attention | PAS Design Book §4.1 |
| PAS proposes | signal-approval | PAS Design Book §4.9 |
| Today's pipeline | border-strong | PAS Design Book §4.4 / §4.5 |
| System status | border-strong | PAS Design Book §8.6 |

A module-level rehearsal note sits above the grid per Dashboard IA §11:
"Rehearsal mode — these cards are simulated."

An "Ask PAS" prompt block below the cards follows Command Center §4.1
item 5.

### What is intentionally static / not implemented

- Sidebar collapse toggle — no JS interactivity yet
- Notification drawer — bell button present, drawer is Step 7
- Profile menu — avatar present, menu is Step 5 (auth)
- Composer send — input renders and accepts typing; no submit wired
- Search / command bar — input renders; Cmd+K and routing are Step 4
- Mobile bottom tab bar — sidebar hidden on mobile; tab bar is Step 13
- Card data — all cards use empty-state copy; real data lands in Step 9
- Peek pane / inspector / approval drawer — contextual panels land in Step 6+

### Tenant / workspace strip

Shows workspace context (left) and severity level labels (right).
On ≤1279 px, severity labels collapse to dots only.
On mobile (≤767 px), strip is hidden.

### Demo/rehearsal labelling

Demo tokens are immutable per Design System §26:
- DemoBanner: full-width amber strip, always visible above frame
- StatusChip in TopBar: "Demo / rehearsal" amber chip
- Module-level rehearsal note: inline above the card grid
- Per-card "Simulated" pills: on every card in every module

### Severity level indicators

5 severity levels displayed in TenantStrip (right-aligned):
FYI · Needs attention · Urgent · Approval required · Critical
Each paired with a colored dot (Design System §25 tokens).

---

---

## Step 4 — Role-aware route skeletons

`docs/pas_frontend_foundation_plan.md §14` Step 4: **Routing skeleton.**
Branch: `pas-web-route-skeletons`.

### Files created

```
web/lib/navigation/
└── routes.ts                   Frontend-only route registry (types, ROUTES[], helpers)

web/components/modules/
├── ModuleSkeleton.tsx           Reusable RSC: family chip, title, three info sections, disclaimer
└── ModuleSkeleton.module.css   Module skeleton styles

web/components/shell/
└── NavList.tsx                  Client component: pathname-aware active nav using route registry

web/app/
├── page.tsx                     Updated: redirect("/command-center")
├── command-center/page.tsx      Moved CC placeholder content here
├── command-center/page.module.css
├── leads/page.tsx
├── calls/page.tsx
├── callbacks/page.tsx
├── bookings/page.tsx
├── pipeline-risks/page.tsx
├── recommendations/page.tsx
├── action-proposals/page.tsx
├── evidence-digest/page.tsx
├── simulation-lab/page.tsx
├── integrations/page.tsx
└── settings/page.tsx
```

Sidebar.tsx was also updated to import `NavList` instead of the former
hardcoded `NAV` array.

### Route registry (`web/lib/navigation/routes.ts`)

Static TypeScript data layer. No backend dependency. No API calls.
Exports: `RouteDefinition`, `NavFamily`, `UserRole`, `NavGroup`,
`DEMO_ROLE`, `ROUTES`, `ROUTES_BY_ID`, `ROUTES_BY_HREF`,
`getRoutesForRole()`, `getNavGroupsForRole()`.

Every route carries:
- `id`, `label`, `href`, `family`
- `description` — one sentence of what the module surfaces
- `pasCan` — what PAS can do here once wired
- `notConnectedYet` — intentionally absent in this skeleton step
- `visibleTo` — list of roles that can see the module (display-only)
- `status: "skeleton"`, `demoOnly: true`, `noLiveBehavior: true`

### Route families

| Family  | Routes |
|---------|--------|
| Operate | Command Center (all roles), Leads (all), Calls (all), Callbacks (no Viewer), Bookings (all) |
| Notice  | Pipeline Risks (no Agent), Recommendations (no Agent), Action Proposals (Owner/Admin/TeamLead/ORVN), Evidence Digest (no Agent) |
| System  | Simulation Lab (no Agent/Viewer), Integrations (no Agent/Viewer), Settings (Owner/Admin/ORVN) |

People family is not in scope for v1 skeleton — omitted per Dashboard IA §2.2
(families with zero visible modules are hidden entirely).

### Role-aware navigation

`DEMO_ROLE = "Broker Owner"` is a compile-time constant in `routes.ts`.
`NavList.tsx` calls `getNavGroupsForRole(DEMO_ROLE)` and uses
`usePathname()` to set `aria-current="page"` and the `.active` CSS
class on the current route.

**This is display-only role shaping. It is NOT a security boundary.**
Real role resolution and permission gates are Step 5 (auth).

### ModuleSkeleton component

Each skeleton page passes its `RouteDefinition` to `<ModuleSkeleton />`.
The component renders:
1. Family chip + Demo/rehearsal chip
2. H1 module title
3. One-paragraph description
4. "What this module will show" section (`route.description`)
5. "What PAS can help with here" section (`route.pasCan`)
6. "Not yet connected" section (`route.notConnectedYet`)
7. Disclaimer: "PAS has not changed live customer behavior."

### Root redirect

`web/app/page.tsx` is now a one-line server-side redirect to
`/command-center` via `next/navigation`'s `redirect()`.

### What is intentionally static / not implemented

- No API calls — all data is static `RouteDefinition` objects
- No auth — `DEMO_ROLE` is a static constant; real session in Step 5
- No real module content — every page except `/command-center` renders
  `ModuleSkeleton` only
- No state management — zero client state added in this step
- No migrations, backend changes, or CORS changes

### Build result (pnpm build)

16 routes compiled, all static (`○`). First Load JS 102 kB shared.
TypeScript clean, no lint errors.

---

---

## Step 6 — PAS composer interaction shell

`docs/pas_frontend_foundation_plan.md §14` Step 6.
Branch: `pas-web-composer-shell`.

### Files updated

```
web/components/shell/Composer.tsx          Rewritten as "use client" interaction shell
web/components/shell/Composer.module.css   Rewritten to support all interaction states
```

### Composer interaction states

| Phase | Behavior |
|---|---|
| `idle` | Presence dot (FYI green) + placeholder text + 5 example prompt chips + session meta |
| `typing` | Input non-empty, send button enabled (brand blue), chips hidden |
| `thinking` | Textarea disabled, presence dot pulses amber at `--anim-presence` (1200ms), send disabled |
| `responded` | Response panel appears above input row with prompt echo, response text, disclaimer + dismiss button |

State is local React `useState` — no network, no state library, no persistence.

### Local-only behavior

Submit handler:
1. Captures prompt text
2. Clears textarea, resets height
3. Sets phase → `"thinking"` (1400ms `setTimeout`)
4. On timer: sets phase → `"responded"`

No fetch, no API call, no backend contact of any kind.

**Future PAS API connection point:** Replace the `setTimeout` in `handleSubmit`
with `fetch('/api/pas/ask', { method: 'POST', body: prompt })` in the API
wiring step. The state machine and UX are ready.

### Demo response

```
Here's what I can help with in this demo shell: pipeline risks,
recommendations, evidence, integrations, and approvals. Real operational
answers will connect through the PAS API later.

PAS has not changed live customer behavior.
```

The disclaimer is rendered in immutable demo tokens (amber, Design System §26).

### Prompt example chips

Five broker-human examples visible when composer is idle and empty:

- What needs attention?
- Which leads are slipping?
- What should I handle next?
- Show recommendations.
- Explain the simulation evidence.

Clicking a chip populates the textarea and focuses it. Chips disappear
when the user starts typing or while thinking/responded.

### Session display

Session meta row (below input, hidden on mobile) shows:
`{workspace.name} · {user.role} · {permissionBoundary} · Enter to ask · Shift+Enter for newline`

Derived from `DEMO_SESSION` — build-time constant, same as all shell components.

### UX principles met

- Embedded into the operating surface — not a floating bubble
- Premium calm — no bounce, no scale, no colour flash
- Thinking state: opacity-only pulse on the presence dot (stops under reduced-motion)
- Chips scroll horizontally on mobile rather than wrapping
- Session meta hidden on mobile to preserve input surface

### Accessibility

- Textarea: `aria-label="Message PAS"`, `aria-describedby="composer-hint"` (keyboard hints)
- Enter submits; Shift+Enter inserts newline (handled in `onKeyDown`)
- Send button: `aria-label="Send message to PAS"`, disabled when empty or thinking
- Dismiss button: `aria-label="Dismiss PAS response"`, visible focus ring
- Response panel: `role="status"` — screen readers announce on mount
- Presence indicator: `aria-label` updates to reflect thinking state
- All interactive elements have `:focus-visible` outlines (2px brand color)
- Thinking animation: `@media (prefers-reduced-motion: reduce)` stops the pulse

### What is intentionally not here

- No AI — no OpenAI, Anthropic, or backend call
- No persistent history — each submit is a single isolated interaction
- No streaming — full response appears after fixed 1400ms delay
- No multi-turn — dismiss resets to idle, no message thread
- No auth — session data is DEMO_SESSION (build-time constant)

---

---

## Step 7 — Notification + presence center shell

`docs/pas_frontend_foundation_plan.md §14` Step 7.
Branch: `pas-web-notification-presence-shell`.

### Files created

```
web/lib/notifications/
└── demoNotifications.ts        SeverityLevel type, DemoNotification interface, 15 demo items

web/components/notifications/
├── NotificationCenter.tsx       "use client" — bell + badge + open/close state
├── NotificationCenter.module.css
├── NotificationDrawer.tsx       "use client" — right-side slide-over / mobile bottom sheet
├── NotificationDrawer.module.css
├── NotificationCard.tsx         "use client" — single card with severity rail, chips, reply affordance
└── NotificationCard.module.css
```

### Files updated

```
web/components/shell/TopBar.tsx  Bell button replaced with <NotificationCenter />
```

### Severity model implemented

Five levels per `docs/pas_notification_architecture.md §2`:

| Level | Badge | Rail color | Chip color |
|---|---|---|---|
| FYI | No badge | `--signal-fyi` | `--signal-fyi` / `--signal-fyi-bg` |
| Needs attention | Yes | `--signal-attention` | `--signal-attention` / `--signal-attention-bg` |
| Urgent | Yes | `--signal-urgent` | `--signal-urgent` / `--signal-urgent-bg` |
| Approval required | Yes | `--signal-approval` | `--signal-approval` / `--signal-approval-bg` |
| Critical | Yes | `--signal-critical` | `--signal-critical` / `--signal-critical-bg` |

Severity is paired with: left-rail color + chip (color + icon + label) + group heading.
Never colour alone — each card uses three independent severity signals.

### Demo notification dataset

15 static notifications across all five severity levels:

| Count | Severity | Unread |
|---|---|---|
| 2 | Critical | 2 |
| 3 | Approval required | 2 |
| 3 | Urgent | 2 |
| 4 | Needs attention | 2 |
| 3 | FYI | 0 |

All notifications are `isDemoLabelled: true` and show a "Simulated" chip.

### NotificationCenter state

Local React `useState` only — no state library, no network, no persistence.

```typescript
const [isOpen, setIsOpen] = useState(false);
const [notifications, setNotifications] = useState<DemoNotification[]>(
  () => DEMO_NOTIFICATIONS
);
// badgeCount = unread non-FYI notifications (FYI does not badge per §3.1)
```

Read operations: `markRead(id)`, `markAllRead()` — both update local state only.

### Drawer interaction

- Right-side slide-over on desktop (420 px wide, `position: fixed`)
- Bottom sheet on mobile (100vw, 90dvh max, `translateY` animation)
- Opens: bell button click
- Closes: ESC key, overlay click, close button
- Focus trap: Tab cycles within the drawer while open
- Body scroll lock: `document.body.style.overflow = "hidden"` while open
- Enter/close animation: `transform` + `visibility` with `--anim-base` duration
- Reduced motion: `transition: none` via `@media (prefers-reduced-motion: reduce)`

### NotificationCard

Each card renders:
1. 3 px left rail (severity color via inline style)
2. Severity chip (icon + label) + "Simulated" demo chip
3. Relative timestamp (ISO absolute in `title` attribute for hover)
4. Mark-as-read button (unread dot, disappears once read)
5. Title + body text
6. Module tag + action link (navigates to relevant module)
7. Reply affordance placeholder (disabled textarea + send button — not wired)

### Grouping order

Drawer groups notifications by severity, ordered Critical → Approval required →
Urgent → Needs attention → FYI. Empty groups are omitted. Each group shows a
count badge.

### Empty state

When all notifications are marked read, the drawer body shows:
"PAS is observing. You will be notified when something requires attention."

### Accessibility

- Bell button: `aria-label` updates with unread count; `aria-expanded`, `aria-haspopup="dialog"`
- Drawer: `role="dialog"`, `aria-modal="true"`, `aria-label="Notifications"`, `aria-hidden` when closed
- Focus trap: Tab / Shift+Tab cycle within focusable drawer elements
- ESC closes drawer and returns focus to bell
- Mark-read button: `aria-label="Mark as read"`
- Reply textarea: `aria-label` describes demo-only state
- Empty state: `role="status"` for screen reader announcement
- All interactive elements have `:focus-visible` outlines (2px brand)

### What is intentionally not here

- No real notifications — all 15 items are static build-time data
- No SSE, no WebSockets, no polling, no `setInterval`
- No localStorage or sessionStorage persistence — state resets on page reload
- No auth coupling — drawer is visible to all roles in demo mode
- No per-topic muting or quiet-hours toggle — architecture §4 defines these for v1.x
- No toast / persistent Critical banner — channel routing is defined in §3.1 for real wiring
- No reply routing — reply field is a placeholder awaiting the PAS API wiring step

---

---

## Step 8 — Command Center intelligence layout

`docs/pas_frontend_foundation_plan.md §14` Step 8.
Branch: `pas-web-command-center-layout`.

### Files created

```
web/lib/demo/
└── commandCenter.ts             Static demo data: 6 exports, all demoOnly + noLiveBehavior

web/components/modules/command-center/
├── CommandCenterHeader.tsx      Operating summary + rehearsal badge + counts
├── CommandCenterHeader.module.css
├── AttentionSummary.tsx         Ordered attention items (severity rail + chip + action)
├── AttentionSummary.module.css
├── RecommendationPreview.tsx    Pending proposals in 2-col grid
├── RecommendationPreview.module.css
├── PipelineSnapshot.tsx         Pipeline count rows (demo snapshot)
├── PipelineSnapshot.module.css
├── SystemStatusPanel.tsx        Integration health (dot + service + detail)
├── SystemStatusPanel.module.css
├── EvidencePreview.tsx          Rehearsal evidence signals
├── EvidencePreview.module.css
├── CommandCenterOverview.tsx    Assembly: all sections + Ask PAS prompt
└── CommandCenterOverview.module.css
```

### Files updated

```
web/app/command-center/page.tsx        Renders <CommandCenterOverview /> inside <main>
web/app/command-center/page.module.css Simplified to single flex-column wrapper
```

### Layout hierarchy (top to bottom)

Answers the five diagnostic questions within 3 seconds of page load:

| Section | Question answered |
|---|---|
| CommandCenterHeader | What is PAS telling me right now? |
| AttentionSummary | What needs my attention? |
| RecommendationPreview | What is PAS proposing I do? |
| PipelineSnapshot | What is today's pipeline state? |
| SystemStatusPanel | Is the system healthy? |
| EvidencePreview | What evidence supports this? |
| Ask PAS prompt | How do I ask PAS anything else? |

### Demo data structure

`web/lib/demo/commandCenter.ts` exports:

| Export | Type | Items |
|---|---|---|
| `OPERATING_SUMMARY` | `OperatingSummary` | 1 — headline + context |
| `ATTENTION_ITEMS` | `AttentionItem[]` | 3 — urgent × 2, needs-attention × 1 |
| `RECOMMENDATION_CARDS` | `RecommendationCard[]` | 2 — approval-required proposals |
| `PIPELINE_ROWS` | `PipelineRow[]` | 5 — callbacks, bookings, leads, proposals, stale |
| `SYSTEM_STATUS` | `SystemStatusItem[]` | 5 — API healthy, Twilio degraded, Cal.com disconnected, Supabase healthy, demo |
| `EVIDENCE_SIGNALS` | `EvidenceSignal[]` | 3 — rehearsal signals |

Every item carries `demoOnly: true` and `noLiveBehavior: true`.

### Severity rendering — attention items

- Left 3px rail: colour via inline style (signal-urgent / signal-attention)
- Chip: colour + label (Urgent / Needs attention)
- Severity is never colour alone — each item has rail + chip + copy hierarchy

### Copy doctrine

- Headline: "PAS has found 3 items worth reviewing before the day gets away from the team."
- Operational language throughout: calm, plain, no jargon
- No "AI-generated insights", no "critical alerts", no exclamation marks
- Every section that uses demo data carries a "PAS has not changed live customer behavior." footer

### Mobile behavior

- Single-column layout on all breakpoints
- RecommendationPreview 2-col grid collapses to 1-col at ≤1023px
- No horizontal overflow on any section
- All content scannable at 375px viewport width

### What is intentionally not connected

- No real lead data, call data, booking data, or callback data
- No live integration health — Twilio/Cal.com status is demo-only
- No real pipeline metrics — all counts are static demo values
- No approve/decline functionality — proposal action links navigate to module skeleton
- No evidence links — "Why this?" is a placeholder (future: opens approval drawer)
- No PAS API — Ask PAS prompt directs to the composer which runs demo-only responses

### Future API connection points

| Section | Real wiring target |
|---|---|
| AttentionSummary | `GET /api/pas/attention` — proactive observer output |
| RecommendationPreview | `GET /api/pas/proposals?status=pending` — action proposal queue |
| PipelineSnapshot | `GET /api/pas/pipeline/summary` — today's operational snapshot |
| SystemStatusPanel | `GET /api/pas/integrations/health` — integration health endpoint |
| EvidencePreview | `GET /api/pas/evidence/digest?limit=3` — top evidence signals |

### Build result

`/command-center` route: 1.5 kB (was 568 B). All 16 routes static (○).
TypeScript clean, pnpm build passes.

---

---

## Step 9 — Module-specific empty states

`docs/pas_frontend_foundation_plan.md §14` Step 9.
Branch: `pas-web-module-empty-states`.

### Goal

Replace the generic route-registry copy in all 11 skeleton routes with
premium, role-aware, module-specific empty states. Still static/demo-only —
no API, no realtime, no auth, no backend calls.

### Config file

`web/lib/demo/moduleEmptyStates.ts` — single typed config:

```typescript
export interface ModuleEmptyState {
  id: string;
  contextCopy: string;                       // header description
  readonly pasCanAnswer: readonly string[];  // rendered as a dash-list
  readonly notConnectedYet: readonly string[];
  demoOnly: true;
  noLiveBehavior: true;
}
export const MODULE_EMPTY_STATES: Readonly<Record<string, ModuleEmptyState>>;
```

All 11 entries: `leads`, `calls`, `callbacks`, `bookings`, `pipeline-risks`,
`recommendations`, `action-proposals`, `evidence-digest`, `simulation-lab`,
`integrations`, `settings`.

### ModuleSkeleton changes

`web/components/modules/ModuleSkeleton.tsx` updated:
- Accepts optional `emptyState?: ModuleEmptyState` prop.
- When present: renders `contextCopy` as header description and both
  `pasCanAnswer` / `notConnectedYet` arrays as `<ul>` dash-lists.
- When absent: falls back to `route.description` / `route.pasCan` /
  `route.notConnectedYet` strings (backward-compatible).
- Section heading changed from "What PAS can help with here" →
  "What PAS can answer here".
- `aria-label` updated from `— skeleton` to `— empty state`.

`web/components/modules/ModuleSkeleton.module.css`:
- Added `.list` and `.listItem` styles (dash prefix via `::before`).

### Routes updated

All 11 module pages now import `MODULE_EMPTY_STATES` and pass
`emptyState={MODULE_EMPTY_STATES[id]}` alongside the existing `route` prop.

### Empty state copy — per module

| Module | Context copy (first line) |
|---|---|
| Leads | "This is where PAS will show lead context, source, ownership…" |
| Calls | "This is where PAS will surface every call — transcript, outcome…" |
| Callbacks | "This is where PAS will track every callback promise…" |
| Bookings | "This is where PAS will show Cal.com-backed appointments…" |
| Pipeline Risks | "This is where PAS will flag which leads and deals are at risk…" |
| Recommendations | "This is where PAS will surface what it thinks should happen next…" |
| Action Proposals | "…bounded, named actions it would like to take — nothing happens until a human approves…" |
| Evidence Digest | "This is where PAS will show its receipts…" |
| Simulation Lab | "…rehearsal calls, scenarios, and recommendations with zero live side effects…" |
| Integrations | "…Read access always comes first. Write access requires explicit approval…" |
| Settings | "…PAS adapts to how your office works, not the other way around." |

### Invariants preserved

- Every page carries the demo/rehearsal chip.
- Every page ends with "PAS has not changed live customer behavior."
- `demoOnly: true` and `noLiveBehavior: true` on every `ModuleEmptyState` entry.
- No fake live metrics, no fake client claims, no AI-gradient styling.
- All 16 routes static, build clean.

---

---

## Step 10 — Vercel deployment preparation

`docs/pas_frontend_foundation_plan.md §14` Step 10.
Branch: `pas-web-vercel-deployment-prep`.
Full deployment guide: `docs/pas_web_vercel_deployment.md`.

### Goal

Prepare the frontend for Vercel deployment without adding backend coupling.
No API calls, no CORS, no auth, no secrets. Backend untouched.

### Files added

| File | Purpose |
|---|---|
| `docs/pas_web_vercel_deployment.md` | Full Vercel setup guide, checklist, CORS sequencing, rollback, smoke test |
| `web/README.md` | Local dev, build, Vercel root directory, env var context |
| `web/.env.example` | Env var reference — `NEXT_PUBLIC_PAS_API_BASE_URL` placeholder only |

### Key decisions

**No `vercel.json` added.** The Vercel dashboard Root Directory setting
(`web`) is sufficient. A `vercel.json` would only be needed for custom
headers, redirects, rewrites, or multi-region config — none required now.

**No package.json changes.** `dev`, `build`, `start`, and `type-check`
are all present. Vercel uses `pnpm build`. No lint script was added —
`type-check` covers static correctness.

**`next.config.ts` unchanged.** The existing comment already notes that
rewrites to the backend land in a later step once the Vercel domain is known.

### CORS sequencing (documented)

Do not update `app/main.py` until:
1. Vercel deployment URL is confirmed
2. Custom domain (`pas.orvnlabs.com`) is active
3. API wiring step is ready to begin

The deployment guide documents exactly when and how to add CORS origins.

### Vercel project settings (summary)

| Setting | Value |
|---|---|
| Root Directory | `web` |
| Framework Preset | Next.js |
| Install Command | `pnpm install` |
| Build Command | `pnpm build` |
| Output Directory | Next.js default |
| Target domain | `pas.orvnlabs.com` |
| `NEXT_PUBLIC_PAS_API_BASE_URL` | empty (wire in Step 11+) |

---

## Canonical sequence — shipped + future

> **This list is authoritative.** `docs/pas_frontend_foundation_plan.md §14`
> follows it. The step numbers below are the numbers used in all branch
> names, commits, and future planning.

### Shipped (Steps 1–11, merged to `main`)

| # | Step | Branch |
|---|---|---|
| 1 | Web tooling foundation | `pas-web-foundation-v1` |
| 2 | Design tokens | `pas-web-foundation-v1` |
| 3 | App shell chrome | `pas-web-app-shell-chrome` |
| 4 | Role-aware route skeletons | `pas-web-route-skeletons` |
| 5 | Session/permission scaffold | `pas-web-session-permission-scaffold` |
| 6 | PAS composer shell | `pas-web-composer-shell` |
| 7 | Notification/presence center shell | `pas-web-notification-presence-shell` |
| 8 | Command Center intelligence layout | `pas-web-command-center-layout` |
| 9 | Module-specific empty states | `pas-web-module-empty-states` |
| 10 | Vercel deployment preparation | `pas-web-vercel-deployment-prep` (PR #39) |
| 11 | API boundary scaffold | `pas-web-api-boundary-scaffold` (PR #42) — read-only fetch client, `IS_DEMO_MODE` gating, `GET /health` probe, connection-status chip. No live wiring beyond health. |

### Next pending step (12) and future (Steps 12–20, not yet merged)

| # | Step | Notes |
|---|---|---|
| 12 | Vercel deployment + domain smoke test | Deploy `/web` as a **separate** Vercel project (demo mode, `NEXT_PUBLIC_PAS_API_BASE_URL` unset); confirm production URL + subdomain `pas.orvnlabs.com`. Must not disturb the existing ORVN website project (`orvnlabs.com` / `www`) — see coexistence rules in `docs/pas_web_vercel_deployment.md`. |
| 13 | CORS allow-list update | Add confirmed Vercel URL/domain to `app/main.py` — only after Step 12. |
| 14 | Read-only PAS205–PAS208 surface integration | Observer, Recommendations, Evidence Digest, Action Proposals — read-only. |
| 15 | Realtime/SSE foundation | PAS thinking presence, notification arrivals, Critical banner. |
| 16 | Integrations framework shell | Connector list, connect flow, health card. Read scopes only. |
| 17 | Auth provider selection + auth scaffold | Provider choice; sign-in / tenant context / sign-out. |
| 18 | Role enforcement with backend validation | Promote Step 5 display-only shaping to server-validated gates. |
| 19 | Action proposal approval UI | Approval drawer wired to the Action Proposals queue; present-only. |
| 20 | Live execution gates | One named, bounded action at a time; mutation gated through the API with audit emission. |

### Merge status

- **Step 11 — API boundary scaffold** was **merged to `main` via
  PR #42** (main at `9baaf50`); commit `99d7f26` is preserved as the
  sole feature commit. It is a read-only boundary scaffold with no
  live API call beyond `GET /health`, no CORS, no auth, no mutations.
- **PAS209** (bounded action proposal package — the backend that
  Step 19's approval UI and Step 20's execution gates will eventually
  surface) was **merged to `main` via PR #40** (`fcffbb4`); remote
  branch `pas209-bounded-action-proposals` (commit `3a554c9`) remains.
  Backend only — see `docs/pas209_action_proposals.md`.
- **Step 12 — Vercel deployment** has **not been executed**. No Vercel
  project, deployment URL, or `pas.orvnlabs.com` domain has been
  created yet (see `docs/pas_web_vercel_deployment.md`).
- **Step 12B — Operational demo layer (PRs A–I)** is **complete and
  merged to `main`**: typed demo data model, Agents, Integrations
  marketplace, Leads/Calls/Callbacks, Settings, PAS Brain, PAS Room,
  notification demo replies, and the synthesized Command Center. All
  frontend-only and demo/rehearsal-labelled — no backend, no live
  behaviour. See `docs/pas_operational_demo_layer_plan.md`.

### Step 11 entry point

When API wiring begins, replace the composer's `setTimeout` in
`handleSubmit` with a request through the typed client
(`web/lib/api/`). Unauthenticated `GET` first; the CORS update
(Step 13) lands only after the Vercel origin is confirmed (Step 12).
