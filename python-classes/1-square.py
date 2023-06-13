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
        initializes a square instance

        args:
            size (int):the size of the square

        attributes:
            __size (int):private instance attribute representing size of square
        """
        self.__size = size
