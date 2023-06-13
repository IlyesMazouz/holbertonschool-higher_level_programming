#!/usr/bin/python3
"""
this module defines a class that represents a square
"""

class Square:
    """
    this class represents a square
    """

    def __init__(self, size=0):
        """
        initializes a Square instance

        args:
            size (int): the size of the square. Defaults to 0

        Raises:
            typeError: if the size is not an integer
            valueError: if the size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
