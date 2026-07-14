---
name: ed-pr-review-workflow
description: Collaborative pull-request review workflow for Ed's repositories. Use when asked to show PRs that need Ed's review, choose a PR stack, understand a stacked change before reviewing it, or walk through PR code together. Present reviewable stacks first, wait for Ed to choose, read the complete selected stack and load the relevant domain skills, then review each PR bottom-up with an overview and a user-paced block-by-block walkthrough.
---

# Ed PR Review Workflow

Treat a stacked review as a collaborative session with explicit stages. Build the
complete context before judging individual diffs, keep each PR scoped to its own
base, and let Ed control when the review moves forward.

## Present The Review Queue

When Ed has not selected a PR or stack:

1. Resolve the repository and current GitHub state.
2. Find open PRs that request Ed's review, need his follow-up, or belong to a
   chain containing one of those PRs.
3. Group PRs into stacks using their live base and head branches. Verify actual
   commit ancestry instead of relying only on PR titles or branch names.
4. Present each stack from root to tip, including:
   - PR numbers, titles, authors, and links;
   - review requests and existing review decisions;
   - checks, conflicts, unresolved threads, and draft state;
   - age or distance from the current default branch;
   - the main implementation areas and likely review skills.
5. Give a concise recommendation when useful, but do not choose the stack for
   Ed. Wait for him to select one.

Treat GitHub review state, checks, and ancestry as time-sensitive. Refresh them
before reporting the queue.

## Understand The Whole Stack First

After Ed selects a stack, read the complete stack before starting the first PR
walkthrough:

1. Read every PR body, commit list, changed-file list, complete diff, check
   result, review thread, and linked ticket or design document.
2. Inspect the current default branch, each PR's exact base and head, and the
   combined stack-tip diff.
3. Trace the intended behavior across the stack and identify:
   - why the stack exists and what outcome it delivers;
   - the responsibility and dependency of each PR;
   - cross-PR contracts, trust boundaries, state transitions, and tests;
   - behavior introduced in one PR but tested, enforced, or deferred in another;
   - pre-existing behavior at the reviewed base versus behavior introduced by
     the stack.
4. Read the relevant implementation and tests around the changed code, not only
   the diff.
5. Select and read every applicable second-brain domain skill before forming
   review conclusions.

Summarize the stack map, end-to-end flow, main risks, applicable skills, review
order, and any context blockers. State when the context pass is complete, then
pause so Ed can begin the PR walkthrough with you.

## Load The Relevant Review Skills

Use this skill as the review coordinator. Load only the skills that match the
selected stack:

- `ed-rust-service-style` for Rust services, workflows, handlers, modules, and
  tests.
- `ed-frontend-review-style` for React, Next.js, TypeScript, and browser flows.
- `ed-service-boundaries` for vendor clients, public APIs, proto/gRPC, webhooks,
  auth boundaries, response parsing, and sensitive logging.
- `ed-schema-database` for schemas, migrations, persistence, and source-of-truth
  decisions.
- `ed-infrastructure-rollout` for secrets, Terraform, cloud configuration,
  drift, and rollout behavior.
- `solana-swig-program-safety` or `evm-swig-contract-safety` for the matching
  wallet domain.
- `ed-git-workflow` when the requested work progresses from read-only review to
  comments, branch changes, re-review, merge, or release actions.

Apply the domain skills to the concrete code. Do not duplicate their rules in
this coordinator skill.

## Review Each PR Bottom-Up

Review the root PR first and continue toward the stack tip. For each PR, compare
its head to its declared base so parent changes are not reviewed again.

### Start With The PR Overview

Before examining individual code blocks, present:

- the PR's job in the stack and what depends on it;
- its PR-local behavioral change and important files;
- the flow through the changed code and the proof supplied by tests;
- existing review comments and whether they appear current, addressed, or still
  actionable;
- your preliminary take, strongest concerns, and promising parts;
- the domain skills being applied and why.

Keep preliminary conclusions open to revision as the walkthrough uncovers more
evidence.

### Walk Through Logical Blocks Together

Divide the PR into coherent implementation blocks such as a migration, proto
contract, transport client, handler, workflow, UI interaction, test group, or
infrastructure change. Do not split code into arbitrary line-count chunks.

For one block at a time:

1. Identify the files and responsibility of the block.
2. Explain how it works and how it connects to earlier and later blocks.
3. Give your take on correctness, ownership, failure behavior, tests, and
   relevant tradeoffs.
4. Call out a potential finding only when supported by concrete code and the
   applicable review skill.
5. Record cross-PR dependencies or questions that must be checked later.
6. Pause for Ed's questions or direction before moving to the next block.

Maintain a compact running ledger of confirmed findings, open questions,
strengths, and deferred cross-stack checks. Resolve ledger items when later
blocks or PRs provide the missing evidence.

## Finish A PR And The Stack

At the end of each PR:

- recap confirmed findings in priority order with exact file and line evidence;
- separate blockers from non-blocking follow-ups and questions;
- state the current review verdict;
- wait for Ed before moving to the next PR or posting anything to GitHub.

After the final PR, reconcile the ledger across the whole stack and give a
stack-level verdict. Do not post comments, submit a review, approve, request
changes, modify branches, or merge unless Ed explicitly asks for that action.
