#!/usr/bin/python3
"""
Unit tests for models/base.py
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for the Base class."""

    def setUp(self):
        """Reset private class attribute before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_load_from_file_no_file(self):
        """Test load_from_file when the JSON file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Test loading Rectangle instances from file."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))

    def test_load_from_file_square(self):
        """Test loading Square instances from file."""
        s1 = Square(5, 1, 3, 1)
        s2 = Square(9, 0, 0, 2)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(s1))
        self.assertEqual(str(loaded[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
