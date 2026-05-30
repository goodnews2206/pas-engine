/*
 * Demo recommendations — what PAS thinks should happen next. Frontend-only.
 * Relations: evidenceIds → evidence.
 */

import { DEMO_META, type Recommendation } from "./types";

export const DEMO_RECOMMENDATIONS: readonly Recommendation[] = [
  {
    ...DEMO_META,
    id: "REC-6601",
    title: "Touch three untouched Zillow leads from Tuesday",
    evidenceIds: ["EV-8804"],
    urgency: "needs_attention",
    impact: "Recovers leads before they go cold.",
    possibleAction: "Assign the batch to a covered agent for first contact.",
  },
  {
    ...DEMO_META,
    id: "REC-6602",
    title: "Recover the overdue 2pm callback",
    evidenceIds: ["EV-8802"],
    urgency: "urgent",
    impact: "Keeps a commitment that is already past due.",
    possibleAction: "Reassign and call within the hour.",
  },
  {
    ...DEMO_META,
    id: "REC-6603",
    title: "Coach Riverside B on first-response time",
    evidenceIds: ["EV-8803"],
    urgency: "fyi",
    impact: "Improves speed-to-lead across the team over time.",
    possibleAction: "Share this week's response-time view in a 1:1.",
  },
];
