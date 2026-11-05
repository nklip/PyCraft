# LeetCode 168: Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/description/
# Task: Convert a positive, one-based column number to its Excel letter title.
# For example, 1 maps to A, 26 to Z, and 27 to AA.
class Solution:
    # Time Complexity: O(d^2) worst case, from repeated string concatenation.
    # Space Complexity: O(d), for the growing title and its reversed result.
    # d = number of letters in the result, O(log(columnNumber + 1)).
    # Assumes constant-time integer arithmetic; concatenation may copy prefixes.
    def convertToTitle(self, columnNumber: int) -> str:
        column_row_id = columnNumber
        title = ''
        while column_row_id > 0:
            column_row_id -= 1

            ch = chr(ord('A') + column_row_id % 26)

            title += ch

            column_row_id = column_row_id // 26

        # reverse a string
        return title[::-1]
