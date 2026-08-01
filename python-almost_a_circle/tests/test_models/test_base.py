#!/usr/bin/python3
"""Unit tests for Base class."""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_auto_id(self):
        """Test of Base() for assigning automatically an ID exists"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_auto_id_increment(self):
        """Test of Base() for assigning automatically an ID + 1 of the previous exists"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        """Test of Base(89) saving the ID passed exists"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test of Base.to_json_string(None) exists"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test of Base.to_json_string([]) exists"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        """Test of Base.to_json_string([ { 'id': 12 }]) exists"""
        res = Base.to_json_string([{'id': 12}])
        self.assertEqual(res, '[{"id": 12}]')

    def test_to_json_string_type(self):
        """Test of Base.to_json_string([ { 'id': 12 }]) returning a string exists"""
        res = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        """Test of Base.from_json_string(None) exists"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test of Base.from_json_string("[]") exists"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_dict(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') exists"""
        res = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(res, [{'id': 89}])

    def test_from_json_string_type(self):
        """Test of Base.from_json_string('[{ "id": 89 }]') returning a list exists"""
        res = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(res, list)


if __name__ == "__main__":
    unittest.main()
