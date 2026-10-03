"""Cross-file refusal for the seal and the floor plan. Does not verify Downloads."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from hive_board import Hive  # noqa: E402
from observer_cut import mount_observer_cut, prefix_unchanged  # noqa: E402
from organism import Organism, ProofWitness  # noqa: E402


class ObserverCutTest(unittest.TestCase):
    def test_cross_file_refuses_and_standing_stays(self) -> None:
        hive = Hive()
        before = {entry.handle: entry.standing for entry in hive.legend()}
        mount_observer_cut(hive)
        filing = hive.file_as("congruence-partition", "relational-observer-record")
        self.assertEqual(filing.outcome, "refuse")
        self.assertIn("is not", filing.detail)
        self.assertEqual(hive.shelf_of("congruence-partition"), "count")
        self.assertEqual(hive.shelf_of("relational-observer-record"), "quantum-observer")
        after = {entry.handle: entry.standing for entry in hive.legend() if entry.handle in before}
        self.assertEqual(before, after)

    def test_organs_do_not_apply_a_witness(self) -> None:
        organism = Organism()
        prior = list(organism.memory)
        organism.repair("biaschisis", "leiorrhoe", "related flow acts; not the same condition")
        self.assertTrue(prefix_unchanged(prior, organism.memory))
        self.assertEqual(
            organism.close_claim("leiorrhoe", ProofWitness("statement", "kernel", True)),
            "refuse: this organ does not apply a witness to standing",
        )
        self.assertEqual(
            next(entry.standing for entry in organism.hive.legend() if entry.handle == "leiorrhoe"),
            "open",
        )


if __name__ == "__main__":
    unittest.main()
