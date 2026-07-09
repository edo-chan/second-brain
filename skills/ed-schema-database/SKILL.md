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

## Data Modeling

- Define enum semantics in proto.
- Store enum values in the database as `SMALLINT`.
- Use `i16` at Rust persistence boundaries and validate/convert from proto enums before storing.
- Store addresses as text.
- Use Prost well-known types where applicable.
- Avoid duplicating data that can be reliably derived.
- When adding request or table fields, identify whether the value is user input, derived state, cached state, or source-of-truth state.

## Change Safety

- Preserve existing data when changing columns, enum values, constraints, or indexes.
- Call out destructive migrations before applying them.
- Include application code, migration file, and focused tests in the same PR when practical.
- For production or staging data changes, check current state and drift first, then apply the smallest clear migration.
