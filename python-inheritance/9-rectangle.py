#!/usr/bin/python3
"""Defines a class BaseGeometry and a class Rectangle that inherits from it"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Calculate the area of the geometry object

        Raises:
            Exception: If the area method is not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer

        Args:
            name (str): The name of the value
            value (int): The value to be validated

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
