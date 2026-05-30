/*
 * AccountShellPanel — the account/session shell. Static, demo-only.
 * Sign-out is inert: real auth lands in a later step (sequence Step 17).
 */

import { DEMO_SESSION } from "@/lib/session/demoSession";
import styles from "./SettingsOverview.module.css";

export default function AccountShellPanel() {
  const { user, workspace, sessionLabel, permissionBoundary } = DEMO_SESSION;

  const fields = [
    { label: "Signed in as", value: user.name },
    { label: "Role", value: user.role },
    { label: "Workspace", value: workspace.name },
    { label: "Session mode", value: sessionLabel },
    { label: "Permission boundary", value: permissionBoundary },
  ];

  return (
    <section className={styles.panel} aria-label="Account">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Account</h2>
        <p className={styles.panelDesc}>
          The session you are viewing PAS with. Real sign-in arrives with
          authentication.
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

      <div className={styles.signOutRow}>
        <button type="button" className={styles.signOutBtn} disabled>
          Sign out
        </button>
        <p className={styles.signOutNote}>
          Sign out connects when real authentication is enabled.
        </p>
      </div>
    </section>
  );
}
