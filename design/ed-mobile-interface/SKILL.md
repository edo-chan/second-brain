---
name: ed-mobile-interface
description: Design and review mobile app screens, PWAs, and mobile-first web interfaces using Ed's clarity-first principles, linear visual hierarchy, single focus, cohesive palettes, explicit design systems, and responsive row-and-column layouts. Use for interface design briefs, wireframes, visual implementation, and layout reviews.
---

# Ed Mobile Interface

Design for clarity. Make the interface easy to understand and act on;
entertainment and visual novelty are not goals in themselves. Establish its
design system, then let content, rows, columns, and shared tokens determine
the layout. Keep the visual hierarchy linear, with one dominant focus at a time.

Apply the [root guidance](../../SKILL.md) for rule composition and scope. When
implementing an interface, also use the [coding router](../../coding/SKILL.md)
and the relevant platform skill. For a separately requested rendered figure,
use [figure design](../../research/ed-figure-design/SKILL.md) for that
artifact; the surrounding mobile interface remains responsive.

Read [Laws of UX](references/laws-of-ux.md) when choosing interaction patterns,
explaining design tradeoffs, or reviewing usability. It maintains Ed's supplied
catalog with practical application notes. Select principles that explain the
actual design decision; it is not a requirement to apply every entry to every
screen. Keep this skill's clarity, single focus, and linear hierarchy primary.

## Keep The Interface Clean And Direct

- Give each screen a clear purpose. Put its main information and next useful
  action where the user can find them immediately.
- Maintain one dominant focus per screen or active view. Establish a deliberate
  top-to-bottom reading order: primary information, supporting context, then
  secondary detail. Keep competing hero values, equal-weight panels, and
  unrelated calls to action out of the same view.
- Give the primary action the strongest action emphasis when one is needed.
  Keep supporting controls visibly subordinate. Use drilldowns or sequential
  steps to change focus deliberately when the task has several decisions.
- Treat blank space as a useful part of the composition. Leave space where it
  separates groups, establishes hierarchy, or gives the content room to read;
  a screen does not need decoration or extra content just to fill it.
- Use direct labels, familiar controls, and a visible information hierarchy.
  Prefer meaningful content to decorative headings, explanatory filler, and
  repeated labels. Pair unfamiliar icons with text instead of making their
  meaning a guessing task.
- Group related information through alignment, spacing, and typography. Use
  borders, cards, shadows, and separators when they clarify a real grouping;
  ordinary list rows do not each need their own decorative container. Keep gaps
  within a group smaller than gaps between groups.
- Keep frequent actions close to their content. Reveal secondary detail through
  a deliberate drilldown or expansion without hiding necessary context.
- Make loading, empty, error, selected, disabled, and success states clear and
  consistent. A clean appearance must preserve labels, recovery actions,
  accessible contrast, and visible focus.

## Reduce The Work Of Using The Interface

These practices distill the source articles linked from the
[Laws of UX reference](references/laws-of-ux.md). Apply them to the actual task:

- **Make each decision understandable.** Group the alternatives for the current
  choice. Reveal later decisions progressively, but show a clear route to more
  options so the visible subset cannot be mistaken for the complete set.
  Simplicity should remove unnecessary decisions, not necessary distinctions.
- **Keep context available.** Carry selections, filters, entered values, and
  comparison context between steps. Show relevant values together instead of
  requiring the user to remember one screen while reading another. Use editable
  defaults and deterministic calculations to remove repeated work.
- **Make touch targets easy to acquire.** Size the interactive area for accurate
  touch, separate adjacent targets, and keep actions near their related content.
  When a row owns one action, the row can be the target rather than a tiny icon;
  keep any secondary actions distinct and independently operable.
- **Show honest feedback promptly.** Acknowledge the interaction while slower
  work continues. Show measured progress when available and an indeterminate
  state otherwise. Preserve the distinction between pending and complete;
  fabricated percentages and artificial delays do not establish trust.
- **Make relevant changes noticeable.** Place feedback at the affected control
  or content and preserve a stable layout while it updates. Avoid several
  competing changes or distant banner-like notices for a local result.
- **Verify clarity through use.** Check whether a user can identify the next
  action, complete it, and explain the result. A pleasing screenshot or positive
  aesthetic reaction is not sufficient usability evidence.

## Establish A Small Design System First

Before composing screens, record the system in the owning project's design
note or existing token source. Reuse an existing system where one exists and
extend it only for a demonstrated missing role. A small app needs a coherent
token set and component rules, not a speculative component framework.

Define these roles explicitly:

- **Color:** Background, surface, primary text, secondary text, border, primary
  accent, and semantic feedback colors.
- **Typography:** Font family and a short scale of named text roles, with size,
  line height, and weight for each. Use the same role for the same meaning.
- **Spacing:** A base unit and a small set of spacing steps for padding, gaps,
  section separation, and control interiors.
- **Shape:** A small consistent set of corner radii, border widths, and any
  necessary elevation levels.
- **Layout:** Page gutters, content width limits, row and column gaps, alignment,
  and the conditions under which content wraps or changes columns.
- **Components:** The actual repeated elements, such as buttons, input rows,
  list rows, navigation, and sheets, including their interactive states and
  touch-target sizing.

Prefer semantic token names over scattered literal values. Token values are
project choices: this skill does not impose a universal brand, font, fixed
palette, or column count. Introduce a new token only when an existing role
cannot express the intended distinction.

## Keep Color Cohesive And Simple

Start with a neutral foundation and one primary accent. Derive surfaces,
borders, text emphasis, and interaction states from a coordinated palette.
Add another accent only when it communicates a distinct role.

Reserve semantic colors for consistent meanings such as error, warning, and
success. Give the same action or state the same treatment across screens.
Use text, icons, or patterns alongside color when the distinction matters.

Prefer spacing and typographic emphasis before adding another hue. Charts may
need several category colors; choose a small coordinated set, keep category
assignments stable, and label the data directly where practical. Avoid making
every metric or section compete through a different saturated background.

## Compose With Rows, Columns, And Derived Dimensions

Sketch the content hierarchy as nested rows and columns. On mobile, start with
a single readable flow; introduce side-by-side regions when their minimum
content widths fit and they support the same focus. Columns may align related
labels, values, and actions, but must preserve the dominant reading order
rather than create several competing destinations for attention.

Let the layout engine compute ordinary positioning. On the web, prefer normal
document flow, CSS Grid, and Flexbox with shared padding and gap tokens. On
native platforms, use the equivalent stack, grid, and constraint primitives.
Use intrinsic content size, flexible tracks, and container width to drive
placement. Prefer CSS layout computation over JavaScript measuring and
repositioning ordinary interface elements.

For equal columns, derive dimensions from the usable container:

```text
W = container width after outer safe-area insets
P = horizontal content padding on each side
G = gap between columns
N = number of columns that fit the content

column width = (W - 2P - (N - 1)G) / N

Example: W = 390, P = 16, G = 12, N = 2
column width = (390 - 32 - 12) / 2 = 173
```

This formula expresses the layout relationship; a grid implementation should
normally calculate the tracks itself. Choose fewer columns when the content
cannot fit. Let row heights follow content, padding, and alignment rather than
assuming a fixed amount of text.

Keep ordinary content out of hand-placed `top`/`left` coordinates, fixed pixel
offsets, and device-specific nudges. Absolute or fixed positioning is suitable
for intentional overlays, anchored badges, chart geometry, or persistent
controls. In those cases, derive placement from the containing region,
reference element, or data scale and shared tokens. Reserve space for fixed
controls so they cannot cover scrolling content or focused fields.

Support safe areas, the on-screen keyboard, longer labels, larger text, and
changing viewport widths through layout rules. Use wrapping, stacking, or
content-driven breakpoints before reducing legibility or clipping controls.

## Apply And Check The Principles

For a design brief or wireframe, name the single focus and reading order, then
provide the token choices, row/column structure, and behavior when space or
content changes. Keep the deliverable at the level the user requested.

When implementing or reviewing a rendered interface, inspect representative
narrow and wide phone widths, long content, larger text, and relevant keyboard
and interaction states. Check the actual result for hierarchy, contrast,
alignment, spacing, wrapping, clipping, and obscured controls. Revise layout
rules and tokens at their owning source instead of patching isolated offsets.

Before delivery, confirm that one focus dominates, the reading order is linear,
the primary information is direct, color has consistent meaning, repeated
elements share the design system, and ordinary positions follow the row/column
layout. State any visual checks that remain unverified.
