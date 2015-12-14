import unittest
from menu import MyMenu

class TestMenu(unittest.TestCase):
  def test_existance(self):
    menu = MyMenu("New Game", "Load Game", "Exit")

unittest.main()
