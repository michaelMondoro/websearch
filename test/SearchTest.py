import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from Search import *


class TestSearchEngine(unittest.TestCase):
    engine = None

    @classmethod
    def setUpClass(cls):
        cls.engine = SearchEngine(logs=False)

    def test_search_engine_init(self):
        engine = SearchEngine(logs=False)
        self.assertEqual(engine.results, [])

    def test_search(self):
        self.engine.search("hello world", 3)
        self.assertEqual(3, len(self.engine.results))

if __name__ == "__main__":
    unittest.main()