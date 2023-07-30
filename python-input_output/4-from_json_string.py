#!/usr/bin/python3
"""
a function that returns an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Parameters:
        my_str (str): The JSON string to be converted to a Python data structure

    Returns:
        object: The Python data structure represented by the JSON string
    """
    python_data = json.loads(my_str)

    return python_data
