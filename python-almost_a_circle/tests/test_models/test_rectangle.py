#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_1_2(self):
        """Test of Rectangle(1, 2) exists"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        """Test of Rectangle(1, 2, 3) exists"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        """Test of Rectangle(1, 2, 3, 4) exists"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_1_2_3_4_5(self):
        """Test of Rectangle(1, 2, 3, 4, 5) exists"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_str_width(self):
        """Test of Rectangle("1", 2) exists"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_str_height(self):
        """Test of Rectangle(1, "2") exists"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_str_x(self):
        """Test of Rectangle(1, 2, "3") exists"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_str_y(self):
        """Test of Rectangle(1, 2, 3, "4") exists"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_negative_width(self):
        """Test of Rectangle(-1, 2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        """Test of Rectangle(1, -2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        """Test of Rectangle(0, 2) exists"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        """Test of Rectangle(1, 0) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        """Test of Rectangle(1, 2, -3) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        """Test of Rectangle(1, 2, 3, -4) exists"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test of area() exists"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test of __str__() for Rectangle exists"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        """Test of display() without x and y exists"""
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Test of display() without y exists"""
        r = Rectangle(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), " ##\n ##\n")

    def test_display_all(self):
        """Test of display() exists"""
        r = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test of to_dictionary() in Rectangle exists"""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_update_empty(self):
        """Test of update() in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(r.id, 10)

    def test_update_arg_89(self):
        """Test of update(89) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_arg_89_1(self):
        """Test of update(89, 1) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_arg_89_1_2(self):
        """Test of update(89, 1, 2) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_arg_89_1_2_3(self):
        """Test of update(89, 1, 2, 3) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_arg_89_1_2_3_4(self):
        """Test of update(89, 1, 2, 3, 4) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kw_id(self):
        """Test of update(**{ 'id': 89 }) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kw_id_w(self):
        """Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kw_id_w_h(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kw_id_w_h_x(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kw_id_w_h_x_y(self):
        """Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test of Rectangle.create(**{ 'id': 89 }) in Rectangle exists"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_w(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle exists"""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_w_h(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_w_h_x(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_w_h_x_y(self):
        """Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test of Rectangle.save_to_file(None) in Rectangle exists"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test of Rectangle.save_to_file([]) in Rectangle exists"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_valid(self):
        """Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists"""
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open("Rectangle.json", "r") as f:
            self.assertIn('"id": 1', f.read())

    def test_load_from_file_no_file(self):
        """Test of Rectangle.load_from_file() when file doesn't exist exists"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_file_exists(self):
        """Test of Rectangle.load_from_file() when file exists exists"""
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)


if __name__ == "__main__":
    unittest.main()
