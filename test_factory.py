import pytest
import unittest
from factory import BreadFactory


class TestFactory(unittest.TestCase):
    tested_class = BreadFactory()

    def test_dough(self):
        self.assertTrue(self.tested_class.make_dough(True, True))

    def test_naan(self):
        self.assertEqual(self.tested_class.bake_naan(True), "naan")

    def test_run(self):
        self.assertEqual(self.tested_class.run_factory(["water", "flour"]), "naan")
