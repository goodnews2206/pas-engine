# PAS Web Foundation v1

> Status: shipped. Branch: `pas-web-foundation-v1`. Owner: ORVN Labs.
> Created: 2026-05-25.

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

## Next steps (Step 2)

`docs/pas_frontend_foundation_plan.md §14` Step 2: **Design tokens.**
Audit `globals.css` against the final sign-off values and lock the
signature hue. No components yet.

Step 3 following that: **App shell** — TopBar chrome, Sidebar chrome,
Composer chrome, main slot, overlay region. Still no routes or data.
