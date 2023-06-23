#!/usr/bin/python3
"""
checks if the object is an instance of
a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against

    Returns:
        bool: True if the object is an instance of
        a class that inherited from the specified class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
