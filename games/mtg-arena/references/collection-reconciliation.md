# Collection Reconciliation

Read the state files required by the MTG skill before updating ownership or
quoting a craft cost. Keep desired deck contents, dated collection snapshots,
and completed acquisitions distinct.

## Establish What The Evidence Shows

- An imported or exported deck is a list of requested copies. Arena permits
  imported decks with missing cards; the list alone does not prove ownership.
  See Wizards' [deck-import instructions](https://mtgarena-support.wizards.com/hc/en-us/articles/360049857771-Importing-a-Deck).
- A collection view with readable owned quantities, an explicit confirmation
  from Ed, or a completed acquisition can establish owned copies. An ambiguous
  deck-builder screenshot establishes only the visible configuration.
- Record the source, date, quantity, and whether it shows a snapshot or a new
  acquisition. Distinguish the event date from the date it was reported.
- Confirm that an acquisition credited playable copies. A card style, preview,
  recommendation, or uncompleted choice does not add copies.

When ownership affects a craft decision and the screenshot is ambiguous, ask
for the missing owned quantity or collection view. Continue evaluating the
deck's structure while that evidence is missing.

## Reconcile Without Double Counting

1. Locate the latest supported quantity and its evidence date for the card.
   Check the acquisition log for events already included in that quantity.
2. For a new owned-copy snapshot of `n`, the lower bound becomes the greater of
   the existing supported minimum and `n`; do not add two snapshots together.
3. For a distinct completed acquisition of `k` copies after the baseline, add
   `k` only if it has not already been counted or included in a later snapshot.
   Repeated images or reports of the same reward are one event.
4. If an acquisition predates the baseline, or overlap cannot be resolved,
   preserve the evidence without adding it again. Ask only if the uncertainty
   changes the next decision.
5. An exact quantity requires complete evidence for its stated scope and date.
   A later partial view cannot establish that the rest of the collection is
   absent. Preserve conflicting evidence and explain it instead of silently
   reducing or inflating the recorded quantity.

For example, an owned snapshot showing two copies followed by a confirmed new
reward of one supports three. A screenshot of that same reward adds nothing;
a later owned snapshot showing three still supports three.

Record set codes only when established; otherwise use `unknown`. Do not treat
an unknown-printing row as extra copies when later identifying its printing.
Omit ordinary basic lands unless a particular style or printing matters.
Retain dated historical records when their original evidence is unavailable;
do not invent a correction to them from a new general rule.

## Turn A Target List Into A Craft Decision

Confirm format, queue, main deck and relevant sideboard, then aggregate required
copies by card. Distinguish playable copies across eligible printings from a
request for a particular cosmetic or printing; verify unusual version or
legality questions under the MTG skill's current-source rules.

With exact owned quantities, the missing count is
`max(0, required - owned)`. With only a lower bound, that calculation is an
upper bound on missing copies, not an exact craft bill. A card absent from the
tracker has unknown ownership. Show confirmed overlap, unresolved quantities,
and any resulting upper-bound cost before requesting an exact collection check.

Check the intended list's totals and current legality before recommending a
craft. Use current wildcard balances for affordability. Keep a proposed craft
in the plan until Ed confirms completion; then reconcile the acquisition once.
