# Laws Of UX

Maintain the 30-entry catalog supplied by Ed on 2026-09-07, attributed to
**Jon Yablonski's [Laws of UX](https://lawsofux.com/)**. The names and coverage
were checked against the source index on that date. The principle summaries
below restate the list supplied in the conversation; the application notes
describe how to use it with Ed's interface-design preferences. The directly
linked articles were also read on 2026-09-07 to distill the main skill's
interaction practices. Article guidance is interpreted through Ed's priorities,
rather than adopted wholesale.

Use these as design heuristics with different scopes and evidence, not as
universal numerical rules or substitutes for observing users. They support the
[mobile interface skill](../SKILL.md): clarity, a single focus, linear visual
hierarchy, useful whitespace, and a coherent design system.

## Catalog

### 1. [Aesthetic-Usability Effect](https://lawsofux.com/aesthetic-usability-effect/)

**Principle:** Visual appeal can improve perceived usability.
**Apply:** Use coherent typography, alignment, and color to make the interface
feel orderly. Verify task completion separately; polish does not demonstrate
that a confusing interaction works.

### 2. Choice Overload

**Principle:** An abundance of options can overwhelm people.
**Apply:** Present the choices relevant to the current decision. Group or
progressively reveal secondary options while keeping necessary alternatives
discoverable.

### 3. Chunking

**Principle:** Related pieces of information are easier to handle as meaningful
groups.
**Apply:** Group related labels, values, and controls through spacing and shared
structure. Each group should support the screen's main purpose.

### 4. Cognitive Bias

**Principle:** Systematic patterns in judgment can affect interpretation and
decisions.
**Apply:** Examine how defaults, ordering, labels, and comparison baselines
influence a choice. Make the relevant context visible rather than assuming the
presentation is neutral.

### 5. [Cognitive Load](https://lawsofux.com/cognitive-load/)

**Principle:** Understanding and operating an interface consumes mental effort.
**Apply:** Remove unnecessary interpretation, repeated entry, and memory work.
Keep the current state and next useful action apparent.

### 6. [Doherty Threshold](https://lawsofux.com/doherty-threshold/)

**Principle:** The supplied catalog associates rapid interaction, around
400 milliseconds or less, with a more continuous working rhythm.
**Apply:** Respond promptly to an action and show honest progress for slower
work. Treat the number as a responsiveness heuristic, not a universal backend
deadline or permission to display success before an operation completes.
The source also suggests inaccurate progress bars and deliberate delay;
Ed's clarity-first interpretation retains truthful state and useful feedback
instead of adopting those suggestions.

### 7. [Fitts's Law](https://lawsofux.com/fittss-law/)

**Principle:** Target size and distance influence the effort to reach it.
**Apply:** Give frequent mobile actions adequately sized, reachable targets and
enough separation for accurate touch. Check the actual interaction area, not
only the icon's visual size.

### 8. Flow

**Principle:** People can become absorbed in an activity with sustained focus.
**Apply:** Preserve continuity through predictable actions, saved progress, and
few interruptions. Support the user's task; entertainment and prolonged
engagement are not independent design goals here.

### 9. Goal-Gradient Effect

**Principle:** Motivation can increase as a goal feels closer.
**Apply:** Show accurate progress and the remaining work in a bounded task.
Progress indicators should reflect real completion rather than simulated
advancement.

### 10. [Hick's Law](https://lawsofux.com/hicks-law/)

**Principle:** More numerous or complex choices can increase decision time.
**Apply:** Organize a decision around clear, distinguishable alternatives and a
visible primary path. Reduce choice complexity without burying important
options behind extra steps.

### 11. [Jakob's Law](https://lawsofux.com/jakobs-law/)

**Principle:** Familiarity with other interfaces shapes expectations.
**Apply:** Prefer established navigation, control behavior, and terminology.
Use novel interaction patterns only when they improve the specific task enough
to justify learning them.

### 12. [Law of Common Region](https://lawsofux.com/law-of-common-region/)

**Principle:** A shared visible region can communicate that elements belong
together.
**Apply:** Use a surface or boundary when it clarifies a real relationship.
Whitespace and alignment may already group an ordinary row sufficiently.

### 13. [Law of Proximity](https://lawsofux.com/law-of-proximity/)

**Principle:** Nearby elements tend to be understood as related.
**Apply:** Keep spacing within a group tighter than spacing between groups.
Leave blank space where it makes those relationships clearer.

### 14. Law of Prägnanz

**Principle:** Perception tends to favor a simple, coherent interpretation of
complex visual material.
**Apply:** Use legible structure, consistent shapes, and clear alignment. Remove
visual ambiguity while retaining distinctions the user needs to understand.

### 15. Law of Similarity

**Principle:** Similar-looking elements tend to be perceived as related.
**Apply:** Give equivalent controls and states equivalent visual treatment.
Reserve differences in color, weight, or shape for meaningful differences.

### 16. Law of Uniform Connectedness

**Principle:** A visible connection strongly suggests a relationship.
**Apply:** Connect steps, controls, or data only when that relationship exists.
Lines and shared tracks should explain sequence or association rather than
serve as decoration.

### 17. Mental Model

**Principle:** People use an internal understanding of how a system works to
predict its behavior.
**Apply:** Organize information around the user's task and familiar concepts.
Explain consequential behavior, such as whether a setting changes historical
reports, where the user makes that decision.

### 18. [Miller's Law](https://lawsofux.com/millers-law/)

**Principle:** The supplied catalog uses the familiar seven-plus-or-minus-two
formulation to describe limited short-term memory capacity.
**Apply:** Reduce recall demands through visible context, recognition, and
meaningful grouping. This is not a seven-item limit for menus, categories,
navigation, or every screen; visible choices are different from memory tasks.

### 19. Occam's Razor

**Principle:** When explanations perform equally well, favor fewer assumptions.
**Apply:** As a design analogy, choose the simplest interaction that fully
supports the task. Removing a necessary state or capability is not an
equivalent simpler solution.

### 20. Paradox of the Active User

**Principle:** People often start using software before reading instructions.
**Apply:** Make the main path understandable through its controls, labels, and
feedback, with help at the point of need. Treat this as a tendency, not a claim
that nobody reads documentation.

### 21. Pareto Principle

**Principle:** A relatively small subset of causes can account for much of an
outcome, often summarized as 80/20.
**Apply:** Prioritize the actions and information that matter most in observed
use. Measure that concentration; do not assume the exact ratio or discard
infrequent but necessary tasks.

### 22. Parkinson's Law

**Principle:** Work can expand to occupy the time available for it.
**Apply:** Give tasks a bounded purpose, a visible finish, and sensible defaults
that reduce unnecessary effort. Artificial countdowns are not required.

### 23. Peak-End Rule

**Principle:** Particularly salient moments and an experience's ending can
strongly influence how it is remembered.
**Apply:** Handle consequential moments, errors, and completion with care. End
with a clear result and useful next step; preserve usability throughout the
flow rather than relying on an impressive finale.

### 24. Postel's Law

**Principle:** The catalog advocates tolerant input handling and predictable
output.
**Apply:** Accommodate harmless formatting variations when their meaning is
unambiguous. Validate required fields, amounts, identifiers, permissions, and
workflow state strictly; this heuristic does not override the coding skills'
typed boundaries or fail-closed rules. Ask for correction when input is
ambiguous instead of silently guessing.

### 25. [Selective Attention](https://lawsofux.com/selective-attention/)

**Principle:** Attention concentrates on a subset of available information,
often related to the person's goal.
**Apply:** Make the current focus dominant and supporting information quieter.
Place relevant feedback close to the action; avoid competing banners, bright
panels, and unrelated prompts.

### 26. Serial Position Effect

**Principle:** People may remember the beginning and end of a sequence more
readily than its middle.
**Apply:** Put orienting information at the start and a useful conclusion at the
end. Keep meaningful sequence and grouping intact instead of mechanically
moving every important control to an edge.

### 27. [Tesler's Law](https://lawsofux.com/teslers-law/)

**Principle:** Some task complexity must be handled somewhere in the system.
**Apply:** Let the application perform deterministic calculations and retain
context, while making consequential choices explicit to the user. Simplifying
the screen must not hide unresolved ambiguity or erase necessary work.

### 28. Von Restorff Effect

**Principle:** An item that differs from otherwise similar items can be more
memorable.
**Apply:** Reserve visual emphasis for the current focus or a material exception.
If every element is emphasized, the intended distinction is lost.

### 29. [Working Memory](https://lawsofux.com/working-memory/)

**Principle:** Temporary mental storage supports holding and manipulating the
information needed for a task.
**Apply:** Keep selections, units, comparison periods, and relevant context
visible. Preserve state between steps so users can act through recognition
rather than reconstructing what they just saw.

### 30. Zeigarnik Effect

**Principle:** Unfinished or interrupted tasks can remain salient in memory.
**Apply:** Make legitimate unfinished work easy to resume and completed work
clearly finished. Save progress and offer a deliberate dismissal or deferral
instead of leaving perpetual attention demands.

## Supporting Article

[Design Principles for Reducing Cognitive Load](https://lawsofux.com/articles/2015/design-principles-for-reducing-cognitive-load/)
informs the skill's labeled icons, familiar controls, editable defaults, and
visible choice groups. Its useful distinction is that visual simplification
must preserve clarity. In Ed's workflow, progressive disclosure separates
successive decisions while keeping the alternatives for the current decision
discoverable; it does not justify hiding a necessary option.

## Maintain The Reference

Keep all supplied entries and their source attribution when refining the
application notes. Record additions, removals, or renames explicitly when Ed
updates the list or requests a source refresh. Keep the supplied wording's
meaning separate from local interpretations and from stronger empirical claims.

Use the relevant primary research when a quantitative threshold, behavioral
claim, or consequential product decision requires evidence beyond this
catalog. Update the checked date only after inspecting the source again.
