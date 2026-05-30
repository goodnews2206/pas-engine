/*
 * OperatingBrief — the one-glance brokerage brief. Static RSC, demo-only.
 * Headline counts derive from the operational model.
 */

import {
  DEMO_CALLBACKS,
  DEMO_LEADS,
  DEMO_PROPOSALS,
} from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

export default function OperatingBrief() {
  const overdue = DEMO_CALLBACKS.filter((c) => c.status === "overdue").length;
  const slipping = DEMO_LEADS.filter(
    (l) => l.riskLevel === "urgent" || l.riskLevel === "needs_attention",
  ).length;
  const proposals = DEMO_PROPOSALS.length;
  const total = overdue + slipping + proposals;

  return (
    <header className={styles.brief}>
      <div className={styles.briefTop}>
        <h1 className={styles.briefTitle}>Command Center</h1>
        <span className={styles.demoPill}>Simulated</span>
      </div>
      <p className={styles.briefHeadline}>
        PAS has found {total} {total === 1 ? "thing" : "things"} worth a look
        before the day gets away — {overdue} overdue{" "}
        {overdue === 1 ? "promise" : "promises"}, {slipping}{" "}
        {slipping === 1 ? "lead" : "leads"} slipping, and {proposals} bounded{" "}
        {proposals === 1 ? "action" : "actions"} waiting on your approval.
      </p>
      <p className={styles.rehearsalNote}>
        Rehearsal mode — every number here is simulated.
      </p>
    </header>
  );
}
