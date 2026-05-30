/*
 * Demo safety assertions.
 *
 * Pure functions — usable in later tests to guarantee every demo object
 * carries the safety invariant (`demoOnly: true` + `noLiveBehavior: true`).
 * No side effects, no network, no mutations.
 */

import type { DemoMeta } from "./types";

/** True only when the value carries both demo-safety flags. */
export function hasNoLiveBehavior(value: unknown): value is DemoMeta {
  return (
    typeof value === "object" &&
    value !== null &&
    (value as { demoOnly?: unknown }).demoOnly === true &&
    (value as { noLiveBehavior?: unknown }).noLiveBehavior === true
  );
}

/** Throws if a single object is not demo-only + no-live-behavior. */
export function assertDemoOnlyObject(value: unknown): asserts value is DemoMeta {
  if (!hasNoLiveBehavior(value)) {
    throw new Error(
      "Demo invariant violated: object is not { demoOnly: true, noLiveBehavior: true }.",
    );
  }
}

/** Throws if any item in a collection breaks the demo-only invariant. */
export function assertDemoOnlyCollection(
  items: readonly unknown[],
): asserts items is readonly DemoMeta[] {
  items.forEach((item, index) => {
    if (!hasNoLiveBehavior(item)) {
      throw new Error(
        `Demo invariant violated at index ${index}: item is not demo-only.`,
      );
    }
  });
}
