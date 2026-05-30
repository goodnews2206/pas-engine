/*
 * Typed fetch wrapper for the PAS API.
 * Returns null immediately when IS_DEMO_MODE is true (no network call made).
 * No auth headers. No retries. No mutations. No hidden network behavior.
 */

import { PAS_API_BASE_URL, IS_DEMO_MODE, API_TIMEOUT_MS } from "./config";
import { PasApiError, PasConnectionError } from "./errors";

export async function apiGet<T>(path: string): Promise<T | null> {
  if (IS_DEMO_MODE || !PAS_API_BASE_URL) return null;

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), API_TIMEOUT_MS);

  try {
    const res = await fetch(`${PAS_API_BASE_URL}${path}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      signal: controller.signal,
    });

    clearTimeout(timer);

    if (!res.ok) {
      throw new PasApiError(res.status, `PAS API responded with ${res.status}`);
    }

    return res.json() as Promise<T>;
  } catch (e) {
    clearTimeout(timer);
    if (e instanceof PasApiError) throw e;
    // AbortError (timeout) or network failure
    throw new PasConnectionError();
  }
}
