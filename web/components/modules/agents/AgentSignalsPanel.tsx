/*
 * AgentSignalsPanel — "what PAS is watching" across the roster. Static RSC,
 * demo-only. Every line is derived from the demo model, never hardcoded counts.
 * Severity is never colour alone: each signal has a rail + a labelled chip.
 */

import {
  DEMO_AGENTS,
  DEMO_CALLBACKS,
  DEMO_LEADS,
} from "@/lib/demo/operational";
import styles from "./AgentsOverview.module.css";

type SignalTone = "urgent" | "attention" | "fyi";

interface Signal {
  id: string;
  tone: SignalTone;
  label: string;
  text: string;
}

const TONE: Record<SignalTone, { rail: string; chip: string; label: string }> = {
  urgent: { rail: "var(--signal-urgent)", chip: styles.chipUrgent, label: "Urgent" },
  attention: {
    rail: "var(--signal-attention)",
    chip: styles.chipAttention,
    label: "Needs attention",
  },
  fyi: { rail: "var(--signal-fyi)", chip: styles.chipFyi, label: "FYI" },
};

function plural(n: number, one: string, many: string): string {
  return `${n} ${n === 1 ? one : many}`;
}

function buildSignals(): Signal[] {
  const signals: Signal[] = [];
  const stretchedAgentIds = new Set(
    DEMO_AGENTS.filter((a) => a.coverageStatus !== "covered").map((a) => a.id),
  );

  const overdue = DEMO_CALLBACKS.filter((cb) => cb.status === "overdue");
  if (overdue.length > 0) {
    signals.push({
      id: "overdue",
      tone: "urgent",
      label: TONE.urgent.label,
      text: `${plural(overdue.length, "callback promise is", "callback promises are")} overdue with no recovery logged.`,
    });
  }

  const stretchedCallbacks = DEMO_CALLBACKS.filter(
    (cb) => cb.status !== "kept" && stretchedAgentIds.has(cb.ownerId),
  );
  if (stretchedCallbacks.length > 0) {
    signals.push({
      id: "stretched-callbacks",
      tone: "attention",
      label: TONE.attention.label,
      text: `${plural(stretchedCallbacks.length, "callback promise is", "callback promises are")} sitting with agents who are currently stretched or have a coverage gap.`,
    });
  }

  const riskyLeads = DEMO_LEADS.filter(
    (l) => l.riskLevel === "urgent" || l.riskLevel === "needs_attention",
  );
  if (riskyLeads.length > 0) {
    signals.push({
      id: "risky-leads",
      tone: "attention",
      label: TONE.attention.label,
      text: `${plural(riskyLeads.length, "owned lead is", "owned leads are")} flagged at risk and may need a faster first touch.`,
    });
  }

  const coached = DEMO_AGENTS.filter((a) => a.coachingFlags.length > 0);
  if (coached.length > 0) {
    signals.push({
      id: "coaching",
      tone: "fyi",
      label: TONE.fyi.label,
      text: `${plural(coached.length, "agent has", "agents have")} an open coaching signal worth a 1:1.`,
    });
  }

  return signals;
}

export default function AgentSignalsPanel() {
  const signals = buildSignals();

  return (
    <section className={styles.panel} aria-label="What PAS is watching">
      <h2 className={styles.panelTitle}>What PAS is watching</h2>
      {signals.length === 0 ? (
        <p className={styles.signalText}>
          Nothing needs attention across the team right now.
        </p>
      ) : (
        <ul className={styles.signals}>
          {signals.map((signal) => {
            const tone = TONE[signal.tone];
            return (
              <li key={signal.id} className={styles.signal}>
                <div
                  className={styles.signalRail}
                  style={{ background: tone.rail }}
                  aria-hidden="true"
                />
                <div className={styles.signalBody}>
                  <span className={`${styles.signalChip} ${tone.chip}`}>
                    {signal.label}
                  </span>
                  <p className={styles.signalText}>{signal.text}</p>
                </div>
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}
