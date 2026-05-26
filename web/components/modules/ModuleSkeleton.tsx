import type { RouteDefinition } from "@/lib/navigation/routes";
import styles from "./ModuleSkeleton.module.css";

interface ModuleSkeletonProps {
  route: RouteDefinition;
}

/*
 * Reusable skeleton page for every route not yet connected to real data.
 * Shows: module name, family, demo label, what this module will surface,
 * what PAS can eventually do here, what is intentionally not wired yet,
 * and the invariant demo disclaimer.
 */
export default function ModuleSkeleton({ route }: ModuleSkeletonProps) {
  return (
    <main className={styles.page} aria-label={`${route.label} — skeleton`}>
      {/* Header */}
      <div className={styles.header}>
        <div className={styles.chips}>
          <span className={styles.familyChip}>{route.family}</span>
          <span className={styles.demoChip} aria-label="Demo / rehearsal data only">
            Demo / rehearsal
          </span>
        </div>
        <h1 className={styles.title}>{route.label}</h1>
        <p className={styles.description}>{route.description}</p>
      </div>

      {/* Session / permission boundary note */}
      <p className={styles.authNote} role="note">
        Access and permissions shown here are demo-only until real auth is connected.
      </p>

      <div className={styles.divider} role="presentation" />

      {/* What this module will show */}
      <section className={styles.section} aria-labelledby="what-heading">
        <h2 className={styles.sectionLabel} id="what-heading">
          What this module will show
        </h2>
        <p className={styles.sectionBody}>{route.description}</p>
      </section>

      {/* What PAS can help with */}
      <section className={styles.section} aria-labelledby="pas-heading">
        <h2 className={styles.sectionLabel} id="pas-heading">
          What PAS can help with here
        </h2>
        <p className={styles.sectionBody}>{route.pasCan}</p>
      </section>

      {/* What is not connected yet */}
      <section className={styles.section} aria-labelledby="not-connected-heading">
        <h2 className={styles.sectionLabel} id="not-connected-heading">
          Not yet connected
        </h2>
        <p className={styles.sectionBody}>{route.notConnectedYet}</p>
      </section>

      <div className={styles.divider} role="presentation" />

      {/* Invariant disclaimer */}
      <p className={styles.disclaimer} role="note">
        PAS has not changed live customer behavior.
      </p>
    </main>
  );
}
