#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    safely prints x elements from my_list

    Args:
        my_list (list): The list containing elements to print
        x (int): The number of elements to print

    Returns:
        int: The actual number of elements printed
    """
    printed_count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
    except IndexError:
        pass

    print()
    return printed_count
