"use client";

/*
 * NotificationCenter — bell button, unread badge, and drawer controller.
 * Manages: open/close state, per-notification read state, mark-all-read.
 * No network. No persistence. Pure useState.
 * Authority: docs/pas_notification_architecture.md §1 §2 §3
 */

import { useState } from "react";
import { DEMO_NOTIFICATIONS } from "@/lib/notifications/demoNotifications";
import type { DemoNotification } from "@/lib/notifications/demoNotifications";
import NotificationDrawer from "./NotificationDrawer";
import styles from "./NotificationCenter.module.css";

export default function NotificationCenter() {
  const [isOpen, setIsOpen] = useState(false);
  const [notifications, setNotifications] = useState<DemoNotification[]>(
    () => DEMO_NOTIFICATIONS
  );

  // Badge: unread count at needs-attention and above; FYI does not badge per §3.1.
  const badgeCount = notifications.filter(
    (n) => !n.isRead && n.severity !== "fyi"
  ).length;

  function markRead(id: string) {
    setNotifications((prev) =>
      prev.map((n) => (n.id === id ? { ...n, isRead: true } : n))
    );
  }

  function markAllRead() {
    setNotifications((prev) => prev.map((n) => ({ ...n, isRead: true })));
  }

  return (
    <>
      <button
        type="button"
        className={styles.bellBtn}
        onClick={() => setIsOpen(true)}
        aria-label={
          badgeCount > 0
            ? `Notifications — ${badgeCount} unread`
            : "Notifications"
        }
        aria-expanded={isOpen}
        aria-haspopup="dialog"
      >
        <BellIcon />
        {badgeCount > 0 && (
          <span className={styles.badge} aria-hidden="true">
            {badgeCount > 9 ? "9+" : badgeCount}
          </span>
        )}
      </button>

      <NotificationDrawer
        isOpen={isOpen}
        notifications={notifications}
        onClose={() => setIsOpen(false)}
        onMarkRead={markRead}
        onMarkAllRead={markAllRead}
      />
    </>
  );
}

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
