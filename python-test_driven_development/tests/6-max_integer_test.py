#!/usr/bin/python3
"""
unittests for the function def max_integer(list=[])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 2, -4]), 2)
        self.assertEqual(max_integer([10, -15, 20, -25]), 20)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([3, 3, 3, 0]), 3)

    def test_list_with_strings(self):
        self.assertEqual(max_integer(['apple', 'banana', 'orange']), 'orange')

if __name__ == '__main__':
    unittest.main()
