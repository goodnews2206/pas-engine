import type { Metadata } from "next";
import IntegrationsOverview from "@/components/modules/integrations/IntegrationsOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "Integrations" };

export default function IntegrationsPage() {
  return (
    <main className={styles.page} aria-label="Integrations">
      <IntegrationsOverview />
    </main>
  );
}
