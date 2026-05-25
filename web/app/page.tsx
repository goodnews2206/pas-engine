import type { Metadata } from "next";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "PAS",
};

export default function HomePage() {
  return (
    <main className={styles.root}>
      <div className={styles.content}>
        <p className={styles.eyebrow}>ORVN Labs</p>
        <h1 className={styles.wordmark}>PAS</h1>
        <p className={styles.tagline}>
          Making your company queryable, adaptive, and operationally
          intelligent.
        </p>
        <span className={styles.demoChip}>
          Demo / rehearsal web foundation
        </span>
      </div>
    </main>
  );
}
