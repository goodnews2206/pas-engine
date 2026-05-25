# PAS Web Foundation v1

> Status: shipped (Step 1 + 2 + 3). Owner: ORVN Labs.
> Step 1+2 branch: `pas-web-foundation-v1` (merged to main 2026-05-25).
> Step 3 branch: `pas-web-app-shell-chrome`.

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

## Next steps (Step 4)

`docs/pas_frontend_foundation_plan.md §14` Step 4: **Routing skeleton.**
All routes mounted with placeholder content. Role gating wired at the
route layer. No real data yet.
