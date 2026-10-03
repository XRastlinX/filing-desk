"""Routing checks for the hive board. Does not mount a fifteenth act."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from act_handles import Act, Provenance, Standing  # noqa: E402
from hive_board import Hive, module_bytes, write_outputs  # noqa: E402


class HiveBoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.before = module_bytes()
        self.hive = Hive()

    def test_fourteen_mounted_and_one_clash(self) -> None:
        handles = [entry.handle for entry in self.hive.legend()]
        self.assertEqual(len(handles), 14)
        self.assertEqual(len(handles), len(set(handles)))
        self.assertEqual(len(self.hive.clashes), 1)
        clash = self.hive.clashes[0]
        self.assertEqual(clash.handle, "dual-correspondence")
        self.assertEqual(clash.kept_shelf, "l-cluster")
        self.assertEqual(clash.refused_shelf, "sound-alike")

    def test_l_cluster_wording_kept(self) -> None:
        entry = next(item for item in self.hive.legend() if item.handle == "dual-correspondence")
        self.assertIn("Galois data", entry.recovery)
        self.assertNotIn("sheaves", entry.recovery)
        self.assertEqual(entry.standing, "partial")

    def test_specified_filings(self) -> None:
        expect = {
            ("biaschisis", "leiorrhoe"): "refuse",
            ("kernel-checker", "dual-correspondence"): "refuse",
            ("indistinguishable-family", "dual-correspondence"): "refuse",
            ("leiorrhoe", "leiorrhoe"): "land",
        }
        for pair, outcome in expect.items():
            filing = self.hive.file_as(*pair)
            self.assertEqual(filing.outcome, outcome, pair)

    def test_landing_does_not_update_standing(self) -> None:
        before = next(item.standing for item in self.hive.legend() if item.handle == "leiorrhoe")
        self.hive.file_as("leiorrhoe", "leiorrhoe")
        after = next(item.standing for item in self.hive.legend() if item.handle == "leiorrhoe")
        self.assertEqual(before, "open")
        self.assertEqual(after, before)

    def test_unmounted_and_slot_mismatch_refuse(self) -> None:
        self.assertEqual(self.hive.file_as("not-a-handle", "leiorrhoe").outcome, "refuse")
        drifted = Act(
            handle="leiorrhoe",
            stem="leios + rheo",
            act="a different sentence",
            object_="unforced three-dimensional incompressible flow",
            condition="viscosity present, external force absent, dimension 3",
            nonclaim="does not mean a forced tear, an Euler cousin, or a pipe flow",
            standing=Standing.OPEN,
            provenance=Provenance("prize statement", "viscous incompressible smoothness, unforced"),
        )
        filing = self.hive.file_as(drifted, "leiorrhoe")
        self.assertEqual(filing.outcome, "refuse")
        self.assertIn("slots differ", filing.detail)

    def test_exact_remount_is_idempotent(self) -> None:
        mounted = self.hive._mounted["phoros"][1]
        before = len(self.hive.clashes)
        self.hive.mount("flow-check-count", mounted)
        self.assertEqual(len(self.hive.clashes), before)
        self.assertEqual(len(self.hive.legend()), 14)

    def test_source_bytes_unchanged(self) -> None:
        write_outputs(Path(__file__).resolve().parent)
        self.assertEqual(self.before, module_bytes())
        verification = json.loads(
            (Path(__file__).resolve().parent / "hive-verification.json").read_text(encoding="utf-8")
        )
        self.assertTrue(verification["source_bytes_unchanged"])
        self.assertFalse(verification["schesis_invoked"])
        self.assertEqual(verification["mounted"], 14)


if __name__ == "__main__":
    unittest.main()
