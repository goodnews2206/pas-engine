import type { Metadata } from "next";
import ModuleSkeleton from "@/components/modules/ModuleSkeleton";
import { ROUTES_BY_ID } from "@/lib/navigation/routes";

export const metadata: Metadata = { title: "Evidence Digest" };

export default function EvidenceDigestPage() {
  return <ModuleSkeleton route={ROUTES_BY_ID["evidence-digest"]} />;
}
