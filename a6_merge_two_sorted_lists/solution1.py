from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        my_list = []
        flag = list1
        while flag is not None:
            my_list.append([flag.val, flag])
            flag = flag.next
        flag = list2
        while flag is not None:
            my_list.append([flag.val, flag])
            flag = flag.next
        sorted_list = sorted(my_list, key=lambda x: x[0])
        if not sorted_list:
            return None
        pre_node = sorted_list[0][1]
        for index in range(1, len(sorted_list)):
            current_node = sorted_list[index][1]
            pre_node.next = current_node
            pre_node = current_node
        pre_node.next = None
        return sorted_list[0][1]
