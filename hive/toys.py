"""Toys for roots, branches, streams, and friction.

A toy may define an operator. It may not close an open claim.
operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

import json
from pathlib import Path

from act_handles import Act, Provenance, Standing
from organism import Organism


def primes_upto(limit: int) -> list[int]:
    primes: list[int] = []
    candidate = 1
    while len(primes) < limit:
        candidate += 1
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    return primes


def particles(n: int, primes: list[int]) -> list[int]:
    """Multiplicative root. Unique prime factors, exponents dropped."""
    factors = []
    rest = n
    for prime in primes:
        if prime * prime > rest:
            break
        if rest % prime == 0:
            factors.append(prime)
            while rest % prime == 0:
                rest //= prime
    if rest > 1:
        factors.append(rest)
    return factors


def stream(prime: int, index: int, primes: list[int]) -> dict:
    """Branch under next-modulus = pi(residue). Three halts, not one fate."""
    residue = prime % index
    steps = [(index, residue)]
    for _ in range(8):
        if residue < 1:
            return {"halt": "residue_0", "steps": steps}
        modulus = sum(1 for p in primes if p <= residue)
        if modulus < 1:
            return {"halt": "pi_1", "steps": steps}
        residue = residue % modulus
        steps.append((modulus, residue))
        if (modulus, residue) == (1, 0):
            return {"halt": "sink_1_0", "steps": steps}
    return {"halt": "unfinished", "steps": steps}


def friction(organism: Organism, left: str, right: str) -> dict:
    """Tension is a refused filing, not a force in the equation."""
    filing = organism.hive.file_as(left, right)
    return {"pair": [left, right], "outcome": filing.outcome, "detail": filing.detail}


def main() -> None:
    organism = Organism()
    primes = primes_upto(300)
    halt_counts = {"residue_0": 0, "pi_1": 0, "sink_1_0": 0, "unfinished": 0}
    both_views = []
    for index, prime in enumerate(primes, start=1):
        branch = stream(prime, index, primes)
        halt_counts[branch["halt"]] += 1
        if index in {1, 11, 23, 101}:
            both_views.append(
                {
                    "value": prime,
                    "index": index,
                    "root": particles(prime, primes),
                    "branch": branch,
                }
            )
    tensions = [
        friction(organism, "index-remainder", "leiorrhoe"),
        friction(organism, "hemigrammos", "euler-product-from-a-parameter"),
        friction(organism, "kernel-checker", "elegxis"),
        friction(organism, "biaschisis", "leiorrhoe"),
    ]
    # New operator, declared as a view: depth of the branch. Not a prime invariant beyond the rule.
    depths = []
    for index, prime in enumerate(primes, start=1):
        depths.append(len(stream(prime, index, primes)["steps"]))
    organism.grow(
        "branch-depth",
        "count steps until a declared halt",
        "p_n under next modulus pi(residue)",
        "depth is a property of this rule, not of the prime alone",
    )
    organism.metabolize(
        "Can branch-depth place a zero of the continued prime-product function?"
    )
    report = {
        "operation_effect": "RECORD_AND_ROUTE",
        "promotion_effect": "NONE",
        "authority_effect": "NONE",
        "halt_counts": halt_counts,
        "mean_branch_depth": round(sum(depths) / len(depths), 3),
        "both_views": both_views,
        "tensions": tensions,
        "does_not_solve": [
            "unforced three-dimensional smoothness",
            "half-line location of nontrivial zeros",
            "arithmetic Langlands match",
        ],
        "close_leiorrhoe": organism.close_claim("leiorrhoe"),
        "close_hemigrammos": organism.close_claim("hemigrammos"),
    }
    path = Path(__file__).resolve().parent / "toys.json"
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("halt_counts", "mean_branch_depth", "tensions", "does_not_solve", "close_leiorrhoe")}, indent=2))
    print("views", json.dumps(both_views))


if __name__ == "__main__":
    main()
