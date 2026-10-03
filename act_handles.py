"""Staged handles for acts, not eponyms.

A class here is a legend with slots. It is not the relation it names.
authority_effect: NONE. Nothing in this module proves, formalizes, or files
one act under another.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Standing(Enum):
    """How far the act has been carried. Not a proof status granted by the class."""

    NAMED = "named"
    OPEN = "open"
    CLAIMED = "claimed"
    PARTIAL = "partial"
    NOT_THE_PRIZE = "not_the_prize"


@dataclass(frozen=True)
class Provenance:
    """Off-handle record. Stripping this fails the bleach."""

    source: str
    locus: str


@dataclass(frozen=True)
class Act:
    """act + object + condition. A person-name in the handle is rejected."""

    handle: str
    act: str
    object_: str
    condition: str
    nonclaim: str
    standing: Standing
    provenance: Provenance
    stem: str = ""

    def recovery(self) -> str:
        """Turn the handle back into the old statement. No metaphor slot."""
        return f"{self.act} on {self.object_}, when {self.condition}."

    def rejects(self, other: Act) -> bool:
        """Same nickname is not enough. Condition mismatch means different act."""
        return self.condition != other.condition or self.object_ != other.object_


@dataclass(frozen=True)
class FlowAct(Act):
    """A flow-law claim. Viscous, forced, and inviscid are not one class."""

    viscosity: bool = True
    external_force: bool = False
    dimension: int = 3


@dataclass(frozen=True)
class CheckAct(Act):
    """A deduction-kind claim. Kernel check and carried reason are different acts."""

    kernel_checked: bool = False
    person_can_carry: bool = False


def _tag(source: str, locus: str) -> Provenance:
    return Provenance(source=source, locus=locus)


LEIORRHOE = FlowAct(
    handle="leiorrhoe",
    stem="leios + rheo",
    act="stay smooth for all later time",
    object_="unforced three-dimensional incompressible flow",
    condition="viscosity present, external force absent, dimension 3",
    nonclaim="does not mean a forced tear, an Euler cousin, or a pipe flow",
    standing=Standing.OPEN,
    provenance=_tag("prize statement", "viscous incompressible smoothness, unforced"),
    viscosity=True,
    external_force=False,
    dimension=3,
)

BIASCHISIS = FlowAct(
    handle="biaschisis",
    stem="bia + schisis",
    act="tear in finite time",
    object_="smooth flow under an external force",
    condition="external force present",
    nonclaim="does not answer leiorrhoe",
    standing=Standing.NOT_THE_PRIZE,
    provenance=_tag("September 2026 forced-tear claim", "kernel check separate from the act"),
    viscosity=True,
    external_force=True,
    dimension=3,
)

ARHEOSCHISIS = FlowAct(
    handle="arheoschisis",
    stem="a + rheos + schisis",
    act="tear with viscosity removed",
    object_="inviscid flow",
    condition="viscosity absent",
    nonclaim="must not be filed under leiorrhoe",
    standing=Standing.PARTIAL,
    provenance=_tag("Euler cousin", "related, not the same act"),
    viscosity=False,
    external_force=False,
    dimension=3,
)

HEMIGRAMMOS = Act(
    handle="hemigrammos",
    stem="hemisys + gramme",
    act="sit on the line of real part 1/2",
    object_="nontrivial zeros of the continued prime-product function",
    condition="the function and the half-line claim kept as two objects",
    nonclaim="renaming does not move a zero",
    standing=Standing.OPEN,
    provenance=_tag("half-line claim", "continued prime-product function"),
)

ELEGXIS = CheckAct(
    handle="elegxis",
    stem="elegchos",
    act="accept every step from stated axioms",
    object_="a deduction",
    condition="a proof checker is the acceptor",
    nonclaim="does not mean a person can carry the hinge",
    standing=Standing.NAMED,
    provenance=_tag("kernel-checked deduction", "axioms, steps, kernel"),
    kernel_checked=True,
    person_can_carry=False,
)

PHOROS = CheckAct(
    handle="phoros",
    stem="phero",
    act="restate the hinge and use it on a nearby statement",
    object_="a reason",
    condition="a person can carry it",
    nonclaim="does not mean the kernel rejected the steps",
    standing=Standing.NAMED,
    provenance=_tag("carried reason", "hinge, restatement, transfer"),
    kernel_checked=False,
    person_can_carry=True,
)

INDEX_REMAINDER = Act(
    handle="index-remainder",
    stem="",
    act="leave the remainder",
    object_="the nth prime divided by its index",
    condition="modulus is the index, not a fixed integer",
    nonclaim="not a gear, a class type, or a second structure beside the index",
    standing=Standing.NAMED,
    provenance=_tag("A004648", "p_n mod n"),
)

HANDLES: tuple[Act, ...] = (
    LEIORRHOE,
    BIASCHISIS,
    ARHEOSCHISIS,
    HEMIGRAMMOS,
    ELEGXIS,
    PHOROS,
    INDEX_REMAINDER,
)


def file_as(claimed: Act, target: Act) -> str:
    """Refuse a filing that uses one nickname for two conditions."""
    if claimed.rejects(target):
        return (
            f"refuse: {claimed.handle} is not {target.handle} "
            f"({claimed.condition} != {target.condition})"
        )
    return f"same act: {claimed.handle}"


def main() -> None:
    for handle in HANDLES:
        print(f"{handle.handle}: {handle.recovery()} [{handle.standing.value}]")
    print(file_as(BIASCHISIS, LEIORRHOE))
    print(file_as(ELEGXIS, PHOROS))


if __name__ == "__main__":
    main()
