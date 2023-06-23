#!/usr/bin/python3
"""
a function that eturns list of available attributes and methods of an object
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object

    Args:
        obj (object): The object to look up

    returns:
        list: A list of available attributes and methods
    """
    return dir(obj)
