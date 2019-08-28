import unittest
import math
import calculator.pycalc
from math import (
    e,
    pi,
    cos,
    sin,
    log
)


class ErrorTest(unittest.TestCase):
    """Check Error tests"""

    def test_check_error_null(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('')
        self.assertEqual(result, "ERROR: no input data")

    def test_check_brackets_balance(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('15*(25+1')
        self.assertEqual(result, "ERROR: brackets aren't balanced")

    def test_check_function_name(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('func')
        self.assertEqual(result, 'ERROR: unknown function namefunc')

    def test_check_error_first_sign(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('%1863')
        self.assertEqual(result, "ERROR: expression starts with operator")

    def test_check_error_first_sign_2(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('\\1142')
        self.assertEqual(result, "ERROR: expression starts with operator")

    def test_check_error_in_param(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('log(10,0,8)')
        self.assertEqual(result, "ERROR: too many arguments in function")

    def test_check_error_not_param(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('hypot()')
        self.assertEqual(result, "ERROR: too little arguments in function with 2 arguments")


class FunctionsTest(unittest.TestCase):
    """Check function work"""

    def test_sin(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('sin(pi/2)')
        self.assertEqual(result, eval('sin(pi/2)'))

    def test_acos(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('acos(0.84)')
        self.assertEqual(result, eval('math.acos(0.84)'))

    def test_acosh(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('acosh(1)')
        self.assertEqual(result, eval('math.acosh(1)'))

    def test_asin(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('asin(0.99)')
        self.assertEqual(result, eval('math.asin(0.99)'))

    def test_asinh(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('asinh(0.86)')
        self.assertEqual(result, eval('math.asinh(0.86)'))

    def test_atan(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('atan(0.24)')
        self.assertEqual(result, eval('math.atan(0.24)'))

    def test_fsum_one_argument(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('fsum([88])')
        self.assertEqual(result, eval('math.fsum([88])'))

    def test_fsum_two_argument(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('fsum([6,3])')
        self.assertEqual(result, eval('math.fsum([6,3])'))

    def test_fsum_more_argument(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('fsum([5,3,5])')
        self.assertEqual(result, eval('math.fsum([5,3,5])'))

    def test_log_2param(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('log(6,7)')
        self.assertEqual(result, eval('log(6,7)'))

    def test_gcd_2param(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('gcd(11,36)')
        self.assertEqual(result, eval('math.gcd(11,36)'))

    def test_ceil(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('ceil(5)')
        self.assertEqual(result, eval('math.ceil(5)'))

    def test_degrees(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('degrees(8)')
        self.assertEqual(result, eval('math.degrees(8)'))


class CalculateTest(unittest.TestCase):
    """Check calculating"""

    def test_normal(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('-13')
        self.assertEqual(result, eval('-13'))

    def test_calc(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('2+2*2')
        self.assertEqual(result, eval('2+2*2'))

    def test_bracket_and_minus(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('6-(-13)')
        self.assertEqual(result, eval('6-(-13)'))

    def test_many_minuses(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('1---1')
        self.assertEqual(result, eval('1---1'))

    def test_many_minuses_2(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('-+---+-1')
        self.assertEqual(result, eval('-+---+-1'))

    def test_negative_number(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('8+(-9*6-5)')
        self.assertEqual(result, eval('8+(-9*6-5)'))

    def test_del_space(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('4*9 -16')
        self.assertEqual(result, eval('4*9 -16'))

    def test_log_1param(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('log(1+9)')
        self.assertEqual(result, eval('log(1+9)'))

    def test_degree_function(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('7^sin(5)')
        self.assertEqual(result, eval('7**sin(5)'))

    def test_degree_negative_number(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('6^-1')
        self.assertEqual(result, eval('6**(-1)'))

    def test_negative_numbers(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('--+-48')
        self.assertEqual(result, eval('--+-48'))

    def test_negative_numbers_multiplication(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('4*-8')
        self.assertEqual(result, eval('4*-8'))

    def test_float_numbers(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('8.1-9.8')
        self.assertEqual(result, eval('8.1-9.8'))

    def test_compare_function_equal(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('6==5')
        self.assertEqual(result, eval('6==5'))

    def test_compare_function_not_equal(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('8!=1')
        self.assertTrue(result)

    def test_complex_expression(self):
        result = calculator.pycalc.calculate_reversed_polish_notation('sin(e^log(e^e^sin(2.0),45.0) + '
                                                                      'cos(3.0+log10(e^-e)))')
        self.assertEqual(result, eval('sin(e**log(e**e**sin(2.0),45.0) + cos(3.0+math.log10(e**-e)))'))


if __name__ == '__main__':
    unittest.main()
