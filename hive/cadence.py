"""Periodic agent jobs. Each returns a record and stops before apply.

operation_effect: RECORD_AND_ROUTE
promotion_effect: NONE
authority_effect: NONE
"""

from __future__ import annotations

from act_handles import Act, Provenance, Standing


def _job(handle: str, act: str, object_: str, condition: str, nonclaim: str) -> Act:
    return Act(
        handle=handle,
        stem="cadence",
        act=act,
        object_=object_,
        condition=condition,
        nonclaim=nonclaim,
        standing=Standing.NAMED,
        provenance=Provenance("periodic program", "record only, apply outside"),
    )


JOBS: tuple[Act, ...] = (
    _job(
        "row-restore",
        "reseat each binding on its shelf",
        "one internal service",
        "clash logged, standing unwritten, unbound door if recovery fails",
        "not a disk cleanup and not a heal",
    ),
    _job(
        "recovery-pass",
        "decode each mounted handle back to its sentence",
        "the legend",
        "mismatch appends a residual and does not remount",
        "a failed recovery is not a rewrite",
    ),
    _job(
        "prefix-check",
        "compare the encounter prefix to the prior record",
        "the append-only log",
        "a shorter later log is a refuse",
        "a new file alone does not prove old events survived",
    ),
    _job(
        "door-check",
        "ask a bound local door for the mounted sentence",
        "loopback bindings only",
        "a different answer unbinds the proposal, not the host",
        "an idle port is not a bind",
    ),
    _job(
        "halt-count",
        "recount the three stream halts",
        "p_n under next modulus pi(residue)",
        "counts are evidence, range is stated",
        "a count does not close leiorrhoe or hemigrammos",
    ),
)


CADENCE = {
    "row-restore": "daily",
    "recovery-pass": "daily",
    "prefix-check": "on each append",
    "door-check": "when a bind is proposed",
    "halt-count": "on demand",
}


def assign(handle: str) -> str:
    job = next((item for item in JOBS if item.handle == handle), None)
    if job is None:
        return "refuse: unassigned"
    return f"{CADENCE[handle]}: {job.recovery()} stop before apply"
