import styles from "./TenantStrip.module.css";

/* Severity levels — visible as static labels per component inventory §10 */
const SEVERITY_LEVELS = [
  { label: "FYI", token: "fyi" },
  { label: "Needs attention", token: "attention" },
  { label: "Urgent", token: "urgent" },
  { label: "Approval required", token: "approval" },
  { label: "Critical", token: "critical" },
] as const;

type SeverityToken = (typeof SEVERITY_LEVELS)[number]["token"];

function severityClass(token: SeverityToken): string {
  const map: Record<SeverityToken, string> = {
    fyi: styles["level-fyi"],
    attention: styles["level-attention"],
    urgent: styles["level-urgent"],
    approval: styles["level-approval"],
    critical: styles["level-critical"],
  };
  return map[token];
}

export default function TenantStrip() {
  return (
    <div className={styles.strip} role="complementary" aria-label="Workspace context">
      {/* Left: workspace context items */}
      <div className={styles.context}>
        <span className={styles.item}>
          <span className={styles.label}>Workspace</span>
          <span className={styles.value}>ORVN Demo Realty</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Role</span>
          <span className={styles.value}>Broker Owner</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Data</span>
          <span className={styles.value}>Demo / rehearsal</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Backend</span>
          <span className={styles.value}>Railway</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Web</span>
          <span className={styles.value}>Vercel-ready</span>
        </span>
      </div>

      {/* Right: notification severity level indicators */}
      <ol
        className={styles.presenceRail}
        aria-label="Notification severity levels"
      >
        {SEVERITY_LEVELS.map((level) => (
          <li
            key={level.token}
            className={`${styles.level} ${severityClass(level.token)}`}
          >
            <span className={styles.levelDot} aria-hidden="true" />
            <span className={styles.levelLabel}>{level.label}</span>
          </li>
        ))}
      </ol>
    </div>
  );
}
