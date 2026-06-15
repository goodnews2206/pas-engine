/*
 * AccountShellPanel — the account / profile shell (PAS301A). Static, demo-only.
 *
 * This is identity-level profile SCAFFOLDING, not real authentication. It reads
 * the build-time DEMO_SESSION; there is no sign-in, no persistence, no backend.
 *
 * It makes the PAS301 ownership doctrine visible:
 *   • A person owns their identity and professional self (portable).
 *   • A workspace governs the business records created within it.
 * Person identity is shown separately from the current workspace/role context,
 * and workspace switching is intentionally NOT implied yet (that is PAS301B).
 *
 * Sign-out stays inert until real auth lands in a later checkpoint.
 */

import { DEMO_SESSION } from "@/lib/session/demoSession";
import styles from "./SettingsOverview.module.css";

export default function AccountShellPanel() {
  const { user, workspace, sessionLabel, profile, assistant, auth } =
    DEMO_SESSION;

  // Person-owned identity (PAS301 §4 class A — travels with the person).
  const identityFields = [
    { label: "Name", value: user.name },
    { label: "Email", value: user.email },
    { label: "Timezone", value: profile.timezone },
    { label: "Working hours", value: profile.workingHours },
  ];

  // Personal PAS configuration (PAS301 §15 — person-owned, portable).
  const assistantFields = [
    { label: "Assistant name", value: assistant.assistantName },
    { label: "Tone", value: assistant.tone },
  ];

  // Current workspace context (PAS301 §4 classes C/D — governed by the tenant).
  const workspaceFields = [
    { label: "Workspace", value: workspace.name },
    { label: "Your role here", value: user.role },
    { label: "Session mode", value: sessionLabel },
  ];

  return (
    <section className={styles.panel} aria-label="Account and profile">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>Account &amp; profile</h2>
        <p className={styles.panelDesc}>
          Who you are in PAS, and where you are working right now. Your identity
          is yours and travels with you; the workspace governs its own business
          records. Real sign-in arrives with authentication.
        </p>
      </div>

      {/* ── Person identity (you own this) ── */}
      <div className={styles.accountSubsection}>
        <p className={styles.capLabel}>You · person-owned &amp; portable</p>
        <div className={styles.accountGrid}>
          {identityFields.map((field) => (
            <div key={field.label} className={styles.accountField}>
              <span className={styles.accountLabel}>{field.label}</span>
              <span className={styles.accountValue}>{field.value}</span>
            </div>
          ))}
        </div>
        <p className={styles.ownershipNote}>
          This is yours. Your identity, profile, and personal PAS setup follow
          you across every workspace and stay with you if you leave one.
        </p>
      </div>

      {/* ── Personal PAS preferences (person-owned) ── */}
      <div className={styles.accountSubsection}>
        <p className={styles.capLabel}>Your PAS · personal preferences</p>
        <div className={styles.accountGrid}>
          {assistantFields.map((field) => (
            <div key={field.label} className={styles.accountField}>
              <span className={styles.accountLabel}>{field.label}</span>
              <span className={styles.accountValue}>{field.value}</span>
            </div>
          ))}
        </div>
        <p className={styles.lockedNote}>
          Editing connects when the backend is wired — display-only for now.
        </p>
      </div>

      {/* ── Current workspace context (governed by the tenant) ── */}
      <div className={styles.accountSubsection}>
        <p className={styles.capLabel}>
          Current workspace · governed records
        </p>
        <div className={styles.accountGrid}>
          {workspaceFields.map((field) => (
            <div key={field.label} className={styles.accountField}>
              <span className={styles.accountLabel}>{field.label}</span>
              <span className={styles.accountValue}>{field.value}</span>
            </div>
          ))}
        </div>
        <p className={styles.ownershipNote}>
          Client and transaction records here belong to the workspace, not to
          you. Switching between workspaces arrives in a later checkpoint.
        </p>
      </div>

      {/* ── Access & security (real auth not connected) ── */}
      <div className={styles.accountSubsection}>
        <p className={styles.capLabel}>Access &amp; security</p>
        <div className={styles.authStatusCard}>
          <p className={styles.authStatusCurrent}>{auth.current}</p>
          <p className={styles.capLabel}>Coming later</p>
          <ul className={styles.list}>
            {auth.plannedMethods.map((method) => (
              <li key={method} className={styles.listItem}>
                {method}
              </li>
            ))}
          </ul>
          <p className={styles.lockedNote}>{auth.note}</p>
        </div>
      </div>

      <div className={styles.signOutRow}>
        <button type="button" className={styles.signOutBtn} disabled>
          Sign out
        </button>
        <p className={styles.signOutNote}>
          Sign out connects when real authentication is enabled.
        </p>
      </div>
    </section>
  );
}
