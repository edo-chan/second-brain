# PoE 1 Crafting Methods And Odds

Snapshot: Path of Exile 1, patch 3.29, verified 2026-08-10.

Read currency wording in game before an irreversible click. This reference
describes the normal effect; item rarity, influence, corruption, fractures,
metamods, and league-specific variants can change eligibility.

## Core Currency

| Method | Normal effect | What remains | Primary risk |
| --- | --- | --- | --- |
| Transmutation | normal item becomes magic | base, implicits, quality | random magic affixes |
| Alteration | rerolls all explicit modifiers on a magic item | base, implicits, quality | loses the current magic roll |
| Augmentation | adds one modifier to a magic item if possible | existing magic modifier | random eligible affix |
| Regal | magic item becomes rare and gains one modifier | existing magic modifiers | random added affix |
| Alchemy | normal item becomes rare | base, implicits, quality | all explicit affixes random |
| Chaos | rerolls all explicit modifiers on a rare item | base, implicits, quality | destroys the current rare affixes |
| Exalted | adds one modifier to a rare item with an open affix | every current modifier | random eligible open-side affix |
| Annulment | removes one removable explicit modifier | all modifiers not selected | protected affix can be removed |
| Scouring | removes removable explicit modifiers | base, implicits, quality, fractures | destroys the current craft |
| Divine | rerolls values inside current explicit modifier ranges | modifier identities | may lower strong rolls |

An Exalted Orb selects from the eligible side when only prefixes or only
suffixes are open. An Annulment Orb is random across all removable explicit
modifiers unless a special currency or item state narrows it.

## Targeted Reforging

### Essences

An Essence upgrades a normal item to rare or reforges a rare item while
guaranteeing the Essence modifier. All other non-fractured explicit modifiers
are regenerated. The guaranteed value is not necessarily the same as a natural
tier. Do not assume a metamod protects an Essence reforge.

### Fossils And Resonators

Fossils reforge an item with tag multipliers, exclusions, or special outcomes.
For example, Dense Fossils heavily favour defence modifiers and prevent Life
modifiers. Recompute the pool after every fossil in a resonator: multiplying a
target tag also multiplies every competing modifier with that tag.

### Harvest

Harvest crafts reforge or modify items using the tag or operation in their
current wording. Some respect crafted metamods and some operations have special
constraints. Verify the exact current craft rather than transferring rules
from an older league.

### Crafting Bench And Metamods

- A normal bench craft adds one crafted modifier and occupies its affix side.
- `Can have up to 3 Crafted Modifiers` is itself a suffix and counts toward the
  three crafted modifiers.
- `Prefixes Cannot Be Changed` is a suffix.
- `Suffixes Cannot Be Changed` is a prefix.
- `Cannot roll Attack Modifiers` and `Cannot roll Caster Modifiers` are
  suffixes.
- A temporary bench modifier can block a mod group or fill a side, but only if
  the next currency respects that state.

Patch 3.29 also added bench options that reroll one modifier or three modifiers
on a rare item. Treat their selected modifiers as random until current game
wording or verified testing establishes a narrower rule.

## Eldritch Explicit Currency

| Dominant implicit | Chaos | Exalted | Annulment |
| --- | --- | --- | --- |
| Searing Exarch | rerolls prefixes | adds a prefix | removes a prefix |
| Eater of Worlds | rerolls suffixes | adds a suffix | removes a suffix |

The higher-tier Eldritch implicit determines dominance. Equal tiers provide no
dominance. Standard Eldritch explicit currency requires a compatible
non-influenced armour item; conventional influence and Eldritch influence are
not interchangeable.

## Veiled, Influence, And Fracture Methods

| Method | Effect | Critical warning |
| --- | --- | --- |
| Veiled Exalted Orb | removes a random modifier, then adds a random Veiled modifier | identify the eligible removable mods first |
| Veiled Chaos Orb | rerolls a rare item with a random Veiled modifier | not a side-preserving slam |
| Fracturing Orb | fractures one random eligible explicit modifier on a sufficiently filled rare | other modifiers can be selected; failure is permanent for that base |
| Influenced Exalted Orb | adds its influence and an eligible influenced modifier | cannot be used on every influenced or fractured state |
| Awakener's Orb | consumes a donor, moves one influence modifier from each item, then rerolls remaining affixes on the target base | donor is destroyed; isolate exactly one desired influence mod on each item |
| Orb of Dominance | removes one influenced modifier and upgrades another eligible influenced modifier | needs multiple influence modifiers; the wrong one can be removed |

## Beastcrafting, Recombinators, And Corruption

- A beastcraft imprint records a magic item and can restore that recorded magic
  state after a failed later step. It does not snapshot a rare item.
- Splitting creates separate items under the current split rules and marks them
  split; verify which affixes and links can transfer.
- Recombinators consume two compatible items and produce one probabilistic
  combination. Base selection, affix counts, mod groups, exclusive modifiers,
  and special rules make simple independent-weight multiplication invalid.
- Vaal and other corruption methods are irreversible unless a specifically
  compatible tainted method exists. Confirm sockets, links, and finished
  explicit modifiers first.

## Allflame Crafting In 3.29

[Official 3.29 overview and patch notes](https://www.pathofexile.com/allflame)

Allflame Crafting combines an item, an eligible crafting currency, and Dead
Man's Sulphur. It applies the chosen action to the same original item multiple
times, previews the ghostly outcomes, and lets the player keep one. Ship
upgrades can increase the normal outcome count up to four.

Each use adds Intangibility. Increasing Intangibility reduces future outcome
counts and can collapse a craft to one outcome, so do not treat every future
Allflame operation as four guaranteed previews. Record the item's current
Intangibility and the UI's offered outcome count before calculating odds.

The underlying currency still controls what changes. An Allflame Eldritch
Annulment is an Eldritch Annulment performed through Allflame previews; it does
not become a generic annul. Reconfirm dominance and eligible side first.

Ducats provide separate named effects and should be evaluated from their exact
current item text. Do not generalise one Ducat's socket, enchantment, tattoo,
or modifier behavior to another.

## Probability Model

For one random eligible modifier selection:

```text
p = combined weight of acceptable outcomes / total eligible weight
```

For `n` independent previews from the same original state:

```text
chance of at least one success = 1 - (1 - p)^n
```

If the craft has probability `c` of collapsing to one preview and otherwise
offers `n` previews:

```text
effective chance = c*p + (1-c)*(1-(1-p)^n)
```

For `k` repeated crafts with effective per-craft chance `q`:

```text
chance within k crafts = 1 - (1 - q)^k
expected crafts = 1 / q
```

Use the calculator:

```bash
python3 scripts/craft_odds.py --chance 10 --choices 4 --attempts 5
python3 scripts/craft_odds.py \
  --success-weight 1000 --total-weight 61000 \
  --choices 4 --single-choice-chance 20 --cost-per-craft 12
```

The weight form is exact only for one draw from the supplied eligible pool.
Use Craft of Exile's calculator or simulator, or an explicit enumeration, for:

- Alteration outcomes with variable prefix/suffix counts;
- a rare reforge requiring two or more modifier families;
- fossils changing several competing weights;
- dependent affixes or shared mod groups;
- Awakener, recombinator, fracture, unveil, conflict, or corruption outcomes.

State every assumption with the result: base, item level, influence, occupied
affixes, blocked mod groups, crafting method, success definition, outcome
count, Intangibility behavior, and whether choices are independent.
