---
name: ed-figure-design
description: Create and review rendered figures, charts, explanatory diagrams, architecture visuals, and data visualizations using Ed's fixed-canvas design-system workflow. Use when drawing or revising a visual figure or diagram, implementing it with TanStack or D3, or preparing a publication-ready PNG.
---

# Ed Figure Design

Make each figure communicate one clear idea through a deliberately established
design system, a 12-column composition, and a verified fixed-size PNG.

## Choose A Figure Deliberately

Use the simplest clear presentation. Keep the global preference for ASCII
charts, sectioned lists, and tables when they communicate the material equally
well. Apply this skill when the user requests a rendered visual or when spatial
relationships, quantitative shape, hierarchy, or flow materially benefit from
one.

## Establish The Design System First

Write down the figure's design tokens before drawing or implementing it. For an
existing product, inherit its font family and palette, then map them to the
fixed tokens below. For a standalone figure, use these defaults:

| System part | Fixed default |
| --- | --- |
| Canvas | 1600 x 900 px |
| Background | `#F8FAFC`, opaque |
| Safe margin | 80 px on every side |
| Layout grid | 12 columns, 24 px gutters, 98 px columns at the default canvas |
| Spacing unit | 8 px; use 8, 16, 24, 32, 48, or 64 px |
| Font family | Inter, then a bundled or system sans-serif fallback |
| Ink | `#0F172A` |
| Muted ink | `#475569` |
| Rule or border | `#CBD5E1` |
| Primary accent | `#2563EB` |
| Secondary accent | `#0F766E` |
| Warning | `#B45309` |
| Danger | `#B91C1C` |
| Stroke widths | 1.5 px regular, 2 px emphasis, 3 px selected path |
| Corner radii | 0, 8, or 16 px |

Use a destination's exact required dimensions when it specifies them. Declare
that fixed width and height before drawing, retain 12 columns, and calculate
the column width as `(canvas width - 2 * margin - 11 * gutter) / 12`. Do not
switch to a responsive or content-sized final canvas.

Treat the typography scale as a closed set. Assign every text role to one of
these T-shirt tokens; do not invent intermediate sizes or weights:

| Token | Font size | Line height | Weight | Typical role |
| --- | ---: | ---: | ---: | --- |
| XS | 12 px | 16 px | 500 | captions and annotations |
| S | 14 px | 20 px | 500 | axes, keys, and secondary labels |
| M | 16 px | 24 px | 500 | primary labels and body copy |
| L | 20 px | 28 px | 600 | section labels |
| XL | 24 px | 32 px | 600 | figure subtitle or major callout |
| 2XL | 32 px | 40 px | 700 | figure title |
| 3XL | 48 px | 56 px | 700 | single hero value when warranted |

Keep text at XS or larger in the final PNG. Use semantic color consistently,
preserve readable contrast, and pair critical color distinctions with labels,
shapes, line styles, or icons.

## Compose On Twelve Columns

Sketch the visual hierarchy on the 12-column grid before rendering details.
Snap titles, panels, plot areas, legends, notes, and callouts to column and
spacing tokens. Let marks and paths use the space inside those regions without
forcing every point onto a column line.

Give the figure one dominant reading path and one primary claim. Prefer direct
labels over distant legends, reserve whitespace intentionally, and remove
decoration that does not clarify structure or data.

## Draw With TanStack Or D3

Implement every rendered figure with an appropriate TanStack library or D3.
Use the repository's existing TanStack visualization primitive when it already
fits a standard structured view. Use D3 for scales, axes, paths, force or
hierarchical layouts, spatial geometry, and custom diagrams.

Choose one as the primary abstraction. Combine them only when the ownership
boundary is explicit, such as TanStack owning structured data state while D3
owns scales and geometry. SVG, Canvas, HTML, and CSS may be rendering surfaces;
keep the visual model and layout logic in TanStack or D3 rather than building a
second ad hoc drawing system.

Bind dimensions, spacing, typography, color, strokes, and radii to the declared
design tokens. Avoid scattered magic numbers and responsive rules that can
change the final composition.

## Export, Inspect, And Adjust

Always produce a PNG at the exact declared canvas dimensions. Keep the final
background opaque unless transparency is explicitly required. Source files may
remain HTML, TypeScript, SVG, or Canvas code, but the required usable output is
the PNG.

Treat the first render as a draft:

1. Render and export the fixed-size PNG.
2. Verify its pixel dimensions and PNG format.
3. Inspect the actual PNG at full size and at fit-to-window or thumbnail scale.
4. Check clipping, overlap, wrapping, alignment, density, hierarchy, contrast,
   legibility, and misleading encodings.
5. Adjust the source, re-export, and inspect again until the image is ready.

Do not use or deliver an uninspected first render. Do not auto-crop, stretch, or
resize the final file after inspection; make layout corrections in the source
and export again at the fixed canvas size.

## Completion Gate

Confirm all of the following before delivery:

- The design system was declared before implementation.
- The composition uses a 12-column grid.
- Every text role uses a fixed T-shirt size and weight.
- TanStack or D3 owns the visual model or layout.
- The output is a PNG at the declared fixed dimensions.
- The rendered PNG was inspected and adjusted before use.
- The figure remains legible at full size and thumbnail scale.
