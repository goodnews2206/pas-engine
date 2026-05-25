import styles from "./DemoBanner.module.css";

/*
 * Persistent demo/rehearsal banner — Design System §26.
 * Non-removable by user theme preference.
 * Copy from Product Design Book §8.5 (adapted per Step 3 brief).
 */
export default function DemoBanner() {
  return (
    <div
      className={styles.banner}
      role="status"
      aria-live="polite"
      aria-label="Rehearsal workspace notice"
    >
      <span className={styles.indicator} aria-hidden="true" />
      <span className={styles.copy}>
        This is a demo / rehearsal workspace. PAS has not changed live customer
        behavior.
      </span>
    </div>
  );
}
