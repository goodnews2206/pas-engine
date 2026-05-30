import type { Metadata } from "next";
import PasRoomOverview from "@/components/modules/pas-room/PasRoomOverview";
import styles from "./page.module.css";

export const metadata: Metadata = { title: "PAS Room" };

export default function PasRoomPage() {
  return (
    <main className={styles.page} aria-label="PAS Room">
      <PasRoomOverview />
    </main>
  );
}
