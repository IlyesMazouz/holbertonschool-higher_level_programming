#!/usr/bin/python3
"""
this module defines a class that represents a square
"""


class Square:
    """
    Represents a square

    Attributes:
        size (int): The size of the square
        position (tuple): The position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square. Defaults to 0
            position (tuple): The position of the square. Defaults to (0, 0)
        """
        self.size = size
        self.position = position

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

        Args:
            value (int): The size value to set

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): The position value to set

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers
            ValueError: If the value does not meet the position requirements
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'

        If size is equal to 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
