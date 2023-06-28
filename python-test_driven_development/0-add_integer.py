#!/usr/bin/python3
"""
adds two integers
"""


def add_integer(a, b=98):
    """

    Args:
        a (int or float): The first integer or float
        b (int or float): The second integer or float. Default is 98

    Raises:
        TypeError: If a or b is not an integer or float

    Returns:
        int: The addition of a and b as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
