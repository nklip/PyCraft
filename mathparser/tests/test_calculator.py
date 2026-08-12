"""
Created on 02.08.2011

@author: Nikita Lipatov
"""
import unittest

from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_plus(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("2 + 3"), 5.0)
        pass

    def test_minus(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("2-3"), -1.0)
        pass

    def test_multiple_pluses(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("2+2+2"), 6.0)
        pass

    def test_multiple_minuses(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("12-22-50"), -60.0)
        pass

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("12*2"), 24.0)
        pass

    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("12/2"), 6.0)
        pass

    def test_multiple_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("12*2*10"), 240.0)
        pass

    def test_multiple_division(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("12/2/3"), 2.0)
        pass

    def test_brackets(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("(2 + 2) * 2"), 8.0)
        pass

    def test_degree(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("(4 - 2)^4"), 16.0)
        pass

    def test_modulus_with_zero(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("6%3"), 0.0)
        pass

    def test_division_by_zero(self):
        calc = Calculator()
        self.assertRaises(BaseException, calc.calculate, "6/0")
        pass

    def test_modules_by_zero(self):
        calc = Calculator()
        self.assertRaises(BaseException, calc.calculate, "6%0")
        pass

    def test_brackets_unbalance(self):
        calc = Calculator()
        self.assertRaises(BaseException, calc.calculate, "(2 + 2 * 2")
        pass

    def test_function_abs(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("abs(-5)"), 5.0)
        pass

    def test_function_log10(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("log10(100)"), 2.0)
        pass

    def test_function_sqrt(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("sqrt(144)"), 12.0)
        pass

    def test_function_acos(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("ceil(acos(6.0))"), 2.0)
        pass

    def test_function_asin(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("asin(0)"), 0.0)
        pass

    def test_function_atan(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("atan(0)"), 0.0)
        pass

    def test_function_cos(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("cos(0)"), 1.0)
        pass

    def test_function_sin(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("sin(0)"), 0.0)
        pass

    def test_function_tan(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("tan(0)"), 0.0)
        pass

    def test_function_ceil(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("ceil(0.5)"), 1.0)
        pass

    def test_function_floor(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("floor(0.5)"), 0.0)
        pass

    def test_function_sinInCeil(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("ceil(sin(0.5))"), 1.0)
        pass

    def test_function_degreeInCos(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("cos(180))"), -1.0)
        pass

    def test_function_degreeInSin(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("floor(sin(180)))"), 0.0)
        pass

    def test_function_pow(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("pow(2, 10)"), 1024.0)
        pass

    def test_function_log(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("log(2, 1024)"), 10.0)
        pass

    def test_function_min(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("min(2, 3,4,5,6)"), 2.0)
        pass

    def test_function_max(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("max(2, 3,4,5,6)"), 6.0)
        pass

    def test_function_sum(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("sum(1, 2,3,4,5,6,7,8,9,10)"), 55.0)
        pass

    def test_function_avg(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("avg(2,4,6,8,10,12,14,16,18,20, 22)"), 12.0)
        pass

    def test_function_variables(self):
        calc = Calculator()
        self.assertEqual(calc.calculate("key1=2+2*2"), 6.0)
        self.assertEqual(calc.calculate("key2=3+3*3"), 12.0)
        self.assertEqual(calc.calculate("key3=key1+key2"), 18.0)
        self.assertEqual(calc.calculate("key3 + max(key1, key2)"), 30.0)
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPlusMinus']
    unittest.main()
