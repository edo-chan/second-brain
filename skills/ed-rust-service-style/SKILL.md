---
name: ed-rust-service-style
description: Rust code organization, workflow layout, async boundaries, formatting, linting, and testing preferences for Ed's service repos. Use when editing Rust services, workflows, handlers, modules, or tests.
---

# Ed Rust Service Style

Favor small, explicit, local changes that match the surrounding module style.

## Code Organization

- Use `mod.rs` only for wiring and exports. Do not put business logic there.
- Keep types next to the consumer that exposes or uses them.
- Avoid giant shared type files, vendor type dumps, and premature type extraction.
- Avoid generic request/response wrappers for vendor or domain APIs unless the repo already uses them.
- Do not add pass-through helpers that only rename or forward another call.

## Workflow Layout

- Organize workflow code under `Workflow/<workflow name>/`.
- Put the workflow definition in `Workflow/<workflow name>/definition.rs`.
- Put the main activity implementation in `Workflow/<workflow name>/activity/<activity name>/definition.rs`.
- Put activity-specific files under `Workflow/<workflow name>/activity/<activity name>/files/`.
- Do not add flat activity files like `Workflow/<workflow name>/activity/<activity name>.rs`.

## Rust Style

- Keep functions concise and single-purpose.
- Prefer typed errors and structured responses where the service already has them.
- Avoid stringly typed error plumbing unless existing code does it.
- Keep async boundaries visible. Do not hide network, database, or signing work inside helpers that look pure.
- For API handlers, keep validation, domain logic, and response mapping easy to follow. Extract helpers only when readability actually improves.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.

## Validation

- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo's standard formatter.
- Run focused tests for touched behavior.
- Run `cargo clippy --all-targets` for service changes when practical.
- Report any checks that could not be run and why.
