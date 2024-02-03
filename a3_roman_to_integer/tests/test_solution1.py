import unittest
from ..solution1 import Solution


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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
