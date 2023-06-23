#!/usr/bin/python3


def lookup(obj):
    """returns a list of available attributes and methods of an object

    Args:
        obj (object): The object to look up

    returns:
        list: A list of available attributes and methods
    """
    return dir(obj)
