# Build Defense And Tankiness

Read `intake.md` first and require the latest PoB for personalized advice.
Tankiness is not one number: identify the actual failure mode, then strengthen
the weakest relevant layer without breaking damage, attributes, reservation, or
recovery.

## Diagnose The Failure Mode

| Symptom | Inspect first | Common solution families |
| --- | --- | --- |
| physical one-shot | physical maximum hit, armour at relevant hit size, endurance charges, flat physical reduction, damage taken conversion | more pool, physical mitigation, reliable guard skill |
| elemental one-shot | elemental maximum hits, maximum resistance, penetration exposure, conditional buffs | more pool, maximum resistance, suppression or spell block |
| repeated attacks | evasion, attack block, recovery on block/hit, stun | avoidance plus recovery and stun protection |
| repeated spells | spell suppression, spell block, maximum resistance, recovery | reliable spell layer plus recovery |
| damage over time | regeneration, leech applicability, recharge interruption, ailment and ground-effect handling | sustained recovery, ailment immunity, movement |
| death after guard or flask expires | uptime assumptions and automation | permanent layer or realistic uptime |
| cannot recover after a hit | regen, leech, recharge delay, recharge interruption, recovery rate | add or accelerate the build's actual recovery mechanism |

Ask what killed the character when the PoB alone cannot distinguish these.

## Audit In Order

1. **Eligibility:** correct life, low-life, CI, MoM, ward, or hybrid model.
2. **Baseline:** capped required resistances, enough attributes, legal gem and
   reservation setup, and no disabled build-enabling item.
3. **Pool:** life, ES, or the actual combined resource protecting the build.
4. **Mitigation:** armour, maximum resistance, physical reduction, damage taken
   conversion, suppression, or another hit-reduction layer.
5. **Avoidance:** evasion, attack block, spell block, dodge where applicable,
   and blind or accuracy interaction.
6. **Recovery:** regeneration, recharge, leech, recoup, gain on block/hit, and
   recovery rate.
7. **Control and immunity:** stun, freeze, shock, ignite, bleed, corrupted
   blood, poison, curses, crit reduction, and movement.
8. **Uptime:** charges, flasks, guard skills, conditional ascendancy effects,
   and enemy debuffs.

Do not recommend several weak partial layers when one reliable completed layer
would solve the observed problem.

## Read PoB Metrics Carefully

- Compare physical and each elemental maximum hit separately; total EHP can
  hide a weak damage type.
- Armour's reduction changes with hit size. Do not quote the character-sheet
  percentage as universal physical mitigation.
- Block and evasion prevent some hits; they do not raise the damage survived
  when a hit gets through.
- Suppression reduces eligible spell hit damage when it succeeds; it is not
  spell block.
- Recovery does not prevent a one-shot, and maximum hit does not prove the
  build can survive sustained damage.
- Conditional flasks, guard skills, charges, and enemy states count only at
  credible uptime.

## CI Checklist

- Treat life and ordinary life rolls as no defensive value unless a verified
  mechanic explicitly consumes them.
- Treat chaos resistance as irrelevant to direct chaos damage while CI grants
  chaos immunity; still verify special mechanics instead of generalising.
- Count Intelligence as global ES scaling, not local item ES.
- Inspect recharge start, interruption, regeneration, leech, and recovery rate
  separately.
- Verify stun handling because life-based stun calculations can be dangerous
  for CI builds without a solution.
- Recalculate ES and attributes after removing the item being replaced.

## Rank Defensive Upgrades

For each candidate, show:

1. observed weakness and baseline metric;
2. proposed change and the exact resource it consumes;
3. new maximum-hit, recovery, avoidance, and pool values from the same PoB
   configuration;
4. damage, socket, resistance, attribute, and movement tradeoffs;
5. current purchase or expected crafting cost;
6. whether the gain is permanent or conditional.

Offer a cheap repair, a balanced upgrade, and an aspirational option when the
budget supports all three. Prioritise the cheapest change that fixes the actual
failure mode rather than the largest isolated EHP number.
