#!/usr/bin/python3
"""
a function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Parameters:
        my_obj: The object to be converted to JSON

    Returns:
        str: The JSON representation of the object as a string
    """
    json_string = json.dumps(my_obj)

    return json_string
