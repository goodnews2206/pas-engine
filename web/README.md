# PAS Web

Next.js 15 App Router frontend for PAS (Performative AI SuperStaff).
Part of the ORVN platform. Backend is a separate FastAPI service on Railway.

## Local development

```bash
# from /web
pnpm install
pnpm dev
```

Opens at `http://localhost:3000`. Redirects to `/command-center`.

## Build

```bash
pnpm build   # production build
pnpm start   # serve production build locally
```

## Type check

```bash
pnpm type-check
```

## Project structure

```
web/
├── app/              Next.js App Router routes + layouts
│   ├── globals.css   Design system tokens (all custom properties)
│   └── layout.tsx    Root layout — Inter + JetBrains Mono
├── components/       UI components (RSC by default; "use client" only where needed)
│   ├── modules/      Per-module page components
│   ├── notifications/ Notification center + drawer + card
│   └── shell/        TopBar, Sidebar, Composer
└── lib/
    ├── demo/         Static demo/rehearsal data (no live data)
    ├── navigation/   Route registry + nav helpers
    └── session/      Demo session scaffold (no auth yet)
```

## Vercel deployment

- **Root Directory:** `web`
- **Framework:** Next.js (auto-detected)
- **Install:** `pnpm install`
- **Build:** `pnpm build`
- **Target domain:** `pas.orvnlabs.com`

See `docs/pas_web_vercel_deployment.md` for the full setup guide.

## Environment variables

Copy `.env.example` to `.env.local` for local overrides.
Never commit `.env.local`.

| Variable | Purpose | Required now |
|---|---|---|
| `NEXT_PUBLIC_PAS_API_BASE_URL` | Railway backend URL | No — Step 11+ |

At this stage the frontend makes **no backend calls**. The env var is
a placeholder for when API wiring is added.

## What is and is not connected

**Connected:**
- Design system (CSS custom properties, typography, spacing, color)
- App shell (TopBar, Sidebar, Composer)
- Notification center (client island, 15 demo notifications)
- Command Center intelligence layout (7 sections, demo data)
- 11 module empty states (module-specific copy)
- Navigation (role-aware display, demo session)

**Not yet connected:**
- Backend API (FastAPI on Railway)
- Auth (no Clerk, Auth0, or Supabase Auth)
- Real-time (no SSE, WebSockets, or push)
- Any live data source

All content is clearly labelled demo / rehearsal.
PAS has not changed live customer behavior.
