/*
 * SettingsOverview — calm trust controls for /settings. Static RSC, demo-only.
 * Answers: who belongs here · what each role can do · what needs approval ·
 * which signals are urgent · what's connected · what session is active · where
 * sign-out will live. No backend, no auth, no persistence.
 */

import WorkspaceProfilePanel from "./WorkspaceProfilePanel";
import AccountShellPanel from "./AccountShellPanel";
import MembersPanel from "./MembersPanel";
import RolePermissionsPanel from "./RolePermissionsPanel";
import ApprovalPolicyPanel from "./ApprovalPolicyPanel";
import NotificationRulesPanel from "./NotificationRulesPanel";
import PasBehaviorPanel from "./PasBehaviorPanel";
import styles from "./SettingsOverview.module.css";

export default function SettingsOverview() {
  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerTop}>
          <h1 className={styles.title}>Settings</h1>
          <span className={styles.demoPill}>Simulated</span>
        </div>
        <p className={styles.intro}>
          What PAS can see, what PAS can do, and what always needs a human. These
          are trust controls — not admin clutter.
        </p>
        <p className={styles.rehearsalNote}>
          Rehearsal mode — these controls are display-only.
        </p>
      </header>

      <WorkspaceProfilePanel />
      <AccountShellPanel />
      <MembersPanel />
      <RolePermissionsPanel />
      <ApprovalPolicyPanel />
      <NotificationRulesPanel />
      <PasBehaviorPanel />

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. PAS has not changed live customer behavior.
      </p>
    </>
  );
}
