import io
import unittest
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class
    """

    def setUp(self):
        """
        Set up a Rectangle instance before each test method
        """
        self.rect = Rectangle(4, 5, 1, 2, 10)

    def test_attributes(self):
        """
        Test the attributes of the Rectangle instance
        """
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 2)
        self.assertEqual(self.rect.id, 10)

    def test_area(self):
        """
        Test the area() method of the Rectangle instance
        """
        self.assertEqual(self.rect.area(), 20)

    def test_str(self):
        """
        Test the __str__() method of the Rectangle instance
        """
        expected = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(self.rect), expected)

    def test_display(self):
        """
        Test the display() method of the Rectangle instance
        """
        expected_output = "\n\n ####\n ####\n ####\n ####\n ####\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rect.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_update_args(self):
        """
        Test the update() method of the Rectangle instance with *args
        """
        self.rect.update(20, 6, 7, 3, 4)
        self.assertEqual(self.rect.id, 20)
        self.assertEqual(self.rect.width, 6)
        self.assertEqual(self.rect.height, 7)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)

    def test_update_kwargs(self):
        """
        Test the update() method of the Rectangle instance with **kwargs
        """
        self.rect.update(width=8, height=9, x=5, y=6)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 9)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 6)


if __name__ == '__main__':
    unittest.main()
