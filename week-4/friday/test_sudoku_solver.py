import sudoku_solver
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_long(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too long.")

    def test_is_complete_duplicate_element(self):
        test_input = [1, 1, 3, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "An element is duplicated.")

    def test_is_complete_out_of_range_element(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "Out of range element in array.")

    def test_is_complete_invalid_element(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, "x"]
        expected = False
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "Invalid element in array.")

    def test_is_complete_basic_order(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = True
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The basic ordering of 1-9 is correct.")

    def test_is_complete_descending_order(self):
        test_input = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = True
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The descending ordering of 1-9 is correct.")

    def test_is_complete_random_order(self):
        test_input = [4, 8, 2, 6, 5, 9, 3, 7, 1]
        expected = True
        actual = sudoku_solver.is_complete(test_input)
        self.assertEqual(expected, actual, "The random ordering of 1-9 is correct.")

unittest.main()
