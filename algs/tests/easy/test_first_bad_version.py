import unittest

from algs.easy.first_bad_version import Solution


class TestFirstBadVersion(unittest.TestCase):
    def test_first_bad_version_is_four(self):
        self.assertEqual(Solution(4).firstBadVersion(5), 4)

    def test_only_version_is_bad(self):
        self.assertEqual(Solution(1).firstBadVersion(1), 1)


if __name__ == "__main__":
    unittest.main()
