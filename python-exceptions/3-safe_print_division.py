#!/usr/bin/python3

"""
a function that divides two integers and prints the result

Prototype: def safe_print_division(a, b)

Args:
    a (int): The dividend
    b (int): The divisor

Returns:
    float or None: The result of the division if successful, None otherwise
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result

    Args:
        a (int): The dividend
        b (int): The divisor

    Returns:
        float or None: The result of the division if successful, None otherwise
    """

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
