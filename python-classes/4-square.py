#!/usr/bin/python3
"""
this module defines a class that represents a square
"""


class Square:
    """
    represents a square

    attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square. Defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """
        int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        args:
            value (int): The size value to set

        raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
