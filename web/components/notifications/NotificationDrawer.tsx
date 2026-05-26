"use client";

/*
 * NotificationDrawer — right-side slide-over (mobile: bottom sheet).
 * Groups notifications by severity: Critical first, FYI last.
 * ESC closes. Overlay click closes. Focus-trapped while open.
 * No network. No persistence.
 * Authority: docs/pas_notification_architecture.md §3 §8
 */

import { useEffect, useRef } from "react";
import type { DemoNotification, SeverityLevel } from "@/lib/notifications/demoNotifications";
import NotificationCard from "./NotificationCard";
import styles from "./NotificationDrawer.module.css";

const SEVERITY_ORDER: SeverityLevel[] = [
  "critical",
  "approval-required",
  "urgent",
  "needs-attention",
  "fyi",
];

const GROUP_LABELS: Record<SeverityLevel, string> = {
  "critical": "Critical",
  "approval-required": "Approval required",
  "urgent": "Urgent",
  "needs-attention": "Needs attention",
  "fyi": "FYI",
};

const GROUP_LABEL_CLASSES: Record<SeverityLevel, string> = {
  "critical": styles.groupLabelCritical,
  "approval-required": styles.groupLabelApprovalRequired,
  "urgent": styles.groupLabelUrgent,
  "needs-attention": styles.groupLabelNeedsAttention,
  "fyi": styles.groupLabelFyi,
};

interface Props {
  isOpen: boolean;
  notifications: DemoNotification[];
  onClose: () => void;
  onMarkRead: (id: string) => void;
  onMarkAllRead: () => void;
}

export default function NotificationDrawer({
  isOpen,
  notifications,
  onClose,
  onMarkRead,
  onMarkAllRead,
}: Props) {
  const drawerRef = useRef<HTMLDivElement>(null);
  const hasUnread = notifications.some((n) => !n.isRead);

  // Focus trap + ESC handler
  useEffect(() => {
    if (!isOpen) return;
    const el = drawerRef.current;
    if (!el) return;

    const focusable = el.querySelectorAll<HTMLElement>(
      'button:not([disabled]), [href], input:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    first?.focus();

    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") { onClose(); return; }
      if (e.key !== "Tab" || !focusable.length) return;
      if (e.shiftKey) {
        if (document.activeElement === first) { e.preventDefault(); last?.focus(); }
      } else {
        if (document.activeElement === last) { e.preventDefault(); first?.focus(); }
      }
    }

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  // Body scroll lock while open
  useEffect(() => {
    document.body.style.overflow = isOpen ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [isOpen]);

  const groups = SEVERITY_ORDER
    .map((severity) => ({
      severity,
      label: GROUP_LABELS[severity],
      labelClass: GROUP_LABEL_CLASSES[severity],
      items: notifications.filter((n) => n.severity === severity),
    }))
    .filter((g) => g.items.length > 0);

  return (
    <>
      <div
        className={`${styles.overlay} ${isOpen ? styles.overlayVisible : ""}`}
        onClick={onClose}
        aria-hidden="true"
      />
      <div
        ref={drawerRef}
        className={`${styles.drawer} ${isOpen ? styles.drawerOpen : ""}`}
        role="dialog"
        aria-label="Notifications"
        aria-modal="true"
        aria-hidden={!isOpen}
        tabIndex={-1}
      >
        <header className={styles.drawerHeader}>
          <h2 className={styles.drawerTitle}>Notifications</h2>
          <div className={styles.drawerActions}>
            {hasUnread && (
              <button
                type="button"
                className={styles.markAllBtn}
                onClick={onMarkAllRead}
              >
                Mark all read
              </button>
            )}
            <button
              type="button"
              className={styles.closeBtn}
              onClick={onClose}
              aria-label="Close notifications"
            >
              <CloseIcon />
            </button>
          </div>
        </header>

        <div className={styles.drawerBody}>
          {groups.length === 0 ? (
            <div className={styles.emptyState} role="status">
              <p className={styles.emptyTitle}>No notifications</p>
              <p className={styles.emptyBody}>
                PAS is observing. You will be notified when something requires attention.
              </p>
            </div>
          ) : (
            groups.map(({ severity, label, labelClass, items }) => (
              <section key={severity} className={styles.group}>
                <h3 className={`${styles.groupLabel} ${labelClass}`}>
                  {label}
                  <span className={styles.groupCount}>{items.length}</span>
                </h3>
                <ul className={styles.groupList}>
                  {items.map((n) => (
                    <li key={n.id} className={styles.groupItem}>
                      <NotificationCard notification={n} onRead={onMarkRead} />
                    </li>
                  ))}
                </ul>
              </section>
            ))
          )}
        </div>

        <footer className={styles.drawerFooter}>
          <p className={styles.footerNote}>
            PAS has not changed live customer behavior.
          </p>
        </footer>
      </div>
    </>
  );
}

function CloseIcon() {
  return (
    <svg
      width="14"
      height="14"
      viewBox="0 0 14 14"
      fill="none"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M1 1l12 12M13 1L1 13"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
    </svg>
  );
}
