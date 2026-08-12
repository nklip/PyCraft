"""
Created on 02.08.2011

@author: Lipatov
"""
import unittest

from calculator.number import Number


class TestNumber(unittest.TestCase):

    def test_number_set_value_get_value(self):
        temp = Number()
        self.assertEqual(0, temp.get_value())
        temp.set_value("5.0")
        self.assertEqual(5.0, temp.get_value())


if __name__ == "__main__":
    unittest.main()
