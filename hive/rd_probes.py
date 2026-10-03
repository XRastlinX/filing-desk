"""R&D probes. Evidence returns to the organism. Standing is not updated.

operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

import json
from pathlib import Path

from act_handles import Act, Provenance, Standing
from organism import Organism


def index_remainder(limit: int) -> dict:
    """p_n mod n. A table, not a new structure."""
    primes = [2]
    residues = []
    zeros = []
    prime_residue = 0
    composite_residue = 0
    residue_one = 0
    for n in range(2, limit + 1):
        candidate = primes[-1] + 1
        while True:
            if all(candidate % p for p in primes if p * p <= candidate):
                primes.append(candidate)
                break
            candidate += 1
        residue = primes[-1] % n
        residues.append(residue)
        if residue == 0:
            zeros.append(n)
        elif residue == 1:
            residue_one += 1
        elif all(residue % p for p in primes if p * p <= residue) and residue > 1:
            prime_residue += 1
        else:
            composite_residue += 1
    return {
        "limit": limit,
        "zeros_after_index_1": zeros,
        "residue_one": residue_one,
        "prime_residue": prime_residue,
        "composite_or_other": composite_residue,
        "max_residue": max(residues),
        "mean_residue_over_index": round(sum(residues) / len(residues) / (limit / 2), 4),
        "head": residues[:12],
    }


def reconfiguration(limit: int) -> dict:
    """Next modulus is pi(residue). Undefined at pi(1)=0. Not a gear train."""
    primes = []
    halt = {"pi_1": 0, "residue_0": 0, "sink_1_0": 0}
    samples = []
    candidate = 1
    while len(primes) < limit:
        candidate += 1
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    for n, prime in enumerate(primes, start=1):
        residue = prime % n
        steps = [(n, residue)]
        reason = "start"
        for _ in range(8):
            if residue < 1:
                reason = "residue_0"
                halt["residue_0"] += 1
                break
            modulus = sum(1 for p in primes if p <= residue)
            if modulus < 1:
                reason = "pi_1"
                halt["pi_1"] += 1
                break
            residue = residue % modulus
            steps.append((modulus, residue))
            if (modulus, residue) == (1, 0):
                reason = "sink_1_0"
                halt["sink_1_0"] += 1
                break
        if n in {1, 2, 3, 4, 5, 9, 26}:
            samples.append({"n": n, "prime": prime, "reason": reason, "steps": steps})
    return {"limit": limit, "halt": halt, "samples": samples}


def main() -> None:
    organism = Organism()
    remainder = index_remainder(400)
    rule = reconfiguration(400)
    organism.metabolize(
        "Index remainder through n=400: zeros after index 1 = "
        f"{remainder['zeros_after_index_1'] or 'none'}."
    )
    organism.metabolize(
        "Reconfiguration halts: "
        f"pi(1)={rule['halt']['pi_1']}, residue 0={rule['halt']['residue_0']}, "
        f"sink={rule['halt']['sink_1_0']}."
    )
    organism.grow(
        "halt-split",
        "count how a pi(residue) step stops",
        "the first 400 primes",
        "pi(1)=0 and residue 0 are different halts",
    )
    organism.repair(
        "index-remainder",
        "leiorrhoe",
        "a remainder table is not a smoothness claim",
    )
    drifted = Act(
        handle="leiorrhoe",
        stem="leios + rheo",
        act="settled by a 400-step table",
        object_="unforced three-dimensional incompressible flow",
        condition="viscosity present, external force absent, dimension 3",
        nonclaim="a table is not a proof",
        standing=Standing.CLAIMED,
        provenance=Provenance("R&D probe", "must refuse"),
    )
    refused = organism.hive.file_as(drifted, "leiorrhoe")
    organism._remember("probe-filing", {"verdict": refused.verdict})
    report = {
        "operation_effect": "RECORD_AND_ROUTE",
        "promotion_effect": "NONE",
        "authority_effect": "NONE",
        "index_remainder": remainder,
        "reconfiguration": rule,
        "standing_after": {
            entry.handle: entry.standing
            for entry in organism.hive.legend()
            if entry.handle in {"leiorrhoe", "hemigrammos", "index-remainder"}
        },
        "close_attempt": organism.close_claim("leiorrhoe"),
        "drifted_filing": refused.verdict,
        "memory_tail": [item.kind for item in organism.memory],
    }
    out = Path(__file__).resolve().parent / "rd-probes.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("index_remainder", "standing_after", "close_attempt", "drifted_filing")}, indent=2))
    print("reconfiguration halt", rule["halt"])
    print("samples", json.dumps(rule["samples"]))


if __name__ == "__main__":
    main()
