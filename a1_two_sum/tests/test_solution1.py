import unittest
from ..solution1 import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_pairs(self):
        result = self.solution.twoSum([3, 2, 4], 6)
        self.assertIn(result, [[1, 2]])
