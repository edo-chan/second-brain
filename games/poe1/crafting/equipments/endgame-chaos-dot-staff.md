# Endgame Chaos Damage Over Time Staff

Snapshot: Path of Exile 1, patch 3.29, verified 2026-08-10.

Use this guide for an Essence Drain/Contagion or similar spell-based Chaos DoT
staff. Recheck the current modifier table, bench crafts, build calculation, and
trade prices before spending. Do not apply these priorities to attack-based
poison or ailment builds without recalculating their scaling.

## Target Item

The aspirational five-mod rare has three damage prefixes and two damage
suffixes:

| Modifier | Side | Top ordinary value | Min ilvl | Base weight |
| --- | --- | ---: | ---: | ---: |
| all Spell Skill Gems | prefix | +2 | 55 | 250 |
| all Chaos Spell Skill Gems | prefix | +4 | 77 | 100 |
| spell damage | prefix | 150-174% | 79 | verify live |
| Chaos DoT multiplier | suffix | +66-75% | 78 | 50 |
| cast speed | suffix | 44-49% | 83 | 1000 |

Use a caster staff, not a warstaff. Item level 83 unlocks every target tier in
the table; item level 86 is acceptable but is not required by this exact set of
targets. Higher item level may add competing modifiers.

Confirm in Path of Building that another base, an influence modifier, or a
crafted modifier does not outperform the ordinary target for the current
character. Conventional influence also prevents normal Eldritch implicits,
though staves do not use Eldritch implicits.

## Value Tiers

- **Minimum keep:** +2 all Spell Skill Gems and +4 all Chaos Spell Skill Gems,
  with enough open affixes to add meaningful spell damage and Chaos DoT
  multiplier.
- **Strong:** both gem prefixes, strong spell damage, and either strong Chaos
  DoT multiplier or cast speed.
- **Aspirational:** all five target families at high natural tiers, with the
  sixth affix useful or open.

For this build, gem levels and Chaos DoT multiplier usually deserve priority
over cast speed. Verify the actual PoB delta because gem level breakpoints,
existing increases, and skill choice can change the ordering.

## Completion Routes

### Buy The Finished Item

Search current trade listings with the two gem-level prefixes as hard filters,
then compare total PoB damage using spell damage, Chaos DoT multiplier, and cast
speed. This is the default when the expected cost of reproducing the rare gem
prefix pair exceeds the finished-item premium.

### Finish A Natural Gem-Prefix Pair

If the item already has both gem prefixes:

1. Confirm the third prefix and all suffixes before touching it.
2. Keep an open prefix for spell damage when it is missing.
3. Keep an open suffix for Chaos DoT multiplier when it is missing.
4. If the remaining natural modifiers are weak, compare a safe multimod finish
   with buying a stronger item before attempting a random annulment.
5. With only the two natural gem prefixes, one common safe finish is the
   current `Can have up to 3 Crafted Modifiers` suffix plus crafted spell
   damage and crafted Chaos DoT multiplier. Verify current bench values and
   unlocks before committing.

Multimod itself consumes one suffix and counts as one of the three crafted
modifiers. The two added bench modifiers consume one prefix and one suffix,
leaving one suffix open in the clean two-prefix starting state.

### Build Around A Fracture Or Preview Craft

A fracture can protect one rare target while the rest of the item is rerolled,
but it does not make the second gem prefix likely. Allflame previews can improve
the chance of seeing a useful result from the same original item, while
Intangibility can reduce later preview counts. For either route:

1. define the minimum acceptable final state;
2. reproduce the exact base, item level, fracture, blocks, and crafting method
   in the current Craft of Exile simulator;
3. include the cost of failed bases or resets;
4. stop when the expected remaining spend exceeds a comparable finished staff.

Do not recommend a raw fossil, Essence, Chaos, Exalted, or Annulment operation
as an endgame plan without enumerating what it can overwrite and its recovery
path.

## Probability Boundary

The +2 all-spell prefix has base weight 250 and the +4 chaos-spell prefix has
base weight 100, but multiplying two single-draw weight ratios is not the exact
chance of rolling both on a rare reforge. Rare items have variable affix counts,
prefix and suffix selection, modifier groups, tag changes, blocks, and method-
specific rules.

Use `../../scripts/craft_odds.py` only after a current calculator or verified
pool gives a valid per-outcome probability for one selection or one full craft.
Use simulation for the complete two-prefix or five-mod target. Report:

- chance per craft and assumptions;
- expected attempts and expected total cost;
- 50%, 90%, and 95% attempt counts;
- price of the closest finished trade alternative.

## Stop And Reassess

Pause immediately after obtaining both gem prefixes or a high-tier Chaos DoT
multiplier alongside one gem prefix. Recount all affixes, verify whether each
line is natural, fractured, Essence, Veiled, or crafted, and price the item in
its current state before another irreversible click.
