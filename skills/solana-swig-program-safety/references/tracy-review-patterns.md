# Tracy Review Patterns

This is a reusable synthesis of Tracy's `swig-wallet` reviews, not an immutable protocol specification. Re-fetch current PR state and comments when the task depends on the latest review decision.

The initial snapshot was collected on 2026-07-14 from 23 open or merged PRs updated since 2026-01-01. It contained 66 Tracy-authored review events and 36 substantive comments across 15 PRs.

- Open PRs inspected: [#138](https://github.com/anagrambuild/swig-wallet/pull/138), [#155](https://github.com/anagrambuild/swig-wallet/pull/155), [#165](https://github.com/anagrambuild/swig-wallet/pull/165), [#179](https://github.com/anagrambuild/swig-wallet/pull/179), [#180](https://github.com/anagrambuild/swig-wallet/pull/180), [#181](https://github.com/anagrambuild/swig-wallet/pull/181), [#182](https://github.com/anagrambuild/swig-wallet/pull/182), [#183](https://github.com/anagrambuild/swig-wallet/pull/183), and [#184](https://github.com/anagrambuild/swig-wallet/pull/184).
- Merged PRs inspected: [#107](https://github.com/anagrambuild/swig-wallet/pull/107), [#123](https://github.com/anagrambuild/swig-wallet/pull/123), [#133](https://github.com/anagrambuild/swig-wallet/pull/133), [#134](https://github.com/anagrambuild/swig-wallet/pull/134), [#136](https://github.com/anagrambuild/swig-wallet/pull/136), [#144](https://github.com/anagrambuild/swig-wallet/pull/144), [#153](https://github.com/anagrambuild/swig-wallet/pull/153), [#156](https://github.com/anagrambuild/swig-wallet/pull/156), [#160](https://github.com/anagrambuild/swig-wallet/pull/160), [#164](https://github.com/anagrambuild/swig-wallet/pull/164), [#166](https://github.com/anagrambuild/swig-wallet/pull/166), [#168](https://github.com/anagrambuild/swig-wallet/pull/168), [#170](https://github.com/anagrambuild/swig-wallet/pull/170), and [#171](https://github.com/anagrambuild/swig-wallet/pull/171).

Closed, unmerged PRs were excluded from the synthesis.

## Contract Consistency

- Treat behavior changes hidden inside optimizations as breaking changes. A uniqueness helper must not accidentally make fixed and recurring limits mutually exclusive. See [PR #171](https://github.com/anagrambuild/swig-wallet/pull/171#discussion_r3423681554).
- Resolve design-document and implementation mismatches explicitly. Do not silently preserve one permission gate while claiming another. See [PR #180](https://github.com/anagrambuild/swig-wallet/pull/180#pullrequestreview-4568399475).
- Keep runtime account indexes, instruction definitions, IDL, and client builders synchronized. See [PR #183](https://github.com/anagrambuild/swig-wallet/pull/183#discussion_r3517384165).
- Preserve account order and ask whether any positional change breaks existing clients. See [PR #134](https://github.com/anagrambuild/swig-wallet/pull/134#discussion_r2760613430).
- Complete the established public SDK surface, not only the lowest-level builder. See [PR #182](https://github.com/anagrambuild/swig-wallet/pull/182#discussion_r3573686504).

## State And Account Safety

- Enforce exact versioned layouts. Reject all-zero pseudo-tails, truncated entries, extra padding, and entry-plus-padding when the contract permits only empty or one exact entry. See [PR #179](https://github.com/anagrambuild/swig-wallet/pull/179#discussion_r3464976527).
- Validate bytes before preserving them across role mutation; otherwise reallocations carry malformed state forward. See [PR #179](https://github.com/anagrambuild/swig-wallet/pull/179#discussion_r3464985144).
- Reallocate on shrink as well as growth to avoid progressive account bloat and incorrect later offsets. See [PR #183](https://github.com/anagrambuild/swig-wallet/pull/183#discussion_r3573733792).
- Reject both the Swig wallet-address PDA and the Swig config PDA when an external destination must not alias Swig-owned state. See [PR #180](https://github.com/anagrambuild/swig-wallet/pull/180#discussion_r3573662855) and [PR #184](https://github.com/anagrambuild/swig-wallet/pull/184#discussion_r3576069266).
- Use a closed discriminator or tombstone for deterministic accounts so closed state cannot be confused with live state or trivially squatted. See [PR #123](https://github.com/anagrambuild/swig-wallet/pull/123#pullrequestreview-3558540972).
- Remove unnecessary writable flags to reduce lock contention. See [PR #138](https://github.com/anagrambuild/swig-wallet/pull/138#discussion_r2850754372).

## Authorization And Recovery

- Bind ProgramExec proof to the exact state transition. Verifying only the preceding program and discriminator leaves role ids and replacement keys attacker-controlled. See [PR #156](https://github.com/anagrambuild/swig-wallet/pull/156#discussion_r3249295975).
- Authorize who may create recovery policy for a wallet; a transaction signer alone is not proof of authority over the target Swig. See [PR #156](https://github.com/anagrambuild/swig-wallet/pull/156#discussion_r3249289391).
- Audit every authority variant when changing rotation or recovery. Do not accidentally remove session-authority behavior. See [PR #183](https://github.com/anagrambuild/swig-wallet/pull/183#discussion_r3517392384).
- Place duplicate or state-dependent checks after authentication, while still keeping them before realloc or mutation. See [PR #155](https://github.com/anagrambuild/swig-wallet/pull/155#discussion_r3231013031).
- Prevent the Swig program from serving as its own external ProgramExec authority unless explicitly designed. See [PR #107](https://github.com/anagrambuild/swig-wallet/pull/107#discussion_r2528104362).

## Parser, Runtime, And Compute Discipline

- Check account count before unchecked indexing and use checked arithmetic for offsets, counters, and session expiry. See [PR #107](https://github.com/anagrambuild/swig-wallet/pull/107#discussion_r2443162882) and [PR #107](https://github.com/anagrambuild/swig-wallet/pull/107#discussion_r2443180087).
- Respect zero-copy alignment in host tests; `[u8; N]` is not sufficient storage for an 8-byte-aligned struct without an aligned wrapper. See [PR #107](https://github.com/anagrambuild/swig-wallet/pull/107#discussion_r2443138697).
- Avoid heap-backed `Vec` changes in on-chain parser hot paths when fixed bounded scratch works. Re-run compute-unit comparisons. See [PR #165](https://github.com/anagrambuild/swig-wallet/pull/165#discussion_r3392530392).
- After parser changes, run the TypeScript SDK LiteSVM suite to catch account-meta and wire incompatibilities. See [PR #165](https://github.com/anagrambuild/swig-wallet/pull/165#issuecomment-4736965008).
- Update CU expectations intentionally when new dispatch variants add measured cost. See [PR #107](https://github.com/anagrambuild/swig-wallet/pull/107#discussion_r2442835225) and [PR #123](https://github.com/anagrambuild/swig-wallet/pull/123#pullrequestreview-3580880203).

## Test And Scope Discipline

- Test the new rejection cases directly; a nearby mismatch test is not coverage for cross-type rejection behavior. See [PR #183](https://github.com/anagrambuild/swig-wallet/pull/183#discussion_r3517407046).
- Build auth matrices across k1, r1, account mismatch, program mismatch, challenge mismatch, duplicate fields, and empty scopes. See [PR #138](https://github.com/anagrambuild/swig-wallet/pull/138#discussion_r2850747987).
- Follow literal rollback requests and keep the diff scoped. A request to revert a file entirely means no unrelated cleanup remains in that file. See [PR #156](https://github.com/anagrambuild/swig-wallet/pull/156#discussion_r3260594285).
