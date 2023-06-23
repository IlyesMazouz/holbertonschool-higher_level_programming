#!/usr/bin/python3
"""
base geometry
"""


class BaseGeometry:
    """A class representing base geometry"""

    def area(self):
        """Raises an exception indicating that
        the area method is not implemented"""
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with the given width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Validates that the given value is a positive integer"""
        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be an integer greater than0".format(name))

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)