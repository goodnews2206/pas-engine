/*
 * ObjectThreadPanel — threads that live on operational objects. Static RSC,
 * demo-only. Resolves titles + evidence counts against the model so each
 * thread is welded to real work (leads, callbacks, proposals).
 */

import {
  DEMO_CALLBACKS,
  DEMO_PROPOSALS,
  DEMO_EVIDENCE,
  type ObjectThread,
  type ThreadObjectType,
  type MessageType,
} from "@/lib/demo/operational";
import ObjectThreadCard, { type ObjectThreadView } from "./ObjectThreadCard";
import styles from "./PasRoomOverview.module.css";

const TYPE_LABELS: Record<ThreadObjectType, string> = {
  lead: "Lead",
  callback: "Callback",
  proposal: "Proposal",
  recommendation: "Recommendation",
  booking: "Booking",
  call: "Call",
  room: "Room",
};

const STATUS_FROM_TYPE: Partial<Record<MessageType, string>> = {
  decision_record: "Decided",
  approval: "Approved",
  assignment: "Assigned",
};

const EVIDENCE_IDS = new Set(DEMO_EVIDENCE.map((e) => e.id));

function resolveTitle(thread: ObjectThread): string {
  const label = TYPE_LABELS[thread.objectType];
  if (thread.objectType === "callback") {
    const cb = DEMO_CALLBACKS.find((c) => c.id === thread.objectId);
    if (cb) return `${label} ${thread.objectId} · Demo Lead ${cb.leadId}`;
  }
  if (thread.objectType === "proposal") {
    const proposal = DEMO_PROPOSALS.find((p) => p.id === thread.objectId);
    if (proposal) return `${label} ${thread.objectId} · ${proposal.title}`;
  }
  if (thread.objectType === "lead") return `Demo Lead ${thread.objectId}`;
  return `${label} ${thread.objectId}`;
}

function toView(thread: ObjectThread, authorNames: Record<string, string>): ObjectThreadView {
  const last = thread.messages[thread.messages.length - 1];
  const participants = new Set(
    thread.messages
      .filter((m) => m.authorType === "human")
      .map((m) => authorNames[m.authorId] ?? m.authorId),
  ).size;
  const evidenceCount = new Set(
    thread.messages.flatMap((m) => m.evidenceIds).filter((id) => EVIDENCE_IDS.has(id)),
  ).size;

  return {
    id: thread.id,
    typeLabel: TYPE_LABELS[thread.objectType],
    title: resolveTitle(thread),
    lastMessage: last ? last.body : "No messages yet.",
    participants,
    statusLabel: last ? STATUS_FROM_TYPE[last.type] ?? "Active" : "Active",
    evidenceCount,
  };
}

interface Props {
  threads: ObjectThread[];
  authorNames: Record<string, string>;
}

export default function ObjectThreadPanel({ threads, authorNames }: Props) {
  const views = threads.map((t) => toView(t, authorNames));

  return (
    <aside className={styles.region} aria-label="Object threads">
      <div className={styles.regionHeader}>
        <h2 className={styles.regionTitle}>Object threads</h2>
        <p className={styles.regionDesc}>
          Discussion stays welded to the work it concerns.
        </p>
      </div>

      {views.length === 0 ? (
        <p className={styles.threadLast}>No object threads yet.</p>
      ) : (
        <ul className={styles.threadList}>
          {views.map((view) => (
            <ObjectThreadCard key={view.id} thread={view} />
          ))}
        </ul>
      )}
    </aside>
  );
}
