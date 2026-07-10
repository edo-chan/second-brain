# Personal Agent Guidelines for Ed

These are my baseline preferences across repos. Repo-level `AGENTS.md` files override this when they are more specific.

## Second Brain

- The canonical second-brain repository is `/Users/edchan/Documents/Playground/Dev/second-brain`.
- Use its `README.md` as the current index of reusable agent skills.
- Before non-trivial work in Ed's repositories, identify any relevant skill under `second-brain/skills/` and read its `SKILL.md` completely before acting. Load only the skills relevant to the task.
- Use `ed-git-workflow` for branch, PR, merge, and release work.
- Use `ed-rust-service-style` for Rust services, workflows, handlers, modules, and tests.
- Use `ed-frontend-review-style` for React, Next.js App Router, and TypeScript implementation and pull-request reviews.
- Use `ed-service-boundaries` for vendor clients, public APIs, proto/gRPC, webhooks, auth boundaries, response parsing, and sensitive logging.
- Use `ed-schema-database` for schema design, migrations, database state, and persistence boundaries.
- Use `ed-infrastructure-rollout` for secrets, Terraform, cloud configuration, drift, and rollout work.
- Use `evm-swig-contract-safety` for EVM Swig contract changes and reviews.
- Treat `second-brain/AGENTS.md` as the tracked snapshot of this global file. When changing global guidance, update that snapshot through the second-brain repository's branch, pull-request, and merge workflow.

## Git Workflow

- Always make changes on a feature branch, open a pull request, and merge the pull request. Do not push commits directly to `main`.
- When making or cutting a release, also publish the release on GitHub.

## Code Organization

- Do not put business logic in `mod.rs`; use `mod.rs` only for module wiring and exports.
- Keep types next to the consumer that exposes or uses them. Avoid giant shared type files, vendor type dumps, and moving types into separate files before there is a real reuse boundary.
- Keep vendor property/lookup types with the feature or endpoint that exposes them; avoid giant shared vendor type files.
- Treat each vendor endpoint as a distinct contract. Vendor libraries must expose explicit endpoint-specific methods that return clear concrete response structs.
- Use `Option` only for fields the vendor contract truly marks optional. Model required fields as required concrete fields; do not pass uncertainty through with `Option` or `serde(default)` merely to accept malformed responses.
- Distinguish missing data from unknown values. Keep extensible vendor identifiers as required strings when new codes are valid, and reject missing identifiers instead of collapsing them to `UNKNOWN` or `UNSPECIFIED`.
- Do not expose generic vendor request/response wrappers, generic JSON methods such as `get_json<T>`, `serde_json::Value`, or raw upstream response bodies to consuming services.
- Keep HTTP, authentication, retries, response-body handling, and deserialization inside the vendor library. A raw body may exist only inside a private transport helper and must be parsed before the public endpoint method returns.
- Let consuming services perform only the explicit mapping from typed vendor structs into domain or proto types.
- Reject responses that omit required upstream data with a structured boundary error instead of returning partial output. Use `FAILED_PRECONDITION` at a gRPC boundary when the missing field makes the requested result unusable.
- Return authoritative vendor identifiers and let downstream presentation own display labels. Do not synthesize provider or product names from codes unless a distinct typed vendor metadata endpoint supplies the canonical name.
- Test each endpoint's concrete response deserialization inside the vendor library, including documented successes, missing required fields, and typed errors.
- For Rust consuming-service tests, use `mockall` to generate mocks from the concrete typed vendor client. Do not introduce a trait or hand-written mock solely for testing; return typed successes or errors from the generated mock and assert downstream status and domain mapping.
- Do not use an HTTP mock server to claim consuming-service logic coverage. It primarily proves that the configured fixture returns what was configured rather than isolating application behavior.
- Treat any new or extended violation of these vendor-client boundary rules as blocking for approval. Request changes even when functional behavior and tests otherwise pass.

## Sensitive Logging

- Do not log sensitive vendor payloads, launch URLs, KYC/PII fields, upstream response bodies, API keys, signatures, or tokens.
- Prefer logging stable non-sensitive fields such as status code, error class, request id, organization id, and internal ids over relying on broad redaction helpers.

## Proto / gRPC Service Organization

- Keep proto files to one service each. If a new independently routed service is needed, create a separate proto file and wire descriptor generation, Rust codegen, gateway routing, and client type generation for that file.
- gRPC services with names prefixed by `Api` are public API-key authenticated services. Register them with the repo's API-key auth interceptor at the service boundary, or use the existing centralized API-key auth pattern before handler logic runs.
- Webhook gRPC services must have an explicit verification boundary, such as a webhook signature interceptor or gateway verifier, before trusted handler logic runs.

## Workflow Code Organization

- Organize workflow code under `Workflow/<workflow name>/`.
- Put the actual workflow definition in `Workflow/<workflow name>/definition.rs`.
- Put the main activity implementation in `Workflow/<workflow name>/activity/<activity name>/definition.rs`.
- Do not use flat activity files like `Workflow/<workflow name>/activity/<activity name>.rs`.
- Put any activity-specific files under `Workflow/<workflow name>/activity/<activity name>/files/`.

## Rust Coding Style

- Keep functions concise and single-purpose.
- Prefer small, explicit functions over broad abstractions. Match the surrounding module style before introducing new traits, builders, or helper layers.
- Do not add wrapper helpers that only forward a call or rename, clone, trim, borrow, or convert a value. Keep trivial transformations inline, or fix the source type so the conversion disappears.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.
- Use typed errors and structured error responses where the service already has them. Avoid stringly typed error plumbing unless the existing code does it.
- Keep async boundaries clear. Do not hide network, database, or signing work inside helpers that look pure.
- For API handlers, keep validation, domain logic, and response mapping easy to follow. Extract helpers when the handler stops being readable.
- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo’s standard formatter.
- Run the narrow relevant checks before committing: usually `cargo test` for touched behavior and `cargo clippy --all-targets` for service changes.

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
- Preserve existing data when changing columns, enum values, constraints, or indexes. If a migration is destructive, call that out before applying it.
- Avoid duplicating data that can be derived reliably, especially request fields like token accounts, token programs, or wallet-derived addresses.
- When adding request or table fields, verify whether the value is user input, derived state, cached state, or source-of-truth state.
- For production or staging data changes, check current state and drift first, then apply the smallest clear migration.

## Infrastructure

- Treat pasted credentials, API keys, private keys, and session tokens as sensitive unless explicitly marked throwaway.
- Do not persist private keys or secrets in source. Public keys and non-secret config can live in parameter/config stores when appropriate.
- For Terraform, inspect plan/drift before applying unless I explicitly ask for a direct apply.
- Keep infrastructure changes scoped by environment. If a resource is per-env, name and store it per-env.
- Prefer AWS SSM Parameter Store for deployed configuration. Do not add local environment-variable overrides when the expected source is Param Store.
- Prefer deleting deprecated resources once traffic and dependencies are confirmed gone, especially old EKS, ClickHouse, indexer, and unused Helm resources.
- For AWS signing/enclave work, keep private material owned by KMS/enclave flows where possible; store only public keys or ciphertext blobs outside the signer boundary.
- When CI, branch protection, credentials, or cloud state blocks a rollout, state the exact blocker and the next action.
