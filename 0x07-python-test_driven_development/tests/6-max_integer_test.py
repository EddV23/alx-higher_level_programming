#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test a list with a max value at the beginning
        self.assertEqual(max_integer([4, 2, -1, -3]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list of one negative integer
        self.assertEqual(max_integer([-5]), -5)

        # Test with a list of repeated integers
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test with a list of floats
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 4.8]), 4.8)

        # Test with a list containing both integers and floats
        self.assertEqual(max_integer([1, 2.5, 3, 4]), 4)

        # Test with a large list of integers
        self.assertEqual(max_integer(list(range(10**6))), 999999)

if __name__ == "__main__":
    unittest.main()
