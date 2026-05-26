/*
 * CommandCenterHeader — operating summary and rehearsal context.
 * Static RSC. Data from build-time demo constants only.
 */

import {
  OPERATING_SUMMARY,
  ATTENTION_ITEMS,
  RECOMMENDATION_CARDS,
} from "@/lib/demo/commandCenter";
import styles from "./CommandCenterHeader.module.css";

export default function CommandCenterHeader() {
  return (
    <section className={styles.header} aria-label="Operating summary">
      <p className={styles.rehearsalBadge} role="note">
        Rehearsal mode — demo snapshot
      </p>
      <p className={styles.headline}>{OPERATING_SUMMARY.headline}</p>
      <p className={styles.context}>{OPERATING_SUMMARY.context}</p>
      <div className={styles.counts}>
        <span className={styles.countItem}>
          <span className={styles.countNum}>{ATTENTION_ITEMS.length}</span>{" "}
          items need attention
        </span>
        <span className={styles.countSep} aria-hidden="true">·</span>
        <span className={styles.countItem}>
          <span className={styles.countNum}>{RECOMMENDATION_CARDS.length}</span>{" "}
          proposals awaiting review
        </span>
      </div>
    </section>
  );
}
