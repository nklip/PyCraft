import unittest

from algs.easy.pascals_triangle import Solution


class TestPascalsTriangle(unittest.TestCase):
    def test_five_rows(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]

        self.assertEqual(Solution().generate(5), expected)

    def test_one_row(self):
        self.assertEqual(Solution().generate(1), [[1]])


if __name__ == "__main__":
    unittest.main()
