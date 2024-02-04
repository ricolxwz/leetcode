import unittest
from .solution1 import Solution as Solution1


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_single_numeral(self):
            self.assertEqual(self.solution.romanToInt('I'), 1)

        def test_standard_numerals(self):
            self.assertEqual(self.solution.romanToInt('III'), 3)
            self.assertEqual(self.solution.romanToInt('XXII'), 22)
            self.assertEqual(self.solution.romanToInt('LXV'), 65)

        def test_with_subtractive_notation(self):
            self.assertEqual(self.solution.romanToInt('IV'), 4)
            self.assertEqual(self.solution.romanToInt('IX'), 9)
            self.assertEqual(self.solution.romanToInt('XL'), 40)

        def test_largest_numeral(self):
            self.assertEqual(self.solution.romanToInt('MMMCMXCIX'), 3999)

        def test_empty_string(self):
            self.assertEqual(self.solution.romanToInt(''), 0)

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
