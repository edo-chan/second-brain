---
name: ed-schema-database
description: Migration-first schema and database change rules for Ed's repos. Use when modifying Prisma, SQLx, Postgres, ClickHouse, migrations, enum persistence, production or staging data, or database-backed request fields.
---

# Ed Schema Database

Use migrations as the source of truth and preserve production data by default.

## Migration Rules

- Prefer migrations over direct schema pushes.
- Do not use `db:push` in repos where migrations are expected.
- Use Tilt as the local source of truth for services such as Postgres.
- Apply schema changes through the repo's migration script.
- If a migration file was already applied locally and is modified, undo it first, then rerun the migration script.
- Do not add indexes unless explicitly requested.
- Do not add schema or migration comments.
- Default schema DDL to primary keys and required uniqueness constraints. Do not add `CHECK`, `FOREIGN KEY`, `EXCLUDE`, or similar constraints unless explicitly requested; preserve required-field `NOT NULL` semantics separately.
- This explicit constraint rule supersedes the Notion guide's broader foreign-key
  recommendation: add a foreign key only when the task or repository contract
  specifically requires that invariant.

## Data Modeling

- Define enum semantics in proto.
- Store enum values in the database as `SMALLINT`.
- Use `i16` at Rust persistence boundaries and validate/convert from proto enums before storing.
- Store addresses as text.
- Prefer readable storage types such as UUID or text identifiers, `TEXT`
  addresses, and integer amounts over opaque byte encodings.
- Prefer soft deletion for durable business records. Hard-delete only truly
  transient queue, cache, or disposable data.
- Use Prost well-known types where applicable.
- Avoid duplicating data that can be reliably derived.
- When adding request or table fields, identify whether the value is user input, derived state, cached state, or source-of-truth state.
- Identify each row's granularity: API request, domain item, billable item,
  confirmation, or transport-level group.
- Do not persist a transport-level group when request and per-item records
  already satisfy the consumers. Persist it only when it has its own lifecycle,
  source-of-truth role, or concrete query consumer.
- Keep request telemetry separate from domain and billing records so failures
  and replays do not create duplicate billable work.
- Store authoritative accounting derived from confirmed pre/post metadata, not
  predicted fee arithmetic.
- Keep business logic in service code. Avoid database functions, triggers, and
  materialized views unless a demonstrated database-level need outweighs the
  hidden behavior.

## Change Safety

- Preserve existing data when changing columns, enum values, constraints, or indexes.
- Call out destructive migrations before applying them.
- Include application code, migration file, and focused tests in the same PR when practical.
- For production or staging data changes, check current state and drift first, then apply the smallest clear migration.

## SQLx Queries

- Use SQLx's compile-time checked `query!`, `query_as!`, and `query_scalar!` macros for static SQL in Rust application code and tests.
- Use runtime `query`, `query_as`, or `query_scalar` only when the SQL is genuinely dynamic and cannot be expressed as a static checked query.
- Run checked-query builds with the repository's real migrated schema or its committed SQLx offline metadata; do not weaken a checked query merely to bypass local database setup.
