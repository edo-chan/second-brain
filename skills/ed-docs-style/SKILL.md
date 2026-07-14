---
name: ed-docs-style
description: Write and review affirmative, task-oriented documentation for Ed's repositories. Use for product docs, API docs, guides, tutorials, README content, Mintlify pages, and documentation-focused pull requests.
---

# Ed Docs Style

Write documentation around what the reader can do, which surface they should
use, and what action comes next.

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

## Review documentation

1. Search headings and prose for exclusion-first framing.
2. Identify the capability, supported path, or required action behind each
   negative statement.
3. Rewrite around that positive direction without weakening technical
   boundaries.
4. Confirm that the page still routes readers to the correct SDK, API, or next
   step.
