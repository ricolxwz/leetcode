from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_list(head):
            node_info = []
            current = head
            while current is not None:
                node_info.append([current.val, current])
                current = current.next
            return node_info
        my_list = []
        my_list.extend(linked_list_to_list(list1))
        my_list.extend(linked_list_to_list(list2))
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
