# Figure Data And Delivery

Use this reference when defining a figure's claim and preparing its final
artifacts. The main skill owns Ed's design tokens, twelve-column composition,
TanStack or D3 implementation, and fixed-canvas PNG inspection.

## Establish What The Marks Claim

Decide whether the figure shows measured data, a computed model, an illustrative
example, or a conceptual relationship. Make that distinction visible when a
reader could mistake invented example values or schematic geometry for evidence.

For quantitative figures, establish the source, units, population or
denominator, time window, and transformation behind each series. Preserve
source precision and identify estimates or uncertainty when they affect the
claim. Do not invent observations to complete a chart or turn missing values
into zero. Label units and any normalization or aggregation the reader needs.

For computed results, keep the inputs, assumptions, and calculation connected
to the plotted data. Verify current source facts when the claim depends on
changing information. A visually plausible curve is not a verified result.

For conceptual diagrams, define what nodes, edges, arrows, containment, and
relative position mean. Distinguish sequence, dependency, ownership, and data
flow instead of using one arrow to imply all four. Keep sizes and distances
schematic unless they encode a stated quantity.

## Check The Encoding Against The Claim

- Match labels, keys, units, and plotted values to the same data version.
- Use comparable scales for panels presented as direct comparisons; make any
  necessary difference explicit.
- Choose axis domains that preserve the intended comparison. Length-encoded
  bars ordinarily need a zero baseline; disclose truncation, logarithmic
  scales, breaks, and other choices that change visual interpretation.
- Keep uncertainty, exclusions, and material assumptions readable. Do not
  imply precision or causation that the evidence does not support.
- Provide a concise takeaway and essential context in accompanying text so
  the figure's meaning does not depend only on color or inspecting tiny labels.

## Deliver The Inspected Artifact

Keep the source and its data sufficient to reproduce the delivered figure,
within the task's data-handling constraints. Do not embed credentials or
unrelated private inputs in a portable HTML, SVG, or source bundle.

Before export, verify that fonts, images, and data have loaded. Check whether
external assets are required when a figure must work offline. Then follow the
main skill's actual-PNG inspection loop, including dimensions and thumbnail
legibility.

After a source or data correction, regenerate and inspect the PNG before
delivery. Link the final inspected PNG and any requested reusable source; keep
the caption and accompanying result consistent with that version. Do not
deliver an older export under the corrected source's claims.
