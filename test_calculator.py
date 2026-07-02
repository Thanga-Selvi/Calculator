#!/usr/bin/env python3

import unittest
import math
from calculator import add, subtract, multiply, divide, power, modulo, square_root, factorial

class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-10, -5), -15)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(10, -5), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    # Subtraction tests
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(20, 8), 12)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-10, -5), -5)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(10, -5), 15)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)

    # Multiplication tests
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(3, -4), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    # Division tests
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(15, 3), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-15, -3), 5)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(15, -3), -5)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    # Power tests
    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_power_float_base(self):
        self.assertAlmostEqual(power(2.5, 2), 6.25)

    def test_power_one(self):
        self.assertEqual(power(10, 1), 10)

    # Modulo tests
    def test_modulo_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_negative_dividend(self):
        self.assertEqual(modulo(-10, 3), 2)

    def test_modulo_negative_divisor(self):
        self.assertEqual(modulo(10, -3), -2)

    def test_modulo_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_modulo_floats(self):
        self.assertAlmostEqual(modulo(7.5, 2.5), 0.0)

    # Square root tests
    def test_square_root_perfect_square(self):
        self.assertEqual(square_root(16), 4)

    def test_square_root_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_non_perfect_square(self):
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

    def test_square_root_negative_raises_error(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_square_root_float(self):
        self.assertAlmostEqual(square_root(6.25), 2.5)

    # Factorial tests
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive_integer(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_float_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(5.5)

if __name__ == '__main__':
    unittest.main()
