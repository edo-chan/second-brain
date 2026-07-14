# Solana Swig Source Map

Use this map to trace a change through the current `swig-wallet` checkout. Re-check paths and commands because feature branches may add or move files.

## State Contracts

- `state/src/action/mod.rs` and `state/src/action/*.rs`: permission discriminants, exact lengths, repeatability, match data, and limit consumption.
- `state/src/authority/mod.rs` and `state/src/authority/*.rs`: authority discriminants, serialized lengths, authentication, counters, sessions, and message binding.
- `state/src/authority/programexec/`: instruction-sysvar authentication and ProgramExec session behavior.
- `state/src/swig.rs` and `state/src/role.rs`: header, role iteration, role mutation, and account-layout boundaries.
- `state/src/transmute.rs` and `no-padding/`: unsafe zero-copy casts, alignment, and padding assertions.

## Program Boundary

- `program/src/lib.rs`: entrypoint dispatch and shared account routing.
- `program/src/instruction.rs`: instruction discriminants, account declarations, and IDL-facing definitions.
- `program/src/actions/*.rs`: validation, authorization, mutation, CPI, and persistence order.
- `program/src/actions/sign_v2.rs`: instruction parsing, account snapshots, CPI execution, integrity checks, delta accounting, and permission consumption.
- `program/src/error.rs`: stable program errors.
- `program/idl.json`: generated public instruction and account contract.
- `program/tests/*.rs`: LiteSVM integration and compute-unit regression coverage.

## Client And Wire Layers

- `instructions/src/compact_instructions.rs` and `instructions/src/lib.rs`: compact wire parsing, scratch buffers, and account indexing.
- `interface/src/lib.rs`: public instruction constructors and account metas.
- `rust-sdk/src/instruction_builder.rs`: low-level builder surface.
- `rust-sdk/src/wallet.rs` and `rust-sdk/src/client_role.rs`: high-level wallet and role APIs.
- `docs/program_diagrams.md`: current architecture and intended behavior; confirm it still agrees with accepted design decisions.
- Adjacent `swig-ts` LiteSVM tests: downstream compatibility for account metas, signer/writable flags, hashing, and instruction bytes.

## Review Order

1. Read the ticket or design section and recent accepted review comments.
2. Compare stored state and instruction payloads separately.
3. Trace every account index from client builder through instruction definition to handler.
4. Trace authorization inputs through the verifier to the exact state mutation.
5. Trace permission matching before and after CPI.
6. Check IDL and every public client surface.
7. Add negative tests before optimizing or generalizing.

## Current Validation Surface

Use the repository's active CI definitions as the source of truth. The established gates include:

```bash
cargo fmt --all -- --check
cargo build-sbf --arch v1
cargo nextest run --config-file nextest.toml --profile ci --all --workspace --no-fail-fast
cargo build-sbf --arch v1 --features=program_scope_test
cargo nextest run --config-file nextest.toml --profile ci --all --workspace --no-fail-fast --exclude test-program-authority --features=program_scope_test
cargo nextest run --config-file nextest.toml --profile ci --all --workspace --no-fail-fast --exclude test-program-authority --features=rust_sdk_test,program_scope_test
```
