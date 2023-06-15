#!/usr/bin/python3

"""
a function that raises a name exception with a message

"""


def raise_exception_msg(message=""):
    """
    Raises a name exception (NameError) with a custom message

    Args:
        message (str): The message to be included in the exception
    """
    raise NameError(message)
