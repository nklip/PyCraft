# LeetCode 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# Task: From the sorted list letters, choose the earliest letter alphabetically
# that comes strictly after target. If none qualifies, wrap to letters[0].
class Solution:
    # Time Complexity: O(log n), halving the search interval at each step.
    # Space Complexity: O(1), storing indices and the current answer.
    # n = len(letters).
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left_index = 0
        right_index = len(letters) - 1

        answer = letters[left_index]

        while (left_index <= right_index):
            mid_index = right_index - (right_index - left_index) // 2;

            if letters[mid_index] > target:
                answer = letters[mid_index]
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

        return answer
