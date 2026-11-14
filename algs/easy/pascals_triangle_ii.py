# LeetCode 119: Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/description/
# Task: Return rowIndex's row of Pascal's triangle using zero-based indexing,
# so row 0 is [1]. Each row starts and ends with 1, and each interior entry
# adds the two neighboring entries from the previous row.
class Solution:
    # Time Complexity: O(r^2), building all rows up to the requested row.
    # Space Complexity: O(r^2), because recursive frames retain earlier row lists;
    # the returned row itself and the call stack each use O(r) space.
    # r = rowIndex + 1; arithmetic is O(1) under the problem's bounded row index.
    def getRow(self, rowIndex: int) -> list[int]:
        row1 = [1]
        if rowIndex == 0:
            return row1

        row2 = [1,1]
        if rowIndex == 1:
            return row2
        return self.pascalsTriangle(rowIndex, 2, row2)

    def pascalsTriangle(self, numRows: int, rows: int, previousRow: list[int]) -> list[int]:
        row = [1]
        for i in range(rows - 1):
            sum = previousRow[i] + previousRow[i + 1]
            row.append(sum)
        row.append(1)
        if numRows > rows:
            return self.pascalsTriangle(numRows, rows + 1, row)
        else:
            return row
