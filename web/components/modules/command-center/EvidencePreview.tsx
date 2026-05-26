/*
 * EvidencePreview — rehearsal evidence signals.
 * Static RSC. All signals are clearly labelled as demo/simulated.
 * Authority: docs/pas_notification_architecture.md §10 invariant 6.
 */

import { EVIDENCE_SIGNALS } from "@/lib/demo/commandCenter";
import styles from "./EvidencePreview.module.css";

export default function EvidencePreview() {
  return (
    <section className={styles.section} aria-label="Rehearsal evidence">
      <header className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>Rehearsal evidence</h2>
        <span className={styles.demoChip}>Simulated signals</span>
      </header>
      <ul className={styles.items}>
        {EVIDENCE_SIGNALS.map((item) => (
          <li key={item.id} className={styles.item}>
            <p className={styles.signal}>{item.signal}</p>
            <p className={styles.source}>Source: {item.source}</p>
          </li>
        ))}
      </ul>
      <p className={styles.disclaimer}>
        Rehearsal evidence only — not from live calls or live brokerage data.
      </p>
    </section>
  );
}
