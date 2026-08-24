---
name: ed-solidity-coding
description: Solidity and EVM contract implementation and review standards for Ed's repositories, including strict Swig parity, storage and upgrade safety, exact intent binding, ABI and SDK compatibility, and security gates. Use when changing or reviewing Solidity contracts, evm/src/SwigConfig, evm/src/SwigVault, authority types, permission layouts, verifiers, vault execution, upgrades, SignV2, ERC-4337/UserOp auth behavior, or EVM contract PRs.
---

# Ed Solidity Coding

Treat `evm/` contract work as security-critical wallet code. Preserve its storage, authorization payloads, ABI, deployment topology, public SDK, and client compatibility while making the smallest explicit change that satisfies the requested behavior. Do not treat it as scaffold code unless the user explicitly requests a shape-only draft, and even then unsafe asset movement must be disabled or denied by default.

Read [references/solana-swig-parity.md](references/solana-swig-parity.md) before implementing or reviewing EVM Swig contract changes. Use [references/solana-to-evm-security-map.md](references/solana-to-evm-security-map.md) to translate a Solana invariant into EVM mechanics without assuming that similarly named primitives have identical security properties.

## Trace The Entire Contract

Before editing, trace the affected behavior through every layer that consumes it:

1. storage structs, namespaced storage, mappings, enums, and reserved slots
2. implementation, proxy, beacon, factory, vault, verifier, and module contracts
3. public interfaces, ABI selectors, events, custom errors, and typed-data schemas
4. deployment scripts, chain configuration, initializers, salts, and predicted addresses
5. SDK encoders, signing helpers, ERC-4337 adapters, and application entrypoints
6. tests, Anvil or fork fixtures, documentation, and downstream client fixtures

Classify each field separately as persisted storage, initialization input, signed authorization data, runtime-derived state, or client-only metadata. Identical names do not prove identical layout, lifecycle, or trust.

If source, design documentation, accepted review feedback, deployed state, and client behavior disagree, stop and record the product decision before implementing. Do not silently pick one source of truth.

## Solana Parity Gate

Treat EVM Swig as a port of Solana Swig unless a Linear ticket or design doc explicitly records a divergence.

Before changing `evm/src/SwigConfig` or `evm/src/SwigVault`, inspect:

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
- intentional divergence with ticket or doc link

If Solana source, existing EVM review comments, and the design doc disagree, stop and resolve the product decision before implementing.

When checking Solana parity, distinguish stored action layout, creation payload layout, runtime-populated fields, marker permission behavior, and review-approved intentional divergence. If these disagree, do not call it a bug or a fix. Stop and record the intended parity target.

Parity means preserving the security outcome, not transliterating Solana mechanics. A Solana program id is not automatically equivalent to an EVM target address, an account field is not automatically equivalent to arbitrary contract storage, and a CPI permission is not automatically equivalent to unrestricted `call` or `delegatecall`.

## Authorization And Intent Binding

- Bind authorization to the exact chain, verifying contract, Swig/config, vault, role, authority, action, target, selector, value, calldata or calldata hash, nonce, deadline or session bound, and replacement state that the operation relies on.
- Bind ERC-4337 authorization to the intended EntryPoint, account, nonce domain, call data, and UserOperation hash. Do not reuse a direct-call signature or empty-auth shortcut as UserOperation authorization.
- Use an explicit domain separator and unambiguous encoding. Test cross-chain, cross-contract, cross-role, cross-function, and cross-nonce replay. Avoid ambiguous `abi.encodePacked` constructions for signed dynamic values.
- Treat `msg.sender`, recovered EOA identity, ERC-1271 contract signatures, EntryPoint callers, and delegated execution as distinct auth sources. Never use `tx.origin` as wallet authority.
- A proof that an approved contract ran does not prove that it approved the current Swig mutation. Bind program or module authority to the exact state transition or message that contains it.
- Consume nonce/counter state before the first post-auth execution call. Guard auth-time ERC-1271 or verifier callbacks against reentrancy and do not expose partially authorized state. `nonReentrant` is call-safety protection; it is not replay protection.

For every changed auth path, record the authority type, caller context, signed or verified payload, domain, replay source, state consumed, external calls, and negative test.

## Storage And Upgrade Compatibility

- Treat storage slots, field order, field width, enum values, mapping keys, namespace roots, initializer versions, and reserved gaps as public contracts.
- ERC-7201 isolates namespace roots; it does not make field reordering, type changes, key changes, or semantic reinterpretation safe. Append compatible fields or implement an explicit copy, verify, and cutover migration.
- Never reuse removed enum values, role ids, nonces, or storage fields for a different meaning. Preserve tombstones when old identifiers must remain distinguishable.
- Verify the exact EIP-1967, beacon, UUPS, or custom slots in use. Test implementation and admin slot integrity, initializer lockout, reinitialization rejection, and upgrade authorization through the real proxy topology.
- Preserve factory/config/vault pairing. Direct initialization, alternate salts, or user-supplied nonzero pair addresses must not create a bypass unless the design explicitly permits it.
- Compare storage layouts before and after an upgrade and inspect representative raw slots on Anvil when the change affects deployed state. A compiling upgrade is not evidence of storage compatibility.

## Blocking Invariants

A PR is not ready unless touched invariants are encoded in tests:

- Root creation cannot produce a bricked Swig: root must have `ManageAuthority` or `All`.
- `AllButManageAuthority` must not grant `ManageAuthority`, `Upgrade`, or `SubAccount`.
- Marker permissions must use the exact accepted Solana layout.
- Unsupported authority, session, and program authority variants must be rejected at validation.
- k1, r1, and ed25519 must work consistently on every management and signing path where they are claimed to be supported.
- Direct-caller auth and signature auth must be separate code paths.
- Empty auth bytes must never be reused in ERC-4337/UserOp validation.
- Every signature auth path must have replay protection.
- Nonce/counter state must be consumed before the first post-auth execution call, and every external validation or execution boundary must be reentrancy-safe.
- Session authorities must bind their parent role and authority, have an enforceable maximum duration, and be unable to refresh or extend themselves past that bound.
- r1 verifier/precompile address must be supplied by factory or chain config.
- Verifier calls must reject missing code, invalid address, revert, false/zero return, malformed return length, wrong pubkey length, wrong signature length, and wrong signer.
- Vault execution must route through Swig policy.
- Subaccount executors must not call arbitrary vault execution directly unless vault-local policy limits are implemented and tested.
- ETH semantics must choose exactly one model: vault-held spend with `msg.value == 0`, or caller-funded forwarding with `msg.value == value`.
- Generic execution must not be able to call config, vault, or proxy upgrade selectors unless the role has explicit `Upgrade`.
- Direct proxy/config initialization must not allow arbitrary nonzero vault addresses if factory-paired deployment is required.
- Asset-moving paths must deny by default unless `All`, `AllButManageAuthority`, or a matching scoped permission is present and consumed.

## Permission Semantics

- Preserve each permission's discriminant, stored shape, creation shape, match key, destination key, repeatability, reset behavior, and consumption rules.
- Translate Solana permissions by security effect. `Program`, `ProgramScope`, and `ProgramCurated` require an explicit EVM policy over target, selector, decoded parameters, value, and observable postconditions; a target allowlist alone is not equivalent.
- Treat token approval, permit, operator approval, and delegation as creation of future spending authority. A role must not bypass spend limits by approving a third party and moving assets later.
- Deny unmatched ETH, ERC-20, ERC-721, and ERC-1155 movement. Account for fee-on-transfer, rebasing, callback-capable, and non-standard tokens using observed effects where supported; reject unsupported semantics explicitly.
- Keep `All`, `AllButManageAuthority`, `ManageAuthority`, `Upgrade`, recovery, close, subaccount, and scoped asset permissions distinct. Generic execution must not make a narrower permission equivalent to `All`.
- Do not add `delegatecall` to generic execution unless storage authority, implementation trust, and upgrade-equivalent consequences are explicitly designed and tested. Default to rejecting it.

## Solidity Numeric Conversion Style

- Avoid dense nested cast-and-shift expressions. Convert raw bytes into a named value at the destination width, then perform the shift.
- Keep both shift operands at compatible widths when Solidity warns about mixed-width behavior. Do not reintroduce opaque casts merely to silence the compiler.
- Name endian-specific helpers explicitly and test byte order with representative values.

Prefer:

```solidity
uint64 byteValue = uint64(uint8(data[offset + i]));
value |= byteValue << uint64(i * 8);
```

over:

```solidity
value |= uint64(uint256(uint8(data[offset + i])) << (i * 8));
```

## Auth Path Matrix

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

## Verifier Failure Matrix

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

## External Call And Reentrancy Gate

Any authorized function that makes an external call must include:

- checks and replay-state consumption before the call
- `nonReentrant` or a proof that reentrant callbacks cannot cross an invariant boundary
- a reentrancy regression test
- a test that replaying the same authorization fails even if the first call reenters

Treat ERC-1271 validation, token hooks, fallback/receive handlers, verifier calls, proxy callbacks, and arbitrary target calls as external-call boundaries. Check return-data shape and bubble or normalize reverts deliberately.

## Generic Execution Upgrade Denylist

Any generic execution feature must include negative tests showing it cannot call:

- config upgrade selectors
- vault upgrade selectors
- proxy upgrade selectors
- role-management selectors unless the role has explicit `ManageAuthority`
- recovery or close selectors unless the role has the explicit permission

## SignV2 Gate

Require `signV2` to follow the Solana shape:

1. role exists
2. authority authenticates
3. target/program permission is checked before execution when scoped
4. execution happens through the Swig-controlled vault
5. native/token deltas are measured and charged to matching limits
6. unmatched spend reverts

Pre/post enforcement must cover every permission-relevant effect, not only the nominal call arguments. Include ETH balance deltas, token balance or ownership deltas, newly granted approvals/operators, and protected config/vault integrity as applicable. For batch execution, charge aggregate observed effects and revert the whole batch on any unmatched effect.

A shape-only `signV2` PR may omit full permission mapping only when:

- the TODO says the missing enforcement is intentional
- a ticket ID is included
- unsafe fund movement is denied or limited to explicitly broad permissions
- tests prove restricted roles cannot move assets through the gap

## Test Gate

Add negative tests for every touched invariant. Happy-path tests are insufficient.

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
- cross-chain, cross-contract, cross-role, and cross-function signature replay
- storage-layout drift, initializer replay, and unauthorized proxy/beacon upgrade
- approval, permit, operator, or `delegatecall` bypass of a spend or target restriction
- malicious callback and ERC-1271 reentrancy
- fee-on-transfer, rebasing, false-return, no-return, and malformed-return token behavior when supported
- ABI selector, typed-data schema, SDK encoding, salt, or predicted-address mismatch

Use real k1/r1/ed25519 verification in e2e claims. Use mocks only for unit-level failure injection, and do not use mocks to claim real signer compatibility.

## Compatibility And Surface Completion

- Treat ABI selectors, event topics and indexed fields, custom error selectors, storage layout, typed-data type hashes, nonce domains, proxy slots, CREATE2 salts, and predicted addresses as compatibility-sensitive.
- Update contract interfaces, implementations, generated ABI or bindings, SDK encoders, signing helpers, deployment scripts, chain configuration, documentation, and tests together when the feature spans them.
- Do not stop at a low-level ABI call when the established public SDK exposes an equivalent wallet method.
- Test through the real proxy, factory, vault, verifier, EntryPoint, or application adapter used by the claim. A direct implementation-contract unit test cannot prove deployment-path behavior.
- Measure gas when a hot authorization, role lookup, permission scan, batch, or post-execution accounting path changes. Unbounded loops over durable state require an explicit bound or pagination design.

## Review Gate

Do not open or re-request review on an EVM contract PR until:

- `forge fmt --root evm --check` passes
- `forge build --root evm` passes
- `forge test --root evm` passes
- `git diff --check` passes
- the parity note exists
- negative tests cover the changed invariant
- all TODOs around disabled enforcement include a ticket and a deny-by-default test

Use `/Users/edchan/.foundry/bin/forge` when Foundry is installed there but absent from `PATH`. Run the repository's Anvil, fork, deployment, SDK, and ERC-4337 end-to-end gates when the changed contract reaches those surfaces. Name every skipped gate and its exact blocker.

Include this self-review table in the PR body before opening or re-requesting review:

| Area | Checked | Test |
| --- | --- | --- |
| Permission layout parity | yes/no | test name |
| Repeatability parity | yes/no | test name |
| Exact intent and domain binding | yes/no | test name |
| Direct auth safety | yes/no | test name |
| Signature replay | yes/no | test name |
| Verifier failures | yes/no | test name |
| Storage and upgrade compatibility | yes/no | layout/test evidence |
| External-call reentrancy | yes/no | test name |
| Generic exec upgrade blocking | yes/no | test name |
| Approval and delegated-spend blocking | yes/no | test name |
| ABI, SDK, and deployment surface | yes/no | test or note |
| Value semantics | yes/no | test name |
| Gas or loop bounds | yes/no | benchmark or N/A |
| Parity target conflicts resolved | yes/no | note/ticket |
