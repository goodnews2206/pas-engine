/*
 * PAS operational demo data model — public barrel.
 *
 * Frontend-only. No backend, no API, no network, no mutations, no auth.
 * Later module PRs (B–I, see docs/pas_operational_demo_layer_plan.md §10)
 * import their demo data from here. Nothing in this module performs a
 * network call or any live behavior.
 */

// Types + closed vocabularies + safety meta
export * from "./types";

// Safety assertions (for later tests)
export * from "./assertions";

// Collections
export { ROLE_BUNDLES, DEMO_USERS } from "./permissions";
export { DEMO_AGENTS } from "./agents";
export { DEMO_LEADS } from "./leads";
export { DEMO_CALLS } from "./calls";
export { DEMO_CALLBACKS } from "./callbacks";
export { DEMO_BOOKINGS } from "./bookings";
export { DEMO_RISKS } from "./risks";
export { DEMO_RECOMMENDATIONS } from "./recommendations";
export { DEMO_PROPOSALS } from "./proposals";
export { DEMO_EVIDENCE } from "./evidence";
export { DEMO_INTEGRATIONS } from "./integrations";
export {
  DEMO_MEMORY_CANDIDATES,
  DEMO_BRAIN_QUERIES,
  DEMO_BRAIN_UNKNOWNS,
} from "./brain";
export {
  DEMO_NOTIFICATIONS,
  DEMO_NOTIFICATION_REPLIES,
  NOTIFICATION_REPLY_CONFIRMATION,
  DEMO_THREADS,
} from "./communication";

import { ROLE_BUNDLES, DEMO_USERS } from "./permissions";
import { DEMO_AGENTS } from "./agents";
import { DEMO_LEADS } from "./leads";
import { DEMO_CALLS } from "./calls";
import { DEMO_CALLBACKS } from "./callbacks";
import { DEMO_BOOKINGS } from "./bookings";
import { DEMO_RISKS } from "./risks";
import { DEMO_RECOMMENDATIONS } from "./recommendations";
import { DEMO_PROPOSALS } from "./proposals";
import { DEMO_EVIDENCE } from "./evidence";
import { DEMO_INTEGRATIONS } from "./integrations";
import { DEMO_MEMORY_CANDIDATES } from "./brain";
import { DEMO_NOTIFICATIONS, DEMO_THREADS } from "./communication";

/**
 * TypeScript-only sanity summary of the demo data model. Pure data, no
 * side effects — useful for a later "is the model wired?" smoke check.
 */
export const DEMO_DATA_MODEL = {
  version: "pr-a-v1",
  workspace: "Northwind Realty (DEMO)",
  demoOnly: true,
  noLiveBehavior: true,
  counts: {
    roleBundles: ROLE_BUNDLES.length,
    users: DEMO_USERS.length,
    agents: DEMO_AGENTS.length,
    leads: DEMO_LEADS.length,
    calls: DEMO_CALLS.length,
    callbacks: DEMO_CALLBACKS.length,
    bookings: DEMO_BOOKINGS.length,
    risks: DEMO_RISKS.length,
    recommendations: DEMO_RECOMMENDATIONS.length,
    proposals: DEMO_PROPOSALS.length,
    evidence: DEMO_EVIDENCE.length,
    integrations: DEMO_INTEGRATIONS.length,
    memoryCandidates: DEMO_MEMORY_CANDIDATES.length,
    notifications: DEMO_NOTIFICATIONS.length,
    threads: DEMO_THREADS.length,
  },
} as const;
