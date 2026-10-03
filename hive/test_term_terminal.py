"""The term shelf mounts beside the fourteen. It does not replace them."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from hive_board import Hive  # noqa: E402
from term_terminal import mount_term_shelf  # noqa: E402


class TermShelfTest(unittest.TestCase):
    def test_three_acts_refuse_each_other(self) -> None:
        hive = Hive()
        self.assertEqual(len(hive.legend()), 14)
        mount_term_shelf(hive)
        handles = {entry.handle for entry in hive.legend()}
        self.assertEqual(len(handles), 17)
        self.assertTrue({"term", "terminology", "terminal"} <= handles)
        for left, right in (("term", "terminal"), ("terminology", "terminal"), ("term", "terminology")):
            filing = hive.file_as(left, right)
            self.assertEqual(filing.outcome, "refuse", pair := (left, right))
            self.assertIn("is not", filing.detail)
        self.assertEqual(hive.file_as("terminal", "terminal").outcome, "land")
        self.assertEqual(hive.shelf_of("leiorrhoe"), "flow-check-count")


if __name__ == "__main__":
    unittest.main()
