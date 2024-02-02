#!/usr/bin/python3
"""
Defines a matrix function
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers/floats
    Returns a new matrix
    """
    newmatrix = []
    length = 0

    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        newrow = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if length is 0:
            length = len(row)
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            newrow.append(round(item / div, 2))
        newmatrix.append(newrow)
    return newmatrix
