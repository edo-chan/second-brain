# Evolution Method

Improve the teaching system from observed learning outcomes rather than from
novelty or stylistic preference alone.

## Classify the signal

| Signal | Owning location |
| --- | --- |
| Learner-specific knowledge or preference | Project `progress.md` |
| Missing, misplaced, or oversized topic | Project curriculum |
| Weak or misaligned mastery check | Project curriculum |
| Reusable teaching-method improvement | `ed-teacher` skill |
| Unresolved subject question | Project question log |
| Cross-project hypothesis about teaching | `learning/teaching-observations.md` |

## Evidence threshold

Make a durable change when at least one condition holds:

1. Ed explicitly states a stable learning preference or requests the change.
2. The current method contains a clear factual, logical, or pedagogical defect.
3. The same problem appears in two meaningful sessions.
4. A mastery checkpoint consistently measures something other than its stated
   outcome.
5. A missing prerequisite prevents the learner from engaging with the lesson.

Record a one-off uncertain observation without promoting it yet.

## Improvement cycle

1. Capture the observation and concrete evidence.
2. Name the smallest owning layer that can fix it.
3. State the proposed change and expected learning signal.
4. Make the smallest coherent edit.
5. Preserve prior evidence in project progress.
6. Validate links, skill structure, and repository diff.
7. Use the revised method in a later session.
8. Record whether the expected signal appeared; retain, refine, or revert the
   change accordingly.

## Curriculum review

When progress stalls, inspect in this order:

1. prerequisite coverage;
2. lesson size;
3. notation and definitions;
4. example quality;
5. learner practice;
6. checkpoint alignment;
7. topic ordering.

Prefer inserting the smallest repair lesson over replacing the full track.
Keep the destination stable unless accumulated evidence shows that the
destination itself is wrong.

## Teacher-skill review

Promote only behavior that is useful across topics. Keep subject-specific
insights in the relevant curriculum. After editing `SKILL.md` or its
references:

- confirm the frontmatter still describes every intended trigger;
- confirm the instructions remain concise and non-duplicative;
- regenerate `agents/openai.yaml` when its interface is stale;
- run the skill validator;
- summarize the behavior change and its evidence to Ed.
