#!/usr/bin/python3
"""
a function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation

    Parameters:
        my_obj: The object to be saved to the file
        filename (str): The name of the file to write the JSON representation

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
