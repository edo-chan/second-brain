---
name: ed-documentation
description: Write and review documentation for Ed's repositories. Use for product docs, API docs, guides, tutorials, README content, Mintlify pages, PRDs, RFCs, architecture proposals, design documents, technical specifications, and documentation-focused pull requests.
---

# Ed Documentation

When entering this skill directly, read the [coding router](../SKILL.md) once
to select any applicable implementation or domain rules.

Write documentation around what the reader can do, which surface they should
use, and what action comes next.

For evidence-backed review of a PRD, RFC, architecture proposal, or design
document, read [document-review.md](references/document-review.md) and follow
its workflow for reviewing the whole document.

Apply the following standards to both writing and review.

## Keep prose simple and scannable

- Use the shortest wording that preserves the contract. Prefer one clear
  sentence when a paragraph adds no meaning; keep one idea per paragraph.
- Use bullets for independent points and numbered lists for ordered steps.
  Break dense prose into meaningful sections, without fragmenting simple ideas.
- State purpose directly: what the system does, for whom, and to what end.
  Keep rationale distinct and beside the decision it explains; retain only the
  evidence or tradeoff needed to understand that decision.
- Explain a rule once at its owning section and reference it where needed.

## Reserve callouts for decisions

- Use callouts only to record a selected approach or settled decision.
- Write the decision in one sentence when possible. Add only the condition or
  consequence needed to interpret it.
- Put notifications, tips, definitions, and ordinary explanations in the text.
  Give every other visual element a clear explanatory purpose and apply the
  same brevity standard. Remove decoration that competes with the content.

## Choose the simplest useful format

- Prefer prose or lists for documentation. Use tables for side-by-side
  comparisons or a compact matrix whose dimensions genuinely require them.
- Use a diagram only when relationships or flow are clearer visually than in
  a short sequence. Keep it small and focused on the decision under review.
- Avoid large charts and tables used merely to divide a wall of text. Rewrite
  the content first; each cell, node, and label should earn its place.

## Frame guidance affirmatively

- Lead with capabilities, supported paths, and recommended actions.
- Route readers to adjacent products directly. For example: "Use the Protocol
  SDK for full protocol control."
- Integrate product boundaries into purpose and routing prose.
- Avoid exclusion-first headings or sections such as "When not to use it,"
  "What this is not," "What this does not cover," and "What to avoid."
- Replace ordinary "do not" instructions with the required action. For
  example, write "Keep API keys on the server" instead of "Do not expose API
  keys in the browser."
- Preserve explicit security, correctness, permission, and irreversible-action
  constraints. State the safe required action first, then explain the risk when
  it helps the reader.
- Keep literal API errors, status names, and factual permission limits exact.

## Show complete and correct code contracts

- Prefer a concrete code example when it communicates the design more clearly
  than prose. Show every proposed change to customer-facing APIs and schemas
  with enough context to review the affected contract.
- For protobuf, include syntax, package, required imports, the enclosing
  service, affected RPCs, applicable route annotations, request/response
  messages, and referenced types needed to understand the changed surface.
  An isolated RPC or field is insufficient.
- For DDL, make the complete migration the primary example, including every
  proposed column, constraint, and index change. Add existing schema context
  only where needed to understand the migration. A complete `ALTER TABLE`
  change can stand on its own; full final model or table definitions are not
  required.
- Comments may stand in for unchanged, unrelated members or implementation
  details. Keep valid enclosing syntax and all dependencies and behavior needed
  to understand the affected contract; comments must not hide proposed changes.
  Scope completeness to the affected surface, without copying the whole system.
- Verify syntax, names, types, field numbers, and behavior against the target
  repository and toolchain. Compile or parse runnable examples where practical;
  distinguish proposed code from existing implementation and label pseudocode.

## Deliver a finished design

- Consider the relevant alternatives, dependencies, edge cases, failure paths,
  and tradeoffs deeply enough to make the decision. Present the smallest
  cohesive explanation that makes the resulting design understandable and
  implementable.
- Resolve material questions and ambiguous behavior before finalizing the
  document. A final design contains decisions and their necessary rationale;
  remove open-question lists, brainstorming, preparation history, and chat-log
  narration from the finished artifact.
- During review, surface unresolved decisions directly and seek the evidence
  or owner input needed to resolve them. Keep the document unfinished until
  those decisions are settled; never hide uncertainty or invent agreement to
  make it read as complete.
- Express deliberate deferrals as clear scope decisions. Preserve the
  assumptions, limits, and failure behavior that implementers need.
- Acceptance criteria and rollout plans are optional. Their absence is not a
  documentation finding; assess the correctness of the proposed behavior and
  migration directly.

## Review documentation

Review the whole document before returning a consolidated assessment of what
needs attention. Treat violations of these explicit rules as review material.
Keep presentation feedback distinct from correctness findings and prioritize
the changes that help the reader understand the decision and its complete
contract. Use section-by-section co-review only when the user asks for it.
Include a simple, direct draft comment to the author with every finding,
including writing and presentation findings. Follow the review workflow's
comment format and posting boundary.
