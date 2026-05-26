import type { Metadata } from "next";
import ModuleSkeleton from "@/components/modules/ModuleSkeleton";
import { ROUTES_BY_ID } from "@/lib/navigation/routes";
import { MODULE_EMPTY_STATES } from "@/lib/demo/moduleEmptyStates";

export const metadata: Metadata = { title: "Recommendations" };

export default function RecommendationsPage() {
  return (
    <ModuleSkeleton
      route={ROUTES_BY_ID["recommendations"]}
      emptyState={MODULE_EMPTY_STATES["recommendations"]}
    />
  );
}
