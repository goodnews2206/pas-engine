/*
 * LeadsOverview — operational demo for /leads. Static RSC, demo-only.
 * Answers: which leads are active · which are slipping · who owns them ·
 * what should happen next. Consumes DEMO_LEADS + related callbacks/calls.
 */

import {
  DEMO_LEADS,
  DEMO_CALLBACKS,
  DEMO_CALLS,
} from "@/lib/demo/operational";
import ContinuityHeader from "@/components/modules/continuity/ContinuityHeader";
import ContinuityMetricStrip from "@/components/modules/continuity/ContinuityMetricStrip";
import LeadCard from "./LeadCard";
import styles from "@/components/modules/continuity/continuity.module.css";

export default function LeadsOverview() {
  const callbacksByLead: Record<string, number> = {};
  for (const cb of DEMO_CALLBACKS) {
    callbacksByLead[cb.leadId] = (callbacksByLead[cb.leadId] ?? 0) + 1;
  }
  const callsByLead: Record<string, number> = {};
  for (const call of DEMO_CALLS) {
    callsByLead[call.leadId] = (callsByLead[call.leadId] ?? 0) + 1;
  }

  const slipping = DEMO_LEADS.filter(
    (l) => l.riskLevel === "urgent" || l.riskLevel === "needs_attention",
  ).length;
  const owners = new Set(DEMO_LEADS.map((l) => l.ownerId)).size;

  return (
    <>
      <ContinuityHeader
        title="Leads"
        intro="Every lead PAS is tracking — where it came from, who owns it, and what should happen next before it goes cold."
      />

      <ContinuityMetricStrip
        ariaLabel="Lead summary"
        metrics={[
          { label: "Active leads", value: DEMO_LEADS.length },
          { label: "Slipping", value: slipping, tone: slipping > 0 ? "urgent" : "fyi" },
          { label: "Owners", value: owners },
        ]}
      />

      <ul className={styles.recordList} aria-label="Leads">
        {DEMO_LEADS.map((lead) => (
          <LeadCard
            key={lead.id}
            lead={lead}
            callbackCount={callbacksByLead[lead.id] ?? 0}
            callCount={callsByLead[lead.id] ?? 0}
          />
        ))}
      </ul>

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
