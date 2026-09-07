---
name: ed-games-router
description: Select Ed's MTG Arena or Path of Exile 1 guidance and the evidence needed for a live decision, personalized recommendation, or mechanics explanation. Use when entering game-advice work or switching between game modes.
---

# Ed Games Router

Apply the [root guidance](../SKILL.md), then select the game and the decision
being made. Keep the requested game's rules, state, and economy separate.

- **MTG Arena:** use [ed-mtg-arena](mtg-arena/SKILL.md). It routes collection,
  deck, acquisition, Draft, and live-play evidence.
- **Path of Exile 1:** use [ed-poe-build-advisor](poe1/SKILL.md). It routes
  current PoB intake, character diagnosis, gear comparison, and crafting.

Read the selected skill completely and follow its conditional references. Do
not load the other game's state. A direct invocation of either game skill can
continue through its own router without restarting discovery.

## Match Evidence To The Decision

- For a live pick, turn, or crafting step, establish the current visible state
  and lead with the next action. Follow the game's stopping rule before
  assuming a random result or completed action.
- For a personalized plan, load the current collection or build evidence and
  the user's goal and constraints. Request missing evidence only when it
  changes the recommendation or the owning skill requires it.
- For a general mechanics explanation, answer at that scope. It does not
  establish ownership or show that a change fits the user's current build.
- Verify patch, legality, event, and market facts under the game's source
  policy. Keep snapshot dates and uncertain evidence visible when relevant.

For tutoring about game probability or decision theory, add the
[learning router](../learning/SKILL.md). The game skill still owns the facts
and personalization requirements. Add [figure design](../presentation/ed-figure-design/SKILL.md)
only when a rendered figure is part of the requested explanation.
