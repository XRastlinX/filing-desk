"""Act hive: a legend and a switchboard for staged mathematical handles.

Import and query. Do not treat a landing as a proof.

    from acthive import Hive

    hive = Hive()
    hive.file("biaschisis", "leiorrhoe")

authority_effect: NONE. This module does not simulate, formalize, or settle an act.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Standing(Enum):
    """How far the act has been carried. Not a status the class can grant."""

    NAMED = "named"
    OPEN = "open"
    CLAIMED = "claimed"
    PARTIAL = "partial"
    NOT_THE_PRIZE = "not_the_prize"


@dataclass(frozen=True)
class Provenance:
    """Off-handle record. A bleach that drops this has failed."""

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
        """Turn the handle back into the statement. No metaphor slot."""
        return f"{self.act} on {self.object_}, when {self.condition}."

    def rejects(self, other: Act) -> bool:
        """Same nickname is not enough. Condition mismatch means a different act."""
        return self.condition != other.condition or self.object_ != other.object_


@dataclass(frozen=True)
class LegendEntry:
    shelf: str
    handle: str
    recovery: str
    standing: str
    nonclaim: str


@dataclass(frozen=True)
class Filing:
    requested: str
    landed: str
    verdict: str


def _tag(source: str, locus: str) -> Provenance:
    return Provenance(source=source, locus=locus)


def _act(
    handle: str,
    stem: str,
    act: str,
    object_: str,
    condition: str,
    nonclaim: str,
    standing: Standing,
    source: str,
    locus: str,
) -> Act:
    return Act(
        handle=handle,
        stem=stem,
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=standing,
        provenance=_tag(source, locus),
    )


FLOW_CHECK_COUNT: tuple[Act, ...] = (
    _act(
        "leiorrhoe",
        "leios + rheo",
        "stay smooth for all later time",
        "unforced three-dimensional incompressible flow",
        "viscosity present, external force absent, dimension 3",
        "does not mean a forced tear, an Euler cousin, or a pipe flow",
        Standing.OPEN,
        "prize statement",
        "viscous incompressible smoothness, unforced",
    ),
    _act(
        "biaschisis",
        "bia + schisis",
        "tear in finite time",
        "smooth flow under an external force",
        "external force present",
        "does not answer leiorrhoe",
        Standing.NOT_THE_PRIZE,
        "September 2026 forced-tear claim",
        "kernel check separate from the act",
    ),
    _act(
        "arheoschisis",
        "a + rheos + schisis",
        "tear with viscosity removed",
        "inviscid flow",
        "viscosity absent",
        "must not be filed under leiorrhoe",
        Standing.PARTIAL,
        "Euler cousin",
        "related, not the same act",
    ),
    _act(
        "hemigrammos",
        "hemisys + gramme",
        "sit on the line of real part 1/2",
        "nontrivial zeros of the continued prime-product function",
        "the function and the half-line claim kept as two objects",
        "renaming does not move a zero",
        Standing.OPEN,
        "half-line claim",
        "continued prime-product function",
    ),
    _act(
        "elegxis",
        "elegchos",
        "accept every step from stated axioms",
        "a deduction",
        "a proof checker is the acceptor",
        "does not mean a person can carry the hinge",
        Standing.NAMED,
        "kernel-checked deduction",
        "axioms, steps, kernel",
    ),
    _act(
        "phoros",
        "phero",
        "restate the hinge and use it on a nearby statement",
        "a reason",
        "a person can carry it",
        "does not mean the kernel rejected the steps",
        Standing.NAMED,
        "carried reason",
        "hinge, restatement, transfer",
    ),
    _act(
        "index-remainder",
        "",
        "leave the remainder",
        "the nth prime divided by its index",
        "modulus is the index, not a fixed integer",
        "not a gear, a class type, or a second structure beside the index",
        Standing.NAMED,
        "A004648",
        "p_n mod n",
    ),
)

SOUND_ALIKE: tuple[Act, ...] = (
    _act(
        "particle-stepper",
        "lammps",
        "step positions of many particles under a force field",
        "a molecular or materials configuration",
        "classical forces, large parallel run, not a proof kernel",
        "a stable release is not higher mathematics and not a fluid theorem",
        Standing.NAMED,
        "LAMMPS 30 September 2026 stable",
        "molecular dynamics simulator",
    ),
    _act(
        "kernel-checker",
        "lean",
        "accept or reject a formal step from stated axioms",
        "a text in a proof language",
        "the kernel is the acceptor",
        "a checked text is not a carried reason, and not a particle simulation",
        Standing.NAMED,
        "Lean proof assistant",
        "elegxis tool, not the theorem",
    ),
)

L_CLUSTER: tuple[Act, ...] = (
    _act(
        "continuous-symmetry",
        "lie",
        "differentiate a smooth symmetry group at the identity",
        "a Lie group",
        "the algebra is the tangent object, not the group",
        "not a packet, not an L-function, not a proof kernel",
        Standing.NAMED,
        "Lie group / Lie algebra",
        "the objects the classification sorts",
    ),
    _act(
        "dual-group",
        "L-group",
        "attach the dual reductive group, with Galois action",
        "a reductive group",
        "dual, not the original group",
        "building the dual does not prove the match",
        Standing.NAMED,
        "Langlands dual",
        "target of the parameter",
    ),
    _act(
        "indistinguishable-family",
        "L-packet",
        "collect irreducible representations with the same parameter",
        "representations of a reductive group over a local field",
        "same L-parameter, hence same L-function and epsilon factors",
        "a packet is not one representation and not the global conjecture",
        Standing.NAMED,
        "Langlands classification",
        "local sorting",
    ),
    _act(
        "euler-product-from-a-parameter",
        "L-function",
        "build an Euler product, then continue it",
        "a Galois representation or an automorphic form",
        "the product and the continued function kept distinct",
        "not the half-line claim about the prime-product zeta function",
        Standing.NAMED,
        "Artin / automorphic L-function",
        "the matching invariant",
    ),
    _act(
        "dual-correspondence",
        "langlands",
        "match Galois data to automorphic data through the dual",
        "a reductive group and its L-group",
        "geometric case proved 2024; arithmetic case is not that proof",
        "does not locate zeros and does not check a kernel",
        Standing.PARTIAL,
        "Langlands program",
        "classification plus conjecture",
    ),
)

SHELVES: dict[str, tuple[Act, ...]] = {
    "flow-check-count": FLOW_CHECK_COUNT,
    "sound-alike": SOUND_ALIKE,
    "l-cluster": L_CLUSTER,
}


class Hive:
    """Switchboard. One handle, one shelf. Cross-filing returns refuse."""

    def __init__(self, shelves: dict[str, tuple[Act, ...]] | None = None) -> None:
        self._by_handle: dict[str, tuple[str, Act]] = {}
        self.clashes: list[str] = []
        for shelf, acts in (shelves or SHELVES).items():
            self.mount(shelf, acts)

    def mount(self, shelf: str, acts: tuple[Act, ...]) -> None:
        """Add acts. A repeated handle with a different sentence is a clash."""
        for act in acts:
            if act.handle not in self._by_handle:
                self._by_handle[act.handle] = (shelf, act)
                continue
            prior_shelf, prior = self._by_handle[act.handle]
            if prior.recovery() == act.recovery():
                continue
            self.clashes.append(f"{act.handle}: {prior_shelf} vs {shelf}")
            self._by_handle[act.handle] = (shelf, act)

    def legend(self) -> list[LegendEntry]:
        return [
            LegendEntry(
                shelf=shelf,
                handle=handle,
                recovery=act.recovery(),
                standing=act.standing.value,
                nonclaim=act.nonclaim,
            )
            for handle, (shelf, act) in sorted(self._by_handle.items())
        ]

    def file(self, requested: str, onto: str) -> Filing:
        """Land only if the two handles name the same act."""
        if requested not in self._by_handle or onto not in self._by_handle:
            missing = requested if requested not in self._by_handle else onto
            return Filing(requested, onto, f"refuse: no such handle {missing}")
        _, claimed = self._by_handle[requested]
        shelf, target = self._by_handle[onto]
        if claimed.rejects(target):
            return Filing(requested, onto, f"refuse: {requested} is not {onto} on {shelf}")
        return Filing(requested, onto, f"land: {onto} on {shelf}")

    def shelf_of(self, handle: str) -> str:
        if handle not in self._by_handle:
            return "refuse: unknown"
        return self._by_handle[handle][0]

    def __len__(self) -> int:
        return len(self._by_handle)


def main() -> None:
    hive = Hive()
    print(f"hive size: {len(hive)}")
    for entry in hive.legend():
        print(f"[{entry.shelf}] {entry.handle} :: {entry.standing}")
    print("---")
    for requested, onto in (
        ("biaschisis", "leiorrhoe"),
        ("kernel-checker", "dual-correspondence"),
        ("indistinguishable-family", "dual-correspondence"),
        ("leiorrhoe", "leiorrhoe"),
    ):
        print(hive.file(requested, onto).verdict)


if __name__ == "__main__":
    main()
