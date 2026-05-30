/*
 * Demo role bundles + users. Frontend-only, display shaping only —
 * NOT a security boundary (real enforcement is sequence Step 18).
 * Simple built-in bundles with toggles, not an RBAC matrix.
 */

import { DEMO_META, type RoleBundle, type User } from "./types";

function perm(key: string, label: string, allowed: boolean) {
  return { key, label, allowed };
}

export const ROLE_BUNDLES: readonly RoleBundle[] = [
  {
    role: "broker_owner",
    label: "Broker Owner",
    description: "Full visibility and approval authority across the brokerage.",
    permissions: [
      perm("view_all", "View all modules", true),
      perm("approve_proposals", "Approve action proposals", true),
      perm("manage_members", "Manage members & roles", true),
      perm("edit_settings", "Edit workspace settings", true),
    ],
  },
  {
    role: "admin",
    label: "Admin / Ops Manager",
    description: "Operational control without ownership-level billing access.",
    permissions: [
      perm("view_all", "View all modules", true),
      perm("approve_proposals", "Approve action proposals", true),
      perm("manage_members", "Manage members & roles", true),
      perm("edit_settings", "Edit workspace settings", true),
    ],
  },
  {
    role: "team_lead",
    label: "Team Lead",
    description: "Visibility and coordination scoped to their team.",
    permissions: [
      perm("view_team", "View team modules", true),
      perm("approve_proposals", "Approve action proposals", false),
      perm("manage_members", "Manage members & roles", false),
      perm("edit_settings", "Edit workspace settings", false),
    ],
  },
  {
    role: "agent",
    label: "Agent",
    description: "Their own leads, calls, callbacks and bookings.",
    permissions: [
      perm("view_own", "View own objects", true),
      perm("approve_proposals", "Approve action proposals", false),
      perm("manage_members", "Manage members & roles", false),
      perm("edit_settings", "Edit workspace settings", false),
    ],
  },
  {
    role: "viewer",
    label: "Viewer",
    description: "Read-only visibility, no actions.",
    permissions: [
      perm("view_readonly", "Read-only visibility", true),
      perm("approve_proposals", "Approve action proposals", false),
      perm("manage_members", "Manage members & roles", false),
      perm("edit_settings", "Edit workspace settings", false),
    ],
  },
  {
    role: "orvn_internal_admin",
    label: "ORVN Internal Admin",
    description: "ORVN Labs cross-tenant support and incident access.",
    permissions: [
      perm("view_all", "View all modules", true),
      perm("approve_proposals", "Approve action proposals", false),
      perm("manage_members", "Manage members & roles", true),
      perm("edit_settings", "Edit workspace settings", true),
    ],
  },
];

export const DEMO_USERS: readonly User[] = [
  {
    ...DEMO_META,
    id: "U-OWNER-01",
    name: "Demo Broker · Northwind",
    email: "owner@northwind-demo.local",
    role: "broker_owner",
    status: "active",
  },
  {
    ...DEMO_META,
    id: "U-ADMIN-01",
    name: "Demo Ops Manager · Northwind",
    email: "ops@northwind-demo.local",
    role: "admin",
    status: "active",
  },
  {
    ...DEMO_META,
    id: "U-LEAD-01",
    name: "Demo Team Lead · Riverside",
    email: "lead.riverside@northwind-demo.local",
    role: "team_lead",
    status: "active",
  },
];
