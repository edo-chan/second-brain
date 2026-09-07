---
name: ed-coding-router
description: Select and compose Ed's second-brain coding skills for implementation, debugging, code review, technical documentation, and infrastructure or Git work. Use when entering coding work or when its scope crosses languages, service boundaries, persistence, or publication.
---

# Ed Coding Router

These skills express Ed's engineering rules, including deliberate restrictions
and blocking conventions. Preserve those choices when applying or maintaining
the skills. Correct technical errors, conflicting instructions, and ambiguous
scope without replacing Ed's policy with generic engineering preferences.

## Establish The Route

1. Read the repository's applicable `AGENTS.md` instructions and identify the
   requested action and affected contracts.
2. For implementation, debugging, refactoring, testing, or code review, read
   [ed-general-coding](general/SKILL.md) as the shared baseline.
3. Add only the domain skills below that apply to the actual work. For
   documentation or infrastructure work, add the general baseline when the
   task also changes or evaluates code, service contracts, or persistence.
4. Follow each selected skill's conditional reference links. Read required
   references completely before acting on the corresponding part of the task.

Read each skill or reference once per task unless it changes or new scope makes
another reference relevant. A direct invocation of a domain skill enters this
same route; retain already-loaded instructions rather than restarting it.

## Select The Domain Skills

- [ed-typescript-coding](typescript/SKILL.md): TypeScript, React, Next.js, and
  browser interactions.
- [ed-rust-coding](rust/SKILL.md): Rust services, applications, libraries,
  workflows, and their tests.
- [ed-solana-coding](solana/SKILL.md): Solana programs and Swig account,
  instruction, authority, permission, and client compatibility contracts. Use
  it as the primary domain skill for on-chain Rust. Add the Rust skill when a
  separate service or library responsibility also needs its rules.
- [ed-solidity-coding](solidity/SKILL.md): Solidity and EVM contract work,
  including Swig security and Solana parity.
- [ed-documentation](documentation/SKILL.md): technical writing and document
  review. Follow its document-review workflow when evaluating a proposal.
- [ed-ci-infrastructure](infrastructure/SKILL.md): infrastructure, configuration,
  CI, local service topology, and Git publication. Add it when work advances
  to branch, commit, PR, merge, or release actions.

The general skill routes vendor/API/auth work to its service-boundary reference
and persistence work to its database reference, regardless of implementation
language. A language skill supplements those rules rather than replacing them.
Use the existing review workflow for a guided PR walkthrough; an explicitly
requested independent findings pass loads the
[Git workflow](infrastructure/references/git-workflow.md#independent-review-gate)
and follows its independent-review contract. Writing or publishing review
comments remains separately scoped.

## Apply Precedence And Revisit Scope

- Follow Ed's explicit instructions and existing task authorization. Apply
  more-specific repository `AGENTS.md` guidance before these reusable defaults.
- Within these skills, a rule for the specific domain or boundary takes
  precedence over the general baseline. A stricter naming or organization
  convention may therefore block approval even when the general rule treats
  personal preferences as non-blocking.
- When equally applicable rules disagree, identify the exact conflict and
  resolve the intended rule. Keep independent work moving while a required
  decision is pending.
- Revisit the route when the task expands to another language, trust boundary,
  persistence surface, deployment, or publication step. Load the newly relevant
  skill or reference before performing that work.

The repository README routes between top-level areas; this skill composes the
coding skills; each domain skill routes to its own detailed references. Add
another router only when a layer has a real selection decision to own.
