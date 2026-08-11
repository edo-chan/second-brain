# PoE 1 Crafting Probability

Snapshot: Path of Exile 1, patch 3.29, verified 2026-08-10.

Define success and establish the eligible pool before calculating an outcome.
Modifier weight is relative, not automatically a percentage.

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

Use the calculator from the `games/poe1` directory:

```bash
python3 scripts/craft_odds.py --chance 10 --choices 4 --attempts 5
python3 scripts/craft_odds.py \
  --success-weight 1000 --total-weight 61000 \
  --choices 4 --single-choice-chance 20 --cost-per-craft 12
```

The weight form is exact only for one draw from the supplied eligible pool.
Use Craft of Exile's current calculator or simulator, or an explicit
enumeration, for:

- Alteration outcomes with variable prefix/suffix counts;
- a rare reforge requiring two or more modifier families;
- fossils changing several competing weights;
- dependent affixes or shared mod groups;
- Awakener, recombinator, fracture, unveil, conflict, or corruption outcomes.

State every assumption with the result: base, item level, influence, occupied
affixes, blocked mod groups, crafting method, success definition, outcome
count, Intangibility behavior, and whether choices are independent. Report the
per-craft chance, expected attempts, confidence points, expected cost, and the
price of the closest finished trade alternative when relevant.
