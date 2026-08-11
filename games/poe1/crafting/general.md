# General PoE Item Crafting

Use this reference for shared Path of Exile 1 rare-item crafting and purchase
decisions. Use an item guide under `equipments/` when one exists, and verify
patch-specific values and currency behavior live.

## Contents

- [Read the item state](#read-the-item-state)
- [Rank modifiers and keep thresholds](#rank-modifiers-by-function)
- [Protect the correct side](#protect-the-correct-side)
- [Choose and evaluate a method](#choose-the-crafting-method)
- [Evaluate against the build and market](#evaluate-against-the-build)

## Read The Item State

Before recommending a click, record:

- base type, item level, quality, base-defense percentile, and influence;
- displayed local defenses;
- every explicit modifier and its prefix or suffix side;
- crafted, fractured, veiled, essence, Delve, and influence provenance;
- Eldritch implicits and which side is dominant;
- open prefix and suffix counts;
- the equipped-item delta and the user's remaining constraints.

Combined display lines may belong to one modifier. Match the line combination
to the current modifier table instead of counting each line separately.

## Rank Modifiers By Function

Use this order:

1. Build-enabling requirements: attributes, resistance caps, reservation,
   sockets, or required influence.
2. Primary local scaling: flat defense plus increased local defense, gem
   levels, damage-over-time multiplier, or the build's equivalent core pair.
3. Defensive layers and recovery.
4. Flexibility: overcap, attributes for future swaps, and open bench space.
5. Luxury modifiers.

For local armour, evasion, and ES items, inspect flat and percentage modifiers
together. A high percentage roll can still produce a weak item when the flat
base or flat prefix is small.

## Use Keep Thresholds

Define thresholds from the user's equipped item and budget:

- **Minimum keep:** materially improves the equipped item without breaking a
  constraint.
- **Strong:** worth finishing with deterministic crafts and implicits.
- **Aspirational:** justifies expensive suffix or prefix manipulation.

Use displayed item totals when they summarize local scaling more reliably than
a remembered tier name. Include useful global modifiers, such as Intelligence
for CI, separately rather than pretending they are part of local item ES.

## Protect The Correct Side

For standard Eldritch currency, verify current wording and use this baseline:

| Dominant implicit | Eldritch Chaos | Eldritch Exalted | Eldritch Annulment |
| --- | --- | --- | --- |
| Searing Exarch | rerolls prefixes | adds a prefix | removes a prefix |
| Eater of Worlds | rerolls suffixes | adds a suffix | removes a suffix |

Dominance comes from the higher-tier Eldritch implicit, not its numeric roll.
Equal tiers do not provide dominance. Re-check Allflame or other league
variants instead of assuming they preserve the standard behavior.

When all prefixes are occupied, a regular Exalted Orb can add only a suffix;
the reverse is true when all suffixes are occupied. A regular Annulment Orb
remains random across all removable explicit modifiers.

## Choose The Crafting Method

- Use fossils when their tag multipliers and exclusions target the required
  modifier families.
- Use essences when the guaranteed modifier is competitive with the natural
  target and the remaining pool is acceptable.
- Use Eldritch currency after the protected side is genuinely worth keeping.
- Use the bench for the final deterministic modifier or a temporary block.
- Avoid influence when required Eldritch implicits are more valuable, because
  conventional influence and Eldritch influence are incompatible.
- Compare expected remaining spend with the price of a finished item before
  continuing.

Do not spend premium suffix-fixing currency on mediocre protected prefixes
merely because the craft has already consumed currency.

## Evaluate Random Steps

For every annulment, exalt, reforge, or conflict operation, state:

- the exact eligible modifiers;
- the chance or qualitative risk of losing the protected result;
- the useful outcomes;
- the recovery path after failure;
- the maximum additional budget.

Pause after a valuable hit. Recount the item before another click.

## Evaluate Against The Build

Use the current PoB and the focused references under `build/` to calculate lost
attributes, resistances, defenses, recovery, damage, sockets, and reservation.
Item quality alone does not establish that the item improves the character.

## Market Decisions

Use current listings and currency exchange values. Compare:

- the candidate's actual character delta;
- finished implicits and bench space;
- cost to repair unfinished affixes;
- price of a better finished item;
- expected cost and variance of continuing the craft.

Recommend selling an intermediate result when another build values its affix
combination more than the current build does.
