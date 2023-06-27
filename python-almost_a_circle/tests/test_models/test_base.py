#!/usr/bin/python3

"""
unittest for base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_init_with_id(self):
        """
        Test the initialization of Base with an explicit id
        """
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        """
        Test the initialization of Base without an explicit id
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()
