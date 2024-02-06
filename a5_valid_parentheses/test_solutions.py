import unittest
from .solution1 import Solution as Solution1


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_empty_string(self):
            self.assertTrue(self.solution.isValid(""))

        def test_valid_parentheses(self):
            self.assertTrue(self.solution.isValid("()[]{}"))

        def test_invalid_parentheses(self):
            self.assertFalse(self.solution.isValid("(]"))

        def test_valid_nested_parentheses(self):
            self.assertTrue(self.solution.isValid("({[]})"))

        def test_invalid_nested_parentheses(self):
            self.assertFalse(self.solution.isValid("({[)]}"))

        def test_left_remain_parentheses(self):
            self.assertFalse(self.solution.isValid("([]"))

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
