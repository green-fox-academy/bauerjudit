import unittest
from counter import count_letter

class LetterCounterTest(unittest.TestCase):
    def test_if_exists(self):
        self.assertEqual(count_letter(""), {})

    def test_simple_letters(self):
        self.assertEqual(count_letter("a"), {"a":1})
        self.assertEqual(count_letter("aa"), {"a":2})

    def test_differernt_letters(self):
        self.assertEqual(count_letter("b"), {"b":1})

    def test_distinct_letters(self):
        self.assertEqual(count_letter("ab"), {"a":1, "b":1})



unittest.main()
