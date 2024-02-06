import unittest
from .solution1 import Solution as Solution1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    """Helper function to convert a list to a linked list."""
    head = current = None
    for number in lst:
        if not head:
            head = ListNode(number)
            current = head
        else:
            current.next = ListNode(number)
            current = current.next
    return head


def linked_list_to_list(node):
    """Helper function to convert a linked list back to a list."""
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


def create_test_class(solution_class):
    class TestSolution(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.solution = solution_class()

        def test_empty_lists(self):
            list1 = list_to_linked_list([])
            list2 = list_to_linked_list([])
            expected = []
            result = linked_list_to_list(self.solution.mergeTwoLists(list1, list2))
            self.assertEqual(result, expected)

        def test_example_1(self):
            list1 = list_to_linked_list([1, 2, 4])
            list2 = list_to_linked_list([1, 3, 4])
            expected = [1, 1, 2, 3, 4, 4]
            result = linked_list_to_list(self.solution.mergeTwoLists(list1, list2))
            self.assertEqual(result, expected)

        def test_example_2(self):
            list1 = list_to_linked_list([])
            list2 = list_to_linked_list([0])
            expected = [0]
            result = linked_list_to_list(self.solution.mergeTwoLists(list1, list2))
            self.assertEqual(result, expected)

    TestSolution.__name__ = f'Test{solution_class.__name__}'
    return TestSolution


TestSolution1 = create_test_class(Solution1)
