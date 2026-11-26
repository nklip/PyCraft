import unittest

from algs.easy.search_insert_position import Solution


class TestSearchInsertPosition(unittest.TestCase):
    def test_existing_target(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 5), 2)

    def test_insert_between_elements(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 2), 1)

    def test_insert_after_last_element(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 7), 4)


if __name__ == "__main__":
    unittest.main()
