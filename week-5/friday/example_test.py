import unittest
from example import duplicate_encode

class TestFilter(unittest.TestCase):
    def test_existance(self):
        self.assertEqual(duplicate_encode(), "")
    def test_return_with_(self):
        self.assertEqual(duplicate_encode(""), "(")

unittest.main()
