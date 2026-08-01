#!/usr/bin/python3
"""
Unit tests for models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def setUp(self):
        """Reset private class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """Test conversion of Rectangle to dictionary."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        expected = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), expected)
        self.assertIsInstance(r1.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
