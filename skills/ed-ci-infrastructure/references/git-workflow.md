# Ed Git Workflow

Use a feature branch for repository changes. Do not commit or push directly to `main`.

## Branch

- Inspect the current branch and worktree before editing.
- Create or switch to a feature branch for changes, using `codex/` by default unless the user asks for another prefix.
- If the user asks only for analysis, review, or planning, do not make code changes unless the request clearly implies implementation.
- If the user explicitly says not to open a PR, stop at the requested local or pushed branch state.

## Commit

- Keep commits scoped to the requested work.
- Do not revert unrelated user changes.
- Run the narrow relevant checks before committing.
- Stage only files that belong to the task.
- Use clear, behavior-focused commit messages.

## Pull Request

- Open a PR for completed repository changes unless the user explicitly says not to.
- For multi-part work, default to a linear stack of small, focused PRs. A
  single cohesive change may remain one PR; do not manufacture artificial
  splits.
- Branch each dependent slice from the preceding stack head and base its PR on
  that immediate predecessor. Keep every PR independently readable, buildable,
  and semantically honest.
- Keep stack ancestry linear. Use sibling branches only for genuinely
  independent work when that shape is clearer.
- Include validation commands and results in the PR body.
- Before marking a PR ready, apply every relevant second-brain coding skill and
  resolve violations of the Swig Coding Standard. Treat new durable style
  guidance from review as a required second-brain update before merge.
- Re-request review only after the requested fixes are implemented and the relevant checks pass.

## Merge And Release

- Do not merge any PR unless the user explicitly authorizes merges in the
  current session. An implementation request, green checks, merge readiness, or
  approval from a prior session is not merge authorization.
- Treat merge authorization as scoped. It may name one PR, a specific stack, or
  grant session-wide permission; merge only the scope the user approved.
- Without current-session merge authorization, leave the PR or stack open and
  report its readiness and blockers.
- When authorized to merge a stack, merge base-to-tip and restack or retarget
  the remaining PRs as needed.
- Do not force-push or use destructive git commands unless the user explicitly asks.
- When making or cutting a release, publish the release on GitHub as part of the rollout.
