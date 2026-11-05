import unittest

from algs.easy.excel_sheet_column_number import Solution


class TestExcelSheetColumnNumber(unittest.TestCase):
    def test_column_a(self):
        self.assertEqual(Solution().titleToNumber("A"), 1)

    def test_column_ab(self):
        self.assertEqual(Solution().titleToNumber("AB"), 28)

    def test_column_zy(self):
        self.assertEqual(Solution().titleToNumber("ZY"), 701)


if __name__ == "__main__":
    unittest.main()
