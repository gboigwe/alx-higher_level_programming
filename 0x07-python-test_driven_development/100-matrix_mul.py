#!/usr/bin/python3
"""

Module composed by a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for element_item in m_a:
        if not isinstance(element_item, list):
            raise TypeError("m_a must be a list of lists")

    for element_item in m_b:
        if not isinstance(element_item, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for list_type in m_a:
        for element_item in list_type:
            if not type(element_item) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for list_type in m_b:
        for element_item in list_type:
            if not type(element_item) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    len_size = 0

    for element_item in m_a:
        if len_size != 0 and len_size != len(element_item):
            raise TypeError("each row of m_a must be of the same size")
        len_size = len(element_item)

    len_size = 0

    for element_item in m_b:
        if len_size != 0 and len_size != len(element_item):
            raise TypeError("each row of m_b must be of the same size")
        len_size = len(element_item)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    results_1 = []
    index_item_1 = 0

    for a in m_a:
        results_2 = []
        index_item_2 = 0
        num = 0
        while (index_item_2 < len(m_b[0])):
            num += a[index_item_1] * m_b[index_item_1][index_item_2]
            if index_item_1 == len(m_b) - 1:
                index_item_1 = 0
                index_item_2 += 1
                results_2.append(num)
                num = 0
            else:
                index_item_1 += 1
        results_1.append(results_2)

    return results_1
