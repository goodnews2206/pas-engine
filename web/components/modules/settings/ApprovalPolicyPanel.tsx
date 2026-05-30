/*
 * ApprovalPolicyPanel — the trust rules. Static, demo-only. Copy is local UI
 * policy text (clearly demo); references the integration model for write counts.
 */

import { DEMO_INTEGRATIONS } from "@/lib/demo/operational";
import styles from "./SettingsOverview.module.css";

export default function ApprovalPolicyPanel() {
  const writeEnabled = DEMO_INTEGRATIONS.filter(
    (i) => i.writeScope.length > 0,
  ).length;

  const policies = [
    {
      title: "Outbound re-engagement requires approval",
      desc: "PAS can draft a message, but a human approves before anything is sent.",
    },
    {
      title: "Action proposals require approval",
      desc: "Every bounded action waits for sign-off. Nothing runs automatically.",
    },
    {
      title: "Write-enabled integrations require approval",
      desc: `${writeEnabled} connectors can prepare a write — each one is approval-gated.`,
    },
    {
      title: "Critical notifications can override quiet hours",
      desc: "Only Critical breaks through. Everything else respects quiet hours.",
    },
    {
      title: "PAS cannot act live in demo mode",
      desc: "This workspace is in rehearsal. PAS has not changed live customer behavior.",
    },
  ];

  return (
    <section className={styles.panel} aria-label="Approval policy">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Approval policy</h2>
        <p className={styles.panelDesc}>
          What always needs a human. These are the guardrails that keep PAS a
          partner, not an autopilot.
        </p>
      </div>
      <div className={styles.grid2}>
        {policies.map((policy) => (
          <div key={policy.title} className={styles.card}>
            <h3 className={styles.cardTitle}>{policy.title}</h3>
            <p className={styles.cardDesc}>{policy.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
