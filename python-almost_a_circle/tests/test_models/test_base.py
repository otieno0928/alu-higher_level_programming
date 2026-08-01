#!/usr/bin/python3
"""Unit tests for models/base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{'id': 12}])


if __name__ == "__main__":
    unittest.main()
