/*
 * Sidebar — persistent shell primitive. Design System §9.
 * Static RSC wrapper; NavList is the client boundary for pathname detection.
 *
 * Display-only scaffold. Real security belongs to the backend/auth layer.
 * Workspace and role data comes from DEMO_SESSION (build-time constant).
 * Replace with real session context in the auth step.
 */

import NavList from "./NavList";
import WorkspaceSwitcher from "./WorkspaceSwitcher";
import { DEMO_SESSION } from "@/lib/session/demoSession";
import styles from "./Sidebar.module.css";

const { workspace, user } = DEMO_SESSION;

export default function Sidebar() {
  return (
    <aside className={styles.sidebar} aria-label="Main navigation">
      {/* Wordmark + brand */}
      <div className={styles.header}>
        <span className={styles.wordmark}>PAS</span>
        <span className={styles.brand}>ORVN Labs</span>
      </div>

      {/* Workspace shell — active workspace, role/hat, inert switcher (PAS301B) */}
      <WorkspaceSwitcher />

      {/* Module navigation — client component for pathname-aware active state */}
      <nav className={styles.nav} aria-label="Module navigation">
        <NavList />
      </nav>

      {/* Footer: identity slot */}
      <div className={styles.footer} aria-label="Workspace identity">
        <span className={styles.footerWorkspace}>{workspace.name}</span>
        <span className={styles.footerRole}>{user.role}</span>
      </div>
    </aside>
  );
}
