"""Quantum seal and modulo floor plan. Two shelves. Cross-file refuses.

Adapted to this board's Act and file_as. Act has no shelf field;
the shelf is the mount argument. This module does not close a claim.
operation_effect: ROUTE_NAMES_ONLY
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _act(handle: str, stem: str, act: str, object_: str, condition: str, nonclaim: str, source: str, locus: str) -> Act:
    return Act(
        handle=handle,
        stem=stem,
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=Standing.NAMED,
        provenance=Provenance(source, locus),
    )


WIGNER_OBSERVER = _act(
    "relational-observer-record",
    "wigner",
    "maintain an uncollapsed unitary description across an isolated boundary",
    "an isolated laboratory containing a measurement record",
    "thermodynamic seal present, measurement channel absent",
    "does not mean a mind collapses the state, and does not mean classical ignorance",
    "Wigner friend / Frauchiger-Renner",
    "isolated lab",
)

MODULO_FLOOR_PLAN = _act(
    "congruence-partition",
    "congruence",
    "partition the integers into disjoint residue classes",
    "the integers under a chosen modulus",
    "all occupants readable, no physical seal",
    "does not create a superposition of houses, and does not hide an outcome",
    "congruence arithmetic",
    "Z/mZ",
)


def mount_observer_cut(hive) -> None:
    hive.mount("quantum-observer", (WIGNER_OBSERVER,))
    hive.mount("count", (MODULO_FLOOR_PLAN,))


def prefix_unchanged(prior: list, later: list) -> bool:
    """Append-only check. A new file alone cannot show that old events survived."""
    if len(later) < len(prior):
        return False
    return later[: len(prior)] == prior
