/*
 * BrainInsightStrip — compact "what PAS is learning" strip. Static, demo-only.
 * Reused on Command Center (a strip, not a redesign) and atop PAS Brain.
 * Shows the top candidate memories + a link to the full surface.
 */

import Link from "next/link";
import { DEMO_MEMORY_CANDIDATES } from "@/lib/demo/operational";
import ConfidenceLabel from "./ConfidenceLabel";
import styles from "./BrainInsightStrip.module.css";

interface Props {
  /** How many candidate memories to preview (default 2). */
  limit?: number;
}

export default function BrainInsightStrip({ limit = 2 }: Props) {
  const items = DEMO_MEMORY_CANDIDATES.slice(0, limit);

  return (
    <section className={styles.strip} aria-label="What PAS is learning">
      <div className={styles.top}>
        <p className={styles.label}>What PAS is learning</p>
        <span className={styles.demoPill}>Simulated</span>
      </div>

      <ul className={styles.list}>
        {items.map((memory) => (
          <li key={memory.id} className={styles.item}>
            <ConfidenceLabel confidence={memory.confidence} />
            <span className={styles.statement}>{memory.statement}</span>
          </li>
        ))}
      </ul>

      <div className={styles.footer}>
        <span className={styles.note}>
          Candidate memory — a human decides what becomes trusted.
        </span>
        <Link className={styles.link} href="/pas-brain">
          Open PAS Brain →
        </Link>
      </div>
    </section>
  );
}
