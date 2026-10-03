"""Ratio box, house address, address cipher.

A box whose edges are moduli assigns a room. It is a cipher only if the
address recovers the occupant. A ratio is not a constitution by being named.
operation_effect: ROUTE_NAMES_ONLY
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _act(handle: str, act: str, object_: str, condition: str, nonclaim: str) -> Act:
    return Act(
        handle=handle,
        stem="ratio-box",
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=Standing.NAMED,
        provenance=Provenance("modulo houses", "edges are moduli, not a seal"),
    )


RATIO_BOX = _act(
    "ratio-box",
    "take the edge lengths as the moduli",
    "a rectangular cell with stated positive integer edges",
    "each edge is a public modulus",
    "a ratio does not hide an occupant and does not ratify a charter",
)

HOUSE_ADDRESS = _act(
    "house-address",
    "assign the residue on each edge",
    "an occupant and a ratio-box",
    "address is (x mod a, y mod b, z mod c), all coordinates readable",
    "sharing an address is not sharing a sealed record",
)

ADDRESS_CIPHER = _act(
    "address-cipher",
    "recover the occupant from the address",
    "a house-address and the box that made it",
    "decode returns the occupant, or the filing refuses",
    "a public ratio is an encoding, not a secret, until a key is a separate slot",
)

BOX_SHELF: tuple[Act, ...] = (RATIO_BOX, HOUSE_ADDRESS, ADDRESS_CIPHER)


def address(occupant: tuple[int, int, int], edges: tuple[int, int, int]) -> tuple[int, int, int]:
    """Public residue. Not a seal."""
    return tuple(part % edge for part, edge in zip(occupant, edges))


def mount_box_shelf(hive) -> None:
    hive.mount("ratio-box", BOX_SHELF)
