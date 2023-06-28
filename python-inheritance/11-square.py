#!/usr/bin/python3
"""
The square class
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for performing geometric calculations
    """

    def area(self):
        """
        Calculates the area of the geometry

        Raises:
            Exception: This method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer value

        Args:
            name (str): The name of the value
            value (int): The value to be validated

        Raises:
            TypeError: If the provided value is not an integer
            ValueError: If the provided value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle is a class for representing rectangles

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle

        Returns:
            str: The string representation of the Rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Square is a subclass of Rectangle that represents squares

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """
        Initializes a Square object

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
