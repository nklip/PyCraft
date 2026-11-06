# LeetCode 225: Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/
# Task: Provide a LIFO stack using two queues, supporting push, pop, top, and
# empty. The most recently pushed value must be the first returned by pop/top.
# This implementation represents both queues with Python lists.
class MyStack:
    # Space Complexity: O(n) total across both lists; n = current stack size.

    primary = None
    secondary = None

    # Time Complexity: O(1), initializing two empty lists.
    def __init__(self):
        self.primary = []
        self.secondary = []

    # Time Complexity: O(n^2), moving n entries with repeated list.pop(0) calls;
    # each front removal shifts all remaining entries in the primary list.
    def push(self, x: int) -> None:
        # secondary is always empty when we add 1,2,3
        self.secondary.append(x)
        # add 1: primary is empty for 1, nothing happens
        # add 2: primary is not empty, contains 1
        # so we add 1 to 2
        # result: secondary is 2,1
        # add 3: primary is not empty, contains 2,1
        # so we add 2,1, to 3
        # result: secondary 3,2,1
        while self.empty() == False:
            self.secondary.append(self.primary.pop(0))
        # we clean secondary
        temp = self.primary
        self.primary = self.secondary
        self.secondary = temp

    # Time Complexity: O(n), shifting the remaining entries after front removal.
    def pop(self) -> int:
        return self.primary.pop(0)

    # Time Complexity: O(1), reading the first entry directly.
    def top(self) -> int:
        return self.primary[0]

    # Time Complexity: O(1), checking the stored list length.
    def empty(self) -> bool:
        return True if len(self.primary) == 0 else False
