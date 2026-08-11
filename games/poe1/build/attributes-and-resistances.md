# Attributes And Resistances

Read `intake.md` first and require the latest PoB for personalized advice.
Solve requirements against the proposed final gear set, not the currently
equipped totals.

## Calculate The Real Deficit

For Strength, Dexterity, and Intelligence:

```text
remaining after swap = current total - attribute on removed items
deficit = max(0, highest enabled requirement - remaining after swap)
```

Repeat the calculation for fire, cold, lightning, and any relevant chaos
resistance using uncapped values. Include resistance penalties and the content
the user plans to run.

Check every enabled gem at its intended level, equipment requirement, support,
alternate gem, and weapon swap. A gem the user plans to level later can create
a future requirement even when the current PoB is legal.

## Choose Where To Solve It

Use the least expensive flexible source that does not consume a critical affix:

1. temporary passive or attribute mastery while changing gear;
2. one efficient ring, amulet, belt, jewel, tattoo, or cluster source whose
   current-patch behavior is verified;
3. a bench craft on an otherwise finished item;
4. a natural or Essence attribute suffix when the slot can support it;
5. a more expensive global gear reallocation only when it improves several
   constraints together.

Amulets and rings often carry attributes efficiently, but they also compete
with damage, resistance, curse, and other valuable suffixes. Belts can solve
resistances and Strength but do not all share the same natural Intelligence
pool. Verify the exact base and item class before planning a suffix.

## Plan The Swap Safely

- Include attributes and resistances on the item being removed.
- Preserve enough overcap for the user's mapping modifiers and debuffs when
  that matters to the goal.
- Leave a small attribute buffer for gem leveling and future swaps; avoid paying
  heavily for unused overcap.
- Prefer fixing broad requirements on stable slots before crafting a premium
  item whose suffixes are more valuable.
- When buying several items, solve the full set together instead of forcing
  each slot to be independently capped.

For CI, Intelligence can add defensive value beyond meeting requirements, but
separate that global value from the local ES displayed on an item.

## Report The Answer

Show:

- current, required, and post-swap value for each relevant attribute;
- uncapped resistance before and after the complete swap;
- the cheapest temporary fix;
- the preferred finished allocation and which affix slots it consumes;
- any gem that must remain below maximum level until the fix is equipped.

Do not say an item is wearable or resistances remain capped without performing
the subtraction for every removed item in the proposed swap.
