import NavList from "./NavList";
import styles from "./Sidebar.module.css";

/*
 * Sidebar — persistent shell primitive. Design System §9.
 * Static RSC wrapper; NavList is the client boundary for pathname detection.
 */
export default function Sidebar() {
  return (
    <aside className={styles.sidebar} aria-label="Main navigation">
      {/* Wordmark + brand */}
      <div className={styles.header}>
        <span className={styles.wordmark}>PAS</span>
        <span className={styles.brand}>ORVN Labs</span>
      </div>

      {/* Workspace context + role */}
      <div className={styles.workspace}>
        <span className={styles.workspaceName}>ORVN Demo Realty</span>
        <span className={styles.roleChip} aria-label="Role: Broker Owner">
          Broker Owner
        </span>
      </div>

      {/* Module navigation — client component for pathname-aware active state */}
      <nav className={styles.nav} aria-label="Module navigation">
        <NavList />
      </nav>

      {/* Footer: identity slot */}
      <div className={styles.footer} aria-label="Workspace identity">
        <span className={styles.footerWorkspace}>ORVN Demo Realty</span>
        <span className={styles.footerRole}>Broker Owner</span>
      </div>
    </aside>
  );
}
