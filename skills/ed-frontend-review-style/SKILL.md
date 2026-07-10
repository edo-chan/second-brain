---
name: ed-frontend-review-style
description: React, Next.js App Router, and TypeScript implementation and pull-request review standards for Ed's repos. Use when building or reviewing TS/TSX files, components, hooks, App Router routes, Server and Client Component boundaries, frontend API integration, UI state, error handling, or frontend tests.
---

# Ed Frontend Review Style

Follow the repository's established conventions first. Use these sources as the reference baseline without importing their example architecture wholesale:

- [Bulletproof React](https://github.com/alan2207/bulletproof-react) for feature organization and React maintainability.
- [Next.js App Router project structure](https://nextjs.org/docs/app/getting-started/project-structure) for framework boundaries and colocation.
- [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) for language conventions.
- [typescript-eslint typed linting](https://typescript-eslint.io/getting-started/typed-linting/) for type-aware static analysis.

## Architecture And Ownership

- Colocate feature- or route-specific components, hooks, types, schemas, and tests with the feature or route that owns them.
- Move code into shared folders only after a real reuse boundary exists. Avoid giant shared type files and generic API layers.
- Import directly from the defining module. Avoid barrel exports that hide ownership or create dependency cycles.
- Use Server Components by default in the App Router. Add `"use client"` only when browser APIs, state, effects, or client event handlers require it, and keep that client boundary narrow.
- Keep server-only secrets, vendor credentials, and privileged operations out of client bundles. Validate authorization and untrusted input at the server boundary.
- Keep network, storage, signing, and other asynchronous work visible. Do not hide I/O inside helpers that appear pure.

## Components And Interactions

- Keep components focused and readable. Do not define nested components or large nested render functions inside another component.
- Keep props focused on what the component owns. Avoid broad pass-through objects and long prop chains when ownership should be moved.
- Do not add wrapper helpers that only rename, forward, trim, convert, or wrap a single call. Extract logic only when it creates a meaningful boundary or restores readability.
- Represent mutually exclusive UI states explicitly, preferably with a discriminated union such as idle, loading, success, and error.
- Handle loading, empty, error, cancellation, retry, and duplicate-submission behavior where the interaction can reach those states.
- Invoke user-activation browser APIs such as `window.open`, clipboard access, file pickers, and payment prompts synchronously inside the user event. Do not place the activation call after an `await`; open or reserve the target first, then complete asynchronous work.
- Use semantic HTML and preserve keyboard access, labels, focus behavior, and visible error association.
- Keep side effects in event handlers or effects. Derive values during render instead of synchronizing redundant state with an effect.

## TypeScript

- Keep `strict` and `noUncheckedIndexedAccess` enabled.
- Do not use `any`. Treat external data and caught values as `unknown`, then parse or narrow them with a schema, type guard, or runtime check.
- Model required values as required. Use `?` only when omission is valid and the program remains correct without the value; never use optionality to pass malformed or incomplete data downstream.
- Declare explicit types at exported, component-prop, API, storage, and other architectural boundaries. Let TypeScript infer obvious local values.
- Prefer `satisfies` when checking an object against a contract without widening its inferred type.
- Avoid type assertions and non-null assertions. They silence the compiler without adding runtime safety; validate the assumption instead. Document the rare assertion whose safety is locally obvious.
- Use interfaces for object contracts and type aliases for unions, tuples, and derived type expressions.
- Prefer `readonly` data when mutation is not part of the contract.
- Use discriminated unions and exhaustive checks for finite application states. Prefer string literal unions over new enums unless a generated or canonical domain enum already owns the values.
- Use the simplest type that expresses the contract. Avoid mapped, conditional, or generic type machinery when explicit properties are clearer.
- Minimize exported symbols. Use named exports except where Next.js requires a default export, such as `page.tsx` and `layout.tsx`.
- Use inline type imports when the repository enforces them.

## Data And API Boundaries

- Define concrete request and response types for each endpoint or operation and keep them near the feature that consumes them.
- Do not add generic request/response wrappers, untyped JSON pass-throughs, or generic helpers that erase endpoint differences.
- Parse untrusted responses at the boundary before application code consumes them. Do not expose raw response bodies beyond the transport helper.
- Preserve authoritative identifiers and let the presentation layer own display labels unless a canonical metadata endpoint supplies them.
- Surface structured errors that let the UI distinguish validation, precondition, authentication, network, and upstream failures.

## Tests

- Test user-visible behavior and feature outcomes rather than implementation details, source strings, or snapshots of incidental markup.
- Prefer focused integration tests for components and routes, and end-to-end tests for critical user flows.
- Cover success, validation failure, upstream failure, retry or cancellation, and duplicate submission when relevant.
- Mock a real external boundary only when it isolates behavior under test. Do not treat a configured HTTP fixture returning its configured response as proof of application logic.

## Review Severity

Treat the following as blocking when introduced or extended:

- A functional browser or rendering bug, including loss of user activation across an asynchronous boundary.
- A Server and Client Component boundary violation or a secret exposed to client code.
- Untrusted external data asserted as a trusted type without runtime validation.
- A required contract value made optional in a way that permits unusable state.
- A generic API wrapper, raw response pass-through, or trivial helper layer that obscures ownership and endpoint behavior.
- Missing failure-state handling that can strand the user or repeat a sensitive action.

Treat isolated naming or formatting preferences as non-blocking when the repository's automated tooling already owns them.
