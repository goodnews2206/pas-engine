# PAS Web — Vercel Deployment Guide

> Status: preparation complete (Step 10). First deploy not yet executed.
> Backend: Railway (separate service — not touched here).
> Frontend target: `pas.orvnlabs.com`

---

## Overview

The PAS frontend (`/web`) is a Next.js 15 App Router application.
It deploys to Vercel as a standalone service.
The Python/FastAPI backend remains on Railway.
These two services are decoupled until API wiring is added (Step 11+).

At this step:
- The frontend builds and renders fully as a static demo shell.
- No API calls are made.
- No CORS configuration has been added to the backend yet.
- No secrets are stored in Vercel yet.

---

## Coexistence with the existing ORVN Labs website

`orvnlabs.com` already exists in Vercel and powers the ORVN Labs
marketing website. PAS web is a **separate concern** and must not
disturb that project.

**Hard rules:**

- The existing ORVN website stays on its **current Vercel project**.
  Do not import the PAS repo into it.
- `orvnlabs.com` and `www.orvnlabs.com` **must remain untouched** — do
  not edit, move, or remove these domains from the existing project.
- PAS web deploys as a **new, separate Vercel project** (suggested
  name: `pas-web` / `pas-engine-web`) importing the same GitHub repo
  `goodnews2206/pas-engine` with Root Directory `web`.
- PAS uses the **subdomain `pas.orvnlabs.com` only**. Adding a
  subdomain to the new project does not affect the apex `orvnlabs.com`
  or `www` on the existing project — Vercel scopes each hostname
  independently.
- **First deploy is demo mode:** `NEXT_PUBLIC_PAS_API_BASE_URL` stays
  unset, so the app makes no backend calls. No secrets, no env vars.
- **Backend CORS is not touched** until the PAS Vercel URL/domain is
  confirmed and Railway is ready (see "When to add CORS" below).

### If Vercel reports a domain conflict

If Vercel says `pas.orvnlabs.com` (or the domain) is already in use, or
shows any "assigned to another project" message:

1. **Stop.** Do not proceed with the domain attach.
2. **Do not** click any option that removes or reassigns the domain
   from another project — that would risk the existing ORVN website.
3. Record the **exact** message verbatim and escalate before any
   further action.

The subdomain `pas.orvnlabs.com` is expected to be free even though the
apex `orvnlabs.com` is in use elsewhere. A conflict on the subdomain
means it was previously assigned and needs manual review — never an
automatic removal.

---

## Vercel project setup

### 1. Create project from GitHub

1. Log in to vercel.com → **Add New Project**
2. Import `goodnews2206/pas-engine` from GitHub
3. Vercel will ask to configure the project — set the following:

| Setting | Value |
|---|---|
| Root Directory | `web` |
| Framework Preset | Next.js (auto-detected) |
| Install Command | `pnpm install` |
| Build Command | `pnpm build` |
| Output Directory | *(leave default — Next.js)* |
| Node.js Version | 20.x (LTS) |

> **Root Directory is critical.** The repo root is not the Next.js project.
> Set Root Directory to `web` before the first deploy or the build will fail.

### 2. Environment variables

Add the following in Vercel → Settings → Environment Variables.

| Variable | Value | Required now |
|---|---|---|
| `NEXT_PUBLIC_PAS_API_BASE_URL` | *(leave empty for now)* | No — wire in Step 11+ |

Do **not** add any secrets, Supabase keys, or auth tokens at this stage.
The frontend does not make backend calls yet.

### 3. Deploy

Click **Deploy**. Vercel will:
1. Clone the repo
2. Set Root Directory to `web`
3. Run `pnpm install`
4. Run `pnpm build`
5. Deploy 16 static routes to the Edge network

---

## Custom domain

Target: `pas.orvnlabs.com` — attached to the **new, separate PAS Vercel
project**, never the existing ORVN website project (see "Coexistence
with the existing ORVN Labs website" above). The apex `orvnlabs.com`
and `www.orvnlabs.com` stay where they are.

Steps (after first deploy succeeds):
1. Vercel → Project → Settings → Domains → Add `pas.orvnlabs.com`
2. Add a CNAME record at your DNS provider:
   ```
   pas.orvnlabs.com  CNAME  cname.vercel-dns.com
   ```
3. Wait for DNS propagation (~5 min to 24 h depending on TTL)
4. Vercel provisions TLS automatically

> Do not add the custom domain before verifying the deploy works on the
> `*.vercel.app` preview URL first.

---

## Backend (Railway)

The FastAPI backend is a separate Railway service.
It is **not** affected by this Vercel deployment.

### CORS

**Do not update `app/main.py` yet.**

CORS origins must be updated only after the actual Vercel deployment URL
(or custom domain) is confirmed. The correct sequence:

1. First Vercel deploy → note the `*.vercel.app` URL
2. Confirm custom domain (`pas.orvnlabs.com`) is active
3. Add both to `CORS_ORIGINS` in `app/main.py`:
   ```python
   CORS_ORIGINS = [
       "https://pas.orvnlabs.com",
       "https://<project>.vercel.app",  # preview fallback
   ]
   ```
4. Redeploy Railway backend
5. Set `NEXT_PUBLIC_PAS_API_BASE_URL` in Vercel to the Railway URL
6. Trigger a Vercel redeploy

This sequence prevents CORS from being opened before the frontend URL is known.

---

## Package scripts

All scripts required by Vercel are present in `web/package.json`:

| Script | Command | Purpose |
|---|---|---|
| `dev` | `next dev` | Local development |
| `build` | `next build` | Production build (Vercel uses this) |
| `start` | `next start` | Local production server |
| `type-check` | `tsc --noEmit` | TypeScript validation (CI) |

No additional scripts are needed for Vercel deployment.

---

## vercel.json

**Not added.** The Vercel dashboard Root Directory setting (`web`) is
sufficient for this project structure. A `vercel.json` would only be needed
if custom headers, redirects, rewrites, or multi-region config were required.
None of those apply at this stage.

---

## Deployment checklist

### Before first Vercel deploy

- [ ] Root Directory set to `web` in Vercel project settings
- [ ] Framework Preset is Next.js
- [ ] Install command is `pnpm install`
- [ ] Build command is `pnpm build`
- [ ] `NEXT_PUBLIC_PAS_API_BASE_URL` left empty (no backend calls yet)
- [ ] No secrets added to Vercel env vars
- [ ] `pnpm build` passes locally from `/web`
- [ ] `python -m compileall -q app scripts tests` passes from repo root
- [ ] Backend (`app/main.py`) is **not** modified

### After first Vercel deploy

- [ ] All 16 routes return 200 on the `*.vercel.app` URL
- [ ] `/command-center` loads and renders the Command Center layout
- [ ] Notification drawer opens and closes
- [ ] Composer renders (no submit wired yet — that is Step 11+)
- [ ] All module empty states render their specific copy
- [ ] No console errors in the browser
- [ ] No 404s on static assets
- [ ] Demo chips and disclaimers visible on every module page

### When to add custom domain (`pas.orvnlabs.com`)

After the first deploy smoke test passes on `*.vercel.app`.

### When to add CORS

After confirming:
1. Vercel deployment URL is stable
2. Custom domain is active
3. API wiring step (Step 11+) is ready to begin

### When to wire `NEXT_PUBLIC_PAS_API_BASE_URL`

When Step 11+ API wiring begins. Set to the Railway backend URL
(e.g. `https://pas-engine-production.up.railway.app`).

---

## Rollback procedure

1. Vercel → Project → Deployments
2. Find the last known-good deployment
3. Click **Promote to Production**

Rollback takes effect in under 30 seconds. No backend changes required
since the frontend makes no backend calls at this stage.

---

## Post-deploy smoke test

Run manually after each production deploy:

```
Route                    Expected
/                        Redirects to /command-center
/command-center          Command Center layout renders
/leads                   Leads empty state — module-specific copy visible
/calls                   Calls empty state visible
/callbacks               Callbacks empty state visible
/bookings                Bookings empty state visible
/pipeline-risks          Pipeline Risks empty state visible
/recommendations         Recommendations empty state visible
/action-proposals        Action Proposals empty state visible
/evidence-digest         Evidence Digest empty state visible
/simulation-lab          Simulation Lab empty state visible
/integrations            Integrations empty state visible
/settings                Settings empty state visible
```

Check on each route:
- Demo / rehearsal chip is visible
- "PAS has not changed live customer behavior." disclaimer is present
- No live data or live API calls are made
- Browser console is clean

---

## Environment file reference

`web/.env.example` contains all supported variables with placeholder values.
Copy to `web/.env.local` for local overrides. Never commit `.env.local`.

```
NEXT_PUBLIC_PAS_API_BASE_URL=
```
