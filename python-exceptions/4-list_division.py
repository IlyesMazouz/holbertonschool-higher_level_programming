#!/usr/bin/python3
"""
a function that divides element by element between two lists

"""


def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element between two lists

    Args:
        my_list_1 (list): The first list
        my_list_2 (list): The second list
        list_length (int): The desired length of the new list

    Returns:
        list: A new list of length list_length containing the division results

    """
    result_list = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            result = dividend / divisor
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError as e:
            print(str(e))
            result = 0
        finally:
            result_list.append(result)

    return result_list
