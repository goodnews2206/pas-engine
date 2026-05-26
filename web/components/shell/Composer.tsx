"use client";

/*
 * PAS Composer — persistent interaction shell. Design System §11.3 / §16.1.
 *
 * Frontend-only demo interaction. No network requests.
 * Real PAS API connection point: replace handleSubmit's setTimeout with
 * a fetch to /api/pas/ask (or equivalent) in the API wiring step.
 *
 * Not a chatbot bubble — embedded into the operating surface.
 * Session context from DEMO_SESSION (build-time constant).
 */

import { useState, useRef, useEffect } from "react";
import { DEMO_SESSION } from "@/lib/session/demoSession";
import styles from "./Composer.module.css";

const PROMPT_EXAMPLES = [
  "What needs attention?",
  "Which leads are slipping?",
  "What should I handle next?",
  "Show recommendations.",
  "Explain the simulation evidence.",
] as const;

const DEMO_RESPONSE =
  "Here’s what I can help with in this demo shell: pipeline risks, " +
  "recommendations, evidence, integrations, and approvals. Real operational " +
  "answers will connect through the PAS API later.";

type ComposerPhase = "idle" | "thinking" | "responded";

const { user, workspace, permissionBoundary } = DEMO_SESSION;

export default function Composer() {
  const [value, setValue] = useState("");
  const [phase, setPhase] = useState<ComposerPhase>("idle");
  const [lastPrompt, setLastPrompt] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const canSubmit = value.trim().length > 0 && phase === "idle";
  const showChips = phase === "idle" && value.length === 0;
  const presenceText =
    phase === "thinking" ? "PAS is thinking…" : "PAS is observing";

  function handleChange(e: React.ChangeEvent<HTMLTextAreaElement>) {
    setValue(e.target.value);
    const el = e.target;
    el.style.height = "auto";
    el.style.height = `${el.scrollHeight}px`;
  }

  function handleSubmit() {
    if (!canSubmit) return;
    const prompt = value.trim();
    setLastPrompt(prompt);
    setValue("");
    if (textareaRef.current) textareaRef.current.style.height = "auto";
    setPhase("thinking");
    timerRef.current = setTimeout(() => setPhase("responded"), 1400);
  }

  function handleDismiss() {
    setPhase("idle");
    setLastPrompt("");
    textareaRef.current?.focus();
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (canSubmit) handleSubmit();
    }
  }

  function handleChipClick(prompt: string) {
    setValue(prompt);
    textareaRef.current?.focus();
  }

  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, []);

  return (
    <div className={styles.composer} role="region" aria-label="PAS composer">
      <div className={styles.inner}>
        {/* Response panel — appears after submit, dismissible */}
        {phase === "responded" && (
          <div className={styles.responsePanel} role="status">
            <div className={styles.responseHeader}>
              <span className={styles.responsePrompt}>{lastPrompt}</span>
              <button
                type="button"
                className={styles.dismissButton}
                onClick={handleDismiss}
                aria-label="Dismiss PAS response"
              >
                <CloseIcon />
              </button>
            </div>
            <p className={styles.responseText}>{DEMO_RESPONSE}</p>
            <p className={styles.responseDisclaimer}>
              PAS has not changed live customer behavior.
            </p>
          </div>
        )}

        {/* Input row */}
        <div className={styles.inputRow}>
          <div
            className={`${styles.presence} ${phase === "thinking" ? styles.presenceThinking : ""}`}
            aria-label={`PAS status: ${phase === "thinking" ? "thinking" : "observing"}`}
          >
            <span className={styles.presenceDot} aria-hidden="true" />
            <span className={styles.presenceLabel}>{presenceText}</span>
          </div>

          <textarea
            ref={textareaRef}
            className={styles.input}
            value={value}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            placeholder="Ask PAS what needs attention, which leads are slipping, or what should happen next."
            rows={1}
            aria-label="Message PAS"
            aria-describedby="composer-hint"
            disabled={phase === "thinking"}
          />

          <button
            type="button"
            className={styles.sendButton}
            onClick={handleSubmit}
            disabled={!canSubmit}
            aria-label="Send message to PAS"
          >
            <SendIcon />
          </button>
        </div>

        {/* Prompt example chips — visible when idle and input is empty */}
        {showChips && (
          <div className={styles.chipsRow} aria-label="Example prompts">
            {PROMPT_EXAMPLES.map((prompt) => (
              <button
                key={prompt}
                type="button"
                className={styles.chip}
                onClick={() => handleChipClick(prompt)}
              >
                {prompt}
              </button>
            ))}
          </div>
        )}

        {/* Session meta + keyboard hints */}
        <div className={styles.sessionMeta}>
          <span className={styles.metaItem}>{workspace.name}</span>
          <span className={styles.metaSep} aria-hidden="true">·</span>
          <span className={styles.metaItem}>{user.role}</span>
          <span className={styles.metaSep} aria-hidden="true">·</span>
          <span className={styles.metaItem}>{permissionBoundary}</span>
          <span className={styles.metaSep} aria-hidden="true">·</span>
          <span id="composer-hint" className={styles.hintGroup}>
            <kbd className={styles.kbd}>Enter</kbd>
            <span className={styles.hintText}> to ask</span>
            <span className={styles.metaSep} aria-hidden="true">·</span>
            <kbd className={styles.kbd}>Shift+Enter</kbd>
            <span className={styles.hintText}> for newline</span>
          </span>
        </div>
      </div>
    </div>
  );
}

function CloseIcon() {
  return (
    <svg
      width="10"
      height="10"
      viewBox="0 0 10 10"
      fill="none"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M1 1l8 8M9 1L1 9"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
    </svg>
  );
}

function SendIcon() {
  return (
    <svg
      width="15"
      height="15"
      viewBox="0 0 15 15"
      fill="none"
      aria-hidden="true"
      focusable="false"
    >
      <path
        d="M2 7.5h11M9.5 3L13 7.5 9.5 12"
        stroke="currentColor"
        strokeWidth="1.4"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
