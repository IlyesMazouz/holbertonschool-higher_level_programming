#!/usr/bin/python3
"""
afunction that prints the first x elements of a list, considering only integers
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x integers in my_list

    Args:
        my_list (list): The list containing elements to print
        x (int): The number of integers to print

    Returns:
        int: The real number of integers printed
    """

    printed_count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_count += 1
    except IndexError:
        pass

    print()
    return printed_count
