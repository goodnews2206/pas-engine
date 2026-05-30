/*
 * ProposalSnapshot — what PAS is proposing and recommending. Static RSC,
 * demo-only. Links to /action-proposals and /recommendations.
 */

import Link from "next/link";
import {
  DEMO_PROPOSALS,
  DEMO_RECOMMENDATIONS,
  type ProposalStatus,
} from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

const STATUS_LABELS: Record<ProposalStatus, string> = {
  candidate: "Awaiting approval",
  approved_for_manual_review: "Approved for review",
  rejected: "Rejected",
  deferred: "Deferred",
};

export default function ProposalSnapshot() {
  return (
    <section className={styles.snapshot} aria-label="What PAS is proposing">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>What PAS is proposing</h2>
        <Link href="/action-proposals" className={styles.moduleLink}>
          Action Proposals →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        PAS has enough evidence to propose {DEMO_PROPOSALS.length} bounded{" "}
        {DEMO_PROPOSALS.length === 1 ? "action" : "actions"}. Nothing happens
        until a human approves.
      </p>
      <ul className={styles.rows}>
        {DEMO_PROPOSALS.map((proposal) => (
          <li key={proposal.id} className={styles.row}>
            <div className={styles.rowMain}>
              <span className={styles.rowTitle}>{proposal.title}</span>
              <span className={styles.rowSub}>
                {proposal.id} · {proposal.scope}
              </span>
            </div>
            <span className={styles.rowValue}>
              {STATUS_LABELS[proposal.status]}
            </span>
          </li>
        ))}
      </ul>
      <p className={styles.snapshotLead}>
        PAS also has {DEMO_RECOMMENDATIONS.length} open{" "}
        {DEMO_RECOMMENDATIONS.length === 1 ? "recommendation" : "recommendations"}.{" "}
        <Link href="/recommendations" className={styles.moduleLink}>
          Recommendations →
        </Link>
      </p>
    </section>
  );
}
