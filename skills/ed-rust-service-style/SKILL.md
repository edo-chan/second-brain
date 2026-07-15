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
- Do not extend generic vendor request/response wrappers or generic JSON deserialization APIs just because existing code uses them.
- Prefer explicit endpoint-specific methods that return concrete response structs.
- Do not let `serde_json::Value` or raw vendor response bodies cross the vendor-library boundary.
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
- Do not introduce generics or explicit lifetime parameters unless Ed explicitly specifies them. Prefer concrete types and elided lifetimes.
- Keep async boundaries visible. Do not hide network, database, or signing work inside helpers that look pure.
- For API handlers, keep validation, domain logic, and response mapping easy to follow. Extract helpers only when readability actually improves.
- Install missing dependencies or toolchains when they clearly help the work instead of reinventing existing tooling.

## Redis

- Use `deadpool_redis` for Redis access in Rust services. Do not introduce unmanaged raw Redis connections.
- Acquire connections from the pool at the visible async boundary and keep Redis commands explicit.
- When `rediss://` support is required, enable the underlying `redis` crate's Tokio/Rustls transport feature, but continue to manage connections and issue commands through `deadpool_redis`.

## Validation

- Use `cargo +nightly fmt` when the repo expects nightly rustfmt; otherwise use the repo's standard formatter.
- Run focused tests for touched behavior.
- Run `cargo clippy --all-targets` for service changes when practical.
- Report any checks that could not be run and why.
