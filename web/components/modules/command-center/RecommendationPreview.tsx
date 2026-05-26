/*
 * RecommendationPreview — pending proposals the user can approve or decline.
 * Dashboard IA §4.1 item 2. Static RSC.
 */

import { RECOMMENDATION_CARDS } from "@/lib/demo/commandCenter";
import styles from "./RecommendationPreview.module.css";

export default function RecommendationPreview() {
  return (
    <section className={styles.section} aria-label="PAS proposes">
      <header className={styles.sectionHeader}>
        <h2 className={styles.sectionTitle}>PAS proposes</h2>
        <span
          className={styles.badge}
          aria-label={`${RECOMMENDATION_CARDS.length} proposals`}
        >
          {RECOMMENDATION_CARDS.length}
        </span>
      </header>
      <div className={styles.cards}>
        {RECOMMENDATION_CARDS.map((card) => (
          <article
            key={card.id}
            className={styles.card}
            aria-label={card.title}
          >
            <div className={styles.cardRail} aria-hidden="true" />
            <div className={styles.cardBody}>
              <header className={styles.cardHeader}>
                <h3 className={styles.cardTitle}>{card.title}</h3>
                <span className={styles.approvalChip}>Approval required</span>
              </header>
              <p className={styles.scope}>{card.scope}</p>
              <p className={styles.evidence}>{card.evidenceSummary}</p>
              <footer className={styles.cardFooter}>
                <span className={styles.expires}>{card.expiresLabel}</span>
                <div className={styles.actions}>
                  <a href={card.actionHref} className={styles.actionBtn}>
                    {card.actionLabel}
                  </a>
                  <span className={styles.whyLink}>Why this?</span>
                </div>
              </footer>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
