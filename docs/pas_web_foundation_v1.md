# PAS Web Foundation v1

> Status: shipped (Step 1 + 2 + 3 + 4). Owner: ORVN Labs.
> Step 1+2 branch: `pas-web-foundation-v1` (merged to main 2026-05-25).
> Step 3 branch: `pas-web-app-shell-chrome` (merged to main 2026-05-25).
> Step 4 branch: `pas-web-route-skeletons`.

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

## Next steps (Step 7+)

`docs/pas_frontend_foundation_plan.md §14` Step 7: **API wiring.**
Connect composer submit to FastAPI `/api/pas/ask`. Type-safe fetch client.
Replace the `setTimeout` with a real request. No auth yet — unauthenticated
endpoint first.
