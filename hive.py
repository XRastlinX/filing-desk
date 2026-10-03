"""Hive: a legend and a switchboard for staged acts.

A swarm here is a registry. It does not run simulations, call models, or settle acts.
authority_effect: NONE.
"""

from __future__ import annotations

from dataclasses import dataclass

from act_handles import HANDLES, Act
from l_cluster import CLUSTER
from sound_alikes import SOUND_ALIKES


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


class Hive:
    """Switchboard. One handle, one shelf. Cross-filing returns refuse."""

    def __init__(self) -> None:
        self._by_handle: dict[str, tuple[str, Act]] = {}
        self._mount("flow-check-count", HANDLES)
        self._mount("sound-alike", SOUND_ALIKES)
        self._mount("l-cluster", CLUSTER)

    def _mount(self, shelf: str, acts: tuple[Act, ...]) -> None:
        for act in acts:
            if act.handle in self._by_handle:
                prior_shelf, prior = self._by_handle[act.handle]
                if prior.recovery() == act.recovery():
                    return
                # Same nickname, different act: keep the later shelf and mark the clash.
                act = Act(
                    handle=act.handle,
                    stem=act.stem,
                    act=act.act,
                    object_=act.object_,
                    condition=act.condition,
                    nonclaim=(
                        f"{act.nonclaim}; clashes with {prior_shelf}:{prior.handle}"
                    ),
                    standing=act.standing,
                    provenance=act.provenance,
                )
            self._by_handle[act.handle] = (shelf, act)

    def legend(self) -> list[LegendEntry]:
        rows = []
        for handle, (shelf, act) in sorted(self._by_handle.items()):
            rows.append(
                LegendEntry(
                    shelf=shelf,
                    handle=handle,
                    recovery=act.recovery(),
                    standing=act.standing.value,
                    nonclaim=act.nonclaim,
                )
            )
        return rows

    def file(self, requested: str, onto: str) -> Filing:
        if requested not in self._by_handle or onto not in self._by_handle:
            missing = requested if requested not in self._by_handle else onto
            return Filing(requested, onto, f"refuse: no such handle {missing}")
        _, claimed = self._by_handle[requested]
        shelf, target = self._by_handle[onto]
        if claimed.rejects(target):
            return Filing(
                requested,
                onto,
                f"refuse: {requested} is not {onto} on {shelf}",
            )
        return Filing(requested, onto, f"land: {onto} on {shelf}")

    def shelf_of(self, handle: str) -> str:
        if handle not in self._by_handle:
            return "refuse: unknown"
        return self._by_handle[handle][0]


def main() -> None:
    hive = Hive()
    print(f"hive size: {len(hive.legend())}")
    for entry in hive.legend():
        print(f"[{entry.shelf}] {entry.handle} :: {entry.standing}")
    print("---")
    print(hive.file("biaschisis", "leiorrhoe").verdict)
    print(hive.file("kernel-checker", "dual-correspondence").verdict)
    print(hive.file("indistinguishable-family", "dual-correspondence").verdict)
    print(hive.file("leiorrhoe", "leiorrhoe").verdict)


if __name__ == "__main__":
    main()
