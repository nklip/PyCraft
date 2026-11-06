# LeetCode 232: Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/
# Task: Provide a FIFO queue with push to the back, pop/peek at the front, and
# an empty check. LeetCode requires two stacks with only stack operations.
# This implementation uses a single list and removes from its front with pop(0),
# which does not satisfy that restriction; the bounds below describe this code.
class MyQueue:
    # Space Complexity: O(n) total, for the backing list; n = current queue size.

    queue = None

    # Time Complexity: O(1), initializing an empty list.
    def __init__(self):
        self.queue = []

    # Time Complexity: O(1) amortized; O(n) worst case when the list resizes.
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Time Complexity: O(n), shifting the remaining entries after front removal.
    def pop(self) -> int:
        return self.queue.pop(0)

    # Time Complexity: O(1), reading the first entry directly.
    def peek(self) -> int:
        return self.queue[0]

    # Time Complexity: O(1), checking the stored list length.
    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
