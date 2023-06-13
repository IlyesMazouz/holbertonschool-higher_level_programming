#!/usr/bin/python3
"""
this module defines a class that represents a square
"""


class Square:
    """
    this class represents a square
    """

    def __init__(self, size):
        """
        initializes a Square instance

        args:
            size (int): The size of the square

        attributes:
            __size (int): The private instance attribute representing the size of the square
        """
        self.__size = size
