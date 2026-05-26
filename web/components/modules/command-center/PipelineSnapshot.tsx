/*
 * PipelineSnapshot — today's pipeline at a glance.
 * Dashboard IA §4.1 item 3. Static RSC. Demo numbers only.
 */

import { PIPELINE_ROWS } from "@/lib/demo/commandCenter";
import styles from "./PipelineSnapshot.module.css";

export default function PipelineSnapshot() {
  return (
    <section className={styles.section} aria-label="Today's pipeline">
      <header className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>Today&rsquo;s pipeline</h2>
        <span className={styles.demoChip}>Demo snapshot</span>
      </header>
      <ul className={styles.rows}>
        {PIPELINE_ROWS.map((row) => (
          <li key={row.id} className={styles.row}>
            <span className={styles.rowLabel}>{row.label}</span>
            {row.hint && (
              <span
                className={`${styles.rowHint} ${
                  row.severityHint === "attention"
                    ? styles.rowHintAttention
                    : ""
                }`}
              >
                {row.hint}
              </span>
            )}
            <span className={styles.rowCount}>{row.count}</span>
          </li>
        ))}
      </ul>
      <p className={styles.disclaimer}>
        Example pipeline — demo data only. PAS has not changed live customer
        behavior.
      </p>
    </section>
  );
}
