import unittest
from .solution1 import Solution as Solution1


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_multiple_pairs(self):
            result = self.solution.twoSum([3, 2, 4], 6)
            self.assertIn(result, [[1, 2]])

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
