/*
 * API config — derived from build-time env vars.
 * NEXT_PUBLIC_PAS_API_BASE_URL is optional.
 * When absent the app operates in demo mode with no network calls.
 */

export const PAS_API_BASE_URL: string | undefined =
  process.env.NEXT_PUBLIC_PAS_API_BASE_URL || undefined;

/** True when no API base URL is configured — app renders demo shell only. */
export const IS_DEMO_MODE = !PAS_API_BASE_URL;

/** Fetch timeout for all PAS API calls. */
export const API_TIMEOUT_MS = 8_000;
