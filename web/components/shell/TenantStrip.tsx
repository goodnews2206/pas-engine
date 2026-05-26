/*
 * TenantStrip — workspace context strip. Dashboard IA §3.7.
 * Static RSC. Session fields derived from DEMO_SESSION (build-time constant).
 * Replace with real session context in the auth step.
 */

import { DEMO_SESSION } from "@/lib/session/demoSession";
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

const { workspace, user, sessionLabel, permissionBoundary } = DEMO_SESSION;

export default function TenantStrip() {
  return (
    <div className={styles.strip} role="complementary" aria-label="Workspace context">
      {/* Left: workspace context items */}
      <div className={styles.context}>
        <span className={styles.item}>
          <span className={styles.label}>Workspace</span>
          <span className={styles.value}>{workspace.name}</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>User</span>
          <span className={styles.value}>{user.name}</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Role</span>
          <span className={styles.value}>{user.role}</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Session</span>
          <span className={styles.value}>{sessionLabel}</span>
        </span>
        <span className={styles.sep} aria-hidden="true">·</span>
        <span className={styles.item}>
          <span className={styles.label}>Permissions</span>
          <span className={styles.value}>{permissionBoundary}</span>
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
