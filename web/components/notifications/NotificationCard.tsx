"use client";

/*
 * NotificationCard — single notification entry.
 * Severity left rail (3px inline color), severity chip + icon, read/unread state,
 * demo label, local demo reply (quick instruction capture — no network).
 * No network. No persistence.
 * Authority: docs/pas_notification_architecture.md §2 §7
 */

import { useState } from "react";
import type { DemoNotification, SeverityLevel } from "@/lib/notifications/demoNotifications";
import { NOTIFICATION_REPLY_CONFIRMATION } from "@/lib/demo/operational";
import styles from "./NotificationCard.module.css";

const SEVERITY_LABELS: Record<SeverityLevel, string> = {
  "fyi": "FYI",
  "needs-attention": "Needs attention",
  "urgent": "Urgent",
  "approval-required": "Approval required",
  "critical": "Critical",
};

const RAIL_COLORS: Record<SeverityLevel, string> = {
  "fyi": "var(--signal-fyi)",
  "needs-attention": "var(--signal-attention)",
  "urgent": "var(--signal-urgent)",
  "approval-required": "var(--signal-approval)",
  "critical": "var(--signal-critical)",
};

const CHIP_CLASSES: Record<SeverityLevel, string> = {
  "fyi": styles.chipFyi,
  "needs-attention": styles.chipNeedsAttention,
  "urgent": styles.chipUrgent,
  "approval-required": styles.chipApprovalRequired,
  "critical": styles.chipCritical,
};

interface Props {
  notification: DemoNotification;
  onRead: (id: string) => void;
}

export default function NotificationCard({ notification, onRead }: Props) {
  const {
    id,
    severity,
    title,
    body,
    module: moduleName,
    timestamp,
    relativeTime,
    isRead,
    isDemoLabelled,
    actionLabel,
    actionHref,
  } = notification;

  const [replyText, setReplyText] = useState("");
  const [submittedReply, setSubmittedReply] = useState<string | null>(null);

  function handleReply() {
    const trimmed = replyText.trim();
    if (!trimmed) return;
    setSubmittedReply(trimmed);
    setReplyText("");
  }

  return (
    <article className={`${styles.card} ${isRead ? styles.read : styles.unread}`}>
      <div
        className={styles.rail}
        style={{ background: RAIL_COLORS[severity] }}
        aria-hidden="true"
      />
      <div className={styles.body}>
        <header className={styles.cardHeader}>
          <div className={styles.chips}>
            <span className={`${styles.chip} ${CHIP_CLASSES[severity]}`}>
              <SeverityIcon severity={severity} />
              {SEVERITY_LABELS[severity]}
            </span>
            {isDemoLabelled && (
              <span className={styles.demoChip}>Simulated</span>
            )}
          </div>
          <div className={styles.headerRight}>
            <time
              className={styles.time}
              dateTime={timestamp}
              title={timestamp}
            >
              {relativeTime}
            </time>
            {!isRead && (
              <button
                type="button"
                className={styles.markReadBtn}
                onClick={() => onRead(id)}
                aria-label="Mark as read"
              >
                <span className={styles.unreadDot} aria-hidden="true" />
              </button>
            )}
          </div>
        </header>

        <p className={styles.title}>{title}</p>
        <p className={styles.bodyText}>{body}</p>

        <footer className={styles.cardFooter}>
          <span className={styles.moduleTag}>{moduleName}</span>
          {actionLabel && actionHref && (
            <a href={actionHref} className={styles.actionLink}>
              {actionLabel}
            </a>
          )}
        </footer>

        {/* Local demo reply — quick instruction capture, no network */}
        <div className={styles.replyForm}>
          <label htmlFor={`reply-${id}`} className={styles.replyLabel}>
            Reply with an instruction for PAS
          </label>
          <div className={styles.replyRow}>
            <textarea
              id={`reply-${id}`}
              className={styles.replyInput}
              placeholder="Reply with an instruction for PAS…"
              rows={1}
              value={replyText}
              onChange={(e) => setReplyText(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  handleReply();
                }
              }}
              aria-label="Reply with an instruction for PAS"
            />
            <button
              type="button"
              className={styles.replyBtn}
              onClick={handleReply}
              disabled={replyText.trim().length === 0}
            >
              Send demo reply
            </button>
          </div>
          {submittedReply && (
            <div className={styles.replyResult}>
              <p className={styles.submittedReply}>
                <span className={styles.submittedLabel}>You (demo):</span>{" "}
                {submittedReply}
              </p>
              <p className={styles.replyConfirm} role="status">
                {NOTIFICATION_REPLY_CONFIRMATION}
              </p>
            </div>
          )}
        </div>
      </div>
    </article>
  );
}

function SeverityIcon({ severity }: { severity: SeverityLevel }) {
  switch (severity) {
    case "fyi":
      return (
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
          <circle cx="5.5" cy="5.5" r="4" stroke="currentColor" strokeWidth="1.3" />
          <path d="M5.5 5v2.5M5.5 3.5v.01" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "needs-attention":
      return (
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
          <path d="M5.5 1.5L9.5 8.5H1.5L5.5 1.5Z" stroke="currentColor" strokeWidth="1.3" strokeLinejoin="round" />
          <path d="M5.5 4.5v1.5M5.5 7.5v.01" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "urgent":
      return (
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
          <circle cx="5.5" cy="5.5" r="4" stroke="currentColor" strokeWidth="1.3" />
          <path d="M5.5 3v2.5M5.5 7.5v.01" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "approval-required":
      return (
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
          <rect x="1.5" y="1.5" width="8" height="8" rx="1.5" stroke="currentColor" strokeWidth="1.3" />
          <path d="M3.5 5.5L5 7L7.5 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "critical":
      return (
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
          <circle cx="5.5" cy="5.5" r="4" stroke="currentColor" strokeWidth="1.3" />
          <path d="M3.5 3.5l4 4M7.5 3.5l-4 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
  }
}
