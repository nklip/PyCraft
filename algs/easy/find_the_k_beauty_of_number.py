# LeetCode 2269: Find the K-Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
# Task: Count the contiguous k-digit portions of num whose integer values divide
# num evenly. Allow leading zeros, exclude zero divisors, and count matching
# portions at different positions separately.
class Solution:
    # Time Complexity: O(d + (d - k + 1) * k), converting num to text, then
    # slicing and parsing each k-digit window before checking divisibility.
    # Space Complexity: O(d), for the decimal string and current slice of size k.
    # d = number of decimal digits in num, 1 <= k <= d.
    # Assumes constant-time arithmetic for the problem's bounded integers.
    def divisorSubstrings(self, num: int, k: int) -> int:

        num_str = str(num)

        count = 0

        # +1 includes len(num_str) becase range()
        # excludes it's stop value
        for i in range(k, len(num_str) + 1):
            substring = num_str[i-k:i]

            sub_int = int(substring)

            if sub_int != 0 and num % sub_int == 0:
                count += 1

        return count
