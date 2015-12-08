import unittest
from cerlic import Cerlic

class TestCelric(unittest.TestCase):
    def test_existance(self):
        celric = Cerlic("Test", 100, 10)
    def test_inheritance(self):
        cerlic = Cerlic("Test", 100, 10)
        self.assertEqual(cerlic.hp, 100)
    def test_heal(self):
        cerlic = Cerlic("Test", 100, 10)
        other = Cerlic("Other", 100, 10)
        cerlic.heal(other)
        self.assertEqual(other.hp, 110)



unittest.main()
