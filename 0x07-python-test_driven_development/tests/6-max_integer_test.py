#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_len(self):
        self.assertEqual(max_integer(), None)

    def test_value_number(self):
        self.assertEqual(max_integer([1000, -3, 63, 2]), 1000)
        self.assertEqual(max_integer([-1, 0, -4, -10]), 0)

    def test_value_string(self):
        self.assertEqual(max_integer(["betty", "Holberton"]), "betty")

    def test_value_float(self):
        self.assertEqual(max_integer([0.1, -3.4, -67]), 0.1)


if __name__ == '__main__':
    unittest.main()
