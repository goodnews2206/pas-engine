import type { Metadata } from "next";
import LeadsOverview from "@/components/modules/leads/LeadsOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "Leads" };

export default function LeadsPage() {
  return (
    <main className={styles.page} aria-label="Leads">
      <LeadsOverview />
    </main>
  );
}
