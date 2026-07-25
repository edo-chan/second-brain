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
- Use the correct stacked base branch when the work is part of a PR stack.
- Include validation commands and results in the PR body.
- Before marking a PR ready, apply every relevant second-brain coding skill and
  resolve violations of the Swig Coding Standard. Treat new durable style
  guidance from review as a required second-brain update before merge.
- Re-request review only after the requested fixes are implemented and the relevant checks pass.

## Merge And Release

- Merge through the PR when the user expects the work to land and branch protection allows it.
- Do not force-push or use destructive git commands unless the user explicitly asks.
- When making or cutting a release, publish the release on GitHub as part of the rollout.
