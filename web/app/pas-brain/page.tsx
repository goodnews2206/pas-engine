import type { Metadata } from "next";
import PasBrainOverview from "@/components/modules/pas-brain/PasBrainOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "PAS Brain" };

export default function PasBrainPage() {
  return (
    <main className={styles.page} aria-label="PAS Brain">
      <PasBrainOverview />
    </main>
  );
}
