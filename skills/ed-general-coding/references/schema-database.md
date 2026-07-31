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
- When one configuration owns exactly one environment, store that environment
  on the configuration row. Add an environment child table only when one
  configuration must own simultaneous environment records with independent
  lifecycle or cardinality.
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
- Keep SQL row structs private to the persistence module. Repositories should
  own the mapping and return domain models or explicit mutation outcomes, not
  leak `*Row` types into handlers and services.
- Split broad repositories by domain ownership. Do not expose a god repository
  that gives unrelated features access to every query or the raw connection
  pool.
- Nullable columns and `Option` fields must represent real persisted absence.
  Do not keep obsolete columns, always-null fields, or nullable joins merely
  because an earlier flow once used them.
- Make security configuration cardinality a persistence invariant. When a
  domain requires exactly one selected credential or key, update selection in
  one transaction and prevent or explicitly repair ambiguous active rows; do
  not make an unordered query choose whichever row happens to appear first.
- Store only the minimum state required to verify and advance a workflow.
  Separate immutable authorization context from stage-specific state, preserve
  the exact response data required for idempotency, and remove fields after
  their owning stage no longer needs them.
- Give transient authentication rows and encrypted PII an explicit retention
  deadline and cleanup owner. Consumption or expiry must not leave plaintext,
  stale signing material, or obsolete challenge state indefinitely.
- Low-entropy codes and enumerable identity values require a server-held keyed
  verifier with domain separation. Do not store an ordinary digest that a
  database reader can brute-force or enumerate offline.
- Encrypt retained secrets and authentication PII with separately owned,
  versioned keys, unique nonces, and record-and-field-bound authenticated data.
  Persist ciphertext format and key version explicitly, and remove plaintext
  through a verified migration rather than keeping a fallback column.
- For application-owned envelope encryption, generate one random data key per
  configuration, encrypt that key with the deployed master secret, and persist
  only the encrypted data key. Encrypt each secret field with its own nonce and
  authenticated data bound to the configuration, organization, environment,
  and field kind.

## Change Safety

- Preserve existing data when changing columns, enum values, constraints, or indexes.
- Call out destructive migrations before applying them.
- Include application code, migration file, and focused tests in the same PR when practical.
- For production or staging data changes, check current state and drift first, then apply the smallest clear migration.

## SQLx Queries

- Use SQLx's compile-time checked `query!`, `query_as!`, and `query_scalar!` macros for static SQL in Rust application code and tests.
- Use runtime `query`, `query_as`, or `query_scalar` only when the SQL is genuinely dynamic and cannot be expressed as a static checked query.
- Run checked-query builds with the repository's real migrated schema or its committed SQLx offline metadata; do not weaken a checked query merely to bypass local database setup.
- Make query cardinality explicit in repository names and implementations.
  Use `find_*` with `fetch_optional` for expected absence, `get_*` with
  `fetch_one` for required records, and explicit outcomes for conditional
  updates or deletes. Do not fetch an invariant relation optionally and defer
  the missing-record failure to a distant caller.
- Name repository writes for the persistence operation, such as `create`,
  `update_*`, or `set_*`, not for one initial lifecycle value. Pass `pending`,
  `approved`, or another status as data; do not encode it in a name such as
  `create_pending`.
- Return a typed applied, not-found, conflict, or already-final outcome from
  conditional mutations. Do not make callers infer mutation state from a
  leaked row, nullable field cluster, or affected-row count without domain
  meaning.
- Make comparison and failure charging one atomic transition for authentication
  attempts and other security budgets. Concurrent invalid guesses must not all
  compare against the same stale attempt count before increments are recorded.
- Reserve one-time proofs atomically for one immutable attempt and store a
  typed completion outcome. A retry of the same attempt may resume or return
  the same result; another identity, redirect, proof key, or message must not
  reuse the reservation.
- Coalesce required aggregates in SQL and return concrete numeric values. Do
  not expose `Option` for counts, sums, or maxima when the domain defines a
  concrete empty-set result.
