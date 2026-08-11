#!/usr/bin/env python3
"""Print a compact review snapshot from a Path of Building export code."""

from __future__ import annotations

import argparse
import binascii
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zlib

from decode_pob import decode_pob


STAT_GROUPS = (
    (
        "Damage",
        (
            "CombinedDPS",
            "TotalDPS",
            "TotalDot",
            "FullDPS",
            "FullDotDPS",
            "Speed",
            "AverageHit",
        ),
    ),
    (
        "Attributes",
        ("Str", "ReqStr", "Dex", "ReqDex", "Int", "ReqInt"),
    ),
    (
        "Resources",
        (
            "Mana",
            "ManaUnreserved",
            "ManaUnreservedPercent",
            "ManaCost",
            "ManaPerSecondCost",
        ),
    ),
    (
        "Defenses",
        (
            "Life",
            "EnergyShield",
            "Ward",
            "Armour",
            "PhysicalDamageReduction",
            "Evasion",
            "MeleeEvadeChance",
            "ProjectileEvadeChance",
            "TotalEHP",
            "PhysicalMaximumHitTaken",
            "FireMaximumHitTaken",
            "ColdMaximumHitTaken",
            "LightningMaximumHitTaken",
            "ChaosMaximumHitTaken",
            "EffectiveBlockChance",
            "EffectiveSpellBlockChance",
            "EffectiveSpellSuppressionChance",
            "FireResist",
            "FireResistOverCap",
            "ColdResist",
            "ColdResistOverCap",
            "LightningResist",
            "LightningResistOverCap",
            "ChaosResist",
            "ChaosResistOverCap",
            "EffectiveMovementSpeedMod",
        ),
    ),
    (
        "Recovery",
        (
            "LifeRegenRecovery",
            "LifeLeechGainRate",
            "EnergyShieldRegenRecovery",
            "EnergyShieldLeechGainRate",
            "ManaRegenRecovery",
        ),
    ),
    (
        "Charges",
        (
            "PowerCharges",
            "PowerChargesMax",
            "FrenzyCharges",
            "FrenzyChargesMax",
            "EnduranceCharges",
            "EnduranceChargesMax",
        ),
    ),
)


def read_export(path: Path | None) -> str:
    return path.read_text() if path else sys.stdin.read()


def format_value(raw_value: str) -> str:
    try:
        value = float(raw_value)
    except ValueError:
        return raw_value
    if value.is_integer():
        return str(int(value))
    if abs(value) >= 1000:
        return f"{value:,.0f}"
    return f"{value:.2f}".rstrip("0").rstrip(".")


def find_main_skill(root: ET.Element, main_socket_group: int) -> tuple[str, list[str]]:
    skills = root.find("Skills")
    if skills is None:
        return "unknown", []

    active_set = skills.get("activeSkillSet")
    skill_sets = skills.findall("SkillSet")
    selected_set = next(
        (skill_set for skill_set in skill_sets if skill_set.get("id") == active_set),
        skill_sets[0] if skill_sets else None,
    )
    if selected_set is None:
        return "unknown", []

    skill_groups = selected_set.findall("Skill")
    if not 1 <= main_socket_group <= len(skill_groups):
        return "unknown", []

    selected_group = skill_groups[main_socket_group - 1]
    enabled_gems = [
        gem.get("nameSpec", "unknown")
        for gem in selected_group.findall("Gem")
        if gem.get("enabled") != "false"
    ]
    return selected_group.get("slot", "unknown"), enabled_gems


def print_snapshot(root: ET.Element) -> None:
    build = root.find("Build")
    if build is None:
        raise ValueError("the export does not contain a Build section")

    main_socket_group = int(build.get("mainSocketGroup", "1"))
    main_slot, main_gems = find_main_skill(root, main_socket_group)
    stats = {
        player_stat.get("stat", ""): player_stat.get("value", "")
        for player_stat in build.findall("PlayerStat")
    }

    print("# PoB Snapshot")
    print()
    print(f"- Class: {build.get('className', 'unknown')}")
    print(f"- Ascendancy: {build.get('ascendClassName', 'unknown')}")
    print(f"- Level: {build.get('level', 'unknown')}")
    print(f"- Main socket group: {main_socket_group} ({main_slot})")
    print(f"- Enabled main-group gems: {', '.join(main_gems) if main_gems else 'unknown'}")

    for heading, stat_names in STAT_GROUPS:
        available = [(name, stats[name]) for name in stat_names if name in stats]
        if not available:
            continue
        print()
        print(f"## {heading}")
        print()
        for name, value in available:
            print(f"- {name}: {format_value(value)}")

    print()
    print(
        "Configuration, uptime, item sets, skill parts, and disabled gems still "
        "require review in the decoded XML or Path of Building."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print a compact review snapshot from a PoB export code."
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="file containing the export code; omit to read stdin",
    )
    args = parser.parse_args()

    try:
        root = ET.fromstring(decode_pob(read_export(args.path)))
        print_snapshot(root)
    except (OSError, ValueError, binascii.Error, ET.ParseError, zlib.error) as error:
        print(f"pob_snapshot.py: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
