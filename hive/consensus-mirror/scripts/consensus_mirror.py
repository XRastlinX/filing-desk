"""Local check for a consensus-mirror draft. Does not render media or apply.

operation_effect: RECORD_AND_ROUTE
authority_effect: NONE
"""

from __future__ import annotations

import sys
from pathlib import Path

FORBIDDEN = (
    "we proved",
    "the seal holds",
    "white rabbit",
    "sovereign_key",
    "antisis",
    "epochi",
    "dodecahedron",
)
STOP = "sources stay until the archive is applied"


def check(text: str) -> list[str]:
    lowered = text.lower()
    failures = [token for token in FORBIDDEN if token in lowered]
    if STOP not in lowered:
        failures.append("missing stop line")
    return failures


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: consensus_mirror.py slides.md [video-shotlist.md]")
        sys.exit(2)
    failed = False
    for name in sys.argv[1:]:
        text = Path(name).read_text(encoding="utf-8")
        failures = check(text)
        if failures:
            failed = True
            print(f"refuse {name}: {', '.join(failures)}")
        else:
            print(f"land {name}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
