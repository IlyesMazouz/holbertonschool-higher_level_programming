#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file"

    Parameters:
        filename (str): The name of the JSON file to load the object from

    Returns:
        object: The object represented by the JSON data in the file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        json_data = json.load(file)

    return json_data
