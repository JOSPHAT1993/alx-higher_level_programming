#!/usr/bin/python3
"""2-matrix_divided

   matrix_divided function
"""


def matrix_divided(matrix, div):
    """matrix divided function
    Args:
       matrix: (list of list) of numbers
       div: divisor number
    Raise:
       TypeError: matrix must be a matrix (list of lists) of integers/floats
       TypeError: Each row of the matrix must have the same size
       TypeError: div must be a number
       ZeroDivisionError: division by zero
    Returns:
       new matrix that divides all elements of a matrix
    """
    if (type(matrix) is not list or
            not all(type(x) is list for x in matrix) or
            not all(type(i) in [float, int] for x in matrix for i in x)):
        raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(i / div, 2) for i in x] for x in matrix]

    return result
