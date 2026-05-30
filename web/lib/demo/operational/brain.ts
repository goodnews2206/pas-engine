/*
 * Demo PAS Brain — memory candidates + learned signals. Frontend-only.
 * Every statement is graded by confidence and linked to evidence.
 * "Memory" here is seeded fictional data, not learned from real activity.
 */

import { DEMO_META, type MemoryCandidate } from "./types";

export const DEMO_MEMORY_CANDIDATES: readonly MemoryCandidate[] = [
  {
    ...DEMO_META,
    id: "MEM-9901",
    statement:
      "Riverside leads from Zillow convert faster when first contact is under 10 minutes.",
    confidence: "likely",
    evidenceIds: ["EV-8803", "EV-8804"],
    status: "candidate",
  },
  {
    ...DEMO_META,
    id: "MEM-9902",
    statement:
      "Overdue callbacks on the Riverside team cluster on Friday afternoons.",
    confidence: "observed",
    evidenceIds: ["EV-8802"],
    status: "candidate",
  },
  {
    ...DEMO_META,
    id: "MEM-9903",
    statement:
      "Long-horizon buyers respond better to monthly market notes than weekly outreach.",
    confidence: "uncertain",
    evidenceIds: [],
    status: "candidate",
  },
];

/** Example queries PAS can answer — seeds the Brain surface and composer. */
export const DEMO_BRAIN_QUERIES: readonly string[] = [
  "Which callbacks are overdue right now?",
  "Which leads have had no first touch today?",
  "Why is lead D-1042 flagged as worth attention?",
  "Which agent is most stretched this week?",
];

/** Explicit edge-of-knowledge — honesty as a trust feature. */
export const DEMO_BRAIN_UNKNOWNS: readonly string[] = [
  "PAS does not yet know live CRM data — integrations are demo-only.",
  "PAS does not yet track outcomes after a booking is completed.",
  "PAS cannot confirm whether a callback was actually made off-platform.",
];
