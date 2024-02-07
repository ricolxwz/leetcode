import unittest
from .solution1 import Solution as Solution1


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_negative_number(self):
            self.assertFalse(self.solution.isPalindrome(-1))

        def test_positive_palindrome(self):
            self.assertTrue(self.solution.isPalindrome(121))

        def test_positive_non_palindrome(self):
            self.assertFalse(self.solution.isPalindrome(123))

        def test_palindrome_with_trailing_zeros(self):
            self.assertFalse(self.solution.isPalindrome(10))

        def test_single_digit_number(self):
            self.assertTrue(self.solution.isPalindrome(0))
            self.assertTrue(self.solution.isPalindrome(7))

        def test_large_palindrome_number(self):
            self.assertTrue(self.solution.isPalindrome(123454321))

        def test_large_non_palindrome_number(self):
            self.assertFalse(self.solution.isPalindrome(123456789))

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
