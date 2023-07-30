#!/usr/bin/python3

"""
a function that returns the dictionary description with simple data structure
 (list, dictionary, string, integer and boolean)
   for JSON serialization of an object:"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean)
      for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary description of the
          object suitable for JSON serialization.
    """
    return obj.__dict__
