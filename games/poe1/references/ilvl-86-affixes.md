# PoE 1 ilvl 86 Affix Reference

Snapshot: Path of Exile 1, patch 3.29, verified 2026-08-10.

Use this as the fast build-centric reference for ordinary rare items. Recheck
PoEDB after a patch changes item modifiers. Influence, Essence, Delve,
Incursion, Veiled, Synthesised, Corrupted, Foulborn, and Eldritch modifiers use
separate pools unless a row explicitly says otherwise.

Modifier weight is relative, not a percentage. It becomes a direct probability
only when the craft selects exactly one modifier from the stated eligible pool:

```text
single-draw chance = successful eligible weight / total eligible weight
```

Mod groups, occupied affixes, item tags, metamods, fossils, and other crafting
rules can change the eligible pool.

## What ilvl 86 Actually Unlocks

- Pure-ES body armour and hybrid Armour/ES body armour can roll the natural
  101-110% local defence prefix at ilvl 86.
- Hybrid Armour/ES gloves, helmets, and boots do **not** get that body-only
  tier. Their best natural local percentage prefix is 92-100% at ilvl 84.
- Boots gain natural 35% movement speed at ilvl 86.
- Body armour gains 59-66% faster start of ES recharge at ilvl 86.
- Helmets gain 56-60 Intelligence at ilvl 85. Other eligible armour slots and
  rings stop at 51-55 Intelligence at ilvl 82.
- Intelligence and hybrid armour slots gain 36-38% increased ES recharge rate
  at ilvl 85.

Higher item level can add unwanted high-level modifiers to the pool. Buy ilvl
86 for a specific unlock, not because every craft is automatically better.

## Pure Energy Shield Body Armour

[Current modifier table](https://poedb.tw/us/Body_Armours_int) ·
[Twilight Regalia](https://poedb.tw/us/Twilight_Regalia)

Twilight Regalia has 262-302 base ES before quality. The three ordinary local
ES prefixes used for a high-ES rare are:

| Affix | Side | Top range | Min ilvl | Base weight |
| --- | --- | ---: | ---: | ---: |
| flat maximum ES | prefix | +91-100 | 75 | 1000 |
| increased ES | prefix | 101-110% | 86 | 1000 |
| increased ES plus stun/block recovery | prefix | 39-42% plus 16-17% | 78 | 1000 |

Useful ordinary suffixes include 59-66% faster start of ES recharge at ilvl
86 and 46-48% single elemental resistance at ilvl 84. A displayed flat ES
total can combine the pure flat prefix with a hybrid ES/mana or ES/life prefix;
inspect advanced modifier lines before assigning a tier.

For a local estimate, add the base ES and all local flat ES, then multiply by
quality plus all local increased-ES modifiers. Use the final displayed item ES
for purchase decisions because game rounding and combined affixes are easy to
misread.

## Armour/Energy Shield Gloves And Helmets

[Armour modifier families](https://poedb.tw/us/Armour) ·
[Paladin Gloves](https://poedb.tw/us/Gloves_str_int) ·
[hybrid helmets](https://poedb.tw/us/Helmets_str_int)

The ordinary three-prefix ceiling on gloves and helmets is:

| Affix | Side | Top range | Min ilvl | Base weight on hybrid base |
| --- | --- | ---: | ---: | ---: |
| flat Armour plus ES | prefix | +301-375 Armour, +73-80 ES | 79 | 1000 |
| increased Armour and ES | prefix | 92-100% | 84 | 1000 |
| increased Armour and ES plus stun/block recovery | prefix | 39-42% plus 16-17% | 78 | 1000 |

The +47 Armour/+22 ES family is only the 28-48 Armour/+13-22 ES tier. It is not
close to the 301-375 Armour/+73-80 ES top tier even when paired with a strong
percentage prefix.

Useful ordinary suffixes:

| Affix | Top range | Min ilvl | Notes |
| --- | ---: | ---: | --- |
| single elemental resistance | 46-48% | 84 | one suffix per element |
| Intelligence on gloves | +51-55 | 82 | hybrid-base weight 500 |
| Intelligence on helmet | +56-60 | 85 | helmet-only top tier |
| ES recharge rate | 36-38% | 85 | hybrid-base weight 500 |

For CI ED/Contagion gloves, prioritise the final displayed Armour/ES totals,
then the exact missing resistance, then Intelligence or recharge. Eldritch
implicits such as Chaos DoT multiplier or suppression are separate from these
explicit affixes.

## Armour/Energy Shield Boots

[Current hybrid boot table](https://poedb.tw/us/Boots_str_int)

Boots share the hybrid flat, percentage, hybrid-percentage, resistance,
Intelligence, and recharge tiers above. Natural 35% movement speed is an ilvl
86 prefix and competes with the three local-defence prefixes. Decide up front
whether the craft is a three-defence-prefix boot or a movement-speed boot.

## Crystal Belt

[Crystal Belt](https://poedb.tw/us/Crystal_Belt) ·
[current belt table](https://poedb.tw/us/Belts)

- implicit: +60-80 maximum ES;
- ordinary flat ES prefix: +48-51 at ilvl 80, weight 1000;
- ordinary single elemental resistance suffix: 46-48% at ilvl 84;
- ordinary belts do not naturally roll the standard Intelligence suffix;
- Deafening Essence of Spite guarantees +51-58 Intelligence as a suffix;
- bench-crafted attributes or Strength/Intelligence can preserve flexibility;
- Crusader influence can add 13-15% increased maximum ES at ilvl 82, but an
  influenced belt has a different pool and plan.

Do not spend premium prefix finishing on a low Crystal Belt implicit unless the
other affixes justify it.

## Rings

[Current ring table](https://poedb.tw/us/Rings)

| Affix | Side | Top ordinary range | Min ilvl | Base weight |
| --- | --- | ---: | ---: | ---: |
| flat maximum ES | prefix | +44-47 | 74 | 1000 |
| Intelligence | suffix | +51-55 | 82 | 1000 |
| cast speed | suffix | 13-16% | 30 | 800 |
| single elemental resistance | suffix | 46-48% | 84 | 1000 |

Deafening Essence of Woe guarantees +44-47 ES; Deafening Essence of Spite
guarantees +51-58 Intelligence. In 3.29, new Moonstone Rings have 7-10% cast
speed rather than the old ES implicit, so never price a current Moonstone as if
it still supplied implicit ES.

## Caster Staves For Chaos DoT

[Current staff table](https://poedb.tw/us/Staves) ·
[Chaos DoT multiplier tiers](https://poedb.tw/us/Damage_over_time_multiplier)

| Affix | Side | Top ordinary value | Min ilvl | Base weight |
| --- | --- | ---: | ---: | ---: |
| all Spell Skill Gems | prefix | +2 | 55 | 250 |
| all Chaos Spell Skill Gems | prefix | +4 | 77 | 100 |
| spell damage | prefix | 150-174% | 79 | verify live |
| Chaos DoT multiplier | suffix | +66-75% | 78 | 50 |
| cast speed | suffix | 44-49% | 83 | 1000 |

The ideal +2 all-spell, +4 chaos, and high spell-damage combination fills all
three prefixes. Chaos DoT multiplier and cast speed are suffixes. Because the
gem-level and multiplier weights are very low, calculate or simulate the exact
method instead of expecting a raw Chaos, fossil, or Essence reforge to land the
finished five-mod item.

## Special Pools To Keep Separate

- Warlord helmet +1 maximum Power Charge is an influenced prefix at ilvl 75
  with base weight 125. It is not an ordinary helmet affix.
- A conventional influenced item cannot also use normal Eldritch implicits.
- Veiled body armour block modifiers are prefixes: 8-9% attack block or 9-10%
  spell block before their lower bench-crafted versions.
- Fractured modifiers remain fixed through ordinary reforges but still occupy
  their prefix or suffix and mod group.
- Essence values may exceed or differ from natural tiers and must be identified
  as Essence modifiers.
