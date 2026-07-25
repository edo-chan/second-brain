---
name: ed-rust-service-style
description: Rust code organization, workflow layout, async boundaries, formatting, linting, and testing preferences for Ed's service repos. Use when editing Rust services, workflows, handlers, modules, or tests.
---

# Ed Rust Service Style

Favor small, explicit, local changes that match the surrounding module style.

## Code Organization

- Use `mod.rs` only for wiring and exports. Do not put business logic there.
- Keep types next to the consumer that exposes or uses them.
- Avoid giant shared type files, vendor type dumps, and premature type extraction.
- Do not extend generic vendor request/response wrappers or generic JSON deserialization APIs just because existing code uses them.
- Prefer explicit endpoint-specific methods that return concrete response structs.
- Do not let `serde_json::Value` or raw vendor response bodies cross the vendor-library boundary.
- Do not add pass-through helpers that only rename or forward another call.

## Workflow Layout

- Organize workflow code under `Workflow/<workflow name>/`.
- Put the workflow definition in `Workflow/<workflow name>/definition.rs`.
- Put the main activity implementation in `Workflow/<workflow name>/activity/<activity name>/definition.rs`.
- Put activity-specific files under `Workflow/<workflow name>/activity/<activity name>/files/`.
- Do not add flat activity files like `Workflow/<workflow name>/activity/<activity name>.rs`.

## Rust Style

- Avoid `unwrap()`, `expect()`, and panic-based control flow in production
  paths. Propagate or handle errors explicitly; panic only when terminating the
  process is the intended behavior.
- Prefer expression-style error propagation with `?` and `map_err` when a
  branch would only wrap and return an error.
- Keep control flow flat. Prefer early returns or one clear `match` over nested
  condition towers.
- Keep every function concise, focused, and single-purpose. When a function becomes difficult to scan or mixes phases, split it into concrete focused functions before adding more logic.
- Prefer typed errors and structured responses where the service already has them.
- Avoid stringly typed error plumbing unless existing code does it.
- Do not write generic Rust code unless Ed explicitly approves it. This includes
  generic functions, structs, enums, type aliases, traits, and explicit lifetime
  parameters. Prefer concrete types and elided lifetimes.
- Prefer owned data and simple concrete types when borrowing would add lifetime
  plumbing without a demonstrated need.
- Keep async boundaries visible. Do not hide network, database, or signing work inside helpers that look pure.
- For API handlers, keep validation, domain logic, and response mapping easy to follow. Extract helpers only when readability actually improves.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.
- Keep dynamic log values in structured fields and log messages
  low-cardinality. Use `info` for normal lifecycle events, `warn` for degraded
  but recoverable behavior, and `error` for failed operations.
- Do not extract helpers that only rename, clone, trim, borrow, convert, or map
  a small enum to a string. Keep the operation inline at its consumer. Add a
  helper or inherent method only when reuse is real or the mapping is domain
  behavior that deserves one authoritative boundary.
- Prefer descriptive names over dense acronyms.

## Tests

- Keep service tests in separate test files most of the time. Inline tests are
  appropriate for small local helpers, especially in `common/` crates.

## Lifecycle And Accounting

- Keep top-level phases visible: validation, idempotency, preparation,
  irreversible external call, accepted state, confirmation, accounting,
  persistence, and response mapping.
- Make the irreversible boundary explicit. A later nested error must not reset
  state in a way that permits the same external effect to run again.
- Do not add a production trait merely because a test framework exists. A trait
  is justified when production code owns a replaceable dependency boundary,
  such as `Arc<dyn VendorClient>`, even when a Mockall mock is currently the
  only alternate implementation.
- Mockall concrete-struct mocks have a different type from the real struct.
  Replacing a concrete dependency therefore requires `mockall_double`,
  test-only import rewriting, or generic code. Do not require concrete-struct
  mocking when trait injection is the simpler production shape.
- Keep dependency traits focused on the methods their consumers need. Treat the
  thin trait implementation that delegates to the concrete client as boundary
  wiring, not as a prohibited pass-through helper.
- When a consuming crate mocks a trait from another crate, a local `mock!`
  declaration may need to repeat the trait methods. Accept that when it is the
  simplest local test boundary; add an exported or feature-gated shared mock
  only when multiple consumers justify the extra test-support surface.
- Derive billing and spend from authoritative confirmed pre/post state. Treat
  predicted fees and locally reconstructed arithmetic as estimates, not final
  accounting.
- For batch or bundle behavior, include a success test with multiple items that
  proves order, cardinality, and per-item result mapping.

## Redis

- Use `deadpool_redis` for Redis access in Rust services. Do not introduce unmanaged raw Redis connections.
- Acquire connections from the pool at the visible async boundary and keep Redis commands explicit.
- When `rediss://` support is required, enable the underlying `redis` crate's Tokio/Rustls transport feature, but continue to manage connections and issue commands through `deadpool_redis`.

## Validation

- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo's standard formatter.
- Run focused tests for touched behavior.
- Run `cargo clippy --all-targets` for service changes when practical.
- Report any checks that could not be run and why.
