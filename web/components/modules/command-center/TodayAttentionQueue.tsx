/*
 * TodayAttentionQueue — what needs attention today, ordered by severity.
 * Static RSC, demo-only. Synthesizes callbacks, proposals, risks, leads from
 * the operational model. Severity is never colour alone (rail + chip + text).
 */

import Link from "next/link";
import {
  DEMO_CALLBACKS,
  DEMO_PROPOSALS,
  DEMO_RISKS,
  DEMO_LEADS,
  type Severity,
} from "@/lib/demo/operational";
import RiskChip from "@/components/modules/continuity/RiskChip";
import { railColorForSeverity } from "@/components/modules/continuity/severity";
import styles from "./CommandCenterOverview.module.css";

interface AttentionItem {
  id: string;
  severity: Severity;
  text: string;
  source: string;
  href: string;
}

const RANK: Record<Severity, number> = {
  critical: 0,
  approval_required: 1,
  urgent: 2,
  needs_attention: 3,
  fyi: 4,
};

function buildItems(): AttentionItem[] {
  const items: AttentionItem[] = [];

  for (const cb of DEMO_CALLBACKS) {
    if (cb.status === "overdue") {
      items.push({
        id: cb.id,
        severity: cb.riskLevel,
        text: `Callback ${cb.id} is overdue — Demo Lead ${cb.leadId}.`,
        source: "Callbacks",
        href: "/callbacks",
      });
    }
  }

  for (const proposal of DEMO_PROPOSALS) {
    if (proposal.status === "candidate") {
      items.push({
        id: proposal.id,
        severity: "approval_required",
        text: `PAS proposes: ${proposal.title}.`,
        source: "Action Proposals",
        href: "/action-proposals",
      });
    }
  }

  for (const risk of DEMO_RISKS) {
    if (risk.severity === "urgent" || risk.severity === "critical") {
      items.push({
        id: risk.id,
        severity: risk.severity,
        text: risk.reason,
        source: "Pipeline Risks",
        href: "/pipeline-risks",
      });
    }
  }

  for (const lead of DEMO_LEADS) {
    if (lead.riskLevel === "urgent") {
      items.push({
        id: lead.id,
        severity: lead.riskLevel,
        text: `Lead ${lead.id} is slipping — ${lead.nextAction}`,
        source: "Leads",
        href: "/leads",
      });
    }
  }

  return items.sort((a, b) => RANK[a.severity] - RANK[b.severity]).slice(0, 5);
}

export default function TodayAttentionQueue() {
  const items = buildItems();

  return (
    <section className={styles.snapshot} aria-label="What needs attention today">
      <div className={styles.snapshotHeader}>
        <h2 className={styles.snapshotTitle}>What needs attention today</h2>
      </div>
      <ul className={styles.attnList}>
        {items.map((item) => (
          <li key={`${item.source}-${item.id}`} className={styles.attnItem}>
            <div
              className={styles.attnRail}
              style={{ background: railColorForSeverity(item.severity) }}
              aria-hidden="true"
            />
            <div className={styles.attnBody}>
              <div className={styles.attnMeta}>
                <RiskChip severity={item.severity} />
              </div>
              <p className={styles.attnText}>{item.text}</p>
              <div className={styles.attnFooter}>
                <span className={styles.attnSource}>{item.source}</span>
                <Link href={item.href} className={styles.moduleLink}>
                  Open →
                </Link>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
}
