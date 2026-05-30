/*
 * RolePermissionsPanel — six role bundles as simple cards (not an RBAC grid).
 * Static, demo-only. Shows purpose, permission count, can-do and cannot-do.
 */

import { ROLE_BUNDLES } from "@/lib/demo/operational";
import styles from "./SettingsOverview.module.css";

export default function RolePermissionsPanel() {
  return (
    <section className={styles.panel} aria-label="Roles and permissions">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Roles &amp; permissions</h2>
        <p className={styles.panelDesc}>
          What each role can see and do. Simple bundles, not a permission grid —
          PAS never lets the UI offer more than the role allows.
        </p>
      </div>

      <div className={styles.grid3}>
        {ROLE_BUNDLES.map((bundle) => {
          const can = bundle.permissions.filter((p) => p.allowed);
          const cannot = bundle.permissions.filter((p) => !p.allowed);
          return (
            <div key={bundle.role} className={styles.card}>
              <div className={styles.cardHeaderRow}>
                <h3 className={styles.cardTitle}>{bundle.label}</h3>
                <span className={styles.countChip}>
                  {can.length}/{bundle.permissions.length}
                </span>
              </div>
              <p className={styles.cardDesc}>{bundle.description}</p>

              <div>
                <p className={styles.capLabel}>Can</p>
                <ul className={styles.list}>
                  {can.map((p) => (
                    <li key={p.key} className={styles.listItem}>
                      {p.label}
                    </li>
                  ))}
                </ul>
              </div>

              {cannot.length > 0 && (
                <div>
                  <p className={styles.capLabel}>Cannot</p>
                  <ul className={styles.list}>
                    {cannot.map((p) => (
                      <li key={p.key} className={styles.listItemNo}>
                        {p.label}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          );
        })}
      </div>
      <p className={styles.lockedNote}>
        Display-only — real enforcement is server-side. Demo / rehearsal.
      </p>
    </section>
  );
}
