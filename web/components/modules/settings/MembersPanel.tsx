/*
 * MembersPanel — workspace people (managers + agents). Static, demo-only.
 * Resolves role labels from ROLE_BUNDLES. Management is demo-only.
 */

import {
  DEMO_USERS,
  DEMO_AGENTS,
  ROLE_BUNDLES,
  type Role,
} from "@/lib/demo/operational";
import styles from "./SettingsOverview.module.css";

const ROLE_LABEL: Record<Role, string> = Object.fromEntries(
  ROLE_BUNDLES.map((b) => [b.role, b.label]),
) as Record<Role, string>;

const COVERAGE_LABEL: Record<string, string> = {
  covered: "Available",
  stretched: "Stretched",
  gap: "Coverage gap",
};

export default function MembersPanel() {
  return (
    <section className={styles.panel} aria-label="Members">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Members</h2>
        <p className={styles.panelDesc}>
          Everyone in the workspace and the role bundle they carry. Inviting and
          editing members connects when the backend is wired.
        </p>
      </div>

      <div>
        {DEMO_USERS.map((user) => (
          <div key={user.id} className={styles.memberRow}>
            <div className={styles.memberMain}>
              <span className={styles.memberName}>{user.name}</span>
              <span className={styles.memberSub}>{user.email}</span>
            </div>
            <div className={styles.memberRight}>
              <span className={styles.roleChip}>{ROLE_LABEL[user.role]}</span>
              <span className={styles.statusChip}>Active</span>
            </div>
          </div>
        ))}

        {DEMO_AGENTS.map((agent) => (
          <div key={agent.id} className={styles.memberRow}>
            <div className={styles.memberMain}>
              <span className={styles.memberName}>{agent.name}</span>
              <span className={styles.memberSub}>{agent.id}</span>
            </div>
            <div className={styles.memberRight}>
              <span className={styles.roleChip}>{ROLE_LABEL[agent.role]}</span>
              <span className={styles.statusChip}>
                {COVERAGE_LABEL[agent.coverageStatus] ?? "Active"}
              </span>
            </div>
          </div>
        ))}
      </div>

      <p className={styles.lockedNote}>
        Member management is demo-only. No invitations are sent.
      </p>
    </section>
  );
}
