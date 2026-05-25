import styles from "./TopBar.module.css";

function BellIcon() {
  return (
    <svg
      width="18"
      height="18"
      viewBox="0 0 18 18"
      fill="none"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M9 1.5A5.25 5.25 0 0 0 3.75 6.75v2.25L2.25 11.25h13.5l-1.5-2.25V6.75A5.25 5.25 0 0 0 9 1.5Z"
        stroke="currentColor"
        strokeWidth="1.4"
        strokeLinejoin="round"
      />
      <path
        d="M7.125 13.5a1.875 1.875 0 0 0 3.75 0"
        stroke="currentColor"
        strokeWidth="1.4"
        strokeLinecap="round"
      />
    </svg>
  );
}

export default function TopBar() {
  return (
    <header className={styles.topbar} role="banner">
      {/* Left: page title + environment status */}
      <div className={styles.left}>
        <h1 className={styles.pageTitle}>Command Center</h1>
        <span
          className={styles.statusChip}
          aria-label="Environment: Demo / rehearsal"
        >
          Demo / rehearsal
        </span>
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
        <button
          type="button"
          className={styles.iconButton}
          aria-label="Notifications"
        >
          <BellIcon />
        </button>
        <button
          type="button"
          className={styles.profileButton}
          aria-label="Profile: Broker Owner"
        >
          <span className={styles.avatar} aria-hidden="true">
            BO
          </span>
        </button>
      </div>
    </header>
  );
}
