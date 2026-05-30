"use client";

/*
 * IntegrationsOverview — operational demo marketplace for /integrations.
 * Client component: holds the selected-integration state for the detail
 * drawer. No network, no OAuth, no mutations. Consumes DEMO_INTEGRATIONS.
 */

import { useState } from "react";
import {
  DEMO_INTEGRATIONS,
  type Integration,
} from "@/lib/demo/operational";
import { CATEGORY_META, CATEGORY_ORDER } from "./meta";
import IntegrationCard from "./IntegrationCard";
import IntegrationHealthPanel from "./IntegrationHealthPanel";
import IntegrationDetailDrawer from "./IntegrationDetailDrawer";
import styles from "./IntegrationsOverview.module.css";

export default function IntegrationsOverview() {
  const [selected, setSelected] = useState<Integration | null>(null);

  const groups = CATEGORY_ORDER.map((category) => ({
    category,
    label: CATEGORY_META[category].label,
    items: DEMO_INTEGRATIONS.filter((i) => i.category === category),
  })).filter((g) => g.items.length > 0);

  return (
    <>
      <header className={styles.header}>
        <div className={styles.headerTop}>
          <h1 className={styles.title}>Integrations</h1>
          <span className={styles.demoPill}>Simulated</span>
        </div>
        <p className={styles.lead}>
          The systems PAS can connect to. PAS always starts by reading — it can
          prepare a change, but nothing is written without your approval.
        </p>
        <p className={styles.rehearsalNote}>
          Rehearsal mode — these connections are simulated.
        </p>
      </header>

      <IntegrationHealthPanel />

      {groups.map((group) => (
        <section
          key={group.category}
          className={styles.categorySection}
          aria-label={group.label}
        >
          <h2 className={styles.categoryTitle}>{group.label}</h2>
          <div className={styles.grid}>
            {group.items.map((integration) => (
              <IntegrationCard
                key={integration.id}
                integration={integration}
                onOpen={setSelected}
              />
            ))}
          </div>
        </section>
      ))}

      <p className={styles.disclaimer}>
        This is demo/rehearsal data. No OAuth flow runs here and PAS has not
        changed live customer behavior.
      </p>

      <IntegrationDetailDrawer
        integration={selected}
        onClose={() => setSelected(null)}
      />
    </>
  );
}
