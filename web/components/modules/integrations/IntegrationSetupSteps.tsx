/*
 * IntegrationSetupSteps — ordered, read-first setup outline for the drawer.
 * Display-only. Steps come from the demo model; no flow is started here.
 */

import styles from "./IntegrationDetailDrawer.module.css";

interface Props {
  steps: string[];
}

export default function IntegrationSetupSteps({ steps }: Props) {
  if (steps.length === 0) {
    return <p className={styles.noteText}>No setup steps for this connector.</p>;
  }

  return (
    <ol className={styles.steps}>
      {steps.map((step, index) => (
        <li key={index} className={styles.step}>
          <span className={styles.stepNumber} aria-hidden="true">
            {index + 1}
          </span>
          <span className={styles.stepText}>{step}</span>
        </li>
      ))}
    </ol>
  );
}
