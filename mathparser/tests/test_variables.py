"""
Created on 02.08.2011

@author: Lipatov
"""
import unittest

from calculator.variables import Variables


class TestVariables(unittest.TestCase):

    def test_variables(self):
        variables = Variables()
        variables.add("key1", 5.0)
        self.assertEqual(variables.get("key1"), 5.0)
        variables.add("key2", 6.0)
        variables.add("key3", 7.0)
        variables.remove("key2")
        self.assertEqual(variables.get("key3"), 7.0)
        self.assertEqual(variables.contains("key4"), False)


if __name__ == "__main__":
    unittest.main()
