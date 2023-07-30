#!/usr/bin/python3

"""
a script that adds all arguments to a Python list, and then save them to a file
"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

with open(file_name, 'a') as file:
    """
    If the file is not empty, load its content and append the new content to it
    """
    if (os.path.getsize(file_name) != 0):
        items = load_from_json_file(file_name)
        items += sys.argv[1:]
        save_to_json_file(items, file_name)
    """
    If the file is empty, just append the new content
    """
    else:
        items = []
        items += sys.argv[1:]
        save_to_json_file(items, file_name)
