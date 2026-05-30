/*
 * OperationalRecordCard — shared record shell: left severity rail + header
 * (title + id + Simulated pill) + chips + body + optional footer.
 * Static, demo-only. Severity rail is paired with chips/text by callers.
 */

import type { ReactNode } from "react";
import styles from "./continuity.module.css";

interface Props {
  recordId: string;
  title: string;
  railColor: string;
  chips?: ReactNode;
  children: ReactNode;
  footer?: ReactNode;
}

export default function OperationalRecordCard({
  recordId,
  title,
  railColor,
  chips,
  children,
  footer,
}: Props) {
  return (
    <li className={styles.card}>
      <div
        className={styles.cardRail}
        style={{ background: railColor }}
        aria-hidden="true"
      />
      <div className={styles.cardBody}>
        <div className={styles.cardHeader}>
          <h3 className={styles.cardTitle}>{title}</h3>
          <span className={styles.cardIdRow}>
            <span className={styles.cardId}>{recordId}</span>
            <span className={styles.demoPill}>Simulated</span>
          </span>
        </div>
        {chips && <div className={styles.cardChips}>{chips}</div>}
        {children}
        {footer && <div className={styles.cardFooter}>{footer}</div>}
      </div>
    </li>
  );
}
