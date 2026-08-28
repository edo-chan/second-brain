# Simplicity Review

Use this focused pass when the user asks what can be deleted, simplified, or
replaced, or requests an over-engineering audit. It complements the normal
correctness and security review; it does not replace them.

## Contents

- Choose the scope
- Hunt for removable complexity
- Classify findings
- Deferred-simplification ledger
- Boundaries

## Choose The Scope

- For a pull request or local change, review only the diff and enough
  surrounding code to verify ownership and reuse.
- For a repository audit, scan the whole tree and rank findings by maintenance
  surface removed.
- Keep the pass read-only unless the user explicitly asks to apply fixes.

## Hunt For Removable Complexity

Look for:

- dead code, unused flexibility, speculative features, flags, and configuration;
- endpoints, schema fields, state variants, compatibility paths, and tests
  belonging only to a superseded product flow;
- standard-library behavior implemented locally;
- hand-maintained standards tables or validators that a focused maintained
  library or reproducible authoritative source already owns;
- dependencies or custom UI that duplicate native platform capabilities;
- interfaces with one implementation, factories with one product, and layers
  with one caller;
- pass-through wrappers and helpers that only rename, forward, clone, trim,
  borrow, or convert;
- duplicated behavior that belongs at one shared ownership boundary;
- several files or abstractions representing one concrete operation;
- internal structs that mirror an existing generated proto value type and add
  only field-for-field `to_proto` / `from_proto` conversions;
- one-purpose discriminator strings, booleans, or optional fields whose only
  valid value or branch can be removed;
- structs with several optional fields that actually represent separate use
  cases and should be lean case-specific types instead; preserve optionality
  when absence is genuinely part of one external wire, deserialization, or
  storage shape;
- data-driven registries built for hypothetical additions when the current
  product supports a small closed set that a direct enum and match express more
  clearly;
- duplicate implementations of one protocol flow where provider-specific code
  or one current product path can replace the generic-plus-patches design;
- knowingly simplified implementations whose ceiling or upgrade trigger is not
  recorded.

Do not flag structure that protects a real ownership, trust, compatibility,
testability, or policy boundary. Apply the repository's module conventions and
the relevant Rust, Solidity, Solana, frontend, service-boundary, database, and
infrastructure guidance before recommending consolidation.

## Classify Findings

Use one of these labels:

- `delete` — remove dead code, unused flexibility, or a speculative feature;
  nothing replaces it.
- `stdlib` — replace local implementation with a named standard-library API.
- `native` — replace code or a dependency with a named platform or framework
  capability.
- `yagni` — defer an abstraction, configuration point, or extension mechanism
  until a concrete second use exists.
- `shrink` — express the same behavior more directly without obscuring intent.
- `centralize` — fix duplicated behavior once at its actual ownership boundary.
- `debt` — add or repair the ceiling, observable trigger, and upgrade path for
  a deliberate simplification.

Each finding must state:

1. the exact file and line or symbol;
2. the concrete maintenance surface being removed;
3. what replaces it, including "nothing";
4. why the replacement preserves behavior and required boundaries.

Before deleting legacy flow code, record the current intended data flow and
enumerate every endpoint, persistence field, state variant, configuration key,
test, and caller that exists only for the old flow. Delete the whole ownership
slice together when compatibility is not required; do not leave dormant
branches and nullable schema behind.

Do not use line count alone as proof. Prefer reductions in dependencies,
configuration, exported surface, indirection, duplicated ownership, files, and
operational burden. Dense or clever code is not simpler.

## Deferred-Simplification Ledger

Search for the repository's ticket marker and `simplification-debt:` comments.
For each deliberate shortcut, report:

- location;
- current ceiling;
- observable upgrade trigger;
- likely upgrade path;
- linked owner or ticket when present.

Flag a marker missing a trigger or upgrade path. Do not create a standalone
ledger file unless the user asks for a durable report.

Suggested neutral form:

```text
simplification-debt: global lock; split per account if measured contention exceeds the service target
```

## Boundaries

- Do not simplify away validation, authorization, replay protection,
  data-loss handling, accessibility, migrations, compatibility, observability,
  or tests required by changed behavior.
- Do not recommend fewer files when that would violate established module or
  ownership boundaries.
- Do not replace application validation with database constraints when the
  repository's schema policy does not authorize those constraints.
- Treat security-critical EVM and Solana negative-test and parity gates as
  non-negotiable.
- Keep correctness, security, and performance findings in the normal review
  pass with their appropriate severity.

If nothing material can be removed, say that the reviewed scope is already
lean and stop.

## Source

Adapted from Ponytail's
[review](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-review/SKILL.md),
[audit](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-audit/SKILL.md),
and
[debt](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-debt/SKILL.md)
workflows.
