# PAS301C — Ownership, Portability & Memory Provenance

> Status: **data-model specification (docs-only)** — no code, no schema, no
> migrations, no UI, no dependency, no auth, no PAS Brain behavior change.
> Owner: ORVN Labs. Naming: **PAS = Proactive Assistant for Scale.**
> Anchored on: `main` @ `99eab94` (PR #80 — PAS301B Workspace Switcher Shell).
> Depends on: PAS300 (doctrine), PAS301 (identity/ownership/session/workspace),
> PAS301.5 (auth decision), PAS212 (memory candidate pipeline).

---

## 1. Status / Scope

- **Checkpoint:** PAS301C, the third and final slice of the PAS301 "shell + spec"
  tranche, after **PAS301A** (Account/Profile Shell) and **PAS301B** (Workspace
  Switcher Shell).
- **Docs-only.** This document **changes no code, schema, migrations, frontend,
  backend, dependencies, lockfiles, workflows, secrets, or memory behavior.** It
  introduces **no executable SQL.**
- **What it is:** the canonical **data doctrine** — the ownership, portability,
  and memory-provenance contract — that every later auth, workspace, role,
  offboarding, and PAS Brain checkpoint **must reference and must not violate.**
  It converts the prose doctrine in PAS301 §4/§19/§21 into a normative,
  implementation-guiding model, grounded against the current repository.
- **Why now:** the data doctrine must be settled **before** backend enforcement
  (PAS301F/G/I/J), the PAS211G JWT/route migration, or any expansion of PAS Brain
  memory power. Building enforcement on an undefined doctrine is the risk this
  checkpoint removes.

---

## 2. Core Doctrine (locked)

The following statements are **binding** for all downstream work:

1. **A person owns their identity and professional self.** Identity, profile,
   preferences, the name/tone they gave PAS, self-authored scripts, personal
   coaching, and generalized personal operating patterns are the person's.
2. **A workspace governs the business records created within it.** Client PII,
   leads, deals, transactions, recordings/transcripts, SOPs, integration
   credentials, compliance records, and audit trails are workspace-owned.
3. **Workspaces borrow access to the person.** A workspace is granted scoped
   access to a person's attention and labor for the life of the membership; it
   never acquires the person. When membership ends, the borrowed access ends.
4. **Client, transaction, compliance, recording, integration, and audit records
   do not leave the workspace** — not by export, not by account portability, not
   by hostile departure.
5. **Portable memory must be PII-clean and client-data-free.** Anything that
   travels with the person carries no client PII and no workspace-confidential
   data, by construction.
6. **Ties resolve toward the workspace.** Any ambiguous or mixed-subject record
   or memory is classified as workspace-governed and stays.
7. **PII-bearing memory is non-portable by default.** Carrying PII or regulated
   data forces the workspace-governed, non-portable classification.

---

## 3. Ownership Taxonomy

Seven classes. Maps PAS301 §4 classes A–F into implementable owner/portability
tuples (the new "workspace-governed person-associated" row makes the §4C/§4D
"about the person but owned by the tenant" case explicit).

| Class | Owner | Portability | Examples | Visibility | Offboarding behavior |
|---|---|---|---|---|---|
| **Person-owned** | Person identity | **Portable** (PII-clean) | identity, profile, PAS name/tone, self-authored scripts, personal coaching, generalized operating patterns | The person only | Travels with the person, intact |
| **Personal-workspace-owned** | Person (controller of own tenant) | **Portable** (person controls) | self-sourced leads/sphere, private notes, personal documents | The person only | Stays in the person's own workspace, which they keep |
| **Workspace-governed, person-associated** | Workspace | **Non-portable** | "agent X handled lead Y", assignment/ownership records, a team lead's knowledge *about* members | By role within the workspace | Access revoked at departure; record retained by workspace |
| **Portable personal preference** | Person | **Portable** (PII-clean only) | tone, working hours, notification preferences, talk-track style | The person only | Travels with the person |
| **Non-portable client/transaction record** | Brokerage workspace | **Never portable** | client PII, brokerage-sourced leads, deals, recordings/transcripts, integration credentials, compliance/audit | By role; retention-bound | Retained by workspace under legal retention; never exported to the person |
| **Structural / aggregate learning** | Workspace | **Non-portable** (tenant-scoped) | team standards, source-lead-quality signals, aggregate operational health | By role | Stays with the workspace |
| **ORVN / system operational telemetry** | ORVN platform | **Non-portable** | cross-tenant platform health, provisioning, incident records, platform audit | ORVN internal scope only | Governed by ORVN platform policy; never customer-facing |

---

## 4. Subject × Source Resolving Rule

Every record or memory is classified by two axes:

- **Subject** — who/what it is *about* (the person, a client, a deal, a
  colleague, the organization, a lead source).
- **Source** — where the evidence *came from* (the person's own observed
  behavior, or tenant data such as a call, document, or record).

Decision order (first match wins):

1. **About a client / deal / workspace process → workspace-governed.**
2. **Derived from tenant data (call, recording, document, record) →
   workspace-governed.**
3. **PII-bearing (carries client or third-party personal data) →
   workspace-governed, non-portable.**
4. **About another person (colleague, team member, lead) → workspace-governed**;
   never the departing person's to keep.
5. **Generalized from the person's own behavior AND PII-clean AND
   client-data-free → person-portable may be allowed.**
6. **Uncertain / mixed → default to workspace-governed.** Ties resolve toward
   the workspace.

> The bright line: *about the person, from the person, PII-clean* → portable.
> Everything else → governed by the workspace.

---

## 5. Current Repo Reality (grounding)

This spec is grounded against the live repository at the anchor commit:

- **Tenant/workspace unit = brokerage.** `brokerages` (`scripts/schema.sql`) is
  the single isolation unit; there is **no** independent person/identity entity
  and **no** workspace-type concept (personal/team/brokerage/ORVN).
- **Membership exists, identity does not.** `brokerage_users` (`brokerage_id`,
  `user_id` → Supabase `auth.users`, `role`, `removed_at`) and `admin_users`
  carry membership/role; there is no durable person object spanning workspaces.
- **Agents are routing/metrics assets, not login identities.** The `agents` table
  tracks human agents for routing and performance, not authenticated people.
- **Business records are brokerage-scoped.** `leads`, `calls`, `bookings`,
  `pas_events`, `training_logs`, `audit_log`, `lead_ingestion_dedupe` are all
  scoped by `brokerage_id`; tenant isolation is enforced in application code
  (RLS policies in `migrate_v9` are defined but dormant under the service-role
  key).
- **MemoryCandidate** (`app/services/memory/candidate_contracts.py`) currently
  carries: `brokerage_id`, `subject_type` (`lead` / `brokerage` / `agent` /
  `source`), `subject_id`, `candidate_type`, `proposed_memory` (summary only),
  `evidence_refs`, `provenance` (free-text), `confidence`, `status`
  (`candidate` / `approved` / `rejected` / `archived`), `reviewed_by`,
  `reviewed_at`.
- **Hard rules already enforced today:** tenant isolation mandatory (no
  `brokerage_id` → invalid); evidence mandatory; **raw-transcript tokens
  forbidden** (`transcript` / `turns` / `raw_text` / `utterance`); candidate by
  default (manual review first).
- **Governed context boundary** (`app/services/memory/memory_context_boundary.py`)
  is default-off, tenant-scoped, approved-only, sanitized, read-only — it changes
  no production behavior unless explicitly enabled.

**Gaps this spec names (to be implemented by later checkpoints, not here):**
no distinction between **owning** and **originating** workspace; no
**portability_scope**; no explicit **sensitivity_class** (only the transcript
token block); no **retention/offboarding_behavior**; no **person/self** subject
owned by a personal workspace; no **workspace type**.

---

## 6. Target Memory-Provenance Field Model

Conceptual target fields every memory should eventually carry. **This is a
specification — no executable SQL, no migration.** "Current support" is assessed
against `MemoryCandidate` and the schema at the anchor commit.

| Field | Purpose | Example values | Current support | Likely implementing checkpoint |
|---|---|---|---|---|
| **subject_type** | who/what the memory is about | `lead`, `brokerage`, `agent`, `source`, *(target: add `person/self`)* | **Partial** (no `person/self`) | PAS301G / PAS306 |
| **subject_id** | stable id of the subject | `lead_123`, `agent_7` | **Yes** | — |
| **source_type** | kind of evidence origin | `observed_behavior`, `call`, `document`, `record` | **Partial** (implicit in `provenance` string) | PAS306 |
| **source_workspace_id** | workspace whose data produced the evidence | a workspace id | **Partial** (conflated with `brokerage_id`) | PAS301G |
| **owning_workspace_id** | who governs the memory now | a workspace id | **Yes** (`brokerage_id`) | — |
| **originating_workspace_id** | where the memory was first formed | a workspace id | **Missing** | PAS301G / PAS301J |
| **portability_scope** | may it travel with the person | `portable`, `non_portable`, `conditional_pii_clean` | **Missing** | PAS301C-derived; PAS301J |
| **approval_state** | review lifecycle | `candidate`, `approved`, `rejected`, `archived` | **Yes** (`status`) | — |
| **evidence_refs** | non-raw evidence pointers | `["event:abc", "booking:xyz"]` | **Yes** | — |
| **sensitivity_class** | data-sensitivity tag | `non_sensitive`, `confidential`, `pii` | **Partial** (transcript-token block only) | PAS301I / PAS306 |
| **retention_behavior** | how long / under what rule it is kept | `retain_with_tenant`, `person_retained`, `expire` | **Missing** | PAS301J |
| **offboarding_behavior** | what happens on departure | `retain_with_tenant`, `travels_with_person`, `delete` | **Missing** | PAS301J |
| **raw_data_exclusion** | no raw transcript/PII text stored | enforced boolean / validation rule | **Yes** (forbidden-token validation) | — (extend to PII) |

---

## 7. Portability Rules

- **Travels with the person** (person-owned, PII-clean): identity, profile,
  preferences, PAS name/tone, self-authored scripts, personal coaching,
  generalized operating patterns.
- **Never travels:** client PII, brokerage-sourced leads, deals/transactions,
  recordings/transcripts, integration credentials, compliance/audit records,
  internal SOPs, source-specific brokerage data, and any memory *about another
  person*.
- **May travel only after sanitization:** a personal insight derived from the
  person's own behavior that *could* reference client/workspace data travels
  **only** once stripped to a PII-clean, client-data-free generalization
  (`conditional_pii_clean`). If it cannot be cleanly generalized, it does not
  travel.
- **Belongs to workspace history:** assignment/ownership records, who-did-what,
  decisions recorded in the workspace, and the audit trail.
- **Becomes structural learning:** repeated, de-identified patterns (team
  standards, source-quality signals, aggregate operational health) stay
  workspace-scoped.
- **ORVN may see only platform telemetry:** cross-tenant health, provisioning,
  and incident signals — never customer business data as content.

---

## 8. Offboarding Rules

When a person leaves a workspace (removed by an admin/owner, or by leaving):

- **Tenant access revoked immediately** — including any residual visibility a
  former team lead had into members.
- **Workspace records retained by the workspace** — client PII, leads, deals,
  recordings, compliance and audit records stay intact, under retention.
- **In-flight obligations reassigned inside the workspace** — pending callbacks
  and live deals are reassigned within the tenant so clients are never dropped;
  nothing is exported to the departing person.
- **Personal capital survives** — identity, profile, preferences, personal PAS
  configuration, self-authored scripts, and PII-clean personal coaching leave
  with the person, whole.
- **The agent cannot export** tenant PII, recordings, transcripts, leads, client
  records, deal records, source-specific brokerage data, or internal SOPs — under
  any flow, including account export and hostile departure.
- **"My obligations" view** may show only the *person's own* obligations across
  their workspaces; it must **never** surface another workspace's client data or
  records into the personal layer or any other workspace.

---

## 9. PAS Brain Memory Rules (locked)

- **Manual approval remains mandatory.** No candidate becomes usable memory
  without an explicit operator decision. Automatic approval is permitted **only**
  if a future checkpoint explicitly authorizes it.
- **Raw transcripts remain excluded.** Memory stores summaries and non-raw
  evidence pointers, never call text. (Extend the existing forbidden-token rule
  toward explicit PII exclusion.)
- **Tenant isolation remains mandatory.** A memory without an owning workspace is
  invalid; one workspace's memory is never returned to another.
- **Approved memory must carry provenance** — subject, source, owning workspace,
  and evidence — so it can be governed and, at offboarding, correctly retained or
  released.
- **Active workspace scopes retrieval.** Brain queries run within the active
  workspace only.
- **No cross-workspace citations.** Every cited piece of evidence resolves inside
  the active workspace; a citation exposing another workspace's record is a
  breach.
- **Personal coaching can be reused across workspaces only if PII-clean and
  client-data-free.** It never carries personal-workspace client data into a
  brokerage, nor brokerage data into the personal layer.
- **Workspace-governed memory stays inside the workspace.**

---

## 10. Downstream Checkpoints That Must Reference This Spec

- **PAS301F** — Backend Auth Boundary (server-side identity/session enforcement).
- **PAS301G** — Workspace Membership Model (memberships, roles, owning vs.
  originating workspace).
- **PAS301I** — Role Enforcement Server-Side (per-workspace authorization +
  sensitivity-aware visibility).
- **PAS301J** — Offboarding Lifecycle (retention, portability, reassignment).
- **PAS302** — Role-Specific Experience Map (UX must reflect these ownership
  boundaries).
- **PAS303** — Agent Cockpit (person-owned surface; must honor portability).
- **PAS306** — PAS Brain / queryable memory (provenance fields, sensitivity, no
  cross-tenant citations).
- **PAS211G** — JWT verification / route migration (the seam where workspace
  scope becomes server-enforced; RLS becomes effective).

---

## 11. Non-Goals

PAS301C explicitly does **not**:

- change any schema or add any migration;
- implement any authentication or session handling;
- implement role enforcement;
- change any PAS Brain or memory-candidate behavior;
- change the governed context boundary or its default-off flag;
- change raw-transcript handling;
- change any frontend or backend code;
- add dependencies, lockfiles, workflows, or runtime/deploy config.

---

## 12. Locked Invariants

Future work **must not** violate:

- A person owns their identity and professional self.
- A workspace governs the business records created within it.
- Ties resolve toward the workspace.
- PII-bearing memory is non-portable by default.
- Manual approval is required before memory is used.
- Raw data (transcripts / PII text) is excluded from stored memory.
- Active-workspace scoping governs retrieval.
- No cross-tenant leakage in queries, citations, notifications, or search.
- `brokerage_id` (workspace identity) is never trusted from an inbound payload;
  it is derived from the authenticated server-side context.

---

### Validation note

This document is **docs-only**. It makes **no** changes to code, schema,
migrations, frontend, backend, dependencies, lockfiles, workflows, secrets, the
PAS209 work, or memory behavior. It defines the ownership, portability, and
memory-provenance data doctrine and the fields/rules future checkpoints must
implement; it implements none of it. Nothing is pushed.
