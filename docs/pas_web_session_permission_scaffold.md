# PAS Web Session & Permission Scaffold

> Status: shipped (Step 5). Owner: ORVN Labs.
> Branch: `pas-web-session-permission-scaffold`.
> Authority: `docs/pas_frontend_foundation_plan.md §14 Step 5`.

## What Step 5 added

A frontend-only demo session and permission boundary scaffold so PAS
behaves like a role-aware workspace before real auth exists.

### Files created

```
web/lib/session/
├── demoSession.ts    Types (Role, Permission, DemoUser, DemoWorkspace, DemoSession),
│                     ROLE_PERMISSIONS table, DEMO_SESSION constant
└── permissions.ts    hasPermission(), hasAnyPermission(), canViewRoute(),
                      getVisibleRoutesForSession(), getNavGroupsForSession(),
                      getSessionRoleLabel()
```

### Files updated

```
web/lib/navigation/routes.ts             Added requiredPermissions: Permission[] to
                                         RouteDefinition; updated UserRole names;
                                         imported Permission type from demoSession.ts
web/components/shell/NavList.tsx         Switched from DEMO_ROLE/getNavGroupsForRole
                                         to DEMO_SESSION/getNavGroupsForSession
web/components/shell/Sidebar.tsx         Workspace, role, footer from DEMO_SESSION
web/components/shell/TopBar.tsx          Avatar initials and aria-label from DEMO_SESSION
web/components/shell/TenantStrip.tsx     Session + permission boundary context items
web/components/modules/ModuleSkeleton.tsx  Added auth boundary note
web/components/modules/ModuleSkeleton.module.css  Added .authNote style
```

---

## Why this is NOT real auth

| What it is | What it is not |
|---|---|
| A static TypeScript constant resolved at build time | A server session |
| Display-only navigation filtering | An access control boundary |
| A documented permission model for the demo | An enforced permission check |
| A scaffold to replace with real auth | Authentication or authorization |

`DEMO_SESSION` is a compile-time constant. It is not stored in
localStorage, sessionStorage, or cookies. It cannot be changed at
runtime by the user. Any user who can load the page sees the same
demo session.

A comment appears in every component that reads from DEMO_SESSION:
> "Display-only scaffold. Real security belongs to the backend/auth layer."

---

## How future auth will replace DEMO_SESSION

When Supabase Auth (or another provider) is wired in the real auth step:

1. `DEMO_SESSION` is replaced by a server session resolved per request
   (e.g., Supabase `createServerClient`, Next.js route handlers, or
   middleware cookies).
2. `DemoSession` interface extends into a real `Session` type with a
   verified JWT claim or database-resolved role.
3. `DEMO_ROLE` / `DEMO_SESSION` references in shell components are
   replaced by `await getServerSession()` or equivalent RSC patterns.
4. `permissions.ts` helpers stay intact — they accept any `DemoSession`
   shape; replacing the constant with a real session requires no helper
   rewrites.
5. Route gating moves from display-only to enforced: Next.js middleware
   or server-side redirect checks `canViewRoute(session, route)` and
   redirects unauthenticated or unauthorized requests.

---

## What must be enforced server-side later

The following are display-only in this step and MUST be enforced
server-side in the auth step:

- Route access (currently: nav hides routes; server does not gate them)
- Permission checks (currently: `canViewRoute` drives nav only)
- Role assignment (currently: `DEMO_SESSION.user.role` is a constant)
- Workspace isolation (currently: single hardcoded workspace)
- Action approval gates (currently: `approve_*` permissions are display labels)

**No UI check in this file prevents a user from directly navigating
to a restricted URL in the skeleton phase.**

---

## Roles and permissions

| Permission | Broker Owner | Admin/Ops | Team Lead | Agent | Read-only Viewer | ORVN Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| view_all_leads | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| view_assigned_leads | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| view_calls | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| view_callbacks | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| view_bookings | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| view_pipeline_risks | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| view_recommendations | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| approve_recommendations | ✓ | ✓ | — | — | — | ✓ |
| view_action_proposals | ✓ | ✓ | ✓ | — | — | ✓ |
| approve_action_proposals | ✓ | ✓ | — | — | — | ✓ |
| view_simulation_lab | ✓ | ✓ | ✓ | — | — | ✓ |
| view_evidence_digest | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| manage_integrations | ✓ | ✓ | — | — | — | ✓ |
| manage_settings | ✓ | ✓ | — | — | — | ✓ |
| manage_users | ✓ | ✓ | — | — | — | ✓ |
| view_billing | ✓ | ✓ | — | — | — | ✓ |
| view_audit_logs | ✓ | ✓ | — | — | — | ✓ |
| orvn_admin_access | — | — | — | — | — | ✓ |

---

## Route visibility by role

`getNavGroupsForSession(session)` calls `canViewRoute(session, route)` for
each route. A route is visible if `requiredPermissions` is empty OR the
session user holds at least one of the listed permissions (`hasAnyPermission`).

| Route | Required permissions (any) | Hidden from |
|---|---|---|
| /command-center | none | nobody |
| /leads | view_all_leads, view_assigned_leads | nobody |
| /calls | view_calls | nobody |
| /callbacks | view_callbacks | Read-only Viewer |
| /bookings | view_bookings | nobody |
| /pipeline-risks | view_pipeline_risks | Agent |
| /recommendations | view_recommendations | Agent |
| /action-proposals | view_action_proposals | Agent, Read-only Viewer |
| /evidence-digest | view_evidence_digest | Agent |
| /simulation-lab | view_simulation_lab | Agent, Read-only Viewer |
| /integrations | manage_integrations | Agent, Read-only Viewer |
| /settings | manage_settings | Team Lead, Agent, Read-only Viewer |

Empty families (no visible routes) are omitted from the nav per
Dashboard IA §2.2. People family remains out of scope for v1.

---

## Risks avoided

- **No localStorage/sessionStorage**: session cannot be tampered by the user
- **No Clerk/Auth0/Supabase Auth**: zero third-party auth dependencies in v1
- **No API calls**: `DEMO_SESSION` is a static constant; no network request
- **No state library**: permission helpers are pure functions
- **No backend changes**: FastAPI backend untouched
- **No CORS change**: no new cross-origin surface
- **No secrets**: no tokens, keys, or credentials anywhere

---

## DEMO_SESSION at a glance

```typescript
DEMO_SESSION = {
  mode: "demo",
  sessionLabel: "Demo session",
  permissionBoundary: "Display-only",
  workspace: { id: "demo-orvn-realty", name: "ORVN Demo Realty", slug: "orvn-demo-realty" },
  user: {
    id: "demo-broker-owner",
    name: "Demo Broker",
    email: "demo@orvn.demo",
    initials: "DB",
    role: "Broker Owner",
    permissions: ROLE_PERMISSIONS["Broker Owner"],  // 17 permissions
  },
}
```

---

## Build result

`pnpm build` — 16 routes, all static (`○`), TypeScript clean.
`python -m compileall -q app scripts tests` — clean, no output.

---

## Next steps (Step 6+)

`docs/pas_frontend_foundation_plan.md §14` Step 6: **API wiring.**
Connect the Next.js frontend to the FastAPI backend via typed fetch
clients. No auth yet — unauthenticated read endpoints first.
Real auth (Supabase session, middleware gates) follows in a later step.
