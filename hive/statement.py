"""Statement of the work, in the shape the runs actually had.

operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

STATEMENT = """
What we are doing
-----------------
We are building a switchboard and a legend for mathematical acts.
A handle names an act, an object, and a condition.
The board lands a filing only when those slots match.
It refuses a filing when they do not.
Organs beside the board may remember, ask, propose, and append a correction.
They may not close an open claim.
A computation may add evidence. Evidence is not a proof.

What we are not doing
---------------------
We are not solving the unforced smoothness question.
We are not locating the nontrivial zeros.
We are not finishing the arithmetic Langlands match.
We are not turning p_n mod n into a second structure.
A new operator is a toy until a recovery sentence maps it back
onto a statement that was already a statement.

Goal
----
Keep one name from covering two acts, while the decade's texts
arrive faster than they can be read.
Success is a refusal that preserves the difference,
and a landing that does not change standing.

Term, terminology, terminal
---------------------------
These share a root and do not share an act.
Term marks the boundary the recovery sentence must respect.
Terminology is the legend on the wall.
Terminal is the conduit that returns land or refuse.
Mounting all three is allowed. Filing one onto another is a refuse.
The relation they point at is not in the terminal.
"""

PSEUDOCODE = """
ACT := handle, act, object, condition, nonclaim, standing, provenance

recovery(ACT) :=
    return act + " on " + object + ", when " + condition

BOARD.mount(shelf, ACT):
    if handle is new:
        store ACT on shelf
    else if slots equal mounted slots:
        do nothing
    else:
        append clash(handle, kept=mounted shelf, refused=shelf)
        leave the mounted ACT in place

BOARD.file(source, target):
    if either handle is unmounted:
        return refuse
    if source.handle != target.handle:
        return refuse
    if slots(source) != slots(mounted):
        return refuse
    return land on shelf
    # standing is not written

ORGANISM.metabolize(text) -> definition | model-note | question
ORGANISM.grow(handle, act, object, condition) -> candidate
    # candidate is not mounted
ORGANISM.repair(source, target, correction):
    append the filing, then append the correction
    # the prior filing stays
ORGANISM.close(handle, witness):
    return refuse
    # this organ does not apply a witness to standing

PROBE.index_remainder(n):
    return p_n mod n
    # evidence for the named act, not a new act

PROBE.stream(p_n):
    residue := p_n mod n
    repeat:
        if residue < 1: halt residue_0
        if pi(residue) < 1: halt pi_1
        residue := residue mod pi(residue)
        if state is (1, 0): halt sink
    # three halts are not one fate

TERM marks a boundary
TERMINOLOGY holds the legend
TERMINAL returns land or refuse
file(term, terminal) = refuse
file(terminology, terminal) = refuse
"""


def main() -> None:
    print(STATEMENT)
    print(PSEUDOCODE)


if __name__ == "__main__":
    main()
