---
name: ed-poe-build-advisor
description: Review and improve Path of Exile 1 builds using Path of Building exports, pasted item text, screenshots, trade listings, or conversational build state. Use for PoB analysis, gear-upgrade prioritization, item-level 86 affix availability, modifier weights, crafting-method effects and outcome probabilities, prefix/suffix and Eldritch-currency safety, resistance or attribute checks, CI and other defensive constraints, gem/socket decisions, and current-market buy-versus-craft comparisons.
---

# Ed PoE Build Advisor

Give short, stateful, evidence-backed advice. Treat every item click as a state
transition: identify what is protected, what can change, the desired outcome,
and the stopping condition before recommending currency.

## Establish The Current Build

1. Confirm Path of Exile 1, the current patch or league, and the user's main
   skill when they are not already clear.
2. Use the newest PoB or item artifact as authoritative. Do not silently mix an
   older snapshot with later gear changes.
3. Decode compressed PoB text with `scripts/decode_pob.py` when necessary.
4. Record the constraints that affect the requested slot:
   - life, low-life, or CI;
   - main damage type and scaling tags;
   - equipped base, explicit modifiers, implicits, quality, and item level;
   - elemental resistances and overcaps;
   - total and required attributes;
   - armour, evasion, ES, suppression, block, recovery, and ailment defenses;
   - socket, reservation, and gem requirements.
5. Recalculate constraints after removing the equipped item. A current total
   can conceal an attribute or resistance supplied by the item being replaced.

## Verify Current Data

Browse for current patch mechanics, affix ranges, crafting-currency behavior,
trade prices, and recommendations that depend on the live economy. Prefer:

1. official GGG patch notes and item descriptions;
2. the current PoE Wiki for mechanics;
3. current PoEDB modifier tables;
4. the official trade site or another current market source for prices.

State when a conclusion is an inference. Do not carry affix values, league
mechanics, prices, or crafting odds forward from memory when they are cheap to
verify.

Use [ilvl-86-affixes.md](references/ilvl-86-affixes.md) as a patch-stamped
starting point for common item-level 86 bases. Recheck PoEDB when the current
patch differs from the reference snapshot or the target modifier is not listed.

## Evaluate An Upgrade

Compare the candidate with the equipped item, not with an abstract ideal.

- Separate local item defenses from global character scaling.
- Calculate the lost attributes and resistances before crediting the new item.
- Treat life as dead on CI unless another verified mechanic consumes it.
- Treat chaos resistance as irrelevant to CI unless the build has a mechanic
  that changes chaos immunity.
- Credit life regeneration as ES recovery only after verifying the build's
  conversion mechanism.
- Keep block and suppression separate; they are different defensive rolls.
- Quantify the delta and opportunity cost before calling an item an upgrade.

Use actual modifier values and final item totals. Do not trust a tier label
without matching it to the current item class, modifier family, and patch.

## Guide A Craft

Read [item-crafting.md](references/item-crafting.md) before advising on a rare
item craft, Eldritch manipulation, influence, annulment, or market valuation.
Read [crafting-methods.md](references/crafting-methods.md) before choosing a
crafting currency or claiming that an operation is deterministic. Read
[ilvl-86-affixes.md](references/ilvl-86-affixes.md) when the advice depends on
modifier tiers, item level, modifier weight, or the ordinary versus special
modifier pool.

For each stage:

1. Name the desired modifier families and whether each is a prefix, suffix, or
   implicit.
2. Give a minimum keep threshold and an aspirational threshold.
3. Count occupied and open prefixes and suffixes.
4. Explain exactly what the next currency can change.
5. Stop after a material hit and reassess before another irreversible click.
6. Prefer deterministic or side-locked operations over random annulment.
7. Set a spending cap appropriate to the quality of the protected affixes.

Never recommend a regular Annulment, Exalted, Chaos, fossil, essence, or
Eldritch currency without first checking which modifiers it can affect.

## Calculate Crafting Odds

Define success before calculating it: exact modifier family, minimum tier,
number of acceptable outcomes, and whether other affixes must also survive.
Then establish:

- the crafting method and current item state;
- the eligible modifier pool and verified current weights;
- the number of independent choices or previews;
- any chance to collapse the result to a single choice, such as Allflame
  Intangibility;
- the number and cost of attempts.

Use `scripts/craft_odds.py` when the method can be modeled from one verified
per-choice probability or a single weighted selection. Report the per-choice
chance, effective chance per craft, expected attempts, and a useful confidence
point. For example:

```bash
python3 scripts/craft_odds.py --chance 10 --choices 4 --attempts 5
python3 scripts/craft_odds.py --success-weight 1000 --total-weight 61000 \
  --choices 4 --single-choice-chance 20 --attempts 10
```

Do not present simple weight division as an exact answer for a multi-affix
craft, variable-affix-count reroll, fossils, essences, tag interactions,
blocking, or mutually exclusive modifier groups. Use the current Craft of
Exile calculator or simulator for those cases and state the assumptions. Treat
preview choices as independent only when the current mechanic actually draws
them independently from an unchanged pool.

## Communicate Interactively

- Lead with `keep`, `reroll`, `buy`, `sell`, or the exact next action.
- Give the reason in one or two concrete comparisons.
- Ask for the new result after one meaningful random step.
- Correct earlier assumptions explicitly when new item text or PoB evidence
  contradicts them.
- Distinguish an acceptable temporary item from a worthwhile finished item.

Avoid long generic crafting recipes when the user is already at a specific
step. Tell them the next safe click and the condition that should stop them.

## PoB Decoding

Run:

```bash
python3 scripts/decode_pob.py /path/to/pob-code.txt
```

Pipe the XML into `rg` for focused inspection. Do not expose the full decoded
build when only a few stats or item lines are needed.
