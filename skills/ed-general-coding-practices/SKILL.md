---
name: ed-general-coding-practices
description: Language-agnostic implementation and review standards for readable, maintainable, testable, and risk-calibrated software. Use when building, modifying, refactoring, debugging, testing, or reviewing production code in Ed's repositories, then layer on any applicable language and domain skills.
---

# Ed General Coding Practices

Favor the simplest complete change that improves code health without speculative
machinery. Apply repository conventions and more specific language or domain
skills when they impose stronger requirements.

## Design And Scope

- Solve the concrete problem that exists now. Avoid speculative abstractions,
  unused extension points, and genericity introduced for hypothetical needs.
- Keep each change self-contained and reviewable. Include the production
  behavior, tests, documentation, and configuration needed for its contract.
- Keep every PR buildable and semantically honest at its own head. A later
  stacked PR may add behavior, but should not be required to make an earlier
  public field, endpoint, or success response truthful.
- Include a concrete consumer or usage with a new API when practical so its
  shape can be reviewed against a real need.
- Separate broad formatting, dependency upgrades, generated output, and
  mechanical refactors from behavioral changes unless they are inseparable.
- Preserve surrounding conventions when they remain healthy. Do not require
  unrelated perfection or expand a focused change into opportunistic cleanup.

## Readability And Ownership

- Prefer direct control flow, explicit state transitions, and names that reveal
  purpose without requiring a comment.
- Keep functions, modules, and components focused on one responsibility. Split
  code when it mixes phases, trust boundaries, or unrelated side effects.
- Keep data and types near the code that owns their meaning. Introduce shared
  abstractions only after a real reuse or policy boundary exists.
- Avoid pass-through wrappers and helpers that only rename, forward, clone,
  trim, borrow, convert, or hide a single call.
- Write comments to explain rationale, invariants, non-obvious constraints, and
  tradeoffs. Simplify code that needs a comment merely to explain what it does.
- Document purpose, usage, and failure behavior. Update documentation when a
  change affects how users or developers build, test, deploy, release, or use a
  system.

## Boundaries And Failure Behavior

- Identify trusted and untrusted inputs. Validate and canonicalize untrusted
  data at the trusted boundary before domain code consumes it.
- Fail closed for authentication, authorization, token, asset, and other
  security decisions. Do not silently weaken a requirement when configuration
  or dependency state is missing.
- Return errors that preserve actionable context without exposing secrets,
  sensitive payloads, or unnecessary internal details.
- Keep network, database, storage, signing, process, and other side effects
  visible at the call site or behind an explicitly named boundary.
- Prefer standard, well-tested APIs for common parsing, security, concurrency,
  and operating-system tasks. Never pass untrusted data to shell execution or
  dynamic evaluation.
- Make concurrency ownership and lifecycle explicit. Prevent duplicate work,
  races, leaked tasks, and partial state transitions where they matter.

## Tests And Validation

- Add or update tests in the same change as new behavior and bug fixes.
- Choose the test layer that proves the behavior: unit tests for focused logic,
  integration tests for boundaries and public contracts, and end-to-end tests
  for critical user flows.
- Test observable outcomes and side effects. Avoid source-string assertions,
  over-mocked internals, and fixtures that only prove they return configured
  values.
- Ask whether each test would fail if the intended behavior were broken. Cover
  relevant success, invalid input, dependency failure, permission, retry,
  cancellation, and duplicate-submission cases.
- Keep tests deterministic, readable, and no more complex than necessary. Test
  code is maintained code.
- Run focused checks while iterating and the repository's required formatter,
  linter, type, test, and diff checks before publication. Report any check that
  could not run and why.

## Review Severity

- Block concrete correctness, security, authorization, data-loss, public
  contract, and trust-boundary failures introduced by the change.
- Block missing proof for changed critical behavior and required checks that do
  not pass.
- Keep tool-owned formatting, personal naming preferences, optional hardening,
  speculative improvements, and unrelated cleanup non-blocking.
- Calibrate review depth to exposure and impact. Public interfaces,
  authentication, tokens, assets, persistence, concurrency, and external input
  deserve stronger proof than trusted local or internal tooling.
- Prefer reproducible evidence, technical facts, and explicit failure modes over
  personal preference. Explain why a finding matters and name the negative case
  that would prove it fixed.

## Dependencies And Change Hygiene

- Add a dependency only when it provides a clear capability that is preferable
  to a small, understandable local implementation.
- Minimize dependency and feature surface. Do not combine unrelated upgrades
  with feature work without a concrete need.
- Keep generated artifacts reproducible and tool-owned. Do not maintain them
  manually when generation can be automated and verified.
- Keep changes easy to understand, revert, and diagnose in production.

## Sources

- [Google Engineering Practices](https://google.github.io/eng-practices/review/)
  for code health, simplicity, review scope, tests, comments, and severity.
- [NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf)
  for risk-based secure development and continuous improvement.
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
  for trust boundaries, validation, fail-closed behavior, sensitive data, and
  safe use of platform APIs.
