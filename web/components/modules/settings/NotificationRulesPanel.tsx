/*
 * NotificationRulesPanel — five severities + quiet-hours logic. Static,
 * demo-only. Mirrors the notification architecture; display-only here.
 */

import styles from "./SettingsOverview.module.css";

const RULES: { label: string; chip: string; rule: string }[] = [
  { label: "FYI", chip: styles.sevFyi, rule: "Bell only. Respects quiet hours." },
  {
    label: "Needs attention",
    chip: styles.sevAttention,
    rule: "Bell + badge. Respects quiet hours.",
  },
  {
    label: "Urgent",
    chip: styles.sevUrgent,
    rule: "Bell + badge + toast. Respects quiet hours.",
  },
  {
    label: "Approval required",
    chip: styles.sevApproval,
    rule: "Surfaced until acted on. Respects quiet hours.",
  },
  {
    label: "Critical",
    chip: styles.sevCritical,
    rule: "Banner + push. Overrides quiet hours.",
  },
];

export default function NotificationRulesPanel() {
  return (
    <section className={styles.panel} aria-label="Notification rules">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Notification rules</h2>
        <p className={styles.panelDesc}>
          How loud each signal is allowed to be. Quiet hours hold everything
          except Critical.
        </p>
      </div>

      <div>
        {RULES.map((rule) => (
          <div key={rule.label} className={styles.sevRow}>
            <span className={`${styles.sevChip} ${rule.chip}`}>{rule.label}</span>
            <span className={styles.sevRule}>{rule.rule}</span>
          </div>
        ))}
      </div>

      <p className={styles.lockedNote}>
        Quiet hours: 8:00 PM – 7:00 AM (demo default). Editing connects later.
      </p>
    </section>
  );
}
