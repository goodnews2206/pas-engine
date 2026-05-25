import styles from "./Composer.module.css";

/*
 * Persistent PAS composer — Design System §11.3 / §16.1.
 * Always present on every dashboard page. One instance, never duplicated.
 * Not a chatbot bubble — feels like in-app staff communication.
 * No send functionality in this step; wired to PAS API in a later step.
 */
export default function Composer() {
  return (
    <div
      className={styles.composer}
      role="region"
      aria-label="PAS composer"
    >
      <div className={styles.inner}>
        {/* PAS presence indicator */}
        <div className={styles.presence} aria-label="PAS status: observing">
          <span className={styles.presenceDot} aria-hidden="true" />
          <span className={styles.presenceLabel}>PAS is observing</span>
        </div>

        {/* Compose input */}
        <textarea
          className={styles.input}
          placeholder="Ask PAS what needs attention, which leads are slipping, or what should happen next."
          rows={1}
          aria-label="Message PAS"
          aria-describedby="composer-hint"
        />

        {/* Keyboard shortcut hint */}
        <div className={styles.hint} id="composer-hint" aria-hidden="true">
          <kbd className={styles.kbd}>Enter</kbd>
          <span className={styles.hintText}>to ask</span>
        </div>
      </div>
    </div>
  );
}
