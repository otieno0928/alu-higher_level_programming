#!/usr/bin/python3
"""
Unit tests for models/square.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for the Square class."""

    def setUp(self):
        """Reset private class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        """Test conversion of Square to dictionary."""
        s1 = Square(10, 2, 1, 1)
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected)
        self.assertIsInstance(s1.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
