/*
 * WorkspaceProfilePanel — workspace identity. Static, demo-only.
 * Sourced from the demo session scaffold (no persistence).
 */

import { DEMO_SESSION } from "@/lib/session/demoSession";
import styles from "./SettingsOverview.module.css";

export default function WorkspaceProfilePanel() {
  const { workspace, sessionLabel } = DEMO_SESSION;

  const fields = [
    { label: "Workspace", value: workspace.name },
    { label: "Slug", value: workspace.slug },
    { label: "Mode", value: sessionLabel },
    { label: "Operating posture", value: "Read-first · approval-gated" },
  ];

  return (
    <section className={styles.panel} aria-label="Workspace profile">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Workspace</h2>
        <p className={styles.panelDesc}>
          The brokerage PAS is operating for. Profile editing connects when the
          backend is wired.
        </p>
      </div>
      <div className={styles.accountGrid}>
        {fields.map((field) => (
          <div key={field.label} className={styles.accountField}>
            <span className={styles.accountLabel}>{field.label}</span>
            <span className={styles.accountValue}>{field.value}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
