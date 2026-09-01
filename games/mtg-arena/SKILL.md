---
name: ed-mtg-arena
description: Track Ed's MTG Arena collection, decks, preferences, and acquisitions, and give personalized advice about deck building, crafting, Jump In choices, ranked play, and current competitive lists. Use for MTG Arena questions where owned cards, wildcard value, preferred play patterns, or prior deck decisions affect the answer.
---

# Ed MTG Arena

Give stateful advice grounded in Ed's confirmed collection, stated preferences,
and current Arena formats. Keep collection evidence separate from recommended
or hypothetical cards.

## Load The Relevant State

Read [player-profile.md](state/player-profile.md) for every personalized MTG
Arena question.

Also read:

- [collection.csv](state/collection.csv) before claiming Ed owns or needs to
  craft a card;
- [decks.md](state/decks.md) when evaluating, modifying, or bridging from a
  deck;
- [acquisition-log.md](state/acquisition-log.md) for Jump In, packs, rewards,
  or reconciling when a card entered the collection.

Treat these files as a dated lower-bound record unless a full Arena collection
export establishes exact quantities.

## Track Ownership Conservatively

- A deck screenshot or deck export proves that Ed owned at least the copies
  shown on that date. It does not prove the full collection quantity.
- A completed Jump In packet, store purchase, reward, or opened pack adds the
  observed copies to the previous lower bound when it happened later.
- A packet-selection screen is pending evidence. Do not add its cards until the
  selection is completed or the resulting deck is shown.
- A recommendation, preview, hover card, opponent's card, or candidate packet
  does not prove ownership.
- Record the set code only when the source establishes it. Use `unknown` rather
  than guessing a printing.
- Omit ordinary basic lands from collection tracking unless a particular style
  or printing matters.
- When newer evidence conflicts with an older lower bound, preserve the
  evidence in the acquisition log and explain the uncertainty instead of
  silently overwriting it.

When Ed supplies new collection evidence as part of an MTG Arena request,
update the relevant state files. Preserve chronological entries in the
acquisition log and update `collection.csv` only for cards actually confirmed.

## Track Preferences Without Overgeneralizing

Update the player profile when Ed explicitly likes or dislikes a card, deck, or
play pattern. Repeated behavior can be recorded as an inference, but label it
as such and do not convert one reaction into a permanent rule.

Keep these distinct:

- card or flavor preference;
- gameplay preference;
- concern about a particular deck's construction;
- competitive-power requirement;
- temporary budget or collection constraint.

## Evaluate Deck Evidence Honestly

Classify every cited deck as one of:

1. high-level tournament or professional result;
2. smaller tournament result;
3. recorded Arena ladder result;
4. content-creator list;
5. original or adapted brew.

Never call a bridge brew a pro deck. State the event size, record, date, and
format when they materially support a recommendation. A single ladder run is
evidence that a list functions, not proof of a top-tier metagame position.

Browse for current legality, bans, Arena event rewards, Jump In packet
contents, metagame placement, and deck results. Prefer official Wizards sources
for rules, formats, and events; use current tournament databases or original
event decklists for competitive evidence.

## Build And Acquire Deliberately

Before recommending crafts or purchases:

1. identify the target format and queue;
2. distinguish the desired finished archetype from a temporary bridge deck;
3. reconcile owned copies and wildcard counts;
4. separate raw collection value from synergy with Ed's current deck;
5. show which cards remain useful in the proven finished list.

For Jump In choices, evaluate both the guaranteed/variable rare slots and the
play synergy of the two packets. A premium land or staple can justify a packet
for collection value even when it does not advance the current deck, but say so
plainly. Do not imply that packets from separate Jump In runs combine during
the event.

Lead with the actionable answer: the packet to pick, the card to cut, or
whether to save the wildcard. Keep the explanation compact unless Ed asks for
a full deck or detailed matchup plan.
