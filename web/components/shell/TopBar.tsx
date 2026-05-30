/*
 * TopBar — 56 px shell header. Design System §11.1.
 * RSC. Avatar and role derived from DEMO_SESSION (build-time constant).
 * NotificationCenter and ConnectionStatus are client islands embedded here.
 * Replace with real session context in the auth step.
 */

import { DEMO_SESSION } from "@/lib/session/demoSession";
import NotificationCenter from "@/components/notifications/NotificationCenter";
import ConnectionStatus from "@/components/shell/ConnectionStatus";
import styles from "./TopBar.module.css";

const { user } = DEMO_SESSION;

export default function TopBar() {
  return (
    <header className={styles.topbar} role="banner">
      {/* Left: page title + API boundary status */}
      <div className={styles.left}>
        <h1 className={styles.pageTitle}>Command Center</h1>
        <ConnectionStatus />
      </div>

      {/* Center: global command / search entry point */}
      <div className={styles.center}>
        <div className={styles.searchWrap}>
          <span className={styles.searchHint} aria-hidden="true">⌘K</span>
          <input
            className={styles.searchInput}
            type="text"
            placeholder="Ask PAS anything operational…"
            aria-label="Search or ask PAS — press ⌘K"
            autoComplete="off"
          />
        </div>
        <span className={styles.envChip}>Simulation only</span>
      </div>

      {/* Right: notifications bell + profile */}
      <div className={styles.right}>
        <NotificationCenter />
        <button
          type="button"
          className={styles.profileButton}
          aria-label={`Profile: ${user.name} — ${user.role}`}
        >
          <span className={styles.avatar} aria-hidden="true">
            {user.initials}
          </span>
        </button>
      </div>
    </header>
  );
}
