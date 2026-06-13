# PAS — Product Architecture

## Delivery model

- **Web-first.** PAS is delivered through the browser today. The web app is the primary and canonical surface.
- **Progressive Web App (PWA) — in progress.** PAS is moving toward being an installable PWA: home-screen install, offline tolerance, and push notifications, without depending on an app store.
- **Native mobile — deferred.** Native iOS/Android is explicitly *later*, not now. Do not scope, design, or build native mobile work unless told the deferral has been lifted. When mobile-ness matters, the answer is "PWA," not "native app."

## Stack overview

| Layer | Platform | Role |
|---|---|---|
| **Backend** | **Railway** | Application backend / services hosting. Build via nixpacks against `constraints.txt`. |
| **Frontend** | **Vercel** | Web app hosting and delivery (the web-first / PWA surface). |
| **Data** | **Supabase** | Data layer — persistence for users, operations, and the memory hierarchy. |

### Backend — Railway

- Hosts the PAS backend.
- Builds with **nixpacks**, which uses **`constraints.txt`**; **pip is pinned to 26.1.2**.
- **Note:** PAS211K.2C is currently **blocked by a Railway subscription issue** (billing/account-level, not code). See `PAS_SEQUENCE_AND_STATUS.md`.

### Frontend — Vercel

- Hosts the web-first app and the evolving PWA.
- This is where install/offline/push behavior lands as the PWA matures.

### Data — Supabase

- The persistence layer behind PAS.
- Stores the operational record that feeds the memory hierarchy (see `PAS_MEMORY_ARCHITECTURE.md`).
- **Do not apply migrations** without explicit authorization.

## Build / dependency invariants

- `constraints.txt` — **committed**, authoritative.
- `pip` — **pinned to 26.1.2**.
- `nixpacks` — builds using `constraints.txt`.
- Do **not** modify `requirements.txt`, `constraints.txt`, or `nixpacks.toml` without explicit instruction. These exist to keep builds reproducible across Railway.

## What PAS is architecturally (positioning)

PAS is an **intelligence + memory layer**, not a thin UI over a database:

- It ingests operational events (leads, contacts, follow-ups, agent actions).
- It acts on them with speed (speed-to-lead) and continuity (follow-up that doesn't depend on a human remembering).
- It accumulates a persistent operational record — the **PAS Brain** — that survives staff turnover and handoffs.

It is **not** a CRM, chatbot, or social app. The architecture serves infrastructure goals: reliability, memory, and operational visibility — not feeds or engagement.

## Standing constraints relevant to architecture

- Do not touch **PAS209**.
- Do not delete `__pycache__`.
- Do not apply migrations.
- Do not push or merge without authorization.
