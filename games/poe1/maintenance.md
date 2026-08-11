# PoE Knowledge Maintenance

Apply this audit whenever the PoE skill receives a material knowledge update.
Do not wait for one giant cleanup.

## Keep Stable And Patch-Specific Knowledge Separate

- Keep reasoning workflows, PoB intake, state accounting, and safety rules free
  of patch numbers when the concepts are stable.
- Patch-stamp modifier values, item-level requirements, currency behavior,
  league mechanics, trade assumptions, and specific crafting routes.
- Update a verification date only for claims actually rechecked.
- Do not hard-code market prices; record how to query and compare them live.

## Source Order

Prefer current sources in this order:

1. official GGG patch notes, league pages, and item wording;
2. current Path of Building Community behavior for calculations and exports;
3. current PoE Wiki mechanics;
4. current PoEDB modifier tables;
5. Craft of Exile for eligible-pool calculation and simulation;
6. official trade listings and currency exchange for prices.

State when a recommendation is inferred from several sources. Do not copy a
crafting rule forward from an older patch merely because the currency name is
unchanged.

## Reorganize When A Trigger Fires

Split or move material when any of these is true:

- one document exceeds roughly 200 lines and contains separable concerns;
- three or more paragraphs describe one equipment target inside a broad affix
  reference;
- the same rule appears in more than one detailed document;
- a directory gains enough files that the main `SKILL.md` routing is unclear;
- patch-specific tables obscure stable decision guidance;
- a new build archetype needs different damage or defense assumptions.

Keep `SKILL.md` as the direct router. Every maintained reference must be linked
from it with a clear condition for reading it. Avoid reference chains in which
an agent must discover a file only through another reference.

## Equipment Guide Rules

- Add a guide under `crafting/equipments/` when the target has a distinct base,
  affix set, build purpose, or crafting sequence.
- Start from `crafting/equipments/guide-template.md`.
- Keep shared currency behavior in `crafting/methods.md` and shared probability
  math in `crafting/probability.md`.
- Move repeated build evaluation back into the relevant file under `build/`.
- Preserve one source of truth for modifier ranges and link to it rather than
  duplicating full tables.

## Validation After Reorganization

1. update every path in `SKILL.md`, repository indexes, and related references;
2. search for old paths and orphaned files;
3. run `quick_validate.py` on the skill;
4. run each touched script and its negative cases;
5. run `git diff --check` and the repository secret scan;
6. forward-test the intake, defense, damage, attribute, and crafting routes when
   an isolated validation surface is available;
7. publish through the second-brain feature-branch and PR workflow.
