---
name: ed-document-review
description: Evidence-backed review workflow for PRDs, RFCs, architecture proposals, Notion design docs, and technical specifications in Ed's repositories. Use when asked to review a design document, proposal, implementation plan, mini-PRD, or spec for correctness, scope, trust boundaries, implementation readiness, risks, and actionable blocking findings. Pair it with the relevant domain skill; use ed-docs-style instead for prose- and presentation-focused documentation review.
---

# Ed Document Review

Review the proposal as a contract for a future implementation. Verify that the
described behavior can be built safely on the actual system rather than judging
the document only by internal coherence.

## Establish The Review Baseline

1. Read the complete target document, including comments, linked sections, open
   questions, acceptance criteria, and declared non-goals.
2. Identify the decision the document is asking reviewers to approve. Separate
   that decision from background material and future work.
3. Read the directly related parent design, prior version, PRD, ticket, or source
   document when the proposal claims to extend or reuse it.
4. Inspect the current repository state when the proposal depends on existing
   APIs, schemas, services, workflows, or security boundaries. Record the exact
   branch, commit, PR, or release used as the baseline.
5. Verify unstable external claims against current primary documentation,
   especially vendor API fields, platform behavior, limits, and supported flows.

Do not treat planned behavior as already implemented. Distinguish clearly among
the current system, the proposed change, and deferred follow-up work.

## Load The Relevant Review Bar

Use this skill as the review coordinator and load only the domain skills needed
for the proposal:

- `ed-service-boundaries` for vendor clients, APIs, proto/gRPC, webhooks, auth,
  response parsing, and sensitive logging.
- `ed-schema-database` for persistence ownership, migrations, derived data, and
  source-of-truth decisions.
- `ed-infrastructure-rollout` for secrets, cloud configuration, drift, and
  rollout safety.
- `ed-rust-service-style` or `ed-frontend-review-style` when implementation
  shape is part of the proposal.
- `solana-swig-program-safety` or `evm-swig-contract-safety` for wallet or
  contract behavior in those domains.
- `ed-docs-style` only when the user also wants wording, information
  architecture, or reader-routing feedback.

Do not duplicate domain rules inside the review. Apply them to the proposal and
cite the exact section or implementation surface that conflicts.

## Trace The Proposed Flow

Follow one representative request or user action end to end:

1. entrypoint and caller identity;
2. authentication and authorization;
3. validation and source-of-truth lookup;
4. external calls or asynchronous work;
5. persistence and state transitions;
6. response or user-visible outcome;
7. retries, reconciliation, failure recovery, and observability.

Repeat the trace for materially different modes such as direct versus delegated
auth, buy versus sell, happy path versus retry, or standard versus preferred
provider flow.

## Review For Implementation Readiness

Check the proposal for:

- **Scope and decisions:** MVP boundaries, explicit product choices, deferred
  work, and contradictions between acceptance criteria and open questions.
- **Authority and trust:** authenticated principal, ownership checks, policy
  enforcement, trusted identifiers, signature or approval boundaries, and who
  is allowed to mutate state or move assets.
- **Contracts:** endpoint-specific request and response shapes, required fields,
  compatibility, authoritative external identifiers, and handling of unknown
  values.
- **State and data ownership:** canonical source of truth, derived versus stored
  values, idempotency, expiry, replay behavior, atomic updates, and duplicated
  persistence.
- **Failure behavior:** partial success, timeouts, retries, duplicate delivery,
  stale data, malformed upstream responses, reconciliation, and terminal versus
  temporary states.
- **Security and privacy:** secret handling, sensitive payloads, PII retention,
  logging, external URLs or tokens, and deny-by-default behavior for privileged
  or asset-moving actions.
- **Rollout and operations:** migration safety, feature gates, provider or
  environment limitations, metrics, support tooling, rollback, and drift.
- **Verification:** acceptance criteria that are observable, negative tests for
  changed invariants, and a clear way to prove the complete flow works.

Treat an unresolved product decision as blocking when different answers produce
materially different security, data, API, or user behavior. Do not silently
choose one implementation and review the document as though that choice were
approved.

## Write Findings That Can Be Acted On

Lead with the verdict, then list findings in priority order.

Use these severities:

- **P0:** unsafe or irreversible behavior, broken authorization, asset or secret
  exposure, destructive data risk, or a design that cannot safely ship.
- **P1:** blocking correctness, contract, ownership, reliability, or acceptance
  gap that should be resolved before implementation or approval.
- **P2:** important follow-up that can be handled without changing the core
  decision or safety of the proposed design.

Each finding must include:

1. the concrete problem;
2. evidence from the document, repository, or primary source;
3. the behavior or risk it creates;
4. the specific decision or change needed.

Prefer a small set of independent findings over a long checklist. Combine
symptoms that share one root cause, and avoid style comments unless wording
changes the technical contract. Do not present unanswered questions as findings
when the document explicitly and safely places them outside the approved scope.

## Finish The Review

- State whether the document is ready, ready with follow-ups, or needs changes.
- Call out the strongest parts briefly after the findings when useful.
- Cite the exact document sections, repository files and lines, commits, and
  primary external sources used for material claims.
- State what was not verified and why.
- Keep the review read-only unless the user explicitly asks to edit the document
  or add comments.
- When asked to add comments, attach each finding to the narrowest relevant
  section and avoid duplicating the same issue across multiple comments.
