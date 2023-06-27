#!/usr/bin/python3
"""
unittest for rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class
    """

    def test_init_with_id(self):
        """
        Test the initialization of Rectangle with an explicit id
        """
        r = Rectangle(2, 4, 1, 1, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_init_without_id(self):
        """
        Test the initialization of Rectangle without an explicit id
        """
        Rectangle._Base__nb_objects = 0  # Reset the nb_objects count
        r1 = Rectangle(3, 5, 2, 2)
        r2 = Rectangle(4, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)


if __name__ == "__main__":
    unittest.main()
