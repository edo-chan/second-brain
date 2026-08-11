# Personalized Build Intake

Require a fresh [Path of Building Community](https://github.com/PathOfBuildingCommunity/PathOfBuilding)
export before giving personalized build, gear, passive-tree, gem, or upgrade
advice.

## Hard Gate

If the current conversation does not contain the latest full PoB export code or
an attached file containing it, ask for it and stop before recommending changes:

> Please paste or attach your latest full Path of Building export code. In PoB,
> open Import/Export Build and copy the long export string. Also tell me your
> league, approximate budget, and whether the main problem is one-shots,
> sustained damage, recovery, damage, attributes, or something else.

Prefer the raw compressed export content over a third-party paste URL. Do not
assume an older PoB elsewhere in the thread still matches the equipped build.

A pure mechanics question may be answered without a PoB when the answer does
not claim to fit the user's character. A question about a single crafting click
may use complete item text, but do not call the item a build upgrade without the
current PoB.

## Minimum Inputs

- latest raw PoB export or attached export file;
- Path of Exile 1 patch and league;
- budget in the currency the user actually uses;
- content goal: mapping, bosses, invitations, delving, hardcore, or another
  target;
- observed problem, including what kills the character or where damage feels
  insufficient;
- any item being replaced or crafted, copied with advanced modifier text.

Ask only for missing inputs that materially change the recommendation.

## Decode And Snapshot

From the `games/poe1` directory, run:

```bash
python3 scripts/pob_snapshot.py /path/to/pob-code.txt
python3 scripts/decode_pob.py /path/to/pob-code.txt > /tmp/pob.xml
```

Use the snapshot for orientation and the XML for exact skills, items, passive
specs, item sets, and configuration. Keep the decoded XML temporary; do not add
the user's build to the repository.

## Validate The PoB Before Comparing

Confirm:

1. class, ascendancy, level, active item set, and active skill set;
2. intended main skill and its selected skill part;
3. enabled gems, auras, curses, guard skills, flasks, and alternate qualities;
4. life, ES, mana, armour, evasion, block, suppression, resistances, attributes,
   recovery, maximum hits, and relevant damage output;
5. configuration assumptions such as charges, enemy type, Wither stacks,
   exposure, curses, shock, flasks, nearby enemies, and conditional buffs;
6. whether every assumed effect has realistic uptime in the stated content.

Do not compare two PoBs with different enemy, configuration, flask, or skill
settings and attribute the entire difference to one item.

## Establish A Baseline

Record a compact baseline before modifying anything:

- primary skill and damage component;
- current damage under an honest boss configuration;
- life or ES pool and physical, fire, cold, lightning, and chaos maximum hits;
- attack block, spell block, suppression, armour, evasion, resistances, and
  maximum resistances;
- recovery sources and their conditions;
- current versus required Strength, Dexterity, and Intelligence;
- uncapped resistance overage;
- open sockets, reservation headroom, and gear affix pressure.

This baseline is the control for every proposed upgrade.
