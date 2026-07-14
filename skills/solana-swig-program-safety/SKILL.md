---
name: solana-swig-program-safety
description: Security, compatibility, account-layout, authorization, permission, CPI, compute-unit, and test gates for Solana Swig. Use when implementing or reviewing swig-wallet state, actions, authorities, program instructions, SignV2, recovery, sessions, ProgramExec, compact-instruction parsing, account reallocations, IDL/interface/Rust SDK surfaces, or Solana Swig pull requests.
---

# Solana Swig Program Safety

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
- Reject unsafe aliasing, including a Swig config PDA, wallet-address PDA, subaccount, or other Swig-owned account supplied as an external destination or authority when the operation requires an independent account.
- Keep instruction definitions, processor indexes, `program/idl.json`, interface account metas, and SDK builders identical.
- Preserve existing account order. Append optional accounts when compatibility permits; do not reorder existing accounts without an explicit breaking-change decision and client migration.
- Mark only mutated accounts writable. Avoid unnecessary transaction write locks.
- Authenticate before returning sensitive state-dependent validation errors, but complete all validation before reallocating, mutating state, or invoking another program.

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
- Apply the same strict validator before preserving or moving existing bytes. Never carry malformed state through a mutation path.
- Prove every unsafe cast, unchecked slice, and zero-copy view has satisfied length and alignment requirements first. Test buffers holding `#[repr(C, align(8))]` values with real 8-byte alignment.
- Reallocate for both growth and shrinkage. Preserve validated tails and neighboring roles, calculate rent changes safely, and test grow-to-shrink and shrink-to-grow sequences.
- Avoid heap allocation in on-chain parsing and SignV2 hot paths. Prefer bounded fixed scratch with explicit capacity checks, and prove compute-unit behavior did not regress.
- Use a closed-account discriminator or tombstone when closing deterministic Swig accounts so stale data cannot be interpreted as active state and the address cannot be silently squatted.

## Permission Semantics

- Preserve each concrete permission's discriminant, layout, match key, destination key, repeatability, reset behavior, and consumption rules.
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

## Compatibility And Surface Completion

- Treat discriminants, account positions, optional-account rules, instruction data, error codes, and serialized state as compatibility-sensitive.
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

Do not open or re-request review until the changed invariant has a negative test and every skipped gate is named with its exact blocker.

Include this self-review table in the PR body for security-relevant changes:

| Area | Checked | Evidence |
| --- | --- | --- |
| Stored and wire layout | yes/no | test or note |
| Account validation and ordering | yes/no | test or note |
| Auth and replay binding | yes/no | test or note |
| Permission semantics | yes/no | test or note |
| Grow and shrink reallocations | yes/no | test or note |
| CPI and SignV2 enforcement | yes/no | test or note |
| IDL and SDK compatibility | yes/no | test or note |
| Compute units | yes/no | benchmark or N/A |
| Design conflicts resolved | yes/no | decision or ticket |
