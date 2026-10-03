"""Modulo houses. A partition toy, not a measurement theory.

Two moduli are two floor plans of the same integers.
An integer is in one house per plan. Observers can disagree
on who shares a house. They cannot disagree on the integer.
operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

import json
from pathlib import Path


def houses(modulus: int, occupants: range) -> dict[int, list[int]]:
    rooms = {residue: [] for residue in range(modulus)}
    for number in occupants:
        rooms[number % modulus].append(number)
    return rooms


def disagree(plan_a: dict[int, list[int]], plan_b: dict[int, list[int]]) -> list[tuple[int, int]]:
    """Pairs that share a house in one plan and not in the other."""
    mate_a = {}
    mate_b = {}
    for room, occupants in plan_a.items():
        for number in occupants:
            mate_a[number] = room
    for room, occupants in plan_b.items():
        for number in occupants:
            mate_b[number] = room
    splits = []
    numbers = sorted(mate_a)
    for left in numbers:
        for right in numbers:
            if right <= left:
                continue
            same_a = mate_a[left] == mate_a[right]
            same_b = mate_b[left] == mate_b[right]
            if same_a != same_b:
                splits.append((left, right))
                if len(splits) == 8:
                    return splits
    return splits


def main() -> None:
    occupants = range(0, 24)
    plan_4 = houses(4, occupants)
    plan_6 = houses(6, occupants)
    report = {
        "operation_effect": "RECORD_AND_ROUTE",
        "promotion_effect": "NONE",
        "authority_effect": "NONE",
        "claim": "a modulus is a floor plan, not a sealed measurement",
        "houses_mod_4": {str(k): v for k, v in plan_4.items()},
        "houses_mod_6": {str(k): v for k, v in plan_6.items()},
        "same_event_different_roommate": disagree(plan_4, plan_6),
        "does_not_model": [
            "Wigner outside a sealed lab",
            "a result that exists for one observer and not the other",
            "superposition of houses",
        ],
    }
    path = Path(__file__).resolve().parent / "modulo_houses.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["same_event_different_roommate"]))
    print("mod 4 room 1", plan_4[1])
    print("mod 6 room 1", plan_6[1])


if __name__ == "__main__":
    main()
