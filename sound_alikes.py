"""Sound-alike shelf. Three names, three acts.

LAMMPS, Lean, and Langlands are not one tech.
A class keeps the condition that the nickname drops.
authority_effect: NONE. No species here proves a correspondence or runs a simulator.
"""

from __future__ import annotations

from act_handles import Act, CheckAct, Provenance, Standing


def _tag(source: str, locus: str) -> Provenance:
    return Provenance(source=source, locus=locus)


LAMMPS_ACT = Act(
    handle="particle-stepper",
    stem="lammps",
    act="step positions of many particles under a force field",
    object_="a molecular or materials configuration",
    condition="classical forces, large parallel run, not a proof kernel",
    nonclaim="a stable release is not higher mathematics and not a fluid theorem",
    standing=Standing.NAMED,
    provenance=_tag("LAMMPS 30 September 2026 stable", "molecular dynamics simulator"),
)

LEAN_ACT = CheckAct(
    handle="kernel-checker",
    stem="lean",
    act="accept or reject a formal step from stated axioms",
    object_="a text in a proof language",
    condition="the kernel is the acceptor",
    nonclaim="a checked text is not a carried reason, and not a particle simulation",
    standing=Standing.NAMED,
    provenance=_tag("Lean proof assistant", "elegxis tool, not the theorem"),
    kernel_checked=True,
    person_can_carry=False,
)

LANGLANDS_ACT = Act(
    handle="dual-correspondence",
    stem="langlands",
    act="match representations on one side to sheaves or functions on the dual",
    object_="a reductive group and its dual, over a stated base",
    condition="the geometric case is a proved correspondence; the arithmetic case is not that proof",
    nonclaim="does not place zeros, does not step particles, does not check a kernel",
    standing=Standing.PARTIAL,
    provenance=_tag("geometric Langlands, 2024", "arithmetic and quantum forms remain other acts"),
)


SOUND_ALIKES: tuple[Act, ...] = (LAMMPS_ACT, LEAN_ACT, LANGLANDS_ACT)


def file_as(claimed: Act, target: Act) -> str:
    if claimed.rejects(target):
        return f"refuse: {claimed.handle} is not {target.handle}"
    return f"same act: {claimed.handle}"


def main() -> None:
    for act in SOUND_ALIKES:
        print(f"{act.stem}: {act.handle}: {act.recovery()} [{act.standing.value}]")
    print(file_as(LAMMPS_ACT, LEAN_ACT))
    print(file_as(LEAN_ACT, LANGLANDS_ACT))
    print(file_as(LAMMPS_ACT, LANGLANDS_ACT))


if __name__ == "__main__":
    main()
