#!/usr/bin/python3
"""Unit tests for Square class."""
import os
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_1(self):
        """Test of Square(1) exists"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        """Test of Square(1, 2) exists"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Test of Square(1, 2, 3) exists"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_str_size(self):
        """Test of Square("1") exists"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_str_x(self):
        """Test of Square(1, "2") exists"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_str_y(self):
        """Test of Square(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        """Test of Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_negative_size(self):
        """Test of Square(-1) exists"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_negative_x(self):
        """Test of Square(1, -2) exists"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_negative_y(self):
        """Test of Square(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero_size(self):
        """Test of Square(0) exists"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test of __str__() for Square exists"""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        """Test of to_dictionary() in Square exists"""
        s = Square(10, 1, 9, 1)
        expected = {'id': 1, 'size': 10, 'x': 1, 'y': 9}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_empty(self):
        """Test of update() in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(s.id, 10)

    def test_update_arg_89(self):
        """Test of update(89) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_arg_89_1(self):
        """Test of update(89, 1) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_arg_89_1_2(self):
        """Test of update(89, 1, 2) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_arg_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kw_id(self):
        """Test of update(**{ 'id': 89 }) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kw_id_s(self):
        """Test of update(**{ 'id': 89, 'size': 1 }) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kw_id_s_x(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kw_id_s_x_y(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists"""
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_s(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square exists"""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_s_x(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_s_x_y(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid(self):
        """Test of Square.save_to_file([Square(1)]) in Square exists"""
        Square.save_to_file([Square(1, 0, 0, 1)])
        with open("Square.json", "r") as f:
            self.assertIn('"id": 1', f.read())

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn't exist exists"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        """Test of Square.load_from_file() when file exists exists"""
        Square.save_to_file([Square(1, 0, 0, 1)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)


if __name__ == "__main__":
    unittest.main()
