import unittest

from algs.easy.excel_sheet_column_title import Solution


class TestExcelSheetColumnTitle(unittest.TestCase):
    def test_column_1(self):
        self.assertEqual(Solution().convertToTitle(1), "A")

    def test_column_28(self):
        self.assertEqual(Solution().convertToTitle(28), "AB")

    def test_column_701(self):
        self.assertEqual(Solution().convertToTitle(701), "ZY")


if __name__ == "__main__":
    unittest.main()
