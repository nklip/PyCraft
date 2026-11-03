import unittest

from algs.easy.binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def test_target_exists(self):
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_target_does_not_exist(self):
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
