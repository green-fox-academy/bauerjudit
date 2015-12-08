import unittest
from decorator import Rusty

class RustyTest(unittest.TestCase):
    def test_rusty_effect(self):
        weapon = Rusty(TestWeapon())
        self.assertEqual(5, weapon.damage())
        self.assertEqual(15, RustyHace().damage)

class TestWeapon:
    def damage(self):
        return 10

class TestHace:
    def demage(self):
        return 30

if __name__ == "__main__":
    unittest.main()
