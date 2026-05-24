# PAS206 — Read-only Supabase snapshot adapter

## What PAS206 proves

PAS206 connects the PAS205 read-only proactive observer to existing PAS
Supabase tables through a strictly read-only snapshot adapter. It proves
that:

* PAS can pull a normalized pipeline snapshot — leads, calls, bookings,
  agents, and (optionally) callbacks — out of live Supabase tables
  without touching production data.
* The proactive observer is composable with a real data source, not just
  hand-seeded fixtures.
* Read access can be added to PAS without changing the engine, the
  scheduler, the worker, the Twilio path, or the Slack outbound surface.
* Missing or unreachable tables degrade gracefully into an
  `unavailable_sources` list rather than blowing up the digest.

The adapter is a single file:

  `app/services/proactive/supabase_snapshot_adapter.py`

and a CLI runner:

  `scripts/pas206_run_observer_from_supabase_snapshot.py`

## What PAS206 does NOT prove

PAS206 is deliberately the smallest possible read-only connector. It
does not prove any of the following — those are later phases:

* PAS206 does not surface the digest in Slack. (PAS207.)
* PAS206 does not propose any action, recommendation, or operator
  prompt. (PAS208.)
* PAS206 does not execute any bounded action, even an approved one.
  (PAS209.)
* PAS206 does not start a scheduler, worker, or background loop.
* PAS206 does not write, mutate, upsert, or RPC against Supabase.
* PAS206 does not call Twilio, send SMS, send email, or post to Slack.
* PAS206 does not introduce a new external vendor.
* PAS206 does not modify the PAS engine or live state machine.

## Why this is read-only by construction

The adapter calls only the following Supabase verbs:

  `.table(name).select(cols).eq("brokerage_id", value).limit(n).execute()`

The PAS206 readiness gate textually asserts that the adapter source
contains **no** `.insert(`, `.update(`, `.delete(`, `.upsert(`, or
`.rpc(` calls, and that it imports no Twilio / Slack outbound /
scheduler / worker modules. Every snapshot result carries a
`read_only=True` invariant on the envelope.

If a table is missing or a select fails for any reason, the adapter
catches the exception, marks that source `unavailable`, and continues.
The rest of the snapshot still loads. No exception escapes.

## Result envelope

`load_snapshot(client, brokerage_id, *, row_limit=500, loaded_at=None)`
returns a `SupabaseSnapshotResult`:

| Field                 | Meaning                                                   |
|-----------------------|-----------------------------------------------------------|
| `snapshot`            | A PAS205 `ObservedSnapshot`, ready for `observe()`        |
| `source_status`       | Per-source `"ok"` / `"empty"` / `"unavailable"`           |
| `unavailable_sources` | Tuple of sources that did not load                        |
| `row_counts`          | Per-source row count actually normalized                  |
| `loaded_at`           | ISO 8601 UTC timestamp the adapter ran at                 |
| `brokerage_id`        | Scope filter applied to every read                        |
| `read_only`           | Always `True` — invariant asserted by the readiness gate  |

## CLI

The CLI runs the adapter and the observer end-to-end:

```
python scripts/pas206_run_observer_from_supabase_snapshot.py \
    --brokerage-id demo-brokerage
```

Default behavior is **stub mode**. The CLI ships a deterministic
in-memory stub Supabase client so the script is safe to execute on a
laptop with no Supabase reachability and no production credentials in
the environment.

Live mode requires explicit operator acknowledgement:

```
python scripts/pas206_run_observer_from_supabase_snapshot.py \
    --brokerage-id <id> \
    --live \
    --i-understand-this-is-readonly
```

The adapter remains read-only regardless of the flag — the
acknowledgement gates only the intent to touch the live database, not
the adapter's behavior.

## How PAS206 moves PAS closer to proactive agents

PAS205 introduced the signal layer on seeded snapshots. PAS206 wires
that signal layer to live data without crossing any of the action
boundaries that would make PAS autonomous. The progression is:

| Phase  | Layer                                       |
|--------|---------------------------------------------|
| PAS205 | Signal generation from in-memory snapshots  |
| **PAS206** | **Read-only snapshot from Supabase**     |
| PAS207 | Slack proactive digest surface (read)       |
| PAS208 | Operator approval for proactive recommendations |
| PAS209 | Bounded action proposals                    |

Each step is additive and reversible. PAS206 in particular is fully
revertable by deleting one module and one script.

## Future path: PAS207

PAS207 will mount the PAS206 digest behind a Slack slash command. PAS207
must still not push notifications — it remains pull/read. It will reuse
the same observer and the same adapter; only the surface changes.

## Safety doctrine

* **READ-ONLY.** Only `select / eq / limit / order / execute`.
* **NO MUTATION.** No `insert / update / delete / upsert / rpc`.
* **NO TWILIO.** Calling logic is not imported.
* **NO SLACK OUTBOUND.** No Slack-API write calls.
* **NO SCHEDULER, NO WORKER, NO CRON.**
* **NO MIGRATIONS.** No `combined_supabase_migration.sql`.
* **NO SECRETS.** Credentials are never required by the adapter itself;
  they live with the injected client.
* **PARKED STASH UNTOUCHED.**
