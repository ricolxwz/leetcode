import unittest
from .solution1 import Solution as Solution1
from .solution2 import Solution as Solution2


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_common_prefix(self):
            self.assertEqual(self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

        def test_no_common_prefix(self):
            self.assertEqual(self.solution.longestCommonPrefix(["dog", "racecar", "car"]), "")

        def test_empty_string(self):
            self.assertEqual(self.solution.longestCommonPrefix(["", "b", ""]), "")

        def test_single_character(self):
            self.assertEqual(self.solution.longestCommonPrefix(["a", "a", "a"]), "a")

        def test_empty_list(self):
            self.assertEqual(self.solution.longestCommonPrefix([]), "")

        def test_single_string(self):
            self.assertEqual(self.solution.longestCommonPrefix(["single"]), "single")

        def test_case_sensitivity(self):
            self.assertEqual(self.solution.longestCommonPrefix(["Case", "ca"]), "")

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
TestSolution2 = create_test_class(Solution2)
