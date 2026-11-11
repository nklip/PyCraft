from algs.list_node import ListNode

# LeetCode 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# Task: Determine whether following next links from head can revisit the same
# node. Return True for a cycle and False when the list ends, including an empty
# list. Equal values in different nodes do not form a cycle.
class Solution:
    # Time Complexity: O(n), detecting a cycle and then locating its entry.
    # Space Complexity: O(1), using slow and fast pointers without a visited set.
    # n = number of distinct nodes reachable from head.
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pos = -1
        has_cycle = False
        if head is None:
            return has_cycle

        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                has_cycle = True

                pos = 0

                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    pos += 1

                break
        return has_cycle

