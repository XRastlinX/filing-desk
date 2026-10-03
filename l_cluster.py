"""L-cluster shelf. One classification, five handles.

These are the Langlands words, not LAMMPS and not Lean.
A class is a legend. It does not prove the correspondence.
authority_effect: NONE.
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _tag(source: str, locus: str) -> Provenance:
    return Provenance(source=source, locus=locus)


LIE = Act(
    handle="continuous-symmetry",
    stem="lie",
    act="differentiate a smooth symmetry group at the identity",
    object_="a Lie group",
    condition="the algebra is the tangent object, not the group",
    nonclaim="not a packet, not an L-function, not a proof kernel",
    standing=Standing.NAMED,
    provenance=_tag("Lie group / Lie algebra", "the objects the classification sorts"),
)

L_GROUP = Act(
    handle="dual-group",
    stem="L-group",
    act="attach the dual reductive group, with Galois action",
    object_="a reductive group",
    condition="dual, not the original group",
    nonclaim="building the dual does not prove the match",
    standing=Standing.NAMED,
    provenance=_tag("Langlands dual", "target of the parameter"),
)

L_PACKET = Act(
    handle="indistinguishable-family",
    stem="L-packet",
    act="collect irreducible representations with the same parameter",
    object_="representations of a reductive group over a local field",
    condition="same L-parameter, hence same L-function and epsilon factors",
    nonclaim="a packet is not one representation and not the global conjecture",
    standing=Standing.NAMED,
    provenance=_tag("Langlands classification", "local sorting"),
)

L_FUNCTION = Act(
    handle="euler-product-from-a-parameter",
    stem="L-function",
    act="build an Euler product, then continue it",
    object_="a Galois representation or an automorphic form",
    condition="the product and the continued function kept distinct",
    nonclaim="not the half-line claim about the prime-product zeta function",
    standing=Standing.NAMED,
    provenance=_tag("Artin / automorphic L-function", "the matching invariant"),
)

LANGLANDS = Act(
    handle="dual-correspondence",
    stem="langlands",
    act="match Galois data to automorphic data through the dual",
    object_="a reductive group and its L-group",
    condition="geometric case proved 2024; arithmetic case is not that proof",
    nonclaim="does not locate zeros and does not check a kernel",
    standing=Standing.PARTIAL,
    provenance=_tag("Langlands program", "classification plus conjecture"),
)

CLUSTER: tuple[Act, ...] = (LIE, L_GROUP, L_PACKET, L_FUNCTION, LANGLANDS)


def main() -> None:
    for act in CLUSTER:
        print(f"{act.stem}: {act.recovery()} [{act.standing.value}]")
    print("refuse: packet is not the program; function is not the half-line claim")


if __name__ == "__main__":
    main()
