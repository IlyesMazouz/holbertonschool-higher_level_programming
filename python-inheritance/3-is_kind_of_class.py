#!/usr/bin/python3
"""
 function that returns True if the object is an instance of,
 or if the object is an instance of a class that inherited from,
 the specified class otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of,
    or inherited from, the specified class

    Args:
        obj (object): The object to check
        a_class (class): The class to compare against

    Returns:
        bool: True if the object is an instance of or inherited from the class,
         False otherwise
    """
    return isinstance(obj, a_class)
