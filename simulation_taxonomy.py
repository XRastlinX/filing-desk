"""Staged taxonomy of simulation handles.

Darwin: shared characters, inherited from a parent act, split by condition.
Dewey: a job code, so a flow-tear is not shelved under a zero-claim.

A species is a runnable model specification. It is not the relation it models.
authority_effect: NONE. No species here solves, formalizes, or promotes a claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from act_handles import (
    ARHEOSCHISIS,
    BIASCHISIS,
    ELEGXIS,
    HEMIGRAMMOS,
    INDEX_REMAINDER,
    LEIORRHOE,
    PHOROS,
    Act,
    Standing,
)


@dataclass(frozen=True)
class Taxon:
    """One shelf. Code is Dewey-like. Parent is the Darwinian inheritance."""

    code: str
    rank: str
    name: str
    job: str
    parent: str
    nonclaim: str


@dataclass(frozen=True)
class SimulationSpecies:
    """A Python-shaped model of an act. Running it is not settling it."""

    taxon: Taxon
    act: Act
    state: str
    step: str
    refuses: tuple[str, ...]

    def card(self) -> str:
        return (
            f"{self.taxon.code} {self.taxon.name} "
            f"models {self.act.handle} [{self.act.standing.value}]"
        )


KINGDOM = Taxon(
    code="000",
    rank="kingdom",
    name="executable-description",
    job="hold an act in slots a checker can read",
    parent="",
    nonclaim="not the terrain",
)

FLOW = Taxon(
    code="532",
    rank="phylum",
    name="flow-models",
    job="step a velocity field under a stated force and viscosity",
    parent="000",
    nonclaim="a step is not a smoothness theorem",
)

CHECK = Taxon(
    code="513",
    rank="phylum",
    name="check-models",
    job="separate kernel acceptance from carried reason",
    parent="000",
    nonclaim="a flag is not a proof",
)

COUNT = Taxon(
    code="512",
    rank="phylum",
    name="count-models",
    job="index integers and record remainders or zero claims",
    parent="000",
    nonclaim="a remainder is not a second structure",
)

SPECIES: tuple[SimulationSpecies, ...] = (
    SimulationSpecies(
        taxon=Taxon(
            code="532.1",
            rank="species",
            name="unforced-smoothness-watch",
            job="record whether a numerical flow stays bounded",
            parent="532",
            nonclaim="a bounded grid run is not leiorrhoe",
        ),
        act=LEIORRHOE,
        state="velocity on a grid, force identically zero",
        step="advance viscous incompressible step; log max gradient",
        refuses=("nonzero force", "filing a blowup as the prize act"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="532.2",
            rank="species",
            name="forced-tear-watch",
            job="record a numerical tear when a force is applied",
            parent="532",
            nonclaim="not evidence that the unforced law tears",
        ),
        act=BIASCHISIS,
        state="velocity on a grid, force field stored beside it",
        step="advance with the force; log gradient growth",
        refuses=("erasing the force flag", "relabeling as 532.1"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="532.3",
            rank="species",
            name="inviscid-tear-watch",
            job="record a tear with the viscous term removed",
            parent="532",
            nonclaim="Euler is not the viscous prize statement",
        ),
        act=ARHEOSCHISIS,
        state="velocity on a grid, viscosity coefficient zero",
        step="advance inviscid step; log gradient growth",
        refuses=("turning viscosity back on", "filing under 532.1"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="512.1",
            rank="species",
            name="half-line-watch",
            job="hold the half-line claim next to computed ordinates",
            parent="512",
            nonclaim="a computed zero is not a location theorem",
        ),
        act=HEMIGRAMMOS,
        state="list of computed ordinates, claim kept separate",
        step="append an ordinate; do not mark the claim settled",
        refuses=("writing standing=settled", "naming the function after a person"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="512.7",
            rank="species",
            name="index-remainder-watch",
            job="compute p_n mod n and store it as that remainder",
            parent="512",
            nonclaim="not a gear, a type, or a new prime particle",
        ),
        act=INDEX_REMAINDER,
        state="index n, prime p_n, remainder r",
        step="r = p_n % n; record (n, r)",
        refuses=("setting the next modulus from a gear story", "calling r a class type"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="513.1",
            rank="species",
            name="kernel-check-watch",
            job="record that a checker accepted or rejected steps",
            parent="513",
            nonclaim="acceptance is not carried understanding",
        ),
        act=ELEGXIS,
        state="axioms, steps, checker verdict",
        step="ask the checker; store the verdict beside the text",
        refuses=("copying the verdict into phoros", "dropping the axiom list"),
    ),
    SimulationSpecies(
        taxon=Taxon(
            code="513.2",
            rank="species",
            name="carried-reason-watch",
            job="record whether a person can restate the hinge",
            parent="513",
            nonclaim="a restatement is not a kernel verdict",
        ),
        act=PHOROS,
        state="hinge, restatement, nearby statement",
        step="store the restatement; do not invent a checker flag",
        refuses=("treating eloquence as acceptance", "filing under 513.1"),
    ),
)


def shelf() -> list[str]:
    """Dewey order. Inheritance is in parent, not in the sort."""
    lines = [
        f"{KINGDOM.code} {KINGDOM.name}: {KINGDOM.job}",
        f"{FLOW.code} {FLOW.name}: {FLOW.job}",
        f"{CHECK.code} {CHECK.name}: {CHECK.job}",
        f"{COUNT.code} {COUNT.name}: {COUNT.job}",
    ]
    for species in sorted(SPECIES, key=lambda item: item.taxon.code):
        lines.append(species.card())
    return lines


def crossings() -> list[str]:
    """Darwinian refusals: shared phylum is not shared condition."""
    found: list[str] = []
    for left in SPECIES:
        for right in SPECIES:
            if left is right or left.taxon.parent != right.taxon.parent:
                continue
            if left.act.rejects(right.act) and left.taxon.code < right.taxon.code:
                found.append(
                    f"refuse cross-file {left.taxon.code} -> {right.taxon.code}"
                )
    return found


def main() -> None:
    print("\n".join(shelf()))
    print("---")
    print("\n".join(crossings()))
    open_acts = [item.act.handle for item in SPECIES if item.act.standing is Standing.OPEN]
    print("open, not simulated away:", ", ".join(open_acts))


if __name__ == "__main__":
    main()
