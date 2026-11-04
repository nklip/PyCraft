import unittest

from algs.easy.check_if_n_and_its_double_exist import Solution


class TestCheckIfNAndItsDoubleExist(unittest.TestCase):
    def test_number_and_its_double_exist(self):
        self.assertTrue(Solution().checkIfExist([10, 2, 5, 3]))

    def test_no_number_and_its_double_exist(self):
        self.assertFalse(Solution().checkIfExist([3, 1, 7, 11]))


if __name__ == "__main__":
    unittest.main()
