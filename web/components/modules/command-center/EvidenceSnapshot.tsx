/*
 * EvidenceSnapshot — the receipts behind today's signals. Static RSC,
 * demo-only. Summaries only. Links to /pas-brain.
 */

import Link from "next/link";
import { DEMO_EVIDENCE } from "@/lib/demo/operational";
import styles from "./CommandCenterOverview.module.css";

export default function EvidenceSnapshot() {
  const items = DEMO_EVIDENCE.slice(0, 3);

  return (
    <section className={styles.snapshot} aria-label="Evidence">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>What the evidence shows</h2>
        <Link href="/pas-brain" className={styles.moduleLink}>
          PAS Brain →
        </Link>
      </div>
      <p className={styles.snapshotLead}>
        Every signal points back to a receipt. Open one to see the source.
      </p>
      <ul className={styles.rows}>
        {items.map((evidence) => (
          <li key={evidence.id} className={styles.evidenceRow}>
            <a href={evidence.link} className={styles.evidenceId}>
              {evidence.id}
            </a>
            <span className={styles.evidenceText}>{evidence.summary}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
