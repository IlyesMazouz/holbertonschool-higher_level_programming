#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    filename (str): The name of the file to read.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
