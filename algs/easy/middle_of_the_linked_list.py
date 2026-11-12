from algs.list_node import ListNode

# LeetCode 876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# Task: Return the middle node of a singly linked list. When its length is even,
# choose the second of the two middle nodes. Return the existing node, retaining
# its links to the rest of the list.
class Solution:
    # Time Complexity: O(n), advancing slow and fast pointers through the list.
    # Space Complexity: O(1), using two pointers without copying any nodes.
    # n = number of nodes in the list.
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        slow_node = head
        fast_node = head

        while True:
            if fast_node.next is None:
                return slow_node
            elif fast_node.next.next is None:
                return slow_node.next

            slow_node = slow_node.next
            fast_node = fast_node.next.next
