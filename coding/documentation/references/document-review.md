# Ed Document Review

Review the proposal as a contract for a future implementation. Verify that the
described behavior can be built safely on the actual system rather than judging
the document only by internal coherence.

Apply the [documentation standards](../SKILL.md) throughout: concise prose,
decision callouts, purposeful visuals, affirmative scope, complete code
contracts, and a finished design with resolved decisions. Use them within the
review sequence below.

## Review The Whole Document First

Treat a request to review a document as authorization to complete the analysis
and return a consolidated assessment. Read the whole document, establish the
baseline, trace the proposed flows, and apply the relevant review standards
before reporting what needs attention.

The first review report should include:

1. a concise overall assessment;
2. material findings in priority order, with evidence, recommended changes, and
   a simple draft comment to the author for each finding;
3. grouped writing and presentation issues, each with its own author comment;
4. unresolved decisions and verification limits that affect readiness.

Complete this pass without waiting for the user to select individual sections
or request a separate findings report. Include only enough summary to orient
the reader. If a decision requires user input, identify it in the assessment
and continue reviewing the rest of the document.

## Establish The Review Baseline

1. Read the complete target document, including comments, linked sections, and
   declared scope and decisions.
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

- `ed-general-coding` for vendor clients, APIs, proto/gRPC, webhooks, auth,
  response parsing, and sensitive logging.
- `ed-general-coding` for persistence ownership, migrations, derived data, and
  source-of-truth decisions.
- `ed-ci-infrastructure` for secrets, cloud configuration, drift, and
  rollout safety.
- `ed-rust-coding` or `ed-general-coding` when implementation
  shape is part of the proposal.
- `ed-solana-coding` or `ed-solidity-coding` for wallet or
  contract behavior in those domains.

Do not duplicate domain rules inside the review. Apply them to the proposal and
cite the exact section or implementation surface that conflicts.

## Examine The Implementation And Presentation

Work through the implementation-bearing sections autonomously. Focus on
decisions, data flows, contracts, trust boundaries, persistence, failure
behavior, and migration correctness. Read background for context and
apply the documentation standards throughout the document.

Acceptance criteria, rollout plans, and full final database model definitions
are not required document sections. Do not report their absence as findings.
Review the migration and any concrete correctness or safety issue on their merits.

For each material issue, verify the relevant code, schema, primary source, or
other evidence. Explain the consequence and the narrowest change needed.
Reconcile contradictions across sections and combine repeated symptoms before
presenting the assessment.

## Discuss Findings After The Review

Use follow-up discussion to resolve findings or examine the areas the user
chooses. Section-by-section co-review is an optional mode when explicitly
requested. In that mode, treat "next" as selection of the next logical block
and keep the response focused on it.

Review authorization covers analysis and findings. Editing the source document
or posting comments requires the user's instruction; preserve any scope already
authorized in the session. A request to post the findings authorizes the agreed
set without requiring separate approval for every comment.

## Maintain The Agreed Model

Keep a compact working distinction among:

- current-system behavior verified from code or primary sources;
- the document's original proposal;
- the target model agreed with the user during review;
- choices that remain unresolved.

When the user changes a cross-cutting concept, restate the exact resulting
structure before commenting. Translate shorthand into the precise contract: for
example, distinguish deleting a role from removing one permission on that role.
Carry the accepted decision into later blocks instead of continuing to review
against superseded terminology or data shapes.

If a later decision makes an earlier document comment stale, correct that
comment immediately. Prefer editing it or replying in the same discussion over
adding a disconnected correction elsewhere. Preserve the decision history only
when it helps the author understand why the target changed.

## Make Cross-Cutting Contracts Explicit

When behavior depends on several dimensions such as permission, operation,
scope, state, override, or authority type, consolidate the rules in the smallest
clear representation. Prefer a compact list when it suffices. Use a contract
matrix when the dimensions require side-by-side comparison; define its rows
and columns explicitly and keep cells concise.

Include broad-permission and recovery exceptions. Use existing implementation
tests as evidence where relevant. Make hierarchy boundaries explicit: a broad
permission at one layer inherits a scoped permission at another only when the
contract says so.

## Run A Decision Fallout Pass

After accepting a cross-cutting change, scan the rest of the document for stale
consequences. Check the summary, diagram, data layouts, instructions, runtime
flow, authorization, limits, indexing, alternatives, comparison tables,
compatibility, open questions, and verification plan as applicable.

Separate new design questions from mechanical cleanup. Call out calculations,
cost comparisons, instruction numbers, action counts, and compatibility claims
that must be recomputed rather than merely renamed.

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

- **Scope and decisions:** MVP boundaries, explicit product choices, deliberate
  deferrals, and unresolved or contradictory behavior.
- **Authority and trust:** authenticated principal, ownership checks, policy
  enforcement, trusted identifiers, signature or approval boundaries, and who
  is allowed to mutate state or move assets.
- **Contracts:** endpoint-specific request and response shapes, required fields,
  compatibility, authoritative external identifiers, and handling of unknown
  values. Verify that code examples show the complete affected service and
  message definitions or the complete migration under the documentation
  standards.
- **State and data ownership:** canonical source of truth, derived versus stored
  values, idempotency, expiry, replay behavior, atomic updates, and duplicated
  persistence.
- **Failure behavior:** partial success, timeouts, retries, duplicate delivery,
  stale data, malformed upstream responses, reconciliation, and terminal versus
  temporary states.
- **Security and privacy:** secret handling, sensitive payloads, PII retention,
  logging, external URLs or tokens, and deny-by-default behavior for privileged
  or asset-moving actions.
- **Migration correctness:** validity against the current schema, data
  preservation, compatibility, and completeness of the proposed SQL changes.
- **Evidence:** source, examples, tests, or measurements supporting the claims
  under review, with verification limits stated in the review report.

Treat an unresolved product decision as blocking when different answers produce
materially different security, data, API, or user behavior. Do not silently
choose one implementation and review the document as though that choice were
approved.

Resolve these questions through the review and carry the resulting decisions
into the final document. Keep a genuine unresolved decision visible to the user
while the design is unfinished; a polished final document must not conceal it
or leave implementers to choose the behavior.

## Return A Consolidated Assessment

Return the assessment as part of the initial review. Lead with whether the
document is ready, ready with follow-ups, or needs changes, then list material
unresolved findings in priority order. If no material issues were found, say so
and report the verification limits; avoid manufacturing findings.

Use these severities:

- **P0:** unsafe or irreversible behavior, broken authorization, asset or secret
  exposure, destructive data risk, or a design that cannot safely ship.
- **P1:** blocking correctness, contract, ownership, or reliability
  gap that should be resolved before implementation or approval.
- **P2:** important follow-up that can be handled without changing the core
  decision or safety of the proposed design.

Each finding must include:

1. the concrete problem;
2. evidence from the document, repository, or primary source;
3. the behavior or risk it creates;
4. the specific decision or change needed;
5. a draft comment addressed to the author, attached to that finding in the
   review report.

### Write Simple Author Comments

- Include an author comment for every finding, including presentation issues.
- Address one issue and request the specific change directly. Prefer one or
  two short sentences; add the reason only when it helps the author act.
- Anchor the finding to the relevant section or code example. Keep detailed
  evidence and severity in the review rather than repeating them in the comment.
- Use plain language and the same brevity rules as the document. Avoid praise
  padding, review-process narration, and long lists of questions.
- Label the text **Comment to author** so it can be copied into the document.
  Drafting a comment is part of the review; posting it requires authorization.

For example:

> Please specify the result of disabling an already-disabled user, including
> whether `disabledAt` changes.

Prefer a small set of independent findings over a long checklist. Combine
symptoms that share one root cause. Distinguish correctness findings from
violations of Ed's explicit documentation standards and from optional style
preferences; summarize presentation feedback separately. Treat deliberate,
safe deferrals outside the approved scope as scope decisions.

## Finish The Review

- Complete the whole-document assessment before asking the user which finding
  to discuss. Follow any explicit request for a narrower review instead.
- Keep follow-up discussion focused on the selected issue and update the
  assessment when a decision changes its conclusion.
- Call out the strongest parts briefly after the findings when useful.
- Cite the exact document sections, repository files and lines, commits, and
  primary external sources used for material claims.
- State what was not verified and why.
- Keep the review read-only unless the user explicitly asks to edit the document
  or add comments.
- When authorized to post comments, attach each to the narrowest relevant
  section, keep it to one issue, and avoid duplicating it across comments.
