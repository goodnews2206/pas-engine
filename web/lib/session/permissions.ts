/*
 * PAS Permission helpers — frontend display scaffold only.
 *
 * DISPLAY-ONLY. Not a security boundary.
 * Real permission enforcement belongs to the backend auth layer.
 * These helpers drive navigation visibility and UI state only.
 *
 * Authority: docs/pas_web_session_permission_scaffold.md
 */

import type { DemoSession, Permission } from "./demoSession";
import { ROUTES } from "@/lib/navigation/routes";
import type { RouteDefinition, NavGroup, NavFamily } from "@/lib/navigation/routes";

export function hasPermission(
  session: DemoSession,
  permission: Permission
): boolean {
  return session.user.permissions.includes(permission);
}

export function hasAnyPermission(
  session: DemoSession,
  permissions: Permission[]
): boolean {
  return permissions.some((p) => hasPermission(session, p));
}

export function canViewRoute(
  session: DemoSession,
  route: RouteDefinition
): boolean {
  if (route.requiredPermissions.length === 0) return true;
  return hasAnyPermission(session, route.requiredPermissions);
}

export function getVisibleRoutesForSession(
  session: DemoSession
): RouteDefinition[] {
  return ROUTES.filter((r) => canViewRoute(session, r));
}

const FAMILY_ORDER: NavFamily[] = [
  "Operate",
  "Notice",
  "People",
  "System",
  "ORVN",
];

export function getNavGroupsForSession(session: DemoSession): NavGroup[] {
  const visible = getVisibleRoutesForSession(session);
  return FAMILY_ORDER.map((family) => ({
    family,
    routes: visible.filter((r) => r.family === family),
  })).filter((g) => g.routes.length > 0);
}

export function getSessionRoleLabel(session: DemoSession): string {
  return session.user.role;
}
