"""Term, terminology, and terminal. One root, three acts.

The pun is mountable. The identity is not.
operation_effect: ROUTE_NAMES_ONLY
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _act(handle: str, act: str, object_: str, condition: str, nonclaim: str) -> Act:
    return Act(
        handle=handle,
        stem="terminus",
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=Standing.NAMED,
        provenance=Provenance("term/terminal split", "legend is not the conduit"),
    )


TERM = _act(
    "term",
    "mark a boundary the recovery sentence must respect",
    "one act",
    "the word is checkable against act, object, and condition",
    "a term is not the conduit and not the whole relation",
)

TERMINOLOGY = _act(
    "terminology",
    "hold the legend of allowed meanings",
    "the set of mounted handles",
    "a legend entry, not a filing result",
    "the wall list is not the slot that answers",
)

TERMINAL = _act(
    "terminal",
    "accept a filing and return land or refuse",
    "one switchboard slot",
    "verdict is computed from slots, not from the pun",
    "output is not the relation the legend points at",
)

TERM_SHELF: tuple[Act, ...] = (TERM, TERMINOLOGY, TERMINAL)


def mount_term_shelf(hive) -> None:
    """Add the three acts. Does not identify them."""
    hive.mount("term-terminal", TERM_SHELF)
