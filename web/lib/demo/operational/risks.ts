/*
 * Demo pipeline risks. Frontend-only.
 * Relations: affectedLeadIds → leads.
 */

import { DEMO_META, type PipelineRisk } from "./types";

export const DEMO_RISKS: readonly PipelineRisk[] = [
  {
    ...DEMO_META,
    id: "RISK-5501",
    severity: "urgent",
    reason: "First-response time slipping on new Realtor.com leads.",
    affectedLeadIds: ["D-1043"],
    suggestedRecovery: "Rebalance new-lead routing away from stretched agents.",
  },
  {
    ...DEMO_META,
    id: "RISK-5502",
    severity: "needs_attention",
    reason: "Overdue callback with no recovery attempt logged.",
    affectedLeadIds: ["D-1043"],
    suggestedRecovery: "Trigger the callback recovery proposal PROP-7701.",
  },
  {
    ...DEMO_META,
    id: "RISK-5503",
    severity: "fyi",
    reason: "Friday afternoon coverage gap on the Riverside team.",
    affectedLeadIds: ["D-1042", "D-1045"],
    suggestedRecovery: "Confirm on-call coverage before Friday 3pm.",
  },
];
