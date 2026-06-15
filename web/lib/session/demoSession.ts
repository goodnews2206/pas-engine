/*
 * PAS Demo Session — frontend-only session scaffold.
 *
 * DISPLAY-ONLY. This file is NOT a security boundary.
 * No authentication is performed here. No cookies, no localStorage,
 * no sessionStorage. DEMO_SESSION is resolved at build time.
 *
 * Replace DEMO_SESSION with a real server session in the auth step
 * (Frontend Foundation Plan §14 Step 5 auth phase).
 *
 * Authority: docs/pas_web_session_permission_scaffold.md
 */

export type Role =
  | "Broker Owner"
  | "Admin/Ops"
  | "Team Lead"
  | "Agent"
  | "Read-only Viewer"
  | "ORVN Internal Admin";

export type Permission =
  | "view_all_leads"
  | "view_assigned_leads"
  | "view_calls"
  | "view_callbacks"
  | "view_bookings"
  | "view_pipeline_risks"
  | "view_recommendations"
  | "approve_recommendations"
  | "view_action_proposals"
  | "approve_action_proposals"
  | "view_simulation_lab"
  | "view_evidence_digest"
  | "view_agents"
  | "view_pas_brain"
  | "view_pas_room"
  | "manage_integrations"
  | "manage_settings"
  | "manage_users"
  | "view_billing"
  | "view_audit_logs"
  | "orvn_admin_access";

export interface DemoWorkspace {
  id: string;
  name: string;
  slug: string;
}

export interface DemoUser {
  id: string;
  name: string;
  email: string;
  initials: string;
  role: Role;
  permissions: Permission[];
}

/*
 * Person-owned identity profile (PAS301 §4 class A — portable).
 * Attributes of the PERSON, not the workspace: they travel with the person
 * across every workspace and survive departures. Display-only here.
 */
export interface DemoIdentityProfile {
  timezone: string;
  workingHours: string;
}

/*
 * Personal PAS configuration (PAS301 §4 class A / §15 — person-owned, portable).
 * The name and tone the person chose for their assistant. Display-only.
 */
export interface DemoAssistantPreferences {
  assistantName: string;
  tone: string;
}

/*
 * Auth placeholder status. PAS301A is a SHELL — there is no real sign-in.
 * The chosen direction (PAS301.5) is Google sign-in primary + email magic-link
 * fallback; both are wired in a later checkpoint, not here.
 */
export interface DemoAuthStatus {
  connected: false;
  current: string;
  plannedMethods: string[];
  note: string;
}

export interface DemoSession {
  mode: "demo";
  sessionLabel: string;
  permissionBoundary: string;
  workspace: DemoWorkspace;
  user: DemoUser;
  /* Person-owned (portable) — added in PAS301A. */
  profile: DemoIdentityProfile;
  assistant: DemoAssistantPreferences;
  /* Auth shell status — added in PAS301A. */
  auth: DemoAuthStatus;
}

/*
 * Role → permission sets.
 * Not enforced here — real enforcement is server-side.
 * This table documents the intended access model for the demo.
 */
export const ROLE_PERMISSIONS: Record<Role, Permission[]> = {
  "Broker Owner": [
    "view_all_leads",
    "view_assigned_leads",
    "view_calls",
    "view_callbacks",
    "view_bookings",
    "view_pipeline_risks",
    "view_recommendations",
    "approve_recommendations",
    "view_action_proposals",
    "approve_action_proposals",
    "view_simulation_lab",
    "view_evidence_digest",
    "view_agents",
    "view_pas_brain",
    "view_pas_room",
    "manage_integrations",
    "manage_settings",
    "manage_users",
    "view_billing",
    "view_audit_logs",
  ],
  "Admin/Ops": [
    "view_all_leads",
    "view_assigned_leads",
    "view_calls",
    "view_callbacks",
    "view_bookings",
    "view_pipeline_risks",
    "view_recommendations",
    "approve_recommendations",
    "view_action_proposals",
    "approve_action_proposals",
    "view_simulation_lab",
    "view_evidence_digest",
    "view_agents",
    "view_pas_brain",
    "view_pas_room",
    "manage_integrations",
    "manage_settings",
    "manage_users",
    "view_billing",
    "view_audit_logs",
  ],
  "Team Lead": [
    "view_all_leads",
    "view_assigned_leads",
    "view_calls",
    "view_callbacks",
    "view_bookings",
    "view_pipeline_risks",
    "view_recommendations",
    "view_action_proposals",
    "view_simulation_lab",
    "view_evidence_digest",
    "view_agents",
    "view_pas_brain",
    "view_pas_room",
  ],
  "Agent": [
    "view_assigned_leads",
    "view_calls",
    "view_callbacks",
    "view_bookings",
  ],
  "Read-only Viewer": [
    "view_all_leads",
    "view_calls",
    "view_bookings",
    "view_pipeline_risks",
    "view_recommendations",
    "view_evidence_digest",
  ],
  "ORVN Internal Admin": [
    "view_all_leads",
    "view_assigned_leads",
    "view_calls",
    "view_callbacks",
    "view_bookings",
    "view_pipeline_risks",
    "view_recommendations",
    "approve_recommendations",
    "view_action_proposals",
    "approve_action_proposals",
    "view_simulation_lab",
    "view_evidence_digest",
    "view_agents",
    "view_pas_brain",
    "view_pas_room",
    "manage_integrations",
    "manage_settings",
    "manage_users",
    "view_billing",
    "view_audit_logs",
    "orvn_admin_access",
  ],
};

export const DEMO_SESSION: DemoSession = {
  mode: "demo",
  sessionLabel: "Demo session",
  permissionBoundary: "Display-only",
  workspace: {
    id: "demo-orvn-realty",
    name: "ORVN Demo Realty",
    slug: "orvn-demo-realty",
  },
  user: {
    id: "demo-broker-owner",
    name: "Demo Broker",
    email: "demo@orvn.demo",
    initials: "DB",
    role: "Broker Owner",
    permissions: ROLE_PERMISSIONS["Broker Owner"],
  },
  profile: {
    timezone: "America/New_York (ET)",
    workingHours: "Mon–Fri · 8:00 AM – 6:00 PM",
  },
  assistant: {
    assistantName: "PAS",
    tone: "Calm · concise · proactive",
  },
  auth: {
    connected: false,
    current: "Demo session — real sign-in not connected yet",
    plannedMethods: ["Continue with Google", "Email magic link"],
    note: "Google sign-in / magic link will be wired in a later checkpoint.",
  },
};
