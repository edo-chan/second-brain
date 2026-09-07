# PoB Comparison Evidence

Apply [intake.md](intake.md) first. This guide governs comparisons after the
fresh-export requirement is met; it does not relax that requirement.

## Separate Stored Values From Calculated Results

`decode_pob.py` decodes the export. `pob_snapshot.py` reads serialized
`Build/PlayerStat` values and selected build fields. Neither script executes
the Path of Building calculation engine.

Label evidence according to what actually produced it:

- **Supplied:** the latest export, item text, or result shown by Ed.
- **Parsed:** a value read from the export, including its stored statistics.
- **Recomputed:** a result obtained by running the stated build and configuration
  through a compatible Path of Building Community calculation engine.
- **Inferred:** a qualitative expectation or a separate calculation with
  explicit assumptions.

Editing an item, skill, or passive in XML does not update its stored
`PlayerStat` values. Unchanged stored DPS after such an edit is not evidence of
zero gain; changed item text is not evidence of a calculated gain either.
Missing statistics mean unavailable, not zero.

## Hold The Comparison Constant

1. Preserve the supplied export as the baseline. Confirm active item set,
   passive specification, skill set, main skill, and selected skill part.
2. Record the PoB version, game patch, target content, and relevant assumptions:
   enemy, charges, flasks, ailments, curses, stacks, guard skills, and uptime.
3. Create a separate candidate and change one item, passive allocation, gem, or
   other identified decision at a time. State dependencies that make a change
   inseparable from a package; compare that whole package honestly.
4. Recalculate baseline and candidate with the same compatible PoB version and
   shared configuration. Correct an unrealistic baseline assumption on both
   sides before crediting any gain to the candidate. Model newly enabled
   conditional effects explicitly and report their required uptime.
5. Compare damage and defenses alongside recovery, attribute and resistance
   requirements, reservation, sockets, movement, and total cost. A larger DPS
   number does not establish that the resulting character works.

Do not attribute the difference between exports to an item when the skill,
enemy, configuration, or calculation version also changed. Isolate the change
or report that the available comparison cannot isolate its effect.

## Report The Evidence And Its Limit

For a numerical result, show the baseline and candidate values, the absolute
change, and the percentage only when the baseline makes that meaningful. Name
the calculation source and material assumptions. Distinguish saved results
supplied by Ed from calculations you actually ran.

If no compatible calculation engine or freshly calculated comparison is
available, explain what the item and baseline establish qualitatively. Request
the missing PoB calculation when it decides the verdict; do not fabricate a
DPS, maximum-hit, or effective-health delta from parsed XML.

A trade candidate or hypothetical craft remains proposed gear until Ed confirms
the change. After a completed upgrade, obtain the updated export and rerun the
relevant baseline before continuing the roadmap. Keep exports and comparison
artifacts temporary as required by intake.
