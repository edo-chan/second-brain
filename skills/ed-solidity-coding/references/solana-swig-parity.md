# Solana Swig Parity Reference

Use this reference to orient EVM Swig contract work against the Solana implementation. Re-check current files because adjacent checkouts can be on feature branches.

## Source Files To Inspect

- `../swig-wallet/state/src/action/mod.rs`: permission enum, action header, layout validation dispatch.
- `../swig-wallet/state/src/action/*.rs`: action layout, `LEN`, `REPEATABLE`, and `match_data`.
- `../swig-wallet/state/src/authority/mod.rs`: authority enum and authority length dispatch.
- `../swig-wallet/state/src/authority/secp256k1.rs`: k1 authority layout, counter, signature age, and message binding.
- `../swig-wallet/state/src/authority/secp256r1.rs`: r1 authority layout, counter, precompile instruction validation, WebAuthn payloads.
- `../swig-wallet/state/src/authority/ed25519.rs`: ed25519 authority and session auth behavior.
- `../swig-wallet/program/src/actions/sign_v2.rs`: role lookup, authority auth, unrestricted path, scoped program checks, account snapshots, and post-execution delta charging.
- `../swig-wallet/program/tests/*`: parity tests for each authority/action family.

## Permission Shape

Solana permission discriminants:

| Permission | Value | Notes |
| --- | ---: | --- |
| `None` | 0 | No permission. |
| `SolLimit` | 1 | General native spend limit. |
| `SolRecurringLimit` | 2 | Native recurring spend limit. |
| `Program` | 3 | Program-specific execution. |
| `ProgramScope` | 4 | Program/account balance-field scoped execution. |
| `TokenLimit` | 5 | Token mint limit. |
| `TokenRecurringLimit` | 6 | Token mint recurring limit. |
| `All` | 7 | Unrestricted operational permission. |
| `ManageAuthority` | 8 | Authority management. |
| `SubAccount` | 9 | Subaccount management. |
| `StakeLimit` | 10 | Stake limit. |
| `StakeRecurringLimit` | 11 | Stake recurring limit. |
| `StakeAll` | 12 | All stake operations. |
| `ProgramAll` | 13 | Any program execution. |
| `ProgramCurated` | 14 | Curated program execution. |
| `AllButManageAuthority` | 15 | Operational permission excluding authority/subaccount management. |
| `SolDestinationLimit` | 16 | Native destination limit. |
| `SolRecurringDestinationLimit` | 17 | Native recurring destination limit. |
| `TokenDestinationLimit` | 18 | Token mint and destination limit. |
| `TokenRecurringDestinationLimit` | 19 | Token mint and destination recurring limit. |
| `CloseSwigAuthority` | 20 | Close authority. |
| `RecoveryAuthority` | 21 | Recovery path authority. |

EVM may add EVM-only permissions such as `Upgrade`. Any added value must be documented as a deliberate EVM extension rather than Solana parity.

## Authority Shape

Solana authority discriminants:

| Authority | Value | Notes |
| --- | ---: | --- |
| `Ed25519` | 1 | Standard ed25519 authority. |
| `Ed25519Session` | 2 | Session ed25519 authority. |
| `Secp256k1` | 3 | Standard k1 authority. |
| `Secp256k1Session` | 4 | Session k1 authority. |
| `Secp256r1` | 5 | Standard r1/passkey authority. |
| `Secp256r1Session` | 6 | Session r1/passkey authority. |
| `ProgramExec` | 7 | Program execution authority. |
| `ProgramExecSession` | 8 | Session program execution authority. |

EVM must reject authority variants it does not implement. Do not store or accept partially implemented variants.

## SignV2 Execution Shape

Solana `sign_v2` follows this structure:

1. Validate Swig account and wallet-address account classifiers.
2. Parse `SignV2` instruction data.
3. Load the role by `role_id`; missing role fails.
4. Authenticate the role authority.
5. If role has `All` or `AllButManageAuthority`, execute instructions directly and return.
6. Otherwise, compute program permissions before execution.
7. Snapshot writable protected accounts before CPI.
8. Execute compact instructions with the Swig wallet signer.
9. Measure actual native/token/stake/program-scope balance deltas after execution.
10. Verify protected account data/owner did not unexpectedly change.
11. Charge the observed deltas against matching general or destination limits.
12. Revert if spend occurred without a matching limit.

The EVM version should preserve the same security shape even though the mechanics differ: authenticate first, execute only through Swig-controlled vaults, measure/charge observed asset movement, and deny unmatched spend.

## Replay And External Calls

Solana k1/r1 authorities use a monotonic signature odometer and reject reused counters before accepting auth. EVM must provide equivalent replay protection for signature paths.

For EVM, consume nonce/counter state before any external call or use `nonReentrant`. Direct-caller auth must be a distinct direct EOA path, not a signature-auth fallback that can be reused inside ERC-4337 validation.

## Layout Parity Clarifier

When checking an action against Solana, split the comparison into these separate fields:

- stored action layout: bytes persisted in the Swig role
- creation payload layout: bytes supplied when creating the action
- runtime-populated fields: fields filled later by lifecycle instructions
- marker permission behavior: whether presence alone grants a permission
- repeatability: whether multiple instances of the action can exist on one role
- match data: bytes used to select a repeatable action
- review-approved divergence: accepted EVM-specific behavior with a ticket or design note

Do not collapse these into a single "layout" claim. For example, a permission can be zero-data at creation in one design while still having runtime-populated fields elsewhere. If the files, review decision, or design doc disagree, record the target and ask before fixing.

## Known Parity Conflict Pattern

Local Solana checkouts may not always match the latest product decision or review comment. If an action layout in Solana source conflicts with an accepted EVM review decision or design doc, stop and ask for the intended parity target. Do not silently copy the local file or silently follow the review comment.
