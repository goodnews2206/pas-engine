"use client";

/*
 * IntegrationDetailDrawer — right-side slide-over (demo mode).
 * ESC closes. Overlay click closes. Focus-trapped while open. Body scroll lock.
 * No OAuth, no redirects, no network. Buttons are inert/demo-only.
 */

import { useEffect, useRef } from "react";
import type { Integration } from "@/lib/demo/operational";
import {
  STATUS_META,
  TONE_COLORS,
  CATEGORY_META,
  CONNECTION_NOTES,
  formatSync,
} from "./meta";
import IntegrationSetupSteps from "./IntegrationSetupSteps";
import styles from "./IntegrationDetailDrawer.module.css";

interface Props {
  integration: Integration | null;
  onClose: () => void;
}

export default function IntegrationDetailDrawer({ integration, onClose }: Props) {
  const drawerRef = useRef<HTMLDivElement>(null);
  const isOpen = integration !== null;

  // Focus trap + ESC
  useEffect(() => {
    if (!isOpen) return;
    const el = drawerRef.current;
    if (!el) return;

    const focusable = el.querySelectorAll<HTMLElement>(
      'button:not([disabled]), [href], input:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])',
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    first?.focus();

    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === "Escape") {
        onClose();
        return;
      }
      if (e.key !== "Tab" || !focusable.length) return;
      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last?.focus();
        }
      } else if (document.activeElement === last) {
        e.preventDefault();
        first?.focus();
      }
    }

    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, onClose]);

  // Body scroll lock
  useEffect(() => {
    document.body.style.overflow = isOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [isOpen]);

  const status = integration ? STATUS_META[integration.status] : null;
  const category = integration ? CATEGORY_META[integration.category] : null;

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
        aria-label={
          integration ? `${integration.name} integration details` : "Integration details"
        }
        aria-modal="true"
        aria-hidden={!isOpen}
        tabIndex={-1}
      >
        {integration && status && category && (
          <>
            <header className={styles.header}>
              <div className={styles.headerText}>
                <h2 className={styles.title}>{integration.name}</h2>
                <span className={styles.categoryBadge}>{category.label}</span>
              </div>
              <button
                type="button"
                className={styles.closeBtn}
                onClick={onClose}
                aria-label="Close integration details"
              >
                <CloseIcon />
              </button>
            </header>

            <div className={styles.body}>
              <div className={styles.statusRow}>
                <span className={styles.statusChip}>
                  <span
                    className={styles.dot}
                    style={{ background: TONE_COLORS[status.tone] }}
                    aria-hidden="true"
                  />
                  {status.label}
                </span>
                <span className={styles.demoPill}>Simulated</span>
              </div>

              <p className={styles.note}>{CONNECTION_NOTES[integration.status]}</p>

              <Section title="Health">
                <p className={styles.value}>{integration.health}</p>
                <p className={styles.subtle}>
                  Last sync: {formatSync(integration.lastSync)}
                </p>
              </Section>

              <Section title="What PAS can read">
                {integration.readScope.length > 0 ? (
                  <ul className={styles.scopeList}>
                    {integration.readScope.map((scope) => (
                      <li key={scope} className={styles.scopeItem}>
                        {scope}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className={styles.subtle}>No read scopes.</p>
                )}
              </Section>

              <Section title="What PAS can prepare — approval required">
                {integration.writeScope.length > 0 ? (
                  <ul className={styles.scopeList}>
                    {integration.writeScope.map((scope) => (
                      <li key={scope} className={styles.scopeItemWrite}>
                        {scope}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p className={styles.subtle}>
                    No write access. PAS can only read here.
                  </p>
                )}
              </Section>

              <Section title="Setup steps">
                <IntegrationSetupSteps steps={integration.setupSteps} />
              </Section>

              <Section title="Permissions requested">
                <ul className={styles.permList}>
                  {integration.readScope.map((scope) => (
                    <li key={`r-${scope}`} className={styles.permItem}>
                      <span className={styles.permKind}>read</span> {scope}
                    </li>
                  ))}
                  {integration.writeScope.map((scope) => (
                    <li key={`w-${scope}`} className={styles.permItem}>
                      <span className={styles.permKindWrite}>write</span> {scope}
                    </li>
                  ))}
                </ul>
              </Section>

              <p className={styles.warning} role="note">
                This is a demo integration view. No OAuth flow has started and
                PAS has not changed live customer behavior.
              </p>

              <div className={styles.actions}>
                <button type="button" className={styles.primaryBtn} disabled>
                  Start setup
                </button>
                <button type="button" className={styles.secondaryBtn} disabled>
                  View health
                </button>
              </div>
              <p className={styles.actionsNote}>Demo only — buttons are inert.</p>
            </div>
          </>
        )}
      </div>
    </>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className={styles.section}>
      <h3 className={styles.sectionTitle}>{title}</h3>
      {children}
    </section>
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
