#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written

    Parameters:
        filename (str): The name of the file to write the text into. (Optional)
        text (str): The string to be written into the file (Optional)

    Returns:
        int: The number of characters written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters_written = file.write(text)

    return num_characters_written
