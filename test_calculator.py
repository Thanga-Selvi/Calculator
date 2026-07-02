#!/usr/bin/env python3

import unittest
from calculator import add, subtract, multiply, divide

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

if __name__ == '__main__':
    unittest.main()
