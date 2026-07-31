# Personal Agent Guidelines for Ed

These are my baseline preferences across repos. Repo-level `AGENTS.md` files override this when they are more specific.

## Second Brain

- The canonical second-brain repository is `/Users/edchan/Documents/Playground/Dev/second-brain`.
- Use its `README.md` as the current index of reusable agent skills.
- Before non-trivial work in Ed's repositories, identify any relevant skill under `second-brain/skills/` and read its `SKILL.md` completely before acting. Load only the skills relevant to the task.
- Use `ed-general-coding` for general implementation, refactoring, debugging, testing, frontend work, service boundaries, schemas, databases, and code review.
- Use `ed-documentation` for product and API documentation, guides, PRDs, RFCs, architecture proposals, and design-document reviews.
- Use `ed-rust-coding` for Rust crates, services, workflows, handlers, modules, and tests.
- Use `ed-solidity-coding` for Solidity and EVM contract implementation and review, including EVM Swig safety and parity.
- Use `ed-solana-coding` for Solana programs, Swig state, authorities, permissions, parsers, SignV2, recovery, SDKs, and pull-request work.
- Use `ed-ci-infrastructure` for branches, commits, pull requests, merges, releases, CI, secrets, Terraform, cloud configuration, deployment, drift, and rollout work.
- Treat `second-brain/AGENTS.md` as the tracked snapshot of this global file. When changing global guidance, update that snapshot through the second-brain repository's branch, pull-request, and merge workflow.

## Git Workflow

- Always make changes on feature branches and open pull requests. Do not push commits directly to `main`.
- For multi-part work, default to a linear stack of small, focused PRs. Base
  each dependent PR on its immediate predecessor and keep every PR readable,
  buildable, and semantically honest.
- Do not merge any PR unless I explicitly authorize merges in the current
  session. An implementation request, green checks, merge readiness, or
  approval from a prior session is not merge authorization.
- PRs in the canonical second-brain repository are the exception: they may be
  merged without separate user approval once validation and repository gates
  pass. Do not bypass branch protection.
- Treat merge authorization as scoped to the named PR, stack, or session-wide
  permission. Without it, leave the PR or stack open and report status.
- When I authorize merging a stack, merge base-to-tip and restack or retarget
  the remaining PRs as needed.
- When making or cutting a release, also publish the release on GitHub.

## Code Organization

- Do not put business logic in `mod.rs`; use `mod.rs` only for module wiring and exports.
- Keep types next to the consumer that exposes or uses them. Avoid giant shared type files, vendor type dumps, and moving types into separate files before there is a real reuse boundary.
- Keep vendor property/lookup types with the feature or endpoint that exposes them; avoid giant shared vendor type files.
- Treat each vendor endpoint as a distinct contract. Vendor libraries must expose explicit endpoint-specific methods that return clear concrete response structs.
- Name each concrete third-party adapter `{Vendor}Connector`, such as
  `MeldConnector`. Do not use a generic `Client`, `Service`, or `Manager` name
  for a vendor integration.
- Review request contracts as strictly as response contracts. Identify caller-supplied, server-derived, and vendor-derived fields. For signed payloads, distinguish who constructs, funds, and signs; do not mutate a signed message unless every affected signer can sign the result.
- Treat proof-bound transactions as an end-to-end invariant: the proof commits
  to a client-owned key, that key signs the complete canonical message, the
  sponsor validates exact shape before adding only its signature, generated
  artifacts share one source, and replay state rejects changed or reused
  authorization.
- Use `Option` only for fields the vendor contract truly marks optional. Model required fields as required concrete fields; do not pass uncertainty through with `Option` or `serde(default)` merely to accept malformed responses.
- For required-but-nullable vendor fields, accept explicit `null` and reject omission. A plain `Option<T>` does not preserve that distinction.
- Distinguish missing data from unknown values. Keep extensible vendor identifiers as required strings when new codes are valid, and reject missing identifiers instead of collapsing them to `UNKNOWN` or `UNSPECIFIED`.
- Do not expose generic vendor request/response wrappers, generic JSON methods such as `get_json<T>`, `serde_json::Value`, or raw upstream response bodies to consuming services.
- Do not create a new vendor client, endpoint-method layer, trait, or other abstraction solely to eliminate generic JSON. When the current code does not otherwise warrant that layer, deserialize into concrete local structs at the existing ownership boundary.
- When a request selects a vendor environment or credential, keep both out of
  service initialization and long-lived client state. Validate the environment
  in the RPC, load and decrypt the scoped credential there, and pass the
  borrowed `SecretBox` to each typed endpoint call.
- Do not hide repository lookup, lifecycle checks, secret decryption, client
  construction, and one vendor call behind a resolver, runtime context,
  factory, or forwarding helper. Prefer visible local duplication.
- Do not add a client-config object when construction only selects one
  validated environment plus fixed library defaults.
- Do not hide typed endpoint requests behind `get_body`, `post_body`, a string
  HTTP method, an optional body, or a generic request function. Each endpoint
  must visibly build and send its concrete request, check status, read the
  body, and parse its concrete response.
- Keep HTTP, authentication, response-body handling, and deserialization inside the vendor library. A raw body may exist only inside the concrete typed endpoint method and must be parsed before that method returns.
- Do not retry at a generic HTTP transport layer. Retry only in the owning
  endpoint or workflow after proving idempotency and replay behavior. POST
  requests are not retryable by default.
- Keep HTTP client types and raw RPC messages private. Public errors should expose stable error classes and safe context such as status or request ids, not transport implementation types or response bodies.
- Let consuming services perform only the explicit mapping from typed vendor structs into domain or proto types.
- Reject responses that omit required upstream data with a structured boundary error instead of returning partial output. Use `FAILED_PRECONDITION` at a gRPC boundary when the missing field makes the requested result unusable.
- Model only upstream fields that consumers use or the boundary must validate. Validate response cardinality and correlate returned identifiers to requested identifiers before accepting a response.
- Return authoritative vendor identifiers and let downstream presentation own display labels. Do not synthesize provider or product names from codes unless a distinct typed vendor metadata endpoint supplies the canonical name.
- Test each endpoint's concrete response deserialization inside the vendor library, including documented successes, missing required fields, and typed errors.
- For Rust consuming-service tests, use `mockall` at a focused typed vendor boundary. A production trait is justified when the consumer needs a replaceable dependency such as `Arc<dyn VendorClient>`; concrete-struct mocks are different types and otherwise require `mockall_double`, test-only import rewriting, or generics. Do not reject the trait merely because its main alternate implementation is a test mock. Keep the trait consumer-focused, accept local `mock!` signature repetition for an external trait when it is the simplest option, and return typed successes or errors from the mock while asserting downstream status and domain mapping.
- Do not use an HTTP mock server to claim consuming-service logic coverage. It primarily proves that the configured fixture returns what was configured rather than isolating application behavior.
- Treat any new or extended violation of these vendor-client boundary rules as blocking for approval. Request changes even when functional behavior and tests otherwise pass.

## Sensitive Logging

- Do not log sensitive vendor payloads, launch URLs, KYC/PII fields, upstream response bodies, API keys, signatures, or tokens.
- Sanitize gateway access paths that can contain query credentials, and treat
  browser, prover, and circuit debug output as logs. Never emit private
  witnesses, salts, stable identity claims, authorization codes, or proof
  inputs.
- Prefer logging stable non-sensitive fields such as status code, error class, request id, organization id, and internal ids over relying on broad redaction helpers.

## Proto / gRPC Service Organization

- Keep proto files to one service each. If a new independently routed service is needed, create a separate proto file and wire descriptor generation, Rust codegen, gateway routing, and client type generation for that file.
- gRPC services with names prefixed by `Api` are public API-key authenticated services. Register them with the repo's API-key auth interceptor at the service boundary, or use the existing centralized API-key auth pattern before handler logic runs.
- Webhook gRPC services must have an explicit verification boundary, such as a webhook signature interceptor or gateway verifier, before trusted handler logic runs.
- Each authenticated caller uses only its own service secret and surface.
  Admin applications do not possess Developer or Api credentials or forge
  their headers; shared behavior belongs below distinct authenticated handlers.

## Workflow Code Organization

- Organize workflow code under `Workflow/<workflow name>/`.
- Put the actual workflow definition in `Workflow/<workflow name>/definition.rs`.
- Put the main activity implementation in `Workflow/<workflow name>/activity/<activity name>/definition.rs`.
- Do not use flat activity files like `Workflow/<workflow name>/activity/<activity name>.rs`.
- Put any activity-specific files under `Workflow/<workflow name>/activity/<activity name>/files/`.

## Rust Coding Style

- Keep every function concise, focused, and single-purpose. When a function becomes difficult to scan or mixes phases, split it into concrete focused functions before adding more logic.
- Prefer small, explicit functions over broad abstractions. Match the surrounding module style before introducing new traits, builders, or helper layers.
- Do not add wrapper helpers that only forward a call or rename, clone, trim, borrow, or convert a value. Keep trivial transformations inline, or fix the source type so the conversion disappears.
- Prefer short local duplication over a resolver, runtime context, factory,
  store, or helper whose only value is concealing repository access, secret
  decryption, client construction, or an external call.
- Log a failed operation at the boundary that owns it, usually inline in `map_err` when the closure only records context and returns the same error. Do not create generic `log_*_failure(status)` helpers that merely rename one logging call.
- Do not write generic Rust code unless I explicitly approve it. This includes
  generic functions, structs, enums, type aliases, traits, and explicit lifetime
  parameters. Prefer concrete types and elided lifetimes.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.
- Use typed errors and structured error responses where the service already has them. Avoid stringly typed error plumbing unless the existing code does it.
- Keep async boundaries clear. Do not hide network, database, or signing work inside helpers that look pure.
- For API handlers, keep validation, domain logic, and response mapping easy to follow. Extract helpers when the handler stops being readable.
- Keep lifecycle phases and irreversible external-call boundaries visible. After external acceptance, persist accepted state or its identifier before later work, and never release idempotency in a way that permits the effect to repeat.
- Enforce consent and proof deadlines at the server transition, reserve
  one-time verification atomically for one immutable attempt, and make
  completion idempotent for that attempt without reopening it for another
  identity, redirect, proof key, or message.
- Decide whether the caller, vendor client, workflow, or platform owns retries. Do not add implicit retries at a layer that cannot reason about idempotency.
- Record exactly one API-request event per invocation, including errors and replays. Emit domain or billing events only for newly completed work.
- Do not introduce production traits merely because a test framework exists. A trait used by production code as a replaceable dependency boundary, such as `Arc<dyn Client>`, is legitimate even when Mockall supplies the only current alternate implementation; thin delegation to the concrete client is boundary wiring.
- When an API layer needs unit-test substitution, define a focused
  consumer-owned trait around only the connector's typed operations and inject
  it into the API service. Do not expose HTTP verbs, raw bodies, generic
  requests, or connector construction through that trait.
- Keep production Rust files free of inline `#[cfg(test)] mod tests` blocks.
  Put crate tests under the crate's `tests/` directory.
- Derive billing and spend from authoritative confirmed pre/post state, not predicted fee arithmetic.
- For batch or bundle behavior, include a multi-item success test that proves order, cardinality, and per-item mapping.
- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo’s standard formatter.
- Run the narrow relevant checks before committing: usually `cargo test` for touched behavior and `cargo clippy --all-targets` for service changes.

## Redis Boundaries

- Use the concrete `deadpool_redis` pool and keep connection acquisition and
  commands visible at the feature boundary.
- Do not put Redis behind a model, `Store`, `Repository`, resolver, or
  persistence trait. Durable Postgres state owns the model/repository layer.
  Keep Redis access in a small number of feature-local functions such as
  `cache_quote` and `get_quote`.

## EVM Swig Contract Requirements

`evm/` contract work is security-critical wallet code. Do not treat it as scaffold code unless I explicitly request a shape-only draft, and even then unsafe asset movement must be disabled or denied by default.

### Solana Parity Is Required

EVM Swig must be treated as a port of Solana Swig unless a Linear ticket or design doc explicitly records a divergence.

Before changing `evm/src/SwigConfig` or `evm/src/SwigVault`, inspect the relevant Solana Swig source:

- `../swig-wallet/state/src/action/mod.rs`
- the touched `../swig-wallet/state/src/action/*.rs` files
- `../swig-wallet/state/src/authority/*.rs`
- `../swig-wallet/program/src/actions/sign_v2.rs`
- matching Solana tests under `../swig-wallet/program/tests/`

For every touched permission or authority, include a parity note in the PR body or commit message:

- Solana source file
- EVM source file
- enum/discriminant value
- action data length
- repeatability
- match key or destination key
- replay/nonce behavior
- enforcement status
- any intentional divergence with ticket or doc link

If Solana source, existing EVM review comments, and the design doc disagree, stop and resolve the product decision before implementing. Do not silently choose one.

When checking Solana parity, distinguish stored action layout, creation payload layout, runtime-populated fields, marker permission behavior, and review-approved intentional divergence. If these disagree, do not call it a bug or a fix. Stop and record the intended parity target.

### Blocking Contract Invariants

A PR is not ready unless these invariants are encoded in tests:

- Root creation cannot produce a bricked Swig: root must have `ManageAuthority` or `All`.
- `AllButManageAuthority` must not grant `ManageAuthority`, `Upgrade`, or `SubAccount`.
- Marker permissions must use the exact accepted Solana layout. Any layout change requires an explicit parity note.
- Unsupported authority, session, and program authority variants must be rejected at validation, not partially accepted.
- k1, r1, and ed25519 must work consistently on every management and signing path where they are claimed to be supported.
- Direct-caller auth and signature auth must be separate code paths. Empty auth bytes must never be reused in ERC-4337/UserOp validation.
- Every signature auth path must have replay protection. Nonce/counter state must be consumed before any external call, or the path must be `nonReentrant`.
- r1 verifier/precompile address must be supplied by factory or chain config. Do not hardcode chain-specific verifier addresses in production contracts.
- Verifier calls must reject missing code, invalid address, revert, false/zero return, malformed return length, wrong pubkey length, wrong signature length, and wrong signer.
- Vault execution must route through Swig policy. Subaccount executors must not call arbitrary vault execution directly unless vault-local policy limits are implemented and tested.
- ETH semantics must be explicit. Choose exactly one: vault-held spend with `msg.value == 0`, or caller-funded forwarding with `msg.value == value`.
- Generic execution must not be able to call config, vault, or proxy upgrade selectors unless the role has explicit `Upgrade`.
- Direct proxy/config initialization must not allow arbitrary nonzero vault addresses if factory-paired deployment is required.
- Asset-moving paths must deny by default unless `All`, `AllButManageAuthority`, or a matching scoped permission is present and consumed.

### Auth Path Matrix

For each auth entrypoint, document and test:

- authority type: k1, r1, ed25519, session, or program
- auth mode: direct caller, signature, verifier, or precompile
- empty auth behavior
- nonce or counter source
- exact point nonce/counter is consumed
- external calls after auth
- ERC-4337/UserOp safety
- replay test name

If `authorization.length == 0` is accepted anywhere, add a test proving it cannot be used through ERC-4337/UserOp validation or any contract-caller path unless explicitly intended.

### Verifier Failure Matrix

Verifier-backed auth must test:

- missing verifier code
- invalid verifier address
- verifier revert
- verifier false or zero return
- malformed return length
- wrong pubkey length
- wrong signature length
- wrong signer
- bad digest or message

r1 must test chain-configured verifier behavior. Hardcoded precompile paths are local-test only.

### External Call And Reentrancy Gate

Any authorized function that makes an external call must include:

- nonce/counter consumption before the call, or `nonReentrant`
- a reentrancy regression test
- a test that replaying the same authorization fails even if the first call reenters

### Generic Execution Upgrade Denylist

Any generic execution feature must include negative tests showing it cannot call:

- config upgrade selectors
- vault upgrade selectors
- proxy upgrade selectors
- role-management selectors unless the role has explicit `ManageAuthority`
- recovery or close selectors unless the role has the explicit permission

### SignV2 Requirements

`signV2` must follow the Solana shape:

1. role exists
2. authority authenticates
3. target/program permission is checked before execution when scoped
4. execution happens through the Swig-controlled vault
5. native/token deltas are measured and charged to matching limits
6. unmatched spend reverts

A shape-only `signV2` PR may omit full permission mapping only when:

- the TODO says the missing enforcement is intentional
- a ticket ID is included
- unsafe fund movement is denied or limited to explicitly broad permissions
- tests prove restricted roles cannot move assets through the gap

### Required Tests For EVM Contract PRs

Every EVM contract PR must include negative tests for the invariant it touches. Happy-path tests are insufficient.

Required categories when relevant:

- missing role
- wrong authority
- wrong auth type
- malformed auth payload
- replayed auth or nonce reuse
- verifier false/revert/bad return length
- unauthorized native transfer
- unauthorized ERC-20 transfer
- wrong destination
- overspend
- unauthorized subaccount execution
- generic execution attempting upgrade selector
- direct proxy/factory bypass
- `msg.value` mismatch
- reentrancy around external calls
- ERC-4337/UserOp empty-auth misuse
- bad digest or message for verifier-backed auth

Use real k1/r1/ed25519 verification in e2e claims. Mocks are allowed only for unit-level failure injection, and must not be used to claim real signer compatibility.

### Agent Gate

Do not open or re-request review on an EVM contract PR until:

- `forge fmt --root evm --check` passes
- `forge test --root evm` passes
- `git diff --check` passes
- the parity note exists
- the negative tests cover the changed invariant
- all TODOs around disabled enforcement include a ticket and a deny-by-default test

Include this self-review table in the PR body before opening or re-requesting review:

| Area | Checked | Test |
| --- | --- | --- |
| Permission layout parity | yes/no | test name |
| Repeatability parity | yes/no | test name |
| Direct auth safety | yes/no | test name |
| Signature replay | yes/no | test name |
| Verifier failures | yes/no | test name |
| External-call reentrancy | yes/no | test name |
| Generic exec upgrade blocking | yes/no | test name |
| Value semantics | yes/no | test name |
| Parity target conflicts resolved | yes/no | note/ticket |

## Schema / Database

- Prefer migrations over direct schema pushes. Do not use `db:push` in repos where migrations are expected.
- Use Tilt as the local source of truth for services such as Postgres.
- Apply schema changes through the repo's migration script.
- If a migration file is modified after being applied locally, undo it first, then run the migration script again.
- Do not add indexes unless explicitly requested.
- Do not add schema or migration comments.
- Define enum semantics in proto. Store enum values in the database as `SMALLINT`, use `i16` at Rust persistence boundaries, and validate/convert from proto enums before storing.
- Store addresses as text.
- Use Prost well-known types where applicable.
- Schema changes should include the application code, migration file, and focused tests in the same PR when practical.
- Name repository writes for the persistence operation, such as `create`,
  `update_*`, or `set_*`, not for one initial lifecycle value. Pass lifecycle
  status as data; do not encode it in a name such as `create_pending`.
- Preserve existing data when changing columns, enum values, constraints, or indexes. If a migration is destructive, call that out before applying it.
- Avoid duplicating data that can be derived reliably, especially request fields like token accounts, token programs, or wallet-derived addresses.
- When adding request or table fields, verify whether the value is user input, derived state, cached state, or source-of-truth state.
- Identify each row's granularity: API request, domain item, billable item, confirmation, or transport-level group. Persist a transport group only when it has its own lifecycle, source-of-truth role, or concrete query consumer.
- Keep API-request telemetry separate from domain and billing records so failures and replays do not create duplicate billable work.
- Make authentication attempt limits atomic and security-configuration
  cardinality explicit. Do not split comparison from failure charging or use
  unordered `LIMIT 1` to choose among multiple active credentials.
- For production or staging data changes, check current state and drift first, then apply the smallest clear migration.

## Infrastructure

- Treat pasted credentials, API keys, private keys, and session tokens as sensitive unless explicitly marked throwaway.
- Do not persist private keys or secrets in source.
- Give each deployed caller only the credential for its own authenticated
  service surface. Removing a Vercel environment variable affects future
  deployments; replace the existing deployment, and rotate the credential when
  immediate revocation from prior immutable deployment snapshots is required.
- Classify configuration as a credential, environment-specific value, customer-specific value, or stable public protocol constant. Store public keys and environment- or customer-specific runtime configuration in SSM.
- Stable canonical public endpoints and paths may live in code when they are not credential-bearing, region-selected, customer-specific, or environment-varying.
- Before adding a new endpoint parameter, check whether an existing credentialed provider endpoint supports the capability and verify it against the live provider contract.
- For Terraform, inspect plan/drift before applying unless I explicitly ask for a direct apply.
- Confirm each repository's environment semantics before changing infrastructure or SSM values. In `swig-dev-portal`, `dev` means the local Docker/Surfpool environment, not a shared cloud staging environment; its service URLs must resolve from local containers and must not point at cloud-only resources such as ElastiCache.
- Keep infrastructure changes scoped by environment. If a resource is per-env, name and store it per-env.
- Provision every new environment-scoped SSM parameter with Terraform before attempting to persist its real value.
- After Terraform creates the parameter, persist the real value in SSM and verify that every target environment can resolve it before deploying code that requires it.
- Treat missing, placeholder, sentinel, or unreadable SSM values as rollout blockers. Never deploy consuming code before the required value is persisted and verified.
- Use AWS SSM Parameter Store as the sole source for environment- and customer-specific service runtime configuration in every environment, including local development.
- Treat declared SSM parameters as required. Do not make them optional or add environment-variable, hardcoded, default-value, or local fallback paths when a parameter is missing.
- Configure local development to authenticate to AWS and read its environment-scoped configuration directly from SSM.
- Prefer deleting deprecated resources once traffic and dependencies are confirmed gone, especially old EKS, ClickHouse, indexer, and unused Helm resources.
- For AWS signing/enclave work, keep private material owned by KMS/enclave flows where possible; store only public keys or ciphertext blobs outside the signer boundary.
- When CI, branch protection, credentials, or cloud state blocks a rollout, state the exact blocker and the next action.
