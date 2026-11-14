import unittest

from algs.easy.points_that_intersect_with_cars import Solution


class TestPointsThatIntersectWithCars(unittest.TestCase):
    def test_overlapping_ranges_count_each_point_once(self):
        self.assertEqual(Solution().numberOfPoints([[3, 6], [1, 5], [4, 7]]), 7)

    def test_separate_ranges_exclude_gap(self):
        self.assertEqual(Solution().numberOfPoints([[1, 3], [5, 8]]), 7)


if __name__ == "__main__":
    unittest.main()
