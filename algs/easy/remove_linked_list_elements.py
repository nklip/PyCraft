from algs.list_node import ListNode

# LeetCode 203: Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/
# Task: Remove every node whose value equals val from a singly linked list.
# Reconnect the surviving nodes in their original order and return the resulting
# head, or None if no nodes remain. Existing node links are modified.
class Solution:
    # Time Complexity: O(n), examining each node once and relinking survivors.
    # Space Complexity: O(1), reusing nodes with a constant number of pointers.
    # n = number of nodes in the original list.
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None

        return_node = None
        current = None

        while head is not None:
            temp = head.next

            if head.val != val:
                if return_node is None:
                    return_node = head
                    head.next = None
                    current = return_node
                else:
                    current.next = head
                    head.next = None
                    current = head
            head = temp
        return return_node
