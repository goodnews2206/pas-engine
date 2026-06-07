"""PAS213B.1 — durable dedupe migration readiness (safety assertions).

These guard the *migration file* itself (scripts/migrate_v8_digital_ingestion_
dedupe.sql) so it stays safe to apply by hand in the Supabase SQL editor before
any paid customer data flows through PAS. They do NOT apply the migration and do
NOT touch any database — they read the committed SQL text only.

Companion runbook: docs/pas213b_1_dedupe_migration_runbook.md.
"""
import os
import re

REPO_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
)
MIGRATION = os.path.join(
    REPO_ROOT, "scripts", "migrate_v8_digital_ingestion_dedupe.sql"
)
RUNBOOK = os.path.join(
    REPO_ROOT, "docs", "pas213b_1_dedupe_migration_runbook.md"
)


def _sql():
    with open(MIGRATION, encoding="utf-8") as fh:
        return fh.read()


def _executable_sql(text):
    """SQL with line comments (-- ...) stripped, so assertions look at DDL only,
    never at the explanatory header which legitimately mentions phone/email."""
    out = []
    for line in text.splitlines():
        idx = line.find("--")
        out.append(line if idx == -1 else line[:idx])
    return "\n".join(out)


# ── existence ──────────────────────────────────────────────────────
def test_migration_file_exists():
    assert os.path.isfile(MIGRATION), "PAS213B durable dedupe migration missing"
    assert _sql().strip(), "migration file is empty"


# ── additive / non-destructive ─────────────────────────────────────
def test_migration_has_no_destructive_sql():
    sql = _executable_sql(_sql())
    for verb in (r"\bDROP\b", r"\bDELETE\b", r"\bTRUNCATE\b", r"\bUPDATE\b"):
        assert not re.search(verb, sql, re.IGNORECASE), \
            f"migration must not contain destructive {verb}"
    # The only ALTER permitted is enabling RLS (additive), never a column/constraint drop.
    for alter in re.findall(r"ALTER\s+TABLE.*?;", sql, re.IGNORECASE | re.DOTALL):
        assert "ENABLE ROW LEVEL SECURITY" in alter.upper(), \
            f"unexpected ALTER TABLE statement: {alter!r}"


def test_migration_is_idempotent_create():
    sql = _executable_sql(_sql()).upper()
    assert "CREATE TABLE IF NOT EXISTS" in sql
    assert "CREATE INDEX IF NOT EXISTS" in sql


# ── expected structure: table + unique + index ─────────────────────
def test_migration_creates_expected_table_and_constraints():
    sql = _executable_sql(_sql())
    assert "lead_ingestion_dedupe" in sql
    # tenant-scoped uniqueness (the race backstop)
    assert re.search(
        r"UNIQUE\s*\(\s*brokerage_id\s*,\s*dedupe_key\s*\)", sql, re.IGNORECASE
    ), "tenant-scoped UNIQUE(brokerage_id, dedupe_key) missing"
    # secondary lookup index
    assert "lead_ingestion_dedupe_ext_idx" in sql


# ── no raw PII columns ─────────────────────────────────────────────
def test_migration_has_no_raw_pii_columns():
    sql = _executable_sql(_sql())
    # Inspect only the column list inside CREATE TABLE ( ... ).
    body = re.search(
        r"CREATE\s+TABLE[^(]*\((.*?)\)\s*;", sql, re.IGNORECASE | re.DOTALL
    )
    assert body, "could not locate CREATE TABLE column list"
    cols = body.group(1).lower()
    for pii in ("phone", "email", "message", "notes", "transcript", " name "):
        assert pii not in cols, f"dedupe ledger must not store raw PII column: {pii!r}"
    # the allowed-but-similarly-named id columns are fine
    assert "brokerage_id" in cols and "dedupe_key" in cols
    assert "external_lead_id" in cols  # vendor id, not PII


# ── RLS enabled (repo parity) ──────────────────────────────────────
def test_migration_enables_rls():
    sql = _executable_sql(_sql()).upper()
    assert "ENABLE ROW LEVEL SECURITY" in sql, \
        "RLS must be enabled to match leads / calls / pas_events / audit_log"


# ── self-contained: no dependency on tables it doesn't create ──────
def test_migration_has_no_foreign_keys_or_external_deps():
    sql = _executable_sql(_sql())
    assert not re.search(r"\bREFERENCES\b", sql, re.IGNORECASE), \
        "dedupe ledger uses soft refs only (no FK), like pas_events / audit_log"
    assert "auth.users" not in sql, "migration must not depend on auth.users"


# ── runbook companion exists and covers the required sections ──────
def test_runbook_exists_and_is_complete():
    assert os.path.isfile(RUNBOOK), "PAS213B.1 migration runbook missing"
    with open(RUNBOOK, encoding="utf-8") as fh:
        doc = fh.read().lower()
    for needle in (
        "migrate_v8_digital_ingestion_dedupe.sql",
        "pre-apply",
        "verification",
        "rollback",
        "before migration",
        "after migration",
        "duplicate",
        "paid",
    ):
        assert needle in doc, f"runbook missing section/keyword: {needle!r}"


# ── readiness must not have applied the migration in code ──────────
def test_no_code_applies_the_migration():
    """The migration stays operator-applied. No python should read/execute the
    .sql file or auto-create the table."""
    offenders = []
    for base in ("app", "scripts"):
        root = os.path.join(REPO_ROOT, base)
        for dirpath, _dirs, files in os.walk(root):
            if "__pycache__" in dirpath:
                continue
            for name in files:
                if not name.endswith(".py"):
                    continue
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    text = fh.read()
                if "migrate_v8_digital_ingestion_dedupe.sql" in text:
                    # mentioning the filename in a docstring/log is fine;
                    # actually opening/executing it is not.
                    if re.search(
                        r"open\([^)]*migrate_v8_digital_ingestion_dedupe",
                        text,
                    ):
                        offenders.append(path)
                if "CREATE TABLE" in text and "lead_ingestion_dedupe" in text:
                    offenders.append(path)
    assert not offenders, f"migration must not be applied by code: {offenders}"
