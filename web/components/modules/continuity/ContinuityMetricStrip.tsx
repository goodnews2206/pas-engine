/*
 * ContinuityMetricStrip — a calm row of operational counts. Static, demo-only.
 * Tones are derived counts from the model, never invented live metrics.
 */

import styles from "./continuity.module.css";

export type MetricTone = "neutral" | "fyi" | "attention" | "urgent";

export interface Metric {
  label: string;
  value: string | number;
  tone?: MetricTone;
}

const TONE_CLASS: Record<MetricTone, string> = {
  neutral: "",
  fyi: styles.metricValueFyi,
  attention: styles.metricValueAttention,
  urgent: styles.metricValueUrgent,
};

interface Props {
  metrics: Metric[];
  ariaLabel: string;
}

export default function ContinuityMetricStrip({ metrics, ariaLabel }: Props) {
  return (
    <section className={styles.metricStrip} aria-label={ariaLabel}>
      {metrics.map((metric) => (
        <div key={metric.label} className={styles.metric}>
          <span
            className={`${styles.metricValue} ${TONE_CLASS[metric.tone ?? "neutral"]}`}
          >
            {metric.value}
          </span>
          <span className={styles.metricLabel}>{metric.label}</span>
        </div>
      ))}
    </section>
  );
}
