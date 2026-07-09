---
name: evm-swig-contract-safety
description: Strict EVM Swig contract safety, Solana Swig parity, verifier, vault, permission, and SignV2 review gates. Use when changing or reviewing evm/src/SwigConfig, evm/src/SwigVault, EVM authority types, permission layouts, verifiers, vault execution, upgrades, SignV2, or EVM Swig PRs.
---

# EVM Swig Contract Safety

Treat `evm/` contract work as security-critical wallet code. Do not treat it as scaffold code unless the user explicitly requests a shape-only draft, and even then unsafe asset movement must be disabled or denied by default.

Read [references/solana-swig-parity.md](references/solana-swig-parity.md) before implementing or reviewing EVM Swig contract changes.

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
- Nonce/counter state must be consumed before any external call, or the path must be `nonReentrant`.
- r1 verifier/precompile address must be supplied by factory or chain config.
- Verifier calls must reject missing code, invalid address, revert, false/zero return, malformed return length, wrong pubkey length, wrong signature length, and wrong signer.
- Vault execution must route through Swig policy.
- Subaccount executors must not call arbitrary vault execution directly unless vault-local policy limits are implemented and tested.
- ETH semantics must choose exactly one model: vault-held spend with `msg.value == 0`, or caller-funded forwarding with `msg.value == value`.
- Generic execution must not be able to call config, vault, or proxy upgrade selectors unless the role has explicit `Upgrade`.
- Direct proxy/config initialization must not allow arbitrary nonzero vault addresses if factory-paired deployment is required.
- Asset-moving paths must deny by default unless `All`, `AllButManageAuthority`, or a matching scoped permission is present and consumed.

## SignV2 Gate

Require `signV2` to follow the Solana shape:

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

Use real k1/r1/ed25519 verification in e2e claims. Use mocks only for unit-level failure injection, and do not use mocks to claim real signer compatibility.

## Review Gate

Do not open or re-request review on an EVM contract PR until:

- `forge fmt --root evm --check` passes
- `forge test --root evm` passes
- `git diff --check` passes
- the parity note exists
- negative tests cover the changed invariant
- all TODOs around disabled enforcement include a ticket and a deny-by-default test
