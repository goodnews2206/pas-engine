/*
 * PAS Route Registry — frontend-only metadata layer.
 *
 * This file defines DISPLAY-ONLY role shaping for the navigation.
 * It is NOT a security boundary. No permissions are enforced here.
 * Real role resolution + permission gates belong to the backend auth layer.
 *
 * Authority: docs/pas_dashboard_information_architecture.md §2–§3
 *            docs/pas_product_design_book.md §2 §4
 *            docs/pas_web_session_permission_scaffold.md
 */

import type { Permission } from "@/lib/session/demoSession";

export type NavFamily = "Operate" | "Notice" | "People" | "System" | "ORVN";

export type UserRole =
  | "Broker Owner"
  | "Admin/Ops"
  | "Team Lead"
  | "Agent"
  | "Read-only Viewer"
  | "ORVN Internal Admin";

export interface RouteDefinition {
  id: string;
  label: string;
  href: string;
  family: NavFamily;
  /** One-sentence description of what the module surfaces. */
  description: string;
  /** Forward-looking: what PAS can do here once wired. */
  pasCan: string;
  /** What is intentionally not connected in this skeleton step. */
  notConnectedYet: string;
  /** Roles that can see this module (display-only; not enforced). */
  visibleTo: UserRole[];
  /** Permissions required to view this route (display-only; not enforced). */
  requiredPermissions: Permission[];
  status: "skeleton" | "operational-demo";
  demoOnly: true;
  noLiveBehavior: true;
}

export interface NavGroup {
  family: NavFamily;
  routes: RouteDefinition[];
}

/* ── Route definitions — copy from Product Design Book §4 ── */
export const ROUTES: RouteDefinition[] = [
  /* ── Operate ── */
  {
    id: "command-center",
    label: "Command Center",
    href: "/command-center",
    family: "Operate",
    description:
      "The single landing surface — what needs your attention, what PAS proposes, what just happened.",
    pasCan:
      "Surface pending recommendations, flag pipeline risks, show today's bookings and callbacks, propose next actions.",
    notConnectedYet:
      "Proactive Observer (PAS205), Recommendations (PAS208), Action Proposals (PAS209), live call data, notification delivery.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Agent",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: [],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "leads",
    label: "Leads",
    href: "/leads",
    family: "Operate",
    description:
      "Every lead — where it came from, who owns it, where it is in the pipeline, what happens next.",
    pasCan:
      "Find stalled leads, flag pipeline risks, suggest next touchpoints, draft callback requests.",
    notConnectedYet:
      "Lead source integrations (Zillow, Realtor.com, Facebook), CRM adapter, PAS Brain qualification scoring.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Agent",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_all_leads", "view_assigned_leads"],
    status: "operational-demo",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "calls",
    label: "Calls",
    href: "/calls",
    family: "Operate",
    description:
      "Every call with transcript, outcome, FSM state trace, and evidence panel.",
    pasCan:
      "Summarize calls, flag items for review, surface objection patterns, identify coaching moments.",
    notConnectedYet:
      "Twilio live routing, Deepgram transcription, ElevenLabs voice, PAS Brain tone model.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Agent",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_calls"],
    status: "operational-demo",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "callbacks",
    label: "Callbacks",
    href: "/callbacks",
    family: "Operate",
    description:
      "Every scheduled callback — owner, time, confirmation status, and evidence of the original ask.",
    pasCan:
      "Surface missed callbacks, suggest reschedule language, flag stale promises, route to the right agent.",
    notConnectedYet:
      "PAS callback capture flow (PAS128), notification delivery, calendar sync.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Agent",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_callbacks"],
    status: "operational-demo",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "bookings",
    label: "Bookings",
    href: "/bookings",
    family: "Operate",
    description:
      "Cal.com-backed appointments — status, confirmation, reassignment, evidence of source call.",
    pasCan:
      "Flag at-risk bookings, suggest reassignment when agents are unavailable, confirm qualification before the meeting.",
    notConnectedYet:
      "Cal.com integration, agent calendar sync, booking confirmation webhooks.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Agent",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_bookings"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },

  /* ── People ── */
  {
    id: "agents",
    label: "Agents",
    href: "/agents",
    family: "People",
    description:
      "Your team — who is available, who owns follow-up, where coverage is thin, and who PAS is watching.",
    pasCan:
      "Watch agent coverage against callback promises and lead ownership, flag stretched agents, surface coaching moments.",
    notConnectedYet:
      "Live agent presence, CRM ownership sync, response-time telemetry, performance history.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_agents"],
    status: "operational-demo",
    demoOnly: true,
    noLiveBehavior: true,
  },

  /* ── Notice ── */
  {
    id: "pipeline-risks",
    label: "Pipeline Risks",
    href: "/pipeline-risks",
    family: "Notice",
    description:
      "Which leads and deals are at risk of stalling — risk reason, last touch, suggested intervention.",
    pasCan:
      "Explain the risk, propose a recovery action, simulate the intervention outcome before committing.",
    notConnectedYet:
      "Proactive Observer (PAS205), live CRM data, pipeline scoring model.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_pipeline_risks"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "recommendations",
    label: "Recommendations",
    href: "/recommendations",
    family: "Notice",
    description:
      "Operator-approved suggestions PAS would like to act on — each backed by evidence.",
    pasCan:
      "Explain its reasoning, refresh evidence on demand, route a recommendation directly to an approval drawer.",
    notConnectedYet:
      "Action Proposals (PAS209), Evidence Digest wiring, approval routing, PAS208 live recommendations.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_recommendations"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "action-proposals",
    label: "Action Proposals",
    href: "/action-proposals",
    family: "Notice",
    description:
      "Bounded, named actions PAS proposes to take — pending your sign-off before anything happens.",
    pasCan:
      "Take the bounded action on approval, explain every step, emit a full audit trail, flag if the window lapses.",
    notConnectedYet:
      "PAS209 bounded action layer, integration write paths, audit emission, expiry countdown.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_action_proposals"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "evidence-digest",
    label: "Evidence Digest",
    href: "/evidence-digest",
    family: "Notice",
    description:
      "The receipts — why PAS said what it said, linked to source transcripts, snapshots, and observer signals.",
    pasCan:
      "Expand an evidence chain on demand, explain confidence levels, link to source calls and snapshot rows.",
    notConnectedYet:
      "Audit Logs, linked transcript viewer, PAS201–PAS203 evidence surface, evidence export.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "Read-only Viewer",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_evidence_digest"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },

  /* ── System ── */
  {
    id: "simulation-lab",
    label: "Simulation Lab",
    href: "/simulation-lab",
    family: "System",
    description:
      "Run a call, a scenario, or a recommendation without any live side effects — every artifact is rehearsal.",
    pasCan:
      "Simulate any scenario with rehearsal data, export evidence artifacts, replay a call flow end-to-end.",
    notConnectedYet:
      "Simulation runner, Cal.com sim, voice simulation, scenario library.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["view_simulation_lab"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "integrations",
    label: "Integrations",
    href: "/integrations",
    family: "System",
    description:
      "Connect external systems — see what PAS can read and write, view health, manage scopes.",
    pasCan:
      "Show exactly what it can answer with each connection, surface sync errors, guide the reconnect flow.",
    notConnectedYet:
      "OAuth / API key connect flow, CRM adapter, Cal.com, Twilio, Deepgram, ElevenLabs, lead source connectors.",
    visibleTo: [
      "Broker Owner",
      "Admin/Ops",
      "Team Lead",
      "ORVN Internal Admin",
    ],
    requiredPermissions: ["manage_integrations"],
    status: "operational-demo",
    demoOnly: true,
    noLiveBehavior: true,
  },
  {
    id: "settings",
    label: "Settings",
    href: "/settings",
    family: "System",
    description:
      "Workspace configuration — brokerage profile, operational hours, tone, disclosures, default scripts.",
    pasCan:
      "Flag configuration conflicts with PAS Brain, suggest optimal operational hours, guide initial brokerage setup.",
    notConnectedYet:
      "Settings persistence, PAS Brain config, member management, API key rotation.",
    visibleTo: ["Broker Owner", "Admin/Ops", "ORVN Internal Admin"],
    requiredPermissions: ["manage_settings"],
    status: "skeleton",
    demoOnly: true,
    noLiveBehavior: true,
  },
];

/* ── Lookup helpers ── */

export const ROUTES_BY_ID = Object.fromEntries(
  ROUTES.map((r) => [r.id, r])
) as Record<string, RouteDefinition>;

export const ROUTES_BY_HREF = Object.fromEntries(
  ROUTES.map((r) => [r.href, r])
) as Record<string, RouteDefinition>;

/** Returns only routes visible to the given role, preserving original order. */
export function getRoutesForRole(role: UserRole): RouteDefinition[] {
  return ROUTES.filter((r) => r.visibleTo.includes(role));
}

/** Returns nav groups (family → routes) visible to the given role.
 *  Empty families are omitted per Dashboard IA §2.2. */
export function getNavGroupsForRole(role: UserRole): NavGroup[] {
  const visible = getRoutesForRole(role);
  const FAMILY_ORDER: NavFamily[] = [
    "Operate",
    "Notice",
    "People",
    "System",
    "ORVN",
  ];
  return FAMILY_ORDER.map((family) => ({
    family,
    routes: visible.filter((r) => r.family === family),
  })).filter((g) => g.routes.length > 0);
}
