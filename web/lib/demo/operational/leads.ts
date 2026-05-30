/*
 * Demo leads for Northwind Realty (DEMO). Clearly fictional, opaque IDs.
 * Relations: ownerId → agents.
 */

import { DEMO_META, type Lead } from "./types";

export const DEMO_LEADS: readonly Lead[] = [
  {
    ...DEMO_META,
    id: "D-1042",
    source: "Zillow (demo)",
    ownerId: "AG-RIVERSIDE-01",
    stage: "qualified",
    lastTouch: "2026-05-29T16:10:00Z",
    riskLevel: "needs_attention",
    nextAction: "Confirm budget and schedule a showing.",
    pasNote: "Asked about closing timeline twice — warm. (simulated)",
  },
  {
    ...DEMO_META,
    id: "D-1043",
    source: "Realtor.com (demo)",
    ownerId: "AG-RIVERSIDE-02",
    stage: "new",
    lastTouch: "2026-05-29T13:02:00Z",
    riskLevel: "urgent",
    nextAction: "First touch overdue — call now.",
    pasNote: "No first response in 26h. Slipping. (simulated)",
  },
  {
    ...DEMO_META,
    id: "D-1044",
    source: "Facebook Lead Ads (demo)",
    ownerId: "AG-LAKESHORE-01",
    stage: "nurturing",
    lastTouch: "2026-05-28T18:45:00Z",
    riskLevel: "fyi",
    nextAction: "Send the monthly market note.",
    pasNote: "Long-horizon buyer, ~6 months out. (simulated)",
  },
  {
    ...DEMO_META,
    id: "D-1045",
    source: "Website Form (demo)",
    ownerId: "AG-RIVERSIDE-01",
    stage: "appointment_set",
    lastTouch: "2026-05-29T09:20:00Z",
    riskLevel: "fyi",
    nextAction: "Prepare comps for the Thursday showing.",
    pasNote: "Booking BK-4401 confirmed. (simulated)",
  },
];
