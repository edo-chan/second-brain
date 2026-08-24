---
name: ed-solana-coding
description: Solana implementation and review standards for Ed's repositories, including strict Swig security and compatibility gates. Use when implementing or reviewing Solana programs, swig-wallet state, actions, authorities, instructions, SignV2, recovery, sessions, ProgramExec, compact parsing, account reallocations, CPI, compute units, IDL/interface/Rust SDK surfaces, or Solana PRs.
---

# Ed Solana Coding

Treat Solana Swig as security-critical wallet code. Preserve its stored state, wire contracts, public builders, and client compatibility while making the smallest explicit change that satisfies the requested behavior.

Read [references/source-map.md](references/source-map.md) when orienting an unfamiliar or cross-crate change. Read [references/tracy-review-patterns.md](references/tracy-review-patterns.md) before implementing or reviewing authority, permission, parser, account-layout, recovery, close, or SignV2 changes.

## Trace The Entire Contract

Before editing, trace the affected behavior through every layer that consumes it:

1. stored state in `state/`
2. program dispatch, account definitions, and handler logic in `program/`
3. instruction wire format and compact parsing in `instructions/`
4. public constructors in `interface/`
5. ergonomic entrypoints in `rust-sdk/`
6. `program/idl.json`, documentation, integration tests, and downstream SDK fixtures

Classify each field separately as stored layout, creation payload, runtime-populated state, or client-only metadata. Do not infer that identical names imply identical layout or semantics.

If source, design documentation, accepted review feedback, and client behavior disagree, stop and record the product decision before implementing. Do not silently pick one source of truth.

## Account And Instruction Boundaries

- Check account-slice length before every index or unchecked load.
- Validate signer, writable, owner, executable program, PDA seeds and bump, and key relationships at the boundary where each property becomes trusted.
- For a changed instruction, record one account-contract row per named,
  authority-context, variadic, CPI, and introspected account: index or role,
  expected key or PDA, signer, writable, program owner, executable state, data
  shape, alias rules, validation boundary, and negative test. Complete it before
  reducing an `AccountInfo` to only its key or passing it into domain logic.
- Reject unsafe aliasing, including a Swig config PDA, wallet-address PDA, subaccount, or other Swig-owned account supplied as an external destination or authority when the operation requires an independent account.
- Keep instruction definitions, processor indexes, `program/idl.json`, interface account metas, and SDK builders identical.
- Preserve existing account order. Append optional accounts when compatibility permits; do not reorder existing accounts without an explicit breaking-change decision and client migration.
- Mark only mutated accounts writable. Avoid unnecessary transaction write locks.
- Authenticate before returning sensitive state-dependent validation errors, but complete all validation before reallocating, mutating state, or invoking another program.

### Default To Shank Instruction Contexts

- For Solana program instruction enums, default to
  `#[derive(ShankInstruction, ShankContext)]` and ordered `#[account(...)]`
  declarations. Keep an established non-Shank ABI generator only when mixing
  generators would create a second source of truth or require an explicit
  migration.
- Model a conditionally used account with the Shank `optional` account marker
  while preserving its fixed account index. The default builder representation
  for `None` is a read-only program-ID account meta; a real `Some` account keeps
  its required signer and writable flags. Never shorten the account list or
  shift later indexes unless the active parser and every client deliberately
  implement that wire contract.
- Treat the generated `Option<&AccountInfo>` as untrusted input. When stored
  state requires the account, require `Some` and validate its exact key, owner,
  signer/writable flags, and non-aliasing rules. When stored state does not
  require it, handle `None` with the explicit protocol fallback and reject an
  unrelated `Some`. Accept a legacy explicit fallback account only when its key
  matches that fallback exactly.
- Verify the pinned Shank implementation before relying on optional-account
  behavior. Swig's pinned Shank context uses the program ID as a fixed-position
  sentinel. Do not enable `legacy_optional_accounts_strategy` or assume
  variable-length omission without an explicit compatibility decision.
- Regenerate the IDL and update interface/SDK builders and tests in the same
  change. Assert the sentinel account meta and at least one later account index,
  then exercise both `None` and `Some` paths against a rebuilt SBF artifact.

## Atomic Batch And Migration Operations

For an instruction that accepts a collection of accounts, assets, or state
entries, define whether success means all entries were handled or whether
best-effort processing is an explicit public contract. Default security-critical
wallet migrations to all-or-error behavior.

- Use a complete preflight pass before the first lamport, data, counter, or
  external-program mutation. Validate every supplied entry's program ownership,
  versioned layout, initialized state, asset identity, authority, destination,
  and required account relationships.
- Build a validation ledger for every condition that can reject or skip an
  entry. Include each `continue`, `break`, fallible read, and CPI after the first
  mutation, and map every malformed case to a hard error and negative test.
- Separate preflight from execution when that makes the all-or-error contract
  explicit. After execution begins, propagate every failure so Solana rollback
  restores prior state; never catch or silently skip malformed input.
- A zero-balance or otherwise empty entry may skip its CPI only after the entry
  has passed the same structural and semantic validation as a non-empty entry.

## Close Drain And Refund Flows

For every close, drain, reclaim, or tombstone path, build a funds-flow ledger
before implementing. Partition each source balance into operational SOL, rent
reserve, retained tombstone rent, and any other protocol-owned amount; bind each
partition to its authoritative destination and fallback.

- Record each source's total balance, every partition and destination, the
  validation that precedes mutation, and the balance test. Calculate rent for
  each source from that account's own data length.
- Trace the immutable rent-claimer contract through every close consumer and
  use the strict tail decoder before mutation. Do not infer that all lamports in
  one account have the same owner or destination.
- Validate configured, unset, missing, wrong, and source-alias destinations
  before changing counters, data, account size, or lamports.
- When a stacked PR establishes a funds-routing policy, apply and test that same
  policy in every dependent close path rather than rediscovering it per PR.

## Authorization And Intent Binding

- Require authorization for the exact Swig, role, authority, instruction, destination, amount, and replacement state being changed.
- Do not treat proof that a preceding instruction called an approved program as proof that the program approved the current Swig payload. Bind ProgramExec authorization to the verified state or message that contains the full intended mutation.
- Keep Ed25519, Secp256k1, Secp256r1, ProgramExec, and their session variants explicit. Reject unsupported variants instead of partially parsing or silently downgrading them.
- Preserve replay protection and signature-age rules. Use checked arithmetic for counters, expirations, instruction indexes, offsets, lengths, and accumulated amounts.
- Validate instruction-sysvar program ids, indexes, offsets, account counts, message hashes, and signer/writable flags before trusting introspected data.
- Prevent Swig itself from serving as an external ProgramExec authority unless an explicit design permits and safely binds that recursion.

For every changed auth path, record the authority type, auth source, signed or verified payload, replay source, state consumed, and negative test.

## State And Memory Layout

- Treat discriminants, `LEN`, alignment, offsets, and padding rules as public contracts.
- Accept only layouts explicitly defined by the active version. Reject truncated entries, extra padding, all-zero pseudo-entries, malformed tails, and trailing bytes unless the format deliberately permits them.
- For each stored-state change, record the generation or source, discriminator
  and length, overlaid fields and offsets, canonical decoder, creation guard,
  runtime guard, migration behavior, and legacy fixture.
- Use one canonical decoder or classification rule wherever validation and
  runtime dispatch interpret the same stored discriminant or numeric field.
  Test noncanonical high bits and other representations that could make the two
  paths disagree.
- When tightening construction validation, audit already-stored accounts that
  predate the invariant. Add a runtime guard or explicit migration; creation
  rejection alone does not make legacy state safe.
- Establish the account generation before reading any version-specific field.
  When generations overlay the same bytes, record an offset map for each
  generation and test legacy values whose low or high bytes look valid under
  the new layout.
- Apply the same strict validator before preserving or moving existing bytes. Never carry malformed state through a mutation path.
- Prove every unsafe cast, unchecked slice, and zero-copy view has satisfied length and alignment requirements first. Test buffers holding `#[repr(C, align(8))]` values with real 8-byte alignment.
- Reallocate for both growth and shrinkage. Preserve validated tails and neighboring roles, calculate rent changes safely, and test grow-to-shrink and shrink-to-grow sequences.
- Avoid heap allocation in on-chain parsing and SignV2 hot paths. Prefer bounded fixed scratch with explicit capacity checks, and prove compute-unit behavior did not regress.
- Use a closed-account discriminator or tombstone when closing deterministic Swig accounts so stale data cannot be interpreted as active state and the address cannot be silently squatted.

## Permission Semantics

- Preserve each concrete permission's discriminant, layout, match key, destination key, repeatability, reset behavior, and consumption rules.
- For a delta-based limit, record each transition's before and after values,
  observed delta, charged budget, cumulative state, and expected result. Cover
  increase, decrease, unchanged, repeated operations, reset windows, exact
  boundary, and limit plus one. When multiple observed fields can move together,
  decide and test `sum`, `max`, or separate budgets so one operation is neither
  skipped nor double-counted.
- Do not collapse fixed and recurring limits, or other related variants, into one uniqueness key unless mutual exclusion is an explicit product decision.
- Keep `All`, `AllButManageAuthority`, `ManageAuthority`, `CloseSwigAuthority`, recovery, subaccount, staking, program, and scoped asset permissions distinct.
- Deny unmatched asset movement. Restricted roles must not gain authority through a parser fallback, missing destination classification, unsupported instruction variant, or broad default.
- Keep design docs and implementation synchronized. A mismatch is a product decision to resolve, not a license to choose the more convenient behavior.

## SignV2 And CPI Gate

Require SignV2 to follow this order:

1. validate account structure and find the role
2. authenticate the authority and replay state
3. parse instructions with bounded scratch and validate target programs/accounts
4. check scoped program or destination permission before execution where applicable
5. snapshot relevant native and token state
6. execute through the Swig-controlled wallet PDA
7. verify protected-account integrity and measure post-execution deltas
8. consume every matching limit and reject unmatched or oversize spend

Cover every supported transfer encoding, including checked token transfers, and every account classification that changes enforcement. Benchmark restricted and unrestricted paths when parser structure, loops, authority dispatch, or snapshot limits change.

Bind macro arguments once before testing, logging, or unwrapping them when they
can be expensive or fallible. Benchmark every affected SignV2 permission path,
including ProgramScope, rather than inferring full-matrix cost from one variant.

## Compatibility And Surface Completion

- Treat discriminants, account positions, optional-account rules, instruction data, error codes, and serialized state as compatibility-sensitive.
- Public-instruction integration tests must use the production builder's entire
  instruction for the authority variant under test. Construct a negative case
  by changing one dimension of that output; hand-written full account vectors
  require an explicit reason and proof that authentication reached the intended
  boundary.
- Update the program instruction definition, IDL, interface builder, compact encoder/parser, Rust SDK builder, high-level `SwigWallet` method, and tests together when the feature spans them.
- Do not stop at a low-level instruction builder when the established public SDK exposes equivalent wallet methods.
- Run the downstream TypeScript LiteSVM suite after parser, account-meta, signer/writable, hashing, or wire-format changes.
- Keep unrelated generated or shared files unchanged. If review asks for a full-file revert, revert the entire file rather than preserving a narrower semantic subset.

## Required Negative Tests

Add focused regression tests for every touched invariant. Include the relevant cases:

- missing or short account slices and out-of-range instruction indexes
- wrong signer, owner, program id, PDA, bump, writable flag, or account order
- config/wallet/subaccount self-aliasing as a destination or authority
- malformed, truncated, padded, misaligned, or over-capacity state and instruction data
- wrong authority type, unsupported session type, stale signature, replay, and bad message binding
- recovery payload differing from the state approved by the recovery program
- cross-type and same-type authority rotation, including expected rejections
- account growth, shrinkage, rent top-up, and preserved neighboring/tail bytes
- permission variant coexistence, destination mismatch, overspend, and unmatched spend
- every supported native/token transfer variant and protected-account mutation attempt
- Token and Token-2022 program ownership, 165-byte base layout, initialized
  state, mint equality, and source/destination authority, including malformed
  zero-balance accounts
- first, middle, and last malformed entries in batch or migration inputs, with
  the exact error and unchanged native, token, counter, and account-data state
- client and IDL compatibility after account or wire changes
- compute-unit regression when a hot path changes

Use real Ed25519, k1, and r1 verification for compatibility claims. Use test programs or mocks only for controlled failure injection.

## Validation Gate

Run the narrow focused tests first, then the applicable repository gates:

```bash
cargo fmt --all -- --check
cargo build-sbf --arch v1
cargo nextest run --config-file nextest.toml --profile ci --all --workspace --no-fail-fast
git diff --check
```

Run the `program_scope_test`, `rust_sdk_test`, and stake feature variants when the touched behavior reaches them. Run the downstream TypeScript LiteSVM tests for parser or client-contract changes.

Record a final-head receipt with the exact head and base SHAs, formatter, SBF
build, focused tests, applicable feature matrices, downstream compatibility
suites, CU benchmarks, required parent-check conclusions, and every skipped
gate with its exact blocker. A rebase, base merge, generated-code refresh, or
material head change invalidates the receipt. Do not open, approve, or
re-request review until the changed invariant has a negative test and every
applicable required check is green on that head. A green sub-check does not
override a red required parent job.

Give one test fixture or CI workflow clear ownership of every validator
process, port, setup phase, and cleanup path. Startup failure must fail the test,
not degrade into a warning.

Include this self-review table in the PR body for security-relevant changes.
Treat it as a proof artifact: every applicable `yes` cites the code boundary,
focused test, and exact result; every `N/A` gives a concrete reason.

| Area | Checked | Evidence |
| --- | --- | --- |
| Stored and wire layout | yes/no | test or note |
| Stored-state lifecycle and version overlays | yes/no/N/A | decoder matrix and legacy fixtures |
| Account contract and ordering | yes/no | per-account property ledger and tests |
| Atomic batch or migration preflight | yes/no/N/A | validation ledger and rollback tests |
| Close/drain funds and rent routing | yes/no/N/A | funds-flow ledger and destination matrix |
| Auth and replay binding | yes/no | test or note |
| Permission and delta accounting | yes/no | transition matrix and tests |
| Grow and shrink reallocations | yes/no | test or note |
| CPI and SignV2 enforcement | yes/no | test or note |
| IDL and SDK compatibility | yes/no | test or note |
| Compute units | yes/no | benchmark or N/A |
| Design conflicts resolved | yes/no | decision or ticket |
| Final-head required gates | yes/no | head SHA and check results |
