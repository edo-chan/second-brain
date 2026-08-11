#!/usr/bin/env python3
"""Calculate repeated-craft and multiple-preview success probabilities."""

from __future__ import annotations

import argparse
import math


DEFAULT_CONFIDENCE = (50.0, 90.0, 95.0, 99.0)


def percentage(value: str) -> float:
    parsed = float(value)
    if not 0 <= parsed <= 100:
        raise argparse.ArgumentTypeError("percentage must be between 0 and 100")
    return parsed


def positive_integer(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed


def at_least_one(chance: float, trials: int) -> float:
    return 1 - (1 - chance) ** trials


def effective_craft_chance(
    outcome_chance: float, choices: int, single_choice_chance: float
) -> float:
    multiple_choice_chance = at_least_one(outcome_chance, choices)
    return (
        single_choice_chance * outcome_chance
        + (1 - single_choice_chance) * multiple_choice_chance
    )


def attempts_for_confidence(chance: float, confidence: float) -> int | None:
    if chance == 0:
        return None
    if chance == 1:
        return 1
    return math.ceil(math.log1p(-confidence) / math.log1p(-chance))


def format_percent(chance: float) -> str:
    return f"{chance * 100:.4f}%"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Calculate outcome odds for repeated crafts and independent preview "
            "choices, including Allflame-style single-outcome collapse."
        )
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--chance",
        type=percentage,
        metavar="PERCENT",
        help="known success chance for one outcome, as a percentage",
    )
    source.add_argument(
        "--success-weight",
        type=float,
        help="combined weight of successful modifiers in one eligible draw",
    )
    parser.add_argument(
        "--total-weight",
        type=float,
        help="total eligible weight; required with --success-weight",
    )
    parser.add_argument(
        "--choices",
        type=positive_integer,
        default=1,
        help="independent outcomes previewed per craft (default: 1)",
    )
    parser.add_argument(
        "--single-choice-chance",
        type=percentage,
        default=0.0,
        metavar="PERCENT",
        help=(
            "chance the craft produces only one outcome instead of --choices; "
            "use to model verified Intangibility behavior"
        ),
    )
    parser.add_argument(
        "--attempts",
        type=positive_integer,
        default=1,
        help="number of repeated crafts for the cumulative result (default: 1)",
    )
    parser.add_argument(
        "--confidence",
        type=percentage,
        action="append",
        help="confidence target; repeat for multiple values (default: 50,90,95,99)",
    )
    parser.add_argument(
        "--cost-per-craft",
        type=float,
        help="optional cost of one full craft in any consistent currency unit",
    )
    args = parser.parse_args()

    if args.success_weight is not None:
        if args.total_weight is None:
            parser.error("--total-weight is required with --success-weight")
        if args.total_weight <= 0:
            parser.error("--total-weight must be greater than zero")
        if not 0 <= args.success_weight <= args.total_weight:
            parser.error("--success-weight must be between zero and total weight")
        outcome_chance = args.success_weight / args.total_weight
    else:
        if args.total_weight is not None:
            parser.error("--total-weight is only valid with --success-weight")
        outcome_chance = args.chance / 100

    if args.cost_per_craft is not None and args.cost_per_craft < 0:
        parser.error("--cost-per-craft cannot be negative")

    collapse_chance = args.single_choice_chance / 100
    craft_chance = effective_craft_chance(
        outcome_chance, args.choices, collapse_chance
    )
    cumulative_chance = at_least_one(craft_chance, args.attempts)

    print(f"One outcome:              {format_percent(outcome_chance)}")
    print(f"Effective chance/craft:   {format_percent(craft_chance)}")
    print(
        f"Chance within {args.attempts} craft(s): "
        f"{format_percent(cumulative_chance)}"
    )

    if craft_chance == 0:
        print("Expected crafts:          never")
    else:
        expected_crafts = 1 / craft_chance
        print(f"Expected crafts:          {expected_crafts:.4f}")
        if args.cost_per_craft is not None:
            print(
                "Expected cost:            "
                f"{expected_crafts * args.cost_per_craft:.4f}"
            )

    confidence_targets = args.confidence or DEFAULT_CONFIDENCE
    for target in confidence_targets:
        attempts = attempts_for_confidence(craft_chance, target / 100)
        label = f"Crafts for {target:g}%:"
        print(f"{label:<26}{attempts if attempts is not None else 'never'}")

    print(
        "Assumption: preview choices are independent draws with a static "
        "per-outcome chance."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
