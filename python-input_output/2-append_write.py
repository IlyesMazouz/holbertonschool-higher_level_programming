#!/usr/bin/python3
"""
a function that appends a string at the end of a text file (UTF8
 and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
      and returns the number of characters added

    Parameters:
        filename (str): The name of the file to append the text into
        text (str): The string to be appended to the file

    Returns:
        int: The number of characters added to the file
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        num_characters_added = file.write(text)

    return num_characters_added
