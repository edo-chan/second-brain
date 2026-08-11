# Upgrade Prioritization

Read `intake.md` first. Use one stable PoB baseline and rank improvements across
the whole character instead of optimizing the requested slot in isolation.

## Find The Binding Constraint

Classify the next upgrade as one of:

- build-enabling: requirements, caps, sockets, reservation, or mandatory item;
- survival repair: weakest maximum hit, recovery failure, ailment, stun, or
  unreliable uptime;
- damage repair: broken links, inaccurate configuration, missing multiplier,
  or weak weapon;
- quality of life: speed, area, duration, automation, flask uptime, or recovery;
- luxury: expensive improvement after the build's floor is already stable.

Fix build-enabling and survival blockers before luxury damage unless the user
explicitly accepts the risk.

## Compare Candidate Changes

For each candidate, keep the configuration constant and record:

| Field | Required evidence |
| --- | --- |
| change | exact item, passive, gem, flask, or configuration delta |
| benefit | PoB damage, maximum hit, pool, recovery, or requirement delta |
| cost | current purchase price or expected crafting cost and variance |
| lost value | removed affixes, sockets, attributes, resistances, or uptime |
| dependencies | other items or passives required for the change to work |
| confidence | verified calculation, current external data, or inference |

Do not rank by DPS percentage alone. A change that forces a second repair has a
higher total cost than its listing price.

## Produce A Roadmap

Return no more than five ordered actions unless the user asks for a full plan:

1. immediate free or cheap correction;
2. highest-value stable upgrade;
3. next constraint repair created by that upgrade;
4. medium-budget upgrade;
5. aspirational item or craft.

For each action, state the stopping condition and whether to buy or craft. When
crafting, hand off to the relevant guide under `crafting/equipments/` and pause
after each material random result.

Re-run the PoB after every completed upgrade. Do not keep using the original
roadmap after attributes, resistances, sockets, reservation, or gear roles have
changed materially.
