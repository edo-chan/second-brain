# CI High-ES Body Armour

Snapshot: Path of Exile 1, patch 3.29, verified 2026-08-10.

Use this guide for a six-linked pure-ES body armour such as a Twilight Regalia.
Read `../general.md`, `../methods.md`, `../probability.md`, and
`ilvl-86-affixes.md` before recommending a craft.

## Contents

- [Define the target](#define-the-target)
- [Base checklist](#base-checklist)
- [Keep thresholds](#keep-thresholds)
- [Prefix-first routes](#prefix-first-routes)
- [Finish suffixes](#finish-suffixes)
- [Stop conditions](#stop-conditions)

## Define The Target

For a CI build, the core item is usually three local ES prefixes:

- high flat maximum ES;
- high local increased ES;
- hybrid local increased ES plus stun/block recovery.

On an ilvl 86 pure-ES body armour, the top ordinary tiers are listed in
`ilvl-86-affixes.md`. These prefixes multiply the base's innate ES and quality,
so base percentile and quality materially change the displayed result.

Estimate local ES as:

```text
displayed ES ~= (base ES + local flat ES) *
                (1 + quality + local increased ES)
```

Use the displayed item value for decisions because combined affixes and game
rounding are easy to misread.

## Base Checklist

- correct pure-ES base and item level for the intended tiers;
- six links before expensive explicit crafting unless the linking plan is
  already priced and accepted;
- strong base ES percentile;
- quality plan completed before judging the final ceiling;
- fracture, influence, corruption, split, and Intangibility state recorded;
- Eldritch compatibility preserved when side-specific finishing is planned.

Item level 86 matters for the top local percentage prefix and the top faster
start of ES recharge suffix. It does not guarantee a good roll.

## Keep Thresholds

Set exact thresholds from the current PoB and market. As a practical rare-body
classification, not a universal rule:

- **temporary:** a clear ES gain that keeps links, resistances, and attributes;
- **strong:** roughly 900-1000 displayed ES with useful suffixes or safe suffix
  finishing space;
- **aspirational:** 1100+ displayed ES or a slightly lower total whose premium
  suffixes produce a better whole-build result.

Do not pay endgame finishing costs merely because an item crosses a round ES
number. Compare the actual character ES, recovery, resistance, block, and cost.

## Prefix-First Routes

### Dense Fossil Or Defense-Weighted Reforge

Dense Fossils favour defense modifiers and prevent Life modifiers. They still
roll every eligible competing defense modifier and do not guarantee all three
ES prefixes. Use current simulation for the exact base, item level, fossil
combination, and success threshold.

### Essence Route

Use a current Essence only when its guaranteed body-armour modifier belongs in
the finished prefix set. The Essence rerolls every other non-fractured explicit
modifier. Verify its exact current value and tag before buying a large batch.

### Allflame Preview Route

Allflame can preview several results from the same original item, but current
Intangibility can reduce the outcome count. Calculate from the UI's actual
preview count rather than assuming four.

Stop on a prefix set whose displayed ES and recoverability justify suffix work.

## Finish Suffixes

Useful suffix families can include elemental resistance, Intelligence, faster
start of ES recharge, ES recharge rate, regeneration that a verified build can
apply, or physical damage reduction. Value each against the current PoB.

On a compatible non-influenced body armour, establish Eldritch dominance before
using an Eldritch Chaos, Exalted, or Annulment. Reconfirm which side the exact
currency affects. Do not use a regular Annulment to protect valuable prefixes.

Bench block modifiers on body armour occupy a prefix. Physical damage reduction
crafts commonly compete on the suffix side. Verify current bench wording and
open slots before assuming both fit.

## Stop Conditions

Pause when:

- all three prefixes are occupied;
- a target ES total is reached;
- one side becomes valuable enough to protect;
- an unexpected low-tier combined affix changes the tier count;
- only a random annul or expensive side reroll remains;
- expected remaining spend exceeds a better finished listing.

Re-import the candidate into PoB before the final bench craft or purchase.
