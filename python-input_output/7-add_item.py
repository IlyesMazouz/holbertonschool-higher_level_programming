#!/usr/bin/python3
"""
 a script that adds all arguments to a Python list,
 and then save them to a file
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    """Load existing data from the file or
      create an empty list if the file doesn't exist"""
    if path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    """Add all arguments to the list
    """
    my_list.extend(sys.argv[1:])

    """ Save the updated list to the file
    """
    save_to_json_file(my_list, "add_item.json")
