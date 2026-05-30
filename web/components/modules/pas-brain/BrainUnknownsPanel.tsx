/*
 * BrainUnknownsPanel — the edge of PAS's knowledge. Static, demo-only.
 * Honesty as a trust feature: PAS says plainly what it does not know yet.
 */

import { DEMO_BRAIN_UNKNOWNS } from "@/lib/demo/operational";
import styles from "./PasBrainOverview.module.css";

export default function BrainUnknownsPanel() {
  return (
    <section className={styles.panel} aria-label="What PAS does not know yet">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>What PAS does not know yet</h2>
        <p className={styles.panelDesc}>
          PAS only claims what it can support. These are the gaps — knowing them
          is part of being trustworthy.
        </p>
      </div>
      <ul className={styles.unknownList}>
        {DEMO_BRAIN_UNKNOWNS.map((unknown) => (
          <li key={unknown} className={styles.unknownItem}>
            <span className={styles.unknownMark} aria-hidden="true">
              ?
            </span>
            <span className={styles.unknownText}>{unknown}</span>
          </li>
        ))}
      </ul>
    </section>
  );
}
