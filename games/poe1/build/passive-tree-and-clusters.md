# Passive Tree And Cluster Jewels

Read `intake.md` first and require the latest PoB. Evaluate passive changes in a
duplicate tree under the same skill and configuration.

## Audit The Existing Tree

Check:

- travel points and inefficient loops;
- masteries whose condition is not satisfied;
- keystones that conflict with gear or another mechanic;
- life nodes on CI or other nodes outside the actual resource model;
- temporary attribute or resistance nodes that can now be released;
- jewel sockets whose current jewel does not justify the pathing;
- cluster entry, travel, and notable point cost;
- conditional charge, curse, ailment, or nearby-enemy assumptions.

Do not judge a notable only by its text. Include every travel point and the
value of the nodes removed to reach it.

## Compare Point Efficiency

For a candidate allocation, report:

```text
net benefit per point =
  (new build value - removed allocation value) / net points spent
```

Use the metric relevant to the goal: sustained boss damage, a weak maximum hit,
ES or life, recovery, attribute repair, reservation, or quality of life. A
single blended score can hide tradeoffs.

## Medium And Large Clusters

Before crafting or buying a cluster, verify:

- base type and enchantment family;
- item level required by every target notable;
- passive count and total pathing cost;
- prefix or suffix side and mod group of each notable;
- whether duplicate notables stack and whether their relevant effects can
  benefit twice;
- socket position and which notables are encountered first in PoB;
- price of the finished layout versus alteration, augmentation, Regal, fossil,
  or other expected craft cost.

Two copies of a notable may both allocate, but a binary or non-stacking effect
can still make the second copy poor. Confirm the exact current wording and PoB
delta instead of assuming every line doubles.

## Produce A Respec Plan

Give an ordered, legal transition:

1. temporary attributes or resistances needed before gear swaps;
2. points to remove;
3. path and sockets to allocate;
4. jewel or cluster to equip;
5. final stats to verify;
6. refund points and currency required.

Do not propose a final tree that becomes illegal halfway through the user's
actual gear and gem transition.
