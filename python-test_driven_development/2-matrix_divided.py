#!/usr/bin/python3
"""
a function that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor

    Args:
        matrix (list of lists): A matrix represented as a list of lists containing integers or floats
        div (int or float): The divisor, which must be a non-zero number

    Returns:
        list of lists: A new matrix containing the result of the division operation

    Raises:
        TypeError: If the input `matrix` is not a valid matrix (list of lists of integers/floats)
                   or if the input `div` is not a number (integer or float)
        ZeroDivisionError: If the `div` is equal to 0
    """
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
