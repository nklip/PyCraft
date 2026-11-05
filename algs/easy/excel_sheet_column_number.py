# LeetCode 171: Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/description/
# Task: Convert an uppercase Excel column title to its one-based column number.
# The sequence starts A = 1, Z = 26, AA = 27, and continues with more letters.
class Solution:
    # Time Complexity: O(m), processing each letter once with base-26 arithmetic.
    # Space Complexity: O(1), keeping only the running total and current letter.
    # m = len(columnTitle); assumes constant-time, fixed-size integer arithmetic.
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for ch in columnTitle:
            # is the amount of chars in alphabet
            result *= 26

            # ASCII / Unicode values
            # ord() - returns a character's Unicode point
            # so 'A' maps to 1, 'B' maps to 2, 'Z' maps to 26
            number = ord(ch) - ord('A') + 1

            result += number

        return result
