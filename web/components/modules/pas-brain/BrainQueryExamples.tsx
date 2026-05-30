/*
 * BrainQueryExamples — what the brokerage can be asked. Static, demo-only.
 * Queries come from the model (DEMO_BRAIN_QUERIES); these are illustrative,
 * not executable — there is no live search.
 */

import { DEMO_BRAIN_QUERIES } from "@/lib/demo/operational";
import styles from "./PasBrainOverview.module.css";

export default function BrainQueryExamples() {
  return (
    <section className={styles.panel} aria-label="What you can ask PAS">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>What you can ask PAS</h2>
        <p className={styles.panelDesc}>
          Your brokerage is queryable in plain English. Examples — ask these in
          the composer below.
        </p>
      </div>
      <ul className={styles.queryList}>
        {DEMO_BRAIN_QUERIES.map((query) => (
          <li key={query} className={styles.queryItem}>
            <span className={styles.queryPrompt} aria-hidden="true">
              ?
            </span>
            <span className={styles.queryText}>{query}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
