/*
 * Demo agents for "Northwind Realty (DEMO)". Clearly fictional.
 * Consumed by the future /agents route and Command Center.
 */

import { DEMO_META, type Agent } from "./types";

export const DEMO_AGENTS: readonly Agent[] = [
  {
    ...DEMO_META,
    id: "AG-RIVERSIDE-01",
    name: "Demo Agent · Riverside A",
    role: "agent",
    responseSpeedMs: 240_000,
    callbacksOwned: 4,
    activeLeads: 18,
    coverageStatus: "covered",
    coachingFlags: [],
    permissionsRole: "agent",
  },
  {
    ...DEMO_META,
    id: "AG-RIVERSIDE-02",
    name: "Demo Agent · Riverside B",
    role: "agent",
    responseSpeedMs: 1_080_000,
    callbacksOwned: 6,
    activeLeads: 23,
    coverageStatus: "stretched",
    coachingFlags: ["slow_first_response", "callbacks_overdue"],
    permissionsRole: "agent",
  },
  {
    ...DEMO_META,
    id: "AG-LAKESHORE-01",
    name: "Demo Agent · Lakeshore A",
    role: "agent",
    responseSpeedMs: 360_000,
    callbacksOwned: 2,
    activeLeads: 11,
    coverageStatus: "covered",
    coachingFlags: [],
    permissionsRole: "agent",
  },
  {
    ...DEMO_META,
    id: "AG-LEAD-RIVERSIDE",
    name: "Demo Team Lead · Riverside",
    role: "team_lead",
    responseSpeedMs: 180_000,
    callbacksOwned: 0,
    activeLeads: 5,
    coverageStatus: "gap",
    coachingFlags: ["coverage_gap_friday_pm"],
    permissionsRole: "team_lead",
  },
];
