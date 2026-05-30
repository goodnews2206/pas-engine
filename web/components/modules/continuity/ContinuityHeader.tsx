/*
 * ContinuityHeader — shared module header: title + demo pill + intro +
 * rehearsal note. Static, demo-only.
 */

import styles from "./continuity.module.css";

interface Props {
  title: string;
  intro: string;
  rehearsalNote?: string;
}

export default function ContinuityHeader({ title, intro, rehearsalNote }: Props) {
  return (
    <header className={styles.header}>
      <div className={styles.headerTop}>
        <h1 className={styles.title}>{title}</h1>
        <span className={styles.demoPill}>Simulated</span>
      </div>
      <p className={styles.intro}>{intro}</p>
      <p className={styles.rehearsalNote}>
        {rehearsalNote ?? "Rehearsal mode — these records are simulated."}
      </p>
    </header>
  );
}
