"""Living architecture around a name-routing switchboard.

The hive routes names. Memory, metabolism, sensing, growth, and repair sit
beside it. None of them closes an open claim. A computation may add evidence.
Closing still requires a proof this module does not mint.

operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from hive_board import Hive


@dataclass(frozen=True)
class Encounter:
    """One retained event. Later events do not erase it."""

    index: int
    kind: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class Proposal:
    """Metabolic product. A question or a definition, not a standing change."""

    kind: str
    text: str
    missing: tuple[str, ...] = ()


@dataclass(frozen=True)
class ProofWitness:
    """What closing would require. This module never constructs a valid one."""

    statement: str
    checker: str
    accepted: bool


class Organism:
    """Persistent memory and feedback around one Hive. Not a closer."""

    def __init__(self, hive: Hive | None = None) -> None:
        self.hive = hive or Hive()
        self.memory: list[Encounter] = []
        self._connections: list[dict[str, Any]] = []
        self._remember("lineage", {"event": "board mounted", "handles": len(self.hive.legend())})

    def _remember(self, kind: str, payload: dict[str, Any]) -> Encounter:
        encounter = Encounter(len(self.memory), kind, payload)
        self.memory.append(encounter)
        return encounter

    def sense(self) -> dict[str, Any]:
        """Conflicts, missing conditions, and useful non-identities."""
        missing = [
            entry.handle
            for entry in self.hive.legend()
            if not entry.condition.strip()
        ]
        open_acts = [
            entry.handle
            for entry in self.hive.legend()
            if entry.standing in {"open", "partial", "not_the_prize"}
        ]
        report = {
            "clashes": [asdict(clash) for clash in self.hive.clashes],
            "missing_conditions": missing,
            "not_closed": open_acts,
            "related_but_refused": [
                self.hive.file_as("biaschisis", "leiorrhoe").verdict,
                self.hive.file_as("elegxis", "phoros").verdict,
            ],
        }
        self._remember("sensing", report)
        return report

    def metabolize(self, material: str) -> Proposal:
        """Turn incoming text into a definition, a model note, or a question."""
        text = material.strip()
        if not text:
            proposal = Proposal("question", "empty intake", ("act", "object", "condition"))
        elif text.endswith("?"):
            proposal = Proposal("question", text)
        elif "model" in text.lower() or "simulate" in text.lower():
            proposal = Proposal("model-note", text, ("does not update standing",))
        else:
            proposal = Proposal("definition", text)
        self._remember("metabolism", asdict(proposal))
        return proposal

    def grow(self, handle: str, act: str, object_: str, condition: str) -> Proposal:
        """Develop a candidate act. Do not mount it and do not set standing."""
        proposal = Proposal(
            "candidate-act",
            f"{handle}: {act} on {object_}, when {condition}.",
            ("not mounted", "standing unset"),
        )
        self._remember("growth", asdict(proposal))
        return proposal

    def repair(self, source: str, target: str, correction: str) -> Encounter:
        """Revise a connection by appending. The previous filing stays in memory."""
        filing = self.hive.file_as(source, target)
        prior = [item for item in self._connections if item["source"] == source and item["target"] == target]
        record = {
            "source": source,
            "target": target,
            "prior_outcome": filing.outcome,
            "correction": correction,
            "supersedes": prior[-1]["index"] if prior else None,
        }
        encounter = self._remember("repair", record)
        self._connections.append({**record, "index": encounter.index})
        return encounter

    def close_claim(self, handle: str, witness: ProofWitness | None = None) -> str:
        """Refuse closure unless a real checker acceptance is supplied. None is minted here."""
        entry = next((item for item in self.hive.legend() if item.handle == handle), None)
        if entry is None:
            result = "refuse: unmounted"
        elif witness is None or not witness.accepted or not witness.checker:
            result = "refuse: open claim closes only with an accepted proof witness"
        else:
            result = "refuse: this organ does not apply a witness to standing"
        self._remember("close-attempt", {"handle": handle, "result": result})
        return result

    def export(self, path: Path) -> None:
        path.write_text(
            json.dumps(
                {
                    "operation_effect": "RECORD_AND_ROUTE",
                    "promotion_effect": "NONE",
                    "authority_effect": "NONE",
                    "memory": [asdict(item) for item in self.memory],
                    "standing_unchanged": {
                        entry.handle: entry.standing for entry in self.hive.legend()
                    },
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )


def main() -> None:
    organism = Organism()
    organism.metabolize("Is a forced tear the unforced smoothness question?")
    organism.grow("index-remainder", "leave the remainder", "the nth prime", "modulus is the index")
    organism.repair("biaschisis", "leiorrhoe", "related flow acts; not the same condition")
    print(organism.sense()["not_closed"])
    print(organism.close_claim("leiorrhoe"))
    print(f"memory: {len(organism.memory)}")
    organism.export(Path(__file__).resolve().parent / "organism-memory.json")


if __name__ == "__main__":
    main()
