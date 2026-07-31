#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.53, 6.33, -1.2, 4.2]), 6.33)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1.5, 3, 5, 2.2]), 5)

    def test_string(self):
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -20, -3, -50]), -3)


if __name__ == '__main__':
    unittest.main()
