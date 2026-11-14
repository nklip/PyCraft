# LeetCode 2848: Points That Intersect With Cars
# https://leetcode.com/problems/points-that-intersect-with-cars/description/
# Task: Each pair in nums gives a car's inclusive start and end coordinates.
# Count the distinct integer positions covered by at least one car, counting
# overlapping positions only once.
class Solution:
    # Time Complexity: O(s) average, inserting every point of every interval.
    # Space Complexity: O(u), for the set of distinct covered positions.
    # s = sum(end - start + 1) over all intervals, u = distinct covered positions.
    # Set operations average O(1); the problem's coordinates bound u to at most 100.
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()

        for interval in nums:
            first = interval[0]
            last = interval[-1]

            for i in range(first, last + 1):
                points.add(i)

        return len(points)
