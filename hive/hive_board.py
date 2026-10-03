"""Hive board: one switchboard and its legend.

A hive is a switchboard with a legend, not an autonomous mathematical swarm.
Mounting and filing route names only. They do not simulate, check proofs, or
close an open act.

operation_effect: ROUTE_NAMES_ONLY
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

_SOURCES = Path(__file__).resolve().parent.parent
if str(_SOURCES) not in sys.path:
    sys.path.insert(0, str(_SOURCES))

from act_handles import HANDLES, Act, Standing  # noqa: E402
from l_cluster import CLUSTER  # noqa: E402
from sound_alikes import SOUND_ALIKES  # noqa: E402

SOURCE_MODULES = (
    _SOURCES / "act_handles.py",
    _SOURCES / "sound_alikes.py",
    _SOURCES / "l_cluster.py",
)

# Recovered-handle list is a different shelf. Absence is not a merge.
RECOVERED_HANDLES = _SOURCES / "RECOVERED_HANDLES.md"


def module_bytes() -> dict[str, str]:
    """Hash the authoritative modules. Reading is not mounting."""
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in SOURCE_MODULES
    }


def meaning_slots(act: Act) -> dict[str, Any]:
    """Inert dataclass slots. Does not call recovery or any other method."""
    slots: dict[str, Any] = {}
    for field in fields(act):
        value = getattr(act, field.name)
        if isinstance(value, Standing):
            slots[field.name] = value.value
        elif hasattr(value, "__dict__") and not isinstance(value, (str, bytes)):
            slots[field.name] = asdict(value)
        else:
            slots[field.name] = value
    return slots


def recovery_sentence(act: Act) -> str:
    """Derived from declared fields. Does not call Act.recovery."""
    return f"{act.act} on {act.object_}, when {act.condition}."


@dataclass(frozen=True)
class LegendEntry:
    shelf: str
    handle: str
    standing: str
    recovery: str
    act: str
    object_: str
    condition: str
    nonclaim: str
    provenance: dict[str, str]
    slots: dict[str, Any]


@dataclass(frozen=True)
class Filing:
    source: str
    target: str
    outcome: str
    detail: str

    @property
    def verdict(self) -> str:
        return f"{self.outcome}: {self.detail}" if self.detail else self.outcome


@dataclass(frozen=True)
class Clash:
    handle: str
    kept_shelf: str
    refused_shelf: str
    reason: str


class Hive:
    """One board. Precedence is mount order, not nickname similarity."""

    def __init__(self) -> None:
        self._mounted: dict[str, tuple[str, Act]] = {}
        self.clashes: list[Clash] = []
        # L-cluster before sound-alike, so the selected wording stays mounted.
        self.mount("flow-check-count", HANDLES)
        self.mount("l-cluster", CLUSTER)
        self.mount("sound-alike", SOUND_ALIKES)

    def mount(self, shelf: str, acts: tuple[Act, ...] | Act) -> None:
        """Mount by slots. Exact duplicate is idempotent. Difference is a clash."""
        batch = (acts,) if isinstance(acts, Act) else acts
        for act in batch:
            current = self._mounted.get(act.handle)
            if current is None:
                self._mounted[act.handle] = (shelf, act)
                continue
            kept_shelf, kept = current
            if meaning_slots(kept) == meaning_slots(act):
                continue
            self.clashes.append(
                Clash(
                    handle=act.handle,
                    kept_shelf=kept_shelf,
                    refused_shelf=shelf,
                    reason="slots differ; no nickname merge",
                )
            )

    def legend(self) -> list[LegendEntry]:
        rows = []
        for handle, (shelf, act) in sorted(self._mounted.items()):
            slots = meaning_slots(act)
            rows.append(
                LegendEntry(
                    shelf=shelf,
                    handle=handle,
                    standing=act.standing.value,
                    recovery=recovery_sentence(act),
                    act=act.act,
                    object_=act.object_,
                    condition=act.condition,
                    nonclaim=act.nonclaim,
                    provenance=asdict(act.provenance),
                    slots=slots,
                )
            )
        return rows

    def file_as(self, source: str | Act, target: str | Act) -> Filing:
        """Land only when the mounted handle and its meaning slots match.

        Cross-filing onto a different handle is refused. An unmounted handle is
        refused. An Act whose slots differ from the mounted record is refused
        even when its nickname matches. Landing does not update standing.
        """
        source_name, source_act = self._resolve(source)
        target_name, target_act = self._resolve(target)
        if source_name is None:
            return Filing(self._label(source), self._label(target), "refuse", "unmounted source")
        if target_name is None:
            return Filing(source_name, self._label(target), "refuse", "unmounted target")
        if source_name != target_name:
            return Filing(
                source_name,
                target_name,
                "refuse",
                f"{source_name} is not {target_name}",
            )
        if source_act is not None and meaning_slots(source_act) != meaning_slots(self._mounted[source_name][1]):
            return Filing(source_name, target_name, "refuse", "slots differ from mounted record")
        if target_act is not None and meaning_slots(target_act) != meaning_slots(self._mounted[target_name][1]):
            return Filing(source_name, target_name, "refuse", "slots differ from mounted record")
        shelf = self._mounted[source_name][0]
        return Filing(source_name, target_name, "land", f"on {shelf}")

    def _resolve(self, item: str | Act) -> tuple[str | None, Act | None]:
        if isinstance(item, Act):
            if item.handle not in self._mounted:
                return None, item
            return item.handle, item
        if item not in self._mounted:
            return None, None
        return item, None

    @staticmethod
    def _label(item: str | Act) -> str:
        return item.handle if isinstance(item, Act) else item

    def shelf_of(self, handle: str) -> str:
        if handle not in self._mounted:
            return "refuse: unknown"
        return self._mounted[handle][0]


def legend_document(hive: Hive) -> dict[str, Any]:
    filings = [
        hive.file_as("biaschisis", "leiorrhoe"),
        hive.file_as("kernel-checker", "dual-correspondence"),
        hive.file_as("indistinguishable-family", "dual-correspondence"),
        hive.file_as("leiorrhoe", "leiorrhoe"),
    ]
    return {
        "operation_effect": "ROUTE_NAMES_ONLY",
        "promotion_effect": "NONE",
        "authority_effect": "NONE",
        "recovered_handles_merged": False,
        "recovered_handles_present": RECOVERED_HANDLES.is_file(),
        "entries": [asdict(entry) for entry in hive.legend()],
        "clashes": [asdict(clash) for clash in hive.clashes],
        "filings": [asdict(filing) for filing in filings],
    }


def write_outputs(directory: Path | None = None) -> Hive:
    hive = Hive()
    out = directory or Path(__file__).resolve().parent
    before = module_bytes()
    document = legend_document(hive)
    (out / "hive-legend.json").write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    after = module_bytes()
    verification = {
        "source_bytes_unchanged": before == after,
        "before": before,
        "after": after,
        "mounted": len(hive.legend()),
        "clashes": len(hive.clashes),
        "schesis_invoked": False,
    }
    (out / "hive-verification.json").write_text(
        json.dumps(verification, indent=2) + "\n",
        encoding="utf-8",
    )
    return hive


def main() -> None:
    hive = write_outputs()
    print(f"mounted: {len(hive.legend())}")
    for entry in hive.legend():
        print(f"[{entry.shelf}] {entry.handle} :: {entry.standing}")
    print("--- clashes ---")
    for clash in hive.clashes:
        print(f"{clash.handle}: kept {clash.kept_shelf}, refused {clash.refused_shelf}")
    print("--- filings ---")
    for filing in legend_document(hive)["filings"]:
        print(f"{filing['source']} -> {filing['target']}: {filing['outcome']}")


if __name__ == "__main__":
    main()
