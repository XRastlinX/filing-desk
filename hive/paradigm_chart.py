"""Paradigm chart filed as acts. A row is not a running network.

operation_effect: ROUTE_NAMES_ONLY
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _act(handle: str, act: str, object_: str, condition: str, nonclaim: str) -> Act:
    return Act(
        handle=handle,
        stem="chart",
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=Standing.NAMED,
        provenance=Provenance("paradigm chart", "row is not a deployment"),
    )


RECOVERY = _act(
    "reversible-term-cut",
    "recover the statement from the handle",
    "a mounted act",
    "D(N(S)) returns S, slots unchanged",
    "a reversible name is not a local URI scheme",
)

ADMISSIBLE = _act(
    "condition-match",
    "admit a filing only when the condition matches",
    "a source handle and a target handle",
    "prestige and vote count are not slots",
    "admissible is not true, and not proved",
)

HUMAN_KEY = _act(
    "human-apply",
    "leave the final apply outside the board",
    "standing and closure",
    "no organ writes standing",
    "a key on the chart is not a key in a lock",
)

APPEND_ONLY = _act(
    "append-only-record",
    "retain the prior encounter under a new correction",
    "an encounter sequence",
    "prefix unchanged",
    "a ledger row is not WORM media already written",
)

CHART: tuple[Act, ...] = (RECOVERY, ADMISSIBLE, HUMAN_KEY, APPEND_ONLY)


def mount_chart(hive) -> None:
    hive.mount("chart", CHART)
