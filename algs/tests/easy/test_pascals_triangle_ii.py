import unittest

from algs.easy.pascals_triangle_ii import Solution


class TestPascalsTriangleII(unittest.TestCase):
    def test_row_index_three(self):
        self.assertEqual(Solution().getRow(3), [1, 3, 3, 1])

    def test_row_index_zero(self):
        self.assertEqual(Solution().getRow(0), [1])

    def test_row_index_one(self):
        self.assertEqual(Solution().getRow(1), [1, 1])


if __name__ == "__main__":
    unittest.main()
