/*
 * PasBehaviorPanel — how PAS conducts itself. Static, demo-only.
 * Controls are inert (display current value only, no persistence).
 */

import styles from "./SettingsOverview.module.css";

const CONTROLS: { label: string; desc: string; value: string }[] = [
  {
    label: "AI disclosure",
    desc: "PAS always identifies itself as an assistant in customer-facing copy.",
    value: "Always disclose",
  },
  {
    label: "Tone style",
    desc: "How PAS phrases recommendations and summaries.",
    value: "Calm · plain",
  },
  {
    label: "Callback capture strictness",
    desc: "How readily PAS turns a spoken promise into a tracked callback.",
    value: "Strict",
  },
  {
    label: "Evidence requirement",
    desc: "PAS attaches a receipt to every recommendation and proposal.",
    value: "Required",
  },
  {
    label: "Human-review threshold",
    desc: "When PAS routes an action to a person before anything happens.",
    value: "All actions",
  },
];

export default function PasBehaviorPanel() {
  return (
    <section className={styles.panel} aria-label="PAS behavior">
      <div className={styles.panelHeader}>
        <h2 className={styles.panelTitle}>PAS behavior</h2>
        <p className={styles.panelDesc}>
          How PAS speaks and when it asks for a human. Tuning connects when the
          backend is wired.
        </p>
      </div>

      <div>
        {CONTROLS.map((control) => (
          <div key={control.label} className={styles.controlRow}>
            <div className={styles.controlMain}>
              <span className={styles.controlLabel}>{control.label}</span>
              <span className={styles.controlDesc}>{control.desc}</span>
            </div>
            <span className={styles.controlValue}>{control.value}</span>
          </div>
        ))}
      </div>

      <p className={styles.lockedNote}>
        Controls are locked in demo mode — values are display-only, nothing is
        saved.
      </p>
    </section>
  );
}
