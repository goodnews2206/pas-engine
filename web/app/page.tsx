import type { Metadata } from "next";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Command Center",
};

/* ── Shared sub-components ── */

function DemoPill() {
  return (
    <span className={styles.demoPill} aria-label="Simulated data">
      Simulated
    </span>
  );
}

/* ── Placeholder cards ── */

function NeedsAttentionCard() {
  return (
    <article className={`${styles.card} ${styles.cardAttention}`}>
      <header className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>Needs your attention</h2>
        <DemoPill />
      </header>
      <p className={styles.cardBody}>
        Nothing needs your attention right now. Ask PAS anything, or open a
        module from the sidebar.
      </p>
      <footer className={styles.cardFooter}>
        <span className={styles.evidenceHint}>
          PAS is observing. Nothing has been done on your behalf.
        </span>
      </footer>
    </article>
  );
}

function RecommendationsCard() {
  return (
    <article className={`${styles.card} ${styles.cardApproval}`}>
      <header className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>PAS proposes</h2>
        <DemoPill />
      </header>
      <p className={styles.cardBody}>Nothing to recommend. PAS is observing.</p>
      <footer className={styles.cardFooter}>
        <span className={styles.evidenceHint}>
          All clear. PAS isn&rsquo;t proposing anything right now.
        </span>
      </footer>
    </article>
  );
}

function TodaysPipelineCard() {
  return (
    <article className={`${styles.card} ${styles.cardNeutral}`}>
      <header className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>Today&rsquo;s pipeline</h2>
        <DemoPill />
      </header>
      <p className={styles.cardBody}>
        No bookings scheduled today. PAS surfaces callback requests
        automatically when it hears them on a call.
      </p>
      <footer className={styles.cardFooter}>
        <span className={styles.evidenceHint}>
          Connect Cal.com and Twilio to see live bookings and callbacks here.
        </span>
      </footer>
    </article>
  );
}

const STATUS_ROWS = [
  { label: "Backend", value: "Railway", status: "ready" },
  { label: "Web", value: "Vercel-ready", status: "pending" },
  { label: "Data", value: "Demo / rehearsal", status: "demo" },
  { label: "PAS", value: "Observing", status: "ready" },
] as const;

type StatusKind = (typeof STATUS_ROWS)[number]["status"];

const STATUS_CLASS_MAP: Record<StatusKind, string> = {
  ready: "statusReady",
  pending: "statusPending",
  demo: "statusDemo",
};

function SystemStatusCard() {
  return (
    <article className={`${styles.card} ${styles.cardNeutral}`}>
      <header className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>System status</h2>
        <DemoPill />
      </header>
      <ul className={styles.statusList}>
        {STATUS_ROWS.map((row) => (
          <li key={row.label} className={styles.statusRow}>
            <span
              className={`${styles.statusDot} ${styles[STATUS_CLASS_MAP[row.status]]}`}
              aria-hidden="true"
            />
            <span className={styles.statusLabel}>{row.label}</span>
            <span className={styles.statusValue}>{row.value}</span>
          </li>
        ))}
      </ul>
      <footer className={styles.cardFooter}>
        <span className={styles.evidenceHint}>
          PAS has not changed live customer behavior.
        </span>
      </footer>
    </article>
  );
}

/* ── Ask PAS prompt — Command Center §4.1 item 5 ── */
function AskPASPrompt() {
  return (
    <section className={styles.askPas} aria-label="Ask PAS">
      <p className={styles.askPasHeadline}>Ask PAS anything</p>
      <p className={styles.askPasCopy}>
        Plain English. Typos are fine.{" "}
        <span className={styles.askPasExamples}>
          &ldquo;Which leads are slipping?&rdquo;&nbsp;&middot;&nbsp;&ldquo;What
          happened on the demo call?&rdquo;&nbsp;&middot;&nbsp;&ldquo;What needs
          attention?&rdquo;
        </span>
      </p>
      <span className={styles.askPasHint} aria-hidden="true">
        Use the composer below &darr;
      </span>
    </section>
  );
}

/* ── Page ── */
export default function CommandCenterPage() {
  return (
    <main className={styles.page} aria-label="Command Center">
      {/* Rehearsal mode label inside module per Dashboard IA §11 */}
      <p className={styles.rehearsalNote} role="note">
        Rehearsal mode — these cards are simulated.
      </p>

      {/* 2 × 2 cards grid */}
      <div className={styles.grid}>
        <NeedsAttentionCard />
        <RecommendationsCard />
        <TodaysPipelineCard />
        <SystemStatusCard />
      </div>

      {/* Ask PAS */}
      <AskPASPrompt />
    </main>
  );
}
