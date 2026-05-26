import type { RouteDefinition } from "@/lib/navigation/routes";
import type { ModuleEmptyState } from "@/lib/demo/moduleEmptyStates";
import styles from "./ModuleSkeleton.module.css";

interface ModuleSkeletonProps {
  route: RouteDefinition;
  emptyState?: ModuleEmptyState;
}

/*
 * Reusable empty-state page for every route not yet connected to real data.
 * When `emptyState` is supplied the richer per-module copy is rendered;
 * otherwise falls back to the route registry strings.
 */
export default function ModuleSkeleton({ route, emptyState }: ModuleSkeletonProps) {
  const contextCopy = emptyState?.contextCopy ?? route.description;
  const pasCanItems = emptyState?.pasCanAnswer ?? null;
  const notConnectedItems = emptyState?.notConnectedYet ?? null;

  return (
    <main className={styles.page} aria-label={`${route.label} — empty state`}>
      {/* Header */}
      <div className={styles.header}>
        <div className={styles.chips}>
          <span className={styles.familyChip}>{route.family}</span>
          <span className={styles.demoChip} aria-label="Demo / rehearsal data only">
            Demo / rehearsal
          </span>
        </div>
        <h1 className={styles.title}>{route.label}</h1>
        <p className={styles.description}>{contextCopy}</p>
      </div>

      {/* Session / permission boundary note */}
      <p className={styles.authNote} role="note">
        Access and permissions shown here are demo-only until real auth is connected.
      </p>

      <div className={styles.divider} role="presentation" />

      {/* What PAS can answer here */}
      <section className={styles.section} aria-labelledby="pas-heading">
        <h2 className={styles.sectionLabel} id="pas-heading">
          What PAS can answer here
        </h2>
        {pasCanItems ? (
          <ul className={styles.list}>
            {pasCanItems.map((item) => (
              <li key={item} className={styles.listItem}>
                {item}
              </li>
            ))}
          </ul>
        ) : (
          <p className={styles.sectionBody}>{route.pasCan}</p>
        )}
      </section>

      {/* What is not connected yet */}
      <section className={styles.section} aria-labelledby="not-connected-heading">
        <h2 className={styles.sectionLabel} id="not-connected-heading">
          Not yet connected
        </h2>
        {notConnectedItems ? (
          <ul className={styles.list}>
            {notConnectedItems.map((item) => (
              <li key={item} className={styles.listItem}>
                {item}
              </li>
            ))}
          </ul>
        ) : (
          <p className={styles.sectionBody}>{route.notConnectedYet}</p>
        )}
      </section>

      <div className={styles.divider} role="presentation" />

      {/* Invariant disclaimer */}
      <p className={styles.disclaimer} role="note">
        PAS has not changed live customer behavior.
      </p>
    </main>
  );
}
