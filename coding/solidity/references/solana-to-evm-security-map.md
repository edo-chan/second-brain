# Solana-To-EVM Security Map

Use this map to carry a proven Solana review invariant into EVM without assuming a one-to-one runtime primitive. Preserve the security property, then choose the EVM mechanism that enforces it.

| Solana review concern | EVM expression | EVM-specific caveat |
| --- | --- | --- |
| PDA seeds, bump, and account-key relationships | CREATE2 salt/address derivation, factory/config/vault pairing, proxy implementation/admin slots | A deterministic address does not prove correct code, initialization, or pair ownership. Verify all three. |
| Account owner, executable bit, signer, and writable flags | `msg.sender`, recovered signer, ERC-1271 result, `address.code.length`, target allowlist, storage ownership | Code can be proxied or upgraded. A target address alone may not identify stable behavior. |
| Instruction discriminant, account order, IDL, and SDK builder | Function selector, ABI tuple order, interface, generated binding, typed-data schema, SDK encoder | ABI-compatible types can still have different authorization meaning. Bind semantic fields, not only bytes. |
| Instruction-sysvar or ProgramExec proof | EIP-712 authorization, ERC-4337 UserOperation, ERC-1271 signature, policy-module attestation | Proving a module or signer participated is insufficient unless the proof commits to the exact mutation and execution domain. |
| Monotonic authority odometer and signature age | Nonce domain, deadline/session expiry, chain id, verifying contract, EntryPoint/UserOp hash | Separate direct-call, meta-transaction, session, and UserOperation nonce domains deliberately. |
| CPI target/program permission | External-call target, selector, value, decoded parameters, and postconditions | `call` can create approvals, callbacks, or state changes not visible in the selector. `delegatecall` is effectively storage authority. |
| Pre/post lamport and token-account snapshots | ETH/ERC-20 balance deltas, ERC-721/1155 ownership, allowance/operator changes, protected storage checks | Fee-on-transfer, rebasing, hooks, false/no-return tokens, and approvals require explicit policy. Call arguments are not observed effects. |
| `ProgramScope` account-field policy | Protocol-specific adapter that validates target, selector, decoded parameters, and post-state | Arbitrary EVM storage is not a stable public interface. Do not port raw offsets as a generic permission primitive. |
| Serialized action layout, discriminants, `LEN`, alignment, and padding | Storage layout, enum values, packed fields, mapping keys, ERC-7201 namespace, ABI encoding | ERC-7201 prevents namespace collision but not semantic or intra-namespace layout corruption. |
| Reallocation preserving valid neighboring bytes | Append-only compatible storage or explicit copy/verify/cutover migration | Proxy upgrades do not move state automatically. A new implementation can silently reinterpret old slots. |
| Closed discriminator or account tombstone | Disabled initializers, irreversible closed state, identifier tombstones, deployment registry state | Contract code and deterministic addresses have different lifecycle rules across chains and forks; define whether reopening is ever valid. |
| Swig-controlled CPI signer | Vault-owned execution through policy-checked entrypoints | The vault must not expose an alternate generic executor that bypasses config policy. |
| `AllButManageAuthority` and distinct marker permissions | Separate capability bits/records for operations, authority management, upgrade, recovery, close, and subaccounts | Upgrade authority is an EVM-specific super-capability and must not leak through broad operational execution. |
| IDL, interface, Rust SDK, and TypeScript LiteSVM compatibility | ABI/interface, generated bindings, SDK wallet methods, deployment artifacts, app and Anvil tests | Test the real proxy/factory address and typed-data domain; implementation-only tests miss topology mismatches. |
| Compute-unit regression and bounded on-chain loops | Gas snapshots, fuzz/invariant runs, bounded role/permission iteration, pagination | A logically correct unbounded scan can become a deterministic gas denial of service as state grows. |

## EVM-Native Checks With No Direct Solana Twin

Always add the EVM-native layer after applying the shared invariant:

- proxy, beacon, and implementation slot integrity
- initializer and reinitializer lockout
- `delegatecall`, fallback, receive, and self-call behavior
- ERC-1271 and ERC-4337 caller context
- EIP-712 domain separation and signature malleability handling
- ERC-20 return-value variants, allowances, permits, and token hooks
- ERC-721 and ERC-1155 receiver callbacks and operator approvals
- reentrancy across verifiers, tokens, arbitrary targets, and upgrade hooks
- chain-specific verifier or precompile availability
- CREATE2 salt reuse, predicted-address drift, and factory bypass

## Review Method

For each ported behavior:

1. State the Solana security invariant in one sentence.
2. Identify the EVM trust boundary and persistent state that enforce it.
3. Record where the runtimes differ and whether that creates a product divergence.
4. Implement the smallest deny-by-default EVM policy that preserves the invariant.
5. Add a positive parity test, a negative bypass test, and an EVM-native adversarial test.
6. Verify the public ABI, SDK/signing payload, deployment topology, and live local execution path.
