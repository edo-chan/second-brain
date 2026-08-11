---
name: ed-rust-coding
description: Rust implementation and review standards for Ed's repositories. Use when editing or reviewing Rust crates, services, workflows, handlers, modules, async boundaries, errors, logging, persistence consumers, or tests. Use ed-solana-coding as the primary skill for Solana program work.
---

# Ed Rust Coding

Favor small, explicit, local changes that match the surrounding module style.

## Code Organization

- Use `lib.rs` and `mod.rs` only for module wiring and exports. Do not put
  business logic in either file.
- Keep top-level files under `handler/api/` limited to endpoint handler
  implementations. Put handler-specific validation, orchestration, parsing,
  state-machine, and other supporting code under
  `handler/api/<handler_name>/`; do not add sibling top-level helper files that
  look like additional API handlers.
- Keep types next to the consumer that exposes or uses them.
- Avoid giant shared type files, vendor type dumps, and premature type extraction.
- Organize service modules around stable domains or capabilities. Avoid broad
  function-stage buckets such as `start_*`, `setup_*`, `helpers`, or `store`
  when the code actually belongs to authentication, credentials, developer
  access, client applications, or another named domain.
- Keep transport modules and service implementations named for the stable
  product domain and caller boundary. A provider-specific operation can live
  under that domain module without turning the whole service into a
  provider-named surface.
- Keep top-level service structs flat. Do not retain a clone of a previous or
  superseded service implementation, pass a whole service implementation into
  a child function, or introduce a child service merely to reach a few
  dependencies. Pass the concrete repository, client, signer, configuration,
  or value the operation needs.
- Do not extend generic vendor request/response wrappers or generic JSON deserialization APIs just because existing code uses them.
- Prefer explicit endpoint-specific methods that return concrete response structs.
- Name the concrete third-party adapter after the vendor with a `Connector`
  suffix, such as `MeldConnector`. Do not call a third-party integration a
  generic `Client`, `Service`, or `Manager`.
- When an API layer needs unit-test substitution, define a focused
  consumer-owned trait around the vendor connector's typed endpoint methods
  and inject that trait into the API service. The concrete connector
  implementation may delegate those typed calls; do not add a connector
  factory or expose transport-generic methods through the trait.
- Do not let `serde_json::Value` or raw vendor response bodies cross the vendor-library boundary.
- Do not add pass-through helpers that only rename or forward another call.
- Construct a concrete client directly when the only variable is its validated
  configuration. Do not add a factory trait whose implementation only calls
  that client's constructor.
- When a request selects the vendor environment or credential, keep both out
  of the service implementation and long-lived client state. Validate the
  environment in the request, load the environment-scoped encrypted
  credential in that RPC, decrypt it to `SecretBox`, construct the concrete
  client, and pass the borrowed secret to each typed endpoint call.
- Do not hide repository lookup, lifecycle checks, secret decryption, client
  construction, and one vendor call behind a `Resolver`, `Runtime`,
  `Context`, factory, or forwarding helper. Keep that sequence visible in each
  RPC. Prefer short local duplication when extraction would only rename those
  steps.
- Do not add a client configuration struct when the constructor only needs one
  validated enum plus fixed library defaults. Pass the enum directly and keep
  fixed protocol values at the vendor boundary.
- Do not create a domain-named cipher type whose only state is a master key and
  whose methods forward to encryption primitives. Put concrete envelope
  encryption functions in the shared cipher crate, keep key inputs in
  `SecretBox`, and call those functions at the visible encrypt/decrypt
  boundary.
- Do not inject or store a cipher helper object on an API service
  implementation. Retain only the required secret key material, if the
  endpoint owns it, and pass that secret explicitly to the shared cipher
  function in the RPC.
- Do not hide vendor requests behind `get_body`, `post_body`, a string HTTP
  method, an optional body, or a generic request function. Each typed endpoint
  must visibly build and send its concrete HTTP request, check status, read the
  body, and parse its concrete response.
- Do not retry in a generic HTTP transport loop. Add an endpoint-specific
  retry only after its idempotency and replay contract is proven. POST requests
  are not retryable by default.

## Workflow Layout

- Organize workflow code under `Workflow/<workflow name>/`.
- Put the workflow definition in `Workflow/<workflow name>/definition.rs`.
- Put the main activity implementation in `Workflow/<workflow name>/activity/<activity name>/definition.rs`.
- Put activity-specific files under `Workflow/<workflow name>/activity/<activity name>/files/`.
- Do not add flat activity files like `Workflow/<workflow name>/activity/<activity name>.rs`.

## Rust Style

- Do not add `unwrap()`, `expect()`, `panic!`, `unreachable!`, unchecked
  indexing, unchecked conversions, or other potentially panicking operations
  to request, transaction, proof, persistence, network, or external-state
  paths. Return a typed error or handle the missing/invalid state explicitly.
  Prefer assertions over panic-based extraction in tests. Process startup
  should also return an actionable error instead of panicking unless Ed
  explicitly approves an intentional abort.
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
- For API handlers, extract claims and other boundary context once, destructure
  proto requests immediately, convert primitive proto values into typed domain
  values, and pass only those values onward. Keep validation, domain logic, and
  response mapping easy to follow. Extract helpers only when readability
  actually improves.
- Construct required dependencies as concrete fields during startup. Do not
  store a client, repository, key set, parameter store, or Redis pool in
  `Option` when the served endpoint cannot operate safely without it.
- Use `Option` only for genuine domain absence. Do not use it to represent
  invalid input, failed decoding, a required joined relation, a disabled
  lifecycle record, or one variant of an enum-shaped payload.
- Use Rust or proto enums for closed sets such as flow, status, credential
  kind, provider kind, network, and subscription tier. Keep strings only for
  intentionally extensible identifiers.
- When a proto enum already owns a shared protocol concept, use that generated
  enum directly across participating Rust crates instead of defining parallel
  enums and conversion helpers.
- Define repeated protocol paths, claim names, environment keys, namespaces,
  algorithms, and fixed TTLs as constants at their owning boundary. Do not turn
  typed struct fields into string constants; eliminate string-key access by
  deserializing into the struct instead.
- Keep adjacent one-line validation calls in the main control flow. Do not add a
  helper used once merely to hide a comparison or forward its result.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.
- Keep dynamic log values in structured fields and log messages
  low-cardinality. Use `info` for normal lifecycle events, `warn` for degraded
  but recoverable behavior, and `error` for failed operations.
- Log a failed operation at the boundary that owns it, usually inline in
  `map_err` when the closure only records context and returns the same error.
  Do not create generic `log_*_failure(status)` helpers that merely rename one
  logging call.
- Do not extract helpers that only rename, clone, trim, borrow, convert, or map
  a small enum to a string. Keep the operation inline at its consumer. Add a
  helper or inherent method only when reuse is real or the mapping is domain
  behavior that deserves one authoritative boundary.
- Prefer descriptive names over dense acronyms.
- Fix Clippy findings at their source. Add a narrowly scoped `allow` only when
  the lint is demonstrably inapplicable and record the reason; do not normalize
  crate-wide or handler-wide suppression of `result_large_err`,
  `too_many_arguments`, `large_enum_variant`, or similar design signals.

## Tests

- Keep production Rust files free of inline `#[cfg(test)] mod tests` blocks.
  Put crate tests under that crate's `tests/` directory and group them by the
  concrete feature or endpoint they exercise.
- Service-local unit tests must not require a real database, Redis instance,
  RPC node, provider, Tilt stack, pre-running TCP listener, or another service.
  An isolated Redis-compatible mock is allowed when the test starts it on an
  ephemeral address, owns teardown, requires no shared infrastructure, and
  fails instead of skipping when setup fails. Put other replaceable side
  effects behind focused consumer-owned traits and use `mockall` to test the
  service behavior.
- Move tests that intentionally exercise real infrastructure, generated gRPC
  clients, or complete multi-service flows to a workspace-level integration or
  end-to-end test area outside `services/`. Do not label those tests unit tests
  or make a service crate's normal test command depend on them.

## Lifecycle And Accounting

- Keep top-level phases visible: validation, idempotency, preparation,
  irreversible external call, accepted state, confirmation, accounting,
  persistence, and response mapping.
- Make the irreversible boundary explicit. A later nested error must not reset
  state in a way that permits the same external effect to run again.
- Represent security workflows with concrete state variants. Keep immutable
  authorization context separate from the smallest stage payload, give each
  transition a typed outcome, and preserve the exact response needed for
  same-request idempotency.
- Atomically reserve or compare-and-swap one-time authorization before an
  irreversible effect. The same immutable attempt may resume after a transient
  failure; a different message, proof key, redirect, identity, or security
  configuration must be rejected.
- Enforce authorization and consent deadlines in the transition itself using
  server-owned time. Do not rely on a frontend timer or extend an earlier
  authorization window by moving data into a later cache stage.
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
- Do not put Redis behind a model, `Store`, `Repository`, resolver, or
  persistence trait. The model/repository abstraction is for durable Postgres
  state. Keep Redis operations as a small number of feature-local functions
  such as `cache_quote` and `get_quote`; pass the concrete pool, acquire the
  connection there, and issue the commands visibly.
- When `rediss://` support is required, enable the underlying `redis` crate's Tokio/Rustls transport feature, but continue to manage connections and issue commands through `deadpool_redis`.
- Use an atomic Redis script or transaction for security-sensitive state
  transitions and deadlines. Compare the complete expected typed state,
  advance once, and return a distinct conflict/retry outcome; do not split
  authorization comparison, reservation, and failure charging across
  independently racing commands.

## Validation

- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo's standard formatter.
- Run focused tests for touched behavior.
- Run `cargo clippy --all-targets` for service changes when practical.
- Report any checks that could not be run and why.
