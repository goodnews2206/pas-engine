import styles from "./Sidebar.module.css";

type NavItem = { label: string; active?: boolean };
type NavGroup = { group: string; items: NavItem[] };

const NAV: NavGroup[] = [
  {
    group: "Operate",
    items: [
      { label: "Command Center", active: true },
      { label: "Leads" },
      { label: "Calls" },
      { label: "Callbacks" },
      { label: "Bookings" },
    ],
  },
  {
    group: "Notice",
    items: [
      { label: "Pipeline Risks" },
      { label: "Recommendations" },
      { label: "Action Proposals" },
      { label: "Evidence Digest" },
    ],
  },
  {
    group: "System",
    items: [
      { label: "Simulation Lab" },
      { label: "Integrations" },
      { label: "Settings" },
    ],
  },
];

/*
 * People family (Agents, In-App Communication, Notifications) is hidden here
 * because no People modules are active in the current 12-module shell scope.
 * Per Dashboard IA §2.2: "Families with zero visible modules for a role are
 * hidden entirely — no empty headers."
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

      {/* Module navigation */}
      <nav className={styles.nav} aria-label="Module navigation">
        {NAV.map((section) => (
          <div key={section.group} className={styles.group}>
            <span className={styles.groupLabel} aria-hidden="true">
              {section.group}
            </span>
            <ul className={styles.items} role="list">
              {section.items.map((item) => (
                <li key={item.label} role="listitem">
                  <a
                    href="#"
                    className={
                      item.active
                        ? `${styles.item} ${styles.active}`
                        : styles.item
                    }
                    aria-current={item.active ? "page" : undefined}
                  >
                    {item.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </nav>

      {/* Footer: identity */}
      <div className={styles.footer} aria-label="Workspace identity">
        <span className={styles.footerWorkspace}>ORVN Demo Realty</span>
        <span className={styles.footerRole}>Broker Owner</span>
      </div>
    </aside>
  );
}
