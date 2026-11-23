# LeetCode 13: Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/
# Task: Convert a valid Roman numeral s representing a value from 1 to 3999
# into an integer. Match prefixes for thousands, hundreds, tens, and units;
# the tables include subtractive forms such as IV, IX, XL, XC, CD, and CM.
class Solution:
    # Time Complexity: O(n), due to up to four suffix copies; prefix checks
    # use a fixed number of patterns whose lengths are bounded by four.
    # Space Complexity: O(n), for temporary suffix strings; tables use O(1).
    # n = len(s); under the task's n <= 15 limit, both costs are bounded by O(1).
    def romanToInt(self, s: str) -> int:
        thousands = ["", "M", "MM", "MMM", "MMMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        if s == "":
            return 0

        number = 0

        for i in range(len(thousands) - 1, -1, -1):
            if s.startswith(thousands[i]):
                number += i * 1000

                s = s[len(thousands[i]):]

                break

        for i in range(len(hundreds) - 1, -1, -1):
            if s.startswith(hundreds[i]):
                number += i * 100

                s = s[len(hundreds[i]):]

                break

        for i in range(len(tens) - 1, -1, -1):
            if s.startswith(tens[i]):
                number += i * 10

                s = s[len(tens[i]):]

                break

        for i in range(len(units) - 1, -1, -1):
            if s.startswith(units[i]):
                number += i

                s = s[len(units[i]):]

                break

        return number
