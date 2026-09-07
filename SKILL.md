---
name: ed-second-brain
description: Orient work in Ed's second brain, select the right domain skills, and keep reusable rules separate from project state and current evidence. Use when starting non-trivial work for Ed, combining domains, or organizing and extending this guidance repository.
---

# Ed Second Brain

This repository expresses Ed's rules and accumulated working context. Use the
[README](README.md) as the index and this skill to choose the route. Read each
selected skill and its required references once; revisit them when they change
or the task reaches a new boundary.

## Choose The Route

- **Build, debug, review, document, or publish software:** use the
  [coding router](coding/SKILL.md).
- **Advise on a game, deck, build, collection, or craft:** use the
  [games router](games/SKILL.md).
- **Teach, resume study, assess learning, or improve a curriculum:** use the
  [learning router](learning/SKILL.md).
- **Draw or review a rendered figure:** use
  [figure design](presentation/ed-figure-design/SKILL.md).

Choose by the requested outcome, not a keyword alone. A request to explain a
Rust concept as a lesson belongs to learning; a request to fix its production
implementation belongs to coding. A lesson with a rendered diagram uses both
the teacher and figure-design skills. Game-probability tutoring can use the
teacher while the game skill owns current mechanics and personalization gates.

If no listed skill fits, follow the task and applicable repository guidance.
Use available tools or current authoritative sources as needed; do not invent
a skill or load an unrelated domain to fill the gap.

## Preserve Ed's Rules

- Follow Ed's explicit instructions and existing task authorization. More
  specific repository `AGENTS.md` guidance takes precedence over reusable
  defaults; domain and boundary rules specialize the shared guidance.
- Treat `must`, `require`, and `do not` as requirements. Treat `prefer` and
  `default` as choices within the stated constraints. An unusual or
  opinionated rule remains binding until Ed changes it.
- Apply exceptions only within their stated scope. Honor approval already
  given for the same choice in the current task instead of asking again.
- Distinguish a convention violation from a factual, correctness, or security
  failure. Cite the actual rule or evidence; do not invent a technical risk to
  justify a preference.
- Resolve equally applicable conflicting rules at their owning layer. Keep
  independent work moving while a necessary decision is pending.

## Keep Knowledge At Its Owning Layer

- **Reusable behavior:** a skill or its focused reference.
- **Current personal state:** the owning domain's state files or learning
  project. Preserve the distinction between confirmed, inferred, proposed,
  and completed state.
- **Subject sequence and mastery evidence:** the curriculum and project
  progress, under the teacher's evidence rules.
- **Changing external facts:** dated evidence verified through the relevant
  domain's source policy. A historical note is not proof of current state.
- **Temporary inputs and experiments:** task-local artifacts unless the
  domain explicitly calls for durable storage.

Organizing skills does not demonstrate learner mastery, acquire game items, or
complete a proposed plan. Update personal state only from evidence that meets
the owning skill's rules.

## Organize And Extend Deliberately

Read the existing owner and its callers before adding guidance. Put substantial
conditional procedures in a focused reference with a direct link and loading
condition. Add a domain router when it has real choices to own; keep a single
self-contained skill direct.

Preserve Ed's policy when polishing wording. State the trigger, decision, and
required evidence for an extension; keep examples illustrative and place live
facts in dated references. Maintain one authoritative statement of a rule.

When changing this repository, use the
[Git workflow](coding/infrastructure/references/git-workflow.md). Preserve
unrelated work, validate affected skills and links, and check realistic routing
or behavioral scenarios when a change could alter an agent's decisions.
