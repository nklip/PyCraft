# LeetCode 118: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/
# Task: Return the first numRows rows of Pascal's triangle, starting with [1].
# Each row has 1 at both ends; each interior entry adds the two neighboring
# entries from the preceding row.
class Solution:
    # Time Complexity: O(r^2), computing every entry in the first r rows.
    # Space Complexity: O(r^2) including the output rows; O(r) auxiliary call stack.
    # r = numRows; arithmetic is O(1) under the problem's bounded row count.
    def generate(self, numRows: int) -> list[list[int]]:
        return_list = []
        row1 = [1]
        return_list.append(row1)

        if numRows == 1:
            return return_list

        row2 = [1,1]
        return_list.append(row2)

        if numRows == 2:
            return return_list

        self.pascalsTriangle(numRows, 3, return_list)

        return return_list

    def pascalsTriangle(self, numRows: int, rows: int, returnList: list[list[int]]) -> list[list[int]]:
        previous_row = returnList[rows-2]
        row = [1]
        for i in range(1, rows - 1):
            sum = previous_row[i-1] + previous_row[i]
            row.append(sum)
        row.append(1)
        returnList.append(row)

        if numRows > rows:
            self.pascalsTriangle(numRows, rows + 1, returnList)
